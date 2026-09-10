# Character Reaction Patch v1.1｜人物即时反应补丁

> status: production-main
> owner: skills/prose-preparation/routes/s3a-golden-direct-source.md
> applies_to: SOLE_S3_DIRECT_EDIT_ROUTE
> story_authority: NONE
> reaction_authority: LOCAL_ONLY

## 0. Mission

本层只解决一个问题：

> **同一个已锁定事件撞到这个具体人物身上时，他会自然产生什么即时反应？**

它不改故事，不替代 Direct Source Edit，不承担全文润色。

```text
REACTION_AUTHORITY: YES
PLOT_AUTHORITY: NO
WHOLE_CHAPTER_REWRITE: NO
```

## 1. Inputs

至少读取：

```text
S1 F01 PROTAGONIST_BEHAVIOR_CONTRACT
protagonist-cultural-residue when applicable
CURRENT_STATE / current relationship state when available
current locked Story Motion beat
current Direct Edit span
```

不得新造第二套 Character DNA。

## 2. Trigger test

对重要 beat 只问：

```text
WOULD_THIS_SPECIFIC_CHARACTER_NATURALLY_SHOW_A_DISTINCTIVE_REACTION_HERE?
```

若 NO：不补。

若 YES，只从真实需要的部分选择：

```text
PERCEPTION
INTERPRETATION
IMPULSE
EXPRESSION
```

不要求全部显式写出。

## 3. Allowed local reactions

允许即时吐槽、自然接话、自嘲、轻微损人、现代式反问、现代生活类比、IP / 流行文化联想 when canonically known、荒诞感反应、真实兴奋、失望、嫌弃、嘴硬、犹豫、小算盘、话到嘴边改口、关系化语气、短促内心反应。

这些必须依赖已发生事实，不能创造新的故事条件。

## 4. Forbidden

不得生成：

```text
新剧情
新线索
新规则
新奖励
新解决方案
新伏笔
新关系转折
新角色功能
新任务
新敌意来源
新未来 payoff debt
```

若反应要求 Story Motion 之外的新行动：

```text
REACTION_PATCH_PLOT_LEAK: FAIL
```

## 5. No meme quota

禁止每章必须玩梗、每场景必须吐槽、每 N 字一个笑点、热梗清单强插。

```text
meme / joke / modern analogy
= available character resource
!= decoration quota
```

## 6. Seriousness switch

真实死亡、重大受伤、他人强烈痛苦、不可逆损失、高压生死决定、需要保留恐惧/悲伤/愤怒重量的情绪兑现，默认降低轻松表达。

除非 F01 明确锁定黑色幽默应压。

```text
SERIOUSNESS_SWITCH > MEME_AVAILABILITY
```

## 7. Placement

优先在已有 Direct Edit 的自然缝隙补入：现有内心反应位置、对白位置、停顿位置、beat 结果落下处、人物获得新信息处。

不为了补人味大规模拆段、重排 Source 语言载体。

如果 patch 需要重写上下多句：

```text
PATCH_TOO_LARGE: FAIL
```

## 8. Character fidelity tests

```text
REACTION_SOURCE: existing character foundation
REACTION_TRIGGER: existing story fact
NEW_PLOT_BEAT_COUNT: 0
NEW_RULE_COUNT: 0
NEW_SOLUTION_COUNT: 0
OOC_COUNT: 0
```

现代穿越者适用时额外检查：

```text
CULTURAL_RESIDUE_UNJUSTIFIED_SUPPRESSION
MEME_SPAM
SERIOUSNESS_SWITCH_VIOLATION
```

## 9. Output receipt

```text
CHARACTER_REACTION_PATCH_COUNT: n
REACTION_PATCH_PLOT_LEAK_COUNT: 0
OOC_COUNT: 0
MEME_QUOTA_USED: false
WHOLE_CHAPTER_REWRITE_USED: false
```

## Memory line

> **人物有反应权，没有剧情权。该吐槽时可以吐槽，该兴奋时会兴奋，该收的时候就收；补丁只扎在局部，不重新写整篇。**