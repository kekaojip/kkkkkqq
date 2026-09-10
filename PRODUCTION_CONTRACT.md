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

人物首先是活人，其次才是剧情执行器。

```text
剧情有因果，人物也要有情绪因果。
场景可以结束，情绪不能自动结算。
```

## Owners｜生产白名单

正式生产 Stage 只允许四个 Owner：

```text
S1 → skills/book-construction/SKILL.md
S2 → skills/story-material-engine/SKILL.md
S3 → skills/prose-preparation/SKILL.md
TRACKING → skills/tracking/SKILL.md
```

另登记两个无 Stage 所有权的 S3 内部能力：

```text
PROSE_REALIZATION → skills/novel-prose-writer-zh/SKILL.md
POST_PROSE_DIAGNOSIS → skills/human-grain-pass/SKILL.md
```

完整正文技能不是第五个 Owner；它的原始内容与独立运行能力保持完整。Human Grain 也不是 Owner，不是第二正文引擎。它只能在 S3 已经形成完整、通过真值校验的正文草稿后运行。

Article Memory 不再是正式 Owner。独立 S4 已退役。

```text
PRODUCTION_SKILL_AUTO_DISCOVERY_OUTSIDE_ALLOWLIST: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: ALLOWED_ONLY_AFTER_S3_FULL_DRAFT
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
```

以下没有正式生产路由权：

```text
archive/**
tools/skill-development/**
tests/**
experiments/** when present
backup branches
retired / compatibility artifacts
```

正式任务不得通过“搜索所有 SKILL.md 并挑一个最匹配的”方式绕过 Owner。历史文件只能在明确历史审计 / 回归调查中读取，不能接管当前 Stage。

## 唯一作者可见生产合同

作者前台只能有：

```text
S1 书籍基础
→ 母本拆解
→ 剧情块
→ 人物块
→ 必要章节情绪线
→ 正文
```

内部 Search / Fire / Source Acquisition / Source Shadow / Human Grain / Fidelity / Combination / Validator / Canon / Tracking / Chapter Gate 不得膨胀成作者可见步骤。

```text
AUTHOR_VISIBLE_WORKFLOW_STEP_INFLATION: FORBIDDEN
```

## S1

S1 只构建够写的地基。

```text
NOT_NEEDED_NOW = DO_NOT_ASK
UNKNOWN_FUTURE != MISSING_FIELD
ENOUGH_TO_WRITE = PASS
```

## 母本拆解

一个作者可见步骤，内部两块：

```text
【母本剧情复述】
【母本人物追踪】
```

母本人物追踪使用固定 `状态 / 动作或话 / 结果` 模板。

Source 只提供理解与骨架，不直接拥有 Target 决定权。

## 剧情块

剧情块负责 WHAT HAPPENS。

内部可强制执行当前正式：

```text
母本骨架 / bridge / dwell
Source-to-Target
Target Fire Bloom
world / Canon calibration
Fidelity / output gates
```

这些都只能作为剧情块内部机制。

最终只向作者展示一份完整剧情块候选并等待确认。

## 人物块

剧情块获作者批准后才运行。

人物块负责 HOW APPROVED EVENTS LAND ON PEOPLE，不得重写 Plot。

展示后等待作者确认。

## 章节情绪线

只有 materially relevant 时才需要。

只负责已批准事件连续落到人物身上后的情绪变化与余波，不新增剧情。

需要则展示并等作者确认；不需要则跳过。

## S3 正文｜完整原技能执行，Source Shadow 提供参考

输入：

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ required APPROVED EMOTIONAL THREAD
+ SAFE TRACKING CONTINUITY
+ S2 LOCKED SOURCE IDENTITY / MAPPED SOURCE RANGE
```

S3 只允许：

```text
SOURCE ACQUISITION
→ VERIFIED SAME-POSITION DONOR BODY
→ SOURCE SHADOW EXACT REFERENCE WINDOWS
→ COMPLETE novel-prose-writer-zh TARGET REALIZATION
→ STORY TRUTH / SOURCE FACT LEAK / READER TRUST GATES
→ COMPLETE S3 PROSE DRAFT
```

唯一正式 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

Source Shadow 只有参考权，没有 Target 表面或剧情决定权；完整 Writer 的表达权不得改 Plot / Character / Emotional Thread / Canon / Dwell。

完整调用、无损输入、生产禁用 FREEWRITE 及按需 references 服从 `skills/prose-preparation/references/prose-writer-integration.md`。原技能必须实际加载，不得用能力摘要或重写的简化提示词替代。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

母本原文真实保留；普通词、常见短语、句式、对白接法和呼吸可参考，但不能复制原句、独特比喻、识别性表达、桥段和动作序列。不得为了“原创感”强行同义词升级。局部无适用参考时如实记录，由完整 Writer 在批准边界内实现，不硬套也不豁免来源取得。

### S3 fail-closed

如果当前正式母本正文无法可靠取得，或 Source Shadow 构建失败且合法修复后仍失败：

```text
REPORT exact S3 failure
→ STOP S3
```

正式默认：

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
WRITER_SKILL_SUMMARY_SUBSTITUTION: forbidden
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
OLD_NATIVE_WRITER_AUTOMATIC_FALLBACK: forbidden
GOLDEN_DIRECT_EDIT_AS_INDEPENDENT_ROUTE: forbidden
LEGACY_STRUCTURE_DIAGNOSTICS_AUTO_RUN: forbidden
```

不得用剧情拆解摘要、聊天记忆或模型记忆冒充母本正文，也不得自动偷跑别的写作技能。

只有作者在**当前任务明确点名要求兼容 fallback** 时，才允许临时使用，并必须显式记录：

```text
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: true
COMPATIBILITY_ENGINE_USED: <name>
```

S3 形成完整且通过真值检查的正文后，必须完成 Human Grain 诊断；没有明确剩余阅读问题则逐字原样 PASS，只有实际问题才局部修复并复核。作者看到完整候选，不新增审批。

正文候选不是 Canon。

## Human Grain｜正式正文后置层

固定技能：

`skills/human-grain-pass/SKILL.md`

执行位置：

```text
COMPLETE S3 PROSE DRAFT
→ HUMAN GRAIN DIAGNOSIS
→ PASS_UNCHANGED or NECESSARY LOCAL REPAIR
→ HARD TRUTH RECHECK after edits
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

Human Grain 只诊断明确影响阅读的过度精修/表面人工感，确有问题才使用原有细化参考局部修复。普通、简洁、整齐、旁白少或叙事距离暂时固定本身不是失败；不为了增加毛边插入内容，不重复修 Writer 已解决的问题。

权限硬锁：

```text
STORY_AUTHORITY: NONE
CHARACTER_AUTHORITY: NONE
CANON_AUTHORITY: NONE
WORLD_AUTHORITY: NONE
PLOT_CHANGE: FORBIDDEN
EVENT_ORDER_CHANGE: FORBIDDEN
NEW_EVENT: FORBIDDEN
NEW_FACT: FORBIDDEN
NEW_RELATIONSHIP: FORBIDDEN
NEW_POWER: FORBIDDEN
POV_AUTHORITY_CHANGE: FORBIDDEN
DELIBERATE_TYPO: FORBIDDEN
DELIBERATE_GRAMMAR_ERROR: FORBIDDEN
GRAIN_QUOTA: FORBIDDEN
EDIT_TO_PROVE_EXECUTION: FORBIDDEN
PASS_UNCHANGED: ALLOWED
DUPLICATE_SURFACE_REWRITE: FORBIDDEN
FULL_RESMOOTH_AFTER_GRAIN: FORBIDDEN
```

Human Grain 完成后必须重新通过：

```text
TARGET_STORY_TRUTH: PASS
CHARACTER_CONTINUITY: PASS
EMOTIONAL_CONTINUITY: PASS when relevant
POV_CONTINUITY: PASS
NEW_FACT_INTRODUCTION: 0
SOURCE_FACT_LEAK: 0 when donor prose is in workflow
SOURCE_DISTINCTIVE_EXPRESSION_LEAK: 0 when donor prose is in workflow
GRAMMAR_CLARITY_FLOOR: PASS
READER_FIRST_PASS_CLARITY: PASS
DELIBERATE_ERROR_INJECTION: 0
```

如果 Human Grain 失败：

```text
REPORT exact grain failure
→ revert / repair only the failing local grain edit when legal
→ still fail: STOP before author-facing prose candidate
```

不得自动调用其他 humanizer、AI-detector evasion 工具、Live Prose、旧 Writer、旧 Golden 或 archive 技能补位。

## 正文采用后的后台闭环

只有作者明确采用 Human Grain 完成后的最终正文候选后：

```text
Canon persist
→ Tracking transaction
→ authoritative current state update
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

后台闭环默认自动，不需要额外作者确认。

Tracking 多文件更新必须语义原子；失败则报告并停止。

## Continuity authority

```text
Canon prose = what happened
Tracking = current story-state authority
PROJECT_STATE.md = production state + locks + pointers
```

## Search contract

正式创作默认使用 Firecrawl 校准。

每章 Target Fire Bloom 仍可作为剧情块内部硬 Gate，但：

```text
FIRE_AS_AUTHOR_VISIBLE_STAGE: forbidden
```

Source Shadow 使用的是作者锁定母本正文，不得借 web 搜索偷偷替换成另一本 prose source。

Human Grain 不得用 Web 搜索到的外部成文文本作为改写模板；外部材料只能用于研发 / 校准规则，不能成为本章新的 prose source。

## Retired architecture

```text
S3A / S3B mode select
independent Golden Direct Edit route
Live Prose as automatic prose engine
old Native Writer automatic prose route
S3 execution package
独立 S4 prose stage
archive prose skills
任何新增作者可见 Gate stage
```

Direct Edit 仅留历史审计用途，句段换槽不再参与正式生成。

## Error discipline

```text
REPORT exact failure
→ repair owning layer when legal
→ still fail: STOP
```

失败不等于新增一个作者流程步骤，也不等于获得切换旧技能的许可。

## Memory line

> **四个 Owner 不变；S3 完整调用原正文技能，母本只作真实参考。成稿必须诊断，但不强改；无问题原样通过，有问题局部修复，采用后才提交 Canon / Tracking。**
