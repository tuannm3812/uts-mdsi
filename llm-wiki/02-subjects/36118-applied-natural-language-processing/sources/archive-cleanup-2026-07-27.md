---
type: source-cleanup-record
subject: 36118-applied-natural-language-processing
date: 2026-07-27
---

# Archive Cleanup Record

## Result

- Removed 38 exact, SHA-256-verified duplicate files.
- Recovered approximately 379.9 MiB.
- Retained one canonical copy of every duplicated item.
- Preserved all unique files, including readings, assignment references,
  images, datasets, notebooks, and slide decks.

## Canonical-location Rules

- 2026 materials live in explicit `current-2026/` directories.
- 2025 session slide exports stay in `lectures/raw/archive-2025/`.
- 2025 course notebooks stay in
  `notebooks/raw/archive-2025/course-notebooks/`.
- Supplementary notebooks stay in
  `notebooks/raw/archive-2025/supplementary/`.
- 2025 assessment material stays in `assignments/raw/archive-2025/`.
- Unique files in `lectures/raw/archive-2025/resources/` are
  inherited supporting media and references, not confirmed duplicates.

## Removed Duplicate Families

- Session 1, 2, 3, 4, 5, 6, and 8 PDF export copies from `Uploaded Media`
- Four extra Session 4 PowerPoint copies
- Four extra guest-session PDF exports
- Extra AT1 development-template notebook
- Extra Reddit dataset copy

No unique material was intentionally deleted. Because the removed raw files
were ignored import artefacts rather than Git-tracked files, recovery would
require re-importing the previous-semester source bundle.
