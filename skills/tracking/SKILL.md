---
name: tracking
summary: "POST-PROSE STORY STATE OWNER. After author-approved prose, commit chapter state changes atomically, maintain the authoritative current story state, and render safe continuity views for S2/S3."
---

# Tracking v1.0｜章节事务 + 当前状态 + 安全读取视图

> status: production-main
> role: post-prose story continuity owner
> chapter_gate: `../references/chapter-progress-gate.md`
> emotional_causality: `../references/emotional-causality-contract.md`
> stage_scope_contract: `../references/stage-scope-and-progress-receipt.md`

## 0. Global stage boundary

即使本 Skill 被直接调用、没有先经过 `NOVEL_WORKFLOW_ENTRY.md`，也必须加载并服从：

`../references/stage-scope-and-progress-receipt.md`

```text
TRACKING_HAS_NO_NEW_PLOT_AUTHORITY
TRACKING_MUST_NOT_START_NEXT_CHAPTER_CREATION
MANDATORY_END_OF_RUN_PROGRESS_RECEIPT: true
```

当 Tracking 是由作者正文采用后的 `POST_ADOPTION_CLOSURE` 调用时，成功提交后必须直接交给 Chapter Progress Gate，不额外停下来请求作者批准。

## 1. First principle

Tracking 不是章节摘要。

```text
APPROVED PROSE
→ CHAPTER TRANSACTION
→ AUTHORITATIVE CURRENT STORY STATE
→ DERIVED READ VIEWS
```

正文负责“发生过什么”。
事务负责“这一章改变了什么”。
`_tracking-state.json` 负责“世界现在是什么状态”。
其他 Markdown 文件只是给不同阶段读取的投影视图。

禁止存在第二套可独立写入的连续性权威。

## 2. Canonical workspace

当前书默认维护：

```text
books/{ACTIVE_BOOK}/追踪/_tracking-state.json
books/{ACTIVE_BOOK}/追踪/上下文.md
books/{ACTIVE_BOOK}/追踪/角色状态/*.md
books/{ACTIVE_BOOK}/追踪/伏笔.md
books/{ACTIVE_BOOK}/追踪/时间线/作者真相.md
books/{ACTIVE_BOOK}/追踪/时间线/读者已知.md
books/{ACTIVE_BOOK}/追踪/事务/第NNN章*.json
```

其中：

```text
_tracking-state.json = machine authority for current state / revision
事务/*.json = immutable-or-revisioned state-change record
上下文 / 角色状态 / 伏笔 / 时间线 = derived read views
```

## 3. Admission

章后正式提交必须满足：

```text
CURRENT_CHAPTER_PROSE_COMPLETE: true
CURRENT_CHAPTER_TRACKING_COMMITTED: false
approved prose exists in Canon chapter file
previous tracking revision is readable
```

正文未被作者采用：

```text
TRACKING: BLOCKED
```

Tracking 不得从未批准候选正文提取 Canon。

## 4. Commit boundary

只能提交作者已经批准正文和既有 Canon 能证明的状态变化。

允许：

```text
人物位置 / 生死 / 受制状态
关系已经落地的变化
能力 / 物品 / 资源状态
谁知道什么
读者已经知道什么
作者真相中仍未公开的事实
现实未完成后果
伏笔当前状态
CURRENT_EMOTIONAL_RESIDUE when materially relevant
```

禁止：

```text
NEW_PLOT_AUTHORITY
NEW_FUTURE_SETUP_AUTHORITY
NEW_CHARACTER_DECISION_AUTHORITY
把“可能”写成“已经发生”
把作者真相泄漏进人物已知或读者已知
```

## 5. Epistemic separation

必须区分三层：

```text
AUTHOR TRUTH
CHARACTER KNOWLEDGE
READER KNOWLEDGE
```

`作者真相.md` 可以保存 Foundation 已锁但尚未公开的信息。
`读者已知.md` 只能保存正文已经让读者知道的信息。
角色状态中的“当前已知 / 未知”必须站在角色本人视角。

任何串线：

```text
TRACKING_COMMIT: FAIL
→ revision repair required
```

## 6. Emotional residue

服从 `../references/emotional-causality-contract.md`。

实质跨章余波优先存入对应角色状态，而不是另造一份散文记忆库：

```text
角色状态/{角色}.md
→ CURRENT_EMOTIONAL_RESIDUE
```

只保存会继续影响注意力、选择成本、行为或叙述口吻的余波。

```text
SCENE_CHANGE != EMOTIONAL_RESET
```

## 7. S2 read contract

S2 需要剧情研发权限，可以读取：

```text
_tracking-state.json
上下文.md
相关角色状态
伏笔.md
时间线/作者真相.md
时间线/读者已知.md
```

S2 可以使用作者真相设计剧情，但不得擅自公开未批准信息。

## 8. S3 safe read contract

S3 默认只读取：

```text
上下文.md
相关角色状态
时间线/读者已知.md
与当前章直接相关的当前状态
CURRENT_EMOTIONAL_RESIDUE
```

`时间线/作者真相.md` 默认不进入 Writer 上下文。
只有当前章已批准 Plot Block 明确允许揭示某事实时，才把该事实以最小必要形式交给 S3。

```text
AUTHOR_TRUTH_FULL_DUMP_TO_S3: forbidden
```

## 9. Atomic commit

Tracking 是多文件状态更新时，必须保持语义原子性。

优先：

```text
expected_state_revision check
→ build all changed blobs
→ one tree
→ one commit
→ move branch ref
→ post-commit verification
```

如果当前连接器不支持单提交原子更新：

```text
REPORT ATOMIC COMMIT BLOCKED
→ STOP
```

不得用多个普通 commit 假装一次 Tracking 原子提交。

事务必须记录：

```text
chapter
expected_state_revision
new_state_revision
state_changes
canon_story_changes
```

修正 Tracking 自身错误时使用 revision transaction，不改写故事史。

## 10. Verification

提交后至少验证：

```text
state_revision advanced exactly as intended
last_committed_chapter correct
chapter continuity has no gap
transaction expected revision matches previous state
current state agrees with approved prose
reader-known contains no author-only truth
character-known contains no author-only truth
CURRENT_EMOTIONAL_RESIDUE preserved when materially required
```

若旧官方 shell checker 没有实际运行，只能写：

```text
official_tracking_check: pending_shell_runtime
```

不得声称已通过未运行的 checker。

## 11. Output / routing

成功后：

```text
CURRENT_CHAPTER_TRACKING_COMMITTED: true
→ Chapter Progress Gate
```

如果当前调用属于：

```text
POST_ADOPTION_CLOSURE
```

则：

```text
TRACKING_COMMITTED
→ immediately run Chapter Progress Gate
→ if all gates pass: CHAPTER_COMPLETE
→ STOP
```

这里不需要再请求作者确认 Tracking 或 Chapter Gate。

如果 Tracking 是独立维护 / 修复调用，则完成后仍只报告状态，不得构思下一章。

无论哪种调用，Tracking 自己都不得开始下一章创作。

## Memory line

> **正文是历史事实，事务记录变化，Tracking 保存当前世界状态。S2 可读完整作者态，S3 只读安全视图；跨章情绪属于人物当前状态。所有多文件更新必须原子提交。作者采用正文后的闭环中，Tracking 成功后直接交给 Chapter Gate，不再重复问作者。**