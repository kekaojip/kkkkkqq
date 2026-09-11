# WORKFLOW ORDER LOCK｜正式生产流程顺序锁定契约

> status: AUTHOR_LOCKED_INVARIANT
> authority: 作者明确指令（2026-09-11；2026-09-12 追加外部正文候选 + Mother Mirror 诊断）
> 说明：本文件锁定正式小说生产的完整流程顺序。**顺序一经锁定，不得重排、不得跳过、不得简化、不得替换**。只有作者在当前对话中明确修改，才允许更新本顺序。

## 0. 为什么锁

- 防止凭聊天记忆/旧版本经验“跳步”或“换序”生产。
- 防止把 Story Compose 黑盒拆开重拼。
- 防止作者不可见步骤膨胀或作者可见流程被压缩。
- 保证每一章都走同一套可复现的正式链路。
- 允许作者明确提供外部 AI 正文候选，但不把它伪装成 KKKK 内部生成结果。

```text
ORDER_LOCK: AUTHOR_LOCKED_INVARIANT
REORDER: FORBIDDEN
SKIP: FORBIDDEN
SIMPLIFY: FORBIDDEN
IMPLICIT_SUBSTITUTION: FORBIDDEN
MEMORY_AS_SOURCE: FORBIDDEN
ADOPTION_BY_AI: FORBIDDEN
```

## 1. 每次正式生产启动（固定顺序）

```text
①读取 AGENTS.md
②读取 PRODUCTION_CONTRACT.md
③读取本文件 WORKFLOW_ORDER_LOCK.md
④读取 .active-book → 解析 ACTIVE_BOOK
⑤读取 books/{ACTIVE_BOOK}/PROJECT_STATE.md
⑥读取 tracking 状态（追踪/_tracking-state.json 当存在时）
⑦从 PROJECT_STATE 的 NEXT_TARGET_CHAPTER 恢复，禁止从聊天历史猜进度
```

## 2. 每章正式生产主序（固定，不可改动）

```text
STEP 1  S1（仅新书）── 书籍基础
        skills/book-construction/SKILL.md
        作者 seed → 提取明确信号 → Fire 研究 → S1_PRE_CANDIDATE_RESEARCH_GATE
        → Book Kernel / Presentation / Foundation / 初始 Tracking
        → 作者确认 → BOOK_CONSTRUCTION_STATUS: PASS

STEP 2  S2 ── 母本拆解
        skills/story-material-engine/SKILL.md + references/human-retelling-core.md
        抓真实正文（Fire/浏览器/作者提供文件均可，不许拿简介冒充）
        → RETELLING_BRIDGE_NODES → HUMAN_RETELLING_CORE → COVERAGE_GATE
        → CHARACTER TRACE
        → 拆解结论登记进 skills/simulator-novel-knowledge/

STEP 3  S2 ── 剧情块 Plot Block
        读取 CURRENT_BLOCK
        → 构建中粒度连续剧情块
        → 提取 SCAN_COORDINATES（只算新事实/新信息/新决定/新结果）
        → plot-block-shot-gate.md 可拍性门
        → PLOT_BLOCK_SHOT_GATE: PASS
        → 作者确认

        禁止恢复以下退役旧硬门：
        BRAIN/HISTORY 字数下限 / PANEL_LINES / SYSTEM_SCENES 数量 / EXCLAMATION 数量 /
        DIALOGUE 比例 / 爆点五拍硬门 / 每章强制宣言 / 按章节类型强制换开结尾。

STEP 4  S2 ── 人物块 Character Block
        谁/想要什么/阻碍/选择/变化 + 当前知识边界与声口
        → 作者确认

STEP 5  S2 ── 章节情绪线 Emotional Thread（有实质情绪变化时）
        极薄四行：起点/压力变化/终点/残留
        → 作者确认（必要时）

STEP 6  S3 ── Source Acquisition + Source Shadow
        skills/prose-preparation/SKILL.md + routes/s3-source-shadow.md
        取得已验证同位置母本正文 → SOURCE SHADOW 精确参考包
        （隔离源专有设定/人名/机制/原句；只借鉴表达功能层）
        → SOURCE_SHADOW_PACKET: present

STEP 7  正文候选来源
        允许两条合法来源，但都必须回到同一 S3 真值/扫读硬复核：

        ROUTE A｜KKKK 内部生成
        → Story Compose production preflight
        → 校验 story-compose + novel-prose-writer-zh + human-writing-l2 + story-deslop + Node
        → 缺失：BLOCKED → REPORT → STOP INTERNAL GENERATION
        → 完整 Story Compose 原包调用（唯一内部生成入口）
        → 包内 Phase1 / Phase2 / Phase3 按原包规则执行

        ROUTE B｜作者外部正文候选
        → 作者明确提供 / 选择由其他 AI 或自己写出的正文
        → 标记 AUTHOR_EXTERNAL_PROSE_CANDIDATE
        → 不运行 Story Compose 来伪造来源

        解释：
        KKKK_GENERATES_PROSE → Story Compose mandatory
        AUTHOR_SUPPLIES_PROSE → external candidate intake allowed

STEP 8  S3 ── 所有候选统一硬复核
        无论候选来自 ROUTE A / B，统一检查：
        - Target story truth / event order / endpoint
        - character / emotional continuity
        - POV / knowledge boundary
        - new fact = 0
        - source fact / distinctive-expression leak = 0
        - backstage metadata leak = 0
        - CLEAR_FIRST_READ
        - ENDPOINT_STOP
        - CHAPTER_LENGTH
        - BLOCK_PROGRESS
        - SCAN_STORY

        失败 → 修 owning layer；不在 S3 表面全文润色。
        禁止 post-compose 二次全文自然化 / Human Grain 自动追加。

STEP 9  作者锁定诊断候选
        作者明确说“拿这版跑诊断”或等价意思
        → DIAGNOSTIC_CANDIDATE_LOCKED: true
        → 这不等于 AUTHOR_ADOPTED_CANON

STEP 10 Mother Mirror ── 母本镜像诊断
        skills/mother-prose-contrast/SKILL.md
        → FIXED_ANCHOR = M01 Chapter 1
        → POSITION_ANCHOR = 当前 mapped donor chapter / verified subrange
        → 只诊断：STORY_VISIBILITY / EVENT_MOTION / DIALOGUE_CARRY /
          PANEL_CARRY / EXPLANATION_LOAD / SCREEN_RHYTHM
        → 输出 KEEP / MATERIAL GAP + OWNER / NO_ACTION_REQUIRED / SCAN SUMMARY
        → 不评分、不模仿、不自动改写、不自动采用

STEP 11 候选 + 诊断同版本存档
        优先一次原子 Git 提交：
        books/{ACTIVE_BOOK}/生产记录/正文候选_第NNN章_vK.txt
        books/{ACTIVE_BOOK}/生产记录/母本镜像诊断_第NNN章_vK.md

        保存后：
        CANON_STATUS: NOT_ADOPTED
        TRACKING_WRITE: none
        CHAPTER_COMPLETE: false

STEP 12 作者 review → 修改 / 重跑 / 换版 / 明确采用
        adoption 是作者权限，禁止 AI 代“采用”。
        新版本正文必须使用新的 candidate version，再跑对应诊断后方可替代旧版本。

STEP 13 后台闭环（仅作者明确采用后，无额外作者确认步骤）
        selected candidate → Canon persist
        → Tracking commit（原子，revision 递增，事务文件）
        → Chapter Progress Gate
        → CHAPTER_COMPLETE → NEXT_CHAPTER_ALLOWED

STEP 14 每次回复末尾使用【生产进度】表
        只显示作者可见项：书籍基础/母本拆解/剧情块/人物块/章节情绪线/正文
        不单列 Source Shadow / Story Compose / Mother Mirror / Deslop / Canon / Tracking 等内部节点
```

## 3. Mother Mirror 边界锁

```text
MOTHER_MIRROR_STAGE_OWNER: false
MOTHER_MIRROR_HARD_GATE: false
MOTHER_MIRROR_SCORE: forbidden
MOTHER_MIRROR_AUTO_REWRITE: forbidden
MOTHER_MIRROR_SOURCE_PHRASE_COPY: forbidden
MOTHER_MIRROR_CANON_ADOPTION: forbidden
```

Mother Mirror 发现的差异不自动等于缺陷。只有真正影响剧情显形、扫读、首读清晰度的差异才列 GAP。

如果 Mother Mirror 发现的问题同时触犯 STEP 8 现有硬门：

```text
HARD_GATE_CONFLICT: true
→ return to existing owning layer
```

不得因此发明第六个硬门。

## 4. 外部正文候选边界锁

允许作者使用其他 AI 生成正文，但必须满足：

```text
AUTHOR_EXPLICITLY_SUPPLIES_OR_SELECTS_CANDIDATE: required
EXTERNAL_CANDIDATE_IS_NOT_CANON: true
S3_HARD_REVALIDATION: required
MOTHER_MIRROR_AFTER_DIAGNOSTIC_LOCK: required before standard candidate persistence
AUTHOR_ADOPTION_REQUIRED_FOR_CANON: true
```

禁止把“作者发来一版正文”自动解释成“作者已经采用”。

## 5. 禁止事项（硬）

```text
STORY_COMPOSE_BYPASS_WHEN_KKKK_GENERATES_PROSE: FORBIDDEN
PACKAGE_INTERNAL_REORDER: FORBIDDEN
PACKAGE_CAPABILITY_REDUCTION: FORBIDDEN
PACKAGE_SKILL_SUMMARY_SUBSTITUTION: FORBIDDEN
DIRECT_BOTTOM_SKILL_RECOMPOSITION_BY_KKKK: FORBIDDEN
HUMAN_GRAIN_AUTO_ROUTE: FORBIDDEN
LEGACY_SKILL_AUTO_FALLBACK: FORBIDDEN
LIVE_PROSE_AUTOMATIC_FALLBACK: FORBIDDEN
AUTHOR_VISIBLE_STEP_SKIP: FORBIDDEN
ADOPTION_BY_AI: FORBIDDEN
AUTHOR_VISIBLE_STEP_INFLATION: FORBIDDEN
PROGRESS_ROW_EXPANSION: FORBIDDEN
MOTHER_MIRROR_AUTO_REWRITE: FORBIDDEN
```

## 6. 修改权

- 本顺序只能由作者在当前对话中明确指令修改。
- 作者未明确指令时，任何内部“优化建议”都不构成改序理由。
- 顺序出现在多个文件（本文件/AGENTS.md/NOVEL_WORKFLOW_ENTRY.md/PRODUCTION_MAP.md）时，**本文件为主序真源**，其余只做引用，不得自行产生第二套顺序。

## Memory line

> **生产顺序锁更新：S1 → 母本拆解 → 剧情块（BLOCK+SCAN）→ 人物块 → 情绪线 → Source Shadow → 正文候选来源（内部 Story Compose 或作者外部候选）→ 统一 S3 硬复核 → 作者锁定诊断候选 → Mother Mirror 双镜诊断 → 候选+诊断同版本存档 → 作者采用 → Canon/Tracking/Chapter Gate。Mother Mirror 只诊断不改写，外部候选不自动等于 Canon。**