# Plot Block Shot Gate｜剧情块可拍性门

> status: production-main
> owner: skills/story-material-engine/SKILL.md
> applies_to: S2 Plot Block 构建（Target 剧情块）
> counterpart: references/human-retelling-core.md（Source 拆解同构标准）
> 目的: 保证交给 S3 / Story Compose 的剧情块是"可拍的镜头序列"，而不是"心理状态标签序列"，从输入层根治"正文看不出剧情、一眼看不到在讲什么"的问题。

## 0. 为什么需要这道门

正文"看着没那么简单、一眼看不到剧情"，常见根因不在生成引擎，而在剧情块本身：

```text
抽象节点（情绪到顶点 / 心理博弈 / 局势升级 / 遭遇危机）
→ 生成引擎没有具体画面可写
→ 只能用氛围、心理、修辞填充
→ 正文散、慢、看不到事件在跑
```

Human Retelling Core 已经要求拆母本时用"具体 actor / object / action / change"讲清发生了什么；Plot Block Shot Gate 把**同一标准反向应用到 Target 剧情块构建**，保证输出端拿到的是镜头，不是标签。

## 1. 节点即镜头

每个剧情块节点必须写成**一个可拍摄的镜头**，至少包含：

```text
具体人物（谁）
+ 具体处境 / 物件 / 诱因（什么状态、手里有什么、眼前是什么）
+ 具体动作或对白（做了什么 / 说了什么）
+ 具体局势变化（这一下之后，什么变了）
```

合法示例（母本同型）：

```text
带伤的男人靠着城墙，右手握着一张全家福
→ 他路过蛋糕店，想起今天是生日，正要进去
→ 想到孩子的淬体丹钱，转身离开蛋糕店
→ 孩子从冰箱端出蛋糕，齐声喊"爸，生日快乐"
→ 男人闭眼许愿：一家人平平安安
→ 深夜面板弹出，他愣了两秒："金手指！"
```

## 2. 禁词即不合格

以下词**禁止作为剧情节点本身**，只能作为节点之后的解释：

```text
遭遇危机 / 心理博弈 / 局势升级 / 能力觉醒 / 认知变化
身份跃迁 / 完成反杀 / 获得成长 / 情绪到顶点 / 内心挣扎
希望受挫 / 压力加剧 / 守护支点
```

若一个节点删掉后"谁、拿着什么、做了什么、什么变了"说不出来，它就是标签：

```text
PLOT_NODE_IS_LABEL: FAIL
```

## 3. 分镜预检（MANDATORY）

剧情块收束后、交给 S3 前，必须执行一次"分镜预检"：

```text
把 Plot Block 当拍摄脚本逐条过
→ 每条节点能否由一个镜头拍出来？
→ 删掉所有氛围描写和心理描写后，剧情还能不能靠动作+对白+物件讲完整？
→ 能 → PASS；不能 → 回到该节点，补具体 actor/object/action/change
```

预检标准：

```text
SHOT_TEST_CLEAR: PASS
第1条可拍性通过、事件顺序通过、章末终态通过
```

同时检查"有没有完整一段纯氛围/纯心理"：

```text
PARAGRAPH_WITHOUT_ACTION_OR_DIALOGUE
→ 存在且不承重 → FAIL，改成镜头或并入镜头
```

## 4. 情绪只能作为镜头的余波

剧情块可以保留情绪（Chapter Emotional Thread 职责），但情绪必须**由镜头产生、落在镜头之后**，不能独立成节点：

```text
镜头（具体事件）→ 余波（人物感受 / 残留情绪）
```

禁止：

```text
情绪节点（他很自责）→ 回头找事件凑
```

## 5. 与下游的关系

- S3 收到的 Plot Block 应满足：每条节点 = 镜头，可直接作为 Story Compose 的 Target 写作底稿。
- Story Compose 包内流程不变，本门不修改、不重排、不削弱任何生成技能。
- S3 硬复核若发现"首段无人物 / 整段氛围 / 心理段占比过高"，定位回本门（S2 剧情块），补镜头重跑，不在成品上做表面修复。

## 5.1 镜头功能标注（章节肉块的输入保障）

除"事件镜头"外，剧情块必须为每个镜头标注**功能类型**。模拟器文每章必须覆盖的镜头功能（对应 `../references/simulator-novel-production-contract.md` §6.5 肉块）：

```text
EVENT     事件镜头（推进发生了什么）
BURST     爆点镜头（出货/结算/战斗/打脸，慢写）
VOICE     声口镜头（对白/玩梗/同伴互动）
PANEL     面板镜头（系统面板/规则出现，逐条可点评）
BRAIN     推演镜头（主角当场算金手指价值+定规划，≥1 个，≥120字）
HISTORY   身世镜头（共情锚：往昔/伤/念想，≥1 个/章或跨章轮换）
```

硬门：

```text
若本章出现金手指（新能力/新规则/新结算）→ 必须含 BRAIN 镜头（推演块）
每章至少一个 HISTORY 镜头（身世/共情锚，可轮换主题）
面板出现 → PANEL 镜头内必须有逐条点评（不止属性行）
整章无 BRAIN / HISTORY → PLOT_BLOCK_SHOT_GATE: FAIL
```

### 5.2 系统互动硬指标（模拟器文对齐母本）

剧情块必须为每章安排 **≥2 个系统互动镜头**（对应生产规约 §6.2），主线推理章也不得免除：

```text
SYSTEM_1 抽取/抽卡镜头：出货过程（光团/光点/概率/欧非/身体反应）
SYSTEM_2 选择分支镜头：岔路给 2-3 选项 + 主角逐条点评取舍（可含搞笑选项）
SYSTEM_3 模拟光幕镜头：每年事件 + 中途奖励出现（不可纯快进流水）
SYSTEM_4 结算镜头：逐行亮出 + 身体反应六拍 + 盘点（可加结算诗/评价）
SYSTEM_5 系统吐槽镜头：主角对统子说话/抱怨/许愿（"统子你给力点啊！"）
SYSTEM_6 指引任务/面板升级镜头：新功能解锁 + 主角分析新玩法
```

每章剧情块必须标注本章使用哪 2-3 个 SYSTEM 镜头（用镜头编号标在对应行），缺标 = FAIL。

```text
SYSTEM_SCENE_MIN: 2（每章）
PANEL_LINE_FLOOR: 25（每章）
EXCLAMATION_FLOOR: 15（每章）
```

### 5.3 开头/结尾拍型标注（防模板化）

剧情块必须显式标注本章的开头与结尾手法，并对照上一章避免同型（契约见 `../references/simulator-novel-production-contract.md` §4.1/§4.2）：

```text
OPENING_TYPE: OPENING_DIALOGUE | OPENING_EVENT | OPENING_OBJECT
             | OPENING_CONTINUE | OPENING_PANEL | OPENING_THOUGHT
             （不得与上一章相同；纯氛围开场 FAIL）

ENDING_TYPE:  ENDING_HOOK | ENDING_FROZEN | ENDING_LINE
             | ENDING_ACTION | ENDING_AFTERMATH | ENDING_NATURAL | ENDING_BRANCH
             （不得与上一章相同；默认【可模拟人生】面板收尾 FAIL）
```

同时：

```text
系统循环的下一次模拟提示不强制放在章末；可放章中（结算/开启当场），
章末留给剧情的自然落点或任意钩子。
无钩子自然断章合法（母本第4章先例），不构成 FAIL。
```

缺标注或与上章同型 → PLOT_BLOCK_SHOT_GATE: FAIL → 修改拍型后重过门。

同时，剧情块的爆点/情绪镜头必须**外放**（感叹号 + 喊叫式内心），禁止"压住狂喜"式冷静腔（对应生产规约 §6.1）。

## 6. 回执

```text
PLOT_BLOCK_SHOT_GATE: PASS | FAIL
LABEL_NODE_COUNT: 0（目标）
SHOT_TEST_CLEAR: true
PURE_ATMOSPHERE_PARAGRAPH: 0（目标）
```

> Memory line: **剧情块 = 分镜脚本。每个节点都要能拍出来：谁、拿着什么、做什么、什么变了。抽象状态词当节点一律 FAIL，情绪只做镜头余波。这保证正文一眼能看见剧情。**
