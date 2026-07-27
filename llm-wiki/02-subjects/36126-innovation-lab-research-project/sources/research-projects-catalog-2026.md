# 36126 Innovation Lab: Research Project Topics Catalog (Spring 2026)

This document contains the complete, curated catalog of research project topics available for **36126 Innovation Lab: Research Project** (Spring 2026), extracted from official UTS MDSI research project specifications.

---

## 📌 How to Select a Project
1. **Review the Topics Below**: Projects are grouped by **Domain** and **Supervisor**.
2. **Contact Supervisor**: Contact the supervisor directly via email to confirm project availability and discuss your interest.
3. **Notify Subject Coordinator**: Once confirmed by the academic, notify the 36126 subject coordinator prior to final enrolment.

---

## 🏷️ Domain Breakdown & Navigation

| Domain | Key Technologies / Methods | Supervisors |
|---|---|---|
| **LLMs, GenAI & NLP** | RAG, Federated Learning, Earnings Call NLP, Intent Translation, Code Models | Dr. Mir Kabir, Dr. Tony Huang, Dr. Junaid Akram, Dr. Pouya Salpour, Decidr, Magtech.ai |
| **Computer Vision & Multimodal AI** | Deep Learning, Image Segmentation, Image Recognition, Video Querying | Dr. Ali Anaissi, Dr. Junaid Akram, Dr. Ali Haidar, Magtech.ai, MyVal |
| **Financial AI, Risk & Quant Trading** | Mamba, TimeSformer, RL, XAI, Credit/Cyber Risk, Evolutionary Algos | Dr. Alice Dong, Dr. Mir Kabir |
| **Healthcare, Medical & Mental Health AI** | Federated Vision-Language, Facial Image AI, Multi-Objective Clinical Triage | Dr. Ali Anaissi, Dr. Junaid Akram, Dr. Mir Kabir |
| **Climate, Weather & Environmental AI** | Agentic AI, Satellite Imagery, Bushfire Prediction, Ambient Eco-Visualization | Dr. Arnick Abdollahi, Dr. Alice Dong |
| **AI Governance, Literacy & XAI** | Corporate AI Governance (CAIGA), AI Literacy, Bayesian Adaptive XAI | Dr. David Hason Rudd, Dr. Jianlong Zhou, Dr. Alice Dong |

---

## 1. LLMs, Generative AI & NLP

### 1.1 Financial Text Understanding Using LLMs: Earnings Call Transcripts
- **Supervisor**: Dr. Mir Md Jahangir Kabir (`mirmdjahangir.kabir@uts.edu.au`)
- **Focus**: Empirical evaluation of LLMs (GPT-4, LLaMA, Claude) in interpreting financial jargon, executive sentiment, and forward-looking statements from earnings calls.
- **Dataset**: S&P 500 earnings call transcripts (SeekingAlpha, Bloomberg, EDGAR).
- **Key Methods**: Financial sentiment classification, prompt tuning, post-hoc interpretability.

### 1.2 Infographic Intent Language: Translating Communication Goals to Explainable Designs
- **Supervisor**: Dr. Tony Huang (`weidong.huang@uts.edu.au`)
- **Focus**: Building an intermediate "Infographic Intent Language" to make LLM-assisted infographic design transparent and user-controllable.
- **Key Methods**: Prompt engineering, Intent Language specification, LLM translation, web prototype (React/Streamlit), user study.

### 1.3 Can Large Language Models Critique Infographics Accurately?
- **Supervisor**: Dr. Tony Huang (`weidong.huang@uts.edu.au`)
- **Focus**: Assessing whether multimodal LLMs judge infographic quality, visual hierarchy, and message accuracy as effectively as human reviewers.

### 1.4 Evidence-Grounded Conversational Infographic Design with LLMs
- **Supervisor**: Dr. Tony Huang (`weidong.huang@uts.edu.au`)
- **Focus**: Multi-turn conversational workflows where LLMs query grounded evidence before proposing visual layouts.

### 1.5 LLM-Generated Audio Dialogues for Crisis Detection in Speech
- **Supervisor**: Dr. Junaid Akram (`junaid.akram@uts.edu.au`)
- **Focus**: Synthetic audio dialogue generation using LLMs to train crisis detection algorithms in speech.

### 1.6 Reproducible, Fully-Local Comparison of Small Free LLMs for Coding
- **Supervisor**: Dr. Pouya Salpour (`pouya.salpour@uts.edu.au`)
- **Focus**: Local benching of small open-weights coding LLMs (Ollama, LM Studio) for reproducible software development.

### 1.7 Automated LLM Verification and Assurance
- **Supervisor**: Dr. Pouya Salpour (`pouya.salpour@uts.edu.au`)
- **Focus**: Automated verification frameworks to test consistency, safety, and correctness of LLM outputs.

### 1.8 Grounded AI Assistant for Navigating the National Construction Code 2025
- **Industry Partner**: Magtech.ai (Mr. Mutaz Abu Ghazaleh)
- **Focus**: Building a RAG-based AI assistant grounded in Australia's National Construction Code (NCC 2025) for compliance query answering.

### 1.9 Assessing Credibility of Organisational Knowledge from Fragmented Data
- **Industry Partner**: Decidr (`tom.allen@decidr.ai`, `bianca.hill@decidr.ai`)
- **Focus**: Evaluating truthfulness, recency, and credibility of fragmented business data across enterprise knowledge silos.

---

## 2. Computer Vision & Multimodal AI

### 2.1 Omics Imagification for Cell-Type Classification Using Deep Learning
- **Supervisor**: Dr. Ali Anaissi (`ali.anaissi@uts.edu.au`)
- **Focus**: Converting high-dimensional omics expression data into image representations for CNN/ViT cell-type classification.

### 2.2 Vehicle Reidentification Using Deep Learning for Scalable Data Search
- **Supervisors**: Dr. Ali Anaissi (`ali.anaissi@uts.edu.au`) & Dr. Ali Haidar (NSW Police)
- **Focus**: Multi-camera vehicle re-identification and deep feature extraction across CCTV surveillance video streams.

### 2.3 Interactive Surveillance Video Querying Using LLMs & CCTV Datasets
- **Supervisor**: Dr. Ali Haidar (NSW Police)
- **Focus**: Natural language querying of multi-camera CCTV feeds using vision-language LLMs.

### 2.4 Vehicle Metadata Identification Using Machine Learning
- **Supervisor**: Dr. Ali Haidar (NSW Police)
- **Focus**: Classification of vehicle make, model, year, and features from traffic cameras.

### 2.5 Explainable Fake Image Detection Using Large Multimodal Models
- **Supervisor**: Dr. Junaid Akram (`junaid.akram@uts.edu.au`)
- **Focus**: Detecting AI-generated deepfake images with visual heatmaps and textual explanations.

### 2.6 AI Detection of Floor Slabs from Architectural and Structural Drawings
- **Industry Partner**: Magtech.ai (Mr. Mutaz Abu Ghazaleh)
- **Focus**: Computer vision detection of floor slabs and structural elements from CAD/PDF architectural drawings.

### 2.7 Advanced Image Recognition for Household Item Identification
- **Industry Partner**: MyVal (`https://www.myval.au/`)
- **Focus**: Object detection and classification of household assets to automate property valuation.

---

## 3. Financial AI, Quant Trading & Risk

### 3.1 Multimodal Modeling for Financial Time-Series Forecasting
- **Supervisor**: Dr. Alice Dong (`xiaodan.dong@uts.edu.au`)
- **Focus**: Applying Mamba and TimeSformer architectures to predict asset return covariance matrices for portfolio optimization.

### 3.2 AI-Driven Credit / Cyber Risk Modeling
- **Supervisor**: Dr. Alice Dong (`xiaodan.dong@uts.edu.au`)
- **Focus**: Blending deep learning with traditional statistical models for interpretable credit default and cyber risk prediction.

### 3.3 Automated Portfolio Management Using Reinforcement Learning & Evolutionary Algorithms
- **Supervisor**: Dr. Mir Md Jahangir Kabir (`mirmdjahangir.kabir@uts.edu.au`)
- **Focus**: Combining Deep Q-Learning / Policy Gradients with Genetic Algorithms for dynamic risk-adjusted portfolio rebalancing.

### 3.4 Evolutionary Reward Shaping for Reinforcement Learning Agents
- **Supervisor**: Dr. Mir Md Jahangir Kabir (`mirmdjahangir.kabir@uts.edu.au`)
- **Focus**: Evolving optimal reward functions using Genetic Algorithms in Gymnasium environments to solve sparse reward issues.

### 3.5 Graph-Based XAI for Fraud Detection
- **Supervisor**: Dr. Alice Dong (`xiaodan.dong@uts.edu.au`)
- **Focus**: Graph Neural Networks (GNNs) and visual network explainability for detecting financial fraud.

### 3.6 Personalized Financial Visualizations via Bayesian Framework
- **Supervisor**: Dr. Alice Dong (`xiaodan.dong@uts.edu.au`)
- **Focus**: Adaptive visual explanations tailored to non-expert financial users via Bayesian parameter estimation.

---

## 4. Healthcare & Medical AI

### 4.1 Predicting Rhinoplasty Outcomes Using AI & Facial Image Analysis
- **Supervisor**: Dr. Ali Anaissi (`ali.anaissi@uts.edu.au`)
- **Focus**: Generative deep learning for predicting post-operative facial outcomes from pre-operative photos, packaged with a desktop application UI.

### 4.2 Privacy-Preserving Medical Vision-Language AI Assistant using Federated Learning
- **Supervisor**: Dr. Junaid Akram (`junaid.akram@uts.edu.au`)
- **Focus**: Federated Learning applied to medical vision-language models for privacy-preserving diagnostic assistance.

### 4.3 Multi-Objective Optimization of a Risk-Aware Clinical Support System for Mental Health Triage
- **Supervisor**: Dr. Mir Md Jahangir Kabir (`mirmdjahangir.kabir@uts.edu.au`)
- **Focus**: Evolutionary multi-objective optimization balancing clinical risk, triage accuracy, and resource constraints in mental health settings.

---

## 5. Climate, Weather & Environmental AI

### 5.1 Agentic AI for Early Detection of Weather Extremes
- **Supervisor**: Dr. Arnick Abdollahi (`arnick.abdollahi@uts.edu.au`)
- **Focus**: Multi-agent LLM system synthesizing meteorological data streams for early extreme weather warning.

### 5.2 Satellite-Based Approaches for Bushfire Prediction & Risk Intelligence
- **Supervisor**: Dr. Arnick Abdollahi (`arnick.abdollahi@uts.edu.au`)
- **Focus**: Machine learning on remote sensing satellite imagery for bushfire occurrence forecasting.

### 5.3 Generative AI-Powered Ambient Eco-Visualization for Sustainability
- **Supervisor**: Dr. Alice Dong (`xiaodan.dong@uts.edu.au`)
- **Focus**: Ambient digital display design driven by simulated energy usage data to encourage energy-saving behaviors.

---

## 6. AI Governance & 3D Spatial Inference

### 6.1 Empirical Validation of Corporate AI Governance Architectures (CAIGA)
- **Supervisor**: Dr. David Hason Rudd (`david.hasonrudd@uts.edu.au`)
- **Focus**: Data-driven modeling and empirical assessment of enterprise AI compliance and governance.

### 6.2 GenAI-Enhanced Spatial-Temporal Inference for 3D Indoor 5G Coverage Mapping
- **Supervisor**: Dr. David Hason Rudd (`david.hasonrudd@uts.edu.au`)
- **Focus**: Generative AI spatial inference models for indoor 5G signal mapping and network planning.

### 6.3 Bridging the AI Divide: Empowering Users Through AI Literacy
- **Supervisor**: Dr. Jianlong Zhou (`jianlong.zhou@uts.edu.au`)
- **Focus**: Human-computer interaction frameworks to evaluate and improve AI literacy among diverse user groups.

---

## ✉️ Supervisor Contact Summary

| Supervisor | Email | Research Specialties |
|---|---|---|
| **Dr. Alice Dong** | `xiaodan.dong@uts.edu.au` | Credit/Cyber Risk, Financial Time-Series, Eco-Visualization, Graph XAI |
| **Dr. Ali Anaissi** | `ali.anaissi@uts.edu.au` | Rhinoplasty AI, Omics Deep Learning, Spatiotemporal Crime Prediction |
| **Dr. Arnick Abdollahi** | `arnick.abdollahi@uts.edu.au` | Agentic Weather AI, Satellite Bushfire Prediction |
| **Dr. David Hason Rudd** | `david.hasonrudd@uts.edu.au` | Corporate AI Governance (CAIGA), 3D 5G Spatial Inference |
| **Dr. Jianlong Zhou** | `jianlong.zhou@uts.edu.au` | Human-AI Interaction, XAI, AI Literacy |
| **Dr. Mir Md Jahangir Kabir**| `mirmdjahangir.kabir@uts.edu.au` | Mental Health Triage, Financial LLMs, Evolutionary RL, Quant Portfolio |
| **Dr. Tony Huang** | `weidong.huang@uts.edu.au` | Infographics, Intent Language, LLM Design Critiques, Graph Prompts |
| **Dr. Junaid Akram** | `junaid.akram@uts.edu.au` | Federated Medical Vision-Language, Fake Image Detection, Speech Crisis |
| **Dr. Ali Haidar** (NSW Police) | `ali.haidar@uts.edu.au` | Vehicle Re-ID, Surveillance Video Querying, Traffic Metadata |
| **Dr. Pouya Salpour** | `pouya.salpour@uts.edu.au` | Local Coding LLMs, Automated LLM Assurance |
