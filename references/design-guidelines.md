# Design Guidelines

## Theme Quality Bar

Design for long-term daily WeChat use: calm, readable, low visual noise, clear hierarchy, and consistent light/dark behavior. Avoid high-saturation novelty palettes that make chat and payment screens tiring.

## Warm Paper Direction

The existing YuNi direction uses:

- warm paper backgrounds
- soft brown text and linework
- muted green, blue, orange, red, and purple accents
- pale outgoing and incoming chat bubbles
- dark mode with warm dark surfaces, not pure black
- transparent-background icons with small-object semantics

Representative palette:

```json
{
  "lightBg": "#F3EEE6",
  "lightSurface": "#FFFBF4",
  "darkBg": "#1B1712",
  "darkSurface": "#252018",
  "lightText": "#29231E",
  "darkText": "#F0E7DB",
  "brand": "#8A735B",
  "brandDark": "#D3B895",
  "green": "#7D956E",
  "blue": "#6F8FA3",
  "orange": "#C98A4B",
  "red": "#B96955"
}
```

## Icon Rules

For a premium cartoon ThemeBox theme:

- Use transparent PNG/SVG icon backgrounds.
- Put the subject on a warm off-white rounded paper base when the icon needs a tile.
- Use soft brown linework instead of black.
- Keep detail low enough to read at 80-120 px.
- Make each icon semantic, not a generic circle or card.
- Build dark-mode variants deliberately; do not just invert light icons.
- Keep line width, radius, shadow, and color accents consistent.

High-impact icons to polish first:

1. Chat: paired chat bubbles.
2. Contacts: head/avatar or small group.
3. Discover: globe, compass, or lens.
4. Me: avatar/person.
5. Search: magnifier.
6. Scan: rounded QR frame.
7. Camera and album.
8. File.
9. Favorite/star.
10. Red packet and transfer.
11. Voice and video.
12. Settings.
13. Download/share/copy/delete.
14. Mini program grid.
15. Moments/feed.

## Image Generation Prompt Pattern

Use this structure when asking an image model for original icons:

```text
Create one WeChat ThemeBox DIY icon for "{icon name}". Style: warm paper, premium soft cartoon, hand-drawn sticker, transparent background PNG. Subject: {specific object}. Colors: warm off-white rounded paper base, soft brown outline, small muted green/orange/blue accents. Requirements: readable at small size, clean edges, no text, no watermark, no black outline, no complex background.
```

Negative prompt:

```text
No photorealism, no 3D render, no heavy shadow, no black outline, no neon colors, no cold blue-purple main palette, no glassmorphism, no metallic texture, no complex background, no watermark, no default system icon style, no generic circle-only placeholder, no dirty edges.
```

## Review Checklist

Before shipping a visual update, inspect:

- chat page readability
- tabbar selected/unselected contrast
- red packet and payment text contrast
- search/input surface contrast
- badge readability
- dark mode backgrounds and separators
- icon set consistency across common screens
