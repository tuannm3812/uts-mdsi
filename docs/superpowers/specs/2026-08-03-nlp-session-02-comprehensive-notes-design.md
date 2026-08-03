# NLP Session 02 Comprehensive Notes Design

## Objective

Create one comprehensive, study-ready PDF for 36118 Applied Natural Language
Processing Session 02 using the newly downloaded Spring 2026 lecture deck and
four practical notebooks. Organise the current sources in the existing 2026
lecture and notebook structure, then remove only the verified source copies
from Downloads.

## Deliverables

1. `lectures/session-02-preparation-2026.md` containing the connected,
   source-grounded note text and source inventory.
2. `lectures/handouts/session-02-comprehensive-notes.pdf` rendered and visually
   inspected for lecture use.
3. Current Session 02 sources stored under:
   - `lectures/current-2026/`
   - `notebooks/current-2026/session-02/`
4. Updated lecture, notebook, handout, and source inventory documentation where
   the current repository structure requires it.

No separate note-taking handout is in scope.

## Source Priority and Provenance

Use the files in this order:

1. `ANLP Session2_Week2-5.pdf`, the current Spring 2026 lecture deck.
2. `ANLP_Session_2_Part1_Text_Analysis.ipynb`.
3. `ANLP_Session2_Part2_Topic_Modeling.ipynb`.
4. `ANLP_Session2__Part3_TextClustering.ipynb`.
5. `ANLP_Session_2_HW.ipynb`.
6. Archived 2025 Session 02 material only for gap checking and clearly marked
   supplementary context.

Record file hashes before moving or deleting anything. Current-semester files
remain authoritative if archival terminology or sequencing differs.

## Note Content

Follow the teaching sequence established by the 2026 deck and notebooks. The
notes should connect, where present in those sources:

- exploratory text analysis and preprocessing decisions;
- document representations and their information-loss trade-offs;
- topic modelling concepts, workflow, interpretation, and evaluation;
- text clustering concepts, workflow, comparison, and evaluation;
- practical Python code from the notebooks;
- homework expectations and common failure modes;
- explicit links to AT1 only where the sources or current assessment workflow
  make the relevance clear;
- source-grounded learning objectives and revision prompts.

Preserve formulas and code that are actually taught. Add brief Deep Dives only
when they clarify a concept introduced in Session 02, and do not import later
course material.

## Document Design

Apply the universal lecture-note specification and NLP supplement:

- no cover page;
- numbered Level 1 and Level 2 headings;
- connected prose with selective bullets;
- selectively bolded technical terms in context;
- unnumbered Deep Dive block quotes;
- Google Sans 11 pt body text with single spacing;
- compact paragraph spacing and connected heading hierarchy;
- syntax-highlighted code blocks;
- formulas defined and interpreted where relevant;
- no decorative rules beneath headings.

The existing Session 01 comprehensive notes are the visual and structural
reference, while Session 02 content remains independent and source-grounded.

## Implementation and Validation

1. Inspect slide count, page visuals, notebook cells, Markdown headings, code,
   outputs, and execution metadata.
2. Copy current sources into their final repository locations with stable,
   descriptive names.
3. Write the preparation Markdown with traceable source notes.
4. Render the PDF through the existing NLP comprehensive-notes generator,
   extending the generator only if Session 02 content requires a general,
   reusable capability.
5. Render every PDF page to images and inspect typography, page breaks,
   headings, equations, tables, and code blocks.
6. Confirm the final PDF contains no missing or clipped content and that the
   repository copies match the original Downloads hashes.
7. Remove only the five verified Session 02 files from Downloads. Leave
   `.DS_Store` and unrelated downloads untouched.
8. Run repository checks and commit only 36118 Session 02 changes.

## Error Handling and Safety

- Do not delete Downloads files until final copies and hashes are verified.
- Treat corrupt or non-executable notebook cells as source evidence; preserve
  the originals and document issues rather than silently rewriting them.
- If Google Sans is unavailable to the renderer, stop rather than substituting
  an unapproved body font.
- If the 2026 slides conflict with archived notes, follow the 2026 slides and
  record the discrepancy.
- Do not modify unrelated dirty worktree files.

## Acceptance Criteria

- All five current Session 02 sources are present in the correct repository
  locations and hash-verified.
- The Markdown and PDF cover the slide and notebook sequence without unrelated
  later-session content.
- The PDF follows the established typography and spacing rules and has been
  visually inspected page by page.
- The handout index and relevant source inventories identify Session 02 as
  current 2026 material.
- Only the five verified Session 02 source files are removed from Downloads.
- Verification commands pass and the scoped commit excludes unrelated changes.
