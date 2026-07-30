# Vietnamese Active-Fire Literature Review Design

## Objective

Create one clean Vietnamese literature review by synthesizing:

- `preliminary-findings-fire-hotspot-review-2026-07-29.md`; and
- `active-fire-materials-summary-2026-07-30.md`.

The Vietnamese document is a reading and discussion companion. The English source documents remain unchanged and authoritative for subsequent academic writing.

## Output

Create:

`llm-wiki/02-subjects/36126-innovation-lab-research-project/research/active-fire-literature-review-vi-2026-07-30.md`

Copy the same file to:

`36126 Innovation Lab Research Project/04 Research Work/01 Literature Review`

## Content structure

1. Purpose, scope and evidence status
2. Executive synthesis
3. Operational systems and satellite foundations
4. Australian and international study comparison
5. Cross-study findings
6. Recurring methodological limitations
7. Candidate research gaps
8. Recommended NSW direction
9. Minimum viable experiment
10. Feasibility risks
11. Questions for Dr Arnick
12. Recommended reading sequence
13. English–Vietnamese technical glossary

## Translation rules

- Use natural academic Vietnamese rather than literal sentence-by-sentence translation.
- Preserve author names, product names, dataset names, citations, URLs and quantitative results.
- Introduce important English terminology in parentheses on first use.
- Retain distinctions among hotspot detection, active-fire monitoring, occurrence prediction, fire spread and burned-area mapping.
- Preserve warnings distinguishing verified full-text evidence, preliminary screening and proposed research gaps.
- Do not strengthen tentative claims or present a candidate gap as proven novelty.
- Consolidate overlapping English sections once instead of duplicating them.
- Keep tables concise and readable in Markdown.

## Scope exclusions

- Do not translate the pilot report into this literature review.
- Do not modify the two English source documents.
- Do not create a PDF unless separately requested.
- Do not add unrelated capstone files or temporary output to the research commit.

## Verification

- Confirm all planned sections exist.
- Confirm key citations and operational-source links remain present.
- Compare important figures, sensor resolutions, study regions and limitations with the English sources.
- Scan for untranslated explanatory paragraphs while allowing English technical terms.
- Run `git diff --check`.
- Rerun the active-fire pilot tests before the final research commit.
- Verify the Google Drive copy byte-for-byte.

## Git integration

Use the repository’s Conventional Commit style. The final research commit should include the relevant 36126 research, supervision, literature and pilot files while excluding:

- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/`;
- `tmp/`; and
- unrelated user changes outside the 36126 research project.
