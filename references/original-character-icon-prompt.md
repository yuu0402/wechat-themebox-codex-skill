# Original Character Icon Prompt

Use this reference when a WeChat ThemeBox theme needs a full hand-drawn icon set where every icon carries the same original main character identity. The current default character direction is `星蓝萌团`; replace it only when the user gives a different original IP name.

## Character Bible

Before drawing icons, define a compact character bible and keep it stable across the full asset set:

- IP name: `星蓝萌团`
- Identity: original soft sci-fi cute mascot group for a WeChat ThemeBox theme.
- Core shape language: rounded star/cloud silhouettes, soft antenna or ear-like points, tiny paws or mitten hands, chubby compact bodies, friendly dot eyes, simple expressive mouths.
- Palette: star blue, milk white, moon yellow, small coral or mint accents, soft warm shadow. Avoid a single all-blue palette; keep enough warm contrast for daily WeChat use.
- Linework: hand-drawn, soft dark-blue or warm gray outline, never harsh black.
- Texture: clean sticker-like flat illustration with subtle paper grain or gentle brush edges.
- Reusable character elements: star mark, blue tuft, round ears/antenna, tiny paws, crescent or sparkle accessory, small scarf or badge.
- Do not imitate Disney, Stitch, Sanrio, Pokemon, Line Friends, or any existing protected character. Keep anatomy, silhouette, face, colors, and accessories original.

## Codex Prompt

Paste this to Codex when asking it to produce the theme assets:

```text
你要为 WeChat ThemeBox 制作一套完整的原创微信主题图标资源。主 IP 是“星蓝萌团”，必须是原创角色，不要模仿或复刻任何现有 IP、影视/游戏/动漫角色、品牌吉祥物或参考图里的具体角色。

目标：
1. 根据 ThemeBox 命名规则生成图标资源，优先读取 skill 的 references/asset-naming.md 和 references/design-guidelines.md。
2. 每一个图标都要手绘，不要用系统默认图标换色。
3. 每一个图标都必须带有“星蓝萌团”的主 IP 形象元素，但不能牺牲图标语义和小尺寸可读性。
4. 输出透明背景 PNG/SVG 源资产，按 ThemeBox 文件名保存；需要 dark mode 的资源同时输出 _Dark 版本。

星蓝萌团角色设定：
- 原创软萌星空小团子/小队，不是任何现有角色的同人。
- 形体：圆润小身体，星星或云朵轮廓，短小耳朵/触角，圆手或小爪。
- 脸部：点状眼睛，简洁微笑或小表情，表情可随图标语义变化。
- 标识：星蓝色主色、奶白肚皮、月黄色小星标、少量薄荷绿或珊瑚粉点缀。
- 线条：柔软手绘线，深蓝灰或暖灰描边，不用纯黑粗线。
- 气质：治愈、干净、轻科幻、适合长期微信日常使用。

图标生成规则：
- 每个图标先保留功能物体的清晰轮廓，再加入星蓝萌团元素。
- 主 IP 元素可以是：角色抱着物体、角色头部变成图标主体、星星徽章、耳朵/触角、小爪、尾巴、围巾、发光星尘。
- 不允许只在角落贴一个无关小头像；角色元素要和图标功能结合。
- 不允许每张都画成同一个头像；要按功能做变化。
- 小尺寸优先：80-120 px 仍能看出功能，细节不能糊。
- 图标集合必须统一：相同描边粗细、阴影方向、圆角、颜色饱和度、留白比例。
- 不要文字、不要水印、不要复杂背景、不要照片质感、不要 3D 渲染、不要玻璃拟态。

第一批优先生成并审查：
- tabbar_main.png / tabbar_mainHL.png：聊天气泡 + 星蓝萌团小脸或小爪。
- tabbar_contacts.png / tabbar_contactsHL.png：两个星蓝萌团小头像或小队。
- tabbar_discover.png / tabbar_discoverHL.png：星球/罗盘 + 星蓝萌团触角或星标。
- tabbar_me.png / tabbar_meHL.png：星蓝萌团主头像，选中态更饱满。
- search_filled@3x.png：放大镜由星环构成，角色小爪扶住镜框。
- scan_filled@3x.png：扫码框 + 星蓝萌团探头。
- camera_filled@3x.png：相机机身 + 星标镜头 + 小耳朵。
- icons_filled_album@3x.png：相册叠页 + 星蓝萌团贴纸角标。
- icons_filled_red_envelope@3x.png：红包 + 星星封口 + 小爪递出。
- transfer_filled@3x.png：转账箭头 + 星轨 + 角色小手。
- favorites_filled@3x.png：收藏星星直接采用星蓝萌团星标。
- gear_regular@3x.png：齿轮 + 角色耳朵/星芯。
- icons_filled_qr_code@3x.png：二维码块保持清晰，角上融入星蓝萌团脸部。
- voice_circle_filled@3x.png：声波 + 星星嘴型。
- video_filled@3x.png：摄像机 + 小星天线。

每个图标输出前先写一行设计说明，格式：
filename | 功能语义 | 星蓝萌团元素 | 色彩/状态 | 是否需要 Dark 版

验收标准：
- 文件名完全匹配 ThemeBox 清单。
- 每个图标一眼能看出功能。
- 每个图标都有星蓝萌团元素，并且不是简单角标贴图。
- 全套图标看起来属于同一套手绘主题。
- 没有现有 IP 的可识别特征。
- 透明背景边缘干净，导出尺寸和 @3x 后缀符合目标文件。
```

## Single Icon Prompt Template

Use this when generating assets one at a time:

```text
Create one original WeChat ThemeBox icon for "{filename}". Function: {function}. Style: hand-drawn soft sticker icon, transparent background, readable at 80-120 px. Main IP: "星蓝萌团", an original star-blue cute mascot group with rounded star/cloud body, small ears or antenna, tiny paws, milk-white belly, moon-yellow star mark, blue-gray soft outline. Integrate the mascot into the function: {mascot integration}. Keep the functional symbol clear first, then add mascot identity. Palette: star blue, milk white, moon yellow, small mint/coral accents, gentle warm shadow. No text, no watermark, no complex background, no 3D, no photorealism, no black outline, no copied existing IP, no Disney/Stitch/Sanrio/Pokemon/Line Friends traits.
```

## Production Table

For every batch, maintain a table with these columns:

```text
filename | function | mascot element | selected/dark state | prompt | exported | checked
```

Do not mark a file checked until it has been visually reviewed for small-size clarity, transparent edges, naming accuracy, and IP originality.
