---
type: lecture-note
subject: 94693-big-data-engineering
session: 7
status: draft
---

# Session 07 - Cost, Performance, and Scaling Trade-Offs

## Source Files

- `lectures/raw/bde_slides/Big Data Engineering - Lecture 7.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied slide PDFs. Verify details against source files before using it for assessment.

## Study Objectives

- Evaluate performance trade-offs and resource scaling options.
- Identify bottlenecks in compute, I/O, and orchestration.
- Estimate how choices affect reliability and execution cost.

## Likely Concepts

- streaming: Continuous processing of events with low-latency ingestion and near-real-time outputs.
- big data architecture: A system design for processing and storing data at scale across multiple stages and services.
- batch processing: Periodic processing of data in groups, usually on a schedule rather than in event-time.
- spark: A distributed compute platform commonly used for scalable batch and streaming analytics.
- monitoring: Operational visibility into workflow success, latency, failures, and data drift.
- performance: How quickly and efficiently a system handles data volume, complexity, and concurrency.
- pipeline: A chain of dependent tasks that moves, transforms, validates, and delivers data and insights.
- storage: The physical and logical layer where data is persisted, versioned, and queried.

## Extracted Keywords

- data
- streaming
- real-time
- apache
- processing
- streams
- process
- provides
- stream
- used
- user
- kafka

## What To Understand

- Which data assumptions each lesson makes (source freshness, schema, and quality).
- How architecture, storage, and compute choices affect cost and reliability.
- Where observability and rollback checkpoints are most valuable.
- Which part of this session maps to assignment deliverables.

## Assessment Relevance

- Use these notes when mapping lecture ideas to assignment solutions and project architecture.
- Turn this session into 1–2 concrete design choices with justifications.

## Revision Questions

- What production risk does this topic add if implemented incorrectly?
- Which trade-off (cost, latency, quality, or reliability) is most likely in this session?
- What evidence from the slides directly supports your design decisions?

## LLM Follow-Up Prompt

Using the source files listed above, expand this into an assessment-ready study note with pipeline examples, failure modes, and design alternatives.
