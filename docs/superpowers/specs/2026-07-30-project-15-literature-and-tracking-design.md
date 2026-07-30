# Project 15 Literature and Tracking Design

## Purpose

Prepare the six-member 36127 Capstone team to deliver Project 15, **Build a Custom Harness and Beat an Established One on Terminal-Bench**, through:

1. a detailed, readable literature-summary PDF; and
2. Markdown-based team and individual tracking logs maintained in GitHub.

The artifacts must support technical preparation, equitable workload allocation, weekly contribution evidence, client meetings, assessment writing, and reproducible experiments.

## Source material

The literature summary will synthesise these five verified papers:

1. *Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces*
2. *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering*
3. *OpenHands: An Open Platform for AI Software Developers as Generalist Agents*
4. *Agentless: Demystifying LLM-based Software Engineering Agents*
5. *The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents*

It will also distinguish Terminal-Bench 2.0, discussed in the original paper, from Terminal-Bench 2.1, required by the project brief. Terminal-Bench 2.1 keeps the 89-task structure while correcting benchmark problems identified after the 2.0 release.

## Literature-summary deliverables

### Editable source

Create a Markdown source under:

`llm-wiki/02-subjects/36127-innovation-lab-capstone-project/research/`

### PDF

Create a polished PDF in the same research directory and copy the final PDF into:

`36127 Innovation Lab Capstone Project/03 Project 15 - Terminal-Bench/`

inside the locally synced Google Drive subject folder.

### Required content

The literature summary will contain:

1. Project context and objectives
2. Executive summary
3. Key terminology
4. Detailed summary of each paper
5. Cross-paper thematic synthesis
6. Implications for the custom harness
7. Recommended experimental variables
8. Proposed evaluation framework
9. Failure taxonomy
10. Reproducibility and cost considerations
11. Research questions and hypotheses
12. Six-member reading and research allocation
13. Recommended reading order
14. References with stable URLs

The writing must separate evidence reported by the papers from recommendations inferred for the Capstone project.

## PDF presentation

The PDF will use:

- an A4 page size;
- consistent title, heading, body, table, and callout styles;
- page numbers and a concise footer;
- readable margins and line spacing;
- tables that remain within page boundaries;
- human-readable source links;
- no clipped, overlapping, or malformed content.

The final PDF must be rendered to page images and visually inspected before delivery.

## Markdown tracking system

Create the tracking material under:

`llm-wiki/02-subjects/36127-innovation-lab-capstone-project/project-15/`

### Team tracker

`team-task-tracker.md` will contain:

- project milestones for Weeks 1-12;
- a task table with task ID, workstream, description, primary owner, reviewer, planned week, due date, priority, status, evidence link, and dependencies;
- equal initial allocation across six placeholder members;
- rotating secondary responsibilities;
- client and mentor meeting preparation;
- report and presentation responsibilities;
- a definition of done;
- weekly workload-balancing checks.

### Individual contribution log

`individual-contribution-log-template.md` will contain:

- week and reporting period;
- individual role and responsibilities;
- planned tasks;
- completed work;
- hours;
- contribution to team progress;
- challenges and resolutions;
- decisions or learning;
- next-week plan;
- evidence links;
- meeting and communication participation;
- self-review against the official contribution criteria.

The template must align with the documented contribution weights:

- task completion: 30%;
- evidence quality and quantity: 35%;
- meetings and communication: 20%;
- reflection, planning, and professionalism: 15%.

### Experiment register

`experiment-register.md` will capture:

- experiment ID and hypothesis;
- Terminal-Bench dataset version;
- Harbor and harness versions;
- model and reasoning configuration;
- development or final task split;
- controlled and changed variables;
- number of trials;
- accuracy, token use, cost, runtime, retries, and errors;
- failure category;
- artifact and trajectory links;
- conclusion and follow-up decision.

### Meetings and decisions

`meeting-and-decision-log.md` will capture:

- date, meeting type, attendees, and purpose;
- discussion notes;
- decisions and rationale;
- actions, owners, reviewers, and due dates;
- unresolved questions;
- evidence links.

## Schedule alignment

The tracker will use the confirmed subject calendar:

| Week | Date | Required focus |
|---|---|---|
| 1 | 29 Jul 2026 | Team setup, project understanding, literature allocation, mentor questions |
| 2 | 5 Aug 2026 | Mentor meeting, environment feasibility, benchmark smoke test |
| 3 | 12 Aug 2026 | Architecture decision, baseline design, experiment protocol |
| 4 | 19 Aug 2026 | Mentor review, baseline implementation and initial results |
| 5 | 26 Aug 2026 | Early progress meeting with client |
| 6 | 2 Sep 2026 | Custom harness version 1 and controlled experiments |
| 7 | 9 Sep 2026 | Midpoint review meeting with client |
| 8 | 16 Sep 2026 | Refined harness, ablations, failure analysis |
| STUVAC | 23 Sep 2026 | Consolidation, contingency work, report drafting |
| 9 | 30 Sep 2026 | Pre-final client meeting and design freeze |
| 10 | 7 Oct 2026 | Full evaluation, statistical analysis, final report |
| 11 | 14 Oct 2026 | Final presentation |
| 12 | 21 Oct 2026 | iLab Showcase and final handover |

## Six-member allocation model

Use three primary pairs:

- Pair A: Harbor environment and established baselines
- Pair B: custom harness and agent behaviour
- Pair C: evaluation, analysis, and documentation

Initial primary ownership will be distributed across Members 1-6, with each task assigned a separate reviewer. Secondary responsibilities will rotate at milestone boundaries so every member contributes to technical work, evaluation, writing, and presentation.

Workload equality will be reviewed weekly using:

- planned versus completed tasks;
- approximate hours;
- difficulty and responsibility;
- evidence quality;
- review and meeting contributions;
- upcoming workload.

Equal contribution means comparable effort and accountability, not identical task counts.

## Repository and Git constraints

- Preserve unrelated user changes already present in the worktree.
- Commit only Project 15 literature, tracking, and directly related index updates.
- Do not add downloaded third-party papers to Git unless explicitly required; keep them in Google Drive.
- Validate Markdown links and formatting.
- Push the scoped commit to the current `main` branch only after artifact verification.

## Acceptance criteria

The work is complete when:

1. the detailed Markdown literature review is accurate and source-backed;
2. the PDF renders without visual defects;
3. the final PDF is present in the synced Google Drive Project 15 folder;
4. all four Markdown trackers are populated and aligned with Weeks 1-12;
5. six-member ownership and review responsibilities are balanced;
6. contribution-evidence requirements are explicit;
7. Git contains only the intended Project 15 changes in the new commit; and
8. the commit is successfully pushed to `origin/main`.
