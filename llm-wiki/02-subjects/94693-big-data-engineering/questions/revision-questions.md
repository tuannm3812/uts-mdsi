---
type: question-bank
subject: 94693-big-data-engineering
code: 94693
status: draft
---

# 94693 Big Data Engineering - Revision Questions

## Conceptual Questions

- What is the practical difference between a lake, a warehouse, and a lakehouse in a data pipeline design?
- Why is partitioning important for cost and query performance?
- How does DAG design support reliability and reproducibility?
- How do you decide whether a component should be batch or streaming?
- What does pipeline observability include beyond basic logging?

## Applied Questions

- Draft a pipeline design for a trending-analytics dataset that can scale from one region to multiple regions.
- Choose between at least two storage layouts for the same workload and justify the trade-offs.
- Build a checkpoint and retry strategy for a multi-stage notebook workflow.
- Design a quality gate before loading raw CSV/JSON into analytical tables.
- Sketch a failure-handling approach for a dropped stage in batch processing.

## Technical Questions

- Given a notebook with imports and markdown comments, list five lines you would inspect to confirm reproducibility.
- Which SQL clause patterns best reduce unnecessary table scans at scale?
- How would you profile a slow Spark-style transformation?
- Which indicators tell you a data migration job is dropping records?
- How do you document data lineage for assessment defensibility?

## LLM Prompt

Using these concepts and the curated lecture notes, generate:
- a 10-question viva-style exam set,
- a short model answer key,
- and a scoring rubric with common failure modes.

- big data architecture
- pipeline
- data lake
- streaming
- batch processing
- storage
- query
- quality
- monitoring
- performance
- spark
- reproducibility
