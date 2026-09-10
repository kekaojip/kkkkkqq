# Source Shadow Runtime v1.1｜S3 母本同构场景转写

> status: production-main
> owner: `skills/prose-preparation/SKILL.md`
> story_authority: NONE
> prose_surface_authority: SOURCE_SHADOW_ONLY
> automatic_fallback: FORBIDDEN
> manual_compatibility_reference: `live-prose-calibration.md`

## 0. First principle

```text
APPROVED TARGET STORY
+ VERIFIED SAME-POSITION DONOR PROSE
→ homolog scene windows
→ copy-weighted transduction
→ target prose
```

目标不是让模型记住一个抽象“文风”，而是把真实母本同构场景放在 Writer 面前。

> **只要 Target 事实仍然为真，就尽量沿用母本真实的普通词、短语、句架、分句顺序、对白骨架、段落交接和局部呼吸。**

## 1. Authority order

```text
TARGET CANON / APPROVED PLOT / END STATE
> APPROVED CHARACTER + EMOTIONAL THREAD + CONTINUITY
> INHERITED DWELL
> VERIFIED DONOR HOMOLOG WINDOW
> SOURCE WORDING / SHORT PHRASES / SENTENCE FRAMES
> SOURCE LOCAL BREATH
> MODEL MINIMUM FILL ONLY WHEN SOURCE HAS NO CARRIER
```

没有自动第二 prose authority。

母本没有剧情权。Source 事实与 Target 冲突时必须替换或删除。

## 2. Source acquisition

服从：

- `../../references/source-corpus-acquisition.md`
- `single-prose-source-fidelity.md`

当前生产最小模式：

```text
S2 locked donor / mapped source range
→ acquire verified same-position donor body
→ split that body into local scene windows
→ use this body for PRIMARY Source Shadow
```

仓库若没有 ready 的 `reference-corpus/`：

```text
LOCAL_CORPUS_READY: false
→ approved external SOURCE ACQUISITION may retrieve current mapped donor body
→ Source Shadow may run on that verified body
```

这里的 external fallback 只表示“同一锁定母本正文从哪里取得”，**不是 prose-engine fallback**。

不得因为没有整本 corpus 就假装全书检索。

只有同一 author-locked donor 注册并满足 `LOCAL_CORPUS_READY: true` 后，才允许增加同 donor 其他章节的少量 alternate windows。

## 3. Scene window

基本执行单元：连续母本窗口，通常 3–7 段。

每个 Target macro event / natural event unit：

```text
PRIMARY HOMOLOG WINDOW: 1
ALTERNATES: 0–2 when legally available
```

优先同叙事功能、同压力/决定类型、同动作/对白/信息模式、同 Dwell、相似信息密度和呼吸。

不得主要因为关键词重合就选 window。

## 4. Writer packet

Writer 每个自然窗口只看：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT EMOTIONAL RESIDUE
DWELL WEIGHT
PRIMARY SOURCE WINDOW exact text
OPTIONAL ALTERNATE WINDOWS
SOURCE-SPECIFIC FACT BLACKLIST
LOCAL STOP CONDITION
```

禁止重新塞一大包抽象 Style Checklist。

## 5. Transduction

从 PRIMARY window 的实现路径开始。

事实兼容时优先保留：

```text
普通连接词 / 常用副词 / 句首方式
分句数量与顺序 / 问句或感叹形状
对白标签 / 动作结果顺序
短的常用表达 / 段落交接 / 局部句子承载
```

只替换 Target 必须变化的槽：人物、地点、物件、世界规则、能力、动作对象、因果、结果、关系、知识边界。

Source clause 无 Target 对应物：DELETE。

Target 必须事实无 Source 载体：用最近 source-compatible frame 做最小插入。

## 6. Story density / plot visibility

固定字数不压过：

```text
STORY COMPLETENESS + HOMOLOG STORY DENSITY
```

快速扫读关键段落必须能恢复事件链。

重复解释、二次证明、旁白认证和纯字数 filler 优先删除。

## 7. Source fact leak gate

必须：

```text
APPROVED_EVENT_ORDER: PASS
REQUIRED_EVENT_COVERAGE: PASS
CHARACTER_STATE: PASS
KNOWLEDGE_BOUNDARY: PASS
END_STATE: PASS
FORBIDDEN_REVEALS: 0
SOURCE_PROPER_NOUN_LEAK: 0
SOURCE_WORLD_FACT_LEAK: 0
SOURCE_POWER_LEAK: 0
SOURCE_RELATIONSHIP_LEAK: 0
SOURCE_EVENT_REPLACED_TARGET_EVENT: 0
```

高 wording overlap 本身不是失败。

## 8. Diagnostics

旧 v6 / sentence / boundary / surface：

```text
DISABLED BY DEFAULT
```

只有当前任务明确是旧结构调试 / 回归调查，或作者明确要求时才能运行。

即使运行也只有 warning 权，不得接管 prose generation，不得成为 style authority，不得触发另一个 writer skill。

```text
LEGACY_STRUCTURE_DIAGNOSTICS_AUTO_RUN: forbidden
```

## 9. Fail closed

以下情况不得假运行：

```text
SOURCE_ACQUISITION_STATUS: BLOCKED
SOURCE_TEXT_FIDELITY_STATUS: FAIL
WRONG_SOURCE_POSITION
NO_USABLE_HOMOLOG_WINDOW
SOURCE_SHADOW_VALIDATION_UNREPAIRABLE
```

处理：

```text
REPORT exact failure
→ repair owning layer when legal
→ still fail: S3 BLOCKED
→ STOP
```

正式生产禁止自动：

```text
LIVE_PROSE_FALLBACK
OLD_NATIVE_WRITER
INDEPENDENT_GOLDEN_DIRECT_EDIT
ARCHIVE_PROSE_SKILL
LEGACY_V6_WRITER
```

只有作者在当前任务明确点名要求兼容 fallback 时，才允许读取对应兼容参考，并必须显式记录 override。

## 10. Internal receipts

以下全部是 S3 内部动作，不新增作者审批：

```text
SOURCE_ACQUISITION_RECEIPT
SOURCE_POSITION_RECEIPT
WINDOW_SELECTION_RECEIPT
SOURCE_SHADOW_PACKET_RECEIPT
SOURCE_FACT_LEAK_RECEIPT
FIDELITY_DIAGNOSTIC_RECEIPT
```

默认还必须记录：

```text
SOURCE_SHADOW_ENGINE: required
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: false
COMPATIBILITY_ENGINE_USED: NONE
LEGACY_STRUCTURE_DIAGNOSTICS_USED: false
```

## Failure labels

```text
SOURCE_FACT_LEAK
WRONG_HOMOLOG
BASE_MODEL_DICTION_REBOUND
UNNECESSARY_SYNONYMIZATION
SOURCE_WINDOW_IGNORED
FILLER_FOR_LENGTH
MEDIAN_MUSH
PLOT_VISIBILITY_LOW
BREATH_MISMATCH
SOURCE_SHADOW_FALSE_PASS
SOURCE_SHADOW_AUTOMATIC_FALLBACK
LEGACY_SKILL_AUTO_RUN
```

## Memory line

> **先拿对当前母本正文，再找同构连续场景，尽量沿用真实的词和句架，只把必须变化的剧情槽换成我们的；跑不通就停，不自动换任何旧写作引擎。**
