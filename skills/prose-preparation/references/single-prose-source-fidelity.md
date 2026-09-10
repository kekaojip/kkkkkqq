# Single Prose Source Fidelity v3.0｜S3 单母本正文与同位置保真

> status: production-main
> owner: `source-shadow-runtime.md`
> production_route: `../routes/s3-source-shadow.md`
> authority: SOURCE IDENTITY / POSITION / TEXT FIDELITY ONLY

## 0. First principle

S3 先确认：

> 当前拿来做 Source Shadow 的正文，确实来自作者锁定 donor 的当前映射位置，而且文字可可靠读取。

本协议没有剧情权、人物权或生成权。

## 1. Primary source

默认：

```text
TARGET CHAPTER N
+ STAGE2 LOCKED STORY DONOR
+ STAGE2 mapped source position
→ PRIMARY PROSE SOURCE
```

如果 S2 已锁子区间：严格使用 mapped donor subrange。

```text
SAME_POSITION
= author-locked mapped story position
!= always same numeric chapter index
```

PRIMARY 不能被另一本 donor 或外部“更像”的作品替换。

## 2. Text fidelity gate

取得正文时记录：

```text
SOURCE_TEXT_ACCESS_METHOD
SOURCE_TEXT_CORRUPTION_DETECTED
PUA_OR_CUSTOM_FONT_OBFUSCATION
SOURCE_TEXT_DECODE_AVAILABLE
SOURCE_TEXT_DECODE_METHOD
SOURCE_TEXT_DECODE_CONFIDENCE
SOURCE_TEXT_TRANSPORT_RECOVERY_USED
SOURCE_TEXT_FIDELITY_STATUS
```

乱码、截断、字体混淆未可靠恢复：

```text
SOURCE_TEXT_FIDELITY_STATUS: FAIL
→ REPORT
→ STOP SOURCE SHADOW
```

不得猜字。

## 3. Same-body transport recovery

canonical donor / position 已确认，但当前 transport 不可读时，可使用公开可读的**同一章同一正文**做 transport recovery。

必须验证：

```text
PRIMARY_CHAPTER_IDENTITY_CONFIRMED
RECOVERY_CHAPTER_INDEX_MATCH
RECOVERY_MAPPED_SUBRANGE_MATCH when applicable
RECOVERY_CHAPTER_TITLE_MATCH when applicable
MAJOR_EVENT_ORDER_MATCH
MULTIPLE_ANCHOR_PASSAGES_MATCH
NO_EXTRA_CHAPTER_BODY_MIXED_IN
```

冲突：FAIL / STOP。

## 4. Source Shadow scope

当前正式最小模式：

```text
PRIMARY SOURCE BODY
→ local scene windows inside that body
```

这不算 multi-source fusion。

### 4.1 Cross-chapter alternates

当前仓库没有已 ready 的正式 donor corpus 时：

```text
CROSS_CHAPTER_ALTERNATE_READ: false
```

只有未来满足：

```text
same author-locked donor
+ LOCAL_CORPUS_READY: true
+ corpus integrity PASS
```

才允许 Source Shadow runtime 在同一本 donor 内读取少量 alternate windows。

它们只能补充局部表达参考，不得替换 PRIMARY mapped donor position 的来源定位。所有 Source 均没有 Target 剧情框架权或表面决定权，Target 只服从已批准上游。

## 5. Forbidden substitution

禁止：

```text
another novel as prose source
another author as prose source
plot breakdown as prose body
AI summary as prose body
unverified mirror mix
cross-donor style fusion
```

## 6. Required receipt

```text
TARGET_CHAPTER_INDEX
STAGE2_STORY_DONOR
PROSE_SOURCE_POSITION
AUTHOR_LOCKED_CHAPTER_BOUNDARY_MAP when present
PRIMARY_SOURCE_SCOPE
SOURCE_TEXT_FIDELITY_STATUS
SOURCE_TEXT_DECODE_METHOD when applicable
SOURCE_TEXT_DECODE_CONFIDENCE
SOURCE_TEXT_TRANSPORT_RECOVERY_USED
CROSS_CHAPTER_ALTERNATE_READ
```

## 7. Hard failures

```text
PROSE_SOURCE_POSITION_MISMATCH
AUTHOR_LOCKED_CHAPTER_MAP_IGNORED
SOURCE_TEXT_FIDELITY_FAIL
RECOVERY_CHAPTER_IDENTITY_MISMATCH
CROSS_DONOR_STYLE_FUSION
UNREADY_CORPUS_USED_FOR_ALTERNATES
SUMMARY_USED_AS_SOURCE_PROSE
```

任一失败：报告、修复取得层、仍失败则停止 S3。

## Memory line

> **先拿对作者锁定母本的当前映射正文，再做 Source Shadow。没有可靠原文就不假装“学到了文风”。**
