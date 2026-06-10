# LLM Wiki Scale and Quality Improvement Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Turn the LLM Wiki into a stable, reusable knowledge system that can absorb all master subjects, keep metadata consistent, and stay clean with repeatable validation.

**Architecture:** Keep the repo as a content graph (subject folders + shared concepts) backed by scripted import/normalization and validation. Add a thin tooling layer in `scripts/` and explicit content contracts so humans and agents can make high-volume updates safely.

**Tech Stack:** Python 3, Markdown, existing `scripts/*.py`, Git, optional Makefile/`uv`, Obsidian-compatible Markdown.

---

## Operating model

Run in 3 layers:

1. **Agents** do most repetitive work (per-subject normalization, link fixes, frontmatter checks).
2. **Scripts** enforce consistency at repo scale.
3. **Weekly QA pass** catches regressions before they accumulate.

No semantic changes to coursework content are planned in the first phase; focus on structure, consistency, and reliability.

## Success Criteria

- 100% subject folders in `llm-wiki/02-subjects/*` have:
  - `assignments/assessment-planning.md`
  - `assignments/README.md` with standard sections
  - `lectures/README.md`, `notebooks/README.md`, `questions/README.md` where applicable
- A script-run validation command returns zero high-priority issues.
- `scripts/import_drive_subjects.py` can be rerun idempotently in CI-like checks without breaking existing files.
- At least 90% of new or touched subject folders include consistent frontmatter and internal links.

---

## Task 1: Baseline Audit and Subject Coverage

**Files:**
- New: `docs/superpowers/plans/2026-06-11-llm-wiki-scale-and-quality-plan.md` (this file)
- New: `docs/superpowers/audit/subject-coverage-YYYY-MM-DD.json` (generated)

- [x] Export a full subject map from `scripts/import_drive_subjects.py`:

```bash
python3 scripts/import_drive_subjects.py
python3 - <<'PY'
from pathlib import Path
import csv
import json

manifest = Path("llm-wiki/00-admin/drive-import-manifest.csv")
rows = list(csv.DictReader(manifest.open()))
subjects = sorted(set(r["repo_subject"] for r in rows))
summary = {s: sum(1 for r in rows if r["repo_subject"] == s) for s in subjects}
Path("docs/superpowers/audit").mkdir(parents=True, exist_ok=True)
Path("docs/superpowers/audit/subject-coverage-2026-06-11.json").write_text(json.dumps(summary, indent=2))
print(len(subjects), "subjects found:", ", ".join(subjects))
PY
```

- [x] Record missing subject folders in a short gap list in this plan (owner: Lead Agent).

### Task 1 Execution Notes (completed)

- `docs/superpowers/audit/subject-coverage-2026-06-11.json` created.
- 13 subjects present under `llm-wiki/02-subjects`.
- Missing subject folder list: none.

Subjects:

- 36100-data-science-for-innovation
- 36103-statistical-thinking-for-data-science
- 36104-data-visualisation-and-narratives
- 36106-machine-learning-algorithms-and-applications
- 36118-applied-natural-language-processing
- 36120-advanced-machine-learning-application
- 36121-artificial-intelligence-principles-and-applications
- 36122-python-programming
- 43008-reinforcement-learning
- 94691-deep-learning
- 94692-data-science-practice
- 94693-big-data-engineering
- genai

## Task 2: Formalize Content Contracts

**Files:**
- New: `docs/superpowers/contracts/content-contracts.md`
- Modify: `llm-wiki/07-templates/assessment-template.md`
- Modify: `llm-wiki/07-templates/concept-template.md`
- Modify: `llm-wiki/07-templates/subject-template.md`

- [x] Define explicit required fields for each file class:
  - `subject-index` frontmatter shape for `02-subjects/*/README.md`.
  - `assessment` frontmatter for `assignments/assessment-planning.md`.
  - Standard section ordering for assignments/lectures/questions/notebooks/readmes.
- [x] Add a canonical example in each template:
  - Assessment Workflow
  - LLM Review Prompt block
  - Source count table/section
- [x] Add "What to do if unknown field" policy to avoid partial/inconsistent metadata.

## Task 3: Assignments Standardization (Parallel by subject)

**Files:**
- Existing: `llm-wiki/02-subjects/*/assignments/README.md`
- Existing: `llm-wiki/02-subjects/*/assignments/assessment-planning.md`

- [ ] Dispatch one agent per 4 subjects to apply this exact pattern:
  - heading + overview
  - `## Assessment Pages` links include `assessment-planning.md` + AT pages
  - `## Standard Review Workflow`
  - `## Raw Imports`
  - `## LLM Review Prompt`
  - source count line kept with current naming.
- [ ] Normalize assessment file names per subject (avoid mixed `assignment-1.md` and `assignment1.md` unless source-specific reason exists).
- [ ] Update `llm-wiki/02-subjects/*/assignments/README.md` only; do not alter AT content unless a link is broken.

## Task 4: Import Reliability and Inventory Accuracy

**Files:**
- `scripts/import_drive_subjects.py`
- `llm-wiki/00-admin/drive-import-manifest.csv`
- `llm-wiki/00-admin/import-summary.md` (new or updated)
- `llm-wiki/00-admin/drive-import-manifest` consumers (if any)

- [x] Add deterministic file ordering and clear duplicate handling for reruns.
- [x] Add checksum-based short-circuit when file already exists and unchanged.
- [x] Add explicit `dry-run` flag support and summary mode.
- [x] Add error log file: `docs/superpowers/audit/import-errors-YYYY-MM-DD.json`.
- [x] Validate `REFERENCE_ONLY_EXTENSIONS` policy for all semesters and document any exceptions.

### Task 4 execution notes (completed)

- `scripts/import_drive_subjects.py` now supports:
  - deterministic traversal and stable row ordering
  - duplicate destination detection
  - checksum short-circuit via SHA-256 for existing files
  - `--dry-run` mode and `--summary` output
  - per-run JSON error log in `docs/superpowers/audit/import-errors-YYYY-MM-DD.json`
  - reference-only policy validation and documented status in summary
- `llm-wiki/00-admin/drive-import-manifest.csv` now includes checksum columns.
- `llm-wiki/00-admin/import-summary.md` and generated subject inventories are updated by the same run.

## Task 5: Quality Gates / Linting Script

**Files:**
- New: `scripts/audit_llm_wiki.py`
- New: `scripts/requirements.txt` (if adding third-party libs; keep stdlib preferred)
- New: `Makefile` target `make quality`

- [x] Build checks:
  - every assignment folder has README + assessment-planning
  - AT link exists and file exists
  - markdown links are valid relative paths
  - no duplicate source files under `sources/raw/` and `lectures/raw/` unless expected
  - frontmatter required fields present for subject/assignment pages
- [x] Add non-blocking warnings for optional issues and hard errors for critical schema misses.
- [x] Run with:
```bash
python3 scripts/audit_llm_wiki.py --strict
```
- [x] Gate merges/pushes through this check.

- [x] Task 5 execution notes (completed):
  - `python3 scripts/audit_llm_wiki.py --strict` returns zero errors and zero warnings.
  - `make quality` and `make quality-full` both pass cleanly after duplicate-basename normalization.

## Task 6: Subject Onboarding Pipeline for New Subjects

**Files:**
- `scripts/create_learning_layer.py`
- `scripts/create_obsidian_indexes.py`
- `scripts/import_drive_subjects.py`
- `docs/superpowers/` runbooks

- [ ] Add `--subject` mode to import and scaffold only selected subjects.
- [ ] Auto-generate missing folders from template:
  - `lectures/raw`, `assignments/raw`, `notebooks/raw`, `sources/raw`
  - `README.md` placeholders for lectures/notebooks/questions
- [ ] Add a single command:
```bash
python3 scripts/import_drive_subjects.py --subject "36122-python-programming" --sync
python3 scripts/create_obsidian_indexes.py --subject "36122-python-programming"
```
- [ ] Add "rollback-safe" process: dry-run + manifest comparison.

## Task 7: Obsidian Usability Enhancements

**Files:**
- `llm-wiki/00-admin/obsidian-setup.md`
- `llm-wiki/08-assets/README.md`
- `llm-wiki/00-admin/vault-structure.md`

- [ ] Publish a practical Obsidian setup section:
  - workspace split for `02-subjects` + `03-shared-concepts`
  - graph settings for cross-links
  - common query snippets (Dataview if present)
- [ ] Add consistent note naming conventions for rapid linking.
- [ ] Add quick-start script for opening a fresh vault from this repo.

## Task 8: Link & Naming Consistency Cleanup

**Files:**
- `llm-wiki/02-subjects/*/README.md`
- `llm-wiki/02-subjects/*/*/README.md`
- `llm-wiki/02-subjects/*/glossary.md`

- [ ] Fix inconsistent filenames (`assignment-1.md` vs `assignment1.md`) based on one chosen convention.
- [ ] Enforce consistent slug format in subject slugs and notes.
- [ ] Resolve any broken links found by Task 5 and log intentional exclusions.
- [ ] Add short migration notes for any renamed files to preserve old links.

## Task 9: Multi-Subject AI Prompt Suite

**Files:**
- `llm-wiki/06-prompt-library/master-prompts.md`
- `llm-wiki/06-prompt-library/` (new files)
- `llm-wiki/llm-wiki-workflow.md` references

- [ ] Create standardized prompt packs per subject type:
  - AT review prompts
  - lecture recap prompts
  - synthesis prompts from multiple sessions
  - exam prep prompts tied to shared concepts
- [ ] Add templates for "evidence-first answers" and citation-check prompts.
- [ ] Keep prompts non-assignmentspecific where possible.

## Task 10: Governance and Maintenance Cadence

**Files:**
- `README.md`
- `llm-wiki/README.md`
- `llm-wiki/00-admin/vault-structure.md`

- [ ] Set monthly maintenance cadence:
  - run quality checks
  - regenerate inventory for changed subjects
  - review top 3 broken links and fix first
- [ ] Add a simple "change log" file under `00-admin` for major wiki updates.
- [ ] Define rollback and manual verification workflow before large agentic batch updates.

## Risk Register

- **Risk:** Over-normalizing and losing course-specific nuance in AT files.
  - Mitigation: lock contracts to section-level only; preserve source content unchanged.
- **Risk:** Google Drive path drift or unavailable files.
  - Mitigation: importer strict mode with dry-run first and clear error report.
- **Risk:** Parallel agents creating merge conflicts in adjacent files.
  - Mitigation: per-subject ownership and short, non-overlapping patches.
- **Risk:** Broken legacy links during naming standardization.
  - Mitigation: keep redirect notes or link aliases for renamed files where possible.

## Immediate next 14 days (recommended)

1. Launch Task 1 + Task 2 with one lead.
2. Start Task 3 with 3 agents, each doing 4-5 subjects.
3. Run Task 5 baseline quality gate and fix high priority issues only.
4. Start Task 4 in parallel to reduce future import risk.
5. Pause and review before any large content edits.

Plan complete and saved to `docs/superpowers/plans/2026-06-11-llm-wiki-scale-and-quality-plan.md`. Two execution options:

1. **Subagent-Driven (recommended)** — dispatch one focused agent per task.
2. **Inline Execution** — execute task batches here with checkpointed QA after each epic.
