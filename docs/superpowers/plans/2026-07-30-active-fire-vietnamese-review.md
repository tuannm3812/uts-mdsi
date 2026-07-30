# Vietnamese Active-Fire Literature Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce one accurate, readable Vietnamese synthesis of the two English active-fire literature-review documents, synchronize it to Google Drive, and commit/push the complete 36126 research workspace without unrelated files.

**Architecture:** The output is a standalone Markdown companion organized by research decisions rather than the source files’ separate structures. Verification uses structural checks, citation/figure comparison, repository tests, Git diff inspection, and byte-level Drive comparison.

**Tech Stack:** Markdown, `rg`, Python/pytest for the existing pilot tests, Git, Google Drive filesystem synchronization.

## Global Constraints

- The Vietnamese document synthesizes both English sources without modifying them.
- Important English technical terms appear in parentheses on first use.
- Citations, URLs, quantitative results, task distinctions and evidence-status warnings remain intact.
- Candidate gaps remain provisional rather than asserted novelty.
- The pilot report is not translated into the literature review.
- No PDF is created.
- Unrelated capstone files and `tmp/` are excluded from the final research commit.

---

### Task 1: Build the Vietnamese synthesis

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/research/active-fire-literature-review-vi-2026-07-30.md`
- Modify: `llm-wiki/02-subjects/36126-innovation-lab-research-project/README.md`

**Interfaces:**
- Consumes: the two English review documents and their citations.
- Produces: one Vietnamese reading companion linked from the subject index.

- [ ] **Step 1:** Extract the source documents’ section structures, citations, numerical claims and evidence warnings.
- [ ] **Step 2:** Write the Vietnamese synthesis using the 13 approved sections.
- [ ] **Step 3:** Consolidate repeated material and retain distinct evidence or limitations.
- [ ] **Step 4:** Add the Vietnamese review to the subject README.

### Task 2: Verify translation coverage and accuracy

**Files:**
- Verify: `llm-wiki/02-subjects/36126-innovation-lab-research-project/research/active-fire-literature-review-vi-2026-07-30.md`

**Interfaces:**
- Consumes: the completed Vietnamese document.
- Produces: structural, terminology, citation and quantitative verification evidence.

- [ ] **Step 1:** Check that all 13 approved sections exist.
- [ ] **Step 2:** Confirm MODIS 1 km, VIIRS 375 m, DEA history/update information, MyFireWatch limitations, NSW evidence and key study results match the English sources.
- [ ] **Step 3:** Confirm operational, peer-reviewed, preprint and provisional-gap evidence are not conflated.
- [ ] **Step 4:** Check that key URLs and citation targets remain present.
- [ ] **Step 5:** Run `git diff --check`.

### Task 3: Synchronize Google Drive

**Files:**
- Copy: Vietnamese review to `04 Research Work/01 Literature Review`

**Interfaces:**
- Consumes: verified repository document.
- Produces: byte-identical Drive copy.

- [ ] **Step 1:** Copy the Vietnamese review to the existing literature-review folder.
- [ ] **Step 2:** Compare repository and Drive files with `cmp`.

### Task 4: Verify and commit research workspace

**Files:**
- Stage: relevant `36126-innovation-lab-research-project` files
- Stage: approved design and implementation plan
- Exclude: `36127-innovation-lab-capstone-project`, `tmp/`, and unrelated files

**Interfaces:**
- Consumes: all verified research deliverables accumulated in the current worktree.
- Produces: a Conventional Commit containing only the intended research work.

- [ ] **Step 1:** Run all active-fire pilot tests.
- [ ] **Step 2:** Inspect staged paths and `git diff --cached --check`.
- [ ] **Step 3:** Commit with `feat(research): add active-fire review and data pilot`.

### Task 5: Push and verify remote state

**Files:**
- Push: current `main` branch to its configured upstream.

**Interfaces:**
- Consumes: verified local commits.
- Produces: remote branch containing the Vietnamese review and research workspace.

- [ ] **Step 1:** Confirm the current branch, upstream and ahead/behind state.
- [ ] **Step 2:** Push without force.
- [ ] **Step 3:** Confirm local `HEAD` equals the upstream commit.
- [ ] **Step 4:** Report excluded pending files separately.
