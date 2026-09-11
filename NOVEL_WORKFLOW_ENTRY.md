# 小说工作流入口｜Canonical Route

> status: production-main
> author_visible_workflow: `skills/references/author-visible-workflow-lock.md`
> order_lock: `WORKFLOW_ORDER_LOCK.md` ← 正式生产流程顺序唯一真源（作者锁定，禁止重排/跳过/简化）

## Startup

```text
AGENTS.md
→ PRODUCTION_CONTRACT.md
→ WORKFLOW_ORDER_LOCK.md
→ skills/references/author-visible-workflow-lock.md
→ skills/references/stage-scope-and-progress-receipt.md
→ .active-book
→ books/{ACTIVE_BOOK}/PROJECT_STATE.md
→ books/{ACTIVE_BOOK}/追踪/_tracking-state.json when present
```

禁止靠聊天历史猜生产状态。正式 Stage Owner 必须从当前生产白名单解析，不得通过扫描全仓库 `SKILL.md` 改路由。

## 唯一作者可见主链

```text
S1 书籍基础
↓
母本拆解
  ├─ 母本剧情复述
  └─ 母本人物追踪
↓
【剧情块】
  内部：CURRENT_BLOCK + SCAN_COORDINATES + 母本骨架 + Source-to-Target + Fire 开花 + 内部校验
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
【正文】
  内部候选来源可为：
  A. KKKK 用完整 Story Compose 生成
  B. 作者明确提供 / 选择的外部 AI 正文
↓
S3 统一硬复核
↓
作者指定“拿这版跑诊断”
  内部：Mother Mirror 双镜诊断 + 候选/诊断同版本存档
↓
作者修改 / 重跑 / 换版 / 采用
↓
作者正式采用某一版正文
════════════
后台自动：Canon → Tracking → 本章完成
════════════
```

Mother Mirror 不是新的作者可见 Stage，仍属于“正文”阶段内部动作。

## S2

母本拆解、剧情块、人物块、情绪线继续由 `skills/story-material-engine/SKILL.md` 负责。剧情块形成后必须等待作者批准，人物块和必要情绪线同样遵守既有作者 Gate。

S2 还要保留当前目标章：

```text
SOURCE_IDENTITY
MAPPED DONOR CHAPTER / SUBRANGE
SOURCE DWELL when available
CURRENT_BLOCK
SCAN_COORDINATES
```

供 S3 Source Acquisition、正文候选硬复核与 Mother Mirror 使用。

## S3｜真实参考 + 正文候选统一验证

正式输入：

```text
APPROVED Plot
+ APPROVED Character
+ approved Emotional Thread when required
+ safe Tracking continuity
+ CURRENT_BLOCK
+ SCAN_COORDINATES
+ S2 locked donor position
```

基础链：

```text
Source Acquisition
→ verified same-position donor prose
→ Source Shadow exact reference packet
→ obtain one prose candidate
→ S3 hard truth / source leak / POV / reader-visible checks
→ FULL PROSE CANDIDATE
```

### Candidate source A｜KKKK 内部生成

```text
Story Compose production preflight
→ COMPLETE skills/story-compose/SKILL.md
→ FINAL COMPOSED PROSE
```

当 KKKK 自己生成正文时，Story Compose 仍是唯一内部成文入口。

### Candidate source B｜作者外部正文

作者明确把其他 AI / 自己写的正文发回并指定为当前候选时：

```text
AUTHOR_EXTERNAL_PROSE_CANDIDATE: true
→ do not pretend it came from Story Compose
→ send directly to the same S3 hard validation
```

这不属于 KKKK 绕过 Story Compose 自行换引擎。

唯一 S3 Owner / route：

```text
skills/prose-preparation/SKILL.md
→ skills/prose-preparation/routes/s3-source-shadow.md
```

Story Compose 完整接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

### Story Compose 是内部成文黑盒

它不是 Stage Owner。KKKK 自己生成正文时，不直接调度其底层三个技能，也不重新写一份它的 Phase 1 / Phase 2 / Phase 3 顺序。

```text
PACKAGE_INTERNAL_FLOW_OWNER: story-compose/SKILL.md
STORY_COMPOSE_BYPASS_WHEN_KKKK_GENERATES_PROSE: forbidden
PACKAGE_CAPABILITY_REDUCTION: forbidden
```

完整包可以继续 standalone 使用；但 KKKK 内部正式生成必须先 preflight，只有完整依赖都在才允许进入。缺失时 STOP INTERNAL GENERATION，不能使用 standalone fallback 静默降级。

### Production truth freeze

无论正文来自哪里，都必须服从：

```text
TARGET STORY TRUTH > SOURCE WORDING
APPROVED TARGET PLOT > PROSE ENGINE GENERIC DEFAULTS
CURRENT_BLOCK / SCAN_COORDINATES > EXPLANATION FILLER
```

因此任何正文来源都不得新增或重排已批准剧情。

### 返回后的 S3 只做硬检查

统一验证：

```text
事件/结果/终态
人物与情绪连续性
POV/知识边界
新事实=0
Source 专属事实/识别性表达泄漏=0
后台元数据泄漏=0
CLEAR_FIRST_READ
ENDPOINT_STOP
CHAPTER_LENGTH
BLOCK_PROGRESS
SCAN_STORY
```

不得在候选后自动执行 Human Grain、全文自然化或第二正文引擎。

旧 `skills/human-grain-pass/**` 留作历史兼容和作者明确 A/B test，不属于 current production-main。

## Mother Mirror｜正文候选锁定后的诊断

当作者明确说：

```text
“拿这版跑诊断”
“这版确定，先对比母本”
```

等价语义时：

```text
DIAGNOSTIC_CANDIDATE_LOCKED: true
CANON_STATUS: NOT_ADOPTED
```

然后运行：

`skills/mother-prose-contrast/SKILL.md`

正式双镜：

```text
FIXED_ANCHOR = M01 Chapter 1
POSITION_ANCHOR = 当前 mapped donor chapter / verified range
```

固定第一章只看“读者眼睛怎么往下走”；同位置母本只看“这一类剧情功能怎么落”。

只诊断六项：

```text
STORY_VISIBILITY
EVENT_MOTION
DIALOGUE_CARRY
PANEL_CARRY
EXPLANATION_LOAD
SCREEN_RHYTHM
```

Mother Mirror 不是相似度评分器，也不是自动润色器。差异不等于缺陷。

诊断输出重点：

```text
KEEP
MATERIAL GAP + OWNER
NO_ACTION_REQUIRED
CANDIDATE_SCAN_SUMMARY
```

完成后，同一 candidate version 保存：

```text
books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md
```

优先一次原子 Git 提交保存两份文件。保存后仍然：

```text
CANON_STATUS: NOT_ADOPTED
TRACKING_WRITE: none
CHAPTER_COMPLETE: false
```

作者可以看诊断后继续改、换版本或直接采用。

## S3 fail-closed

下列任一项失败且合法修复后仍失败：Source Acquisition、Source Shadow、内部 Story Compose preflight/执行（当使用内部生成）、最终硬真值复核，均：

```text
REPORT exact failure
→ STOP current candidate route
```

Mother Mirror 需要的任一母本 Anchor 无法取得：

```text
MOTHER_MIRROR: BLOCKED
→ REPORT exact missing anchor
→ do not fabricate comparison
```

不自动改用 Live Prose、Native Writer、Golden Direct Edit、archive prose skill 或其他 humanizer。

## Post-adoption closure

只有作者明确采用某一已知候选版本后：

```text
persist Canon
→ Tracking Commit
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

成功时不新增作者确认。

`DIAGNOSTIC_CANDIDATE_LOCKED` 永远不等于 `AUTHOR_ADOPTED_CANON`。

## Continuity authority

```text
Canon prose = what actually happened
Tracking = current story-state authority
PROJECT_STATE.md = production state + author locks + pointers
```

## Mandatory run ending

每次正式生产回复最后仍使用统一【生产进度】表，不单列 Source Shadow、Story Compose、Mother Mirror、Deslop、Canon、Tracking 等内部节点。

## Memory line

> **新窗口恢复原 Stage；S3 取得真实母本参考并统一验证正文候选。KKKK 自己生成时走完整 Story Compose；作者也可以明确发来外部 AI 候选。候选经硬检后，作者锁定诊断版本才运行 Mother Mirror：母本第一章做固定阅读镜、同位置母本做动态功能镜，候选+诊断同版本存档。只有作者采用后才 Canon / Tracking。**