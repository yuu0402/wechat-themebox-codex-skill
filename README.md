# WeChat ThemeBox Codex Skill

An installable [Codex](https://openai.com/index/introducing-codex/) skill for designing, building, refining, packaging, and reviewing **original WeChat ThemeBox themes** — from minimal color-only packs (`config.json` + `weui_color_new.xml`) to full DIY packages with PNG/SVG assets.

The skill encodes a complete production workflow (style direction → source color tokens → asset generation → packaging → on-device validation) with hard rules for keeping every asset original. It never copies protected third-party themes, `themebox.dat` files, receipts, or paid assets.

## What it does

- Plans original WeChat theme packages from a named visual direction
- Generates `config.json`, `weui_color_new.xml`, `cover.png`, `icon.png`, and full DIY `png/`/`svg/` asset sets
- Enforces original-art rules: hand-drawn or prompt-generated artwork, transparent alpha channels, no placeholder icons in releases
- Validates packages with bundled Python scripts (structure, alpha, XML/SVG checks, dimension manifests, inventories)
- Produces contact sheets and per-build production inventories
- Treats ThemeBox import feedback and device tests as the source of truth

## Repository layout

```text
SKILL.md                     # the skill: workflow + production rules
agents/openai.yaml           # Codex agents interface definition
references/                  # 20+ reference docs (format safety, design, packaging, QA, case studies)
scripts/
  validate_theme_package.py  # package structure / alpha / XML / SVG validator
  make_contact_sheet.py      # PNG contact-sheet generator
```

## Install

1. Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/yuu0402/wechat-themebox-codex-skill ~/.codex/skills/wechat-themebox
```

2. Reference the skill in your project's `AGENTS.md`:

```markdown
skills/wechat-themebox/SKILL.md
```

3. Ask Codex to make a WeChat theme (for example, *"make a midnight-blue WeChat ThemeBox theme called Night Sail"*). The skill activates automatically for ThemeBox / WeChat theme requests.

## Validation scripts

```bash
# release package: list PNGs and validate structure/alpha
python scripts/validate_theme_package.py dist/ThemeName-DIY.zip --list-png

# flat variant
python scripts/validate_theme_package.py dist/ThemeName-DIY-flat.zip --flat --list-png

# strict full check against an inventory
python scripts/validate_theme_package.py dist/ThemeName-DIY.zip \
  --inventory dist/inventory.md --require-no-placeholder --check-xml --check-svg

# contact sheet for visual QA
python scripts/make_contact_sheet.py dist/ThemeName-DIY/png dist/contact-sheet.png
```

## License and credits

This repository is released under the [MIT License](LICENSE).

Reference material on ThemeBox config behavior and WeChat icon formats is adapted from the public [AidenYang1/ThemeDocs_WeChat_For_Themebox](https://github.com/AidenYang1/ThemeDocs_WeChat_For_Themebox) documentation, used for format compatibility only — never copied artwork.
