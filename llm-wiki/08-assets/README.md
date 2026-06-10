# Assets

Use this folder for all non-source study artefacts used by notes in this vault, such as:

- screenshots
- exported notebooks
- diagrams
- course hand-drawn sketches
- generated tables or charts

## Folder Pattern

- `08-assets/raw-imports/` for transient material that still needs cleanup.
- `08-assets/<subject-folder>/` for subject-specific attachments.
- `08-assets/shared-concepts/` for visual aids reused across subjects.

## Naming Pattern

Prefer short, stable names:

- `08-assets/36122-python-programming/attention-overview.png`
- `08-assets/94693-big-data-engineering/bde-workflow-diagram.svg`
- `08-assets/shared-concepts/model-eval-precision-recall.png`

Guidelines:

- Use lowercase kebab-case.
- Include a stable context when needed: `subject-code-topic-variant-v2.ext`.
- Prefer `.png`/`.jpg` for screenshots and `.pdf` for handouts or long visual references.
- Avoid duplicating large source files that already exist in subject `raw/` folders.
- Link attachments with relative Markdown paths from notes, for example:
  
  ```markdown
  ![[../../08-assets/36122-python-programming/confusion-matrix.svg]]
  ```
