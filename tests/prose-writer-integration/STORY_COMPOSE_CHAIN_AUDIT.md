# Story Compose Chain Audit

> status: current after black-box integration
> production route authority: none; verification record only

## Current S3 route

```text
S2 approved truth
+ safe continuity
+ verified Source Shadow reference
→ Story Compose production preflight
→ complete `skills/story-compose/SKILL.md`
→ package-owned Phase 1 / Phase 2 / Phase 3
→ final composed prose
→ S3 hard truth / source leak / POV / endpoint revalidation only
→ author review
```

## Production entry lock

Current production prose entry is:

```text
skills/story-compose/SKILL.md
```

Production direct entry to these package components is forbidden:

```text
skills/novel-prose-writer-zh/SKILL.md
skills/human-writing-l2/SKILL.md
skills/story-deslop/SKILL.md
```

Those components remain complete package members and are orchestrated only by Story Compose in KKKK production.

`skills/human-grain-pass/**` is retained for legacy compatibility / explicit A-B tests, but is not part of the automatic production route.

## Runtime packet alignment

`skills/prose-preparation/runtime/source_shadow_packet.py` now emits:

```text
runtime = source_shadow_reference_packet_v3_story_compose
prose_composer = skills/story-compose/SKILL.md
prose_realization_skill = skills/story-compose/SKILL.md
authority_order includes COMPLETE_STORY_COMPOSE_PACKAGE
```

It also names the three package components for preflight/audit visibility without changing their internal order or rules.

## Test alignment

`tests/prose-writer-integration/test_reference_packet.py` now asserts the Story Compose route rather than the previous direct `novel-prose-writer-zh` route.

## Historical note

`INTEGRATION_AUDIT.md` documents the previous direct `novel-prose-writer-zh` integration. It remains useful as history, but its route semantics are superseded by this audit and by the current production contract.

## Result

```text
CANONICAL_DOCS_ALIGNED: true
S3_OWNER_ALIGNED: true
S3_ROUTE_ALIGNED: true
RUNTIME_PACKET_ALIGNED: true
AUTOMATED_PACKET_TEST_ALIGNED: true
STORY_COMPOSE_INTERNAL_REORDER_BY_KKKK: false
HUMAN_GRAIN_AUTO_ROUTE: false
```
