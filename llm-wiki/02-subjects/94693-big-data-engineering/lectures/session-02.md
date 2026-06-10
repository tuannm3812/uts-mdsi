---
type: lecture-note
subject: 94693-big-data-engineering
session: 2
status: draft
---

# Session 02 - Ingestion, Storage, and File Formats

## Source Files

- `lectures/raw/bde_slides/Big Data Engineering - Lecture 2.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied slide PDFs. Verify details against source files before using it for assessment.

## Study Objectives

- Summarise data ingestion patterns for structured and semi-structured inputs.
- Explain key storage decisions for lake, warehouse, and lakehouse structures.
- Map quality checks to ingestion and early-stage transformation.

## Likely Concepts

- storage: The physical and logical layer where data is persisted, versioned, and queried.
- big data architecture: A system design for processing and storing data at scale across multiple stages and services.
- query: A language-driven operation that retrieves, aggregates, or transforms data.
- quality: Checks and controls for correctness, consistency, completeness, and trustworthiness.
- spark: A distributed compute platform commonly used for scalable batch and streaming analytics.
- reproducibility: The ability to re-run analysis or pipelines and obtain verifiable, auditable results.

## Extracted Keywords

- data
- warehouse
- model
- inmon
- approach
- layer
- kimball
- organization
- business
- source
- marts
- sources

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
