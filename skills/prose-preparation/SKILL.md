---
name: chapter-prose-writer
description: "S3 OWNER. Prepare approved Target truth, safe continuity and verified donor Source Shadow, then invoke the complete Story Compose package unchanged; hard-revalidate final prose only."
---

# Chapter Prose Writer v6.1｜Source Shadow + Story Compose Black Box

> status: production-main
> top_level_stage: S3
> owns: CURRENT CHAPTER PROSE ORCHESTRATION / TRUTH BOUNDARY
> primary_route: `routes/s3-source-shadow.md`
> source_runtime: `references/source-shadow-runtime.md`
> source_acquisition: `../references/source-corpus-acquisition.md`
> source_fidelity: `references/single-prose-source-fidelity.md`
> prose_composer: `../story-compose/SKILL.md`
> integration_contract: `references/prose-writer-integration.md`
> emotional_causality: `../references/emotional-causality-contract.md`

## 0. First principle

S3 负责“把已经批准的故事、连续性和真实母本参考安全交给成文器”，不负责另造一套正文写法。

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY / CANON
+ CURRENT BLOCK / SCAN COORDINATES
+ INHERITED DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ SOURCE SHADOW REFERENCE PACKET
→ COMPLETE STORY COMPOSE PACKAGE
→ FINAL COMPOSED PROSE
→ HARD REVALIDATION ONLY
→ TARGET PROSE CANDIDATE
```

> **Source Shadow 负责真实参考；Story Compose 原包负责完整成文流程。S3 不拆包、不摘要替代、不在包后追加第二套 humanizer。**

## 1. Admission

Required：

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: known
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CURRENT_CHAPTER_PROSE_COMPLETE: false
CHAPTER_EMOTIONAL_THREAD: approved when required
CURRENT_BLOCK: readable
SCAN_COORDINATES: present in current Plot Block
```

必须读取 safe continuity / Canon、author locks、CURRENT_EMOTIONAL_RESIDUE when relevant、CURRENT_BLOCK、SOURCE_IDENTITY / mapped donor range、SOURCE_DWELL_WEIGHT when provided。

上游缺失则返回 owning stage，不让 Story Compose 自行补剧情。

## 2. Authority boundary

```text
PLOT BLOCK = what happens / order / causality / endpoint / dwell / scan coordinates
CURRENT BLOCK = what the larger run is currently paying off
CHARACTER BLOCK = who the person is / wants / fears / reacts
EMOTIONAL THREAD = emotional residue through approved events
CONTINUITY = already true facts / rules / relations / knowledge
SOURCE SHADOW = verified exact reference windows + source isolation
STORY COMPOSE = prose realization and its package-owned internal checks/repairs
S3 POST COMPOSE = hard truth + reader-visible story revalidation only
```

权威顺序：

```text
TARGET CANON / APPROVED STORY
> CURRENT BLOCK / SCAN COORDINATES
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> STORY COMPOSE EXPRESSION WITHIN APPROVED BOUNDARIES
> VERIFIED SOURCE WORDING
```

## 3. Mandatory source acquisition

每章继续服从 `../references/source-corpus-acquisition.md`：

```text
S2 mapped donor position
→ VERIFIED SAME-POSITION SOURCE BODY
```

不得拿 Plot 摘要、聊天记忆或模型记忆冒充母本正文。取得失败且合法修复仍失败：STOP S3，不切旧引擎。

## 4. Source Shadow

唯一正式 route：`routes/s3-source-shadow.md`。

按自然连续事件划 Target windows，并为适用位置选择 verified homolog source windows。Source 可以给普通词、常见短语、对白接法、信息密度和局部呼吸参考，但不能把专属事实、独特比喻、桥段、动作序列或识别性表达移植进 Target。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

无适用局部参考时记录 `NO_APPLICABLE_LOCAL_REFERENCE`，不硬套，也不伪造。

## 5. Story Compose production preflight

调用前必须确认以下正式依赖存在并可运行：

```text
skills/story-compose/SKILL.md
skills/story-compose/scripts/pipeline.sh
skills/novel-prose-writer-zh/SKILL.md
skills/novel-prose-writer-zh/references/INPUT_ADAPTER.md
skills/novel-prose-writer-zh/references/WRITE_CORE.md
skills/human-writing-l2/SKILL.md
skills/human-writing-l2/references/l2-core.md
skills/human-writing-l2/references/web-fiction.md
skills/human-writing-l2/references/positive-writing.md
skills/story-deslop/SKILL.md
skills/story-deslop/scripts/check-ai-patterns.js
skills/story-deslop/scripts/check-degeneration.js
skills/story-deslop/scripts/normalize-punctuation.js
Node.js runtime when Phase 2 is executed
```

若缺失：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact dependency
→ STOP S3
```

正式生产不允许 Story Compose 使用独立模式的降级路径。

## 6. Production input adapter

执行 `references/prose-writer-integration.md`。

必须把已批准 Plot / Character / Emotional Thread、safe continuity、POV/知识边界、CURRENT_BLOCK、SCAN_COORDINATES、Dwell、停点和 Source Shadow 真实参考原样保留到足以执行的粒度。

分成两类权限：

- TARGET = 必须遵守；
- SOURCE = 仅供表达参考。

通用网文写法只在不改变批准事实时生效：

```text
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

生产禁止：新增事件、事实、人物动机、世界规则、关系、能力、未批准 POV、提前揭露、改变事件顺序、改变章末终态。

当前生产规约已经退役的 KPI 不得从旧剧情块或旧 packet 重新激活：

```text
BRAIN / HISTORY 字数下限
PANEL_LINES 数量/区间
SYSTEM_SCENES 数量下限
EXCLAMATION 数量/区间
DIALOGUE 百分比目标
BURST 五拍硬门
每章强制宣言
按 SIM/REALITY/MIX 强制开结尾形态
```

## 7. Complete Story Compose invocation

正式成文只有一个入口：

`../story-compose/SKILL.md`

```text
STORY_COMPOSE_PACKAGE_INTERNAL_MUTATION: FORBIDDEN
STORY_COMPOSE_BYPASS_IN_PRODUCTION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION: FORBIDDEN
```

S3 不重新定义 Story Compose 内部 Phase 顺序，不单独调用底层三个技能来拼另一条路线，也不在它之后加 Human Grain。

## 8. Dwell / POV / emotional continuity

严格继承上游：

```text
EXPAND | NORMAL | BRIDGE_FAST
VIEWPOINT_EXPERIENCE_CONTINUITY: required
EVENT_NODE_RESET: forbidden
EMOTIONAL_RESIDUE_CONTINUES: required
WRITER_DWELL_UPGRADE_AUTHORITY: false
```

Story Compose 负责正文怎么落，但没有升级 Dwell 或重写批准剧情的权限。

## 9. Post-compose hard validation

Story Compose 返回最终正文后，只检查：

```text
A OUTPUT COMPLETENESS / ENDPOINT
B PROSE INPUT FIREWALL
C TARGET STORY TRUTH / EVENT ORDER
D CHARACTER / EMOTIONAL CONTINUITY
E POV / KNOWLEDGE BOUNDARY
F NEW FACT INTRODUCTION = 0
G SOURCE FACT LEAK = 0
H SOURCE DISTINCTIVE EXPRESSION LEAK = 0
I BACKSTAGE METADATA LEAK = 0
J READER-VISIBLE STORY QUALITY
```

A-I 为安全/真值门，继续原样有效。J 表现层不再使用旧 J1-J14 数量型检查。

### 9.1 J 表现层：只保留 5 个硬检查

```text
J_CLEAR_FIRST_READ
J_ENDPOINT_STOP
J_CHAPTER_LENGTH
J_BLOCK_PROGRESS
J_SCAN_STORY
```

#### J_CLEAR_FIRST_READ

初次阅读即可跟上事件顺序，不需要倒回去研究“作者到底在解释什么”。普通句直陈优先；修辞、心理、面板都不能挡住当前发生的事情。

FAIL ownership：

- 输入本身抽象/坐标不足 → 返回 S2 Plot Block；
- 输入清楚但正文表达打结 → 报具体病灶，交 Story Compose 原包允许的局部修复流程；禁止 S3 自己全文润色。

#### J_ENDPOINT_STOP

必须停在批准的自然闭合点。禁止：

```text
越过 Target endpoint
结尾追加总结
预告下一章
当前剧情已闭合后再补重复系统确认
```

系统面板能否出现在章尾，只取决于它是不是当前真实剧情变化，不由 BLOCK_TYPE 决定。

#### J_CHAPTER_LENGTH

```text
正文区汉字正常目标：1900-2500
硬底线：1500
1900-2500 内：PASS，不因字数触发删减/补写
```

低于 1500 时先检查 Plot Block 是否缺真正剧情坐标。不得为了过长度门恢复 BRAIN/HISTORY/PANEL 等退役肉块注水。

#### J_BLOCK_PROGRESS

本章必须满足以下之一：

```text
A. 真实推进当前 BLOCK_PROMISE / BLOCK_PROGRESS
B. CURRENT_BLOCK 的 EXIT_CONDITION 已达成，本章完成合法自然转场
```

连续多章处于同一 SIM / REALITY / MIX BLOCK 完全合法；BLOCK_PROGRESS 看的是“有没有往前走”，不是“有没有换形态”。

如果复盘发现只做了分析、准备、说明，却没有新的事实/信息/决定/结果：FAIL → 返回 S2。

#### J_SCAN_STORY

执行扫读测试：

```text
临时忽略：心理解释 / 氛围 / 修辞 / 背景说明
只看：动作 / 对白 / 事件句 / EVENT_PANEL / 必要 LOCATOR_PANEL
→ 用 1-3 句话复述本章
```

合格复述必须包含：

```text
谁 + 做了什么 + 结果什么变了
```

PASS 示例：

```text
顾川帮周小满通过留用考核，两人进入药徒帮工路线；随后两人开始学《养血法》，顾川经历多次失败后在模拟第33日突破炼血境一重。
```

FAIL 示例：

```text
顾川分析了武道价值，回忆过去，制定了未来计划，并思考该如何利用模拟。
```

如果只能复述“思考/回忆/分析/准备”，说明剧情被解释覆盖：FAIL → 返回 S2 重构剧情块，不在成品上补动作。

每章将 SCAN_STORY 的 1-3 句复述写入 S3 run receipt，便于后续追溯。

### 9.2 EMOTION_VISIBLE｜SCAN_STORY 的补充原则

只检查 S2 已经标出的重大情绪节点；不要求每章必须存在，不设数量配额。

优先可见方式：

```text
明确决定 > 对白 > 动作 > 身体反应
```

允许仅靠一个明确决定完成情绪可见化。身体反应不是默认选项，禁止用瞳孔/呼吸/手指等模板动作堆叠成“情绪证明”。

如果重大情绪只剩抽象句“他很激动/他压住狂喜/他心情复杂”，而没有任何决定、对白或行动结果，视为 J_SCAN_STORY 的可见性问题。

### 9.3 开头/结尾最小规则

不再按 SIM / REALITY / MIX 设置开结尾模板。

```text
开头：快速进入当前事情或明确目标
结尾：当前有效剧情第一个自然闭合点即停
禁止：无承重纯氛围开场 / 结尾补总结 / 预告 / 重复确认
```

BLOCK_TYPE 仍是结构属性，但不再拥有开头/结尾格式解释权。

### 9.4 旧 J 门处置

```text
旧 J1 OPENING_SHOT      → 并入 J_SCAN_STORY 首屏可见性
旧 J2 SHOT_DENSITY      → 退役机械“每段必须动作”要求；剧情停摆由 J_SCAN_STORY 判
旧 J3 PLOT_VISIBLE      → 成为 J_SCAN_STORY 核心
旧 J4 CLEAR_FIRST_READ  → 保留为 J_CLEAR_FIRST_READ
旧 J5 ENDPOINT_STOP     → 保留为 J_ENDPOINT_STOP
旧 J6 BURST_SHOT        → 五拍硬门退役；大爆点改知识库软指导
旧 J7 OPENING_HOOK      → 并入 J_SCAN_STORY / §9.3
旧 J8 PANEL_DIRECT      → 改为 EVENT_PANEL / LOCATOR_PANEL 原则
旧 J9 DECLARATION       → 退役硬门，仅可作剧情需要时的软手法
旧 J10 MEAT_BLOCKS      → 退役
旧 J11 CHAPTER_LENGTH   → 保留并简化为 J_CHAPTER_LENGTH
旧 J12 SIM_EXECUTION    → 并入 J_BLOCK_PROGRESS
旧 J13 SIMULATOR_ENERGY → 数字指标全部退役；情绪可见与面板原则留存
旧 J14 OPEN_END_DIVERSITY → 类型限制退役；只留快速入戏 + 自然停点 + 禁尾巴
```

> 数量指标退役不代表可以写干瘪流水账。事件过薄会直接在 J_BLOCK_PROGRESS / J_SCAN_STORY 失败；表达退化仍由 Story Compose 原包与 story-deslop 工具层处理。

### 9.5 FAIL routing

表现层 FAIL 一律定位 owning layer：

```text
SCAN_COORDINATES / BLOCK_PROGRESS 不足 → S2 Plot Block
情绪/人物知识边界错误 → owning Character / Emotional layer
表达挡剧情但输入完整 → Story Compose package-owned local repair
```

禁止 S3 追加第二套全文改写。

不得把旧 `natural-flow-pass` / `novelization-pass` 变成 Story Compose 后的第二次全文改写。它们仅可在明确硬失败调查中作为诊断参考。

```text
S3_POST_COMPOSE_GENERAL_POLISH: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
FULL_RESMOOTH_AFTER_COMPOSE: FORBIDDEN
```

若硬失败，修具体 owning layer；无法合法修复则 STOP，不换引擎。

## 10. Human Grain status

`../human-grain-pass/**` 保留为 retired current-production compatibility。只有作者明确要求 legacy/A-B test 时才可手动运行，不属于标准主链。

## 11. Author-visible behavior

Source map、Source Shadow packet、Story Compose preflight、内部检测回执全部隐藏。作者只看完整正文候选，然后 review / adopt。

## 12. Output receipt

内部至少记录：

```text
TARGET_CHAPTER: n
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
CURRENT_BLOCK: present
SCAN_COORDINATES: present
STORY_COMPOSE_PREFLIGHT: PASS
PROSE_COMPOSER: story-compose
COMPOSER_INTERNAL_FLOW: package-owned
COMPOSER_DEGRADED_FALLBACK_USED: false
STORY_DESLOP_PIPELINE: PASS | BLOCKED
S3_POST_COMPOSE_REWRITE: none
HUMAN_GRAIN_PRODUCTION_ROUTE: retired
STORY_TRUTH_GATE: PASS
SOURCE_FACT_LEAK_GATE: PASS
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_GATE: PASS
POV_GATE: PASS
CLEAR_FIRST_READ: PASS | FAIL
ENDPOINT_STOP: PASS | FAIL
CHAPTER_LENGTH: PASS | FAIL
BLOCK_PROGRESS: PASS | FAIL
SCAN_STORY: PASS | FAIL
SCAN_STORY_SUMMARY: "谁做了什么，结果什么变了"
TARGET_PROSE_CANDIDATE: present
CANON_STATUS: NOT_ADOPTED
```

这些不写进小说正文，不增加作者步骤。

## Memory line

> **S3 准备真值、连续性、CURRENT_BLOCK、SCAN_COORDINATES 与真实母本参考；完整 Story Compose 原包负责正文。成稿回来后只看首读、停点、篇幅、块推进与扫读剧情，不再用旧数字 KPI 指挥小说。**