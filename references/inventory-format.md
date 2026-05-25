# Inventory Format

Use a project inventory to define what a package must ship. Do not validate against every filename mentioned in reference docs.

## Required Columns

```text
filename | package path | group | required | status | target size | exported size | alpha required | dark variant | selected variant | art source | source | notes
```

Allowed `required` values:

- `yes`: must be present before release.
- `planned`: intended for this package, must be completed or explicitly downgraded before release.
- `optional`: useful but not required.
- `no`: reference-only, do not validate as required.

Allowed `status` values:

- `done`: hand-drawn, exported, visually reviewed, and included in the package.
- `missing`: not generated yet.
- `placeholder`: temporary diagnostic art; blocks release.
- `blocked`: not shippable yet, with reason in notes.
- `not-applicable`: not used by this package.

Release validation should fail when a row with `required=yes` or `required=planned` has `status` other than `done`, or when the package does not contain that filename.

Allowed `art source` values for final icons:

- `image-generated`: final visible icon subject came from an image generation/art workflow.
- `hand-drawn`: final visible icon subject was manually drawn.
- `edited-from-approved-original`: final icon was edited from the project's own approved original art.

Release validation should fail for final icon rows when `art source` is blank, `script-generated`, `placeholder`, `default-icon`, `emoji`, `text-label`, or any value that means the visible icon subject was made by a primitive script.

## Starter Rows For Complete Character-Led Packs

```text
filename | package path | group | required | status | target size | exported size | alpha required | dark variant | selected variant | source | notes
cover.png | root | package identity | yes | missing | unknown | unknown | no | no | no | image-generated | project | theme preview
icon.png | root | package identity | yes | missing | unknown | unknown | yes | no | no | image-generated | project | package icon
launch.png | root or png/ | launch | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | premium character launch art
default_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | calm page background
main_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | session/home background
contacts_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | contacts background
discover_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | discover background
me_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | me/profile background
chat_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | low-noise chat background
album_bg.png | root or png/ | background | planned | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | album background
tabbar_bg.png | root or png/ | navigation | yes | missing | unknown | unknown | no | yes if target uses it | no | image-generated | target export | tabbar background
topbar_bg.png | root or png/ | navigation | yes | missing | unknown | unknown | no | yes if target uses it | no | image-generated | target export | topbar background
tabbar_main.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | image-generated | target export | chat tab
tabbar_mainHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | image-generated | target export | chat tab selected
tabbar_contacts.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | image-generated | target export | contacts tab
tabbar_contactsHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | image-generated | target export | contacts tab selected
tabbar_discover.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | image-generated | target export | discover tab
tabbar_discoverHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | image-generated | target export | discover tab selected
tabbar_me.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | image-generated | target export | me tab
tabbar_meHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | image-generated | target export | me tab selected
input_bg.png | root or png/ | input | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | input area
input_text_bg.png | root or png/ | input | yes | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | text input
input_voice_bg.png | root or png/ | input | planned | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | voice input
input_search_bg.png | root or png/ | input | planned | missing | unknown | unknown | no | if target uses it | no | image-generated | target export | search input
badge.png | root or png/ | badge | yes | missing | unknown | unknown | yes | if target uses it | no | image-generated | target export | unread badge
badge_smail@3x.png | root or png/ | badge | planned | missing | unknown | unknown | yes | if target uses it | no | image-generated | observed upstream spelling | preserve spelling if target uses it
weixin.png | root or png/ | system session | planned | missing | unknown | unknown | yes | if target uses it | no | image-generated | target export | WeChat session placeholder
wepay.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | if target uses it | no | image-generated | target export | generic pay/service icon
filehelper.png | root or png/ | system session | planned | missing | unknown | unknown | yes | if target uses it | no | image-generated | target export | file helper
icons_filled_red_envelope@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | image-generated | target export | red envelope
transfer_filled@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | image-generated | target export | transfer
pay_filled@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | image-generated | target export | payment
icons_outlined_wallet@3x.png | root or png/ | payment/service | planned | missing | unknown | unknown | yes | yes if target uses it | no | image-generated | target export | wallet
```
