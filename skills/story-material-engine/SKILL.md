---
name: story-material-engine
description: "PRODUCTION STAGE 2 OWNER. Grow the author's current story idea through continuous natural human-AI co-creation with search-backed creative replies. Default output target: simple, readable, pleasure-first web-fiction story with relaxed-and-exciting rhythm and only enough realism to avoid immersion breaks."
---

# Story Material Engine v9.5｜S2 连续共创 + 爽文优先 + 章节情绪线 + 真人复述拆书桥

> status: production-main
> stage: S2
> owns: TARGET STORY CO-CREATION + SEARCH-BACKED STORY REASONING + ON-DEMAND DEEP FICTION RESEARCH + HUMAN RETELLING SOURCE BREAKDOWN + STORY APPROVAL + CHAPTER CUT + CHAPTER EMOTIONAL THREAD
> story_room: `references/story-room.md` v2.1+
> fiction_case_research: `references/fiction-plot-case-retrieval.md` v1.1+
> human_retelling_core: `references/human-retelling-core.md` v1.1+ AUTHOR_LOCKED
> emotional_causality: `../references/emotional-causality-contract.md`
> repair_threshold: `references/novel-repair-threshold.md`
> author_step_gate: `../references/author-visible-step-gate.md`

## 0. Global aesthetic inheritance

Stage 2 必须继承全局底线：

```text
纯小白
纯简单
纯好读
纯爽
```

第一目标：

> **让读者看得舒服、看得爽、愿意继续看。**

剧情判断优先级：

```text
1. 好不好看
2. 爽不爽
3. 顺不顺
4. 有没有松弛与变化
5. 人物和因果是否合理到不出戏
6. 重要事件留下的情绪有没有继续影响后面
```

不是：

```text
够不够深刻
够不够复杂
主题是否完整
设定是否解释到论文级
现实主义是否最严密
```

硬规则：

```text
PLEASURE_FIRST: true
LOW_COGNITIVE_LOAD: preferred
SIMPLE_CAUSALITY: preferred
RELAXED_AND_EXCITING_RHYTHM: required
REASONABLE_ENOUGH_NOT_TO_BREAK_IMMERSION: required
COMPLEXITY_FOR_COMPLEXITY: forbidden
PAPER_LIKE_RIGOR: forbidden
```

“爽”不等于一直爆。

```text
爽点 / 反应 / 收获 / 压制 / 新鲜能力
↕
日常 / 玩梗 / 轻松互动 / 探索 / 喘气
↕
再进入下一轮值得期待的东西
```

张弛由作者最终掌控。AI 不得自动把每段都压成高强度高潮，也不得为了“高级感”把故事写沉。

---

## 1. Mission

Stage 2 只回答：

> **这一段故事，我们真正想看什么，而且具体发生什么？这些事连续落到人物身上以后，他带着什么感觉走到章尾？**

正常生产不是阶段问答，而是连续共创：

```text
作者说一点
↕
与当前问题直接相关的搜索校准
↕
AI 顺着想 / 显影 / 推演
↕
作者继续补、改、反驳、转向
↕
卡住时 AI 才主动扩思路
↕
需要更深案例刺激时调用小说案例研究
↕
若实际拆某本小说 / 某个剧情块：必须先做 Human Retelling Core
↕
只把有用、简单、能直接提升故事体验的东西带回来
↕
继续共同把故事长完整
→ current chapter Plot Block（构建后必须过 `references/plot-block-shot-gate.md` 可拍性门）
→ current chapter Character Block
→ thin Chapter Emotional Thread when materially relevant
→ S3 handoff
```

S2 不写正文。

> **Plot Block Shot Gate**：剧情块收束后必须执行 `references/plot-block-shot-gate.md` 分镜预检——每个节点都要是"谁 + 物件/处境 + 动作/对白 + 局势变化"的可拍镜头；抽象状态词（情绪到顶点/局势升级/心理博弈等）禁止当节点；情绪只能做镜头余波。这是 S3 正文"一眼能看到剧情"的输入层保障。

> **模拟器文规约（V3.1）**：本书系为模拟器文专用模式（见 `../references/simulator-novel-production-contract.md`）。S2 每章先读取 `CURRENT_BLOCK`，再用 `SCAN_COORDINATES` 锁定“这一章真正发生什么”；重大爆点要真实发生并改变局势，但不再按“五拍”生产；宣言、面板、对白、情绪表达均按剧情需要使用，不设数量配额。

---

## 2. First principles

### 2.1 Author idea is primary

作者自然语言本身就是正式创意输入。

禁止先编译成 plot function / strategy / DNA / reader matrix / state delta。

### 2.2 No option-machine workflow

正式禁止：

```text
AI 默认给 3..5 方案
A/B/C 选择
每一步都让作者审批编号
案例 A/B/C 请挑选
```

作者还在主动思考时：FOLLOW AUTHOR。
作者模糊时：HELP MAKE EXISTING IDEA CLEARER。
作者卡住 / 明确要求拓展时：AI MAY EXPAND NATURALLY。

默认先给当前最值得尝试的一条具体延伸，必要时再补少量相邻可能，不要求编号选择。

### 2.3 Formal creative replies are search-backed

只要当前回复会新增具体剧情建议、判断剧情逻辑、补人物动机 / 世界反应 / 后果、建议推进、判断同人 Canon、提供创意启发，默认：

```text
S2_FORMAL_CREATIVE_REPLY_SEARCH_REQUIRED: true
PREFERRED_SEARCH_PLUGIN: Firecrawl
```

搜索必须围绕当前具体问题，不得为打勾而搜无关内容。

纯确认、逐字复述、格式转换、无外部创意判断的 repo/file 状态回复可不搜。

### 2.4 Search is evidence, not complexity

搜索结果可以帮助：

```text
避免明显 Canon 错误
发现好用的爽点处理
找到更自然的人物反应
验证简单因果是否说得过去
```

不得因为搜到了复杂解释，就把故事强行复杂化。

```text
SEARCH_COMPLEXITY
!= STORY_COMPLEXITY_REQUIREMENT
```

### 2.5 Reasonability floor

合理性标准只要求：

```text
人物行为不明显犯蠢
动机基本说得通
因果能顺着理解
世界规则不明显打架
```

如果为了修一个小问题需要新增大量解释、设定、阴谋或抽象层：

```text
SIMPLIFY_FIRST
```

### 2.6 Human Retelling before source analysis

当作者要求：

```text
拆书
拆开局
拆剧情块
找一本小说看它第一段怎么走
调研某本书具体剧情
真人复述来源剧情
```

必须加载：

`references/human-retelling-core.md`

并遵守：

```text
SOURCE / NOVEL
→ find a coherent story block
→ RETELLING_BRIDGE_NODES
→ HUMAN_RETELLING_CORE
→ RETELLING_BRIDGE_COVERAGE_GATE
→ analysis only after the story itself is concretely retold
```

作者前台默认先看到的是：

> **一大段像真人看完后第二天讲给朋友听的连续剧情复述。**

必须保留真正承担因果转接的具体东西：

```text
谁当时是什么处境
谁先做了什么
说了什么 / 想要什么（若会改变剧情）
对方怎么反应
什么具体事实逼出了下一步
中间发生了什么变化
最后结果怎样
```

禁止把它替换成：

```text
遭遇危机
信息差
心理博弈
局势升级
能力觉醒
身份跃迁
完成反杀
获得成长
```

这些词只能用于后续解释，不能代替剧情。

Author lock：

```text
RETELLING_BRIDGE_LOCK: AUTHOR_LOCKED_INVARIANT
AUTO_WEAKEN: FORBIDDEN
AUTO_REMOVE: FORBIDDEN
OPTIMIZATION_OVERRIDE: FORBIDDEN
VERSION_UPGRADE_OVERRIDE: FORBIDDEN
```

任何未来重构 / 迁移 / 精简都不得把 Human Retelling Core 再降级为“仅保留、不默认调用”，除非作者明确要求。

### 2.7 Emotional causality is part of story causality

加载：

`../references/emotional-causality-contract.md`

S2 不替正文写情绪，但必须在章节材料收束时检查：重要事件连续发生以后，人物是否真的带着前面的影响进入后面的节点。

```text
SCENE_CHANGE != EMOTIONAL_RESET
PLOT_CAUSALITY_WITHOUT_EMOTIONAL_CAUSALITY: forbidden by default
```

不要为此新增情绪矩阵、强度分数或每节点标签。

---

## 3. Admission

进入 S2 读取：

```text
books/{ACTIVE_BOOK}/PROJECT_STATE.md when active book exists
current Foundation / Canon / CURRENT_STATE
CURRENT_EMOTIONAL_RESIDUE from prior chapter when present
../references/emotional-causality-contract.md
../references/author-visible-step-gate.md
AGENTS.md
```

新书 S1 未 PASS：S2: BLOCKED。
已有书禁止用聊天历史覆盖仓库生产状态。

如果上一章已经提交 `CURRENT_EMOTIONAL_RESIDUE`，本章 S2 必须把它当作人物初始状态的一部分，不得从默认人格重启。

---

## 4. Continuous Story Room

加载 `references/story-room.md v2.1+`。

核心行为：

```text
FOLLOW
SEARCH-CALIBRATE
ILLUMINATE
LOCALLY CONTINUE
KEEP IT SIMPLE
PROTECT FUN / PLEASURE
DEEP-RESEARCH WHEN USEFUL
HUMAN-RETELL SOURCE BLOCKS WHEN USED
CHALLENGE REAL DEFECTS
CONVERGE ONLY WHEN STORY IS READY
```

### 4.1 作者还在自己想

AI 顺着当前思路推进半步，不抢完剩余剧情；正式推进前先做当前问题相关搜索校准。

### 4.2 作者有感觉但说不清

把现有意思说清楚，最多指出一个重要内生后果，不自动扩出完整新链。

### 4.3 作者卡住 / 要求拓展

AI 可以主动给具体延伸，但优先找：

```text
更爽
更顺
更简单
更好玩
更有反应感
```

而不是更复杂。

### 4.4 当前具体问题需要更深案例

加载 `references/fiction-plot-case-retrieval.md v1.1+`。
后台可研究多个小说案例。

如果某个案例真的被拿来拆具体剧情，则必须同时加载 `references/human-retelling-core.md`，先恢复具体故事块，再谈它为什么有用。

不得只凭简介 / 标签 / 摘要就声称已经“拆过这本书”。

如果公开章节无法访问：

```text
REPORT chapter inaccessible / evidence weakness
→ use directory + indexed excerpts + reliable secondary descriptions only with uncertainty clearly marked
```

不得把不确定事件顺序当事实。

### 4.5 持续共创

作者自然反馈：

```text
这个俗
这个舒服
这里别圣母
这个人物不会这样
这段太严谨
这里太累
这里爽一点
这里松一点
```

直接作为当前创作偏好继续使用。

---

## 5. Story pleasure contract

每个故事块不要求固定“每章一个爽点”，也不机械套打脸模板。

但整个故事不能长期处于：

```text
纯铺垫
纯解释
纯受压
纯思考
纯设定展示
```

需要持续给读者某种回报，例如：

```text
能力新鲜感
主角占便宜
反差 / 玩梗
解决问题
拿到东西
压住别人
关系变舒服
探索发现
期待兑现
轻松互动
```

同时允许有松弛段。

```text
PAYOFF_DENSITY: sufficient, not mechanical
BREATHING_ROOM: allowed and desirable
```

如果“更严谨”和“更爽更顺”冲突，在不突破合理性地板的前提下：

```text
CHOOSE MORE FUN / MORE READABLE
```

---

## 6. Repair discipline

只修具体症状：

```text
动机假 → 搜索校准 + 补一个够用的真实原因
因果断 → 补最短可理解桥梁
中间无聊 → 增加具体行动 / 反应 / 收获 / 乐趣
主角像工具人 → 回人物地基 + 当前兴趣
人物前后像情绪清零 → 找到上一个真正留下的余波，让后一个节点在它上面发生
太严谨太沉 → 删除解释层，恢复人物和现场
太炸太累 → 加轻松互动 / 日常 / 探索 / 呼吸
```

禁止：

```text
故事不舒服
→ 新增抽象层 / 矩阵 / 功能表 / 大阴谋
```

```text
NOVEL INTEREST > FORMAL PERFECTION
READER COMFORT > COMPLEXITY
```

---

## 7. Convergence / approval / chapter cut

只有故事基本能从头跑到尾时，AI 才第一次正式收束成自然 whole-story retelling。

只有作者明确“就这样 / 这版可以 / 确定 / 这个故事定了”才：

```text
TARGET_STORY_APPROVED: true
```

然后自然切章；作者批准后：

```text
STORY_CONSTRUCTION_STATUS: PASS_FOR_CURRENT_STORY_BLOCK
TARGET_STORY_APPROVED: true
CHAPTER_PARTITION_APPROVED: true
```

### 7.1 Chapter Emotional Thread｜只留四件事

当前章有实质情绪变化时，在 Plot Block + Character Block 收束后、交给 S3 前，确认一条极薄的：

```text
CHAPTER_EMOTIONAL_THREAD
```

只回答：

```text
CHAPTER_EMOTIONAL_START
EMOTIONAL_PRESSURE / CHANGE
CHAPTER_EMOTIONAL_ENDPOINT
RESIDUE_TO_NEXT_CHAPTER
```

没有实质情绪变化则不硬造。

禁止：

```text
emotion matrix
strength score
one-emotion-label-per-node
psychology model
new plot added only to complete emotion
```

情绪线没有新剧情权，只解释已批准事件连续落在人身上后，人物状态怎样变化。

---

## 8. Stage 3 handoff

S3 当前正式输入：

```text
APPROVED PLOT BLOCK
+ APPROVED CHARACTER BLOCK
+ CURRENT CONTINUITY / CANON
+ CURRENT_BLOCK
+ SCAN_COORDINATES
+ CHAPTER_EMOTIONAL_THREAD when materially relevant
```

```text
S2_TO_S3_HANDOFF: ACTIVE
OLD_STORY_MOTION_HANDOFF: RETIRED
```

不得为了兼容旧 S3 重造旧 Story Motion。

---

## 9. Failure discipline

如果正式创作回复需要搜索插件而 provider 失败：

```text
REPORT exact provider failure
→ retry / repair
→ still fail: do not silently claim search-backed reasoning
```

如果拆书所需的具体章节无法获取：

```text
REPORT exact source-access failure
→ do not fake Human Retelling Core from a book blurb
→ seek another accessible source / indexed chapter / reliable secondary evidence
```

不得跳过搜索或真人复述硬门后继续伪装成正式生产结果。

---

## 10. Hard invariants

```text
AUTHOR IDEA FIRST
PLEASURE FIRST
SIMPLE / READABLE / LIGHT BY DEFAULT
REASONABLE ENOUGH, NOT PAPER-RIGOROUS
RELAXED-AND-EXCITING RHYTHM
NO COMPLEXITY INFLATION
NO A/B/C AUTHOR-CHOICE WORKFLOW
FORMAL CREATIVE REPLY MUST BE SEARCH-BACKED
DEEP FICTION CASE RESEARCH ONLY WHEN USEFUL
FICTION SOURCE BREAKDOWN MUST USE HUMAN RETELLING CORE
RETELLING_BRIDGE_LOCK IS AUTHOR-LOCKED AND MAY NOT BE REMOVED / DEMOTED
NO PERMANENT DONOR
NO PLOT DNA / STRATEGY ABSTRACTION
CHAPTER_EMOTIONAL_THREAD WHEN MATERIALLY RELEVANT
NO EMOTIONAL RESET BETWEEN STORY NODES BY DEFAULT
NO PROSE IN S2
NO OLD STORY MOTION HANDOFF
```

## Memory line

> **S2 v9.5：故事第一目标是简单、好读、舒服、爽。正式创作先搜；真正拆书时先用 Human Retelling Core 讲清楚发生了什么。每章先读 CURRENT_BLOCK，再用 SCAN_COORDINATES 锁定真实事件；章节收束时除了剧情块和人物块，有实质情绪变化再留一条极薄 Chapter Emotional Thread。**