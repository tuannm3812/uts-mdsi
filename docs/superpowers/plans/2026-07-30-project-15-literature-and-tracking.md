# Project 15 Literature and Tracking Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a detailed Google Sans literature-summary PDF and a GitHub-native Markdown tracking system for the six-member Terminal-Bench Project 15 team.

**Architecture:** A source-backed Markdown review is the canonical literature artifact and is rendered into a polished A4 PDF by a focused ReportLab builder. Four small Markdown trackers separate team planning, individual evidence, experiments, and meetings while linking through a Project 15 index. Third-party papers and the final PDF are copied to the synced Google Drive folder; only original Project 15 source and tracking files are committed.

**Tech Stack:** Markdown, Python 3, ReportLab, pypdf, Google Sans Flex, Git, Google Drive desktop sync

## Global Constraints

- Use Google Sans Flex for PDF title, headings, body text, tables, captions, headers, and footers.
- Download the official SIL Open Font License release at execution time; do not commit font binaries.
- Use A4 pages with readable margins, page numbers, and stable source URLs.
- Keep downloaded third-party papers in Google Drive, not Git.
- Keep the literature review’s factual claims traceable to the five verified papers or official Terminal-Bench/Harbor documentation.
- Separate reported evidence from Capstone recommendations and hypotheses.
- Preserve all unrelated worktree changes.
- Commit only Project 15 files and directly related index updates.
- Use the six-member Pair A/Pair B/Pair C allocation model approved in the design.
- Align tracking dates to 29 July through 21 October 2026, including STUVAC on 23 September.

---

## File Structure

### Files to create

- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md`
  - Canonical detailed literature review.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf`
  - Rendered reading copy.
- `scripts/render_project15_literature_pdf.py`
  - Deterministic Markdown-to-PDF builder with Google Sans Flex registration.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/README.md`
  - Project hub and tracker instructions.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/team-task-tracker.md`
  - Populated Week 1-12 team plan.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/individual-contribution-log-template.md`
  - Reusable weekly individual report.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/experiment-register.md`
  - Reproducible experiment log.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/meeting-and-decision-log.md`
  - Mentor/client/team meeting record.

### Files to modify

- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/README.md`
  - Link the Project 15 hub and literature review.
- `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/assignments/README.md`
  - Link the tracking system.

### Temporary and external files

- `/private/tmp/project15-fonts/`
  - Downloaded Google Sans Flex font files and license.
- `/private/tmp/project15-pdf-render/`
  - Rendered page PNGs for visual verification.
- Synced Drive: `.../36127 Innovation Lab Capstone Project/03 Project 15 - Terminal-Bench/`
  - Final PDF reading copy.

---

### Task 1: Acquire and validate Google Sans Flex

**Files:**
- Create temporarily: `/private/tmp/project15-fonts/GoogleSansFlex-VariableFont.ttf`
- Create temporarily: `/private/tmp/project15-fonts/OFL.txt`

**Interfaces:**
- Consumes: Official Google Fonts download or Google Fonts repository.
- Produces: `GOOGLE_SANS_FONT_PATH`, a readable variable TrueType font accepted by ReportLab.

- [ ] **Step 1: Download the official font release**

Run:

```bash
mkdir -p /private/tmp/project15-fonts
curl -L --fail --retry 3 \
  'https://fonts.google.com/download?family=Google%20Sans%20Flex' \
  -o /private/tmp/project15-fonts/google-sans-flex.zip
```

- [ ] **Step 2: Extract the font and license**

Run:

```bash
unzip -o /private/tmp/project15-fonts/google-sans-flex.zip \
  -d /private/tmp/project15-fonts/extracted
find /private/tmp/project15-fonts/extracted -type f \
  \( -name '*.ttf' -o -name 'OFL.txt' \) -print
```

Expected: at least one Google Sans Flex `.ttf` and one `OFL.txt`.

- [ ] **Step 3: Verify ReportLab can register the font**

Run:

```bash
python3 -c "from reportlab.pdfbase import pdfmetrics; from reportlab.pdfbase.ttfonts import TTFont; pdfmetrics.registerFont(TTFont('GoogleSansFlex', '/private/tmp/project15-fonts/extracted/GoogleSansFlex-VariableFont.ttf')); print(pdfmetrics.getFont('GoogleSansFlex').fontName)"
```

Expected: `GoogleSansFlex`.

---

### Task 2: Write the detailed literature review

**Files:**
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md`

**Interfaces:**
- Consumes: Five verified PDFs, official Terminal-Bench 2.1 release/run pages, and Harbor agent documentation.
- Produces: Complete heading-based Markdown consumed by the PDF builder.

- [ ] **Step 1: Create the literature review with traceable sections**

Write the document with this exact major structure:

```markdown
# Project 15 Literature Review
## Project context
## Executive summary
## Key terminology
## Paper 1: Terminal-Bench
## Paper 2: SWE-agent
## Paper 3: OpenHands
## Paper 4: Agentless
## Paper 5: OpenHands Software Agent SDK
## Cross-paper synthesis
## Implications for our custom harness
## Experimental variables
## Evaluation framework
## Failure taxonomy
## Reproducibility, cost, and validity
## Research questions and hypotheses
## Six-member reading allocation
## Recommended reading order
## References
```

For each paper, include:

- research problem;
- proposed approach;
- architecture or workflow;
- evaluation method;
- principal findings;
- limitations;
- relevance to Project 15;
- candidate experiment derived from the paper.

- [ ] **Step 2: Add evidence/recommendation labels**

Use explicit callouts:

```markdown
> **Reported finding:** ...

> **Project implication:** ...

> **Proposed hypothesis:** ...
```

This prevents the Capstone team’s proposals from being misrepresented as findings from the papers.

- [ ] **Step 3: Add the cross-paper comparison table**

Use columns:

```text
Source | Main contribution | Harness lever | Evidence | Limitation | Project use
```

- [ ] **Step 4: Add stable references**

Include plain URLs for:

- `https://arxiv.org/abs/2601.11868`
- `https://arxiv.org/abs/2405.15793`
- `https://arxiv.org/abs/2407.16741`
- `https://arxiv.org/abs/2407.01489`
- `https://arxiv.org/abs/2511.03690`
- `https://www.tbench.ai/news/terminal-bench-2-1`
- `https://www.tbench.ai/docs/run-terminal-bench-2-1`
- `https://www.harborframework.com/docs/agents`

- [ ] **Step 5: Run content checks**

Run:

```bash
rg -n 'TBD|TODO|PLACEHOLDER|citation needed' \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md
```

Expected: no output.

---

### Task 3: Build the Google Sans PDF renderer

**Files:**
- Create: `scripts/render_project15_literature_pdf.py`
- Test input: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md`
- Output: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf`

**Interfaces:**
- Consumes: `--input`, `--output`, and `--font` command-line paths.
- Produces: A4 PDF with embedded Google Sans Flex and page metadata.

- [ ] **Step 1: Write an argument-validation test**

Run before implementation:

```bash
python3 scripts/render_project15_literature_pdf.py \
  --input /missing.md \
  --output /private/tmp/missing.pdf \
  --font /missing.ttf
```

Expected: non-zero exit because the renderer does not exist yet.

- [ ] **Step 2: Implement the renderer**

Implement:

```python
def parse_args() -> argparse.Namespace: ...
def register_google_sans(font_path: Path) -> None: ...
def build_styles() -> dict[str, ParagraphStyle]: ...
def parse_markdown(source: str, styles: dict[str, ParagraphStyle]) -> list[Flowable]: ...
def add_page_chrome(canvas: Canvas, document: BaseDocTemplate) -> None: ...
def build_pdf(input_path: Path, output_path: Path, font_path: Path) -> None: ...
def main() -> int: ...
```

Required rendering support:

- headings levels 1-3;
- paragraphs and blockquotes;
- ordered and unordered lists;
- fenced code blocks;
- simple Markdown tables;
- automatic URL link conversion;
- `KeepTogether` or table splitting where appropriate;
- footer containing `36127 Capstone - Project 15`;
- page number on every content page;
- PDF title and author metadata.

- [ ] **Step 3: Run the missing-input validation**

Run the Step 1 command again.

Expected: non-zero exit with a concise missing-file message.

- [ ] **Step 4: Generate the PDF**

Run:

```bash
python3 scripts/render_project15_literature_pdf.py \
  --input llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md \
  --output llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf \
  --font /private/tmp/project15-fonts/extracted/GoogleSansFlex-VariableFont.ttf
```

Expected: zero exit and non-empty PDF.

- [ ] **Step 5: Verify embedded font and text**

Run:

```bash
python3 -c "from pypdf import PdfReader; p='llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf'; r=PdfReader(p); text=''.join(x.extract_text() or '' for x in r.pages); assert len(r.pages)>=8; assert 'Terminal-Bench' in text; assert 'Research questions and hypotheses' in text; fonts=set(); [(fonts.update(str(v) for v in (page.get('/Resources',{}).get('/Font',{}) or {}).values())) for page in r.pages]; print(len(r.pages), len(text), fonts)"
```

Expected: at least eight pages and required headings present.

- [ ] **Step 6: Render every page for visual verification**

Render into `/private/tmp/project15-pdf-render/` with Poppler when available. If Poppler remains unavailable, use the runtime PDF renderer or macOS conversion tools and inspect every generated page image.

Acceptance checks:

- no clipped titles or table cells;
- no overlapping text;
- consistent Google Sans appearance;
- readable code and URLs;
- correct page numbers;
- no blank unintended pages.

- [ ] **Step 7: Correct defects and regenerate**

Modify only the renderer or source sections responsible for observed problems, rebuild, and rerender until all pages pass.

- [ ] **Step 8: Commit the literature source, renderer, and verified PDF**

```bash
git add \
  scripts/render_project15_literature_pdf.py \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.md \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf
git commit -m "docs(capstone): add project 15 literature review"
```

---

### Task 4: Create the Project 15 GitHub tracking hub

**Files:**
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/README.md`
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/team-task-tracker.md`
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/individual-contribution-log-template.md`
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/experiment-register.md`
- Create: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/meeting-and-decision-log.md`

**Interfaces:**
- Consumes: Confirmed Week 1-12 calendar and six-member workstream design.
- Produces: Linked GitHub-native operational records.

- [ ] **Step 1: Create the Project 15 README**

Include:

- project objective;
- current unknowns for the mentor;
- link to the literature review;
- links to all four trackers;
- Pair A/B/C responsibilities;
- status vocabulary;
- evidence standards;
- weekly update routine.

- [ ] **Step 2: Populate the team task tracker**

Create initial IDs `P15-001` through at least `P15-040`.

Every task row must contain:

```text
ID | Week | Due | Workstream | Task | Primary | Reviewer | Priority | Status | Dependency | Deliverable/evidence
```

Balance ownership so Members 1-6 each own a comparable number of initial tasks and each reviews tasks outside their primary pair.

Milestone coverage:

- Week 1: governance, skills survey, literature, mentor questions
- Week 2: Harbor/Docker setup, oracle smoke test, model/cost confirmation
- Week 3: architecture, baselines, frozen 20-task development split
- Week 4: baseline runs and protocol review
- Week 5: early client progress package
- Week 6: custom harness V1 and first ablations
- Week 7: midpoint demonstration
- Week 8: refined harness, context/retry/verification experiments
- STUVAC: consolidation and contingency
- Week 9: pre-final review and design freeze
- Week 10: full 89-task evaluation and analysis
- Week 11: final presentation
- Week 12: showcase, repository and reproducibility handover

- [ ] **Step 3: Create the individual log template**

Include a copyable weekly block with:

```text
Student:
Week:
Reporting period:
Primary role:
Secondary role:
Hours:

Planned tasks
Completed work
Contribution to team progress
Challenges and responses
Meetings and communication
Learning and decisions
Next-week plan
Evidence links
Self-review
```

The self-review must explicitly address the 30/35/20/15 contribution criteria.

- [ ] **Step 4: Create the experiment register**

Provide:

- immutable run metadata checklist;
- experiment table;
- failure taxonomy;
- decision log;
- example smoke-test row clearly labelled `Example - remove after first real run`.

- [ ] **Step 5: Create the meeting and decision log**

Seed meeting sections for:

- first mentor meeting;
- Week 5 early progress client meeting;
- Week 7 midpoint client meeting;
- Week 9 pre-final client meeting;
- Week 11 final presentation review;
- Week 12 handover retrospective.

- [ ] **Step 6: Validate cross-links and schedule coverage**

Run:

```bash
rg -n '29 Jul|5 Aug|12 Aug|19 Aug|26 Aug|2 Sep|9 Sep|16 Sep|23 Sep|30 Sep|7 Oct|14 Oct|21 Oct' \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15
rg -n 'TBD|TODO|PLACEHOLDER' \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15
```

Expected: every project date is present; no unfinished placeholders.

- [ ] **Step 7: Commit the trackers**

```bash
git add llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15
git commit -m "docs(capstone): add project 15 delivery trackers"
```

---

### Task 5: Update Capstone navigation

**Files:**
- Modify: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/README.md`
- Modify: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/assignments/README.md`

**Interfaces:**
- Consumes: Final Project 15 paths.
- Produces: Discoverable links from existing subject indexes.

- [ ] **Step 1: Add the Project 15 links**

Add links for:

- Project 15 hub;
- literature review;
- team task tracker;
- individual contribution template.

- [ ] **Step 2: Check every new relative link**

Run a small path-resolution check that parses new Markdown links and confirms each local target exists.

Expected: all new local links resolve.

- [ ] **Step 3: Commit navigation**

```bash
git add \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/README.md \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/assignments/README.md
git commit -m "docs(capstone): link project 15 workspace"
```

---

### Task 6: Copy the final PDF to Google Drive

**Files:**
- Source: `llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf`
- Destination: synced Drive `03 Project 15 - Terminal-Bench/00 Project Guide/Project 15 - Detailed Literature Review.pdf`

**Interfaces:**
- Consumes: Verified PDF.
- Produces: User-readable Drive copy with matching SHA-256 digest.

- [ ] **Step 1: Create the destination folder**

```bash
mkdir -p '<synced subject folder>/03 Project 15 - Terminal-Bench/00 Project Guide'
```

- [ ] **Step 2: Copy the verified PDF**

```bash
cp \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/project-15-terminal-bench-literature-review.pdf \
  '<synced subject folder>/03 Project 15 - Terminal-Bench/00 Project Guide/Project 15 - Detailed Literature Review.pdf'
```

- [ ] **Step 3: Verify source and destination hashes**

Run `shasum -a 256` on both files.

Expected: identical digests.

---

### Task 7: Final verification, scoped commit audit, and push

**Files:**
- Verify all files listed in the File Structure section.

**Interfaces:**
- Consumes: All verified deliverables and Git history.
- Produces: Clean scoped commits pushed to `origin/main`.

- [ ] **Step 1: Invoke verification-before-completion**

Run all required artifact and repository verification before claiming completion.

- [ ] **Step 2: Check Markdown and repository whitespace**

```bash
git diff --check
rg -n 'TBD|TODO|PLACEHOLDER|citation needed' \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research \
  llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15
```

Expected: no unintended placeholders or whitespace errors.

- [ ] **Step 3: Verify PDF again after the final commit**

Confirm:

- file exists and is non-empty;
- pypdf opens every page;
- required headings extract successfully;
- Google Sans is embedded;
- rendered pages match the visually approved revision.

- [ ] **Step 4: Audit commit scope**

```bash
git status --short
git log --oneline --decorate -5
git diff --name-status origin/main...HEAD
```

Confirm that unrelated 36126 Research Project changes remain uncommitted and are not part of the Project 15 commits.

- [ ] **Step 5: Push**

```bash
git push origin main
```

Expected: remote reports `main` updated to the final local commit.

- [ ] **Step 6: Verify remote synchronization**

```bash
git fetch origin main
git rev-parse HEAD
git rev-parse origin/main
```

Expected: both commit hashes match.
