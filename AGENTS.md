# 仓库规则｜Novel Production with Tracking

> status: production-main
> branch: `main`
> canonical_entry: `NOVEL_WORKFLOW_ENTRY.md`
> contract: `PRODUCTION_CONTRACT.md`
> author_visible_workflow: `skills/references/author-visible-workflow-lock.md`
> stage_scope_contract: `skills/references/stage-scope-and-progress-receipt.md`

## 0. 第一章式作者可见流程｜全局硬锁

所有正式生产先加载：

`skills/references/author-visible-workflow-lock.md`

作者前台只有：

```text
S1 书籍基础
→ 母本拆解
→ 剧情块
→ 人物块
→ 章节情绪线 when needed
→ 正文
```

```text
AUTHOR_VISIBLE_STEP_INFLATION: FORBIDDEN
```

Fire、Source Fidelity、Source-to-Target、各种 validator / Gate 全部属于现有步骤内部；Canon、Tracking、Chapter Complete 全部属于正文采用后的后台闭环。不得把它们重新做成作者可见步骤或生产进度行。

## 1. 全局体验

```text
纯小白
纯简单
纯好读
纯爽
```

人物首先是活人，其次才是剧情执行器。

```text
剧情有因果，人物也要有情绪因果。
场景结束不等于情绪结算。
冷静选择不等于无感。
```

先检查错误前提、逻辑跳跃和信息缺失。发现异常必须上报，不得静默跳过。

## 2. Production Owner allowlist｜正式生产技能白名单

正式小说生产只允许以下四个 Owner：

```text
S1 → skills/book-construction/SKILL.md
S2 → skills/story-material-engine/SKILL.md
S3 → skills/prose-preparation/SKILL.md
TRACKING → skills/tracking/SKILL.md
```

其中 S3 唯一正式正文 route：

```text
skills/prose-preparation/routes/s3-source-shadow.md
```

高同构时：

```text
direct-source-slot-fill.md
```

只是 Source Shadow 内部执行原语，不是第二条 S3 route。

### 2.1 Repository scan firewall

正式生产禁止通过“全仓库查找 `SKILL.md` / 猜最匹配技能 / 自动技能发现”改变 Owner。

以下目录和文件**绝无正式生产路由权**：

```text
archive/**
tools/skill-development/**
tests/**
experiments/** when present
backup branches
historical / retired / compatibility artifacts
```

尤其禁止把：

```text
archive/legacy-skills/**/SKILL.md
```

当作当前技能执行。它们只允许在明确的历史审计 / 回归调查中被读取，且不得因此改变当前 Owner / route。

`skills/article-memory/SKILL.md` 是 retired compatibility stub，只能重定向到 Tracking，不能作为 Owner 执行。

```text
PRODUCTION_SKILL_AUTO_DISCOVERY_OUTSIDE_ALLOWLIST: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
ARCHIVE_SKILL_EXECUTION_IN_PRODUCTION: FORBIDDEN
TEST_SPEC_AS_RUNTIME_AUTHORITY: FORBIDDEN
```

若任何文件与本白名单冲突：

```text
AGENTS.md
+ NOVEL_WORKFLOW_ENTRY.md
+ PRODUCTION_CONTRACT.md
+ skills/PRODUCTION_MAP.md
```

中的当前 production-main 合同优先；报告冲突并修复，不得自行选择旧技能。

## 3. S1

```text
NOT_NEEDED_NOW = DO_NOT_ASK
UNKNOWN_FUTURE != MISSING_FIELD
UNDECIDED_FUTURE != GATE_FAIL
ENOUGH_TO_WRITE = PASS
```

S1 只做到够写，不规划具体章节。

## 4. S2

S2 是连续共创，不是选项机。

母本模式下，作者可见母本拆解内部固定两块：

```text
【母本剧情复述】
【母本人物追踪】
```

其中母本人物追踪必须服从 `skills/story-material-engine/references/character-trace.md` 固定三字段模板。

然后进入【剧情块】。剧情块内部可以并应按当前规则使用：

```text
母本骨架 / bridge / dwell
Source-to-Target Combination
Target-specific Fire 开花
世界 / Canon 校准
内部 Fidelity / output gates
```

但这些永远不成为作者前台独立步骤。

```text
剧情块候选
→ 作者确认
→ 人物块候选
→ 作者确认
→ 必要章节情绪线
→ 作者确认
```

未确认上一步，不得运行下一作者可见创作步骤。

## 5. Search / Fire

正式创作推进默认使用 Firecrawl 做相关外部校准。

每章剧情块内部的 Target Fire 开花仍按 `skills/references/fire-plot-bloom-gate.md` 强制执行；失败必须报告并阻断剧情块最终交付。

```text
FIRE_IS_INTERNAL_TO_PLOT_CONSTRUCTION: true
FIRE_AS_AUTHOR_VISIBLE_STAGE: forbidden
```

深度案例研究按需。

## 6. S3｜只允许 Source Shadow

```text
APPROVED PLOT
+ APPROVED CHARACTER
+ SAFE TRACKING
+ APPROVED EMOTIONAL THREAD when required
+ VERIFIED MAPPED DONOR PROSE
→ skills/prose-preparation/SKILL.md
→ routes/s3-source-shadow.md
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

S3 不重做剧情、人物块或情绪线。

正式生产默认：

```text
SOURCE_SHADOW_REQUIRED: true
LIVE_PROSE_AUTOMATIC_FALLBACK: forbidden
LEGACY_STRUCTURE_DIAGNOSTICS_AUTO_RUN: forbidden
```

取得不到合法母本正文、Source Shadow 构建失败或无法修复：

```text
REPORT exact failure
→ STOP S3
```

不得悄悄改用 Live Prose、旧 Native Writer、旧 Direct Edit 独立 route、历史 prose skill 或模型自由作文。

只有作者在当前任务里**明确点名要求 fallback**，才允许调用相应兼容能力，并必须在 receipt 中明示。

## 7. 正文采用后的后台闭环

作者明确采用正文后：

```text
Canon persist
→ Tracking Commit
→ Chapter Gate
→ CHAPTER_COMPLETE
```

默认自动执行，不再增加作者审批门。失败则报告并停在失败 Owner。

## 8. 唯一中文生产进度

所有正式生产回复末尾必须播报，但只能使用这几行：

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

```text
[✓] 已完成 / 已批准
[◐] 已展示候选，等待作者确认
[ ] 尚未进行
[-] 本章不需要
```

禁止在进度表中单列：Fire、Fidelity、Combination、Canon、Tracking、Chapter Gate、Chapter Complete、repo commit、handoff。

正文采用并后台闭环成功后，写：

```text
[✓] 正文
当前停点：本章已完成
下一步：等待作者开始下一章 / 下一项工作
```

## Memory line

> **正式生产只认四个 Owner；S3 只认 Source Shadow。archive / tools / tests / 历史 SKILL 没有路由权，Source Shadow 失败就报错停止，不得自动偷跑旧写作技能。**
