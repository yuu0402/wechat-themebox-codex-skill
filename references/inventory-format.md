# Inventory Format

Use a project inventory to define what a package must ship. Do not validate against every filename mentioned in reference docs.

## Required Columns

```text
filename | package path | group | required | status | target size | exported size | alpha required | dark variant | selected variant | source | notes
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

## Starter Rows For Complete Character-Led Packs

```text
filename | package path | group | required | status | target size | exported size | alpha required | dark variant | selected variant | source | notes
cover.png | root | package identity | yes | missing | unknown | unknown | no | no | no | project | theme preview
icon.png | root | package identity | yes | missing | unknown | unknown | yes | no | no | project | package icon
launch.png | root or png/ | launch | yes | missing | unknown | unknown | no | if target uses it | no | target export | premium character launch art
default_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | calm page background
main_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | session/home background
contacts_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | contacts background
discover_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | discover background
me_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | me/profile background
chat_bg.png | root or png/ | background | yes | missing | unknown | unknown | no | if target uses it | no | target export | low-noise chat background
album_bg.png | root or png/ | background | planned | missing | unknown | unknown | no | if target uses it | no | target export | album background
tabbar_bg.png | root or png/ | navigation | yes | missing | unknown | unknown | no | yes if target uses it | no | target export | tabbar background
topbar_bg.png | root or png/ | navigation | yes | missing | unknown | unknown | no | yes if target uses it | no | target export | topbar background
tabbar_main.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | target export | chat tab
tabbar_mainHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | target export | chat tab selected
tabbar_contacts.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | target export | contacts tab
tabbar_contactsHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | target export | contacts tab selected
tabbar_discover.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | target export | discover tab
tabbar_discoverHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | target export | discover tab selected
tabbar_me.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | normal | target export | me tab
tabbar_meHL.png | root or png/ | tabbar icon | yes | missing | unknown | unknown | yes | no | selected | target export | me tab selected
input_bg.png | root or png/ | input | yes | missing | unknown | unknown | no | if target uses it | no | target export | input area
input_text_bg.png | root or png/ | input | yes | missing | unknown | unknown | no | if target uses it | no | target export | text input
input_voice_bg.png | root or png/ | input | planned | missing | unknown | unknown | no | if target uses it | no | target export | voice input
input_search_bg.png | root or png/ | input | planned | missing | unknown | unknown | no | if target uses it | no | target export | search input
badge.png | root or png/ | badge | yes | missing | unknown | unknown | yes | if target uses it | no | target export | unread badge
badge_smail@3x.png | root or png/ | badge | planned | missing | unknown | unknown | yes | if target uses it | no | observed upstream spelling | preserve spelling if target uses it
weixin.png | root or png/ | system session | planned | missing | unknown | unknown | yes | if target uses it | no | target export | WeChat session placeholder
wepay.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | if target uses it | no | target export | generic pay/service icon
filehelper.png | root or png/ | system session | planned | missing | unknown | unknown | yes | if target uses it | no | target export | file helper
icons_filled_red_envelope@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | target export | red envelope
transfer_filled@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | target export | transfer
pay_filled@3x.png | root or png/ | payment/service | yes | missing | unknown | unknown | yes | yes if target uses it | no | target export | payment
icons_outlined_wallet@3x.png | root or png/ | payment/service | planned | missing | unknown | unknown | yes | yes if target uses it | no | target export | wallet
```

