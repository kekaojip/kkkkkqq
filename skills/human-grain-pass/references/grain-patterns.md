# Human Grain Patterns v1.1｜三层真人毛边参考

Use this reference only while applying Human Grain Pass to completed fiction prose.

The pass has three layers:

```text
STRUCTURAL GRAIN
NARRATOR GRAIN
SEMANTIC GRAIN
```

The old eight pattern families still matter, but they now belong to one of these three layers instead of being treated as interchangeable local tricks.

---

# Layer A — Structural Grain｜结构毛边

## A1. Sentence Grain｜句子纹理

### Symptom

Several consecutive sentences share similar length, syntactic shape, or punchline timing. The prose feels metronomic even when each sentence is good.

### Legal moves

- Let one thought stay in a longer ordinary sentence when splitting it would look staged.
- Let another sentence be blunt and short because the thought genuinely ends there.
- Merge two tiny designed sentences when they are really one thought.
- Break a long explanatory sentence only where a person would naturally pause.

### Avoid

- Fixed short/long quotas.
- Random sentence surgery done only to raise variance.

## A2. Paragraph Grain｜段落纹理

### Symptom

Too many one-sentence paragraphs, identical paragraph sizes, or every mobile-screen beat looks deliberately cut.

### Legal moves

- Keep two or three naturally continuous sentences together.
- Preserve a one-line paragraph only when it genuinely lands or turns attention.
- Allow a mundane transitional paragraph to be slightly longer than a designed web-fiction paragraph.
- Preserve rapid dialogue stacks when the characters themselves create the rhythm.

### Avoid

- Making long blocks that hurt mobile readability.
- Alternating paragraph sizes mechanically.
- Flattening naturally fast dialogue just because a scanner flags short paragraphs.

## A3. Designed Beat Smell｜设计节拍味

### Symptom

The page repeatedly performs this pattern:

```text
setup
→ short sentence
→ quotable closer
→ blank line
→ repeat
```

### Legal moves

- Remove one unnecessary landing and let the paragraph roll into the next action.
- Join a setup and its obvious consequence when the split exists only for dramatic shape.

---

# Layer B — Narrator Grain｜叙述者毛边

## B1. Plain Narrator Intrusion｜旁白顺嘴一句

### Symptom

The narrator is so optimized that every judgment must be dramatized through action or inferred by the reader.

### Legal moves

Occasionally allow plain, low-literary directness in the book's own register:

```text
说白了，就是没钱。
这账其实不难算。
修仙归修仙，饭还是得吃。
```

The sentence should sound like someone telling the story, not an essay explaining the story.

### Rule

```text
READER_CAN_INFER
!= NARRATOR_MUST_NEVER_SAY_IT
```

### Avoid

- Explaining every beat.
- Moralizing.
- Repeating the same conclusion immediately after it has already been said in the same way.

## B2. Narrator Distance Grain｜叙述距离毛边

### Symptom

Narrative distance stays perfectly fixed. The prose is always the same amount inside the POV character's head.

### Legal moves

Inside the same POV authority, allow a small distance shift:

```text
close to character perception
→ step back for one plain judgment
→ return to character perception
```

The narrator may state an already-supported situation more directly than the character consciously phrases it.

### Hard boundary

```text
NARRATIVE_DISTANCE_SHIFT: ALLOWED
POV_AUTHORITY_SHIFT: FORBIDDEN
NEW_KNOWLEDGE: FORBIDDEN
OMNISCIENCE: FORBIDDEN
```

## B3. Direct Emotion Naming｜偶尔直接点情绪

### Symptom

Every emotional state is forced to remain implicit even after scene evidence already makes it obvious.

### Legal moves

Occasionally use a plain emotion label or situation judgment after sufficient evidence, especially in simple web fiction.

The purpose is not to replace dramatization. It is to let the narrator occasionally say what a human storyteller would simply say.

### Avoid

- Action + emotion label + explanation + summary all stacked together.
- Naming emotions not supported by approved character truth.

## B4. Human Detour｜短暂人类偏题

### Symptom

Every sentence is plot-efficient. Characters appear to notice only information useful to the outline.

### Legal moves

Permit a tiny observation, complaint, comparison, or calculation that already belongs to the present scene and approved POV.

It must end quickly.

### Rule

```text
REACTION_NEED_NOT_BE_PLOT_EFFICIENT
SHORT_SCENE_GROUNDED_DETOUR: ALLOWED
```

### Avoid

- New backstory.
- New worldbuilding.
- New foreshadowing.
- Inventing a physical object or scene fact just to create texture.
- Detours inserted by quota.

---

# Layer C — Semantic Grain｜语义毛边

## C1. Mild Information Echo｜轻微信息回声

### Symptom

The prose treats every stated fact as "used once, never repeat", which is efficient but unlike human narration.

### Legal moves

Let an important fact reappear when the new scene gives it a new local meaning.

Example:

```text
earlier: he was removed from the outer sect
later: while choosing a partner, the same fact matters because he has little basis to be picky
```

### Rules

```text
FACT REAPPEARANCE IN NEW CONTEXT
!= REDUNDANT EXPLANATION

IMPORTANT_FACT_RELEVANT_AGAIN
→ ALLOW IT TO RESURFACE
```

Do not auto-suppress a fact merely because the reader already knows it.

### Avoid

- Immediate recap after an action already proved the same conclusion.
- Paragraph-level summaries with no new local pressure.

## C2. Semantic Over-Efficiency｜语义效率过高

### Symptom

Every sentence performs one unique job, every fact appears once, every idea is compressed to its minimum form, and nothing overlaps.

The result feels like a clean database export rather than narration.

### Legal moves

- Allow a sentence to partly overlap with the previous meaning when the overlap sounds natural.
- Let one practical thought contain both reaction and explanation instead of splitting them into optimized units.
- Keep a small amount of ordinary redundancy when it carries voice or feeling.

### Avoid

- Repeating paragraphs.
- Restating every conclusion.
- Padding word count.

## C3. Uneven Explanation｜解释力度不平均

### Symptom

Every concept receives the same tidy amount of explanation, creating synthetic fairness.

### Legal moves

- Explain an obvious thing in one plain sentence and move on.
- Linger slightly longer on a detail the narrator / POV actually cares about.
- Let one rule be introduced through consequence while another receives direct explanation.

### Rule

```text
EXPLANATION_SYMMETRY: UNDESIRED
```

### Avoid

- Hiding required causal information.
- Adding lore only to create unevenness.

## C4. Imperfect Closure｜不完美收口

### Symptom

Many paragraphs or micro-scenes end with a thesis, punchline, meaning statement, witty line, or quotable sentence.

### Legal moves

Sometimes end on:

- a small action
- a practical next step
- an ordinary line of dialogue
- an object already present in the scene
- the character simply moving on

Sometimes remove a clever closer entirely.

### Rule

```text
LOCAL_CLOSURE_NOT_ALWAYS_REQUIRED
```

### Avoid

- Removing a chapter hook that genuinely earns its landing.
- Replacing one punchline with a different punchline.

## C5. Punchline / Craft Density｜落锤与“好句”密度

### Symptom

The prose produces a stable stream of quotable mini-lines, witty observations, clean reversals, or perfectly distilled takeaways.

Each line may be good. The accumulation feels performed.

### Legal moves

- Flatten some nonessential quotable lines into ordinary narration.
- Keep the strongest few and let surrounding prose be plain.
- Prefer de-polishing to writing a new clever line.

### Rule

```text
TOO_MANY_GOOD_LINES
CAN_BE_A_TEXTURE_DEFECT
```

## C6. Non-Maximal Wording｜非最优表达

This expands the old Controlled Clumsiness pattern.

### Symptom

Every sentence appears to use the shortest, most elegant, most distilled wording available.

### Legal moves

Prefer believable ordinary syntax when first-pass meaning stays clear:

```text
too distilled: 他并不意外。
ordinary: 周玄倒也没觉得这有什么奇怪的。
```

A sentence may:

- repeat a pronoun
- repeat a common verb already used nearby
- use a plain connector
- take half a clause longer to arrive
- choose the obvious word instead of a more elegant synonym

### Rules

```text
BEST_WORDING: NOT_REQUIRED
FIRST_PASS_CLEAR_WORDING: ENOUGH
```

### Avoid

- Broken grammar.
- Confusing referents.
- Artificial dialect.
- Deliberate misspelling.
- Making every sentence deliberately clumsy.

## C7. Uneven Attention｜注意力不均匀

### Symptom

The prose spends attention exactly in proportion to plot importance. Nothing minor receives an extra sentence; nothing major is handled bluntly.

### Legal moves

Let narrative attention follow the teller's local interest rather than outline importance, provided no new facts are invented.

One small existing detail may receive two sentences because the POV notices it. Another plot-relevant fact may get one blunt sentence and move on.

This is one of the deepest forms of human grain.

---

# Cross-layer rules

## Structural-only repair is not enough

```text
STRUCTURAL_GRAIN_ONLY
!= HUMAN_GRAIN_COMPLETE
```

If Narrator or Semantic defects were diagnosed, they must be addressed or explicitly preserved for a reason.

## Do not distribute grain evenly

Natural irregularity clusters.

```text
GRAIN_DENSITY: CONTEXT_DRIVEN
GRAIN_QUOTA: FORBIDDEN
```

One page may need almost none; another may carry several kinds at once.

## Preserve useful roughness before adding new roughness

If the draft already contains a fragment, tangent, direct aside, ordinary connector, repeated word, uneven paragraph, or non-maximal sentence that reads well, do not polish it away first and recreate another elsewhere.

## De-perform before re-perform

When the problem is excessive craft density:

```text
REMOVE PERFORMANCE
> ADD NEW PERFORMANCE
```

Do not solve an over-polished sentence by writing a different stylish sentence.

## Reader comfort remains the floor

For simple web fiction:

```text
first-pass clarity
> human grain
> elegance
```

If a casual reader has to reread to know what happened, the grain edit failed.

## The target feeling

The narrator should not appear to be trying equally hard at every moment.

```text
sometimes neat
sometimes ordinary
sometimes slightly repetitive
sometimes direct
sometimes allowed to move on without landing
```

That uneven attention is the grain.