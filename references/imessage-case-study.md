# iMessage ThemeBox Case Study

Use `AidenYang1/iMessageApp_WeChat_For_Themebox` as a practical reference for project organization and ThemeBox adaptation patterns. Do not treat it as permission to copy Apple/iMessage visual identity or bundled theme art into a new public release.

Source:

- https://github.com/AidenYang1/iMessageApp_WeChat_For_Themebox

## What It Shows

The project is a complete ThemeBox WeChat theme case study. It demonstrates:

- a main theme folder
- a replaceable-assets folder
- alternate chat bubble color packs
- red-packet and transfer bubble card packs
- Sketch and PSD source files
- helper scripts for asset extraction and duplicate-resource matching
- public releases for versioned theme packages

Observed repository scale at review time:

- 4,692 tracked files
- 855 files under the main `WeChat-iMessage-Themebox` theme folder
- 35 files under `01供替换的素材`
- 301 files under `02更多红包、转账气泡替换`
- 3 Sketch files
- 1 PSD file
- 2 Python helper scripts

## Project Layout Pattern

Useful layout idea:

```text
theme-repo/
  README.md
  themebox-config.txt
  WeChat-iMessage-Themebox/
  01供替换的素材/
  02更多红包、转账气泡替换/
  png/
  其他/
    00官方50版本assets参考/
    01该主题完整项目文件（Sketch）/
    02红包转账气泡制作（PS项目文件）/
    03项目部分输出素材/
    04辅助脚本/
```

For a new original theme, mirror this organization with English or project-specific names:

```text
theme-repo/
  README.md
  themebox-config.txt
  theme/
  replaceable-assets/
  bubble-packs/
  previews/
  source/
    sketch-or-figma/
    psd/
  scripts/
```

Treat `themebox-config.txt` as analysis-only sample material. Do not copy it into a new public release tree unless the current workflow explicitly needs a private export artifact for local inspection. For public theme packages, keep raw export payloads, receipts, and device settings out of the release tree.

## Practical Adaptation Notes

The README emphasizes:

- ThemeBox compatibility is version-sensitive.
- The project targets ThemeBox 1.1.1+ and WeChat 8.0.54+ for its archived open-source baseline.
- Some icon slots reuse the same resource name across multiple UI locations, so one replacement may affect several places.
- The theme relies on full rounded-corner/global rounded settings for best visual fit.
- The main theme folder contents should be imported into the device ThemeBox DIY target, rather than dragging the wrapper folder blindly.
- Restart WeChat after applying theme files.
- Keep checking updated docs and release notes because naming changes with WeChat and ThemeBox versions.

## Design Pattern To Learn, Not Copy

The iMessage project uses:

- blue as the dominant accent
- clean system-style icon language
- light mode and OLED dark mode
- simplified primary/secondary screens
- input bar and menu bar polish
- vectorized icons where possible
- separate treatment for third-party plugin tools
- custom red-packet and transfer card skins

For a new public theme, translate this into original direction rules:

- choose one clear theme language
- define light and dark behavior up front
- keep chat readability higher priority than decoration
- build special packs for red packets, transfers, and bubbles
- document which assets are core, optional, or alternate skins

## Bubble And Card Pack Names

Red-packet/transfer card packs are a major reusable pattern. Common names observed include:

- `ChatRoom_Bubble_HB_Sender@3x.png`
- `ChatRoom_Bubble_HB_Sender_Dark@3x.png`
- `ChatRoom_Bubble_HB_Sender_Handled@3x.png`
- `ChatRoom_Bubble_HB_Sender_Handled_Dark@3x.png`
- `ChatRoom_Bubble_HB_Receiver@3x.png`
- `ChatRoom_Bubble_HB_Receiver_Dark@3x.png`
- `ChatRoom_Bubble_HB_Receiver_Handled@3x.png`
- `ChatRoom_Bubble_HB_Receiver_Handled_Dark@3x.png`
- `ChatRoom_Bubble_HB_Overtime_Sender@3x.png`
- `ChatRoom_Bubble_HB_Overtime_Sender_Dark@3x.png`
- `ChatRoom_Bubble_HB_Overtime_Receiver@3x.png`
- `ChatRoom_Bubble_HB_Overtime_Receiver_Dark@3x.png`

The repo also contains broader text, app, AA, common-mask, sender/receiver, handled, overtime, light, and dark bubble variants. When making a new theme, create a state matrix before drawing:

- sender vs receiver
- normal vs highlighted
- light vs dark
- text bubble vs app bubble
- red packet vs transfer/AA
- normal vs handled vs overtime

For the generated filename inventory from this repository, read [imessage-inventory.md](imessage-inventory.md). For the decoded exported ThemeBox config key list, read [themebox-config-keys.md](themebox-config-keys.md).

## Helper Script Ideas

The project includes scripts for:

- extracting official WeChat asset names, previews, and sizes into a table
- grouping same-image assets under different filenames by image hash
- calculating 1x, 2x, and 3x dimensions

If implementing similar scripts in a new theme builder, keep them read-only for third-party sources and write reports into `notes/` or `reports/`.
