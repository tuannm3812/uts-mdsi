# Obsidian Setup

Open this folder as the vault:

`/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/My Drive/10_Github/1. Study/uts-mdsi/llm-wiki`

```bash
# If this is a new session, launch Obsidian directly:
./00-admin/open-obsidian-vault.sh
```

If the launch script fails:

- run `open -a Obsidian <vault-path>` on macOS, or
- open Obsidian manually and point it to the vault path in section 1.

## Navigation

- Start at [Vault Home](../README.md).
- Use [Course Map](course-map.md) for the whole degree.
- Use [Subjects](../02-subjects/README.md) to jump into a subject folder.
- Use each subject's `sources/drive-source-inventory.md` to see copied and referenced Drive files.

## Raw Files

The `raw/` folders contain copied course files. Large datasets, archives, model weights, and videos are not copied; they are referenced in the import manifest and subject inventories.

## Suggested Workspace Layout

Recommended first-run layout (split pane):

- Left pane: `02-subjects/` (browse by subject)
- Right pane: `03-shared-concepts/` (link into reusable concepts)
- Bottom pane: `06-prompt-library/` (keep prompts available while studying)

Example:

1. Open **UTS Master's LLM Wiki**.
2. Open `02-subjects/36122-python-programming/README.md` in the left pane.
3. Open `03-shared-concepts/` or a concept note in the right pane.
4. Open `00-admin/llm-wiki-workflow.md` in the lower pane.

If your Obsidian install uses workspace snapshots, save this layout as the default workspace after first setup.

## Graph View Settings (for cross-links)

In Graph View, enable:

- Outgoing links to show
- Backlinks to show
- Orphans
- Detached nodes
- Minimum tags: `1`
- Hide local files (optional): disable for broad cross-link discovery
- Filter by tag patterns:
  - `subject-index`
  - `concept`
  - `assessment`
  - `learning-map`

Use graph filters to quickly identify topics with weak linking coverage.

## Query Snippets

If you use Dataview:

```dataview
TABLE file.link AS "Subject Page", subject, code
FROM "02-subjects"
WHERE type = "subject-index" AND status = "active"
SORT file.name ASC
```

```dataview
LIST file.link
FROM "02-subjects"
WHERE contains(file.name, "learning-map") OR contains(file.name, "assignment")
SORT file.mtime DESC
LIMIT 30
```

If Dataview is not installed, keep these as manual search patterns:

- Use `tag:#subject-index` style in search.
- Filter path: `02-subjects` and sort by `File name`.
- Filter path: `03-shared-concepts` to inspect concept coverage.

## Naming and Linking Conventions

- Subject index pages are `README.md` files with a human-readable title in frontmatter.
- Suggested reusable note names: `week-XX-topic.md`, `at2-rubric-checklist.md`, `revision-questions.md`.
- Concept notes: `kebab-case.md` where stable concepts map cleanly across subjects (`bayesian-thinking.md`).
- Keep one canonical subject-level path per concept to avoid duplicate aliases.
