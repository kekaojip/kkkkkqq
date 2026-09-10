# Source-to-Target Combination｜来源拆解到目标构思的组合思考

> version: 0.9
> applies_to: Story Material Engine Stage 2
> status: production-main
> role: S2 thin combination-thinking layer

## 0. Purpose

本技能不新增第三套拆书分析。

它只负责把已经拆好的两块来源材料用于目标小说构思：

```text
BLOCK 1 — HUMAN RETELLING CORE
+
SOURCE TEMPLATE FIDELITY
+
SOURCE NODE DWELL WEIGHT
+
DUAL BLOOM
  L1 TARGET-WORLD BLOOM
  L2 REALIZATION / FICTION-CASE BLOOM when useful
+
AUTHOR / AI TARGET PLOT CO-CREATION
+
BLOCK 2 — CHARACTER TRACE
+
FIRECRAWL REAL-REACTION CALIBRATION
+
TARGET CHARACTER REHEARSAL
+
CHARACTER-BASED TARGET REVISION
```

核心原则：

> **母本 Human Retelling 默认提供经过验证的剧情树干。关键节点、推进顺序、桥接功能、相对停留权重和阶段终点默认保留；目标小说负责把每个节点换成自己的世界、人物和具体事件。Fire 可以让每个节点开花，但只能让“这个节点怎么发生”更丰富，不能借研究换掉树干。**

```text
SOURCE_TEMPLATE_AUTHORITY: STRONG
SOURCE_NODE_DWELL_WEIGHT: PRESERVE_BY_DEFAULT
THIRD_ANALYSIS_SYSTEM: FORBIDDEN
SOURCE_PROSE_COPYING: FORBIDDEN
TARGET_SURFACE_TRANSFORMATION: REQUIRED
DUAL_BLOOM_IS_NODE_LOCAL: true
```

---

## 1. Canonical loop

默认按来源章节 / 完整剧情块逐节点走。

```text
SOURCE HUMAN RETELLING CORE
→ IDENTIFY SOURCE KEY NODES + ORDER + BRIDGE FUNCTIONS + DWELL WEIGHTS + STAGE ENDPOINT
→ TAKE SOURCE NODE 1
→ KNOW WHETHER IT IS EXPAND / NORMAL / BRIDGE_FAST

→ LAYER 1: TARGET-WORLD BLOOM
   FIRECRAWL CALIBRATES / ENRICHES THIS NODE IN TARGET WORLD
   → AI + AUTHOR BUILD A TARGET VERSION

→ LAYER 2: REALIZATION / CASE BLOOM when useful
   ASK: SAME NODE FUNCTION, WHAT OTHER CONCRETE REALIZATIONS EXIST?
   → optionally load fiction-plot-case-retrieval.md in NODE-LOCAL mode
   → collect only node-compatible concrete treatments
   → compare with current Target realization
   → keep / combine / reject without changing source skeleton

→ TARGET RECOMBINATION WITHIN SOURCE DWELL WEIGHT
→ CONNECT TO NEXT PRESERVED SOURCE NODE
→ REPEAT NODE BY NODE

→ CHECK WHOLE TARGET STAGE GRANULARITY + CAPACITY + RELATIVE WEIGHT
→ IF TOO THIN: RETURN TO UNDERBUILT SOURCE-HEAVY NODE
→ DO NOT INFLATE FAST BRIDGES TO REPAIR CAPACITY
→ DO NOT INVENT A NEW SKELETON

→ WHEN SOURCE STAGE ENDPOINT IS REACHED: SHOW CHARACTER TRACE
→ FIRECRAWL CALIBRATES REALISTIC REACTION RANGE
→ AI RUNS TARGET CHARACTER REHEARSAL
→ AUTHOR KEEPS / CHANGES / REJECTS
→ CHARACTER REVISES LOCAL DELIVERY ONLY
→ TARGET BLOCK BECOMES USABLE
```

这不是 A/B/C 流程。作者可以随时打断、修改某个节点或明确要求更换母本骨架。

```text
LAYER_1_TARGET_WORLD_BLOOM: required when useful
LAYER_2_REALIZATION_BLOOM: optional / on-demand
LAYER_2_WHOLE_CHAPTER_AUDIT: forbidden by default
```

---

## 2. Pass 1｜先认母本树干和停留权重

从来源 `Human Retelling Core` 里先抓：

```text
关键节点 1
→ 关键节点 2
→ 关键节点 3
→ ...
→ 当前阶段终点
```

每个关键节点只看四件事：

```text
这里发生了什么类型的事情
→ 主角处境怎么变
→ 为什么它会把故事送到下一个节点
→ 母本在这里是停下来演，还是快速送过去
```

最小权重只分：

```text
EXPAND
NORMAL
BRIDGE_FAST
```

默认保留：

```text
关键节点相对顺序
节点推进功能
重要因果桥
节点相对停留权重
当前阶段终点
```

默认不保留：

```text
人物名
地点
具体物件
原作对白
原作表面事件皮肤
```

```text
LEARN / PRESERVE CAUSAL SKELETON + DWELL RHYTHM
NOT SOURCE SURFACE
```

作者明确说要改变骨架或某节点重量时，作者要求优先。

---

## 3. Dual Bloom｜同一个母本节点，两层开花

### 3.1 Layer 1｜Target-World Bloom

第一层解决：

> **母本这一节点到了目标世界，最自然会长成什么？**

可以查：

```text
这个地图真实有哪些职业 / 地点 / 设施 / 交通
这种权力角色在原作里实际怎么行动
这个节点需要的动作在目标世界有哪些自然实现方式
目标能力 / 物件 / 环境的真实尺寸、限制、用途
哪些世界细节能让这个节点更具体、更有味道
```

输出不是百科，而是当前节点真正可用的少量材料。

```text
FIRE_TARGET_WORLD_ROLE = CALIBRATE + NODE_LOCAL_ENRICHMENT
FIRE_WORLD_FACTS = MATERIAL POOL
FIRE_WORLD_FACTS != NEW PLOT AUTHORITY
FIRE_WORLD_FACTS != DWELL_WEIGHT AUTHORITY
```

### 3.2 Layer 2｜Realization / Fiction-Case Bloom

当 Target Node 已经能成立，但作者想让它更丰富，或 AI 判断存在明显更好的成熟实现时，再问：

> **同一个节点功能，在不换骨架的前提下，还有哪些自然、成熟、具体的做法？**

此时可以调用：

`fiction-plot-case-retrieval.md`

但必须使用 **NODE-LOCAL REALIZATION MODE**。

合法搜索对象：

```text
现实行为中的具体做法
目标原作世界里的相似处理
其他小说里的相似具体桥段
其他成熟叙事中同功能的局部实现
```

正确问题示例：

```text
这个节点要求“弱能力先造成一次真实小兑现”，还有哪些具体动作能完成？
这个节点要求“普通人先干预但仍失败”，弱势角色可以怎样只打断一个关键动作链？
这个节点要求“救下来不等于真正脱身”，有哪些自然的实际撤离实现？
这个节点要求“更大压力来了且主角主动接走”，有哪些不新增支线的具体做法？
```

错误问题：

```text
我们的整章对不对？
别的小说是不是都这么写？
这个 Plot 要不要推翻？
哪本小说结构比母本更好？
```

```text
REALIZATION_BLOOM = ALTERNATIVE IMPLEMENTATION MATERIAL
REALIZATION_BLOOM != WHOLE_CHAPTER_AUDIT
REALIZATION_BLOOM != SOURCE_TEMPLATE_REPLACEMENT
```

### 3.3 Target Recombination

两层材料回来后，不直接搬案例。

必须重新回到：

```text
当前母本节点功能
+ 当前 Target 人物
+ 当前 Target 世界
+ 当前现场限制
+ 当前人物知道什么
+ 下一个保留母本节点
+ 当前 dwell weight
```

然后只留下最适合的一种或少量融合后的实现。

```text
SEARCH WIDE
→ RECOMBINE NARROW
```

丰富不是把所有做法都塞进去。

```text
MORE OPTIONS FOUND != MORE EVENTS ADDED
RICHER REALIZATION != BIGGER PLOT
```

---

## 4. Dual Bloom admission gate｜开花不能换骨

每个新增 / 替换 realization 检查：

```text
Q1. 它长在哪个母本关键节点里？
Q2. 它是否仍然完成这个母本节点原本的推进功能？
Q3. 它有没有让节点更自然、更具体、更有 Target 世界味？
Q4. 它是否仍然把故事送往下一个保留节点？
Q5. 它有没有改变关键节点顺序？
Q6. 它有没有改变当前节点的相对停留权重？
Q7. 它是真的更好，还是仅仅不同 / 更多？
```

失败处理：

```text
Q1 fail → OUTSIDE_TEMPLATE_GROWTH: reject by default
Q2/Q4/Q5 fail → SKELETON_DRIFT: reject by default
Q6 fail → DWELL_WEIGHT_DRIFT: reject / compress by default
Q7 fail → KEEP CURRENT REALIZATION
```

作者明确改模板或加重节点时除外。

---

## 5. AI Role｜长肉，不换骨

AI 在当前节点内部可以主动：

```text
把母本事件翻译成目标世界版本
补目标人物真实生活动作
补同一节点内必要的小碰撞
补更顺的触发方式
补目标世界特有的具体东西
比较当前 realization 与研究带回来的其他 realization
融合少量真正更好的局部处理
```

但必须服从节点原本停留权重。

默认不能：

```text
因为搜到新地点就另开支线
因为案例很精彩就重排关键节点
删掉母本桥后自由发挥
把成熟母本只当灵感起点
把 BRIDGE_FAST 拆成多个完整场景
把 Realization Bloom 跑成 Whole Chapter Case Audit
```

```text
AI_EXPANDS_INSIDE_NODE: true
AI_EXPANSION_WITHIN_SOURCE_WEIGHT: required
AI_REDESIGNS_SKELETON: forbidden by default
BRIDGE_TO_FULL_SCENE_PROMOTION: forbidden by default
NEW_BRANCH_FROM_SEARCH: forbidden by default
```

---

## 6. Target plot block granularity｜目标剧情块颗粒度 + 权重

作者前台看到的目标剧情块，默认保持与来源 `Human Retelling Core` 接近的颗粒度：

> **一整段自然讲完，具体但不细碎；比摘要厚，比人物排戏粗。**

必须保持母本相对停留权重：

```text
SOURCE EXPAND
→ target can 展开到完整关键事件
→ Dual Bloom 可以更积极地找实现材料

SOURCE NORMAL
→ target 给够必要动作和因果
→ Dual Bloom 只补真正有价值的实现

SOURCE BRIDGE_FAST
→ target 用最少必要动作送到下一节点
→ Layer 2 默认不启动，除非桥本身存在真实因果问题
```

禁止：

```text
只剩抽象箭头
逐眼神 / 逐呼吸 / 逐镜头
提前写成正文
把一个快桥拆成多个完整小场景
因为搜索材料丰富而横向增肥
```

```text
TARGET_PLOT_BLOCK_GRANULARITY = HUMAN_RETELLING_LEVEL
TARGET_RELATIVE_DWELL_WEIGHT = SOURCE_RELATIVE_DWELL_WEIGHT
TOO_ABSTRACT = FAIL
BRIDGE_INFLATION = FAIL
FULL_SCENE_PROSE = FORBIDDEN_IN_S2
```

---

## 7. Story capacity｜容量不够，补重节点，不养胖快桥

```text
GRANULARITY != STORY CAPACITY
CAPACITY != EVERY_NODE_EXPANSION
ROUGH != THIN
MORE DETAIL != MORE PLOT
MORE RESEARCH != MORE STORY
```

如果目标太薄，优先检查：

```text
是不是母本本来就重的节点被一句话带过？
是不是某个 EXPAND / NORMAL 节点没有真正发生起来？
是不是当前 realization 太抽象，缺少一个实际动作链？
是不是情绪 / 冲突重心被挪到了母本快桥上？
```

正确修复：

```text
TARGET TOO THIN
→ KEEP SOURCE KEY-NODE ORDER + FUNCTIONS + DWELL WEIGHTS
→ FIND UNDERBUILT EXPAND / NORMAL NODE
→ RUN TARGET-WORLD BLOOM
→ IF STILL THIN / GENERIC: RUN REALIZATION BLOOM
→ RECOMBINE INTO ONE STRONGER TARGET REALIZATION
→ RECONNECT TO NEXT PRESERVED SOURCE NODE
→ RECHECK CAPACITY
```

如果快桥显得薄：

```text
SOURCE BRIDGE_FAST
→ thin is often correct
→ do not automatically enrich
```

---

## 8. Pass 2｜Character Trace

当目标剧情已经按母本节点走到当前阶段终点，再拿来源 `Character Trace` 到前台：

```text
谁按顺序出现
→ 当时什么状态
→ 说什么 / 做什么
→ 这一反应把剧情推到哪里
```

Character Trace 不要求目标人物一一对应，但要提醒：

> **骨架可以来自母本，人物不能变成换皮 NPC。**

目标只放真正需要的人：

```text
主角
事件直接作用对象
相关家人 / 熟人
造成事件的人
现场必要其他人
```

```text
NEEDED_PEOPLE_ONLY: preferred
CAST_INFLATION: forbidden
```

---

## 9. Target Character Rehearsal｜目标人物排戏

正式排目标人物状态、动作或对白前，默认使用 Firecrawl 搜当前具体遭遇下的真实反应范围。

```text
TARGET_CHARACTER_REHEARSAL_SEARCH_REQUIRED: true
SEARCH_RESULT = POSSIBILITY RANGE
SEARCH_RESULT != CHARACTER DESTINY
```

最终反应结合：

```text
真实反应范围
+ 人物基础性格
+ 当前关系
+ 人物知道什么
+ 权力差 / 逃跑空间
+ 此刻最想保住什么
```

禁止自动模板：

```text
愤怒 = 握拳
悲伤 = 流泪
恐惧 = 发抖
孩子 = 标准哭喊
妻子 = 标准跪地求饶
主角 = 双拳紧握强忍怒火
反派 = 标准狞笑
```

默认反应顺序：

```text
当下发生什么
→ 第一眼注意什么
→ 想要 / 害怕什么
→ 身体 / 行动先做什么
→ 做出选择
→ 自然时才说话
→ 造成局部变化
```

人物排戏也不得反向把快桥升级成重场景。

```text
CHARACTER_REACTION_DETAIL != NEW DWELL_WEIGHT
FULL_SCENE_PROSE: forbidden in S2
ILLUSTRATIVE_ACTION / DIALOGUE: allowed
```

---

## 10. Character-based revision｜人物只能轻修节点

人物排戏以后，可以改变：

```text
节点内部事件发生的小方式
谁先动作
谁先说话
触发更自然的原因
节点内部的小因果
```

默认不得：

```text
删除母本关键节点
重排母本关键节点
创造新阶段
借人物反应把剧情拐到另一条主线
借人物反应把 BRIDGE_FAST 变成完整重场景
```

```text
AUTHOR_LOCKED_PLOT > REHEARSAL
SOURCE_TEMPLATE_SKELETON > DEFAULT_CHARACTER_PLOT_DRIFT
SOURCE_DWELL_WEIGHT > DEFAULT_CHARACTER_DETAIL_EXPANSION
MINIMAL_CHARACTER_REVISION: preferred
```

---

## 11. Search failure discipline

需要 Firecrawl 的正式创作步骤如果失败：

```text
REPORT exact failure
→ retry / change query / seek another source
→ still fail: mark current node / reaction as uncalibrated
```

如果是 Layer 2 Realization Bloom 失败：

```text
REPORT weak / failed case research
→ keep Layer 1 target-world bloom and current realization if valid
→ do not mark Plot invalid merely because no cases were found
```

不得静默用模型套路顶上。

---

## 12. Author-facing interaction

前台默认保持自然：

```text
先看来源 Human Retelling Core
→ 当前跑到哪个母本节点，就只处理哪个节点
→ Layer 1：Fire 找目标世界材料，让它先自然长成 Target Version
→ 如果这个节点仍普通 / 卡住 / 作者想更丰富
   Layer 2：再查“同一个功能还有什么具体做法”
→ 把有用材料翻译回当前人物和世界
→ 只留下最顺的 realization
→ 快桥快速过，重节点才停下来长肉
→ 到母本阶段终点
→ 再看 Character Trace
→ 再做人类反应校准和人物排戏
```

不要把后台规则一次全倒给作者，不做 A/B/C，不做案例考试。

---

## 13. Completion signal

当前块满足即可停：

```text
SOURCE KEY-NODE ORDER PRESERVED
+
SOURCE NODE FUNCTIONS PRESERVED
+
SOURCE BRIDGE FUNCTIONS PRESERVED
+
SOURCE RELATIVE DWELL WEIGHT PRESERVED
+
TARGET SURFACE FEELS LIKE ITS OWN WORLD
+
IMPORTANT TARGET NODES HAVE CONCRETE REALIZATIONS
+
SOURCE-HEAVY NODES FEEL ACTUALLY LIVED / HAPPENED
+
SOURCE-FAST BRIDGES STAY LEAN
+
TARGET HAS ENOUGH STORY CAPACITY
+
SOURCE STAGE ENDPOINT REACHED
+
NEEDED PEOPLE FEEL ALIVE
+
CAUSE-AND-EFFECT STAYS SIMPLE
```

---

## 14. Hard boundaries

```text
SOURCE BREAKDOWN STILL HAS ONLY TWO BLOCKS
BLOCK 1 = HUMAN RETELLING CORE
BLOCK 2 = CHARACTER TRACE
THIS FILE IS A COMBINATION LOOP, NOT BLOCK 3

SOURCE_TEMPLATE_AUTHORITY: STRONG
SOURCE_KEY_NODE_ORDER: PRESERVE_BY_DEFAULT
SOURCE_NODE_FUNCTION: PRESERVE_BY_DEFAULT
SOURCE_NODE_DWELL_WEIGHT: PRESERVE_BY_DEFAULT
SOURCE_STAGE_ENDPOINT: PRESERVE
TARGET_SURFACE_TRANSFORMATION: REQUIRED

DUAL_BLOOM: ENABLED
TARGET_WORLD_BLOOM: NODE_LOCAL
REALIZATION_CASE_BLOOM: NODE_LOCAL_AND_OPTIONAL
REALIZATION_CASE_BLOOM_WHOLE_CHAPTER_AUDIT: FORBIDDEN
FIRE_NODE_LOCAL_ENRICHMENT: REQUIRED_WHEN_USEFUL
FIRE_REWRITES_TEMPLATE: FORBIDDEN
FIRE_WORLD_FACTS_OVERRIDE_DWELL_WEIGHT: FORBIDDEN
CASE_RESEARCH_OVERRIDE_SOURCE_TEMPLATE: FORBIDDEN
CASE_RESEARCH_AUTO_CANON: FORBIDDEN

AI_EXPANDS_INSIDE_NODE: ALLOWED_WITHIN_SOURCE_WEIGHT
AI_REDESIGNS_SKELETON: FORBIDDEN_BY_DEFAULT
NEW_BRANCH_FROM_SEARCH_RESULT: FORBIDDEN_BY_DEFAULT
BRIDGE_TO_FULL_SCENE_PROMOTION: FORBIDDEN_BY_DEFAULT
BRIDGE_INFLATION: FORBIDDEN

TARGET_TOO_THIN: RETURN_TO_UNDERBUILT_SOURCE_HEAVY_NODE
DETAIL_DENSITY_AS_CAPACITY_SUBSTITUTE: FORBIDDEN
CAPACITY_REPAIR_BY_INFLATING_BRIDGES: FORBIDDEN
CROSS_STAGE_CAPACITY_REPAIR: FORBIDDEN
CAPACITY_REPAIR_BY_UNRELATED_SIDE_QUEST: FORBIDDEN

TARGET_PLOT_BLOCK_GRANULARITY = HUMAN_RETELLING_LEVEL
TARGET_RELATIVE_DWELL_WEIGHT = SOURCE_RELATIVE_DWELL_WEIGHT
TARGET_CHARACTER_REHEARSAL_SEARCH_REQUIRED: true
SEARCH_RESULT_IS_RANGE_NOT_DESTINY: true
NO PROSE IN S2
AUTHOR_EXPLICIT_TEMPLATE_CHANGE: OVERRIDES
```

## Memory line

> **母本给骨架和快慢。每个节点先做 Target-World Bloom，让它在自己的世界里自然长出来；需要时再做 Realization/Case Bloom，去找“同一个功能还有哪些具体做法”。研究只丰富节点内部怎么发生，不审判整章、不换骨架、不把快桥养胖。**