# Production Skill Map｜Tracking State

> status: production-main
> canonical production rule: `NOVEL_WORKFLOW_ENTRY.md`
> contract: `PRODUCTION_CONTRACT.md`
> stage_scope_contract: `skills/references/stage-scope-and-progress-receipt.md`
> canonical_route: `S1 + S2 + S3 (complete writer + grain diagnosis) + TRACKING`

| Type | Path | Role |
|---|---|---|
| S1 Owner | `skills/book-construction/SKILL.md` | Minimum writeable book foundation |
| S2 Owner | `skills/story-material-engine/SKILL.md` | Story Room / Plot + Character + emotional thread |
| S3 Owner | `skills/prose-preparation/SKILL.md` | Approved materials + safe continuity + exact donor references → complete original prose skill |
| Internal Prose Core | `skills/novel-prose-writer-zh/SKILL.md` | Complete independent skill; owns Target expression only, no new Stage |
| Post-Prose Processor | `skills/human-grain-pass/SKILL.md` | Completed S3 draft → diagnose; unchanged PASS or necessary local repair |
| Tracking Owner | `skills/tracking/SKILL.md` | Post-prose authoritative story-state commit |
| Stage Scope | `skills/references/stage-scope-and-progress-receipt.md` | Hard authority boundaries + mandatory end-of-run progress receipt |
| Chapter Gate | `skills/references/chapter-progress-gate.md` | Routing only |
| Author Gate | `skills/references/author-visible-step-gate.md` | Sequential author approval gate |
| Fire Gate | `skills/references/fire-plot-bloom-gate.md` | Target Plot candidate formed → Fire bloom → Plot approval timing gate |
| Plot Output Contract | `skills/references/plot-block-output-contract.md` | Fire 后强制完整回写 + 剧情块中粒度连续复述硬锁 |
| Emotional Causality | `skills/references/emotional-causality-contract.md` | Cross-stage emotional continuity |

## Production skill allowlist

正式生产 Stage 仍只能由四个 Owner 接管：S1 / S2 / S3 / TRACKING。

`skills/novel-prose-writer-zh/SKILL.md` 是 S3 唯一内部正文核心，按原入口完整加载，不得摘要替代。

`skills/human-grain-pass/SKILL.md` 是唯一登记的正式 **Post-Prose Processor**，不是 Stage Owner，不拥有剧情、人物、Canon、世界观或 Tracking 决策权。

```text
PRODUCTION_SKILL_AUTO_DISCOVERY_OUTSIDE_ALLOWLIST: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: ALLOWED_ONLY_AFTER_S3_FULL_DRAFT
HUMAN_GRAIN_STAGE_OWNERSHIP: FORBIDDEN
```

以下一律没有当前生产路由权：

```text
archive/**
tools/skill-development/**
tests/**
experiments/** when present
backup branches
retired / compatibility artifacts
```

发现这些路径里的 `SKILL.md` 不等于可调用技能。只有明确进行历史审计 / 技能研发 / 回归调查时才可读取，且不得因此改变当前 Stage Owner。

`skills/article-memory/SKILL.md` 仅为 retired compatibility stub，不是 Owner。

## Route

```text
S2 SOURCE / CURRENT INPUT READY
→ S2 TARGET PLOT BLOCK PRE-FIRE CANDIDATE
→ S2 TARGET PLOT FIRE BLOOM
→ ABSORB / REJECT FIRE BRANCHES
→ MANDATORY FULL PLOT BLOCK REWRITE
→ S2 POST-FIRE PLOT BLOCK AUTHOR CANDIDATE
→ AUTHOR APPROVAL OF PLOT
→ S2 CHARACTER BLOCK
→ S2 CHAPTER EMOTIONAL THREAD when relevant
→ S3 CHAPTER PROSE WRITER
   → internal Source Acquisition
   → verified same-position donor body
   → Source Shadow exact reference windows
   → complete novel-prose-writer-zh realization
   → story/source-leak/reader-trust gates
   → complete S3 prose draft
→ HUMAN GRAIN PASS
   → surface-grain diagnosis
   → no defect: PASS_UNCHANGED
   → unresolved real defect: local grain edits only
   → truth / character / POV / clarity recheck
→ FULL PROSE CANDIDATE
→ AUTHOR APPROVAL
→ CANON PROSE
→ TRACKING COMMIT
→ CHAPTER COMPLETE
→ NEXT CHAPTER
```

## S3 complete prose core hard lock

S3 唯一 Owner：

`skills/prose-preparation/SKILL.md`

S3 唯一正式 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

```text
TARGET STORY AUTHORITY
> COMPLETE novel-prose-writer-zh WITHIN APPROVED BOUNDARIES
> APPLICABLE VERIFIED SOURCE REFERENCE
```

`prose-preparation/references/direct-source-slot-fill.md` 仅留历史审计用途，不执行句段换槽。接入合同见 `prose-preparation/references/prose-writer-integration.md`；完整技能核心、具体例子与条件引用必须保留。

正式生产默认：

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
WRITER_SKILL_SUMMARY_SUBSTITUTION: forbidden
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
OLD_NATIVE_WRITER_FALLBACK: forbidden
LEGACY_STRUCTURE_DIAGNOSTICS_AUTO_RUN: forbidden
```

Source Shadow 或 Source Acquisition 失败：

```text
REPORT exact failure
→ legal repair
→ still fail: STOP S3
```

不得自动切换 `prose-preparation/references/live-prose-calibration.md`、旧 Native Writer、旧 Golden 独立 route、archive prose skill 或未登记的其他写作技能。

只有作者在**当前任务明确点名要求某个兼容 fallback** 时，才允许临时使用，并必须输出明确 receipt；不得静默执行。

没有 ready 的 `reference-corpus` 时：

```text
PRIMARY = S2 mapped same-position donor body
CROSS_CHAPTER_ALTERNATES = disabled
```

不得假装全书检索。

## Human Grain hard lock

`skills/human-grain-pass/SKILL.md` 只在 S3 已形成完整、通过 S3 真值校验的正文草稿后自动运行。

它不是第二正文引擎，也不得重做 Source Shadow。没有明确剩余阅读问题必须逐字原样 PASS；只有具体症状造成阅读摩擦才修，Writer 已修问题不再重复加工。统计指标只提示检查，不要求调整至某个分布。

```text
STORY_AUTHORITY: NONE
CHARACTER_AUTHORITY: NONE
CANON_AUTHORITY: NONE
WORLD_AUTHORITY: NONE
NEW_EVENT: FORBIDDEN
NEW_FACT: FORBIDDEN
NEW_RELATIONSHIP: FORBIDDEN
NEW_POWER: FORBIDDEN
DELIBERATE_TYPO: FORBIDDEN
DELIBERATE_GRAMMAR_ERROR: FORBIDDEN
FULL_RESMOOTH_AFTER_GRAIN: FORBIDDEN
```

Human Grain 失败：

```text
REPORT exact grain failure
→ legal local repair
→ still fail: STOP before author-facing prose candidate
```

不得因 Human Grain 失败改用其他 humanizer、旧 Writer、Live Prose、archive 技能或检测器规避工具。

## Hard scope rule

所有 Owner 与正式 Post-Prose Processor 都服从：

```text
ONE_STAGE_ONE_AUTHORITY
CURRENT_STAGE_MAY_NOT_REDECIDE_APPROVED_UPSTREAM
CURRENT_STAGE_MAY_NOT_PRECOMPUTE_DOWNSTREAM_AUTHOR_VISIBLE_OUTPUT
CURRENT_STAGE_MUST_STOP_AT_ITS_OWN_EXIT
MANDATORY_END_OF_RUN_PROGRESS_RECEIPT: true
```

职责速记：

```text
Source = 理解母本
Plot = 形成我们自己的剧情候选并吸收 Fire 后结果
Character = 决定已批准事件落到人物身上时人怎么活
Emotional Thread = 决定情绪如何跨节点变化
S3 = 准备无损安全输入/真实参考并完整调用原正文技能，验证批准真值
Source Shadow = 真实原文参考及来源/适用性/专属内容隔离
novel-prose-writer-zh = 实际中文落句、注意力、对白、心理停点、普通句与分段
Human Grain = 成稿诊断，无问题原样通过，有问题才局部修复
Tracking = 只提交 Canon 已经造成的当前状态
```

每次正式生产输出最后必须显示统一【生产进度】勾选表。

## Tracking reads

```text
S2 = full author-side Tracking views
S3 = safe Tracking views only
Human Grain = no new Tracking authority; read only enough approved truth to detect drift
```

S3 默认不读取 `作者真相.md`。

## Retired architecture

```text
S3A / S3B route select
independent Golden Direct Edit route
S3_EXECUTION_PACKAGE
S3 preparation-only
S4 prose generation / validation stage
Live Prose as automatic prose engine
legacy prose skills under archive/**
```

以上不得恢复为正式主链。

## Legacy continuity

`skills/article-memory/SKILL.md` 与书内 `ARTICLE_MEMORY.md` 仅作迁移兼容，不再是正式可写连续性 Owner。

## Memory line

> **四个 Owner 与作者前台不变；S3 内完整原技能写正文，Source Shadow 提供真实参考，Human Grain 条件修复。不得稀释技能、换槽复制或为了运行痕迹强改正文。**
