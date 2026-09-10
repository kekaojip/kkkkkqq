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
  内部：Source Acquisition + Source Shadow + complete Story Compose + hard revalidation
↓
作者修改 / 重跑 / 采用
↓
作者正式采用正文
════════════
后台自动：Canon → Tracking → 本章完成
════════════
```

## S2

母本拆解、剧情块、人物块、情绪线继续由 `skills/story-material-engine/SKILL.md` 负责。剧情块形成后必须等待作者批准，人物块和必要情绪线同样遵守既有作者 Gate。

S2 还要保留当前目标章：

```text
SOURCE_IDENTITY
MAPPED DONOR CHAPTER / SUBRANGE
SOURCE DWELL when available
```

供 S3 Source Acquisition 使用。

## S3｜真实参考 + 原版 Story Compose

```text
APPROVED Plot
+ APPROVED Character
+ approved Emotional Thread when required
+ safe Tracking continuity
+ S2 locked donor position
→ Source Acquisition
→ verified same-position donor prose
→ Source Shadow exact reference packet
→ Story Compose production preflight
→ COMPLETE skills/story-compose/SKILL.md
→ FINAL COMPOSED PROSE
→ story truth / source leak / POV / endpoint hard recheck only
→ FULL PROSE CANDIDATE
→ AUTHOR REVIEW
```

唯一 S3 Owner / route：

```text
skills/prose-preparation/SKILL.md
→ skills/prose-preparation/routes/s3-source-shadow.md
```

S3 内部唯一成文编排器：

`skills/story-compose/SKILL.md`

完整接入合同：

`skills/prose-preparation/references/prose-writer-integration.md`

### Story Compose 是黑盒成文子流程

它不是 Stage Owner。KKKK 不直接调度其底层三个技能，也不重新写一份它的 Phase 1 / Phase 2 / Phase 3 顺序。

```text
PACKAGE_INTERNAL_FLOW_OWNER: story-compose/SKILL.md
STORY_COMPOSE_BYPASS_IN_PRODUCTION: forbidden
PACKAGE_CAPABILITY_REDUCTION: forbidden
```

完整包可以继续 standalone 使用；但 KKKK 正式生产必须先 preflight，只有完整依赖都在才允许进入。缺失时 STOP S3，不能使用 standalone fallback 静默降级。

### Production truth freeze

传给 Story Compose 的 Target 部分全部是必须遵守的批准真值；Source Shadow 部分只作表达参考。

```text
TARGET STORY TRUTH > SOURCE WORDING
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

因此通用网文建议不得在 production 中新增或重排已批准剧情。

### 返回后的 S3 只做硬检查

只验证：事件/结果/终态、人物与情绪连续性、POV/知识边界、新事实、Source 专属事实/识别性表达泄漏、后台元数据和首次阅读清晰度。

不得在 Story Compose 后再自动执行 Human Grain、全文自然化或第二正文引擎。

旧 `skills/human-grain-pass/**` 留作历史兼容和作者明确 A/B test，不属于 current production-main。

## S3 fail-closed

下列任一项失败且合法修复后仍失败：Source Acquisition、Source Shadow、Story Compose preflight、Story Compose 执行、最终硬真值复核，均：

```text
REPORT exact failure
→ STOP S3
```

不自动改用 Live Prose、Native Writer、Golden Direct Edit、archive prose skill 或其他 humanizer。

## Post-adoption closure

作者采用正文后：

```text
persist Canon
→ Tracking Commit
→ Chapter Progress Gate
→ CHAPTER_COMPLETE
```

成功时不新增作者确认。

## Continuity authority

```text
Canon prose = what actually happened
Tracking = current story-state authority
PROJECT_STATE.md = production state + author locks + pointers
```

## Mandatory run ending

每次正式生产回复最后仍使用统一【生产进度】表，不单列 Source Shadow、Story Compose、Deslop、Canon、Tracking 等内部节点。

## Memory line

> **新窗口恢复原 Stage；S3 取得真实母本参考并把完整 Target 输入交给 Story Compose 原包。Story Compose 自己完成成文流程，返回后只过硬真值 Gate；Human Grain 不再自动追加。**
