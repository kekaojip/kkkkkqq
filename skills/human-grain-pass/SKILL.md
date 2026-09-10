---
name: human-grain-pass
description: Post-process completed fiction prose to restore natural human grain when the draft feels too polished, too symmetrical, too efficient, or mechanically "AI-clean". Use after a full prose draft exists and before author adoption/canonization, especially for web-fiction that should stay simple, direct, readable, conversational, and slightly irregular without changing plot facts, character truth, event order, POV, world rules, or outcomes.
---

# Human Grain Pass v1.1｜真人毛边正文层

## Mission

Take a completed fiction draft that is already correct and readable, then remove **over-polish** without making it sloppy.

Human grain is not random variation. It is **uneven narrative attention**:

```text
sometimes careful
sometimes plain
sometimes repetitive for a reason
sometimes directly explanatory
sometimes allowed to drift for one small thought
sometimes ending without a thesis
```

The target is:

```text
clear story
+ low reading effort
+ uneven human cadence
+ audible narrator presence when natural
+ semantic reappearance / explanation drift when natural
+ ordinary non-maximal wording
- mechanical neatness
- constant performance of "good writing"
```

This is a **post-prose surface pass**. It has no story authority.

## Authority contract

Never change:

```text
PLOT FACTS
EVENT ORDER
CHARACTER MOTIVE / KNOWLEDGE
RELATIONSHIP STATE
POV AUTHORITY
WORLD RULES
POWER / SYSTEM RULES
OUTCOME
CHAPTER END STATE
```

Hard locks:

```text
STORY_AUTHORITY: NONE
CHARACTER_AUTHORITY: NONE
CANON_AUTHORITY: NONE
WORLD_AUTHORITY: NONE
NEW_EVENT: FORBIDDEN
NEW_FACT: FORBIDDEN
NEW_RELATIONSHIP: FORBIDDEN
NEW_POWER: FORBIDDEN
DELIBERATE_TYPO: FORBIDDEN
DELIBERATE_GRAMMAR_ERROR: FORBIDDEN
```

If a desired grain edit requires inventing a fact, skip it.

## Required input

Use only after a complete prose draft exists.

Minimum input:

```text
FULL PROSE DRAFT
+ enough approved story/character truth to detect drift
```

When available, also read the safe continuity / approved plot and character blocks. Do not reopen their decisions.

## Three-layer grain model

Human Grain v1.1 diagnoses and edits three different layers. They are not interchangeable.

### Layer A — Structural Grain

Surface rhythm and page shape:

```text
sentence cadence
paragraph shape
single-line paragraph density
designed short-sentence stacks
dialogue / narration breath
```

### Layer B — Narrator Grain

Whether the prose feels like someone is actually telling the story:

```text
plain narrator judgment
narrator distance moving slightly closer / farther inside the same POV authority
occasional direct naming of an already-evidenced emotion or situation
ordinary connectors and non-performative phrasing
small scene-grounded detours
```

Narrator Grain may move narrative distance. It may **not** create omniscience or reveal knowledge the POV does not own.

### Layer C — Semantic Grain

Whether meaning is distributed too efficiently and evenly:

```text
important facts allowed to resurface in a new local context
explanation length allowed to drift
not every sentence required to perform a unique function
not every paragraph required to land a thesis / punchline
ordinary meaning overlap allowed
non-maximal wording allowed
```

## Workflow

### 1. Freeze truth first

Before changing wording, identify the non-negotiable event chain, POV, character information boundaries, system outputs, and chapter ending.

If these cannot be identified reliably:

```text
HUMAN_GRAIN_PASS: BLOCKED
→ report missing truth anchor
→ STOP
```

### 2. Diagnose over-polish across all three layers

Run `scripts/grain_scan.py` when a local text file is available. Treat its metrics as diagnostics, never as targets.

Then read the entire draft and diagnose by effect, not by quota.

#### Structural symptoms

```text
SENTENCE_RHYTHM_TOO_DESIGNED
PARAGRAPH_SHAPE_TOO_UNIFORM
SINGLE_LINE_PARAGRAPH_RUN_TOO_LONG
SHORT_SENTENCE_STACK_TOO_DESIGNED
```

#### Narrator symptoms

```text
NARRATOR_TOO_INVISIBLE
NARRATIVE_DISTANCE_TOO_STATIC
EVERY_JUDGMENT_FORCED_THROUGH_DRAMATIZATION
ORDINARY_CONNECTIVE_LANGUAGE_TOO_RARE
SCENE_ATTENTION_TOO_PLOT_EFFICIENT
```

#### Semantic symptoms

```text
SEMANTIC_EFFICIENCY_TOO_HIGH
IMPORTANT_FACTS_USED_ONCE_THEN_SUPPRESSED
EXPLANATION_SYMMETRY_TOO_HIGH
PUNCHLINE_DENSITY_TOO_HIGH
MEANING_SUMMARY_CLOSURE_TOO_DENSE
BEST_WORDING_PRESSURE_TOO_HIGH
EVERY_SENTENCE_HAS_UNIQUE_JOB
```

A clean sentence is not automatically a defect. Edit only patterns that accumulate enough to affect reading texture.

### 3. Require layer-complete treatment

Load `references/grain-patterns.md`.

Use only the edits the text supports, but do not confuse a safe structural edit with completion of the whole pass.

Hard rule:

```text
STRUCTURAL_GRAIN_ONLY
!= HUMAN_GRAIN_COMPLETE
```

If Narrator or Semantic symptoms were diagnosed, at least some corresponding symptoms must be actually resolved before PASS.

This does **not** mean every chapter must use every grain family.

```text
DIAGNOSED_LAYER → ADDRESS OR EXPLICITLY PRESERVE WITH REASON
UNDIAGNOSED_LAYER → NO FORCED EDIT
```

### 4. Prefer de-polishing over decorative rewriting

The pass should often remove signs of crafted performance rather than add new flourishes.

Examples:

```text
remove / flatten an unnecessary quotable closer
let an ordinary sentence remain ordinary
allow a fact to reappear instead of inventing a new metaphor
let a paragraph simply move to the next action
use a slightly less distilled sentence when first-pass meaning stays clear
```

Do not replace one polished line with a different polished line.

```text
DE-PERFORM > RE-PERFORM
```

### 5. Protect first-pass readability

After each local change, ask:

```text
Can a casual reader still tell immediately:
who is here?
what just happened?
what the character wants now?
why the next action follows?
```

If clarity drops, roll that edit back.

The pass may make prose less elegant. It may not make prose harder to understand.

### 6. Prevent polish rebound

Do not finish by globally smoothing the new draft.

Forbidden repair pattern:

```text
add grain
→ run full elegance / concision rewrite
→ remove the grain again
```

Only repair concrete errors created by this pass.

```text
ERROR REPAIR: SURGICAL
FULL RESMOOTH: FORBIDDEN
```

### 7. Recheck hard truth

Before output, require:

```text
TARGET_STORY_TRUTH: PASS
CHARACTER_CONTINUITY: PASS
EMOTIONAL_CONTINUITY: PASS when relevant
POV_CONTINUITY: PASS
NEW_FACT_INTRODUCTION: 0
SOURCE_FACT_LEAK: 0 when donor prose is in the workflow
GRAMMAR_CLARITY_FLOOR: PASS
READER_FIRST_PASS_CLARITY: PASS
DELIBERATE_ERROR_INJECTION: 0
```

Also recheck the grain itself:

```text
STRUCTURAL_GRAIN_DIAGNOSIS: ADDRESSED | NOT_PRESENT
NARRATOR_GRAIN_DIAGNOSIS: ADDRESSED | NOT_PRESENT
SEMANTIC_GRAIN_DIAGNOSIS: ADDRESSED | NOT_PRESENT
POLISH_REBOUND: false
```

If a grain edit fails one of the truth gates, revert that edit instead of rewriting the story around it.

## Governing principles

### First-pass clear is enough

```text
BEST WORDING: NOT REQUIRED
FIRST_PASS_CLEAR WORDING: ENOUGH
```

Not every sentence should look selected from ten alternatives.

### Reader inference does not silence the narrator

```text
READER_CAN_INFER
!= NARRATOR_MUST_NEVER_SAY_IT
```

A narrator may occasionally say the obvious when it sounds like a person telling the story. Do not explain every beat.

### Important facts may come back

```text
IMPORTANT_FACT_RELEVANT_AGAIN
→ ALLOW IT TO RESURFACE
```

Do not auto-suppress a fact merely because the reader already knows it. Reappearance must have a new local pressure or meaning.

### Explanation is not a fairness system

```text
EXPLANATION_SYMMETRY: UNDESIRED
```

Some things get one plain sentence. Some get several because the narrator or POV actually cares. Required causal information must still remain clear.

### Not every paragraph earns a landing

```text
LOCAL_CLOSURE_NOT_ALWAYS_REQUIRED
```

A paragraph may simply finish the action and move on. Repeated thesis, punchline, meaning-summary, or quotable closers are a polish smell.

### Attention need not be plot-efficient

A tiny scene-grounded observation or calculation may exist even when it does not build a new plot function. It may not invent new facts, backstory, lore, or foreshadowing.

## What this pass should create

Prefer believable changes such as:

```text
one plain sentence that simply says the obvious
one important fact naturally resurfacing in a new context
a paragraph allowed to run longer because the thought has not finished
a paragraph that ends on an action instead of a polished thesis
a brief narrator judgment in the book's ordinary register
a small scene-grounded calculation / complaint / observation
a slightly longer ordinary sentence instead of the most distilled sentence
a repeated pronoun or plain connector when natural
a concept explained in one line while another is allowed more space
```

It may also **remove** artificial polish, especially:

```text
repeated aphoristic closers
forced punchlines
patterned short-sentence stacks
symmetrical explanation blocks
constant mini-summaries
unnecessary distilled "quote lines"
```

## What not to imitate

Natural grain is not low quality.

Never introduce:

```text
wrong characters
wrong punctuation on purpose
misspellings
broken grammar
factual contradiction
random filler
fake slang unrelated to the character
meaningless sentence-length randomization
forced self-correction
forced tangent
forced repetition
manufactured POV wobble
```

Do not optimize for AI-detector evasion. Public anti-overpolish/humanizer references are only evidence that mechanical uniformity and excessive editing exist; this skill optimizes for fiction reading quality, not detector scores.

## Output behavior

Default output is the **full revised prose**, not a critique report.

Internally retain a minimal receipt:

```text
HUMAN_GRAIN_PASS: PASS | BLOCKED
GRAIN_LAYERS_DIAGNOSED: [STRUCTURAL, NARRATOR, SEMANTIC]
GRAIN_LAYERS_ADDRESSED: [...]
GRAIN_PATTERNS_USED: [...]
TRUTH_RECHECK: PASS | FAIL
NEW_FACT_INTRODUCTION: 0
DELIBERATE_ERROR_INJECTION: 0
```

If explicitly asked for comparison, provide before/after excerpts plus reasons, but do not turn normal production output into a technical report.

## Position in a writing chain

This skill is designed for:

```text
FULL PROSE DRAFT
→ HUMAN GRAIN PASS
→ AUTHOR REVIEW
→ ADOPTION / CANON
```

It is not a replacement for plot design, character design, prose generation, or tracking.

## Memory line

> 毛边不是把句子随机弄乱，而是恢复不均匀的叙述注意力。结构要有纹理，旁白要偶尔像人在说话，意义也不能像数据库一样只写一次、解释得一样多、段段都落锤。清楚优先，真值不动，没必要每句话都写到最优雅。