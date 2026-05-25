#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import struct
import sys
import zipfile
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


def validate(zip_path: str, expect_flat: bool = False):
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


def extract_inventory_names(path: str):
    text = Path(path).read_text(encoding="utf-8")
    pattern = re.compile(r"[\w@&+.\-]+(?:\.png|\.svg)", re.IGNORECASE)
    return sorted(set(pattern.findall(text)))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Validate a WeChat ThemeBox package zip.")
    parser.add_argument("zip_path")
    parser.add_argument("--flat", action="store_true", help="expect documented flat-root test package")
    parser.add_argument("--list-png", action="store_true", help="print PNG dimensions and alpha status")
    parser.add_argument("--inventory", action="append", default=[], help="text/markdown file containing expected .png/.svg filenames")
    args = parser.parse_args(argv)

    errors, warnings, png_rows = validate(args.zip_path, args.flat)
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
                for name in extract_inventory_names(inventory_path):
                    if name not in rel_names:
                        errors.append(f"inventory file missing from package: {name}")
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
