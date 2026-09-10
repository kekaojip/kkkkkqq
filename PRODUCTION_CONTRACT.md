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

另外允许一个固定、无 Stage 所有权的正式后置处理器：

```text
POST_PROSE → skills/human-grain-pass/SKILL.md
```

Human Grain 不是第五个 Owner，也不是第二正文引擎。它只能在 S3 已经形成完整、通过真值校验的正文草稿后运行。

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

## S3 正文｜Source Shadow 唯一引擎

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
→ SOURCE SHADOW HOMOLOG WINDOWS
→ COPY-WEIGHTED TARGET REALIZATION
→ STORY TRUTH / SOURCE FACT LEAK / READER TRUST GATES
→ COMPLETE S3 PROSE DRAFT
```

唯一正式 route：

`skills/prose-preparation/routes/s3-source-shadow.md`

Source Shadow 的表面权不得反过来改 Plot / Character / Emotional Thread / Canon / Dwell。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

只要 Target 事实仍然成立，母本普通词、短语、句架、对白骨架、段落交接与局部呼吸可以直接沿用，不要求为了“原创感”主动同义词化。

### S3 fail-closed

如果当前正式母本正文无法可靠取得，或 Source Shadow 构建失败且合法修复后仍失败：

```text
REPORT exact S3 failure
→ STOP S3
```

正式默认：

```text
SOURCE_SHADOW_REQUIRED: true
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

S3 形成完整正文草稿后，必须进入正式 Human Grain Pass；作者看到的是 Human Grain 完成并回归校验通过后的完整正文候选。

正文候选不是 Canon。

## Human Grain｜正式正文后置层

固定技能：

`skills/human-grain-pass/SKILL.md`

执行位置：

```text
COMPLETE S3 PROSE DRAFT
→ HUMAN GRAIN PASS
→ HARD TRUTH RECHECK
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

Human Grain 只负责恢复过度精修后丢失的真人叙述纹理，包括语境驱动的句子 / 段落不均匀、轻微信息回声、普通旁白介入、短小现场偏题、解释力度不平均、不完美收口、受控的普通句法。

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

Direct Edit 只作为 Source Shadow 高同构原语保留，不再是独立路线。

## Error discipline

```text
REPORT exact failure
→ repair owning layer when legal
→ still fail: STOP
```

失败不等于新增一个作者流程步骤，也不等于获得切换旧技能的许可。

## Memory line

> **生产仍只认四个 Stage Owner；S3 只认 Source Shadow；S3 完整草稿后固定跑 Human Grain，再给作者看最终正文。任何一层失败都停，不自动偷跑其他正文技能。**
