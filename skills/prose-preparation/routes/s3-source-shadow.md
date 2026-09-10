# S3 Source Shadow Route v3.0｜真实参考 + Story Compose 黑盒成文

> status: production-main
> owner: `../SKILL.md`
> source_runtime: `../references/source-shadow-runtime.md`
> source_fidelity: `../references/single-prose-source-fidelity.md`
> integration_contract: `../references/prose-writer-integration.md`
> prose_composer: `../../story-compose/SKILL.md`
> compatibility_auto_route: forbidden

## 0. One route

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY
+ INHERITED DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ Source Shadow exact reference windows
→ Story Compose production preflight
→ COMPLETE story-compose package
→ FINAL COMPOSED PROSE
→ hard story/source-leak/POV/endpoint validation only
→ full prose candidate
→ author review
```

Story Compose 是 S3 内部唯一成文编排器，不是新的 Stage Owner。

## 1. Admission

要求书籍基础、当前章、已批准 Plot / Character、必要情绪线齐全，且当前章正文尚未完成。读取 safe continuity / Canon、CURRENT_EMOTIONAL_RESIDUE、S2 donor identity / mapped range、inherited dwell。

S3 不重做剧情、人物、情绪线或 Dwell。

## 2. Source first

```text
S2 mapped donor position
→ VERIFIED SAME-POSITION SOURCE BODY
```

本地 corpus ready 时本地读取，否则走 approved source acquisition。失败且合法修复仍失败：REPORT → STOP。

不得拿摘要、聊天历史、模型记忆冒充 Source prose；不得自动换 Live Prose / Native Writer / Golden / archive prose skill。

## 3. Target / homolog windows

Target 只按自然连续事件划窗口，不按句数、段数、标点或固定字数配额。

每个 Target window 至少保留：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT EMOTIONAL RESIDUE
DWELL
LOCAL STOP CONDITION
```

从 verified donor 中选功能相近的连续 Source window，优先 narrative function、POV pressure、action/dialogue/information mode、dwell、density 和 local breath。

Source 高度同构可以提供较长真实参考，但不复制原句/原段、独特桥段、动作序列或识别性表达。无适用局部窗口就明确记录，不改变 Target 迁就 Source。

## 4. Build production packet

执行 `../references/prose-writer-integration.md`，把输入整理为：

```text
TARGET AUTHORITY PACKET
+ SOURCE SHADOW REFERENCE PACKET
```

TARGET 必须遵守；SOURCE 仅供表达参考。

```text
TARGET STORY TRUTH > SOURCE WORDING
APPROVED TARGET PLOT > GENERIC WEB-FICTION DEFAULTS
```

## 5. Story Compose preflight

在进入完整 Story Compose 前验证四个同级技能目录、必要 references、`story-compose/scripts/pipeline.sh`、三个 story-deslop 检测入口和 Node 条件。

```text
MISSING PACKAGE COMPONENT
→ STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT
→ STOP S3
```

正式生产禁止调用 Story Compose 的 standalone degradation fallback。

## 6. Complete package invocation

只调用：

`../../story-compose/SKILL.md`

包内如何组合 `novel-prose-writer-zh`、`human-writing-l2`、`story-deslop`，完全服从 Story Compose 自己的原版规则。

```text
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
STORY_COMPOSE_BYPASS: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION: FORBIDDEN
```

S3 不把这些底层技能分别拉出来再排一次，也不以摘要提示词替换任何原技能。

生产事实锁仍然优先：Story Compose 可以决定表达，不得新增事件/事实/动机/世界规则/关系/能力，不得改变事件顺序、POV 权限、Dwell 或章末终态。

## 7. Post-compose validation only

Story Compose 返回后只跑硬检查：

```text
PROSE INPUT FIREWALL
TARGET STORY TRUTH
EVENT ORDER / ENDPOINT
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE
NEW FACT INTRODUCTION = 0
SOURCE FACT LEAK = 0
SOURCE DISTINCTIVE EXPRESSION LEAK = 0
BACKSTAGE METADATA LEAK = 0
PLOT VISIBILITY / READER FIRST-PASS CLARITY
```

禁止：

```text
POST_COMPOSE_HUMAN_GRAIN
POST_COMPOSE_GENERAL_NATURALIZE
POST_COMPOSE_WHOLE_CHAPTER_POLISH
POST_COMPOSE_SECOND_PROSE_ENGINE
```

若硬真值失败，只修具体失败归属层；无法合法修复则 STOP。

## 8. Human Grain status

`../../human-grain-pass/**` 不删除，但 current production-main 不自动运行。只有作者明确要求 legacy/A-B test 才允许单独调用，并必须标明结果不是标准 Story Compose 主链输出。

## 9. Author-visible behavior

Source selection、packet、preflight、Story Compose 内部检测都不新增作者 Gate。作者只看完整正文候选。

## 10. Receipt

```text
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
STORY_COMPOSE_PREFLIGHT: PASS
PROSE_COMPOSER: story-compose
COMPOSER_INTERNAL_FLOW: package-owned
COMPOSER_DEGRADED_FALLBACK_USED: false
STORY_DESLOP_PIPELINE: PASS | BLOCKED
HUMAN_GRAIN_PRODUCTION_ROUTE: retired
S3_POST_COMPOSE_REWRITE: none
STORY_TRUTH_GATE: PASS
SOURCE_FACT_LEAK_GATE: PASS
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_GATE: PASS
POV_GATE: PASS
ENDPOINT_GATE: PASS
TARGET_PROSE_CANDIDATE: present
CANON_STATUS: NOT_ADOPTED
```

## Memory line

> **真实 Source Shadow → 完整 Story Compose 原包 → 硬真值复核。S3 不拆包、不重排、不追加 Human Grain。**
