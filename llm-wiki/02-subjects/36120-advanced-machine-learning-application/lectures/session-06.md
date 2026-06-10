---
type: lecture-note
subject: 36120-advanced-machine-learning-application
session: 6
status: draft
---

# Session 06 - Ensemble, Calibration, and Performance Diagnostics

## Source Files

- `lectures/raw/advml_slides_25sp/36120-25SP-Advanced ML Application-Lecture06.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied lecture PDFs and notebook-linked teaching materials. Verify all details against source files before using this for assessment.

## Study Objectives

- Compare ensemble methods for variance and bias control.
- Use calibration and probability checks before interpretation.

## Likely Concepts

- experiment tracking: Systematic logging of setup, code, and outputs for review and audit.
- model evaluation: Measuring model quality using metrics aligned to a defined objective and failure cost.
- feature engineering: Transforming raw inputs into forms that improve model signal and stability.
- class imbalance: When target classes are not equally represented and metrics can mislead.
- reproducibility: Ability to re-run an experiment and obtain consistent outcomes.
- data leakage: Including information unavailable at prediction time, producing inflated validation scores.
- time-series: Data indexed by time where ordering and dependencies constrain validation strategy.

## Extracted Keywords

- performance
- importance
- models
- features
- feature
- interpretation
- helps
- process
- permutation
- analysis
- understand
- predictions

## What To Understand

- Which target variable and task type this lesson is designed for.
- The assumptions behind each model and split strategy.
- How metrics map to practical decisions.
- What risks could invalidate the reported results.

## Assessment Relevance

- Link this session to AT1/AT2/AT3 evidence using [the assignment evidence map](../assignments/evidence-map.md).
- Turn each high-signal slide section into a concise claim with source evidence.

## Revision Questions

- What is the modelling objective and what data constraints are explicit?
- Which evaluation metric is most honest for this task and why?
- What is a likely leakage source, and how would you prevent it?
- Which model choice is justified by this session’s assumptions?

## LLM Follow-Up Prompt

Using the source files listed above, expand this first-pass note into a precise study note with task examples, metric trade-offs, and assessment-relevant implications.
