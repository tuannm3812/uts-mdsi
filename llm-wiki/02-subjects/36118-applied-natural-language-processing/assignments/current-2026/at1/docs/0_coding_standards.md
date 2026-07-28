# AT1 Coding Standards

These rules adapt the repository's master coding standard to the 36118 AT1
deliverables and marking rubric.

## 1. Deliverable Shape

- Keep one numbered, end-to-end notebook:
  `notebooks/1_skilled_migration_text_analysis.ipynb`.
- Treat the notebook as both executable analysis and report. Every important
  output must be followed by interpretation.
- Keep supplied PDFs in the ignored `data/` directory. Do not duplicate raw
  data or embed the full corpus in Git.
- Export the final notebook to PDF only after a clean restart-and-run.

## 2. Reproducibility

- Use the registered **Python 3.11 (NLP)** kernel.
- Install the pinned dependency ranges in `requirements-at1.txt`.
- Use relative, automatically detected paths; never include a personal home
  directory in notebook code.
- Keep all configuration in one cell, including seed, thresholds, figure
  settings, and theme definitions.
- The submitted notebook must run offline. Do not download tokenisers, models,
  or web metadata during execution.
- Preserve submission identifiers exactly. Do not infer missing sequence
  numbers or merge supplement files.

## 3. Code Quality

- Follow PEP 8 and group standard-library and third-party imports.
- Add type hints and Google-style docstrings to reusable functions.
- Give functions one clear responsibility: inventory, extraction, cleaning,
  measurement, or plotting.
- Catch PDF-level failures and record them instead of terminating the corpus
  run.
- Suppress noisy library diagnostics only when the underlying issue is
  captured by an explicit quality measure.

## 4. Analysis Quality

- Begin with a focused research question and explain why each method helps
  answer it.
- Audit extraction before cleaning or modelling. Flag documents with fewer
  than 500 extracted characters for manual inspection or OCR.
- Keep original text and cleaned tokens conceptually separate.
- Report both document prevalence and length-normalised frequency. Raw keyword
  totals alone over-weight long submissions.
- Treat dictionary matching as transparent exploratory measurement, not as
  sentiment, stance, or proof of policy support.
- Verify representative excerpts against the source PDF before using them in
  final claims.
- Include limitations, sensitivity checks, and unanswered questions.

## 5. Presentation

- Use numbered Markdown sections and concise prose.
- Use a print-friendly white background and the colour-blind-safe **Viridis**
  palette.
- Every figure needs a descriptive title, labelled axes, units, and a nearby
  interpretation.
- Prefer compact tables and charts over large raw outputs.
- Do not include a method simply because it appeared in an older report.

## 6. Git and Submission Checks

- Keep only source notebooks, small documentation, and dependency files in
  Git. Raw data stays ignored.
- Before committing, validate notebook JSON, restart and run all cells, and
  inspect the diff for unintended files or private paths.
- Use a scoped Conventional Commit, for example:
  `feat(36118): build AT1 text analysis baseline`.
- Before submission, export and inspect the PDF for clipped code, tables, and
  figures; submit the `.ipynb` and `.pdf` as separate files.
