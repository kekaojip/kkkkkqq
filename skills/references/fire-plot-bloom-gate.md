# Fire Target Plot Bloom Gate｜目标剧情开花验收门

> status: production-main
> authority: S2 TARGET-PLOT PRE-ADOPTION HARD GATE
> owner: S2 Story Material Engine
> algorithm_owner: `../story-material-engine/references/source-to-target-combination.md`
> timing_owner: this gate
> plot_output_owner: `plot-block-output-contract.md`
> tool: Firecrawl

## 0. First principle

本 Gate 不拥有第二套剧情构思算法，也不拥有最终剧情决定权。

它只确保 Fire 在**已有目标剧情块初版候选之后、作者批准之前**，对现有剧情做受控增殖，并把有用生长交回 S2 收束。

```text
FIRE_TARGET_PLOT_BLOOM_REQUIRED: true
FIRE_IS_CONTROLLED_DIVERGENCE: true
FIRE_IS_FACT_CHECK_ONLY: false
THIS_GATE_FINAL_PLOT_AUTHORITY: NONE
```

核心：

```text
已有剧情树干
→ Fire 让剧情长活
→ S2 剪枝
→ 强制完整回写剧情块
→ 作者批准
```

考据只负责护栏，不能冒充开花完成。

---

## 1. Canonical position

启用母本模式：

```text
Tracking / continuity
→ 母本 Human Retelling + Character Trace
→ Source Framework Fidelity when required
→ Source-to-Target
→ Target Plot Block PRE-FIRE Candidate
→ Target Fire Bloom
→ ABSORB / REJECT BLOOM BRANCHES
→ MANDATORY FULL PLOT BLOCK REWRITE
→ Plot Block Output Gate
→ SHOW POST-FIRE AUTHOR CANDIDATE
→ AUTHOR APPROVAL
→ Target Character Block
```

不启用母本模式：

```text
Tracking / current author idea
→ Target Plot Block PRE-FIRE Candidate
→ Target Fire Bloom
→ ABSORB / REJECT BLOOM BRANCHES
→ MANDATORY FULL PLOT BLOCK REWRITE
→ Plot Block Output Gate
→ SHOW POST-FIRE AUTHOR CANDIDATE
→ AUTHOR APPROVAL
→ Target Character Block
```

硬顺序：

```text
PLOT PRE-FIRE CANDIDATE
→ TARGET FIRE BLOOM
→ MANDATORY FULL PLOT BLOCK REWRITE
→ AUTHOR APPROVAL
→ CHARACTER BLOCK
```

```text
FIRE_BEFORE_TARGET_PLOT_CANDIDATE: forbidden
PLOT_APPROVAL_BEFORE_FIRE_BLOOM: forbidden
POST_FIRE_FULL_PLOT_REWRITE_REQUIRED: true
```

---

## 2. What valid Target Bloom actually does

合法 Fire 调用必须围绕已经存在的目标剧情候选，并优先寻找**剧情增长**：

```text
NODE CONTINUATION
= 当前节点还能自然接出什么事件

REACTION GROWTH
= 既有事件会让人物 / 势力出现什么更有戏的反应

CONSEQUENCE GROWTH
= 当前动作还能造成哪些即时或延迟后果

PRESSURE ESCALATION
= 怎样让压力自然升级

PAYOFF GROWTH
= 旧伏笔 / 情绪 / 能力怎样得到更好的兑现

FORESHADOW GROWTH
= 哪些未来线可以轻埋

SCENE LIFE
= 哪些具体事故 / 环境反馈 / 小误会能让节点更活

WORLD RIPPLE
= 这个事件怎样让世界里其他人产生不同欲望与行动
```

典型问题应当是：

```text
这个节点已经确定以后，还能自然长出什么更有戏的事件与后果？

保持主事件不变，怎样让现场反应、局势升级和人物选择更活？

哪些世界设定可以转化成事件，而不是停在说明层？
```

世界观搜索可以发生，但必须：

```text
FACT / LORE
→ STORY POSSIBILITY
```

不能：

```text
FACT FOUND
→ BLOOM COMPLETE
```

---

## 3. Trunk preservation

Fire 允许：

```text
长局部事件
长人物 / 势力反应
长后果
长伏笔
长世界涟漪
补局部因果
```

Fire 不允许自行：

```text
推翻现有主树干
重启整章
改作者已经确认的核心走向
把当前章改成另一条主线
```

```text
FIRE_MAY_GROW_BRANCHES: true
FIRE_MAY_REPLACE_CURRENT_TRUNK_BY_ITSELF: false
FIRE_MAY_RESTART_PLOT_FROM_ZERO: false
```

---

## 4. Author-facing Fire presentation

默认禁止：

```text
A / B / C / D
方案一 / 方案二 / 方案三
请选择一个
```

除非作者明确要求多个方案。

默认用连续自然语言顺着现有剧情往下想，让作者感觉剧情在生长，而不是在看菜单。

```text
DEFAULT_CHOICE_WALL: forbidden
CONTINUOUS_NATURAL_GROWTH_PRESENTATION: required
```

---

## 5. What does NOT count

以下不能通过本 Gate：

```text
只查母本事实
只查 One Piece 世界设定
只做时间线校验
只确认地点 / 势力 / 人物是否存在
只做合理性审计
泛创作技巧搜索
```

```text
WORLD_FACT_CHECK_ONLY: FAIL
TIMELINE_CHECK_ONLY: FAIL
PLAUSIBILITY_ONLY: FAIL
GENERIC_WRITING_SEARCH: FAIL
```

如果主要结果只是：

```text
这里合理
这里符合原作
这里时间线没问题
这里有海军基地
```

但没有长出新的可用事件 / 反应 / 后果 / 伏笔 / 局势变化：

```text
FIRE_BLOOM_MISUSED: true
FIRE_TARGET_PLOT_BLOOM: INCOMPLETE
```

不得标 `[✓]`。

---

## 6. Fire → Plot mandatory closure

Fire 完成不是 Plot 阶段出口。

Fire 之后必须：

```text
CURRENT PLOT TRUNK
+ AUTHOR LATEST IDEAS
+ USEFUL FIRE GROWTH
→ ABSORB / REJECT LOCALLY
→ MANDATORY FULL PLOT BLOCK REWRITE
→ validate under plot-block-output-contract.md
→ SHOW one complete Plot Block
```

可选的是：

```text
是否吸收某一条枝
是否改变某个局部处理
```

不可选的是：

```text
Fire 后是否完整回写剧情块
```

```text
OPTIONAL_BRANCH_ADOPTION: true
POST_FIRE_FULL_PLOT_REWRITE_REQUIRED: true
FIRE_RESULT_ALONE_IS_PLOT_BLOCK: false
FIRE_SUMMARY_ALONE_IS_PLOT_BLOCK: false
```

如果 Fire 已完成但完整回写没完成：

```text
FIRE_TARGET_PLOT_BLOOM: COMPLETE
POST_FIRE_FULL_PLOT_REWRITE: INCOMPLETE
AUTHOR_PLOT_APPROVAL: BLOCKED
```

恢复时不得重跑 Fire，直接继续完整回写。

---

## 7. Plot output shape handoff

Fire 后回写的作者前台【剧情块】必须服从：

`skills/references/plot-block-output-contract.md`

硬形态：

```text
MEDIUM-GRANULARITY CONTINUOUS RETELLING
NOT BEAT SHEET
NOT SCENE OUTLINE
NOT PROSE
NOT NODE CHECKLIST
NOT PROCESS SUMMARY
```

Fire 开出的枝条不能把剧情块膨胀成半正文。

```text
FIRE_GROWTH != PROSE_EXPANSION
```

---

## 8. Dwell-weight firewall

Fire 可以长枝，但不拥有停留权重。

```text
SOURCE EXPAND → Target 可充分长肉
SOURCE NORMAL → Target 给够动作与因果
SOURCE BRIDGE_FAST → Target 仍快速通过
```

禁止因为 Fire 有很多有趣结果就：

```text
把桥段养成完整支线
无限增加配角镜头
让世界伏笔抢掉本章主事件
把所有开出的花都塞进一个章
```

开花负责长，S2 负责剪。

---

## 9. Pass condition

在作者批准 Plot 前必须同时满足：

```text
TARGET_PLOT_BLOCK_PRE_FIRE_CANDIDATE_EXISTS: true
TARGET_CANDIDATE_NODE_SPECIFIC_FIRE_CALL_COUNT >= 1
PLOT_GROWTH_MATERIAL_CAPTURED: true
AT_LEAST_ONE_NEW_USABLE_EVENT_OR_REACTION_OR_CONSEQUENCE_OR_FORESHADOW_BRANCH: true
FIRE_DID_NOT_REWRITE_CURRENT_TRUNK_BY_ITSELF: true
```

此时只能标：

```text
FIRE_TARGET_PLOT_BLOOM: COMPLETE
```

还不能批准 Plot。

之后必须：

```text
POST_FIRE_FULL_PLOT_REWRITE: COMPLETE
PLOT_BLOCK_OUTPUT_GATE: PASS
```

才允许：

```text
SHOW POST-FIRE AUTHOR CANDIDATE
→ AUTHOR PLOT APPROVAL
```

如果 Firecrawl 不可用或真实失败：

```text
REPORT FIRE_TARGET_PLOT_BLOOM_BLOCKED
→ keep Plot candidate unapproved
→ STOP
```

不得拿母本搜索或世界观考据兜底。

---

## 10. Relationship to Character Fire

```text
Target Plot Fire Bloom
= 在已有 Plot 初版上长事件、反应、后果、局势、伏笔

Character Reaction Fire Calibration
= Plot 已批准后，校准人物在既定事件里怎么活
```

人物阶段不得反过来新增 / 重排 Plot。

---

## 11. Progress receipt

前台统一：

```text
目标剧情 Fire 开花 [✓/◐/ /-]
```

只有真实产生剧情生长材料后才能 `[✓]`。

但即使 Fire `[✓]`，剧情块在完整回写并展示前仍不能 `[◐]`。

```text
FIRE COMPLETE + FULL PLOT REWRITE NOT SHOWN
→ Fire [✓]
→ Plot [ ]
```

```text
FIRE COMPLETE + FULL PLOT REWRITE SHOWN
→ Fire [✓]
→ Plot [◐]
```

---

## Memory line

> **先有剧情树干，再让 Fire 把剧情长活。Fire 只负责受控增殖，考据只是护栏。Fire 后必须剪枝并强制回写一份完整、中粒度、连续自然语言的【剧情块】；枝条吸收可选，完整回写不可选。剧情块没按正确形态回写，就不能交作者批准。**