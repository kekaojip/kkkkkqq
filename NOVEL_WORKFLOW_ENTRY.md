# 小说工作流入口｜Canonical Route

> status: production-main
> author_visible_workflow: `skills/references/author-visible-workflow-lock.md`

## Startup

```text
AGENTS.md
→ PRODUCTION_CONTRACT.md
→ skills/references/author-visible-workflow-lock.md
→ skills/references/stage-scope-and-progress-receipt.md
→ .active-book
→ books/{ACTIVE_BOOK}/PROJECT_STATE.md
→ books/{ACTIVE_BOOK}/追踪/_tracking-state.json when present
```

禁止靠聊天历史猜生产状态。

正式 Stage Owner 必须从 `AGENTS.md` / `skills/PRODUCTION_MAP.md` 白名单解析，不得通过全仓库 `SKILL.md` 搜索重新选 Owner。

## 唯一作者可见主链

```text
S1 书籍基础
↓
母本拆解
  ├─ 母本剧情复述
  └─ 母本人物追踪
↓
【剧情块】
  内部：母本骨架 + Source-to-Target + Fire 开花 + 内部校验
↓
作者确认
↓
【人物块】
↓
作者确认
↓
【章节情绪线】只有需要时
↓
作者确认
↓
S3【完整正文候选】
  内部：Source Acquisition + Source Shadow reference + complete novel-prose-writer-zh + validation + conditional Human Grain repair
↓
作者修改 / 重跑 / 采用
↓
作者正式采用正文
════════════
后台自动：Canon → Tracking → 本章完成
════════════
```

任何内部 Gate、搜索、Source Shadow packet、Human Grain、validator、持久化动作不得新增作者可见步骤。

## S2 Source

母本模式启用时：

```text
Tracking continuity restored
→ source identity / chapter range
→ 【母本剧情复述】
→ 【母本人物追踪】
→ source breakdown complete
→ enter 【剧情块】 construction
```

母本人物追踪必须通过固定三字段模板 Gate。
Source Fidelity / bridge / dwell 等检查可以内部执行，但不作为作者前台步骤。

## S2 Plot

【剧情块】内部正式执行：

```text
source trunk / bridge / dwell when applicable
→ source-to-target combination
→ target-specific Fire bloom
→ world / Canon calibration
→ internal fidelity + output checks
→ one complete Target Plot candidate
```

Fire 失败则在剧情块内部阻断并报告，不允许把 Fire 单独升级成作者流程节点。
最终只展示一份完整【剧情块】候选，然后停止等待作者确认。

S2 还必须保留当前目标章的：

```text
SOURCE_IDENTITY
MAPPED DONOR CHAPTER / SUBRANGE
SOURCE DWELL when available
```

供 S3 Source Acquisition 使用。

## S2 Character

只有剧情块明确采用后：

```text
【人物块】
→ SHOW
→ STOP
→ AUTHOR REVIEW
```

人物块不重做剧情。

## Emotional Thread

只有 materially required 时：

```text
【章节情绪线】
→ SHOW
→ STOP
→ AUTHOR REVIEW
```

不需要时合法标记 `[-]`，直接进入正文。

## S3｜真实参考 + 完整正文技能

```text
APPROVED Plot
+ APPROVED Character
+ approved Emotional Thread when required
+ safe Tracking continuity
+ S2 locked donor position
→ Source Acquisition
→ verified same-position donor prose
→ Source Shadow exact reference packet
→ complete novel-prose-writer-zh realization
→ story truth / source leak / reader trust validation
→ COMPLETE S3 PROSE DRAFT
→ Human Grain diagnosis
→ PASS_UNCHANGED or necessary local repair
→ truth / character / POV / clarity recheck after edits
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

唯一 S3 Owner / route：

```text
skills/prose-preparation/SKILL.md
→ skills/prose-preparation/routes/s3-source-shadow.md
```

S3 内部正文核心：`skills/novel-prose-writer-zh/SKILL.md`。实际加载三个核心文件，按条件读取 Voice / Local Repair；完整接入合同：`skills/prose-preparation/references/prose-writer-integration.md`。

固定成稿诊断 / 条件修复器：

```text
skills/human-grain-pass/SKILL.md
```

Human Grain 不是 S3 替代引擎，不拥有剧情、人物、世界观、Canon 或 Tracking 权限；只在 S3 已形成完整且通过真值校验的正文草稿后运行。

Source Shadow 内部：

```text
TARGET STORY TRUTH > SOURCE WORDING
```

母本真实窗口保留，常见措辞、句式、对白接法与呼吸可供参考；完整原技能决定 Target 表达。不得把技能或母本抽成摘要，不复制原句、独特表达、桥段与动作序列；不得把 Source 句序或段长变成硬要求。

Human Grain 内部：

```text
STORY TRUTH FREEZE
→ diagnose over-polish
→ no real defect: PASS_UNCHANGED
→ real unresolved reading defect: local grain edits only
→ no full resmooth
→ hard truth recheck
```

只在具体阅读问题成立时，参考保留的 grain-patterns 做必要局部修复；不为了增加不均匀、回声、旁白或偏题而改稿。Writer 已处理的问题不重复改写。

禁止：新增事件、事实、关系、能力，故意错字 / 病句，随机配额式“人类痕迹”，以及为了毛边重新写剧情。

### S3 / Human Grain fail-closed

若母本正文取得失败：

```text
REPORT SOURCE ACQUISITION FAILURE
→ repair when legal
→ still fail: STOP S3
```

若 Source Shadow 构建 / 验证失败：

```text
REPORT SOURCE SHADOW FAILURE
→ repair owning layer when legal
→ still fail: STOP S3
```

若 Human Grain 运行或回归校验失败：

```text
REPORT HUMAN GRAIN FAILURE
→ local legal repair / revert failing grain edit
→ still fail: STOP before author-facing prose candidate
```

正式默认：

```text
SOURCE_SHADOW_REFERENCE_REQUIRED: true
PROSE_REALIZATION_CORE: novel-prose-writer-zh
HUMAN_GRAIN_DIAGNOSIS_REQUIRED_AFTER_S3_DRAFT: true
HUMAN_GRAIN_EDITS: ONLY_WHEN_NECESSARY
UNCHANGED_PASS: allowed
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
OLD_NATIVE_WRITER_AUTOMATIC_FALLBACK: forbidden
LEGACY_SKILL_AUTO_FALLBACK: forbidden
LEGACY_STRUCTURE_DIAGNOSTICS_AUTO_RUN: forbidden
```

只有作者在当前任务**明确点名要求某个兼容 fallback**时，才允许临时启用，并必须显式标记 override。新窗口不得自行推断“既然 Source Shadow / Human Grain 失败，就换旧技能”。

正文候选不是 Canon。

## Post-adoption closure

作者明确采用正文后自动：

```text
persist Canon
→ Tracking Commit
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

成功时不再逐项展示 Canon / Tracking / Gate，也不需要额外作者确认。
真实失败：报告具体失败并停止，不得静默跳过。

## Continuity authority

```text
Canon prose = what actually happened
Tracking = current story-state authority
PROJECT_STATE.md = production state + author locks + pointers
```

S2 可读作者侧 Tracking 做研发；S3 默认只读安全连续性，不得泄露未批准作者真相。Human Grain 不获得新的 Tracking 权限，只能读取足以做漂移检查的已批准真值。

## Retired / non-routable

```text
S3A / S3B route select
independent Direct Edit prose route
Live Prose automatic prose route
old Native Writer automatic prose route
S3_EXECUTION_PACKAGE
S4 prose generation
archive/** prose skills
tools/skill-development/** skills
任何新增作者可见 Gate stage
```

Direct Edit 只保留历史审计用途，不参与正式正文生成。

## Mandatory run ending

每次正式生产回复最后使用：

```text
【生产进度】

[✓] 书籍基础
[✓] 母本拆解
[◐] 剧情块
[ ] 人物块
[ ] 章节情绪线
[ ] 正文

当前停点：……
下一步：……
```

不得增加 Fire、Source Shadow、Human Grain、Canon、Tracking、本章完成等独立进度行。

## Memory line

> **新窗口恢复原 Stage；S3 提供真实参考并完整调用原正文技能，成稿无问题原样通过，确有问题只修局部。任何必要层失败仍报告并停止，不调用旧引擎。**
