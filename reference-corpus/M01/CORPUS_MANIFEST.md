# CORPUS MANIFEST｜M01

```text
CORPUS_ID: M01
CANONICAL_TITLE: 说好一年一词条，万词王什么鬼
TITLE_ALIAS_1: 一年抽取一词条，模拟的也可以？
AUTHOR: 六大六子
SOURCE_TYPE: author-provided TXT / persistent ChatGPT Library
LIBRARY_FILE_ID: file_00000000ec2481f5932bddab8d6288cb
SOURCE_HASH_SHA256: d490f1e72ad0fffe8408d0b85aedf404c2f263c900da11d4996a4919afd3d4c1
DETECTED_CHAPTER_COUNT: 607
CHAPTER_RANGE: 1-607
KNOWN_SOURCE_ANOMALIES: none detected in chapter numbering 1-607
LOCAL_GITHUB_RAW_CORPUS_READY: false
VERIFIED_ANCHOR_CACHE_READY: true
ANCHOR_INDEX_PATH: reference-corpus/M01/ANCHOR_INDEX.tsv
FIXED_ANCHOR_CACHE: reference-corpus/M01/anchors/CH001.txt
CURRENT_POSITION_ANCHOR_CACHE: reference-corpus/M01/anchors/CH006.txt
```

## Identity alias

`《一年抽取一词条，模拟的也可以？》` 与 `《说好一年一词条，万词王什么鬼》` 是同一本书的前后书名，统一解析为 `CORPUS_ID: M01`。任何运行时命中任一名称，都不得创建第二份母本身份。

## Authority

当前 canonical raw authority 仍是作者提供的完整 TXT，Library 文件 ID 如上，source hash 绑定为：

`d490f1e72ad0fffe8408d0b85aedf404c2f263c900da11d4996a4919afd3d4c1`

仓库内 `anchors/*.txt` 不是第二份正文权威，只是从该 raw source 按章节边界截取的 verified anchor cache，供 Mother Mirror 在固定 Anchor / 当前 Position Anchor 诊断时稳定读取。

## Verified anchor cache

- `CH001.txt`：M01 Chapter 1，Mother Mirror 固定阅读镜；
- `CH006.txt`：M01 Chapter 6，当前第006章 Position Anchor；
- 每个 cache 的 raw line range 与实际 Git blob SHA 记录在 `ANCHOR_INDEX.tsv`；
- cache 必须能回溯到同一个 canonical raw source 的章节边界；
- raw source hash 变化时，anchor cache 必须重新验证或重建；
- 未缓存的 donor chapter 仍走 `source-corpus-acquisition.md` 的正常 Source Acquisition，不得用摘要或模型记忆代替。

## Future full GitHub corpus

若以后把完整 raw source + transport shards 全部迁入 GitHub，可将：

`LOCAL_GITHUB_RAW_CORPUS_READY: true`

并补全 `CHAPTER_INDEX.tsv / TRANSPORT_INDEX.tsv / TRANSPORT_SHARDS.tsv`。在此之前，不得伪称完整 GitHub corpus 已落地。