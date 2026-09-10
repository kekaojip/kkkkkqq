#!/usr/bin/env python3
"""Lightweight diagnostics for over-uniform Chinese fiction prose.

This script does not score whether text is "human" and does not rewrite text.
It surfaces rhythm/uniformity signals for Human Grain Pass.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

SENTENCE_SPLIT = re.compile(r"(?<=[。！？!?])")
PUNCT_OR_SPACE = re.compile(r"[\s，。！？!?；;：:、,.…—\-\"“”‘’（）()【】\[\]<>《》]+")
CLOSURE_HINTS = (
    "这才", "所以", "也就是说", "这意味着", "说白了", "说到底", "总之",
    "现在看来", "至少", "归根结底", "最终", "这就是", "他忽然意识到",
)


def visible_len(text: str) -> int:
    return len(PUNCT_OR_SPACE.sub("", text))


def coefficient_of_variation(values: list[int]) -> float | None:
    if len(values) < 2:
        return None
    mean = statistics.mean(values)
    if mean == 0:
        return None
    return statistics.pstdev(values) / mean


def max_run(flags: list[bool]) -> int:
    best = cur = 0
    for flag in flags:
        if flag:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def analyze(text: str) -> dict:
    raw_paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    paragraphs = [p for p in raw_paragraphs if not p.startswith("#")]

    sentences: list[str] = []
    paragraph_sentence_counts: list[int] = []
    paragraph_lengths: list[int] = []
    single_sentence_flags: list[bool] = []

    for p in paragraphs:
        ss = [s.strip() for s in SENTENCE_SPLIT.split(p) if s.strip()]
        if not ss:
            ss = [p]
        sentences.extend(ss)
        paragraph_sentence_counts.append(len(ss))
        paragraph_lengths.append(visible_len(p))
        single_sentence_flags.append(len(ss) == 1)

    sentence_lengths = [visible_len(s) for s in sentences if visible_len(s) > 0]
    short_flags = [n <= 8 for n in sentence_lengths]
    closure_hits = sum(1 for s in sentences if any(h in s for h in CLOSURE_HINTS))

    sentence_cov = coefficient_of_variation(sentence_lengths)
    paragraph_cov = coefficient_of_variation(paragraph_lengths)
    paragraph_sentence_cov = coefficient_of_variation(paragraph_sentence_counts)

    metrics = {
        "paragraph_count": len(paragraphs),
        "sentence_count": len(sentence_lengths),
        "mean_sentence_chars": round(statistics.mean(sentence_lengths), 2) if sentence_lengths else 0,
        "sentence_length_cov": round(sentence_cov, 3) if sentence_cov is not None else None,
        "short_sentence_ratio": round(sum(short_flags) / len(short_flags), 3) if short_flags else 0,
        "max_consecutive_short_sentences": max_run(short_flags),
        "single_sentence_paragraph_ratio": round(sum(single_sentence_flags) / len(single_sentence_flags), 3) if single_sentence_flags else 0,
        "max_consecutive_single_sentence_paragraphs": max_run(single_sentence_flags),
        "paragraph_length_cov": round(paragraph_cov, 3) if paragraph_cov is not None else None,
        "paragraph_sentence_count_cov": round(paragraph_sentence_cov, 3) if paragraph_sentence_cov is not None else None,
        "closure_hint_count": closure_hits,
        "closure_hint_ratio": round(closure_hits / len(sentence_lengths), 3) if sentence_lengths else 0,
    }

    flags: list[str] = []
    if sentence_cov is not None and sentence_cov < 0.35 and len(sentence_lengths) >= 20:
        flags.append("sentence_lengths_are_low_variance")
    if paragraph_cov is not None and paragraph_cov < 0.45 and len(paragraphs) >= 12:
        flags.append("paragraph_lengths_are_low_variance")
    if metrics["max_consecutive_short_sentences"] >= 5:
        flags.append("long_short_sentence_stack")
    if metrics["max_consecutive_single_sentence_paragraphs"] >= 6:
        flags.append("long_single_sentence_paragraph_stack")
    if metrics["closure_hint_ratio"] >= 0.08 and len(sentence_lengths) >= 30:
        flags.append("many_explicit_closure_hints")

    return {
        "metrics": metrics,
        "diagnostic_flags": flags,
        "note": "Heuristics only. Do not optimize prose to these numbers.",
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Diagnose over-uniform rhythm in fiction prose.")
    ap.add_argument("file", help="UTF-8 prose file")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    args = ap.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    result = analyze(text)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print("Human Grain diagnostic")
    for key, value in result["metrics"].items():
        print(f"{key}: {value}")
    if result["diagnostic_flags"]:
        print("flags:")
        for flag in result["diagnostic_flags"]:
            print(f"- {flag}")
    else:
        print("flags: none")
    print(result["note"])


if __name__ == "__main__":
    main()
