# ThemeBox Format And Safety

## Known Package Shapes

Observed ThemeBox-style packages use a theme folder rather than a single loose file.

Minimum visible structure from samples:

```text
ThemeName/
  config.json
  color.css
  weui_color.xml
  cover.png
  themebox.dat
```

Modern/recolor-capable structure may be:

```text
ThemeName/
  config.json
  cover.png
  icon.png
  themebox.dat
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

The `png/`, `svg/`, `skin/`, and `assets/` folders are mostly for organization; ThemeBox may also accept resources at the theme root depending on version and import path.

## `config.json`

Common fields:

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
  "bubble_edge": "25*30*13*30",
  "hide_source_title": true,
  "hongbao_text_color": "#2E2B28",
  "hongbao_text_color_dark": "#EDE4DD",
  "luckmoney_text_color": "#2E2B28",
  "luckmoney_text_color_dark": "#EDE4DD"
}
```

Some samples use `#RRGGBB`; some config examples omit `#` for tabbar colors. Preserve the convention already used by the target project unless device tests prove otherwise.

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
