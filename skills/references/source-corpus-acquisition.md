# Source Corpus Acquisition v1.1｜母本语料取得与本地优先路由

> status: production-main
> scope: Stage 2 donor body acquisition + Stage 3 same-position prose body acquisition
> authority: source retrieval / integrity / transport / fallback routing only
> does_not_own: Story interpretation / target Canon / prose style selection / target-world research

## 1. First principle

正式母本取得步骤永远存在：

```text
SOURCE_ACQUISITION
```

但“执行取得步骤”不等于“每次必须重新联网爬正文”。

当仓库中已有作者提供、完整性已校验的私有母本语料：

```text
SOURCE_ACQUISITION_MODE: LOCAL_GITHUB_CORPUS
```

只有本地缺失、损坏、章节缺失、身份不匹配、transport 不可用或作者明确要求重新联网核验时，才进入：

```text
SOURCE_ACQUISITION_MODE: EXTERNAL_FETCH_FALLBACK
```

禁止把 Local Hit 记成 `SOURCE_ACQUISITION_SKIPPED`。

---

## 2. Canonical raw authority vs transport cache

大文件必须区分：

```text
CANONICAL RAW SOURCE
= 唯一正文版本 / provenance / integrity root

DERIVED TRANSPORT SHARDS
= 从同一 raw bytes 确定性派生的只读传输缓存
```

Transport shard：

```text
IS_SOURCE_AUTHORITY: false
IS_INDEPENDENT_PROSE_SOURCE: false
INCREASES_DONOR_COUNT: false
INCREASES_STYLE_SOURCE_COUNT: false
```

它只解决 GitHub Contents/API 对大文件的运行时读取限制。

允许结构：

```text
reference-corpus/{CORPUS_ID}/
  CORPUS_MANIFEST.md
  CHAPTER_INDEX.tsv                 # raw-source line map / audit map
  TRANSPORT_INDEX.tsv               # chapter → shard + shard-relative line range
  TRANSPORT_SHARDS.tsv              # derived shard hashes / sizes
  <canonical raw source>.txt
  transport/
    SHARD_0001_0040.txt
    ...
```

禁止把 transport shard 当作可独立编辑的正文权威。

如果 raw source 发生版本变化：

```text
raw hash changes
→ old transport cache invalid
→ deterministic rebuild required
→ new hashes / indexes required
```

---

## 3. Corpus registry

每个正式本地母本至少必须有：

```text
CORPUS_ID
TITLE
AUTHOR when known
SOURCE_TYPE
SOURCE_AUTHORITY_PATH
SOURCE_HASH
CHAPTER_INDEX_PATH
CHAPTER_RANGE
DETECTED_CHAPTER_COUNT
KNOWN_SOURCE_ANOMALIES
```

当 canonical raw source 大到当前运行接口不能可靠按行读取时，还必须有：

```text
TRANSPORT_INDEX_PATH
TRANSPORT_SHARD_MANIFEST_PATH
TRANSPORT_SHARD_PATHS
TRANSPORT_CACHE_SOURCE_HASH_BINDING
TRANSPORT_RUNTIME_READ_TEST
```

`LOCAL_CORPUS_READY: true` 必须同时意味着：

```text
RAW_SOURCE_STORAGE_INTEGRITY: PASS
AND
CHAPTER_INDEX_INTEGRITY: PASS
AND
RUNTIME_TRANSPORT_READY: PASS
```

仅仅“GitHub 里有大文件”不等于 Ready。

---

## 4. Local-first lookup

取得 Donor Chapter N 时：

```text
1. resolve CORPUS_ID from current donor record / PROJECT_STATE
2. read CORPUS_MANIFEST
3. require LOCAL_CORPUS_READY: true
4. resolve Chapter N through TRANSPORT_INDEX
5. fetch only the named small shard + exact shard-relative Chapter N range
6. verify first heading == requested Chapter N
7. verify end boundary does not consume Chapter N+1
8. return VERIFIED_SOURCE_BODY
```

正常 receipt：

```text
SOURCE_ACQUISITION_STEP: EXECUTED
SOURCE_ACQUISITION_MODE: LOCAL_GITHUB_CORPUS
CORPUS_ID: ...
REQUESTED_CHAPTER_OR_RANGE: ...
LOCAL_CORPUS_HIT: PASS
SOURCE_BODY_PATH: transport shard path
SOURCE_BODY_RANGE: exact shard-relative range
RAW_SOURCE_AUTHORITY_PATH: canonical raw file
SOURCE_INTEGRITY_STATUS: PASS
TRANSPORT_INTEGRITY_STATUS: PASS
EXTERNAL_FETCH_REQUIRED: false
```

不得因为整本已存在就默认整本注入上下文。

```text
WHOLE_CORPUS_DEFAULT_READ: FORBIDDEN
```

---

## 5. Dynamic multi-chapter windows

### Stage 2 Story Block Discovery

允许按 Story Block Owner 的动态窗口读取同一本 donor 多章。

实现方式：

```text
requested chapter range
→ TRANSPORT_INDEX
→ minimum necessary shard set
→ exact requested chapter ranges only
```

跨 shard 时可读取多个 shard，但仍不得把未请求章节默认注入正式分析。

### Stage 2 Formal S2-A

必须重新取得：

```text
Donor Chapter N only
```

即使 Story Block Discovery 先前已经读过 N，也必须执行新的 Source Acquisition receipt。

### Stage 3 S3 mapped-position reference

正式 prose evidence 仍严格是：

```text
same locked donor + S2 author-locked mapped chapter/subrange
```

本地 corpus 只改变“正文从哪里拿到”，不改变作者锁定 donor / mapped-position lock；同位置不等于与 Target 相同数字章号。Source Shadow 的同 donor 少量跨章补充窗口仅在 corpus ready 且完整性通过后按 `../prose-preparation/references/single-prose-source-fidelity.md` 执行，不替换 PRIMARY。Source 只提供真实参考，正文由完整 novel-prose-writer-zh 实现。

---

## 6. Transport integrity

Transport cache 必须绑定 canonical raw source 版本。

至少维护：

```text
RAW SOURCE HASH
TRANSPORT SHARD HASHES
CHAPTER → SHARD RANGE MAP
RAW LINE RANGE BACK-REFERENCE
```

构建器必须：

```text
read canonical raw bytes
verify expected raw hash
parse chapter headings
preserve known missing chapter numbers
create deterministic shards
create shard-relative transport index
refuse duplicate / unexpected missing / raw hash mismatch
```

运行时最少抽查：

```text
first shard readable
middle shard readable
last shard readable
requested Chapter N heading/boundary readable
```

如果 transport cache 存在但当前 connector 无法实际读取正文：

```text
CORPUS_STORAGE_READY_BUT_TRANSPORT_UNREADABLE: FAIL
LOCAL_CORPUS_READY: false
```

不得假 PASS。

---

## 7. External fallback

以下任一出现：

```text
LOCAL_CORPUS_READY != true
CORPUS_MANIFEST_MISSING
TRANSPORT_INDEX_MISSING
TRANSPORT_SHARD_MISSING
REQUESTED_CHAPTER_MISSING
CHAPTER_BOUNDARY_INVALID
SOURCE_HASH_MISMATCH
TRANSPORT_HASH_MISMATCH
CORPUS_ID_MISMATCH
CORPUS_TEXT_CORRUPTION
TRANSPORT_RUNTIME_READ_FAIL
```

则：

```text
LOCAL_CORPUS_HIT: FAIL
EXTERNAL_FETCH_REQUIRED: true
→ use currently approved external provider route
```

外部抓取成功后可用于当前步骤，但不得自动把抓到的正文升级成 corpus 权威版本，除非完成：

```text
identity check
chapter-index check
content-integrity check
manifest update
transport rebuild when required
```

外部 fallback 也失败：

```text
SOURCE_ACQUISITION_STATUS: BLOCKED
→ REPORT exact failure
→ STOP dependent stage
```

不得猜章、补章、自动改编号。

---

## 8. Source anomalies

作者提供语料中的：

```text
missing chapter number
duplicate chapter number
unexpected title
truncation
empty chapter
encoding anomaly
```

必须写入 Manifest。

例如出现：

```text
271 → 273
```

不得自行生成“第272章”、把273重编号成272，或默认为作者故意跳号。

正式请求缺失章时：

```text
REQUESTED_CHAPTER_MISSING
→ external fallback / author repair
```

---

## 9. Local corpus != research replacement

本地 donor corpus 只替代**重复抓取同一母本正文**。

它不替代：

```text
market research
fanfic canon verification
target-world ecology research
S2-B0 target realization search
workflow / architecture research
comparative-work discovery when explicitly required
```

因此：

```text
DONOR_BODY_ACQUISITION
!=
CREATIVE_RESEARCH_ASSIST
```

当当前 Stage 明确要求插件 / web research 时，Local Corpus Hit 不能用来豁免该研究 Gate。

---

## 10. Multiple books

可以注册多个 corpus：

```text
reference-corpus/{CORPUS_A}
reference-corpus/{CORPUS_B}
...
```

用于构思 / 比较 /研究时可按 Owner 规则组合证据。

但正式生产中：

```text
Stage 2 Story Donor count
Stage 3 Single Prose Champion count
```

仍服从各自 Owner，不因 corpus 数量增加自动变成多母本融合。

---

## 11. Required receipt

每次正式 donor body acquisition 至少记录：

```text
SOURCE_ACQUISITION_STEP
SOURCE_ACQUISITION_MODE
CORPUS_ID when local
REQUESTED_CHAPTER_OR_RANGE
LOCAL_CORPUS_HIT
RAW_SOURCE_AUTHORITY_PATH
SOURCE_BODY_PATH
SOURCE_BODY_RANGE / SHARD
SOURCE_INTEGRITY_STATUS
TRANSPORT_INTEGRITY_STATUS
EXTERNAL_FETCH_REQUIRED
EXTERNAL_FETCH_USED
```

---

## 12. Hard failures

```text
SOURCE_ACQUISITION_SILENT_SKIP
LOCAL_CORPUS_FALSE_READY
CORPUS_STORAGE_READY_BUT_TRANSPORT_UNREADABLE
WHOLE_CORPUS_DEFAULT_READ
REQUESTED_CHAPTER_MISSING_NOT_REPORTED
SOURCE_ANOMALY_SILENT_RENUMBER
SOURCE_HASH_MISMATCH_IGNORED
TRANSPORT_HASH_MISMATCH_IGNORED
TRANSPORT_USED_AS_INDEPENDENT_SOURCE_AUTHORITY
LOCAL_HIT_USED_TO_WAIVE_REQUIRED_CREATIVE_RESEARCH
MULTIPLE_CORPORA_USED_TO_BYPASS_SINGLE_DONOR_POLICY
```

任一失败：

```text
REPORT
→ repair acquisition layer
→ rerun
→ still fail: STOP
```

## Memory line

> **整本原文只存一份作为权威和完整性根；运行时从它确定性派生的小 shard 按章读取。取得步骤没有消失，Local Hit 只替代重复爬母本正文，不替代构思研究。**
