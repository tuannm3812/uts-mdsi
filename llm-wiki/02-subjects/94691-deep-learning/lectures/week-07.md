---
type: lecture-note
subject: 94691-deep-learning
week: 7
status: draft
---

# Week 07 - Transfer Learning, ResNet, and Inception

## Source Files

- `lectures/raw/deep_learning_slide/Deep Learning - Lecture 7.pdf` (lecture)
- `lectures/raw/deep_learning_slide/Note/94691 DL - Module 7 - Note.pdf` (lecture)
- `lectures/raw/deep_learning_slide/Note/Deep Learning - Lecture 7 - Note.pdf` (lecture)
- `lectures/raw/deep_learning_slide/dl_slide_2025/Deep Learning - Lecture 7.pptx.pdf` (lecture)
- `notebooks/raw/dl_notebooks/Deep Learning_Lab7_Exercise1_Solutions.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/Deep Learning_Lab7_Exercise2_Solutions.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/Deep Learning_Lab7_Exercise3_Solutions.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7-Checkpointing-TransferLearning-Solution-AWS.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7-Checkpointing-TransferLearning-Solution.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7-Inception-GoogleNet-CNNs-AWS.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7-Inception-GoogleNet-CNNs-Solution-Colab.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7-Residual-Block-ResNet-CNNs-Solution-Colab.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_7/Week7_Checkpointing_TransferLearning-AWS.ipynb` (notebook)

## Working Summary

This note was generated from copied lecture PDFs and notebooks. Treat it as a first-pass study map: verify details against the source files before using it for assessment.

## Study Objectives

- Use pretrained CNNs through transfer learning and fine-tuning.
- Explain residual connections and why they help deep networks train.
- Compare ResNet and Inception-style architectures at a high level.

## Likely Concepts

- computer vision: Methods for representing, analysing, and modelling images or visual data.
- pytorch: A Python deep learning framework used to define tensors, neural network modules, losses, optimisers, and training loops.
- image captioning: A multimodal task that generates text descriptions for images, often using an image encoder and text decoder.
- optimisation: The process of updating model parameters, often with SGD or Adam, to reduce the loss function.
- activation function: A nonlinear function such as ReLU, sigmoid, tanh, or softmax that lets neural networks model non-linear relationships.
- inception: A CNN architecture pattern that combines multiple convolutional filter sizes to capture features at different scales.
- transfer learning: Reusing a pretrained model or representation for a new task, often by freezing or fine-tuning selected layers.
- convolutional neural network: A neural architecture that uses convolutional filters to learn spatial features from image-like inputs.

## Extracted Keywords

- import
- keras
- training
- input
- images
- code
- generator
- train
- function
- dataset
- task
- step

## What To Understand

- What problem this week's models or methods solve.
- What assumptions the method makes about data, labels, architecture, or training.
- How the method is implemented in PyTorch or notebook code.
- How performance should be evaluated and diagnosed.

## Assessment Relevance

- Supports Assignment 2 through transfer learning, pretrained models, ResNet/Inception, and fine-tuning decisions.
- Link useful source files to the relevant assessment page.

## Revision Questions

- Explain the main model or method from this week in plain language.
- What are the key hyperparameters or design choices?
- What failure modes should be checked?
- How would you evaluate whether the model is working?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, formulas, PyTorch implementation details, examples, and likely assessment relevance. Keep all claims traceable to source files.
