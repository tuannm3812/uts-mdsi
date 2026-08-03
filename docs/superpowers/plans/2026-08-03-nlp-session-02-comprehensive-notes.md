# NLP Session 02 Comprehensive Notes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (\`- [ ]\`) syntax for tracking.

**Goal:** Organise the five current Spring 2026 Session 02 sources, create one source-grounded comprehensive notes PDF, verify every page, and remove only the hash-verified source copies from Downloads.

**Architecture:** Treat the downloaded slide deck and notebooks as immutable inputs. Copy them into the established current-2026 structure, extract a source inventory into a curated Markdown note, and render that note with the existing Matplotlib PDF generator after making its session footer reusable. Verification covers file hashes, notebook structure, PDF text, font embedding, page rendering, and scoped Git state before Downloads cleanup.

**Tech Stack:** Python 3.11, \`pypdf\`, \`nbformat\`, Matplotlib/PdfPages, Google Sans TTF resources, PyMuPDF or Poppler for rendering, pytest, Git.

## Global Constraints

- Current Spring 2026 slides and notebooks are authoritative; archived 2025 material is gap-checking reference only.
- Produce one comprehensive PDF and no separate note-taking handout.
- Body font is Google Sans 11 pt with single spacing; code is approximately 9.5 pt with conventional syntax colours.
- Use numbered Level 1 and Level 2 headings, unnumbered Deep Dives, no cover page, and no decorative rules beneath headings.
- Do not introduce later-session content.
- Do not delete Downloads files until repository copies and hashes are verified.
- Remove only the five verified Session 02 sources; leave \`.DS_Store\` and unrelated downloads untouched.
- Do not modify or commit unrelated dirty worktree files.

---

## File Map

**Create**

- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/current-2026/ANLP Session2_Week2-5.pdf\` - authoritative current lecture deck.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02/ANLP_Session_2_Part1_Text_Analysis.ipynb\` - text-analysis practical.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02/ANLP_Session2_Part2_Topic_Modeling.ipynb\` - topic-modelling practical.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02/ANLP_Session2_Part3_TextClustering.ipynb\` - clustering practical with normalised filename.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02/ANLP_Session_2_HW.ipynb\` - homework notebook.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02/README.md\` - notebook order, setup, and summaries.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-02-preparation-2026.md\` - curated source-grounded note content.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/handouts/session-02-comprehensive-notes.pdf\` - final inspected notes.
- \`tests/test_create_nlp_comprehensive_notes.py\` - reusable session-label tests.

**Modify**

- \`scripts/create_nlp_comprehensive_notes.py\` - infer session label and output filename from the input note instead of hard-coding Session 01.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/README.md\` - identify the current Session 02 deck.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/handouts/README.md\` - index the new comprehensive PDF.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/README.md\` - link the Session 02 notebook set.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/sources/current-semester-2026.md\` - record receipt and archive comparison.
- \`llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-02.md\` - replace the draft source list and working summary with a pointer to current materials and the comprehensive note.

## Task 1: Ingest and Verify Current Sources

**Files:**
- Create: the five current source files listed in the file map.
- Create: \`notebooks/current-2026/session-02/README.md\`.

**Interfaces:**
- Consumes: five exact files under \`/Users/tuannm3812/Downloads/\`.
- Produces: immutable repository copies and a SHA-256 manifest printed during verification.

- [ ] **Step 1: Capture source hashes and structural metadata**

Run \`shasum -a 256\` against the five exact Downloads paths. Expected: five SHA-256 rows and no missing-file errors.

- [ ] **Step 2: Copy sources into the current-semester structure**

Use explicit \`mkdir -p\` and \`cp -p\` commands. Rename only the clustering copy from \`ANLP_Session2__Part3_TextClustering.ipynb\` to \`ANLP_Session2_Part3_TextClustering.ipynb\`; preserve all other filenames.

- [ ] **Step 3: Verify copied hashes**

Run \`shasum -a 256\` on the five repository copies and compare each digest with Step 1. Expected: all five digest pairs match exactly.

- [ ] **Step 4: Inspect PDF and notebook structure**

Run:

\`\`\`python
from pathlib import Path
import nbformat
from pypdf import PdfReader

assert len(PdfReader(str(slide_path)).pages) > 0
for path in notebook_paths:
    nb = nbformat.read(path, as_version=4)
    assert nb.cells
    assert all(cell.cell_type in {"markdown", "code", "raw"} for cell in nb.cells)
\`\`\`

Expected: non-zero slide pages and non-empty valid notebooks.

- [ ] **Step 5: Write the Session 02 notebook README**

Document the recommended order: Part 1 Text Analysis, Part 2 Topic Modelling, Part 3 Text Clustering, then Homework. Include Python/kernel requirements discovered from notebook metadata and concise summaries based on inspected cells.

- [ ] **Step 6: Commit the verified source set**

\`\`\`bash
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/current-2026
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/current-2026/session-02
git commit -m "feat(36118): add current session 2 materials"
\`\`\`

## Task 2: Generalise the Comprehensive-Notes Renderer

**Files:**
- Modify: \`scripts/create_nlp_comprehensive_notes.py\`.
- Create: \`tests/test_create_nlp_comprehensive_notes.py\`.

**Interfaces:**
- Consumes: an input Markdown filename such as \`session-02-preparation-2026.md\`.
- Produces: \`infer_session_label(path: Path) -> str\` and \`default_output_for(path: Path) -> Path\`.

- [ ] **Step 1: Write failing tests for session inference**

\`\`\`python
from pathlib import Path
from scripts.create_nlp_comprehensive_notes import default_output_for, infer_session_label


def test_infer_session_label_from_curated_note():
    path = Path("lectures/session-02-preparation-2026.md")
    assert infer_session_label(path) == "Session 02"


def test_default_output_uses_session_number():
    path = Path("lectures/session-02-preparation-2026.md")
    assert default_output_for(path).name == "session-02-comprehensive-notes.pdf"
\`\`\`

- [ ] **Step 2: Run the focused tests and verify failure**

Run:

\`\`\`bash
/opt/homebrew/bin/python3.11 -m pytest tests/test_create_nlp_comprehensive_notes.py -q
\`\`\`

Expected: import failure because both functions are undefined.

- [ ] **Step 3: Implement reusable session inference**

Add:

\`\`\`python
def infer_session_label(path: Path) -> str:
    match = re.search(r"session[-_ ](\d+)", path.stem, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot infer session number from: {path.name}")
    return f"Session {int(match.group(1)):02d}"


def default_output_for(path: Path) -> Path:
    session = infer_session_label(path).lower().replace(" ", "-")
    return path.parent / "handouts" / f"{session}-comprehensive-notes.pdf"
\`\`\`

Pass the inferred label into \`NotesWriter\`, use it in the footer, and resolve the default output after parsing the input argument. Preserve \`--output\` override behaviour.

- [ ] **Step 4: Run tests and generator help**

\`\`\`bash
/opt/homebrew/bin/python3.11 -m pytest tests/test_create_nlp_comprehensive_notes.py -q
/opt/homebrew/bin/python3.11 scripts/create_nlp_comprehensive_notes.py --help
\`\`\`

Expected: tests pass and CLI help exits successfully.

- [ ] **Step 5: Commit renderer generalisation**

\`\`\`bash
git add scripts/create_nlp_comprehensive_notes.py tests/test_create_nlp_comprehensive_notes.py
git commit -m "refactor(36118): generalise lecture note renderer"
\`\`\`

## Task 3: Write the Source-Grounded Session 02 Notes

**Files:**
- Create: \`lectures/session-02-preparation-2026.md\`.
- Modify: \`lectures/session-02.md\`.

**Interfaces:**
- Consumes: slide text, slide visuals, all notebook Markdown/code cells, homework prompts, and archival Session 02 material for gap checking.
- Produces: numbered Markdown sections compatible with \`clean_markdown()\`.

- [ ] **Step 1: Extract source outlines**

Use \`pypdf\` for slide text and \`nbformat\` for notebook cell inventories. Record slide numbers and notebook/cell references in a temporary source map under \`tmp/pdfs/\`; do not include generated extraction files in Git.

- [ ] **Step 2: Render and inspect the current slide deck**

Render all pages with Poppler or PyMuPDF into \`tmp/pdfs/session-02-slides/\` and build a contact sheet. Inspect diagrams, equations, code, and visual-only slides that text extraction may miss.

- [ ] **Step 3: Compare 2026 with archived 2025 Session 02**

Create a temporary comparison containing only meaningful additions, removals, or reordered topics. The current deck wins every conflict. Add archival context only when it clarifies a current topic and label it as a Deep Dive.

- [ ] **Step 4: Draft numbered connected notes**

Follow the current teaching order. Each major method must cover purpose, representation, workflow, interpretation, evaluation, assumptions, and practical failure modes where supported. Preserve executable Python snippets in fenced blocks and define every formula symbol.

- [ ] **Step 5: Add notebook and homework synthesis**

For each notebook, explain what it does, why each major step exists, what outputs mean, and what the student should change or observe. End with source-grounded learning objectives and revision prompts.

- [ ] **Step 6: Run structural content checks**

\`\`\`python
required = [
    "## 1.", "## 2.", "Topic Modelling", "Text Clustering",
    "\`\`\`python", "Learning Objectives",
]
assert all(token in text for token in required)
assert "TBD" not in text and "TODO" not in text
\`\`\`

Also manually confirm every Deep Dive is relevant and unnumbered.

- [ ] **Step 7: Commit curated content**

\`\`\`bash
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-02-preparation-2026.md
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-02.md
git commit -m "docs(36118): write session 2 comprehensive notes"
\`\`\`

## Task 4: Render and Visually Verify the PDF

**Files:**
- Create: \`lectures/handouts/session-02-comprehensive-notes.pdf\`.

**Interfaces:**
- Consumes: \`session-02-preparation-2026.md\` and the reusable renderer.
- Produces: a Google Sans, single-spaced, visually verified PDF.

- [ ] **Step 1: Render the PDF**

\`\`\`bash
/opt/homebrew/bin/python3.11 scripts/create_nlp_comprehensive_notes.py llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-02-preparation-2026.md
\`\`\`

Expected: \`session-02-comprehensive-notes.pdf\` is created in \`lectures/handouts/\`.

- [ ] **Step 2: Run logical PDF checks**

Use \`pypdf\` to assert a non-zero page count, extract non-empty text from every page, and verify \`Session 02\`, \`Topic Modelling\`, \`Text Clustering\`, and \`Learning Objectives\` occur. Use \`pdffonts\` when available to confirm Google Sans and STIX math embedding.

- [ ] **Step 3: Render every final page to PNG**

\`\`\`bash
mkdir -p tmp/pdfs/session-02-final
pdftoppm -png -r 150 llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/handouts/session-02-comprehensive-notes.pdf tmp/pdfs/session-02-final/page
\`\`\`

If Poppler is unavailable, use PyMuPDF at equivalent resolution.

- [ ] **Step 4: Inspect every page and fix defects**

Check hierarchy, orphaned headings, parent/subsection spacing, paragraph spacing, code colours, equation alignment, clipping, black squares, and footer labels. Repeat render and inspection after every fix until no defects remain.

- [ ] **Step 5: Commit verified PDF**

\`\`\`bash
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/handouts/session-02-comprehensive-notes.pdf
git commit -m "docs(36118): render session 2 comprehensive notes"
\`\`\`

## Task 5: Update Indexes, Clean Downloads, and Final Audit

**Files:**
- Modify: lecture, notebook, handout, and current-semester source indexes from the file map.
- Delete after verification: the five exact Session 02 files in Downloads.

**Interfaces:**
- Consumes: verified source hashes and final PDF QA result.
- Produces: discoverable repository documentation and no duplicate Session 02 sources in Downloads.

- [ ] **Step 1: Update indexes and regeneration instructions**

Add current Session 02 links, notebook order, final PDF description, source status, and the exact renderer command. Do not mark subject outline or schedule items as received unless present.

- [ ] **Step 2: Run full scoped verification**

\`\`\`bash
/opt/homebrew/bin/python3.11 -m pytest tests/test_create_nlp_comprehensive_notes.py -q
git diff --check -- scripts/create_nlp_comprehensive_notes.py tests/test_create_nlp_comprehensive_notes.py llm-wiki/02-subjects/36118-applied-natural-language-processing
\`\`\`

Recompute all five repository-copy hashes and confirm they match the recorded source hashes.

- [ ] **Step 3: Remove only verified Downloads copies**

Delete these exact paths without globbing:

\`\`\`text
/Users/tuannm3812/Downloads/ANLP Session2_Week2-5.pdf
/Users/tuannm3812/Downloads/ANLP_Session_2_Part1_Text_Analysis.ipynb
/Users/tuannm3812/Downloads/ANLP_Session2_Part2_Topic_Modeling.ipynb
/Users/tuannm3812/Downloads/ANLP_Session2__Part3_TextClustering.ipynb
/Users/tuannm3812/Downloads/ANLP_Session_2_HW.ipynb
\`\`\`

Expected: those five paths are absent and unrelated Downloads files remain.

- [ ] **Step 4: Verify scoped Git state**

Run \`git status --short\`; preserve unrelated 36126, 36127, \`output/\`, and \`tmp/\` changes.

- [ ] **Step 5: Commit indexes**

\`\`\`bash
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/README.md
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/handouts/README.md
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/notebooks/README.md
git add llm-wiki/02-subjects/36118-applied-natural-language-processing/sources/current-semester-2026.md
git commit -m "docs(36118): index session 2 study materials"
\`\`\`

- [ ] **Step 6: Final handoff audit**

Confirm final PDF path, page count, source count, notebook count, test result, Downloads cleanup result, and commit list. Report remaining uncertainty without claiming completion beyond the evidence.
