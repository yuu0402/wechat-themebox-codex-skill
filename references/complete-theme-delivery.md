# Complete Theme Delivery Standard

Use this reference when the user asks for a complete WeChat ThemeBox theme package or when the agent is new to ThemeBox.

## Definition Of Complete

A complete character-led theme package must include:

- valid package structure from `package-matrix.md`
- `config.json`
- `weui_color_new.xml`
- `cover.png`
- `icon.png`
- `launch.png`
- page backgrounds: `default_bg.png`, `main_bg.png`, `contacts_bg.png`, `discover_bg.png`, `me_bg.png`, `chat_bg.png`, `album_bg.png`
- tabbar background and normal/selected tabbar icons
- topbar/chat topbar resources when present in the target inventory
- chat bubble/input/badge resources
- common action icons
- file/status/window/play/download/share/delete/copy resources when present
- payment/service/wallet/red-packet/transfer resources from `payment-service-assets.md`
- dark variants when the target filename family uses `_Dark`
- an inventory table with every requested file marked as generated, checked, missing, placeholder, or blocked
- a dimension manifest for every generated image

Do not call a package complete while any requested visual resource is still a script placeholder, missing, unreviewed, or undocumented.

## Beginner Agent Workflow

1. Read `SKILL.md`, `production-checklist.md`, `package-matrix.md`, `asset-naming.md`, `icon-size-guidelines.md`, and this file.
2. Decide whether the user asked for a complete pack or a partial pack.
3. Create an inventory table before drawing.
4. Define the original character bible and palette.
5. Define package layout and build outputs.
6. Generate/draw launch, cover, icon, wallpapers, and high-impact UI surfaces first.
7. Draw icon batches by functional group, not random filename order.
8. Replace every placeholder with hand-drawn original art before release.
9. Build the package from source.
10. Run package validation and inventory comparison.
11. Produce a contact sheet or visual review sheet.
12. Record device-test blockers separately from finished local validation.

## Release Handoff Gate

A release is blocked unless these artifacts exist:

- folder-root release zip
- flat-root test zip when import behavior is unknown or requested
- `inventory.md` using `inventory-format.md`
- `dimension-manifest.md`
- `contact-sheet.png`
- `validation-report.txt`
- device-test notes, or an explicit no-device-test blocker

Do not hand off a complete theme with placeholder status rows, missing required files, unknown package layout, or unrecorded dimensions.

## Functional Batch Order

Use this order for full packs:

1. Package identity: `cover.png`, `icon.png`, `launch.png`.
2. Core backgrounds: page backgrounds and chat background.
3. Navigation: tabbar, topbar, chat topbar, selected/unselected states.
4. Chat surfaces: bubbles, input areas, badges, message tips.
5. Core tabs and app actions: chat, contacts, discover, me, search, scan, camera, album.
6. File and status actions: file types, folder, download, share/forward, copy, delete, close, window controls, play/voice/video.
7. Payment and services: pay, wallet, card, red packet, transfer, receipt, keyboard delete, loading states, service-grid entries.
8. Remaining inventory names and dark variants.

## Launch Art Requirements

`launch.png` should be one of the best-looking assets in the theme. It is the opening impression and should establish the original character identity clearly.

Rules:

- Use the original character as the main subject or clear scene anchor.
- Keep the center composition strong and memorable.
- Leave quiet safe space near the top and bottom for launch behavior, cropping, and device variation.
- Keep the top 15-20% and bottom 12-18% free of faces, text-like marks, high-contrast details, and critical character parts.
- Keep the main subject inside the central 60-70% of the canvas, with no important detail within 6% of any edge.
- Avoid text, watermarks, UI labels, and busy patterns.
- Use calm background shapes, soft lighting, and controlled contrast.
- Do not use gradients alone as finished launch art.
- Do not make it darker, noisier, or more detailed than the daily UI can tolerate.
- Create a dark-mode companion only when the target inventory or package pattern needs it.

## Background And Wallpaper Requirements

Backgrounds must support WeChat readability first.

Rules:

- Use subtle character motifs, faint patterns, soft scene hints, or low-contrast decorative elements.
- Do not use busy full-scene illustration behind chat text.
- Do not use high-saturation, noisy, neon, dense starfield, high-frequency texture, or repeating pattern backgrounds.
- Chat backgrounds must be calmer than cover or launch art.
- `chat_bg.png` must be the quietest background: no faces, focal character, large props, or high-contrast motifs in the central message column. Put character cues near corners/edges or use faint patterning only.
- Page roles should differ while staying restrained: `main_bg` = broad theme mood, `contacts_bg` = quiet list-safe texture, `discover_bg` = slightly more playful motif, `me_bg` = strongest personal/character cue, `album_bg` = media-safe neutral surface, `chat_bg` = lowest contrast.
- Main page backgrounds can show more character identity than chat backgrounds, but still must not fight text and cells.
- Dark backgrounds must be separately designed, not blindly inverted.
- Page backgrounds may be opaque; icon assets must not be.

## Dimension And Size Requirements

Do not guess final dimensions.

Required process:

1. If a target package or exported original asset exists, inspect its dimensions and match them.
2. If ThemeDocs or iMessage inventory provides size information, record that source and confidence.
3. If no authoritative size exists yet, create a provisional size, mark it `provisional` in the dimension manifest, and verify on device before final.
4. Keep light, dark, selected, and unselected variants aligned to the same canvas dimensions.
5. Do not crop transparent margins away from icons just to make the artwork look larger.
6. Do not resize backgrounds with non-proportional stretching.

Dimension manifest rows must include:

```text
filename | slot | expected size | exported size | source | confidence | alpha required | status | notes
```

Working guidance before device confirmation:

- tabbar logical size: follow `tabbar_size` in `config.json`, commonly near `28*28` or `30*30`.
- icons: use the target filename family and scale suffix; keep readable at `80-120 px` previews.
- launch/wallpaper/backgrounds: follow the target slot or exported original dimensions; if unknown, generate a high-resolution provisional master at a modern phone portrait ratio, such as `9:19.5` or `1290x2796`, then export only to the measured ThemeBox slot when available. Mark the master and exports provisional until device/import verification confirms dimensions.
- cover/icon package images: stable dimensions must be recorded and validated; do not leave them as arbitrary generation sizes.
