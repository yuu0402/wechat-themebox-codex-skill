#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from pathlib import PurePosixPath


REQUIRED_ROOT = {"config.json", "cover.png", "icon.png", "weui_color_new.xml"}
FORBIDDEN_PARTS = {
    "__MACOSX",
    ".DS_Store",
    ".git",
    "src",
    "scripts",
    "notes",
    "dist",
    "tmp",
    "node_modules",
    "draft",
    "drafts",
    "old",
    "generated-rough",
}
ICON_HINTS = (
    "icon",
    "tabbar_",
    "pay",
    "wallet",
    "wechatpay",
    "wepay",
    "transfer",
    "hongbao",
    "red_envelope",
    "camera",
    "search",
    "scan",
    "voice",
    "video",
    "favorites",
    "folder",
    "file",
    "gear",
)
SURFACE_HINTS = ("_bg", "background", "cover", "launch", "bubble", "topbar", "tabbar_bg")


def png_info(data: bytes):
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        return None
    if len(data) < 33 or data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    color_type = data[25]
    has_alpha = color_type in (4, 6)
    return width, height, color_type, has_alpha


def is_probable_icon(path: str) -> bool:
    name = PurePosixPath(path).name.lower()
    if any(hint in name for hint in SURFACE_HINTS):
        return False
    return any(hint in name for hint in ICON_HINTS) or "@2x" in name or "@3x" in name


def normalized_entries(zf: zipfile.ZipFile):
    return [n.replace("\\", "/") for n in zf.namelist() if n and not n.endswith("/")]


def detect_layout(entries):
    first_parts = [PurePosixPath(e).parts[0] for e in entries if PurePosixPath(e).parts]
    top = sorted(set(first_parts))
    flat_required = REQUIRED_ROOT.intersection({PurePosixPath(e).name for e in entries if len(PurePosixPath(e).parts) == 1})
    if len(top) == 1 and not flat_required:
        return "folder", top[0]
    return "flat", ""


def validate(zip_path: str, expect_flat: bool = False, check_xml: bool = False, check_svg: bool = False):
    errors = []
    warnings = []
    png_rows = []
    with zipfile.ZipFile(zip_path) as zf:
        entries = normalized_entries(zf)
        if not entries:
            errors.append("archive is empty")
            return errors, warnings, png_rows

        layout, root = detect_layout(entries)
        if expect_flat and layout != "flat":
            errors.append("expected flat-root package but archive has a single theme folder")
        if not expect_flat and layout != "folder":
            errors.append("expected exactly one top-level theme folder; use --flat only for documented flat test packages")

        rel_entries = []
        for entry in entries:
            parts = PurePosixPath(entry).parts
            if any(part in FORBIDDEN_PARTS for part in parts):
                errors.append(f"forbidden release path: {entry}")
            if layout == "folder" and root and parts and parts[0] == root:
                rel_entries.append("/".join(parts[1:]))
            else:
                rel_entries.append(entry)

        rel_set = set(rel_entries)
        missing = sorted(REQUIRED_ROOT - rel_set)
        for name in missing:
            errors.append(f"missing required root file: {name}")

        config_path = f"{root}/config.json" if layout == "folder" and root else "config.json"
        if config_path in entries:
            try:
                json.loads(zf.read(config_path).decode("utf-8-sig"))
            except Exception as exc:
                errors.append(f"config.json does not parse as JSON: {exc}")

        for entry in entries:
            lower = entry.lower()
            if check_xml and lower.endswith(".xml"):
                try:
                    ET.fromstring(zf.read(entry).decode("utf-8-sig"))
                except Exception as exc:
                    errors.append(f"XML does not parse: {entry}: {exc}")
            if check_svg and lower.endswith(".svg"):
                try:
                    ET.fromstring(zf.read(entry).decode("utf-8-sig"))
                except Exception as exc:
                    errors.append(f"SVG does not parse as XML: {entry}: {exc}")
            if not entry.lower().endswith(".png"):
                continue
            data = zf.read(entry)
            info = png_info(data)
            if not info:
                errors.append(f"invalid PNG: {entry}")
                continue
            width, height, color_type, has_alpha = info
            png_rows.append((entry, width, height, has_alpha))
            if is_probable_icon(entry) and not has_alpha:
                errors.append(f"icon-like PNG lacks alpha channel: {entry}")
            if width <= 0 or height <= 0:
                errors.append(f"invalid PNG dimensions: {entry}")

    return errors, warnings, png_rows


def parse_manifest_rows(path: str):
    text = Path(path).read_text(encoding="utf-8")
    rows = []
    lines = [line.strip() for line in text.splitlines() if "|" in line]
    header_idx = None
    headers = []
    for idx, line in enumerate(lines):
        cols = [c.strip().lower() for c in line.strip("|").split("|")]
        if "filename" in cols and "required" in cols:
            header_idx = idx
            headers = cols
            break
    if header_idx is None:
        return rows
    for line in lines[header_idx + 1:]:
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < len(headers):
            continue
        row = dict(zip(headers, cols))
        rows.append(row)
    return rows


def extract_inventory_names(path: str, require_no_placeholder: bool = False):
    text = Path(path).read_text(encoding="utf-8")
    names = []
    errors = []
    lines = [line.strip() for line in text.splitlines() if "|" in line]
    header_idx = None
    headers = []
    for idx, line in enumerate(lines):
        cols = [c.strip().lower() for c in line.strip("|").split("|")]
        if "filename" in cols and "required" in cols:
            header_idx = idx
            headers = cols
            break
    if header_idx is not None:
        filename_i = headers.index("filename")
        required_i = headers.index("required")
        status_i = headers.index("status") if "status" in headers else None
        art_source_i = headers.index("art source") if "art source" in headers else None
        for line in lines[header_idx + 1:]:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) <= max(filename_i, required_i):
                continue
            filename = cols[filename_i].strip("` ")
            if not re.search(r"\.(png|svg)$", filename, re.IGNORECASE):
                continue
            required = cols[required_i].lower()
            status = cols[status_i].lower() if status_i is not None and len(cols) > status_i else ""
            art_source = cols[art_source_i].lower() if art_source_i is not None and len(cols) > art_source_i else ""
            if required in ("yes", "planned"):
                names.append(filename)
                if status and status != "done":
                    errors.append(f"inventory row blocks release: {filename} required={required} status={status}")
                blocked_sources = {"", "script-generated", "placeholder", "default-icon", "emoji", "text-label", "geometric-filler"}
                if art_source in blocked_sources:
                    errors.append(f"inventory art source blocks release: {filename} art_source={art_source or 'blank'}")
            if require_no_placeholder and status == "placeholder":
                errors.append(f"inventory contains placeholder row: {filename}")
        return sorted(set(names)), errors
    pattern = re.compile(r"[\w@&+.\-]+(?:\.png|\.svg)", re.IGNORECASE)
    return sorted(set(pattern.findall(text))), errors


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a WeChat ThemeBox package zip.")
    parser.add_argument("zip_path")
    parser.add_argument("--flat", action="store_true", help="expect documented flat-root test package")
    parser.add_argument("--list-png", action="store_true", help="print PNG dimensions and alpha status")
    parser.add_argument("--inventory", action="append", default=[], help="text/markdown file containing expected .png/.svg filenames")
    parser.add_argument("--dimension-manifest", action="append", default=[], help="dimension manifest file to validate against package files")
    parser.add_argument("--require-no-placeholder", action="store_true", help="fail if inventory contains placeholder rows")
    parser.add_argument("--check-xml", action="store_true", help="parse XML files")
    parser.add_argument("--check-svg", action="store_true", help="parse SVG files as XML")
    args = parser.parse_args(argv)

    errors, warnings, png_rows = validate(args.zip_path, args.flat, args.check_xml, args.check_svg)
    if args.inventory:
        with zipfile.ZipFile(args.zip_path) as zf:
            entries = normalized_entries(zf)
            layout, root = detect_layout(entries)
            rel_names = set()
            for entry in entries:
                parts = PurePosixPath(entry).parts
                rel = "/".join(parts[1:]) if layout == "folder" and root and parts and parts[0] == root else entry
                rel_names.add(PurePosixPath(rel).name)
            for inventory_path in args.inventory:
                inventory_names, inventory_errors = extract_inventory_names(inventory_path, args.require_no_placeholder)
                errors.extend(inventory_errors)
                for name in inventory_names:
                    if name not in rel_names:
                        errors.append(f"inventory file missing from package: {name}")
    if args.dimension_manifest:
        with zipfile.ZipFile(args.zip_path) as zf:
            entries = normalized_entries(zf)
            layout, root = detect_layout(entries)
            rel_map = {}
            for entry in entries:
                parts = PurePosixPath(entry).parts
                rel = "/".join(parts[1:]) if layout == "folder" and root and parts and parts[0] == root else entry
                rel_map[PurePosixPath(rel).name] = entry
            for manifest_path in args.dimension_manifest:
                for row in parse_manifest_rows(manifest_path):
                    filename = row.get("filename", "").strip("` ")
                    status = row.get("status", "").lower()
                    required = row.get("required", "").lower()
                    alpha_required = row.get("alpha required", "").lower()
                    exported_size = row.get("exported size", "").lower()
                    if required in ("yes", "planned") and status not in ("done", "provisional"):
                        errors.append(f"manifest row blocks release: {filename} status={status}")
                    if filename and filename not in rel_map:
                        if required in ("yes", "planned"):
                            errors.append(f"manifest file missing from package: {filename}")
                        continue
                    if filename and filename in rel_map and exported_size and exported_size not in ("unknown", "provisional", ""):
                        entry = rel_map[filename]
                        if entry.lower().endswith(".png"):
                            data = zf.read(entry)
                            info = png_info(data)
                            if info:
                                width, height, color_type, has_alpha = info
                                size_text = f"{width}x{height}"
                                if exported_size.replace(" ", "") not in size_text.replace(" ", ""):
                                    errors.append(f"dimension mismatch for {filename}: manifest={exported_size} actual={size_text}")
                                if alpha_required in ("yes", "true") and not has_alpha:
                                    errors.append(f"alpha required but missing for {filename}")
    if args.list_png:
        for path, width, height, has_alpha in png_rows:
            print(f"{path}\t{width}x{height}\talpha={'yes' if has_alpha else 'no'}")
    for warning in warnings:
        print(f"WARN: {warning}", file=sys.stderr)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("ThemeBox package validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
