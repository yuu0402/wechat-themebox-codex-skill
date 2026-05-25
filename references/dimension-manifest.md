# Dimension Manifest

Use this file as the project-specific observed-size record for a theme. Do not invent sizes from memory when a real export or device test is available.

## Columns

- filename
- slot or function
- expected size
- observed size
- source of truth
- alpha required
- dark variant required
- notes

## Priority Rules

- If a filename has an observed original export, use that size.
- If only a slot size is known, record the slot size and mark the filename as unverified.
- If the project needs a tabbar icon size before device testing, use the `tabbar_size` config value as the working reference.
- Keep one row per file, not one row per family, when the file is expected to ship.

