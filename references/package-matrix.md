# Package Matrix

Use this matrix to choose and validate the intended ThemeBox output. Do not merge these layouts into one ambiguous zip.

## Color Diagnostic Package

Purpose: test generated tokens, config, and color XML.

Layout:

```text
ThemeName-color-diagnostic/
  config.json
  weui_color_new.xml
  icon-map.json
  icon-categories.json
  icons/
```

Rules:

- This is not a final release package.
- Do not upload it as the user's finished theme.
- Do not include raw source files or private notes.

## DIY Folder-Root Release

Purpose: default finished package.

Layout:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  weui_color_new.xml
  png/
  svg/
  skin/
  assets/
```

Rules:

- The zip expands to exactly one top-level folder.
- Optional folders appear only when they contain release assets required by the inventory.
- Legacy files such as `weui_color.xml` or `color.css` appear only when documented.
- `themebox.dat` appears only when generated through the current user's own ThemeBox custom/export workflow.

## DIY Flat-Root Test Package

Purpose: import testing when a ThemeBox version expects loose root files.

Layout:

```text
config.json
cover.png
icon.png
weui_color_new.xml
png/
svg/
skin/
assets/
```

Rules:

- Name it clearly, for example `ThemeName-DIY-flat.zip`.
- Keep it separate from the folder-root release.
- Use only when import behavior is unknown or device testing asks for it.

## iMessage-Style Replacement Folder

Purpose: study or mirror a replacement-folder workflow from a compatible project.

Rules:

- Use only as structure evidence.
- Do not copy iMessage artwork, receipts, account files, or binary packs.
- Compare names, folder placement, scale suffixes, and dimensions.
- Rebuild all art from original source assets.

