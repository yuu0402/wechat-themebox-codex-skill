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
4. Export transparent-background PNG/SVG source assets using exact ThemeBox filenames. When a dark-mode asset is needed, also export the _Dark variant.

Icon rules:
- Keep the functional object silhouette clear first, then integrate the character identity.
- The main IP element does not need to be the full character. It can come from the character's signature silhouette, local body features, exclusive accessories, representative patterns, expression language, gestures, motion effects, light effects, particles, trails, or an abstract transformation of the character form into part of the icon subject.
- Do not simply paste a small unrelated character head in the corner. The character element must be integrated with the icon function.
- Do not draw every asset as the same face. Vary poses and integration by function.
- Small-size priority: the icon must remain readable at 80-120 px.
- Keep the set unified: consistent outline width, shadow direction, corner radius, color saturation, and internal padding.
- No text, no watermark, no complex background, no photorealism, no 3D render, no glassmorphism, no copied IP traits.

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
- Transparent-background edges are clean.
- Export size and @3x suffix match the target file.
```

## Single Icon Prompt Template

Use this when generating assets one at a time:

```text
Create one original WeChat ThemeBox icon for "{filename}". Function: {function}. Style: {theme_style}, hand-drawn sticker icon, transparent background, readable at 80-120 px. Main original IP: "{main_original_ip}". Character bible: {character_bible}. Integrate the character into the function: {character_integration}. Keep the functional symbol clear first, then add the character identity. Palette: {palette}. No text, no watermark, no complex background, no 3D, no photorealism, no harsh black outline, no copied existing IP, no traits from Disney/Sanrio/Pokemon/Line Friends or other protected characters.
```

## Production Table

For every batch, maintain a table with these columns:

```text
filename | function | character element | selected/dark state | prompt | exported | checked
```

Do not mark a file checked until it has been visually reviewed for small-size clarity, transparent edges, naming accuracy, and IP originality.
