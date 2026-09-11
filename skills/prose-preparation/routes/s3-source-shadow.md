# S3 Source Shadow Route v4.0｜真实参考 + 统一正文候选入口

> status: production-main
> owner: `../SKILL.md`
> source_runtime: `../references/source-shadow-runtime.md`
> source_fidelity: `../references/single-prose-source-fidelity.md`
> integration_contract: `../references/prose-writer-integration.md`
> internal_prose_composer: `../../story-compose/SKILL.md`
> compatibility_auto_route: forbidden

## 0. One route, two candidate sources

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CHAPTER EMOTIONAL THREAD when required
+ SAFE CONTINUITY
+ CURRENT_BLOCK
+ SCAN_COORDINATES
+ INHERITED DWELL
+ VERIFIED SAME-POSITION DONOR PROSE
→ Source Shadow exact reference windows
→ ONE PROSE CANDIDATE SOURCE
   A. KKKK_GENERATED_PROSE
      → Story Compose production preflight
      → COMPLETE story-compose package
   B. AUTHOR_EXTERNAL_PROSE_CANDIDATE
      → author explicitly supplies/selects prose
      → no Story Compose invocation for this candidate
→ UNIFIED S3 HARD VALIDATION
→ FULL PROSE CANDIDATE
→ author may lock this version for Mother Mirror
```

解释：

```text
KKKK_GENERATES_PROSE → Story Compose mandatory
AUTHOR_SUPPLIES_PROSE → external candidate intake allowed
```

作者外部候选不是 KKKK 自行绕过 Story Compose 换引擎，不得标记为 Story Compose 输出。

## 1. Admission

要求：

```text
BOOK_CONSTRUCTION_STATUS: PASS
CURRENT_TARGET_CHAPTER: known
CURRENT_CHAPTER_PLOT_BLOCK_COMPLETE: true
CURRENT_CHAPTER_CHARACTER_BLOCK_COMPLETE: true
CHAPTER_EMOTIONAL_THREAD: approved when required
CURRENT_BLOCK: readable
SCAN_COORDINATES: present
CURRENT_CHAPTER_PROSE_COMPLETE: false
```

同时读取 safe continuity / Canon、CURRENT_EMOTIONAL_RESIDUE、S2 donor identity / mapped range、inherited dwell。

S3 不重做剧情、人物、情绪线、BLOCK 或 Dwell。

## 2. Source first

```text
S2 mapped donor position
→ VERIFIED SAME-POSITION SOURCE BODY
```

优先按 `../../references/source-corpus-acquisition.md` 取得真实 Source。已存在 verified repository anchor/cache 时可直接使用其精确章节范围；缺失时走正常 Source Acquisition。

禁止用摘要、聊天记忆、Human Retelling 或模型记忆冒充 Source prose。

## 3. Target / homolog windows

Target 只按自然连续事件划窗口，不按句数、段数、标点或固定字数配额。

每个 Target window 至少保留：

```text
TARGET FACTS NOW
CURRENT POV STATE
CURRENT_EMOTIONAL_RESIDUE
DWELL
LOCAL STOP CONDITION
```

Source 只提供普通中文连接、对白接法、信息密度、局部呼吸与叙事功能参考。不得复制专属事实、独特比喻、动作序列、桥段或识别性表达。

```text
TARGET STORY TRUTH > SOURCE WORDING
```

## 4. Candidate source A｜KKKK generated prose

仅当 KKKK 被要求自己生成正文：

```text
PROSE_CANDIDATE_ORIGIN: STORY_COMPOSE
```

先验证完整 Story Compose 包、必要 references、`pipeline.sh`、story-deslop 检测入口和 Node 运行条件。

缺失：

```text
STORY_COMPOSE_PREFLIGHT: BLOCKED
→ REPORT exact dependency
→ STOP INTERNAL GENERATION
```

完整包调用唯一入口：

`../../story-compose/SKILL.md`

```text
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
STORY_COMPOSE_BYPASS_WHEN_KKKK_GENERATES_PROSE: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION: FORBIDDEN
```

S3 不拆包、不重排、不以摘要技能替代原包能力。

## 5. Candidate source B｜Author external prose

当作者明确提供或选择由其他 AI / 自己写出的正文：

```text
PROSE_CANDIDATE_ORIGIN: AUTHOR_EXTERNAL_PROSE_CANDIDATE
AUTHOR_EXPLICITLY_SUPPLIED_OR_SELECTED: true
STORY_COMPOSE_INVOKED_FOR_THIS_CANDIDATE: false
STORY_COMPOSE_BYPASS_VIOLATION: false
```

外部候选只有表达权，没有剧情权、设定权、人物权、Canon 权或 Tracking 权。

不得因为来源外部而跳过 Source Shadow、真值边界或下面的统一硬复核。

## 6. Unified hard validation

无论候选来源，统一检查：

```text
OUTPUT COMPLETENESS / ENDPOINT
PROSE INPUT FIREWALL
TARGET STORY TRUTH / EVENT ORDER
CHARACTER / EMOTIONAL CONTINUITY
POV / KNOWLEDGE BOUNDARY
NEW FACT INTRODUCTION = 0
SOURCE FACT LEAK = 0
SOURCE DISTINCTIVE EXPRESSION LEAK = 0
BACKSTAGE METADATA LEAK = 0

J_CLEAR_FIRST_READ
J_ENDPOINT_STOP
J_CHAPTER_LENGTH
J_BLOCK_PROGRESS
J_SCAN_STORY
```

退役旧 KPI 不得恢复：

```text
BRAIN/HISTORY 字数下限
PANEL_LINES 数量/区间
SYSTEM_SCENES 数量下限
EXCLAMATION 数量/区间
DIALOGUE 百分比目标
BURST 五拍硬门
每章强制宣言
按 SIM/REALITY/MIX 强制开结尾形态
```

若输入层本身事件/坐标不足，返回 S2；若输入完整但正文把事件埋住，标记 `OWNER: PROSE_REALIZATION`。外部候选不得被 S3 偷偷全文改写。

## 7. Post-candidate behavior

禁止：

```text
POST_CANDIDATE_HUMAN_GRAIN
POST_CANDIDATE_GENERAL_NATURALIZE
POST_CANDIDATE_WHOLE_CHAPTER_POLISH
POST_CANDIDATE_SECOND_PROSE_ENGINE
```

Story Compose 内部候选只允许原包自身定义的局部修复；外部候选由作者决定是否回外部 AI 重写、局部修、换版或放弃。

## 8. Mother Mirror handoff

S3 硬复核通过仍不等于 Canon。

作者明确说“拿这版跑诊断”或等价意思：

```text
DIAGNOSTIC_CANDIDATE_LOCKED: true
CANON_STATUS: NOT_ADOPTED
→ ../../mother-prose-contrast/SKILL.md
```

Mother Mirror 不属于 S3 硬门，不自动改写。完成后候选正文与诊断报告按同一版本号存入生产记录。

## 9. Author-visible behavior

Source Acquisition、Source Shadow、候选来源分叉、Story Compose preflight、Mother Mirror 都属于“正文”阶段内部动作，不新增作者可见 Stage 或进度行。

## 10. Receipt

```text
SOURCE_ACQUISITION: PASS
SOURCE_POSITION: verified
SOURCE_SHADOW_PACKET: present
CURRENT_BLOCK: present
SCAN_COORDINATES: present
PROSE_CANDIDATE_ORIGIN: STORY_COMPOSE | AUTHOR_EXTERNAL_PROSE_CANDIDATE | AUTHOR_MANUAL
STORY_COMPOSE_PREFLIGHT: PASS | NOT_APPLICABLE_EXTERNAL_CANDIDATE
STORY_COMPOSE_INVOKED_FOR_THIS_CANDIDATE: true | false
STORY_TRUTH_GATE: PASS | FAIL
SOURCE_FACT_LEAK_GATE: PASS | FAIL
SOURCE_DISTINCTIVE_EXPRESSION_LEAK_GATE: PASS | FAIL
POV_GATE: PASS | FAIL
CLEAR_FIRST_READ: PASS | FAIL
ENDPOINT_STOP: PASS | FAIL
CHAPTER_LENGTH: PASS | FAIL
BLOCK_PROGRESS: PASS | FAIL
SCAN_STORY: PASS | FAIL
SCAN_STORY_SUMMARY: "谁做了什么，结果什么变了"
TARGET_PROSE_CANDIDATE: present
DIAGNOSTIC_CANDIDATE_LOCKED: false until author says so
MOTHER_MIRROR_STATUS: NOT_RUN until candidate lock
CANON_STATUS: NOT_ADOPTED
```

## Memory line

> **真实 Source Shadow 之后允许两种候选来源：KKKK 自己写必须走完整 Story Compose；作者明确提供外部正文则直接作为外部候选。两者统一过 S3 真值/扫读硬检，作者锁定版本后才进入 Mother Mirror，采用后才 Canon / Tracking。**