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
4. Read [production-checklist.md](references/production-checklist.md) before any build, review, package, or handoff.
5. Read [complete-theme-delivery.md](references/complete-theme-delivery.md) when the user asks for a complete theme pack or when the agent is new to ThemeBox.
6. Read [visual-qa-troubleshooting.md](references/visual-qa-troubleshooting.md) when fixing topbar, launch, wallpaper, background, cropping, or placeholder-art problems.
7. Read [payment-service-assets.md](references/payment-service-assets.md) when building payment, wallet, red-packet, transfer, or service-grid assets.
8. Read [package-matrix.md](references/package-matrix.md) when choosing or validating release, flat, or diagnostic package layout.
9. Read [dimension-manifest.md](references/dimension-manifest.md) when recording or checking observed per-file dimensions.
10. Read [inventory-format.md](references/inventory-format.md) before building a complete pack so required/planned files are tracked as data, not memory.
11. Read [themebox-dat-playbook.md](references/themebox-dat-playbook.md) when a workflow mentions `themebox.dat` or import failure around it.
12. Read [asset-naming.md](references/asset-naming.md) before naming or mapping theme images.
13. Read [icon-size-guidelines.md](references/icon-size-guidelines.md) before exporting icon assets or writing icon batch prompts.
14. Read [upstream-sources.md](references/upstream-sources.md) when you need the external ThemeDocs source or version caveats.
15. Read [build-workflow.md](references/build-workflow.md) before creating or modifying a build pipeline.
16. Read [design-guidelines.md](references/design-guidelines.md) before generating visual assets or judging theme quality.
17. Read [original-character-icon-prompt.md](references/original-character-icon-prompt.md) when the user wants every icon hand-drawn around a main original character or mascot.
18. Read [imessage-case-study.md](references/imessage-case-study.md) when using the public iMessage ThemeBox project as an engineering/reference case.
19. Read [imessage-inventory.md](references/imessage-inventory.md) when you need the observed iMessage project filename inventory.
20. Read [themebox-config-keys.md](references/themebox-config-keys.md) only for advanced exported-config analysis.
21. Generate from source tokens, not by editing generated `dist` files. Keep light/dark pairs consistent.
22. Build, inspect the zip layout, generate a contact sheet, and record device-test blockers. Treat ThemeBox import feedback as the source of truth.

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
- Export icon-style resources with transparent backgrounds and real alpha channels. Do not place WeChat icons on white squares, colored blocks, rounded cards, or decorative scene backgrounds unless the target resource is explicitly a background, panel, bubble, tile, cover, or surface image.
- Keep a production inventory for every batch. Do not leave icon counts, filenames, sizes, or export status implicit.
- Keep icon and background families separate. If a resource is an icon, treat it as an icon; if it is a background, treat it as a surface resource.
- All requested resource groups are mandatory unless the user explicitly says to skip them. Do not omit payment, wallet, red-packet, transfer, service, launch, or wallpaper assets because of prompt sensitivity.
- Every theme asset should be hand-drawn original art. Script generation may assist with packaging, resizing, inventory, and validation, but not with final placeholder icon artwork.
- Never ship script-drawn placeholders, default-icon recolors, emoji substitutes, text labels, or primitive geometric filler as finished visual assets. Mark temporary placeholders as `placeholder` and replace them before release.
- Avoid cropping final icon assets. Each icon should read as an independent complete object on a transparent canvas.
- Vary character integration across the icon family: use different poses, silhouettes, local features, accessories, patterns, gestures, particles, and transformations instead of repeating the same mascot head.
- Build launch art and wallpapers from the same original character bible when the project is character-led.
- Treat `launch.png` as a premium character artwork asset, not a generic gradient. Keep wallpapers calm, low-noise, and readable behind WeChat UI.
- Record dimensions for every generated image. If a target size is unknown, mark it provisional and verify with ThemeBox/device feedback before calling the package final.
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

For release zips, run the bundled structure/alpha validator:

```powershell
py path\to\wechat-themebox\scripts\validate_theme_package.py dist\ThemeName-DIY.zip --list-png
py path\to\wechat-themebox\scripts\validate_theme_package.py dist\ThemeName-DIY-flat.zip --flat --list-png
```

To compare the package against an inventory file, add `--inventory` entries:

```powershell
py path\to\wechat-themebox\scripts\validate_theme_package.py dist\ThemeName-DIY.zip --inventory dist\inventory.md --require-no-placeholder --check-xml --check-svg
```

To compare against the project dimension manifest, add `--dimension-manifest`:

```powershell
py path\to\wechat-themebox\scripts\validate_theme_package.py dist\ThemeName-DIY.zip --dimension-manifest dist\dimension-manifest.md
```

To create a contact sheet:

```powershell
py D:\OpenClaw\codex-home\skills\wechat-themebox\scripts\make_contact_sheet.py dist\ThemeName-DIY\png dist\contact-sheet.png
```

Verify:

- generated JSON and XML parse cleanly
- zip does not contain `__MACOSX`
- package root is either one theme folder or a documented flat root variant
- no third-party `themebox.dat`, `wxid_*.receipt`, or protected assets are present
- `cover.png` and `icon.png` exist and have stable dimensions
- icon assets record exported dimensions, preserve target-slot sizing, and keep transparent alpha
- all requested resource categories are explicitly inventoried, not implied
- topbar, launch, wallpaper, payment, and service screens are included in visual QA for full packs
- light and dark token pairs exist for major WeUI colors

Document any remaining blocker, especially ThemeBox requiring `themebox.dat`.
