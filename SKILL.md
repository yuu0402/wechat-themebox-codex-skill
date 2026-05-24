---
name: wechat-themebox
description: Build, refine, package, and review original WeChat ThemeBox-compatible themes. Use when Codex is asked to make a WeChat theme, ThemeBox theme, WeChat DIY theme package, `weui_color_new.xml`, ThemeBox `config.json`, theme cover/icon assets, chat bubble/theme PNG resources, or document WeChat theme production rules and quality standards without copying protected third-party theme assets.
---

# WeChat ThemeBox

## Operating Rules

Create original theme source files and packages for ThemeBox-style WeChat themes. Treat this as a production guide for how to make a WeChat theme: define the style, build the required files, generate original assets, package the theme, and validate it on device.

Do not copy another author's `themebox.dat`, receipt files, paid assets, or protected package contents into a release. Use sample themes only as format evidence. If `themebox.dat` is required, use ThemeBox's own custom/export workflow to produce an original asset pack, then compare filenames and dimensions.

## Workflow

1. Clarify target style, theme name, author string, and whether the user wants a color-only source package or a fuller DIY package with PNG/SVG resources.
2. Inspect any existing project first. If no project exists, create a small source-driven builder instead of hand-editing packaged output.
3. Read [format-and-safety.md](references/format-and-safety.md) before changing package structure or handling third-party samples.
4. Read [build-workflow.md](references/build-workflow.md) before creating or modifying a build pipeline.
5. Read [design-guidelines.md](references/design-guidelines.md) before generating visual assets or judging theme quality.
6. Generate from source tokens, not by editing generated `dist` files. Keep light/dark pairs consistent.
7. Build, inspect the zip layout, and record device-test blockers. Treat ThemeBox import feedback as the source of truth.

## Theme Project Standard

Use a source-driven project layout:

```text
theme-project/
  src/
    tokens.json
  scripts/
    build.js
    build-diy.js
  notes/
  dist/
```

Generate at least:

```text
ThemeName/
  config.json
  weui_color_new.xml
  cover.png
  icon.png
```

For broader DIY packages, add `png/`, `svg/`, optional `weui_color.xml`, and any original resource files ThemeBox expects. Keep a flat zip variant when device import behavior is unknown.

## Theme Production Rules

Follow these standards when making a WeChat theme:

- Start from a named visual direction, not random colors.
- Define all colors as source tokens with light and dark variants.
- Generate `config.json` and XML color files from source data.
- Keep cover, icon, tabbar, chat bubble, background, badge, and input assets visually consistent.
- Use original artwork only.
- Keep common UI readable before adding decorative detail.
- Prefer small, testable package iterations over one large unverified pack.
- Record every device-test failure and update the builder so the next package improves.

## Validation

Run the project's build command, then inspect the generated archive. On Node projects, this is usually:

```powershell
npm run build
npm run build:diy
```

Verify:

- generated JSON and XML parse cleanly
- zip does not contain `__MACOSX`
- package root is either one theme folder or a documented flat root variant
- no third-party `themebox.dat`, `wxid_*.receipt`, or protected assets are present
- `cover.png` and `icon.png` exist and have stable dimensions
- light and dark token pairs exist for major WeUI colors

Document any remaining blocker, especially ThemeBox requiring `themebox.dat`.
