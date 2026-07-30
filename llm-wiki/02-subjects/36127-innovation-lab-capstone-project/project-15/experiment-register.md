# Project 15 Experiment Register

## Purpose

Use this register for every smoke test, baseline run, harness comparison, ablation, and final trial. Configuration must be recorded before interpreting results.

## Immutable run metadata

Record these values in the experiment configuration or linked artifact:

- experiment and trial ID;
- timestamp and operator;
- Git commit;
- Terminal-Bench dataset name and revision;
- Harbor version;
- harness name and version;
- model and provider;
- reasoning effort and sampling settings;
- prompt version or hash;
- tool configuration;
- context policy;
- verification and retry policy;
- task split;
- trial count;
- timeout and resource settings;
- network policy;
- environment or sandbox provider; and
- secrets supplied by name only, never by value.

## Experiment table

| ID | Date | Owner | Reviewer | Hypothesis | Split | Control | Changed variable | Trials | Accuracy | Tokens | Cost | Runtime | Status | Artifact/trajectory |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| EXAMPLE-001 | 5 Aug 2026 | Member 1 | Member 5 | Oracle smoke test confirms Harbor can fetch, build, execute, and verify tasks | First five tasks | N/A | Infrastructure only | 5 | Record result | Record result | Record result | Record result | Example - remove after first real run | Link job directory |

## Trial-level results

| Experiment ID | Trial ID | Task | Harness | Model | Result | Reward | Input tokens | Output tokens | Cost | Runtime | Retries | Error | Failure category | Trajectory |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Failure taxonomy

| Category | Use when | Do not confuse with |
|---|---|---|
| Specification | Required format, path, method, or constraint was violated | A defective verifier |
| Repetition | Ineffective action pattern recurred without new evidence | A justified retry with changed diagnosis |
| Premature completion | Agent stopped without satisfying or checking core requirements | Budget exhaustion |
| Hallucination/guessing | Unsupported result was substituted for required evidence | A documented uncertainty |
| No verification | No relevant core check was observed | Weak verification |
| Weak verification | A check occurred but did not cover required properties | Official verifier success |
| Reasoning-action mismatch | Claims contradicted commands, errors, or artifacts | A later failure that was acknowledged |
| Context failure | Necessary state was lost or context capacity was exceeded | Provider outage |
| Tool/parser failure | Requested action could not be parsed or executed by the custom interface | Incorrect command produced by the model |
| Infrastructure | Docker, Harbor, storage, or orchestration failed | Model reasoning failure |
| Provider | Authentication, rate limit, or model service failed | Harness parser failure |
| Benchmark/verifier | Task environment or official check was defective or unstable | Agent failure |
| Budget exhaustion | Agreed token, time, turn, or cost limit was reached | Premature completion |

## Experiment decision record

| Experiment ID | Result summary | Practical significance | Validity concerns | Decision | Follow-up owner | Evidence |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

## Comparison checklist

Before comparing two conditions, confirm:

- [ ] Same Terminal-Bench dataset revision
- [ ] Same task subset
- [ ] Same model identifier
- [ ] Same reasoning effort and sampling controls
- [ ] Same resource and timeout limits
- [ ] Same network policy
- [ ] Same trial count
- [ ] Same infrastructure class
- [ ] Exactly one intended harness variable changed
- [ ] Failed infrastructure trials handled consistently
- [ ] Raw trajectories retained
- [ ] Cost and token definitions are comparable

## Development-to-final freeze

Before the full evaluation:

- [ ] Select the final configuration using the agreed rule
- [ ] Tag the source commit
- [ ] Freeze dependencies and prompt
- [ ] Freeze tool, context, verification, and retry settings
- [ ] Estimate full-run cost
- [ ] Confirm API/compute approval
- [ ] Confirm rerun policy
- [ ] Confirm leaderboard requirements
- [ ] Test result export and backup
- [ ] Record mentor/client approval

