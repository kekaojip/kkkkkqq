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

登记一个无 Stage 所有权的 S3 内部完整成文器：

```text
PROSE_COMPOSER → skills/story-compose/SKILL.md
```

Story Compose 的底层 `novel-prose-writer-zh`、`human-writing-l2`、`story-deslop` 由 Story Compose 自己编排；KKKK 不另行定义其内部调用顺序，不抽象替代，不减少功能。

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

任何内部 Search / Fire / Source Acquisition / Source Shadow / Story Compose / Deslop / validator / Canon / Tracking / Chapter Gate 都不得新增作者步骤。

## S1 / S2 authority

S1 只构建够写的地基，不规划尚不需要的未来。

S2 负责母本剧情复述、母本人物追踪、Target 剧情块、人物块和必要情绪线。剧情块负责 WHAT HAPPENS；人物块和情绪线只决定已批准事件如何落在人身上，不重写 Plot。

所有作者可见候选仍按原 Gate 等作者确认。

## S3 正文｜外部真值与 Source，内部完整 Story Compose

S3 输入：

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ APPROVED EMOTIONAL THREAD when required
+ SAFE TRACKING CONTINUITY
+ S2 LOCKED SOURCE IDENTITY / MAPPED SOURCE RANGE
```

正式流程：

```text
SOURCE ACQUISITION
→ VERIFIED SAME-POSITION DONOR BODY
→ SOURCE SHADOW EXACT REFERENCE PACKET
→ STORY COMPOSE PREFLIGHT
→ COMPLETE story-compose PACKAGE
→ FINAL COMPOSED PROSE
→ HARD TARGET TRUTH / SOURCE LEAK / POV / ENDPOINT RECHECK ONLY
→ FULL PROSE CANDIDATE
```

唯一 S3 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

Story Compose 接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

### 权威边界

```text
TARGET CANON / APPROVED STORY
> CHARACTER / EMOTION / CONTINUITY
> INHERITED DWELL
> STORY COMPOSE EXPRESSION
> SOURCE WORDING
```

`TARGET STORY TRUTH > SOURCE WORDING`

`APPROVED TARGET PLOT > STORY_COMPOSE / WEB-FICTION GENERIC DEFAULTS`

Story Compose 没有剧情权、人物设定权、世界观权、Canon 权或 Tracking 权。它把已经批准的内容写出来，不得因通用网文规则新增冲突、提前金手指、制造新钩子、改事件顺序或改章末终态。

### 包内零改造合同

正式生产把以下目录视为一个完整发行包：

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

### 正式 preflight 与 fail-closed

调用前确认完整包及执行依赖。缺失则：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact failure
→ STOP S3
```

正式生产禁止使用包内 standalone degradation/fallback 静默降级：

```text
STORY_COMPOSE_DEGRADED_FALLBACK_IN_PRODUCTION: FORBIDDEN
LIVE_PROSE_AUTOMATIC_FALLBACK: FORBIDDEN
OLD_NATIVE_WRITER_AUTOMATIC_FALLBACK: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
```

### Story Compose 返回后

S3 只允许硬复核：

```text
TARGET_STORY_TRUTH
EVENT_ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE BOUNDARY
NEW_FACT_INTRODUCTION = 0
SOURCE_FACT_LEAK = 0
SOURCE_DISTINCTIVE_EXPRESSION_LEAK = 0
BACKSTAGE_METADATA_LEAK = 0
READER_FIRST_PASS_CLARITY
```

禁止在此之后再做一次“自然化”“润色”“Human Grain”或全文重写。若硬真值失败，修 owning layer 的具体失败，不对全章做表面二次加工。

## Human Grain｜retired current production compatibility

`skills/human-grain-pass/SKILL.md` 保留但不在 current production-main 自动路由。

```text
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
HUMAN_GRAIN_MANUAL_AB_TEST: allowed_only_when_author_explicit
```

作者明确要求旧链/A-B test 时可单独运行，但必须标记非标准 Story Compose 输出，不能写回当前主链默认。

## 正文采用后的闭环

只有作者明确采用最终正文候选后：

```text
Canon persist
→ Tracking transaction
→ authoritative current state update
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

Tracking 多文件更新继续要求语义原子；失败则报告并停止。

## Search / Source contract

正式创作默认继续使用 Firecrawl 做当前规则要求的校准。Source Shadow 使用作者锁定母本正文，不得借 web 搜索偷偷换另一本 prose source。

母本真实保留；普通词、常见短语、句式、对白接法和局部呼吸可参考，但 Source 专属事实、独特桥段、独特比喻、识别性表达必须隔离。

## Error discipline

```text
REPORT exact failure
→ repair owning layer when legal
→ still fail: STOP
```

失败不产生新的作者可见 Stage，也不自动切换旧技能。

## Memory line

> **S1/S2/Tracking 原职责不动；S3 先准备真值与 Source Shadow，再把完整任务交给原版 Story Compose。包内流程不拆、不减、不重排；返回后只做硬真值复核，作者采用后才提交 Canon / Tracking。**
