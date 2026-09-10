# S3 Direct Edit Compatibility Route v4.0｜已并入 Source Shadow

> status: COMPATIBILITY ONLY
> production_route: `s3-source-shadow.md`
> direct_edit_primitive: `../references/direct-source-slot-fill.md`
> no_longer_sole_route: true

## 0. Status

历史 Golden Direct Edit 已被 Source Shadow 吸收。

过去：

```text
one same-position source chapter
→ sentence ordinal map
→ one-to-one direct fill
→ target prose
```

现在：

```text
one same-position verified source chapter
→ homolog continuous scene windows
→ copy-weighted transduction
→ target prose
```

Direct Edit 仍保留，但只作为**局部高度同构**时的最强执行原语。

## 1. When this primitive is used

如果某个 Target 局部与 Source window 在叙事功能、信息顺序和动作/对白结构上高度同构：

```text
SOURCE SENTENCE / PARAGRAPH
→ direct content-slot replacement
→ delete source-only material
→ minimum target-only insert
→ minimal grammar repair
```

此时优先 Direct Edit，不需要模型重新改写整段。

## 2. What changed

不再强制：

```text
whole chapter sentence ordinal map
whole chapter one-to-one fill map
source map author approval
fill map author approval
WHOLE_SENTENCE_FREE_REWRITE_COUNT = 0 for every sentence
```

这些会让剧情映射不完全同构时变得过脆。

改为：

```text
natural target window
→ best homolog source window
→ direct edit where homologous
→ minimum source-frame-guided reconstruction where not homologous
```

## 3. What remains hard

仍然必须：

```text
TARGET STORY TRUTH
SOURCE FACT LEAK = 0
SOURCE PROPER NOUN LEAK = 0
FORBIDDEN REVEAL = 0
ENDPOINT MATCH
NO UNNECESSARY EXPLANATORY FILLER
```

高 Source wording overlap 本身不再是失败。

## 4. Author-visible behavior

Source window map / edit receipts 均为 S3 内部动作。

作者只看：

```text
FULL PROSE CANDIDATE
```

服从 `../../references/author-visible-step-gate.md`。

## 5. Canonical route

所有新生产任务必须从：

`skills/prose-preparation/SKILL.md`

进入：

`skills/prose-preparation/routes/s3-source-shadow.md`

本文件不得作为独立 S3 route 恢复。

## Memory line

> **Golden Direct Edit 没被丢掉，它变成 Source Shadow 的高同构档：能原句换槽就直接换，不同构时才放宽到连续 scene-window 转写。**
