# Subject Onboarding Runbook

## Purpose

Use this for adding or refreshing one or more subjects from Google Drive with a safe, repeatable workflow.

## Single-subject refresh (recommended)

```bash
python3 scripts/import_drive_subjects.py --subject "36122-python-programming" --sync --summary
```

What this does:

- Imports copied files for the selected subject and updates the import manifest.
- Refreshes subject scaffolding for that subject:
  - learning layer files (`create_learning_layer.py`)
  - bucket READMEs and import summary references (`create_obsidian_indexes.py`)
- Prints compact status counts.

## Partial refresh of specific files only

If you only need vault scaffolding without copying files:

```bash
python3 scripts/create_learning_layer.py --subject "36122-python-programming"
python3 scripts/create_obsidian_indexes.py --subject "36122-python-programming"
```

For a read-only validation, use `--dry-run` with the import command:

```bash
python3 scripts/import_drive_subjects.py --subject "36122-python-programming" --dry-run --summary
```

## Naming and scope rules

- `--subject` uses repo folder slug(s): `36122-python-programming`.
- Multiple subjects can be passed: `--subject "36122-python-programming" "genai"`.
- `--subject-regex` is also supported for batch runs.
- Runbooks and checks should be done in the subject(s) listed above before any manual review.
