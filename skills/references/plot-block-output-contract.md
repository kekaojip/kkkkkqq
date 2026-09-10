# Plot Block Output Contract｜剧情块回写与输出硬锁

> status: production-main
> authority: S2 TARGET PLOT AUTHOR-VISIBLE OUTPUT HARD CONTRACT
> applies_to: pre-fire plot candidate + post-fire rewritten plot candidate
> canonical_route_owner: `skills/PRODUCTION_MAP.md`
> fire_timing_owner: `skills/references/fire-plot-bloom-gate.md`

## 0. First principle

【剧情块】不是细纲，不是正文，不是节点清单，也不是流程摘要。

【剧情块】的唯一默认前台形态是：

> **用中粒度、连续自然语言，把这一章从开头到结尾发生了什么、为什么发生、局势怎么变化，一口气讲清楚。**

它应当像作者和搭档已经把这一章想明白以后，对着整章故事做一次清楚、顺畅、可直接判断走向的复述。

```text
TARGET_PLOT_BLOCK_OUTPUT_MODE: MEDIUM-GRANULARITY_CONTINUOUS_RETELLING
AUTHOR_FACING_SHAPE: CONTINUOUS_NATURAL_LANGUAGE
```

---

## 1. Mandatory chain｜Fire 后必须回写

硬链路：

```text
TARGET PLOT BLOCK PRE-FIRE CANDIDATE
→ TARGET FIRE BLOOM
→ ABSORB / REJECT BLOOM BRANCHES
→ MANDATORY FULL PLOT BLOCK REWRITE
→ POST-FIRE AUTHOR CANDIDATE
→ AUTHOR APPROVAL
→ CHARACTER BLOCK
```

Fire 结束以后，**不能**把 Fire 文件、Fire 结论、节点清单或“吸收建议”当作 Plot 阶段出口。

必须重新生成一份完整【剧情块】。

```text
POST_FIRE_FULL_PLOT_REWRITE_REQUIRED: true
FIRE_RESULT_ALONE_IS_PLOT_BLOCK: false
FIRE_SUMMARY_ALONE_IS_PLOT_BLOCK: false
FIRE_KEEP_AVOID_LIST_IS_PLOT_BLOCK: false
```

即使 Fire 最终只吸收一个小枝条，也仍必须把它自然融回整份剧情块，再提交作者审核。

如果 Fire 后没有完整回写：

```text
POST_FIRE_PLOT_REWRITE_GATE: FAIL
AUTHOR_PLOT_APPROVAL: BLOCKED
```

---

## 2. Exact plot-block granularity｜只能是这个粒度

剧情块必须介于“细纲”和“正文”之间。

必须做到：

```text
能看清整章起点
能看清主要事件怎么连续发生
能看清关键因果桥
能看清主角关键选择
能看清局势如何升级 / 转折
能看清章尾落点与下一阶段压力
```

但不能下沉到：

```text
逐镜头调度
逐动作拆解
具体对白大段展开
环境描写铺陈
心理活动逐句展开
战斗招式逐拍描写
正文式气氛渲染
```

也不能上浮成：

```text
节点 1 / 节点 2 / 节点 3
A / B / C / D
方案一 / 方案二 / 方案三
功能点列表
事件箭头链
一句话梗概
流程摘要
Backstage function coverage 代替剧情本体
```

硬规则：

```text
PLOT_BLOCK_AS_BEAT_SHEET: forbidden
PLOT_BLOCK_AS_SCENE_OUTLINE: forbidden
PLOT_BLOCK_AS_PROSE_DRAFT: forbidden
PLOT_BLOCK_AS_NODE_CHECKLIST: forbidden
PLOT_BLOCK_AS_OPTION_WALL: forbidden
PLOT_BLOCK_AS_PROCESS_SUMMARY: forbidden
```

---

## 3. Author-facing form｜前台只能这样

默认作者前台只展示：

```text
## 【剧情块】

若干段连续自然语言
```

允许自然分段，但每段仍然是在讲剧情，不得把剧情拆成编号式流程。

推荐阅读感：

> **像把这一章完整讲给作者听，而不是把这一章拆给执行器看。**

一个合格剧情块通常应当让作者读完以后能直接回答：

- 这一章从哪里接上来；
- 主角做了什么；
- 为什么会走到下一步；
- 中间出了什么变化；
- 最后把故事推到了哪里。

但前台不要求把这些问题列出来。

---

## 4. Fire absorption rule｜开花只能优化进去

Fire 的正确关系：

```text
ORIGINAL PLOT TRUNK
+ AUTHOR LATEST IDEAS
+ USEFUL FIRE GROWTH
→ ONE NEW COMPLETE PLOT BLOCK
```

不是：

```text
原剧情块
+ Fire 文件
+ 一份改动摘要
```

Fire 开出的枝条必须经过剪枝后自然融入整章走向。

吸收时优先：

```text
让剧情更活
让因果更顺
让已有节点更有反应
让世界产生自然涟漪
让旧伏笔更好回收
让新伏笔轻量落下
```

但不能因为 Fire 长了很多枝，就把剧情块写成半正文。

```text
FIRE_GROWTH != PROSE_EXPANSION
```

---

## 5. Rewrite preservation rule｜优化，不另起炉灶

Post-Fire 重写默认必须保留已经确认的主树干，只把新增长内容优化进去。

```text
POST_FIRE_REWRITE_MODE: INTEGRATE_AND_OPTIMIZE
RESTART_FROM_ZERO: forbidden_by_default
TRUNK_REPLACEMENT_WITHOUT_AUTHOR_DIRECTION: forbidden
```

如果作者已经确认“整体走向没问题”，Fire 后重写不能借机偷偷重做整章方向。

正确感觉：

> **还是刚才那一章，只是长得更顺、更活、更完整。**

---

## 6. Output gate｜形态不对就不能提交作者批准

提交作者审核之前必须同时通过：

```text
PLOT_BLOCK_FULL_CHAPTER_CAUSALITY_VISIBLE: PASS
PLOT_BLOCK_MEDIUM_GRANULARITY: PASS
PLOT_BLOCK_CONTINUOUS_RETELLING_SHAPE: PASS
PLOT_BLOCK_NOT_BEAT_SHEET: PASS
PLOT_BLOCK_NOT_PROSE: PASS
PLOT_BLOCK_NOT_PROCESS_SUMMARY: PASS
POST_FIRE_BLOOM_ABSORBED_INTO_PLOT: PASS when Fire used
```

任何一项失败：

```text
PLOT_BLOCK_OUTPUT_GATE: FAIL
→ rerender the same plot at correct granularity
→ do not ask for author approval yet
```

---

## 7. Backstage material

后台可以保存：

```text
source-function coverage
Fire branches
keep / reject reasoning
continuity checks
world-rule checks
```

但这些都不能代替作者前台【剧情块】。

```text
BACKSTAGE_ANALYSIS != AUTHOR_FACING_PLOT_BLOCK
```

---

## 8. Relationship to Fire Gate

若 `fire-plot-bloom-gate.md` 中存在旧措辞：

```text
OPTIONAL PLOT REVISION
```

则按本 Contract 解释为：

```text
是否改变主树干 / 是否吸收某条 Fire 枝是 optional
但 Fire 完成后重新输出完整 Plot Block 是 mandatory
```

因此：

```text
OPTIONAL_BRANCH_ADOPTION: true
POST_FIRE_FULL_PLOT_REWRITE: mandatory
```

---

## Memory line

> **剧情块只能是中粒度连续复述：不是细纲，不是正文，不是节点清单。Fire 开花后不管吸收多少，都必须把有用内容优化回原剧情树干，重新写出一份完整【剧情块】再交作者批准。还是刚才那一章，只是更顺、更活、更完整。**