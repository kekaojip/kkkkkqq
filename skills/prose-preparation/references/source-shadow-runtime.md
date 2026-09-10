# Source Shadow Runtime v2.0｜S3 真实母本参考层

> status: production-main
> owner: `skills/prose-preparation/SKILL.md`
> story_authority: NONE
> prose_surface_authority: NONE_REFERENCE_ONLY
> realization_core: `../../novel-prose-writer-zh/SKILL.md`
> automatic_fallback: FORBIDDEN
> manual_compatibility_reference: `live-prose-calibration.md`

## 0. First principle

```text
APPROVED TARGET STORY
+ VERIFIED SAME-POSITION DONOR PROSE
→ homolog scene windows
→ exact reference packet with applicability / isolation
→ complete novel-prose-writer-zh
→ target prose
```

目标不是让模型记住一个抽象“文风”，而是把真实母本同构场景放在 Writer 面前。

> **保留真实原文，让 Writer 参考句子怎样向前、对白怎样接、心理在哪里停及段落呼吸。普通词和常见表达可自然使用；原句、独特表达、桥段与动作序列不得通过换槽复制。**

## 1. Authority order

```text
TARGET CANON / APPROVED PLOT / END STATE
> APPROVED CHARACTER + EMOTIONAL THREAD + CONTINUITY
> INHERITED DWELL
> COMPLETE novel-prose-writer-zh REALIZATION
> VERIFIED DONOR REFERENCE WHEN APPLICABLE
```

Source 没有 Target 表面决定权；完整原技能是唯一正文执行核心。不得将原技能或母本正文抽成摘要后替代原件。

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

基本参考单元：保留足够上下文的连续母本原文。按自然场景边界取用，不规定固定段数，也不据此规定 Target 分段。

每个 Target macro event / natural event unit：

```text
PRIMARY HOMOLOG WINDOW: 1
ALTERNATES: 0–2 when legally available
```

优先同叙事功能、同压力/决定类型、同动作/对白/信息模式、同 Dwell、相似信息密度和呼吸。

不得主要因为关键词重合就选 window。`../runtime/source_shadow_packet.py` 只做候选检索，分数不是同构验证，不能自动把最高分窗口视为已批准参考。无适用局部窗口时记录 `NO_APPLICABLE_LOCAL_REFERENCE`，不硬套；这不豁免真实来源取得与其余参考准备。

## 4. Writer packet

参考包附在完整 Target 材料之后；以下是窗口级辅助信息，不得代替或删薄已批准人物/剧情原内容：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT EMOTIONAL RESIDUE
DWELL WEIGHT
PRIMARY SOURCE WINDOW exact text
OPTIONAL ALTERNATE WINDOWS
SOURCE-SPECIFIC FACT / DISTINCTIVE EXPRESSION ISOLATION
SOURCE PROVENANCE / APPLICABILITY / NON-APPLICABILITY
LOCAL STOP CONDITION
```

禁止重新塞一大包抽象 Style Checklist。

## 5. Reference use; no transduction command

Source 可提供真实普通词、常见短语、常见句式、对白接法、连接方式、叙述密度及局部呼吸参考。不要关闭原文后只给 Writer 一份抽象风格画像，也不要输出必须照抄的词频清单或固定句架。

完整 Writer 按 Target 当前事实、人物、POV 和场景需要决定实际表达。与 Target 不适用的 Source 文字不使用；Target 必须内容没有相应 Source 载体时，在批准边界内自然写出，不受“只许最小补写”限制。

隔离 Source 人名、地名、世界规则、能力、关系、独有记忆、事实与结果；同时隔离独特比喻、桥段、原句、识别性表达和情节动作序列。不能只检查专名。常见中文表达偶然相同不是失败，也不要求刻意同义词化。

具体中文写法完整服从 `../../novel-prose-writer-zh/SKILL.md` 及其必要 references；本层不另造正文规则。

## 6. Story density / plot visibility

固定字数不压过：

```text
STORY COMPLETENESS + TARGET NEEDS + APPLICABLE SOURCE DENSITY REFERENCE
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
SOURCE_DISTINCTIVE_EXPRESSION_LEAK: 0
SOURCE_DISTINCTIVE_SCENE_OR_ACTION_SEQUENCE_IMPORT: 0
```

常用词偶然重合不是失败；大段或识别性表达重合必须人工核查，不能以“事实兼容”放行。n-gram 统计只提示检查位置，不证明原创性或抄袭，也不要求提高重合率。

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
SOURCE_SHADOW_REFERENCE: required
PROSE_REALIZATION_CORE: novel-prose-writer-zh
LOCAL_REFERENCE_STATUS: APPLICABLE | NO_APPLICABLE_LOCAL_REFERENCE
AUTHOR_EXPLICIT_COMPATIBILITY_OVERRIDE: false
COMPATIBILITY_ENGINE_USED: NONE
LEGACY_STRUCTURE_DIAGNOSTICS_USED: false
```

## Failure labels

```text
SOURCE_FACT_LEAK
WRONG_HOMOLOG
SOURCE_DISTINCTIVE_EXPRESSION_LEAK
SOURCE_REFERENCE_FALSE_USE
WRITER_CORE_NOT_LOADED
WRITER_SKILL_SUMMARY_SUBSTITUTION
FILLER_FOR_LENGTH
MEDIAN_MUSH
PLOT_VISIBILITY_LOW
BREATH_MISMATCH
SOURCE_SHADOW_FALSE_PASS
SOURCE_SHADOW_AUTOMATIC_FALLBACK
LEGACY_SKILL_AUTO_RUN
```

## Memory line

> **先拿对当前母本正文，再提供真实连续参考及隔离信息；完整原技能决定 Target 表达。不得硬套不适用窗口、换槽复制或用风格摘要替代原文。来源/技能读取失败仍停止。**
