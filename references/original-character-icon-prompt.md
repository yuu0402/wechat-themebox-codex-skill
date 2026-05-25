# Original Character Icon Prompt

Use this reference when a WeChat ThemeBox theme needs a full hand-drawn icon set where every icon carries the same original main character identity.

This public skill must stay generic. Do not write a user's private theme name, character name, personal name, project-specific IP, or reference-image identity into this file. Put project-specific names only in the user's active project prompt or project notes.

## Character Bible

Before drawing icons, define a compact character bible and keep it stable across the full asset set:

- IP name: `{main_original_ip}`
- Identity: `{short_original_character_identity}`
- Core shape language: `{body_shape}`, `{head_or_ear_shape}`, `{hands_or_paws}`, `{signature_silhouette}`
- Face rules: `{eye_style}`, `{mouth_style}`, `{expression_range}`
- Palette: `{primary_color}`, `{neutral_color}`, `{accent_color_1}`, `{accent_color_2}`, with enough contrast for daily WeChat use.
- Linework: hand-drawn, soft outline, never harsh black unless the theme explicitly requires it.
- Texture: clean sticker-like flat illustration with subtle paper grain or gentle brush edges.
- Reusable character elements: signature silhouette, local body features, exclusive accessories, representative patterns, expression language, gestures, motion effects, particles, trails, or an abstract transformation of the character into part of the icon subject.
- IP safety: do not imitate Disney, Sanrio, Pokemon, Line Friends, game/anime mascots, celebrity likenesses, or any existing protected character. Keep anatomy, silhouette, face, colors, and accessories original.

## Codex Prompt

Paste this to Codex when asking it to produce the theme assets. Replace placeholders with the current project's original character details:

```text
You are creating a complete original WeChat ThemeBox icon resource set.

Main original IP:
- Name: {main_original_ip}
- Character bible: {character_bible}
- This must be an original character. Do not imitate, recreate, trace, or closely transform any existing IP, film/game/anime character, brand mascot, celebrity, or specific reference-image character.

Goals:
1. Generate assets according to ThemeBox naming rules. Read references/asset-naming.md and references/design-guidelines.md first.
2. Hand-draw every icon. Do not recolor default system icons.
3. Every icon must include a visible element of {main_original_ip}, but the icon function must remain clear at small size.
4. Export transparent-background PNG/SVG source assets using exact ThemeBox filenames. PNG icons must have a real alpha channel. When a dark-mode asset is needed, also export the _Dark variant.
5. Icon resources must not have white square backgrounds, colored block backgrounds, rounded card canvases, or full-scene backgrounds. Only non-icon resources such as covers, wallpapers, panels, chat bubbles, and surface/tile assets may use opaque backgrounds.
6. Do not use script-drawn primitive placeholder artwork as final assets. Scripts may resize, package, validate, and make contact sheets, but final icons must be original hand-drawn artwork.
7. Do not crop icons from a larger scene. Each icon must be a complete independent object on a transparent canvas with enough padding.
8. For character-led themes, also draw character-based `cover.png`, `icon.png`, `launch.png`, page wallpapers, and chat backgrounds unless the user explicitly scopes the job to icons only.
9. Payment, wallet, red-packet, transfer, and service-grid assets are mandatory in a full pack. If direct payment wording triggers the image tool, use neutral visual wording while keeping the exact target filename in the inventory.

Icon rules:
- Keep the functional object silhouette clear first, then integrate the character identity.
- The main IP element does not need to be the full character. It can come from the character's signature silhouette, local body features, exclusive accessories, representative patterns, expression language, gestures, motion effects, light effects, particles, trails, or an abstract transformation of the character form into part of the icon subject.
- Do not simply paste a small unrelated character head in the corner. The character element must be integrated with the icon function.
- Do not draw every asset as the same face. Vary poses and integration by function.
- Small-size priority: the icon must remain readable at 80-120 px.
- Keep the set unified: consistent outline width, shadow direction, corner radius, color saturation, and internal padding.
- No text, no watermark, no complex background, no white square background, no colored block background, no opaque canvas, no photorealism, no 3D render, no glassmorphism, no copied IP traits.
- No cropped bodies, cropped ears, cropped tails, screenshot-like cutouts, or partial scene fragments unless the crop itself is a deliberate functional symbol and still reads as a complete icon.

First batch to generate and review:
- tabbar_main.png / tabbar_mainHL.png: chat bubble plus {main_original_ip} element.
- tabbar_contacts.png / tabbar_contactsHL.png: contacts/group metaphor plus {main_original_ip} element.
- tabbar_discover.png / tabbar_discoverHL.png: discover/compass/globe metaphor plus {main_original_ip} element.
- tabbar_me.png / tabbar_meHL.png: profile/avatar treatment based on {main_original_ip}.
- search_filled@3x.png: magnifier with integrated character element.
- scan_filled@3x.png: scan frame with integrated character element.
- camera_filled@3x.png: camera symbol with integrated character element.
- icons_filled_album@3x.png: album/photo stack with integrated character element.
- icons_filled_red_envelope@3x.png: red packet with integrated character element.
- transfer_filled@3x.png: transfer arrows with integrated character element.
- pay_filled@3x.png / pay_regular@3x.png: secure card or coin action with integrated character element.
- icons_filled_wechatpay@3x.png / icons_outlined_wechatpay@3x.png: generic payment/service mark with integrated character element, not copied brand art.
- icons_outlined_wallet@3x.png: wallet compartment with integrated character element.
- c2c_transfer_icon@3x.png / c2c_hongbao_icon_cn@3x.png: transfer/envelope object with integrated character element.
- favorites_filled@3x.png: favorite/star/heart metaphor with integrated character element.
- gear_regular@3x.png: settings gear with integrated character element.
- icons_filled_qr_code@3x.png: clear QR metaphor with integrated character element.
- voice_circle_filled@3x.png: voice/sound wave with integrated character element.
- video_filled@3x.png: video camera with integrated character element.

Before outputting each icon, write one design row:
filename | function | character element | color/state | needs Dark variant

Acceptance criteria:
- Filename exactly matches the ThemeBox list.
- The icon function is recognizable at a glance.
- Every icon includes an integrated original-character element, not a simple pasted corner badge.
- The full icon set looks like one hand-drawn theme.
- No recognizable traits from existing IP.
- Transparent-background edges are clean; no accidental white/solid-color canvas remains after export.
- Export size and @3x suffix match the target file.
- Icon is a complete independent object, not a cropped scene.
- Payment/service filenames are either completed or explicitly listed as blocked with the replacement neutral prompt to try next.
```

## Single Icon Prompt Template

Use this when generating assets one at a time:

```text
Create one original WeChat ThemeBox icon for "{filename}". Function: {function}. Style: {theme_style}, hand-drawn sticker icon, transparent background PNG with real alpha channel, readable at 80-120 px. Main original IP: "{main_original_ip}". Character bible: {character_bible}. Integrate the character into the function: {character_integration}. Keep the functional symbol clear first, then add the character identity. Palette: {palette}. The icon must be a complete independent object with transparent padding, not cropped from a larger scene. Canvas must be transparent with clean alpha edges; do not add a white square, colored block, rounded card, opaque background, scene background, text, watermark, complex background, script-drawn placeholder shapes, 3D, photorealism, harsh black outline, copied existing IP, or traits from Disney/Sanrio/Pokemon/Line Friends or other protected characters.
```

## Production Table

For every batch, maintain a table with these columns:

```text
filename | function | character element | selected/dark state | prompt | exported | checked
```

Do not mark a file checked until it has been visually reviewed for small-size clarity, transparent edges, naming accuracy, and IP originality.
