---
type: lecture-note
subject: 94693-big-data-engineering
session: 1
status: draft
---

# Session 01 - Big Data Engineering Framing and Architecture

## Source Files

- `lectures/raw/bde_slides/Big Data Engineering - Lecture 1.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied slide PDFs. Verify details against source files before using it for assessment.

## Study Objectives

- Explain why big data architecture uses layered storage and processing approaches.
- Differentiate batch and stream orientation in data movement.
- Identify common reliability and correctness risks in distributed pipelines.

## Likely Concepts

- big data architecture: A system design for processing and storing data at scale across multiple stages and services.
- data lake: A central repository that stores raw and processed data in a flexible, scalable layout.
- streaming: Continuous processing of events with low-latency ingestion and near-real-time outputs.
- query: A language-driven operation that retrieves, aggregates, or transforms data.
- monitoring: Operational visibility into workflow success, latency, failures, and data drift.
- pipeline: A chain of dependent tasks that moves, transforms, validates, and delivers data and insights.
- storage: The physical and logical layer where data is persisted, versioned, and queried.
- spark: A distributed compute platform commonly used for scalable batch and streaming analytics.

## Extracted Keywords

- data
- docker
- container
- engineering
- applications
- your
- application
- image
- team
- shipping
- running
- code

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
