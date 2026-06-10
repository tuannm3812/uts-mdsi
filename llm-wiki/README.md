---
type: vault-home
status: active
---

# UTS Master's LLM Wiki

This is a persistent Markdown knowledge base for your UTS master's course. It is based on the subject folders in:

`/Users/tuanm.nguyen/Library/CloudStorage/GoogleDrive-tuannm3812@gmail.com/My Drive/01_Study/0. Master/6. UTS Drive`

Use it with an LLM as a course tutor, synthesis engine, assignment reviewer, and revision partner. The Drive folder remains the source of raw course files; this repo is the curated wiki layer.

## Start Here

- [Course Map](00-admin/course-map.md)
- [LLM Wiki Workflow](00-admin/llm-wiki-workflow.md)
- [Vault Structure](00-admin/vault-structure.md)
- [Assessment Calendar](04-assessments/assessment-calendar.md)
- [Master Prompts](06-prompt-library/master-prompts.md)

## Semesters

- [Sem1 2025 Autumn](01-semesters/sem1-2025-autumn.md)
- [Sem2 2025 Spring](01-semesters/sem2-2025-spring.md)
- [Sem3 2026 Autumn](01-semesters/sem3-2026-autumn.md)
- [Sem4 2026 Spring](01-semesters/sem4-2026-spring.md)

## Subjects

- [36100 Data Science for Innovation](02-subjects/36100-data-science-for-innovation/README.md)
- [36103 Statistical Thinking for Data Science](02-subjects/36103-statistical-thinking-for-data-science/README.md)
- [36104 Data Visualisation and Narratives](02-subjects/36104-data-visualisation-and-narratives/README.md)
- [36106 Machine Learning Algorithms and Applications](02-subjects/36106-machine-learning-algorithms-and-applications/README.md)
- [36118 Applied Natural Language Processing](02-subjects/36118-applied-natural-language-processing/README.md)
- [36120 Advanced Machine Learning Application](02-subjects/36120-advanced-machine-learning-application/README.md)
- [36121 Artificial Intelligence Principles and Applications](02-subjects/36121-artificial-intelligence-principles-and-applications/README.md)
- [36122 Python Programming](02-subjects/36122-python-programming/README.md)
- [43008 Reinforcement Learning](02-subjects/43008-reinforcement-learning/README.md)
- [94691 Deep Learning](02-subjects/94691-deep-learning/README.md)
- [94692 Data Science Practice](02-subjects/94692-data-science-practice/README.md)
- [94693 Big Data Engineering](02-subjects/94693-big-data-engineering/README.md)
- [GenAI](02-subjects/genai/README.md)

## Operating Rules

- Every important claim should trace back to lecture material, readings, code, assignment specs, or your verified work.
- Use the LLM to explain, compare, quiz, critique, and restructure your thinking.
- Do not paste unverified LLM output directly into assignments.
- Put reusable concepts in `03-shared-concepts/`, not only in subject notes.
- Put assessment rubrics and due dates in `04-assessments/`.

## Imported Drive Files

Readable course files are copied into each subject folder under:

- `lectures/raw/`
- `assignments/raw/`
- `notebooks/raw/`
- `sources/raw/`

Large binaries, model weights, videos, archives, and large datasets are referenced instead of copied. The full import log is in [00-admin/drive-import-manifest.csv](00-admin/drive-import-manifest.csv), and each subject has a `sources/drive-source-inventory.md` file.

To rerun a selected subject import and refresh onboarding scaffolding:

```bash
python3 scripts/import_drive_subjects.py --subject "36122-python-programming" --sync
```

To update only scaffolding for one or more subjects (no file copies):

```bash
python3 scripts/create_learning_layer.py --subject "36122-python-programming"
python3 scripts/create_obsidian_indexes.py --subject "36122-python-programming"
```
