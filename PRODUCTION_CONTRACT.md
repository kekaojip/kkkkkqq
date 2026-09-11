# KQ Production Contract｜Chapter Workflow + Tracking

> status: production-main
> default_entry: `NOVEL_WORKFLOW_ENTRY.md`
> author_visible_workflow: `skills/references/author-visible-workflow-lock.md`

## Global reader experience

```text
纯小白
纯简单
纯好读
纯爽
```

人物首先是活人，其次才是剧情执行器。剧情有因果，人物也要有情绪因果。

## Owners｜生产白名单

正式 Stage 只有：

```text
S1 → skills/book-construction/SKILL.md
S2 → skills/story-material-engine/SKILL.md
S3 → skills/prose-preparation/SKILL.md
TRACKING → skills/tracking/SKILL.md
```

登记两个无 Stage 所有权的内部组件：

```text
PROSE_COMPOSER → skills/story-compose/SKILL.md
MOTHER_MIRROR → skills/mother-prose-contrast/SKILL.md
```

Story Compose 的底层 `novel-prose-writer-zh`、`human-writing-l2`、`story-deslop` 由 Story Compose 自己编排；KKKK 不另行定义其内部调用顺序，不抽象替代，不减少功能。

Mother Mirror 只对作者锁定的正文候选做母本双镜诊断，没有正文改写权、Canon 权或 Tracking 权。

旧 `human-grain-pass` 文件保留，但 current production-main 不再自动调用。

## 唯一作者可见流程

```text
S1 书籍基础
→ 母本拆解
→ 剧情块
→ 人物块
→ 必要章节情绪线
→ 正文
```

任何内部 Search / Fire / Source Acquisition / Source Shadow / Story Compose / Mother Mirror / Deslop / validator / Canon / Tracking / Chapter Gate 都不得新增作者可见 Stage 或独立进度行。

正文阶段内部允许作者执行：

```text
发来外部 AI 正文
→ 指定“拿这版跑诊断”
→ 看诊断后决定重写 / 局部修 / 换版 / 采用
```

这些仍然都属于“正文”阶段。

## S1 / S2 authority

S1 只构建够写的地基，不规划尚不需要的未来。

S2 负责母本剧情复述、母本人物追踪、Target 剧情块、人物块和必要情绪线。剧情块负责 WHAT HAPPENS；人物块和情绪线只决定已批准事件如何落在人身上，不重写 Plot。

模拟器文生产时，S2 同时读取 `CURRENT_BLOCK` 并生成 `SCAN_COORDINATES`：BLOCK 只描述当前大段正在兑现什么，不设章数配额；SCAN_COORDINATES 只记录产生新事实、新信息、新决定或新结果的章节事件。

所有作者可见候选仍按原 Gate 等作者确认。

## S3 正文｜真实 Source + 候选真值边界

S3 输入：

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ APPROVED EMOTIONAL THREAD when required
+ SAFE TRACKING CONTINUITY
+ CURRENT_BLOCK
+ SCAN_COORDINATES
+ S2 LOCKED SOURCE IDENTITY / MAPPED SOURCE RANGE
```

### 正文候选来源

允许两种正式候选来源：

```text
A. KKKK_GENERATED_PROSE
   → Story Compose preflight
   → COMPLETE story-compose PACKAGE
   → candidate

B. AUTHOR_EXTERNAL_PROSE_CANDIDATE
   → 作者明确提供 / 选择的外部 AI 或手工正文
   → candidate
```

规则：

```text
KKKK_GENERATES_PROSE → Story Compose remains mandatory
AUTHOR_SUPPLIES_PROSE → external candidate intake allowed
```

作者提供外部候选不属于 `STORY_COMPOSE_BYPASS_IN_PRODUCTION`，因为 KKKK 没有自行换用另一套正文引擎。

无论来源，候选都必须经过相同的 Target 真值与阅读可见性复核，才能进入正式诊断候选。

唯一 S3 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

Story Compose 接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

### 权威边界

```text
TARGET CANON / APPROVED STORY
> CURRENT_BLOCK / SCAN_COORDINATES
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> PROSE EXPRESSION
> SOURCE WORDING
```

`TARGET STORY TRUTH > SOURCE WORDING`

`APPROVED TARGET PLOT > PROSE ENGINE / WEB-FICTION GENERIC DEFAULTS`

任何正文来源都没有剧情权、人物设定权、世界观权、Canon 权或 Tracking 权。不得新增冲突、提前金手指、制造新钩子、改事件顺序或改章末终态。

### 包内零改造合同

KKKK 自己生成正文时，把以下目录视为一个完整发行包：

```text
skills/story-compose/**
skills/novel-prose-writer-zh/**
skills/human-writing-l2/**
skills/story-deslop/**
```

```text
PACKAGE_INTERNAL_FLOW_OWNER: skills/story-compose/SKILL.md
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
PACKAGE_SKILL_SUMMARY_SUBSTITUTION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION_BY_KKKK: FORBIDDEN
```

KKKK 只提供完整 Target 输入与 Source Shadow 参考，并接收最终正文。不得把 Story Compose 拆成若干零件后按 KKKK 自己的顺序执行。

### Story Compose preflight 与 fail-closed

仅当 KKKK 自己生成正文时，调用前确认完整包及执行依赖。缺失则：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact failure
→ STOP S3 INTERNAL GENERATION
```

正式内部生成禁止使用包内 standalone degradation/fallback 静默降级：

```text
STORY_COMPOSE_DEGRADED_FALLBACK_IN_PRODUCTION: FORBIDDEN
LIVE_PROSE_AUTOMATIC_FALLBACK: FORBIDDEN
OLD_NATIVE_WRITER_AUTOMATIC_FALLBACK: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
```

### 所有候选统一硬复核

无论候选来源于 Story Compose 还是作者明确提供的外部 AI，进入 Mother Mirror 前都只允许以下硬复核：

```text
TARGET_STORY_TRUTH
EVENT_ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE BOUNDARY
NEW_FACT_INTRODUCTION = 0
SOURCE_FACT_LEAK = 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK = 0
BACKSTAGE_METADATA_LEAK = 0
CLEAR_FIRST_READ
ENDPOINT_STOP
CHAPTER_LENGTH
BLOCK_PROGRESS
SCAN_STORY
```

模拟器文正文表现层不再使用面板行数、感叹号、系统场景数、BRAIN/HISTORY 字数、对白比例、爆点拍数等数量型 KPI。

禁止在候选后自动再做一次“自然化”“润色”“Human Grain”或全文重写。若硬真值失败，修 owning layer 的具体失败，不对全章做表面二次加工。

## Mother Mirror｜候选锁定后的母本双镜诊断

作者明确说“拿这版跑诊断”后：

```text
DIAGNOSTIC_CANDIDATE_LOCKED: true
CANON_STATUS: NOT_ADOPTED
```

然后运行：

`skills/mother-prose-contrast/SKILL.md`

正式双 Anchor：

```text
FIXED_ANCHOR = M01 Chapter 1
POSITION_ANCHOR = 当前 SOURCE_IDENTITY 的 mapped donor chapter / verified subrange
```

Fixed Anchor 只看跨章节阅读机制；Position Anchor 只看同功能剧情怎么落。禁止把“剧情内容不像第一章”当差距。

Mother Mirror 只检查：

```text
STORY_VISIBILITY
EVENT_MOTION
DIALOGUE_CARRY
PANEL_CARRY
EXPLANATION_LOAD
SCREEN_RHYTHM
```

并输出：

```text
KEEP
少量 MATERIAL GAP + OWNER
NO_ACTION_REQUIRED
CANDIDATE_SCAN_SUMMARY
```

严格禁止：

```text
MOTHER_MIRROR_AS_HARD_GATE
MOTHER_MIRROR_SCORE
MOTHER_MIRROR_AUTO_REWRITE
MOTHER_MIRROR_STYLE_COPY
MOTHER_MIRROR_CANON_ADOPTION
```

差异不自动等于缺陷。只有确实导致剧情被埋、扫读困难、首读发涩的差异才列 GAP。

## 候选 + 诊断存档

Mother Mirror 完成后，同一版本号保存：

```text
books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md
```

优先使用一次原子 Git 提交同时保存两份文件。

```text
CANDIDATE_BODY_PERSISTED_VERBATIM: true
DIAGNOSIS_MATCHES_SAME_CANDIDATE_VERSION: true
CANON_STATUS: NOT_ADOPTED
TRACKING_WRITE: FORBIDDEN
CHAPTER_COMPLETE: false
```

诊断完成后，作者可以直接采用、要求局部修、让外部 AI 重写或换另一版候选。

## Human Grain｜retired current production compatibility

`skills/human-grain-pass/SKILL.md` 保留但不在 current production-main 自动路由。

```text
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
HUMAN_GRAIN_MANUAL_AB_TEST: allowed_only_when_author_explicit
```

作者明确要求旧链/A-B test 时可单独运行，但必须标记非标准 Story Compose 输出，不能写回当前主链默认。

## 正文采用后的闭环

只有作者明确采用某一个已知正文版本后：

```text
selected candidate
→ Canon persist
→ Tracking transaction
→ authoritative current state update
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

Tracking 多文件更新继续要求语义原子；失败则报告并停止。

`DIAGNOSTIC_CANDIDATE_LOCKED` 永远不能替代 `AUTHOR_ADOPTED_CANON`。

## Search / Source contract

正式创作默认继续使用 Firecrawl 做当前规则要求的校准。Source Shadow 使用作者锁定母本正文，不得借 web 搜索偷偷换另一本 prose source。

Mother Mirror 同样必须读取真实母本正文：固定 Anchor 和同位置 Anchor 不得用聊天记忆、剧情摘要或 Human Retelling 冒充原文。

母本真实保留；普通词、常见短语、句式、对白接法和局部呼吸可参考，但 Source 专属事实、独特桥段、独特比喻、识别性表达必须隔离。

## Error discipline

```text
REPORT exact failure
→ repair owning layer when legal
→ still fail: STOP
```

Mother Mirror Anchor 无法取得时，必须报告 `MOTHER_MIRROR: BLOCKED`，不得伪造对照结论。

失败不产生新的作者可见 Stage，也不自动切换旧技能。

## Memory line

> **S1/S2/Tracking 原职责不动；S2 用 BLOCK 管大段承诺、SCAN_COORDINATES 管章节事件。正文候选既可来自完整 Story Compose，也可来自作者明确提供的外部 AI；统一硬检后，作者锁定候选才运行 Mother Mirror，用母本第一章固定镜 + 同位置动态镜找真正影响扫读的差距，并把候选+诊断同版本存档。只有作者采用后才 Canon / Tracking。**