# Build Workflow

## Preferred Project

When working in this user's workspace, use:

```text
D:\OpenClaw\workspace\wechat-theme-yuni
```

Known commands:

```powershell
npm run build
npm run build:diy
npm run clean
```

Known outputs:

```text
dist/
  YuNi Warm Paper/
  YuNi-Warm-Paper-source.zip
  YuNi-Warm-Paper-DIY/
  YuNi-Warm-Paper-DIY.zip
  YuNi-Warm-Paper-DIY-flat.zip
```

## Source Of Truth

Use `src/tokens.json` as the palette and metadata source. Do not hand-edit generated files under `dist/`.

Token groups to preserve:

- theme id, name, author, version
- light/dark backgrounds and surfaces
- text and muted text
- brand/accent colors
- chat bubble colors
- icon background and line colors
- card, money, red packet, file, panel, badge, danger, warning colors

## Build Levels

### Color Source Package

Generate a conservative package with:

```text
ThemeName/
  config.json
  weui_color_new.xml
  icon-map.json
  icon-categories.json
  icons/
  README.txt
```

This is useful for testing token compatibility, but may not load as a complete ThemeBox theme.

### DIY Package

Generate:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  weui_color_new.xml
  weui_color.xml
  png/
  svg/
  DIY-LOAD-NOTES.txt
```

Build both folder-root zip and flat-root zip when import behavior is unknown.

## Generated Asset Strategy

Use deterministic assets first:

- Create SVG line icons for core semantics.
- Generate simple PNG placeholders with correct dimensions and original colors.
- Use known ThemeBox filenames from local notes only as naming compatibility clues.

Then improve quality:

- Replace high-impact icons with original generated or hand-drawn PNG assets.
- Keep naming and dimensions stable.
- Preserve transparent backgrounds for icons.

## Archive Checks

After build, inspect:

```powershell
Expand-Archive -LiteralPath dist\Theme.zip -DestinationPath tmp\inspect -Force
Get-ChildItem -Recurse tmp\inspect
```

Check:

- exactly one top-level folder unless intentionally flat
- no `__MACOSX`
- no sample receipts
- no copied protected binary packs
- required config/color/image files exist
- device notes state whether `themebox.dat` is intentionally absent

## Device Feedback Loop

When the package is tested on a device, update `notes/device-test.md` with:

- date
- ThemeBox/WeChat environment if known
- import method and device path
- zip or extracted folder layout tested
- success/failure result
- exact missing file or error
- next builder change

Treat device behavior as higher confidence than inferred sample structure.
