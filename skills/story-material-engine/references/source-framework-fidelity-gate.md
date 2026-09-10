# Source Framework Fidelity Gate｜母本框架保真闸门

> version: 1.3
> applies_to: Story Material Engine Stage 2 source-to-target combination
> status: production-main

## Purpose

当 S2 使用已经拆解好的热门 / 成熟来源章节帮助构思目标小说时，默认把来源 Human Retelling 当作**经过验证的剧情骨架模板**。

核心原则：

> **母本给树干：关键剧情节点、推进顺序、桥接功能、节点停留权重和阶段终点默认保留。目标世界负责换皮长肉；Firecrawl 负责给每个既定节点寻找目标世界里最自然的材料；AI 负责把这些材料长进节点里，而不是重新设计一棵树。**

```text
SOURCE_TEMPLATE_AUTHORITY: STRONG
SOURCE_KEY_NODE_ORDER: preserve by default
SOURCE_NODE_FUNCTION: preserve by default
SOURCE_NODE_DWELL_WEIGHT: preserve by default
SOURCE_STAGE_ENDPOINT: preserve
TARGET_SURFACE_TRANSFORMATION: required
FIRE_ENRICHES_NODE: true
FIRE_REWRITES_TEMPLATE: forbidden
AI_EXPANDS_INSIDE_NODE: true
AI_REDESIGNS_SKELETON: forbidden by default
```

## 1. What must be preserved

先从来源 Human Retelling 读出真正的关键剧情节点：

```text
NODE A
→ NODE B
→ NODE C
→ NODE D
→ STAGE ENDPOINT
```

每个节点至少包含：

```text
这个节点发生了什么类型的事
主角处境发生什么变化
它为什么把故事推到下一个节点
母本在这里是停下来展开，还是快速桥接过去
```

目标构思默认保留：

```text
关键节点的相对顺序
关键节点承担的推进功能
节点之间的重要因果桥
节点之间的相对停留权重
当前来源阶段终点
```

目标必须改变：

```text
人物身份
地点 / 世界皮肤
具体物件
具体行为方式
对白
目标世界独有的生活细节
```

```text
PRESERVE_CAUSAL_SKELETON: required
PRESERVE_RELATIVE_DWELL_WEIGHT: required
COPY_SURFACE_EVENT: forbidden
COPY_SOURCE_PROSE: forbidden
```

### 1.1 Dwell weight｜母本哪里快，目标默认也哪里快

母本节点不只有“有没有”，还有“停多久”。

最小判断只分三种：

```text
EXPAND
= 母本明显停下来演，承担主要情绪 / 冲突 / 章内重量

NORMAL
= 正常推进，给够必要动作和因果

BRIDGE_FAST
= 主要负责把故事送往下一关键节点，母本本身快速带过
```

这不是第三套分析，不需要额外表格。只要在处理母本节点时知道它属于哪一类即可。

硬规则：

```text
SOURCE_BRIDGE_FAST
→ TARGET_FULL_SCENE_UPGRADE: forbidden by default

SOURCE_EXPAND
→ TARGET_ONE_LINE_SHRINK: forbidden by default
```

目标世界可以改变实现方式，但不能因为材料有趣、人物反应丰富、Fire 搜到很多细节，就把母本一个快速桥节点擅自升级成完整大场景。

特别警惕：

```text
母本：一句或一小段完成“赶路 / 找活 / 被带走 / 跟随几天 / 看见一种常态”
目标：拆成跟踪、试探、换路、观察、对话、再次确认、完整遭遇、完整善后
```

如果这些新增步骤没有改变节点功能，只是在同一桥节点里横向变厚，默认属于：

```text
BRIDGE_INFLATION
→ compress / reject by default
```

判断句：

> **母本这一段的任务，是让读者停下来经历它，还是只让故事顺利抵达下一节点？**

如果答案是后者，目标剧情块也应该快速通过。

## 2. Firecrawl role｜给既定节点开花

Firecrawl 不只做真假校准，但它的扩展权限必须锁在**当前母本节点内部**，并受该节点停留权重限制。

对每个既定节点，可以搜索：

```text
这个地图真实有哪些职业 / 地点 / 设施 / 交通
这种权力关系在原作里实际如何运作
这个节点需要的动作在目标世界里有哪些自然实现方式
有哪些目标世界独有的小细节可以让节点更活
```

正确问题：

> **“母本这一节点到了目标世界，最自然会长成什么？”**

还必须补一句：

> **“母本这里本来停多久？这些材料只够把它写自然，还是正在把一个快桥膨胀成新场景？”**

错误问题：

> **“这个地图还有什么有趣剧情，我们要不要换一条路？”**

```text
FIRE_ROLE = CALIBRATE + NODE_LOCAL_ENRICHMENT
FIRE_WORLD_FACTS = MATERIAL POOL
FIRE_WORLD_FACTS != NEW PLOT AUTHORITY
FIRE_WORLD_FACTS != DWELL_WEIGHT_OVERRIDE
MAP_SCAN_MAY_ENRICH_NODE: true
MAP_SCAN_MAY_REPLACE_NODE_SEQUENCE: false
MAP_SCAN_MAY_UPGRADE_BRIDGE_TO_FULL_SCENE: false by default
```

## 3. AI role｜长肉，不换骨，也不把桥养胖

AI 可以在当前节点内部：

```text
补目标世界的生活动作
补更自然的触发方式
补同一节点内必要的小碰撞
补人物当场反应
补目标世界独有的具体细节
让前后桥接更顺
```

但扩展量必须服从母本节点原本的相对重量。

AI 默认不能：

```text
因为搜索到新地点就换主线
因为地图素材很多就新增平行支线
把母本关键节点删掉后自由重构
为了“更合理”改变原本有效的推进顺序
把热门母本只当灵感起点
把母本快速桥节点拆成多个完整子场景
```

```text
NODE_LOCAL_VARIATION: encouraged
SKELETON_FREEFORM_REWRITE: forbidden by default
NEW_BRANCH_FROM_SEARCH_RESULT: forbidden by default
BRIDGE_TO_FULL_SCENE_PROMOTION: forbidden by default
```

## 4. Capacity rule｜容量不够怎么办

目标剧情太薄时，先检查：

```text
是不是某个母本关键节点没有真正落地？
是不是母本本来就重的节点被一句话带过？
是不是目标世界的重节点还没有长出足够具体的事情？
```

不要把“容量不够”自动解释成“所有节点都要加戏”。

正确修复：

```text
TARGET TOO THIN
→ keep source key-node sequence + functions + dwell weights
→ return to a SOURCE-HEAVY but weak target node
→ Firecrawl-search target-world materials for THIS NODE
→ AI enriches THIS NODE with concrete target-world events / life / reactions
→ reconnect to the next preserved source node
→ repeat until the whole stage has enough story
```

如果薄的是母本本来就快速桥接的节点：

```text
SOURCE_BRIDGE_FAST + TARGET_THIN
→ do not inflate by default
→ inspect whether a SOURCE_EXPAND / NORMAL node elsewhere was underbuilt
```

禁止：

```text
TARGET TOO THIN
→ inflate every bridge
```

```text
TARGET TOO THIN
→ invent unrelated investigation / help-seeking / side quest
```

```text
TARGET TOO THIN
→ jump ahead to next source stage
```

容量来自：

> **把母本本来就该停的地方写活、写够；母本用来过桥的地方保持利落。**

## 5. Admission check for target additions

新增内容检查四个问题：

```text
Q1. 它现在长在哪个母本关键节点里？
Q2. 它是否让这个节点更自然、更具体、更有目标世界味？
Q3. 它是否仍然把故事送往母本下一个既定节点？
Q4. 它有没有把母本原本的快速桥节点升级成完整场景？
```

如果 Q1 回答不出来：

```text
OUTSIDE_TEMPLATE_GROWTH: reject by default
```

如果 Q3 改变了后续骨架：

```text
SKELETON_DRIFT: reject by default
```

如果 Q4 为是，且作者没有明确要求加重：

```text
DWELL_WEIGHT_DRIFT: reject / compress by default
```

作者明确要求改母本框架或加重某节点时，才允许改变。

```text
AUTHOR_EXPLICIT_TEMPLATE_CHANGE > SOURCE_TEMPLATE_AUTHORITY
```

## 6. Example

来源骨架：

```text
主角已有普通生活                     [EXPAND / NORMAL]
→ 外部强权闯入                       [EXPAND]
→ 熟人遭殃，主角无力阻止             [EXPAND]
→ 原生活因此断裂                     [NORMAL / BRIDGE_FAST]
→ 主角被强势力量拖进新处境           [BRIDGE_FAST / NORMAL]
→ 在新处境里看见恶是日常运作         [BRIDGE_FAST / NORMAL]
→ 第二件更近、更难无视的恶事落到眼前 [EXPAND]
→ 主角联想到这些年见过的一切         [EXPAND / ENDPOINT]
```

目标版本可以把：

```text
村庄 / 溃兵 / 官兵 / 地窖
```

换成目标世界自己的：

```text
香波地日常 / 天龙人 / 人贩子链条 / 奴隶交易场景
```

但如果母本“被抓壮丁 → 跟着走 → 看见征粮本质”本来走得很快，目标版“被人贩子盯上 → 被抓 → 看见人口交易运作”也默认保持桥接速度，不能因为目标世界细节丰富就拆成跟踪、试探、绕路、完整抓捕、完整验货、完整估价等多个大场景。

Firecrawl 的作用，是帮助这些节点找到最自然的目标世界材料，并控制在母本原本的重量里。

## 7. Hard rules

```text
SOURCE_TEMPLATE_AUTHORITY: STRONG
SOURCE_KEY_NODE_ORDER: PRESERVE_BY_DEFAULT
SOURCE_NODE_FUNCTION: PRESERVE_BY_DEFAULT
SOURCE_NODE_DWELL_WEIGHT: PRESERVE_BY_DEFAULT
SOURCE_STAGE_ENDPOINT: PRESERVE
TARGET_SURFACE_TRANSFORMATION: REQUIRED
FIRE_NODE_LOCAL_ENRICHMENT: REQUIRED_WHEN_USEFUL
FIRE_REWRITES_TEMPLATE: FORBIDDEN
FIRE_WORLD_FACTS_OVERRIDE_DWELL_WEIGHT: FORBIDDEN
AI_EXPANDS_INSIDE_NODE: ALLOWED_WITHIN_SOURCE_WEIGHT
AI_REDESIGNS_SKELETON: FORBIDDEN_BY_DEFAULT
BRIDGE_TO_FULL_SCENE_PROMOTION: FORBIDDEN_BY_DEFAULT
BRIDGE_INFLATION: FORBIDDEN_BY_DEFAULT
TARGET_TOO_THIN: RETURN_TO_UNDERBUILT_SOURCE_HEAVY_NODE
CAPACITY_REPAIR_BY_INFLATING_BRIDGES: FORBIDDEN
CAPACITY_REPAIR_BY_UNRELATED_SIDE_QUEST: FORBIDDEN
CROSS_STAGE_CAPACITY_REPAIR: FORBIDDEN
AUTHOR_EXPLICIT_TEMPLATE_CHANGE: OVERRIDES
```

## Memory line

> **母本不只控制“发生什么、按什么顺序”，还控制“哪里停、哪里快”。关键节点、推进功能、因果桥、相对停留权重和阶段终点默认保留。母本快速桥接的地方，目标也默认利落通过；容量要优先补母本本来就重却没写够的节点，不能把所有快桥养成完整场景。**