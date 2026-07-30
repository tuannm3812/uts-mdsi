# Project 15 PDF Layout Refresh Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct list indentation and refresh the Project 15 literature-review PDF with Google Sans Regular body text, differentiated heading colours, and selective bold emphasis.

**Architecture:** Keep the Markdown source as the content authority and extend the existing ReportLab renderer. Add regression tests for font registration, heading hierarchy, hanging list indentation, and emphasis before regenerating and visually reviewing the artifact.

**Tech Stack:** Python 3, ReportLab, pypdf, Google Sans Regular and Medium, PDF raster rendering

## Global Constraints

- Use Google Sans Regular for body, list, table, callout, header, and footer text.
- Use Google Sans Medium for headings and bold emphasis.
- Use blue `#0B57D0` for level-one headings, teal `#137F8B` for level-two headings, and violet `#6554C0` for level-three headings.
- Keep list bullets and numbers inside the content frame with a consistent hanging indent.
- Bold only meaningful technical terms, benchmark names, metrics, hypotheses, risks, and key findings.
- Preserve unrelated worktree changes.

---

### Task 1: Add renderer regression tests

**Files:**
- Create: `tests/test_project15_pdf_renderer.py`
- Modify: none

**Interfaces:**
- Consumes: `build_styles()`, `build_list()`, `inline_markup()`
- Produces: regression coverage for the approved presentation rules

- [ ] Write tests asserting distinct heading colours, Google Sans Regular body text, Google Sans Medium bold mapping, safe list geometry, and Markdown bold conversion.
- [ ] Run the tests and confirm they fail against the current renderer for the intended reasons.

### Task 2: Correct typography, hierarchy, lists, and emphasis

**Files:**
- Modify: `scripts/render_project15_literature_pdf.py`
- Modify: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md`

**Interfaces:**
- Consumes: Google Sans Regular and Medium TTF paths supplied on the command line
- Produces: a styled A4 PDF with safe list geometry and selective technical emphasis

- [ ] Register separate Regular and Medium fonts and use them according to the approved hierarchy.
- [ ] Replace cumulative list indentation with one frame-relative hanging-indent model.
- [ ] Apply distinct heading colours and selective Markdown bold markup.
- [ ] Run the regression tests and confirm they pass.

### Task 3: Regenerate and verify the final artifact

**Files:**
- Modify: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf`
- Copy: Google Drive `03 Project 15 - Terminal-Bench/00 Project Guide/Project 15 - Detailed Literature Review.pdf`

**Interfaces:**
- Consumes: renderer and Markdown source
- Produces: verified repository and Drive PDF copies

- [ ] Build the PDF with Google Sans Regular and Medium.
- [ ] Verify embedded fonts, page count, extracted headings, and absence of out-of-frame text.
- [ ] Render every page to PNG and visually inspect list alignment, hierarchy, bold emphasis, page boundaries, headers, and footers.
- [ ] Copy the verified PDF to Google Drive and confirm matching hashes.
- [ ] Run repository quality checks, commit only scoped Project 15 files, and push to `origin/main`.
