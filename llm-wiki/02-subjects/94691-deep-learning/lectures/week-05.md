---
type: lecture-note
subject: 94691-deep-learning
week: 5
status: draft
---

# Week 05 - Convolutional Neural Networks

## Source Files

- `lectures/raw/deep_learning_slide/Deep Learning - Lecture 5.pdf` (lecture)
- `lectures/raw/deep_learning_slide/Note/94691 DL - Module 5 - Note.pdf` (lecture)
- `lectures/raw/deep_learning_slide/Note/Deep Learning - Lecture 5 - Note.pdf` (lecture)
- `lectures/raw/deep_learning_slide/dl_slide_2025/Deep Learning - Lecture 5.pptx.pdf` (lecture)
- `notebooks/raw/dl_notebooks/Deep Learning_Lab5_Exercise1_Solutions.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/Deep Learning_Lab5_Exercise2_Solutions.ipynb` (notebook)
- `notebooks/raw/dl_notebooks/dl_notebooks_2025/week_5/Week5-ConvolutionalNeuralNetworks(CNNs)-Solution.ipynb` (notebook)

## Working Summary

This note was generated from copied lecture PDFs and notebooks. Treat it as a first-pass study map: verify details against the source files before using it for assessment.

## Study Objectives

- Explain why convolution is effective for image data.
- Track feature maps through convolution, pooling, and classifier layers.
- Implement and evaluate CNN models in PyTorch.

## Likely Concepts

- neural network: A model made of layers of learned parameters that transform inputs into predictions through nonlinear functions.
- pytorch: A Python deep learning framework used to define tensors, neural network modules, losses, optimisers, and training loops.
- activation function: A nonlinear function such as ReLU, sigmoid, tanh, or softmax that lets neural networks model non-linear relationships.
- computer vision: Methods for representing, analysing, and modelling images or visual data.
- convolutional neural network: A neural architecture that uses convolutional filters to learn spatial features from image-like inputs.
- loss function: The objective being minimised during training, such as cross-entropy for classification or mean squared error for regression.
- optimisation: The process of updating model parameters, often with SGD or Adam, to reduce the loss function.
- regularisation: Techniques that reduce overfitting, including dropout, weight decay, data augmentation, and early stopping.

## Extracted Keywords

- sequence
- import
- train
- time
- neural
- function
- training
- input
- dataset
- test
- networks
- output

## What To Understand

- What problem this week's models or methods solve.
- What assumptions the method makes about data, labels, architecture, or training.
- How the method is implemented in PyTorch or notebook code.
- How performance should be evaluated and diagnosed.

## Assessment Relevance

- Supports Assignment 1 and Assignment 2 where CNN design, training, and diagnostics are central.
- Link useful source files to the relevant assessment page.

## Revision Questions

- Explain the main model or method from this week in plain language.
- What are the key hyperparameters or design choices?
- What failure modes should be checked?
- How would you evaluate whether the model is working?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, formulas, PyTorch implementation details, examples, and likely assessment relevance. Keep all claims traceable to source files.
