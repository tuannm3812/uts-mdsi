# LLM Wiki Content Contracts

## Scope

These contracts define minimum required structure for files created by the wiki workflows and templates in this repository.

## Subject Index (`02-subjects/*/README.md`)

Required frontmatter:

```yaml
type: subject-index
status: active
```

Optional frontmatter:

```yaml
semester: SemX YYYY Term
code: "36100"
name: Human-readable subject name
source_root: /abs/path/to/drive/folder
```

Required sections in the file body:

- `## Folder Convention`
- `## What This Subject Is About`
- `## Source Subfolders`
- `## Key Concepts`
- `## Assessments`
- `## Curated Study Layer`
- `## Import Summary`

## Assessment Planning (`.../assignments/assessment-planning.md`)

Required frontmatter:

```yaml
type: assessment
subject: <subject-folder-name>
code: <numeric-code-or-name>
status: planning
```

Required sections in the file body:

- `# <subject> Assessment Planning` title
- Canonical AT workflow description line
- AT links:
  - `AT1` (`at1.md`)
  - `AT2` (`at2.md`)
  - `AT3` (`at3.md`)
  - Use only the AT files that are present for the subject.

## Assessment Dashboard (`.../assignments/README.md`)

Required structure:

- heading + quick overview
- `## Assessment Pages`
- `## Standard Review Workflow`
- `## Source Count` or `## Raw Imports`
- `## Raw Imports` (or keep as alias of source count block)
- `## LLM Review Prompt`

## Concept Pages (`03-shared-concepts/*.md`)

Required frontmatter:

```yaml
type: concept
status: active
topics:
  - topic-1
```

Required sections:

- `## Definition`
- `## Why It Matters In This Master's`
- `## Connected Subjects`
- `## Sources`

## Revision / Safety Policy for Unknown Fields

- Unknown top-level frontmatter keys are allowed.
- New mandatory fields should be introduced only in a plan update and accompanied by migration notes.
- Templates should keep examples minimal and concrete; avoid placeholders that look like production content.

## Template Use Notes

- Always generate pages from these templates so the minimum structure exists before subject-specific edits.
- If content is imported and does not match contracts exactly, keep a short migration note in `llm-wiki/00-admin/import-summary.md`.
