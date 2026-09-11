# Plot Block Shot Gate｜剧情块可拍性门

> status: production-main
> owner: skills/story-material-engine/SKILL.md
> applies_to: S2 Plot Block 构建（Target 剧情块）
> counterpart: references/human-retelling-core.md（Source 拆解同构标准）
> purpose: 保证交给 S3 / Story Compose 的剧情块既是可拍镜头，也是读者扫读可见的事件链；禁止用心理、分析和标签替代剧情。

## 0. 核心原则

剧情块不是“这一章想表达什么”，而是“这一章实际发生什么”。

```text
BLOCK：这一大段故事正在兑现什么
SCAN_COORDINATES：这一章真正发生什么
SHOT：这些事情具体怎么被拍出来
```

母本统计数字、面板行数、感叹号、对白比例、BRAIN/HISTORY 字数等不属于本门的 PASS/FAIL。

## 1. CURRENT_BLOCK 必须可读

每章规划前读取 `PROJECT_STATE.md` 的 CURRENT_BLOCK：

```text
BLOCK_ID
BLOCK_TYPE: SIM | REALITY | MIX
BLOCK_PROMISE
BLOCK_ENTRY_EVENT
BLOCK_EXIT_CONDITION
BLOCK_PROGRESS
EXIT_CONDITION_REVISION_REASON: optional
```

S2 只做两件事：

```text
EXIT_CONDITION 已达成 → 规划自然转场
EXIT_CONDITION 未达成 → 本章继续推进 BLOCK_PROMISE
```

BLOCK 不规定章数，也不规定开头/结尾形式。

如因新剧情事实需要细化或修订 EXIT_CONDITION，必须留一行：

```text
EXIT_CONDITION_REVISION_REASON: ...
```

## 2. SCAN_COORDINATES｜先列剧情坐标

剧情块正式展开前，必须先列 `SCAN_COORDINATES`。

坐标不设固定数量。唯一判定：

> **这个节点发生以后，是否产生了新的事实、新信息、新决定或新结果？**

能回答“是”才算剧情坐标。

合法示例：

```text
- 顾川得知药徒留用考核能结束试药身份
- 顾川决定走留用路线
- 周小满通过考核，转入药徒帮工名册
- 顾川《养血法》入门，成为炼血境一重
```

不能独立算坐标：

```text
- 顾川分析三种路线
- 顾川回忆过去八个月
- 顾川意识到机会很珍贵
- 顾川情绪复杂
- 顾川开始认真规划未来
```

这些内容如果必要，只能挂在某个真实坐标后面作为反应/解释。

## 3. 节点即镜头

每个正式剧情节点必须写成一个可拍摄镜头，至少能够回答：

```text
谁
+ 当前处境 / 物件 / 诱因
+ 做了什么 / 说了什么
+ 这一下之后什么变了
```

如果删掉心理与解释以后，“谁做了什么、结果什么变了”说不出来：

```text
PLOT_NODE_IS_LABEL: FAIL
```

## 4. 禁止标签节点

以下词可以作为解释，不能作为节点本体：

```text
遭遇危机 / 心理博弈 / 局势升级 / 能力觉醒 / 认知变化
身份跃迁 / 完成反杀 / 获得成长 / 情绪到顶点 / 内心挣扎
希望受挫 / 压力加剧 / 守护支点 / 做出规划 / 分析利弊
```

必须把它们还原成具体事件。

## 5. 事件先行，解释后挂

剧情块默认组织：

```text
事件 / 对白 / 面板变化
→ 即时反应
→ 当前决定真正需要的最短解释
→ 下一事件
```

禁止把一整段规划成：

```text
规则解释 → 回忆 → 分析 → 计划 → 再分析 → 最后行动
```

思考、回忆、解释可以存在，但不能让它们抢占 SCAN_COORDINATES 的位置。

## 6. 首屏与停点

### 6.1 首屏

不设“前150字”“第二镜头”等数字门。

剧情块必须让正文有条件做到：

> **第一个手机屏内，读者能抓到正在发生的事情或主角眼下明确要做什么。**

纯氛围、纯环境、纯说明书式开场若不承重，则剧情块需重组第一拍。

### 6.2 章末

章末由当前事件自然决定，不按 SIM / REALITY / MIX 强制换壳。

```text
允许：动作 / 台词 / 事件结果 / 必要系统变化 / 自然断章
禁止：剧情闭合后额外补总结 / 预告 / 重复系统确认
```

系统面板是否能收尾，只看它是不是当前真实剧情变化，不看 BLOCK_TYPE。

## 7. 面板镜头

剧情块中的面板只分两类：

```text
EVENT_PANEL：选择 / 获得 / 失败 / 突破 / 死亡 / 结算 / 身份变化
LOCATOR_PANEL：时间 / 身份 / 剩余次数 / 当前必要定位
```

规则：

- EVENT_PANEL 必须服务一个剧情坐标。
- LOCATOR_PANEL 必须足够短，只保留接下来理解事件所需的信息。
- 不要求面板行数，不要求系统场景数量，不要求逐条点评。

判断：

> 删掉面板后既不损失剧情变化，也不损失必要定位 → 压缩或删除。

## 8. 情绪节点

情绪由事件产生，不能独立当剧情坐标。

如果 S2 的 Chapter Emotional Thread 标注了重大情绪节点，剧情块应给它一个可见出口，优先顺序：

```text
明确决定 > 对白 > 动作 > 身体反应
```

允许仅由决定呈现。身体反应不是默认手段，禁止用瞳孔/呼吸/手指等模板反应堆叠制造“爆点”。

没有重大情绪节点的章节完全合法。

## 9. 爆点

突破、重大获得、重大打脸、死亡级事件需要真实展开，不得一句摘要带过。

旧 `≥5 beats` 仅保留为知识库历史技法参考，不再是剧情块硬门。爆点应保证：

```text
触发发生
→ 结果被现场确认
→ 结果改变局势/身份/能力/关系之一
```

具体写几拍由事件自然决定。

## 10. 模拟执行

模拟块不能靠纯日期/年份快进充当推进。每个时间跳点若保留，必须至少承载一个 SCAN_COORDINATE 或推进当前 BLOCK_PROGRESS。

合法：训练失败暴露门槛、获得关键情报、路线选择、危机后果、突破、身份改变。

不要求每章固定数量的 SYSTEM 镜头。

## 11. 分镜预检（MANDATORY）

剧情块收束后、交给 S3 前执行：

```text
1. CURRENT_BLOCK 是否明确？
2. 本章是否真实推进 BLOCK_PROMISE，或完成已达 EXIT 的自然转场？
3. SCAN_COORDINATES 是否全部造成新事实/信息/决定/结果？
4. 每个正式节点能否拍成“谁做什么 → 什么变了”？
5. 暂时删掉心理、解释、氛围后，是否仍能复述本章事件链？
6. 首屏是否能迅速进入当前事情？
7. 章末是否停在自然闭合点，没有额外尾巴？
```

FAIL 时回到具体节点修剧情块，不在正文阶段用表面润色遮盖。

## 12. 回执

```text
PLOT_BLOCK_SHOT_GATE: PASS | FAIL
BLOCK_PROGRESS: PASS | FAIL
SCAN_COORDINATES_PRESENT: true | false
LABEL_NODE_COUNT: 0（目标）
SHOT_TEST_CLEAR: true | false
FIRST_SCREEN_STORY_VISIBLE: true | false
NATURAL_ENDPOINT_DEFINED: true | false
```

> Memory line: **剧情块先写“这一章发生什么”，再写怎么表达。BLOCK 定大方向，SCAN_COORDINATES 定事件骨架；思考、回忆、情绪都不能冒充剧情坐标。**