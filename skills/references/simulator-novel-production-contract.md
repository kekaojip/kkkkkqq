# Simulator Novel Production Contract｜模拟器文生产规约

> status: production-main
> role: 本书系工作流的专用生产规约（模拟器文 / 系统流 · 番茄向）
> applies_to: S1 / S2 / S3 全链（Story Compose 黑盒内部不动，本规约只在上游输入与硬复核生效）
> authority: TARGET 真值 > 本规约 > 泛网文默认

## 0. 为什么有这个文件

模拟器文需要面板、选择、结果、现实兑现与强声口，但这些都必须服务于**剧情显形**。正式生产不再用面板行数、感叹号数量、系统场景数量、对白比例、BRAIN/HISTORY 字数等配额驱动正文。

本规约的最高目标只有三层：

```text
BLOCK：这一大段故事正在兑现什么
SCAN_COORDINATES：这一章真正发生什么
SCAN_STORY：读者扫过去能不能看见这些事情
```

> 数量指标退役 ≠ 质量底线降低。质量由剧情推进、首读清晰、自然停点、Story Compose 原包与 story-deslop 退化检测共同兜底。

## 1. 人物声口契约

主角保持本书已批准的模拟器文声口：口语化、会吐槽、会算收益、会对系统作即时反应。声口必须依附当前事件，不得为了“像网文”单独插入段子或宣言。

```text
VOICE_PLAYFUL: 口语化、会玩梗，密度由场景自然决定
VOICE_EXPRESSIVE: 重大情绪不能只停留在抽象心理说明
VOICE_META: 对系统玩法有认知，但只在当前事件真正需要时出现
VOICE_COMRADE: 已建立的同伴关系可承担信息、冲突、关系与行动，不要求每章固定出场或固定对白比例
```

禁止：

```text
为了声口硬塞感叹号
为了“目标感”每章强制宣言
为了“活人感”无功能互损
只有分析没有行动的准备型长段
```

## 2. BLOCK 层｜章节之上的大段结构

BLOCK 用来描述连续若干章共同兑现的故事承诺。它是**结构状态，不是章数配额**。

### 2.1 CURRENT_BLOCK 字段

```text
BLOCK_ID
BLOCK_TYPE: SIM | REALITY | MIX
BLOCK_PROMISE
BLOCK_ENTRY_EVENT
BLOCK_EXIT_CONDITION
BLOCK_PROGRESS
EXIT_CONDITION_REVISION_REASON: optional
```

定义：

- `BLOCK_TYPE` 只描述当前大块主要发生在模拟、现实或两者交界，不决定开头/结尾形式。
- `BLOCK_PROMISE` 写这段故事最终要兑现的核心结果。
- `BLOCK_ENTRY_EVENT` 必须是已经发生的 Canon/已批准事件。
- `BLOCK_EXIT_CONDITION` 必须写成可判定事件，例如“第二次模拟结算完成”，不得写“节奏差不多了”。
- `BLOCK_PROGRESS` 记录当前已经推进到哪。

### 2.2 BLOCK 纪律

```text
BLOCK_CHAPTER_QUOTA: forbidden
BLOCK_TYPE_OPENING_TEMPLATE: forbidden
BLOCK_TYPE_ENDING_TEMPLATE: forbidden
BLOCK_INTERNAL_SAME_FORM: allowed
```

母本块长度、SIM/REALITY/MIX 占比、连续章数只属于知识库观察值，统一视为：

```text
DESCRIPTIVE_REFERENCE_ONLY: true
```

不得把“中位多少章”“现实块通常几章”转换成生产硬门。

### 2.3 EXIT_CONDITION 可修订但必须留痕

EXIT_CONDITION 不是预言，也不是不可修改的契约锁。S2 在新剧情事实出现后可以细化或修订，但必须同时记录：

```text
EXIT_CONDITION_REVISION_REASON: 因为什么新剧情事实调整
```

每章规划前，S2 读取一次 CURRENT_BLOCK：

```text
EXIT 已达成 → 规划自然转场
EXIT 未达成 → 继续当前块内推进
```

这不是新增作者步骤，也不是新的独立 Gate。

## 3. SCAN_COORDINATES｜章节剧情坐标

每章剧情块必须先列出真正发生的剧情坐标。坐标不设固定数量，只要求足以讲清本章骨架。

唯一判定句：

> **这个节点发生之后，是否产生了新的事实、新信息、新决定或新结果？**

能回答“是”才算坐标。

合法：

```text
顾川得知药徒留用能退出试药册
顾川决定参加留用考核
周小满考核通过，身份转为药徒帮工
顾川《养血法》入门，成为炼血境一重
```

不合法作为独立坐标：

```text
顾川思考三条路线
顾川回忆过去八个月
顾川分析未来价值
顾川感到压力很大
```

思考、回忆、解释、情绪可以存在，但只能依附于已经发生的剧情坐标，不能拿来替代坐标。

## 4. 正文承载顺序｜事件先行，解释后挂

默认组织顺序：

```text
发生 / 对白 / 面板变化
→ 主角即时反应
→ 当前决定真正需要的最短解释
→ 下一件事
```

禁止长链：

```text
规则解释 → 回忆 → 分析 → 计划 → 再分析 → 最后才行动
```

主角思考只写到足以支撑当前决定为止。深度情绪或回忆段可以出现，但必须由当前事件触发，且不能让剧情长期停摆。

### 4.1 首屏原则

不规定 150 字、200 字或“第二镜头”之类数字门。

唯一要求：

> **第一个手机屏内，读者能抓到当前正在发生的事，或者主角眼下明确要做什么。**

纯环境、纯氛围、纯说明书式开场不承担剧情时，应回 S2/S3 重组。

## 5. 系统面板 = 剧情装置

面板分两类：

```text
EVENT_PANEL：选择 / 获得 / 失去 / 突破 / 死亡 / 结算 / 身份变化 / 新任务
LOCATOR_PANEL：时间 / 当前身份 / 剩余次数 / 当前必要定位
```

规则：

- EVENT_PANEL 应承担一个真实剧情变化。
- LOCATOR_PANEL 可以不改变剧情，但必须短，只保留理解接下来事件所需的信息。
- 不因章节属于 SIM / REALITY / MIX 而规定面板数量。
- 不要求面板必须逐条点评；只解释会影响当前决定的关键项。

删减判断：

> **删掉这块面板后，是否会损失剧情变化或必要定位？**

两者都不会 → 删掉或压缩。

## 6. 开头与结尾｜不再按章节类型换壳

BLOCK_TYPE 不拥有开头/结尾模板解释权。

开头只要求：

```text
快速进入当前事情或明确目标
禁止无承重的纯氛围铺垫
```

结尾只要求：

```text
在当前有效剧情的第一个自然闭合点停止
禁止为了“像断章”额外补总结
禁止预告下一章
禁止剧情已经闭合后再补一层重复系统确认
```

任何 BLOCK 都允许剧情真正需要的系统面板。禁止的是**重复确认、总结和尾巴**，不是“REALITY 不能有面板”。

## 7. 情绪可见｜EMOTION_VISIBLE

只检查 S2 已经存在的重大情绪节点；不要求每章必须有重大情绪节点，不设数量配额。

重大情绪优先通过：

```text
明确决定 > 对白 > 动作 > 身体反应
```

允许只靠明确决定完成可见化。例如：顾川当场决定今晚先帮周小满补考，这本身就能承载护短与急切。

身体反应不是默认手段。禁止同一情绪节点叠加“瞳孔缩、呼吸停、手指颤、喉结动、背后出汗”等模板化表演。

禁止只有：

```text
“他很激动”
“他压住狂喜”
“他心情复杂”
```

而当前剧情没有任何可见决定、对白或行动变化。

## 8. 爆点｜不再按拍数生产

突破、重大获得、重大打脸、死亡级事件属于“大爆点”，应给足事件因果与现场确认，让读者看见“发生 → 结果成立”。

`≥5 拍身体反应` 退役为历史技法参考，不再 PASS/FAIL。

爆点不允许一句摘要带过，但也不要求按瞳孔/呼吸/指节模板拆拍。需要放慢多少，由事件本身决定。

## 9. 模拟执行｜不能空转，但不设场景数量

模拟块不能只有年份/日期快进。至少必须有能改变 BLOCK_PROGRESS 或本章 SCAN_COORDINATES 的真实节点，例如：

```text
选择造成路线变化
危机造成新结果
训练失败暴露门槛
获得情报改变下一步
突破改变身份或能力
```

不要求“每章 ≥2 系统场景”。如果一章只有一次关键系统互动但剧情明显推进，完全合法。

## 10. 篇幅管理

```text
CHAPTER_HANZI_TARGET: 1900-2500
CHAPTER_HANZI_FLOOR: 1500
LENGTH_REPAIR_WITHIN_TARGET_RANGE: forbidden
```

1900–2500 整个区间均为正常 PASS，不因字数触发删减或补写。

低于 1500 时先检查是不是剧情坐标本身太薄；如果剧情已经完整，不得靠 BRAIN/HISTORY/PANEL 等退役肉块机械注水。

## 11. 已退役的生产 KPI

以下不得参与当前生产 PASS/FAIL：

```text
BRAIN 字数下限
HISTORY 字数下限
PANEL_LINES 下限/范围
SYSTEM_SCENES 数量下限
EXCLAMATION 数量下限/范围
DIALOGUE 百分比目标
BURST 五拍硬门
每章必须宣言
按 SIM/REALITY/MIX 强制开头/结尾形态
每段必须塞动作/对白的机械密度门
```

知识库可以保留母本统计值与旧技法作为观察和参考，但必须标明非配额。

## 12. S3 表现层最终硬检查

S3 的正文表现层只保留五个硬检查：

```text
CLEAR_FIRST_READ
ENDPOINT_STOP
CHAPTER_LENGTH
BLOCK_PROGRESS
SCAN_STORY
```

`EMOTION_VISIBLE` 是 SCAN_STORY 的补充可见性原则，不单独扩成新的数字 Gate。

Canon、POV、知识边界、Source Fact Leak、Source Distinctive Expression Leak、后台元数据等 A-I 安全门继续原样有效。

## Memory line

> **BLOCK 定“这一大段兑现什么”；SCAN_COORDINATES 定“这一章发生什么”；SCAN_STORY 定“读者扫过去看不看得见”。旧数字 KPI 退役，Story Compose 原包不动。**