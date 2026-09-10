# Story Material Engine local authority

> applies_to: Story Material Engine v9.5+
> role: Stage 2 local authority router

Before Stage 2 execution:

```text
read SKILL.md
read PROJECT_STATE / required Foundation + Current State pointers
read ../references/author-visible-step-gate.md
then load only references required by current need
```

```text
DEFAULT_READ_ALL_REFERENCES: FORBIDDEN
```

---

# Active authority map

```text
Stage 2 routing / admission / exit
→ SKILL.md v9.5+

continuous human-AI story co-creation
→ references/story-room.md v2.1+

on-demand deep similar-fiction research
→ references/fiction-plot-case-retrieval.md v1.1+

S2 source breakdown block 1
→ references/human-retelling-core.md v1.2+ AUTHOR_LOCKED

S2 source breakdown block 2
→ references/character-trace.md v1.2+ AUTHOR_LOCKED_OUTPUT_TEMPLATE

source breakdown → target story co-creation combination loop
→ references/source-to-target-combination.md v0.9+

source framework / bridge-function fidelity
→ references/source-framework-fidelity-gate.md v1.0+

target plot Fire timing / pass gate
→ ../references/fire-plot-bloom-gate.md

author-visible sequential approval
→ ../references/author-visible-step-gate.md
```

```text
NO FILE MAY RECREATE ANOTHER OWNER'S ALGORITHM
```

---

# Author-locked S2 two-block source breakdown

Formal source breakdown contains exactly two default core blocks:

```text
BLOCK 1 — HUMAN RETELLING CORE
BLOCK 2 — CHARACTER TRACE
```

Required route:

```text
SOURCE / NOVEL
→ locate coherent concrete story block
→ RETELLING_BRIDGE_NODES
→ HUMAN_RETELLING_CORE
→ RETELLING_BRIDGE_COVERAGE_GATE
→ CHARACTER TRACE
→ CHARACTER_TRACE_LAYOUT_GATE
→ S2_SOURCE_BREAKDOWN_TWO_BLOCKS: PASS
```

Author-facing labels are locked:

```text
SOURCE HUMAN RETELLING CORE → 【母本剧情复述】
SOURCE CHARACTER TRACE       → 【母本人物追踪】
TARGET PLOT BLOCK            → 【剧情块】
TARGET CHARACTER BLOCK       → 【人物块】
```

```text
SOURCE_CHARACTER_TRACE != TARGET_CHARACTER_BLOCK
SOURCE_CHARACTER_TRACE_COMPLETE != TARGET_CHARACTER_BLOCK_COMPLETE
```

Human Retelling author-facing output must be long continuous natural prose first. Backstage causal-chain / value / function analysis may not replace it.

Character Trace author-facing output must follow the exact three-field template owned by `references/character-trace.md`:

```text
人物名
状态：...
动作 / 话：...
结果：...
```

```text
HUMAN_RETELLING_CORE_CONTINUOUS_PROSE: REQUIRED
ANALYSIS_FIRST_SOURCE_OUTPUT: FORBIDDEN
BULLET_SUMMARY_AS_RETELLING: FORBIDDEN
CHARACTER_TRACE_LAYOUT_GATE: REQUIRED
SOURCE_TARGET_CHARACTER_LABEL_COLLISION: FORBIDDEN
```

---

# Source-to-target combination loop

Admission is hard-locked:

```text
HUMAN_RETELLING_CORE: PASS
+ RETELLING_BRIDGE_COVERAGE_GATE: PASS
+ CHARACTER_TRACE: PASS
+ CHARACTER_TRACE_LAYOUT_GATE: PASS
= S2_SOURCE_BREAKDOWN_TWO_BLOCKS: PASS
→ only then SOURCE FRAMEWORK FIDELITY / SOURCE-TO-TARGET COMBINATION
```

Source Character Trace may not be deferred until after Target Plot construction.

## Correct target-plot sequence

Current canonical timing is:

```text
COMPLETED SOURCE TWO-BLOCK BREAKDOWN
→ identify source bridge / progression functions
→ source framework fidelity check
→ AUTHOR + AI co-create our Target Plot
→ every new target event passes framework-function + causal-bridge gate
→ reach a coherent Target Plot Block candidate
→ TARGET-SPECIFIC FIRE BLOOM against that existing candidate
→ Fire Gate PASS
→ absorb useful Fire material / revise candidate when useful
→ SHOW final Target Plot Block candidate
→ STOP for author approval
→ only after author approval enter TARGET CHARACTER BLOCK
```

This timing is hard-locked:

```text
TARGET_PLOT_CANDIDATE_BEFORE_TARGET_FIRE_BLOOM: REQUIRED
TARGET_FIRE_BLOOM_BEFORE_PLOT_AUTHOR_APPROVAL: REQUIRED
FIRE_BLOOM_WITHOUT_TARGET_CANDIDATE: FORBIDDEN
PLOT_AUTHOR_APPROVAL_BEFORE_REQUIRED_FIRE_BLOOM: FORBIDDEN
```

`references/source-to-target-combination.md` owns the source-to-target combination logic, source skeleton fidelity, node functions, dwell weights, target recombination, and local realization logic.

`../references/fire-plot-bloom-gate.md` owns the timing of the mandatory Target Plot Fire Bloom.

Therefore any historical wording inside `source-to-target-combination.md` that appears to run Target Fire before a coherent Target Plot candidate is formed is treated as an old execution-order description, not current timing authority.

```text
SOURCE_TO_TARGET_OWNS_COMBINATION_LOGIC: true
FIRE_PLOT_BLOOM_GATE_OWNS_BLOOM_TIMING: true
```

The Fire result remains stimulus, not Canon and not Plot authority.

```text
FIRE_RESULT_IS_STIMULUS_NOT_CANON: true
FIRE_REWRITES_SOURCE_SKELETON: forbidden
FIRE_AUTO_APPROVES_PLOT: forbidden
```

If the Target chapter is thin, return to underbuilt source-heavy nodes instead of inventing unrelated side quests or inflating fast bridges.

```text
CAPACITY_REPAIR_BY_SIDE_QUEST: forbidden
BRIDGE_INFLATION: forbidden
```

---

# Recovery state

A new intermediate state now exists and must not be mistaken for Plot completion:

```text
PLOT_CANDIDATE_EXISTS: true
FIRE_TARGET_PLOT_BLOOM: NOT_STARTED / IN_PROGRESS
PLOT_BLOCK_COMPLETE: false
```

When restoring into this state:

```text
DO NOT regenerate the Plot candidate
→ resume Target Fire Bloom against the existing candidate
→ revise same candidate when useful
→ show final candidate
→ wait for author approval
```

Only explicit author approval may create:

```text
PLOT_BLOCK_COMPLETE: true
```

---

# Story Room interaction truth

Normal Story Room is a conversation, not a wizard.

```text
AUTHOR STILL THINKING
→ follow author
→ illuminate / locally continue when useful

AUTHOR FUZZY
→ clarify existing idea
→ expose at most one important implication

AUTHOR STUCK / ASKS FOR HELP
→ expand naturally
→ no mandatory option list
```

Forbidden default interaction:

```text
AI gives A/B/C
→ author chooses
→ next A/B/C
```

Also forbidden:

```text
mandatory 3..5 options
mandatory case board
mandatory case selection gate
```

---

# Search route

Formal creative replies that add / recommend / judge concrete creative content remain search-backed.

```text
FORMAL_CREATIVE_REPLY_SEARCH_REQUIRED: true
PREFERRED_SEARCH_PLUGIN: Firecrawl
```

Pure acknowledgement, verbatim restatement, format-only transformation, or repo/file status reports with no external creative judgment may skip search.

Important distinction:

```text
GENERAL SEARCH CALIBRATION
!= TARGET PLOT FIRE BLOOM GATE
!= DEEP FICTION CASE RESEARCH
```

Ordinary search calibration may happen while S2 is reasoning, but it does not satisfy the mandatory `目标剧情 Fire 开花` unless the Fire Gate conditions are actually met against the existing Target Plot candidate.

```text
SOURCE_RESEARCH_CANNOT_SATISFY_TARGET_BLOOM: true
GENERIC_SEARCH_CANNOT_SATISFY_TARGET_BLOOM: true
```

Deep fiction research remains on-demand.

---

# Target Character Block boundary

Target Character Block only begins after author approval of the final Plot Block candidate.

```text
FINAL PLOT CANDIDATE
→ AUTHOR APPROVAL
→ TARGET CHARACTER BLOCK
```

Target Character work may calibrate reactions and revise local delivery, but may not redesign approved Plot, change stage endpoint, or add new Plot branches.

```text
APPROVED_PLOT > CHARACTER_REHEARSAL
CHARACTER_REDOES_PLOT: forbidden
```

---

# Critical invariants

```text
AUTHOR IDEA FIRST
NO A/B/C AUTHOR-CHOICE WORKFLOW
FOLLOW AUTHOR WHILE AUTHOR IS THINKING
FORMAL CREATIVE REPLY MUST BE SEARCH-BACKED
DEEP FICTION RESEARCH ON DEMAND

S2 SOURCE BREAKDOWN HAS TWO DEFAULT CORE BLOCKS ONLY
BLOCK 1 = HUMAN RETELLING CORE
BLOCK 2 = CHARACTER TRACE
SOURCE TWO-BLOCK BREAKDOWN MUST COMPLETE BEFORE SOURCE-TO-TARGET
SOURCE CHARACTER TRACE MAY NOT BE DEFERRED UNTIL AFTER TARGET PLOT
SOURCE AUTHOR-FACING LABELS = 母本剧情复述 + 母本人物追踪
TARGET AUTHOR-FACING LABELS = 剧情块 + 人物块
SOURCE CHARACTER TRACE != TARGET CHARACTER BLOCK
SOURCE CHARACTER TRACE OUTPUT = EXACT 状态 / 动作或话 / 结果 TEMPLATE
HUMAN RETELLING AUTHOR-FACING OUTPUT = LONG CONTINUOUS NATURAL PROSE FIRST
BACKSTAGE ANALYSIS MUST NOT REPLACE AUTHOR-FACING RETELLING

SOURCE BRIDGE FUNCTION FIRST
EVERY NEW TARGET EVENT MUST HAVE SOURCE FUNCTION + CAUSAL BRIDGE
SOURCE FRAMEWORK FIDELITY REQUIRED WHEN ACTIVE

TARGET PLOT CANDIDATE FIRST
→ TARGET FIRE BLOOM
→ OPTIONAL REVISION
→ AUTHOR APPROVAL
→ TARGET CHARACTER

TARGET FIRE BLOOM WITHOUT PLOT CANDIDATE: FORBIDDEN
PLOT APPROVAL BEFORE REQUIRED TARGET FIRE BLOOM: FORBIDDEN
FIRE SEARCH HIT IS NOT CANON
FIRE MAY NOT REWRITE SOURCE SKELETON

CAPACITY REPAIR BY SIDE QUEST IS FORBIDDEN
BRIDGE INFLATION IS FORBIDDEN
NO PROSE IN S2
```

## Memory line

> **S2 先把母本两块拆完，再用母本骨架构思我们自己的【剧情块】初版候选。剧情候选已经存在以后，才运行【目标剧情 Fire 开花】；把有用的刺激吸收回来，必要时修订，再把最终剧情块候选给作者审核。作者批准剧情块之后，才进入我们自己的【人物块】。**
