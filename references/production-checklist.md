# WeChat ThemeBox Production Checklist

Use this checklist before building, reviewing, packaging, or handing off a ThemeBox-compatible WeChat theme.

## Scope And Source Control

- Work from source files, not hand-edited `dist` output.
- Keep a reproducible builder for `config.json`, `weui_color_new.xml`, generated assets, and zip packages.
- Keep project-specific character names, user names, private references, tokens, receipts, and subscription/account data out of this public skill.
- Record assumptions in the project notes when a ThemeBox version or device import behavior is uncertain.
- Do not silently skip requested resource categories. If a full pack is requested, produce an inventory table and mark each file as planned, generated, checked, or blocked.
- Full-pack means full-pack: payment, wallet, red-packet, transfer, services, launch art, wallpapers, topbar/tabbar, backgrounds, bubbles, and common action icons must be inventoried and either completed or explicitly blocked with a reason.

## IP And Asset Safety

- Use original artwork only.
- Do not imitate, trace, redraw, recolor, or closely transform protected characters, brand mascots, film/game/anime characters, celebrities, paid theme assets, or another creator's theme.
- Do not copy another author's `themebox.dat`, `wxid_*.receipt`, paid media, or extracted protected package assets into a release.
- Samples may be used only for format evidence: folder shape, filenames, dimensions, and replaceable slots.
- If a user provides a reference image with a recognizable IP, convert it into a generic original direction instead of recreating the character.
- Final visual assets for a character-led theme must be hand-drawn original art. Do not ship script-drawn primitive placeholder icons, default system icons, emoji substitutions, text labels, or auto-generated geometric filler as finished assets.

## Package Structure

- Minimum visible package should include `config.json`, `weui_color_new.xml`, `cover.png`, and `icon.png`.
- Broader DIY packages may include `png/`, `svg/`, `skin/`, `assets/`, optional `weui_color.xml`, and optional `color.css` when legacy compatibility is needed.
- Keep a normal folder-root zip and, when import behavior is unknown, also build a documented flat-root variant.
- Do not include `__MACOSX`, `.DS_Store`, editor temp files, cache folders, raw prompt dumps, or private notes in release zips.
- Verify file paths use forward-compatible ASCII-safe names where ThemeBox expects exact resource names.
- Folder-root release zips must expand to exactly one top-level theme folder.
- Flat-root zips must be named and documented as test/import variants, not the default release.
- Release zips must not include `src/`, `scripts/`, `notes/`, `dist/`, `tmp/`, `node_modules/`, `.git/`, drafts, rough generated placeholders, raw references, or working files.
- If `themebox.dat` is present, it must come from the user's own ThemeBox/custom export flow and be documented; otherwise it should be intentionally absent.
- Resource folders must not duplicate the same asset in multiple places unless the target ThemeBox version requires both paths and the inventory says so.

## Naming And Inventory

- Read `asset-naming.md` before mapping image resources.
- Use exact filenames. Case, underscores, hyphens, spelling, suffixes, and extension all matter.
- Preserve `@2x`, `@3x`, `_Dark`, and selected-state suffixes such as `HL` when required.
- Provide both normal and selected states for tabbar icons when listed.
- Provide dark-mode variants when the resource family or current package uses them.
- Do not invent new filenames for WeChat replacement slots unless the builder documents them as project-only source files.
- Maintain a production table with: `filename | function | slot | light/dark/selected state | target size | exported size | alpha checked | generated | device checked | notes`.
- If a file is not drawn yet, mark it `missing` or `placeholder`; never mark it done because a script created a rough stand-in.

## Size And Export Rules

- Read `icon-size-guidelines.md` before exporting icons.
- Match the target slot's known or exported original dimensions.
- Do not use one universal canvas for all resources unless the resource family is known to share one.
- Keep icons readable at small size, especially around `80-120 px`.
- Tabbar config examples commonly use `tabbar_size` values around `28*28` or `30*30`; confirm with the target project and device tests.
- Keep light and dark variants the same dimensions.
- Keep `@3x` files aligned with the target resource family and preserve transparent margins.
- For background, cover, panel, bubble, and surface resources, use the target slot dimensions rather than icon sizing rules.
- Final icons must not be cropped screenshots or partial cutouts. They must be complete independent symbols with enough transparent padding for ThemeBox/WeChat scaling.

## Transparency And Visual Quality

- Icon-style resources must have transparent backgrounds and a real alpha channel.
- Do not export icons on white squares, colored blocks, rounded-card canvases, opaque scene backgrounds, or accidental matte backgrounds.
- Opaque or semi-opaque backgrounds are allowed only for resources that are actually backgrounds, panels, bubbles, tiles, covers, or surfaces.
- Sticker-like internal shapes are allowed only when they are part of the drawn object; the outer canvas still must stay transparent.
- Check edges at 1x and small preview size; remove halos, white fringes, jagged cutouts, and muddy shadows.
- Keep enough internal padding so icons do not clip when ThemeBox or WeChat scales them.
- Keep the function recognizable before adding decoration.
- Keep the set visually unified: outline weight, shadow direction, saturation, texture, corner language, and character motif should match.

## Original Character Icon Sets

- Read `original-character-icon-prompt.md` before generating mascot or main-IP icon sets.
- Define a character bible first, then reuse it consistently.
- Every icon should include an integrated character element, but it does not need to be the full character.
- Character elements may come from silhouette, ears, horns, tail, hands, paws, accessory, pattern, expression language, gesture, pose, light effect, particles, trails, or an abstract transformation of the character into the icon subject.
- Do not paste the same small character head in every corner.
- Vary integration by function while keeping the same identity.
- Avoid protected-character traits in anatomy, silhouette, color blocking, face, accessories, and pose language.
- For character-led themes, `cover.png`, `icon.png`, `launch.png`, page wallpapers, and chat backgrounds must be designed from the character bible, not left as plain generated gradients unless the user explicitly asks for minimalism.

## Color And Config

- Generate `config.json` and color XML from source tokens.
- Keep light and dark color pairs for major WeUI families.
- Preserve the target project's `#RRGGBB` versus `RRGGBB` convention for config colors unless device tests prove otherwise.
- Use `weui_color_new.xml` as the modern color map. Generate `weui_color.xml` or `color.css` only when the target workflow needs legacy compatibility.
- Review contrast for text, badges, chat bubbles, input areas, top bars, tab bars, and menus.
- Do not let decorative palette choices reduce readability in daily WeChat use.
- Treat top navigation and chat navigation as separate QA surfaces. A theme is not ready if topbar resources or nav text colors are unreadable, mismatched, or visibly broken in light/dark mode.

## High-Impact Assets To Cover First

- Cover and package icon: `cover.png`, `icon.png`.
- Page backgrounds: `default_bg.png`, `main_bg.png`, `contacts_bg.png`, `discover_bg.png`, `me_bg.png`, `chat_bg.png`, `album_bg.png`.
- Navigation and bars: `tabbar_bg.png`, `topbar_bg.png`, tabbar normal and selected icons.
- Top/chat navigation: `topbar_bg.png`, `topbar_bg_Dark.png`, `chat_topbar_bg.png`, `chat_topbar_bg_Dark.png` when supported by the target inventory.
- Chat/input surfaces: `input_bg.png`, `input_text_bg.png`, `input_voice_bg.png`, `input_search_bg.png`.
- Badges and message indicators: `badge.png`, `badge_smail@3x.png`, message tips when present.
- Common avatars and system sessions: `weixin.png`, `wepay.png`, `notification_messages.png`, `filehelper.png`, `qqmail.png`, brand/session placeholders.
- Common action icons: search, scan, camera, album, file, download, share/forward, delete, copy, settings, QR code, voice, video, favorites, red packet, transfer, wallet/payment-related icons where present in the filename list.
- Payment and services: cover all names matched by `payment-service-assets.md`; do not skip them because the image tool rejected a direct payment prompt.

## Build And Validation

- Run the project's build command before packaging.
- Parse or lint generated JSON and XML.
- Inspect the zip contents and root layout.
- Verify required files exist and paths are exactly named.
- Verify the archive root matches the chosen layout contract from `format-and-safety.md` and `build-workflow.md`.
- Verify PNG files open, have expected dimensions, and icon resources preserve alpha.
- Verify final visual assets are hand-drawn original assets, not script placeholders.
- Verify SVG files, if used, are valid and contain no external references.
- Verify no protected sample assets, receipts, private files, or raw user references are shipped.
- Device-test import through ThemeBox when possible. Treat ThemeBox import feedback as the source of truth.
- Record missing filenames, wrong dimensions, import failures, dark-mode mismatches, and visual defects, then update the builder rather than manually patching the package.
- Review topbar/chat topbar, launch screen, wallpapers/backgrounds, and payment/service screens before handoff for full packs.

## Handoff Requirements

- Provide the package path and, if built, the flat-root package path.
- Provide the inventory/check table or its project path.
- State what was validated locally.
- State what still requires device testing.
- State any known unsupported or unresolved ThemeBox behavior, especially `themebox.dat` requirements.
