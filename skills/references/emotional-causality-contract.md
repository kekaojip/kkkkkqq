# Emotional Causality Contract｜章节情绪因果 + 跨章余波

> version: 1.4
> status: production-main
> role: cross-stage invariant for S2 → S3 → Tracking

## First principle

```text
剧情有因果，人物也要有情绪因果。
场景可以结束，情绪不能自动结算。
人物的冷静体现在选择上，不等于人物什么都不在乎。
```

这不是要求每章都持续升压，也不是要求人物不停哭、怒、回忆。
它只要求：重要事件如果真的伤到、刺激到、鼓舞到人物，必须留下可以继续影响后文的情绪结果。

---

## S2｜Chapter Emotional Thread

S2 在当前章剧情块与人物块收束时，只在 materially required 时生成一条**极薄**的章节情绪线。

后台只回答四件事：

```text
CHAPTER_EMOTIONAL_START
= 这一章开始时，POV 人物带着什么情绪 / 心态进入

EMOTIONAL_PRESSURE / CHANGE
= 哪些已批准关键事件真正改变、加重、扭转或释放了它

CHAPTER_EMOTIONAL_ENDPOINT
= 章末人物在情绪上与章初相比哪里不同

RESIDUE_TO_NEXT_CHAPTER
= 哪一点还没有结算，必须带进下一章
```

规则：

```text
CHAPTER_EMOTIONAL_THREAD: required when the chapter contains meaningful emotional change
CHAPTER_EMOTIONAL_THREAD_THIN: required
PLOT_CAUSALITY_WITHOUT_EMOTIONAL_CAUSALITY: forbidden by default
EMOTIONAL_THREAD_HAS_NEW_PLOT_AUTHORITY: false
```

章节情绪线不能改变已批准剧情，只负责说明这些事件连续落在人身上以后，情绪怎么走。

### Author-facing output hard lock｜第一章式唯一模板

作者前台如果需要展示【章节情绪线】，只能使用下面这一种排版和粒度：

```text
【章节情绪线】

章初状态：
……

情绪推进：
1. 已批准剧情节点。
   → 这一节点对 POV 人物造成的情绪变化 / 心理成本。
2. 已批准剧情节点。
   → 这一节点怎样继续碰到前面的余波、加重 / 扭转 / 释放它。
3. ……（只列真正改变情绪的关键节点；没有就不凑数）

章末状态：
……

带到下一章：
……
```

这四个槽位分别对应：

```text
章初状态 = CHAPTER_EMOTIONAL_START
情绪推进 = EMOTIONAL_PRESSURE / CHANGE
章末状态 = CHAPTER_EMOTIONAL_ENDPOINT
带到下一章 = RESIDUE_TO_NEXT_CHAPTER
```

第一章式粒度要求：

```text
THIN_NOT_ESSAY: true
ONLY_MATERIAL_EMOTIONAL_CHANGES: true
ONLY_APPROVED_PLOT_NODES: true
NO_FORCED_NODE_COUNT: true
NO_THEME_ANALYSIS: true
NO_CHARACTER_GROWTH_ESSAY: true
NO_PLOT_RETELLING: true
NO_SCENE_EXPANSION: true
NO_NEW_DIALOGUE: true
NO_NEW_EVENT: true
```

允许每个槽位写一到数个短段，但不得自由改成别的作者前台格式。

### 禁止漂移

不得把【章节情绪线】写成：

```text
若干段连续长篇人物成长分析
整章剧情复述
主题 / 价值 / 成长意义分析
情绪矩阵
强度打分
每节点情绪标签
身体反应表
心理学模型
起承转合文学评论
“本章核心是……”式总结报告
表格
另造字段
```

尤其禁止：

```text
把 Plot 节点从头到尾再讲一遍
→ 再在每个剧情节点后补一句情绪
```

如果删掉情绪词以后，剩余内容仍能作为完整剧情梗概阅读：

```text
EMOTIONAL_THREAD_PLOT_CONTAMINATION: FAIL
```

如果输出没有严格使用：

```text
章初状态
情绪推进
章末状态
带到下一章
```

则：

```text
EMOTIONAL_THREAD_LAYOUT_GATE: FAIL
→ rerender same emotional logic using the fixed four-slot template
→ do not ask for author approval yet
```

如果内容明显变成长篇分析、剧情复述或新增剧情：

```text
EMOTIONAL_THREAD_THINNESS_GATE: FAIL
→ trim back to material emotional causality only
→ do not change approved Plot / Character
```

播报与【生产进度】只能放在情绪线本体之后。

```text
PROGRESS_RECEIPT_POSITION: AFTER_EMOTIONAL_THREAD_BODY
PROGRESS_RECEIPT != EMOTIONAL_THREAD_BODY
```

### 第一章回归基准

第一章正式采用的形态就是回归基准：

```text
章初状态：
沈越已经在香波地活了一年，习惯先保命，也习惯用“海贼王世界就是这样”把见过的烂事归档过去。平时仍能嘴欠、过日子，不是持续阴沉状态。

情绪推进：
1. 镀膜大叔被天龙人随手带走。
   → 沈越算出不能动，选择忍；这个正确选择留下憋屈、不甘，以及生活被掐掉一块的感觉。
2. 自己又被人口生意的人抓走。
   → 他仍然选择先活，但上一次的余波没有消失，“这种忍正在成为常态”的感觉开始出现。
3. 看见一家四口为了莉娜一个接一个失败。
   → 他再次算出现在动手没有第二步；答案仍然正确，却已经更难咽。

章末状态：
莉娜最后看向沈越时，他第一次真正受不了自己越来越熟练地把这些事情归成“正常”。

带到下一章：
他仍认可“先活下来”的现实判断，但已经无法毫无负担地把旁观当成正常；对“没有第二步所以只能忍”留下明确厌恶和不甘，莉娜那一眼继续留到下一章。
```

此样例锁的是**版式、粒度和职责**，不是要求后续章节复制第一章的具体情绪内容。

---

## S3｜Emotional Residue

S3 正文必须实现 S2 的章节情绪线，并遵守：

```text
EMOTIONAL_RESIDUE_CONTINUES: required
SCENE_CHANGE != EMOTIONAL_RESET
COOL_DECISION != NO_FEELING
```

同一个稳定人物逻辑可以重复，但心理成本不能机械归零。

例如：

```text
第一次做出“忍”的选择
→ 留下一点憋屈

下一次仍然选择“忍”
→ 旧余波被碰到，可能更烦、更难咽、更麻木或发生别的变化

章尾触发
→ 前面积累出来的东西发生真正变化 / 释放
```

禁止用反复回忆、反复点名情绪来证明连续。
余波应尽量通过人物当下注意、措辞、动作、沉默、旧抓手和 POV 旁白自然流出。

S3 同时遵守：

```text
NARRATION_CARRIES_POV_EMOTION: required
NEUTRAL_CAMERA_NARRATION: forbidden as default
```

近距离第三人称旁白应被当前 POV 的脾气、情绪和判断染色，而不是先中立播报事实，再另起一句解释人物感受。

---

## Tracking｜Cross-chapter Emotional State

Tracking continuity commit 不只保存：

```text
发生了什么
谁知道什么
谁在哪
获得了什么
关系变成什么
```

还必须在有意义时保存：

```text
CURRENT_EMOTIONAL_RESIDUE
```

实质跨章余波优先写入对应角色当前状态：

```text
追踪/角色状态/{角色}.md
→ CURRENT_EMOTIONAL_RESIDUE
```

只保存会真实影响下一章行为、注意力、叙述口吻或选择成本的余波，不保存一闪而过的小情绪。

最小格式：

```text
CURRENT_EMOTIONAL_RESIDUE:
- POV 人物当前还没过去的感觉 / 心结 / 兴奋 / 不甘 / 羞耻 / 期待等
- 它现在如何影响人物
- 什么已经结算，不必继续带
```

下一章 S2 / S3 必须把这个状态当作 continuity 输入，而不是从默认人格重新开始。

```text
TRACKING_WITHOUT_RELEVANT_EMOTIONAL_RESIDUE: incomplete when residue materially affects next chapter
NEXT_CHAPTER_EMOTIONAL_RESET: forbidden
```

---

## Book-specific locks

本合同只定义通用规则。
具体主角如何“冷静但不无感”、哪些情绪会留下、哪些会消散，必须写在对应书的 `PROJECT_STATE.md` / author locks 中，不得把单书人物名或单书情绪结论硬编码进本全局合同。

---

## Boundary

情绪因果没有新剧情权。

```text
EMOTIONAL_THREAD_HAS_NEW_PLOT_AUTHORITY: false
EMOTIONAL_RESIDUE_HAS_NEW_PLOT_AUTHORITY: false
TRACKING_EMOTION_HAS_NEW_PLOT_AUTHORITY: false
```

不得为了“让情绪更完整”新增事件、拖长 BRIDGE_FAST、改变人物最终决定或提前制造后续剧情。

## Memory line

> **章节情绪线只有需要时才出现，而且永远很薄。作者前台固定四槽：章初状态 → 情绪推进 → 章末状态 → 带到下一章；只写已批准剧情造成的实质情绪变化，不重讲 Plot、不写成长分析、不新增剧情。S3 让这些感觉在正文里不断线，Tracking 保存真正未结算的跨章余波。**
