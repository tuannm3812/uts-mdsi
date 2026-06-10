# Vault Structure

This vault is organized for three use cases: study in Obsidian, local LLM retrieval, and long-term maintenance in Git.

## Top-Level Folders

| Folder | Purpose |
|---|---|
| `00-admin/` | Vault operations, course map, import logs, setup notes, and maintenance rules. |
| `01-semesters/` | Semester-level planning and subject groupings. |
| `02-subjects/` | One folder per subject, with curated notes and raw copied materials. |
| `03-shared-concepts/` | Cross-subject concepts that should be linked from many subjects. |
| `04-assessments/` | Assessment calendar and future assessment-specific notes. |
| `05-literature-notes/` | Paper, textbook, documentation, and external reading notes. |
| `06-prompt-library/` | Reusable LLM prompts for study, review, coding, and synthesis. |
| `07-templates/` | Obsidian templates for subjects, concepts, and assessments. |
| `08-assets/` | Images, exported diagrams, screenshots, and other attachments. |

## Subject Folder Standard

Each subject uses the same internal structure:

| Folder | Purpose |
|---|---|
| `README.md` | Subject overview, source folder, concepts, assessments, and import summary. |
| `lectures/` | Curated weekly lecture notes and copied raw lecture materials. |
| `assignments/` | Assessment briefs, rubric checklists, draft reviews, and copied raw assessment files. |
| `notebooks/` | Notebook explanations, experiment notes, and copied raw notebooks. |
| `sources/` | Drive source inventory and source-level notes. |
| `questions/` | Tutor questions, exam drills, and unresolved questions. |

## Naming Rules

- Use lowercase kebab-case for file and folder paths.
- Keep subject folders as `{subject-code}-{short-subject-name}`.
- Keep durable notes as Markdown.
- Keep copied course files inside `raw/` folders.
- Do not rename raw imported files unless there is a specific reason; source filenames help trace back to Google Drive.
- Prefer concise, descriptive note names such as `week-03-model-evaluation.md` or `at2-rubric-checklist.md`.

## LLM Retrieval Rules

- Ask the LLM to use curated notes first.
- Use `raw/` files as source evidence, not as the main study interface.
- Large datasets, videos, archives, and model weights are referenced in inventories rather than copied.
- When an LLM answer matters for assessment, trace the claim back to a source file or official rubric.

