# ThemeBox Format And Safety

## Known Package Shapes

Observed ThemeBox-style packages use a theme folder rather than a single loose file.

Minimum accepted visible structure:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  weui_color_new.xml
```

Optional legacy or device-specific files may be added when the target workflow needs them:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  themebox.dat
  color.css
  weui_color.xml
  weui_color_new.xml
```

DIY/export-style folders may include:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  weui_color_new.xml
  weui_color.xml
  png/
  svg/
  skin/
  assets/
```

The `png/`, `svg/`, `skin/`, and `assets/` folders are for organization only. Final release packages must not contain source junk, intermediate build output, or duplicate asset trees unless the builder documents why both the folder-root and flat-root variants are needed.

## Package Rules

- Release zips must contain exactly one top-level theme folder unless the documented flat-root variant is intentionally being built for import testing.
- The theme folder must contain only accepted release files and resource folders.
- Do not ship source code, scripts, notes, cache files, temp exports, or raw working directories inside the release zip.
- Do not rename accepted ThemeBox resource files just to make the archive look cleaner.
- If a file is required by the target inventory, it must be present at the expected path in the package root or documented subfolder.
- If a file is not required, leave it out. Do not add placeholder clutter.
- When the target workflow needs a flat-root variant, keep that variant documented and build it separately from the folder-root package.
- Use the same internal file layout for both variants unless the ThemeBox version explicitly requires a different import path.

## `config.json`

Common fields. If the target ThemeBox workflow generates `themeId`, do not hand-fill it; otherwise only set it when a known package workflow requires a stable id.

```json
{
  "themeId": "IDExample001",
  "name": "Theme Name",
  "auth": "Author",
  "version": 1,
  "tabbar_size": "28*28",
  "tabbar_top_enabled": "true",
  "tabbar_top": -10,
  "tabbar_hide_title": "true",
  "tabbar_nor_color": "000000",
  "tabbar_nor_color_dark": "ffffff",
  "tabbar_sel_color": "000000",
  "tabbar_sel_color_dark": "ffffff",
  "badge_color": "ff3b30",
  "badge_color_dark": "ff453a",
  "badge_text_color": "ffffff",
  "badge_text_color_dark": "ffffff",
  "tabbar_top_enabled": false,
  "tabbar_top": -10,
  "tabbar_hide_title": false,
  "bubble_edge": "25*30*13*30",
  "hide_source_title": true,
  "hongbao_text_color": "#2E2B28",
  "hongbao_text_color_dark": "#EDE4DD",
  "luckmoney_text_color": "#2E2B28",
  "luckmoney_text_color_dark": "#EDE4DD"
}
```

Some samples use `#RRGGBB`; some config examples omit `#` for tabbar colors. Preserve the convention already used by the target project unless device tests prove otherwise.

Config field meanings:

- `name`: theme display name.
- `auth`: author name.
- `version`: optional theme version; some workflows auto-generate it.
- `themeId`: system-generated in the upstream ThemeBox guide; avoid manually setting it unless testing proves the target workflow needs it.
- `tabbar_nor_color`, `tabbar_nor_color_dark`: tabbar title color for normal state.
- `tabbar_sel_color`, `tabbar_sel_color_dark`: tabbar title color for selected state.
- `badge_color`, `badge_color_dark`: unread badge background color.
- `badge_text_color`, `badge_text_color_dark`: unread badge text color.
- `tabbar_size`: tabbar icon size, for example `30*30`.
- `tabbar_top_enabled`: enables custom tabbar icon vertical offset when floating tabbar is disabled.
- `tabbar_top`: tabbar icon offset value, for example `-10`.
- `tabbar_hide_title`: hides tabbar titles when floating tabbar is disabled.
- `luckmoney_text_color`, `luckmoney_text_color_dark`: red-packet open-cover text color.
- `hongbao_text_color`, `hongbao_text_color_dark`: red-packet/transfer bubble text color.
- `menu_text_color`, `menu_text_color_dark`: long-press message menu text color.
- `hide_source_title`: hides source title on red-packet, transfer, mini-program, and similar bubbles.
- `bubble_edge`: chat bubble cap insets, commonly written as `top*left*bottom*right`.

## Color Files

`weui_color_new.xml` is the preferred modern color map. Use light/dark paired values where possible:

```xml
<resources>
    <color name="BG_0">#F7F4F1,#2B2A26</color>
    <color name="FG_0">#000000E5,#FFFFFFCC</color>
    <color name="Brand">#3D3A38,#9D9994</color>
</resources>
```

Important families:

- `BG_*`, `FG_*`
- `Glyph_*`
- `Brand*`, `Red*`, `Orange*`, `Green*`, `Blue*`, `Purple*`
- `Separator_*`
- `StateLayer_*`
- `Material_*`
- `ProgressIndicator_Brand_BG`

Older themes may also need `color.css` and `weui_color.xml`. Generate them only when the target workflow needs legacy compatibility.

## Resource Naming Leads

Common DIY resource names:

- Tabbar icons: `tabbar_main`, `tabbar_contacts`, `tabbar_discover`, `tabbar_me`
- Selected tabbar icons: add `HL`
- Dark mode assets: add `_Dark` before `.png`
- Tabbar backgrounds: `tabbar_bg`, `tabbar_bg_Dark`
- Topbar backgrounds: `topbar_bg`, `topbar_bg_Dark`, `chat_topbar_bg`, `chat_topbar_bg_Dark`
- Page backgrounds: `default_bg`, `main_bg`, `constacts_bg`, `discover_bg`, `me_bg`, `chat_bg`, `album_bg`
- Badges: `badge`, `badge_small`
- Chat input: `input_bg`, `input_text_bg`, `input_voice_bg`, `input_search_bg`
- Contact/session avatars: `weixin`, `wepay`, `notification_messages`, `openimbrand`, `brandsessionholder`, `brandservicesessionholder`, `filehelper`, `qqmail`, `brandsessionholder_weapp`

For the full known filename list from the provided naming sheets, read [asset-naming.md](asset-naming.md). Use that file when building a broad theme pack or mapping every icon/resource replacement.

## `themebox.dat`

Treat `themebox.dat` as unresolved packed media/resource data. Local samples showed high entropy and nonstandard headers, suggesting compression or encryption. Do not reverse engineer protected packs or bypass receipts.

Safe path:

1. Build original editable files.
2. Import into ThemeBox test environment.
3. If ThemeBox requires `themebox.dat`, create/export an original blank/custom theme through ThemeBox.
4. Compare only structure, filenames, dimensions, and replaceable slots.
5. Never ship copied `themebox.dat` or `wxid_*.receipt`.

## Device Import Notes

Likely test paths include extracted folders under `Documents/ThemeBox/diy` or `Documents/ThemeBox/Themes`, depending on ThemeBox version. Test extracted folders as well as zip import. Record exact failure messages and missing filenames.

## Structure Acceptance

A package is only acceptable when:

- the root shape matches the documented variant
- required files exist at the expected paths
- no extra source or temp directories are present
- icon/background separation matches the inventory
- device import confirms the structure, not only the file list
