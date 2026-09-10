# Narrative State Graph v6.9｜章节活世界状态模型

> applies_to: Story Material Engine v6.18+
> role: Stage 2 internal target-state data model / causal-state validator
> reconstruction_owner: `full-fidelity-story-recomposition.md` v2.6+
> anti_copy_owner: `chapter-reference-adaptation-boundary.md` v4.1+
> block_migration_owner: `block-migration-recomposition.md` v1.0+
> not_a_skill: true

## Purpose

本文件只回答两件事：

1. **目标世界当前到底是什么状态；**
2. **一个候选事件发生后，哪些状态真实改变。**

它是数据模型与状态验证器，不是第二剧情生成器。

```text
STATE MODEL
!= ADAPTATION ALGORITHM
!= MIGRATION DNA OWNER
!= ANTI-RESKIN OWNER
!= STORY MOTION GENERATOR
```

具体迁移 / 重组 / source quarantine / order revalidation / target causal sovereignty / anti-reskin / Story Motion generation 全部服从对应 Owner，本文件不复制第二份算法。

---

# 1. Admission

State Graph 只在当前重构 Owner 已合法进入 Target 具体实现后实例化。

合法上游至少包括：

```text
AUTHOR / FOUNDATION / CANON
STORY SPINE / CURRENT ARC
ADOPTED CURRENT STATE
APPROVED TARGET MACRO / MICRO BLOCK
CURRENT TARGET CHAPTER ROLE
CURRENT BLOCK DNA OBLIGATION when applicable
current reconstruction Owner's legitimate source-value package
```

本文件不重新判断 donor fit，也不重新执行 Migration DNA 抽取。

S2-B 新创造的 Target 具体事实不得倒流成为 S2-A / Source Block 证据。

```text
TARGET_FACT_BACKFLOW_TO_SOURCE_EVIDENCE: FAIL
```

---

# 2. TARGET_NARRATIVE_STATE_0

只维护当前候选故事真正参与因果的状态域：

```text
CHARACTER_STATE
LOCATION_STATE
OBJECT_RESOURCE_STATE
RELATIONSHIP_STATE
WORLD_MOTION_STATE
INFORMATION_LATTICE
OPEN_THREADS
READER_PROMISES
```

## 2.1 CHARACTER_STATE

按实际需要记录：

```text
identity / role
physical condition
capabilities currently available
resources personally controlled
active goal / want / commitment
fear / aversion when causal
knowledge / belief / suspicion
current location / mobility
```

人物只能基于实际知道、相信、怀疑、想要、害怕、承诺的东西和真实拥有的资源行动。

## 2.2 LOCATION_STATE

仅记录会改变当前选择或行动条件的：

```text
where actors / resources are
access / distance / travel constraints
local authority / hazard / visibility conditions
```

## 2.3 OBJECT_RESOURCE_STATE

记录：

```text
owner / controller
quantity / availability when causal
condition / usability
access requirement
consumption / transfer state
```

## 2.4 RELATIONSHIP_STATE

记录真实成立的：

```text
trust / hostility / obligation / debt / responsibility
information asymmetry
power / authority relation
active promise / bargain / threat
```

## 2.5 WORLD_MOTION_STATE

世界不能停着等主角。

记录当前真正会自行变化的：

```text
NPC plans
institutional process
market / ecological motion
threat progression
time window / deadline
other actor movement
```

## 2.6 INFORMATION_LATTICE

每个关键事实区分：

```text
TRUE WORLD FACT
WHO KNOWS
WHO BELIEVES
WHO SUSPECTS
WHO DOES NOT KNOW
SOURCE OF INFORMATION
RELIABILITY when relevant
```

禁止角色使用自己尚未获得的信息。

## 2.7 OPEN_THREADS / READER_PROMISES

`OPEN_THREADS` 记录故事中尚未解决、仍会产生行动后果的问题。

`READER_PROMISES` 只记录已经由故事真实建立的读者等待对象，不在这里创造 suspense。

Reader expectation 的完整语义继续服从 `reader-expectation-architecture.md`。

---

# 3. Event delta model

主要事件按需记录：

```text
EVENT_ID
TRIGGER / PREREQUISITES
ACTIVE_ACTOR
ACTOR_LOCAL_DRIVING_FORCE
ACTOR_LOCAL_GOAL_OR_WANT
ACTOR_INFORMATION_STATE
BEFORE_STATE
ACTION / OCCURRENCE
IMMEDIATE_OUTCOME
STATE_DELTAS
COGNITIVE_DELTAS
RELATIONSHIP_DELTAS when present
RESOURCE_DELTAS when present
WORLD_MOTION_DELTAS when present
RESIDUE
VALUE_EARNED reference when supplied by reconstruction Owner
BLOCK_DNA_PROGRESS reference when supplied by reconstruction Owner
```

本模型只记录 / 校验这些变化是否成立，不自己决定“下一个事件应该是什么”。

---

# 4. State consistency tests

对每个 major candidate event 至少检查：

```text
PREREQUISITE_SATISFIED
ACTOR_HAS_REQUIRED_INFORMATION
ACTOR_HAS_REQUIRED_CAPABILITY / RESOURCE
ACTOR_MOTIVE_SUPPORTED
WORLD_MOTION_NOT_FROZEN
STATE_DELTA_CAUSALLY_SUPPORTED
NO_ILLEGAL_INFORMATION_LEAK
NO_UNEARNED_RESOURCE / ABILITY
```

若事件需要：

```text
人物降智
世界停等
无根据巧合
尚未获得的能力 / 资源
角色知道不该知道的事实
关系无过程瞬间改变
```

则：

```text
STATE_CAUSAL_CONSISTENCY_FAIL: FAIL
```

具体 `FORWARD_CAUSAL_VALIDATION` 的故事算法由 `full-fidelity-story-recomposition.md` 执行；本文件只提供状态事实供其验证。

---

# 5. Local branch support

State Graph 必须允许记录多个目标本地可行分支：

```text
AVAILABLE_LOCAL_ACTIONS
ACTION_PREREQUISITES
ACTOR-PERCEIVED OPTIONS
EXPECTED LOCAL CONSEQUENCES when knowable
```

它不替主角选择。

若 reconstruction Owner 判断某个 local branch 被 source footprint 强行压掉，具体 failure 仍由 reconstruction / anti-copy Owner 报告。

```text
STATE_GRAPH_DOES_NOT_FORCE_SOURCE_ORDER: true
```

---

# 6. Canon / block consistency

State Graph 必须验证候选事件没有越过：

```text
TARGET FOUNDATION / CANON
CURRENT ARC hard constraints
ADOPTED CONTINUITY
APPROVED TARGET BLOCK bounds
CURRENT CHAPTER ROLE bounds
CURRENT CHAPTER FUNCTIONAL STOPPING DEPTH when supplied
```

但以下算法不属于本文件：

```text
Block Migration DNA retention
Chapter Boundary Parity
Reader Expectation re-earning
Anti-reskin comparison
Target Story Motion generation
```

本模型只提供这些 Owner 需要的 before / after state evidence。

---

# 7. Output

正常只输出调用方真正需要的：

```text
TARGET_NARRATIVE_STATE_0
EVENT_STATE_DELTAS
TARGET_NARRATIVE_STATE_N candidate
OPEN_THREADS_AFTER_EVENT
READER_PROMISE_STATE reference
STATE_CAUSAL_CONSISTENCY: PASS / FAIL
```

不再输出第二份：

```text
adaptation route
source quarantine plan
anti-reskin matrix
Migration DNA
Story Motion
Final Human Retelling
```

这些由唯一 Owner 输出。

---

# 8. Hard failures

```text
TARGET_FACT_BACKFLOW_TO_SOURCE_EVIDENCE
STATE_CAUSAL_CONSISTENCY_FAIL
ILLEGAL_INFORMATION_USE
UNEARNED_RESOURCE_OR_ABILITY
WORLD_MOTION_FROZEN_FOR_PLOT
UNSUPPORTED_RELATIONSHIP_DELTA
STATE_GRAPH_SOURCE_ORDER_FORCING
```

任一失败交还当前 reconstruction Owner：

```text
REPORT exact state contradiction
→ repair smallest owning story layer
→ rerun state validation
→ still fail: STOP
```

## Memory line

> **State Graph 只记“世界现在是什么、事件以后变成什么”。它是剧情发动机的仪表盘，不再自己当第二台发动机。**
