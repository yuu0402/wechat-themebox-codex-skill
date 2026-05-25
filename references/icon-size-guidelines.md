# WeChat ThemeBox Icon Size Guidelines

ThemeBox does not expose one universal size table for every resource. Use the target slot, the exported original asset, and device import feedback as the source of truth.

## Stable Rules

- Keep icon resources transparent and match the target filename's scale suffix.
- Treat the target slot as authoritative when a reference export exists.
- Prefer preserving the original exported dimensions for replaceable assets.
- For hand-drawn icon sets, keep the function readable at roughly `80-120 px`.
- For tabbar icons, the config examples commonly use `tabbar_size: 28*28` or `30*30`.
- If a slot expects a dark variant, export the `_Dark` version with the same dimensions as the light asset.
- Do not invent a single fixed canvas size for all icons unless the target resource family is known to share one.
- If a resource family has mixed 1x/2x/3x assets, keep their logical proportions consistent.

## Practical Working Range

- Tabbar icons: usually near `28*28` or `30*30` in config terms.
- Small action icons: keep the symbol centered with generous transparent padding.
- Bubble / background / cover assets: size follows the target slot, not the icon rule.
- `@3x` assets: keep the exported pixel dimensions aligned with the target resource family and do not crop away required transparent margins.
- When a filename list includes both normal and `_Dark` or `HL` variants, export both with matched dimensions and alignment.

## What To Document Per Batch

- filename
- target slot
- exported size
- dark variant needed or not
- transparent background verified
