#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError as exc:
    raise SystemExit("Pillow is required: py -m pip install pillow") from exc


def collect_images(root: Path):
    return sorted([p for p in root.rglob("*.png") if "__pycache__" not in p.parts])


def make_sheet(input_dir: Path, output: Path, thumb: int = 96, label_h: int = 34, cols: int = 8):
    images = collect_images(input_dir)
    if not images:
        raise SystemExit(f"no PNG files found under {input_dir}")
    rows = math.ceil(len(images) / cols)
    cell_w = thumb + 24
    cell_h = thumb + label_h + 20
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()
    for idx, path in enumerate(images):
        col = idx % cols
        row = idx // cols
        x = col * cell_w + 12
        y = row * cell_h + 10
        with Image.open(path) as im:
            im = im.convert("RGBA")
            im.thumbnail((thumb, thumb), Image.LANCZOS)
            checker = Image.new("RGB", (thumb, thumb), "#f2f2f2")
            cd = ImageDraw.Draw(checker)
            step = 8
            for yy in range(0, thumb, step):
                for xx in range(0, thumb, step):
                    if (xx // step + yy // step) % 2:
                        cd.rectangle([xx, yy, xx + step - 1, yy + step - 1], fill="#ffffff")
            px = x + (thumb - im.width) // 2
            py = y + (thumb - im.height) // 2
            sheet.paste(checker, (x, y))
            sheet.paste(im, (px, py), im)
        name = path.name
        if len(name) > 18:
            name = name[:15] + "..."
        draw.text((x, y + thumb + 4), name, fill="black", font=font)
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)
    print(f"wrote {output} ({len(images)} images)")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Create a PNG contact sheet for ThemeBox assets.")
    parser.add_argument("input_dir")
    parser.add_argument("output")
    parser.add_argument("--thumb", type=int, default=96)
    parser.add_argument("--cols", type=int, default=8)
    args = parser.parse_args(argv)
    make_sheet(Path(args.input_dir), Path(args.output), args.thumb, cols=args.cols)


if __name__ == "__main__":
    main()
