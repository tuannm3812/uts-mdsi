---
type: research-projects-guide
status: active
code: "36126"
name: "36126 Innovation Lab: Research Project Topics Uniform Detailed Guide"
---

# 36126 Innovation Lab: Research Project Uniform Detailed Guide (Spring 2026)

This document provides a **100% standardized, uniform, in-depth comparison guide** for every research project proposed for **36126 Innovation Lab: Research Project** (Spring 2026).

> [!NOTE]
> Every project below is structured into the **EXACT SAME 8 SECTIONS** (Background, Problem Statement, Objectives, Methodology, Datasets, Prerequisites, Deliverables, References) to make side-by-side comparison seamless.

---

## 📋 Quick Supervisor Directory & Email Index

| Supervisor / Partner | Contact Email | Research Focus Areas |
|---|---|---|
| **Dr. Alice Dong** | `xiaodan.dong@uts.edu.au` | Credit/Cyber Risk, Mamba Time-Series, Eco-Viz, Graph XAI, Bayesian Viz |
| **Dr. Ali Anaissi** | `ali.anaissi@uts.edu.au` | Rhinoplasty AI, Omics Imagification, Crime Prediction, Small LLMs |
| **Dr. Arnick Abdollahi** | `arnick.abdollahi@uts.edu.au` | Agentic Weather AI, Satellite Bushfire Prediction |
| **Dr. David Hason Rudd** | `david.hasonrudd@uts.edu.au` | Corporate AI Governance (CAIGA), 3D 5G Spatial Inference |
| **Dr. Jianlong Zhou** | `jianlong.zhou@uts.edu.au` | Mental Health LLM Chatbots, AI Literacy & Human-AI Divide |
| **Dr. Mir Md Jahangir Kabir** | `mirmdjahangir.kabir@uts.edu.au` | Clinical Mental Health Triage, Earnings Call LLMs, Evolutionary RL, Quant Portfolio |
| **Dr. Tony Huang** | `weidong.huang@uts.edu.au` | Infographics, Intent Language, LLM Design Critiques, Graph Prompts |
| **Dr. Junaid Akram** | `junaid.akram@uts.edu.au` | Federated Medical Vision-Language, Fake Image Detection, Speech Crisis |
| **Dr. Ali Haidar** (NSW Police) | `ali.haidar@uts.edu.au` | Vehicle Metadata, Multi-Camera Re-ID, Surveillance Video Querying |
| **Dr. Pouya Salpour** | `pouya.salpour@uts.edu.au` | Local Coding LLMs (LM Studio/Ollama), Automated LLM Verification |
| **Magtech.ai** | `Mutaz Abu Ghazaleh` | RAG Construction Code Assistant, CAD Floor Slab Segmentation |
| **MyVal** | `https://www.myval.au/` | Household Asset Image Recognition & Insurtech Valuation |
| **Decidr** | `tom.allen@decidr.ai` | Enterprise Knowledge Credibility & Fragmented Data |

---

# 📑 UNIFORM PROJECT SPECIFICATIONS CATALOG

## Project #01: Predicting Rhinoplasty Outcomes Using AI and Facial Image Analysis

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Anaissi** (`ali.anaissi@uts.edu.au`)
> - **Domain / Area**: **Healthcare & Computer Vision**
> - **Core Tech Stack**: **Deep Learning**, **Generative AI**, GANs, Diffusion Models, **PyTorch**, Desktop UI

### 1. 📖 Background & Context
This project focuses on developing deep learning models that predict post-operative facial outcomes using pre-operative photographs to assist facial reconstructive and cosmetic surgery consultations.

### 2. ❓ Problem Statement & Research Gap
Surgeons and patients lack realistic, data-driven pre-visualization of surgical outcomes, leading to misaligned expectations.

### 3. 🎯 Key Objectives & Scope
- Model expected facial changes in nasal shape and profile.
- Develop a desktop application UI for photo upload and post-operative visualization generation.
- Evaluate visualization accuracy and user consultation satisfaction.

### 4. 🛠️ Methodology & Technical Approach
- Train conditional GANs (Pix2Pix, CycleGAN) or Diffusion Models on before-and-after facial image pairs.
- Implement facial landmark alignment for structural normalization.
- Optimize inference for CPU desktop execution.

### 5. 📊 Datasets & Experimental Environment
Before-and-after facial photograph dataset of rhinoplasty cases (provided by supervisor).

### 6. 💻 Required Skills & Prerequisites
- Python programming, PyTorch / TensorFlow
- Computer vision (OpenCV, landmark detection)
- Desktop GUI development (PyQt, Tkinter, or web wrapper)

### 7. 🏆 Expected Deliverables & Outcomes
- Trained generative deep learning model
- Desktop application GUI for clinical use
- Empirical evaluation report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #02: Privacy-Preserving Medical Vision-Language AI Assistant using Federated Learning

> [!INFO]
> - **Supervisor / Contact**: **Dr. Junaid Akram** (`junaid.akram@uts.edu.au`)
> - **Domain / Area**: **Medical AI & Privacy-Preserving ML**
> - **Core Tech Stack**: **Federated Learning**, Vision-Language Models, **PyTorch**, FedAvg, Flower

### 1. 📖 Background & Context
Sharing medical images between hospital nodes is restricted due to HIPAA/privacy regulations. Federated Learning allows multi-institutional collaboration without sharing raw patient data.

### 2. ❓ Problem Statement & Research Gap
Centralized medical AI training violates patient privacy, while siloed hospital models suffer from small sample sizes.

### 3. 🎯 Key Objectives & Scope
- Develop a federated vision-language framework across simulated hospital clients.
- Compare federated aggregation algorithms (FedAvg, FedProx, SCAFFOLD).
- Evaluate privacy preservation and diagnostic explanation quality.

### 4. 🛠️ Methodology & Technical Approach
- Integrate chest X-rays / ultrasound images with clinical text notes.
- Implement federated training across decentralized nodes using Flower / PySyft.
- Measure diagnostic accuracy against centralized baselines.

### 5. 📊 Datasets & Experimental Environment
- MIMIC-CXR / MIMIC-CXR-JPG
- Breast Cancer Ultrasound Dataset
- PathVQA

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch / TensorFlow
- Federated Learning principles
- Multi-modal / Vision-Language Model architectures

### 7. 🏆 Expected Deliverables & Outcomes
- Open-source federated medical AI framework
- Comparative benchmark report of FL algorithms
- Diagnostic accuracy and privacy assessment

### 8. 📚 Academic References & Recommended Reading
Nature Scientific Reports: Federated Learning in Medicine (https://www.nature.com/articles/s41598-020-69250-1)

---
## Project #03: Explainable Fake Image Detection using Large Multimodal Models

> [!INFO]
> - **Supervisor / Contact**: **Dr. Junaid Akram** (`junaid.akram@uts.edu.au`)
> - **Domain / Area**: **Computer Vision & Explainable AI**
> - **Core Tech Stack**: **Generative AI**, Large Multimodal Models (LMMs), **Explainable AI**, Heatmaps

### 1. 📖 Background & Context
Generative AI image models produce hyper-realistic synthetic images. Existing detectors operate as black boxes without explaining why an image is fake.

### 2. ❓ Problem Statement & Research Gap
Lack of explainability and visual heatmaps in deepfake detection limits user trust and forensic utility.

### 3. 🎯 Key Objectives & Scope
- Develop a multimodal framework that detects synthetic images AND generates natural language explanations.
- Provide visual evidence heatmaps indicating manipulated regions.
- Evaluate robustness across diverse generative architectures (Midjourney, Stable Diffusion, DALL-E).

### 4. 🛠️ Methodology & Technical Approach
- Fine-tune Large Multimodal Models (LMMs) on real vs fake image pairs.
- Generate attention heatmaps and text explanations highlighting artifact inconsistencies.

### 5. 📊 Datasets & Experimental Environment
Public deepfake datasets (FaceForensics++, GenImage, FakeAVCeleb).

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch / Transformers
- Computer vision & XAI techniques
- Large Multimodal Model APIs

### 7. 🏆 Expected Deliverables & Outcomes
- Explainable deepfake detection codebase
- Heatmap visualization module
- Evaluation paper on multi-model detection performance

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #04: LLM-Generated Audio Dialogues for Crisis Detection in Speech

> [!INFO]
> - **Supervisor / Contact**: **Dr. Junaid Akram** (`junaid.akram@uts.edu.au`)
> - **Domain / Area**: **Speech Processing & LLMs**
> - **Core Tech Stack**: **Large Language Models**, Speech Synthesis, Fine-Tuning, Crisis Detection, Audio NLP

### 1. 📖 Background & Context
Speech carries essential vocal cues (hesitation, tremor, silence) for crisis detection, but real crisis-call recordings cannot be released due to strict privacy rules.

### 2. ❓ Problem Statement & Research Gap
No open audio-text benchmark exists for turn-level speech crisis detection.

### 3. 🎯 Key Objectives & Scope
- Fine-tune an open LLM to generate spoken-register crisis dialogues with turn-level Alert/Confirm labels.
- Synthesize audio via TTS with controlled acoustic parameters (emotion, tremor, pauses).
- Validate corpus scale with automated LLM-judge ensembles and release an open audio benchmark.

### 4. 🛠️ Methodology & Technical Approach
- Fine-tune LLM on CRADLE-Dialogue text corpus.
- Synthesize multi-speaker audio with acoustic perturbations.
- Evaluate audio-LLM crisis classification performance.

### 5. 📊 Datasets & Experimental Environment
CRADLE-Dialogue dataset & companion training corpus.

### 6. 💻 Required Skills & Prerequisites
- Python, HuggingFace Transformers, Audio Processing (torchaudio / Librosa)
- LLM fine-tuning and prompt engineering

### 7. 🏆 Expected Deliverables & Outcomes
- First open synthetic audio-text crisis dialogue benchmark corpus
- Generation pipeline codebase
- Baseline classification evaluation paper

### 8. 📚 Academic References & Recommended Reading
CRADLE-Dialogue (Byun et al., 2026)

---
## Project #05: Vehicle Metadata Identification Using Machine Learning

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Haidar (NSW Police)** (`ali.haidar@uts.edu.au`)
> - **Domain / Area**: **Computer Vision & Traffic Analytics**
> - **Core Tech Stack**: **Machine Learning**, **CNNs**, **Vision Transformers**, **YOLO**, **OpenCV**

### 1. 📖 Background & Context
Extracting detailed vehicle metadata (make, model, color, roof racks, damage, decals) from traffic camera feeds is vital for law enforcement and traffic management.

### 2. ❓ Problem Statement & Research Gap
Low resolution, occlusions, and varied camera angles make fine-grained vehicle attribute extraction difficult.

### 3. 🎯 Key Objectives & Scope
- Develop ML/CV models to classify vehicle make, model, body type, color, and accessories.
- Utilize object detection (YOLO) to isolate damage, roof racks, and decals.
- Benchmark classification accuracy across real traffic camera footage.

### 4. 🛠️ Methodology & Technical Approach
- Preprocess and annotate traffic image datasets.
- Train multi-task CNNs / ViTs for simultaneous attribute prediction.

### 5. 📊 Datasets & Experimental Environment
Public and police traffic camera image datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, OpenCV, PyTorch / TensorFlow
- YOLO / Object Detection frameworks

### 7. 🏆 Expected Deliverables & Outcomes
- Multi-attribute vehicle metadata classifier pipeline
- Performance evaluation report across attributes

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #06: Vehicle Reidentification Using Deep Learning for Scalable Search

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Haidar (NSW Police) / Dr. Ali Anaissi** (`ali.haidar@uts.edu.au`)
> - **Domain / Area**: **Deep Learning & Video Analytics**
> - **Core Tech Stack**: **Deep Learning**, Deep Metric Learning, Contrastive Learning, **PyTorch**, Re-ID

### 1. 📖 Background & Context
Tracking specific vehicles across multi-camera CCTV networks without license plates requires matching subtle visual features across different angles and lighting.

### 2. ❓ Problem Statement & Research Gap
Standard object classifiers fail when license plates are obscured or camera perspectives vary significantly.

### 3. 🎯 Key Objectives & Scope
- Develop deep metric learning models (triplet loss, contrastive learning) for vehicle re-identification.
- Extract robust embedding vectors for fast similarity search across video streams.
- Benchmark re-identification precision (mAP, Rank-1 accuracy).

### 4. 🛠️ Methodology & Technical Approach
- Train ResNet / ViT feature extractors with metric learning loss functions.
- Build vector indexing for fast vehicle retrieval across multi-camera feeds.

### 5. 📊 Datasets & Experimental Environment
VeRi-776, VehicleID, CityFlow multi-camera datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch, OpenCV
- Metric learning & vector search experience

### 7. 🏆 Expected Deliverables & Outcomes
- Vehicle Re-ID feature extraction codebase
- Multi-camera search benchmark evaluation report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #07: Interactive Surveillance Video Querying Using LLMs and Multi-Camera CCTV

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Haidar (NSW Police)** (`ali.haidar@uts.edu.au`)
> - **Domain / Area**: **Vision-Language & Video Retrieval**
> - **Core Tech Stack**: **Large Language Models**, Vision-Language Models, **Streamlit**, Vector Databases, **Python**

### 1. 📖 Background & Context
Security personnel spend hours manually reviewing CCTV footage. Natural language search allows asking questions like 'Show all red cars entering after 5 PM'.

### 2. ❓ Problem Statement & Research Gap
Bridging raw video streams with natural language text queries requires structured spatiotemporal indexing and LLM query translation.

### 3. 🎯 Key Objectives & Scope
- Convert CCTV video metadata into structured spatiotemporal graph indexes.
- Use LLMs to convert natural language user questions into database search filters.
- Build an interactive Streamlit/React web dashboard for video retrieval.

### 4. 🛠️ Methodology & Technical Approach
- Process MEVA/DIVA CCTV datasets into vector/graph metadata.
- Connect LLM prompt parser to Milvus/Weaviate vector database.
- Render interactive timeline video player.

### 5. 📊 Datasets & Experimental Environment
MEVA, DIVA, VIRAT multi-camera CCTV video datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, LLM APIs (GPT-4 / LLaMA)
- Vector databases, Streamlit / React frontend

### 7. 🏆 Expected Deliverables & Outcomes
- Interactive CCTV video query dashboard
- Spatiotemporal metadata indexing pipeline
- System benchmark report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #08: Reproducible, Fully-Local Comparison of Small Free LLMs for Coding

> [!INFO]
> - **Supervisor / Contact**: **Dr. Pouya Salpour** (`pouya.salpour@uts.edu.au`)
> - **Domain / Area**: **LLMs & Software Engineering**
> - **Core Tech Stack**: **Large Language Models**, **LM Studio**, **Ollama**, **Python**, Benchmarking

### 1. 📖 Background & Context
Commercial coding LLMs (GPT-4) are expensive and privacy-restricted. Small open-weights models (7-9B) can run locally on consumer hardware, but lack independent benchmarks.

### 2. ❓ Problem Statement & Research Gap
Lack of reproducible local evaluation under identical hardware/software constraints.

### 3. 🎯 Key Objectives & Scope
- Build a reproducible local benchmarking suite using LM Studio and Ollama.
- Evaluate 7B-9B open-weights coding LLMs across HumanEval, MBPP, and code repair benchmarks.
- Publish an open leaderboard of local model performance.

### 4. 🛠️ Methodology & Technical Approach
- Script local inference execution via Ollama/LM Studio REST APIs.
- Measure pass@1, execution speed, RAM usage, and code correctness.

### 5. 📊 Datasets & Experimental Environment
HumanEval, MBPP, MultiPL-E coding benchmarks.

### 6. 💻 Required Skills & Prerequisites
- Python, REST API scripting
- Familiarity with Ollama, LM Studio, local LLM execution

### 7. 🏆 Expected Deliverables & Outcomes
- Automated local LLM benchmarking suite
- Open performance leaderboard & comparative paper

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #09: Automated LLM Verification and Assurance

> [!INFO]
> - **Supervisor / Contact**: **Dr. Pouya Salpour** (`pouya.salpour@uts.edu.au`)
> - **Domain / Area**: **AI Safety & Software Testing**
> - **Core Tech Stack**: **Large Language Models**, Automated Testing, Synthetic Data, Causal Consistency

### 1. 📖 Background & Context
LLMs often produce correct answers for the wrong reasons, making standard accuracy metrics insufficient for safety-critical enterprise deployment.

### 2. ❓ Problem Statement & Research Gap
Existing evaluation methods fail to test causal consistency and robustness under minor input perturbations.

### 3. 🎯 Key Objectives & Scope
- Build an automated testing framework for causal consistency using paired-input testing.
- Generate a synthetic evaluation dataset for LLM verification.
- Benchmark consistency and robustness of open-source LLMs.

### 4. 🛠️ Methodology & Technical Approach
- Construct paired prompt variations (altering non-essential vs essential context).
- Measure response output divergence and causal reliance.

### 5. 📊 Datasets & Experimental Environment
Synthetic paired evaluation dataset (to be generated).

### 6. 💻 Required Skills & Prerequisites
- Python, automated software testing
- LLM API integration and prompt engineering

### 7. 🏆 Expected Deliverables & Outcomes
- Automated LLM verification framework
- Synthetic assurance dataset
- Evaluation report on LLM consistency

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #10: Grounded AI Assistant for Navigating the National Construction Code 2025

> [!INFO]
> - **Supervisor / Contact**: **Magtech.ai (Mr. Mutaz Abu Ghazaleh)** (`mutaz@magtech.ai`)
> - **Domain / Area**: **Enterprise RAG & Knowledge Graphs**
> - **Core Tech Stack**: **Retrieval-Augmented Generation**, XML/XSD, Knowledge Graphs, **LLMs**, **Python**

### 1. 📖 Background & Context
Navigating Australia's National Construction Code (NCC 2025) is complex. Builders require precise compliance answers backed by exact clause citations.

### 2. ❓ Problem Statement & Research Gap
Standard RAG over unstructured PDF text loses structural clause hierarchies, resulting in hallucinated or incomplete compliance answers.

### 3. 🎯 Key Objectives & Scope
- Parse NCC 2025 Volume One XML/XSD into a 17,000-node structural knowledge graph.
- Build a graph-grounded RAG retrieval pipeline.
- Benchmark answer accuracy and citation precision against naive RAG.

### 4. 🛠️ Methodology & Technical Approach
- Parse `contents.xml` and `ncc.xsd` into GraphX / NetworkX nodes and edges.
- Build LLM orchestration tool to traverse graph hierarchies for compliance answering.

### 5. 📊 Datasets & Experimental Environment
NCC 2025 Volume One XML corpus (5.5 MB), 17,012 nodes, 41,146 edges (provided).

### 6. 💻 Required Skills & Prerequisites
- Python, XML/XSD parsing
- Graph modeling (NetworkX / Neo4j)
- RAG, LLM orchestration, evaluation design

### 7. 🏆 Expected Deliverables & Outcomes
- Graph-grounded RAG query backend
- Interactive prototype UI
- Comparative retrieval accuracy report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #11: AI Detection of Floor Slabs from Architectural and Structural Drawings

> [!INFO]
> - **Supervisor / Contact**: **Magtech.ai (Mr. Mutaz Abu Ghazaleh)** (`mutaz@magtech.ai`)
> - **Domain / Area**: **Computer Vision & Construction Tech**
> - **Core Tech Stack**: Computer Vision, Semantic Segmentation, **PyTorch**, **OpenCV**, **YOLO**, MLStructFP

### 1. 📖 Background & Context
Structural floor plan analysis research focuses heavily on wall detection, but automatic detection of floor slab regions remains unsolved.

### 2. ❓ Problem Statement & Research Gap
Slab detection from CAD/PDF architectural blueprints is unaddressed in public ML pipelines, impeding automated cost estimation.

### 3. 🎯 Key Objectives & Scope
- Extend the MLStructFP benchmark dataset from wall segmentation to floor slab detection.
- Train semantic segmentation models (U-Net, Mask R-CNN) for slab region polygon extraction.
- Benchmark slab detection using IoU and Dice score metrics.

### 4. 🛠️ Methodology & Technical Approach
- Preprocess MLStructFP vector dataset and slab annotations.
- Train segmentation networks and post-process polygon boundaries with Shapely.

### 5. 📊 Datasets & Experimental Environment
MLStructFP public structural floor plan dataset and slab annotations (provided).

### 6. 💻 Required Skills & Prerequisites
- Python, Computer Vision (OpenCV, PyTorch)
- Semantic segmentation, Shapely / GeoJSON geometry

### 7. 🏆 Expected Deliverables & Outcomes
- Floor slab segmentation model pipeline
- Evaluation benchmark paper (IoU, Dice score)
- Polygon vectorization tool

### 8. 📚 Academic References & Recommended Reading
MLStructFP research benchmark repository

---
## Project #12: Using Advanced Image Recognition to Identify Household Items for Property Valuation

> [!INFO]
> - **Supervisor / Contact**: **MyVal (https://www.myval.au/)** (`contact@myval.au`)
> - **Domain / Area**: **Insurtech & Computer Vision**
> - **Core Tech Stack**: Computer Vision, Image Classification, Data Analysis, **Python**, Visual Dashboards

### 1. 📖 Background & Context
Homeowners struggle to accurately document household contents for insurance policies, leading to under-insurance or missed claims.

### 2. ❓ Problem Statement & Research Gap
Manual inventory entry has low customer engagement and lacks automated warranty/recall tracking.

### 3. 🎯 Key Objectives & Scope
- Use computer vision image recognition to detect and classify household items from photos.
- Pattern-match documented items against insurance limits, warranties, and replacement values.
- Build an interactive customer recommendation dashboard.

### 4. 🛠️ Methodology & Technical Approach
- Train object recognition model on household asset categories.
- Link item metadata to warranty and valuation APIs.

### 5. 📊 Datasets & Experimental Environment
MyVal customer inventory image dataset (anonymized).

### 6. 💻 Required Skills & Prerequisites
- Python, basic image recognition / ML
- Data visualization and analytics

### 7. 🏆 Expected Deliverables & Outcomes
- Household item recognition module
- Customer insight dashboard prototype
- Project research report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project #13: Assessing the Credibility of Organisational Knowledge from Fragmented Data

> [!INFO]
> - **Supervisor / Contact**: **Decidr (Bianca Hill & Tom Allen)** (`tom.allen@decidr.ai`)
> - **Domain / Area**: **Enterprise Knowledge & LLMs**
> - **Core Tech Stack**: **LLMs**, Information Retrieval, Knowledge Graphs, Bayesian Reasoning, **Python**

### 1. 📖 Background & Context
Enterprise knowledge is fragmented across email, Slack, and documents. Existing search tools return outdated or unverified claims without credibility scoring.

### 2. ❓ Problem Statement & Research Gap
Lack of confidence calibration and truthfulness scoring when synthesizing fragmented business records.

### 3. 🎯 Key Objectives & Scope
- Develop probabilistic / Bayesian models to score data credibility, recency, and source authority.
- Build an explainable knowledge synthesis pipeline over fragmented enterprise records.
- Evaluate confidence calibration against human ground-truth labels.

### 4. 🛠️ Methodology & Technical Approach
- Combine NLP embeddings, graph relations, and Bayesian confidence scoring.
- Benchmark system accuracy on Decidr's synthetic business dataset.

### 5. 📊 Datasets & Experimental Environment
Decidr synthetic/anonymized enterprise knowledge dataset (provided).

### 6. 💻 Required Skills & Prerequisites
- Python, NLP, Information Retrieval
- Knowledge graphs or Bayesian reasoning
- LLMs & RAG evaluation

### 7. 🏆 Expected Deliverables & Outcomes
- Knowledge credibility scoring engine
- Evaluation report & benchmark analysis
- Technical documentation for Decidr platform

### 8. 📚 Academic References & Recommended Reading
N/A

---


# SECTION 2: INFOGRAPHICS & HUMAN-AI VISUALIZATION RESEARCH (DR TONY HUANG)

## Project TH-01: Infographic Intent Language: Translating Communication Goals into Design Decisions

> [!INFO]
> - **Supervisor / Contact**: **Dr. Tony Huang** (`weidong.huang@uts.edu.au`)
> - **Domain / Area**: **Human-AI Interaction & Visualization**
> - **Core Tech Stack**: **Large Language Models**, Intent Translation, **React**, **Streamlit**, **Python**, UI/UX

### 1. 📖 Background & Context
LLMs currently generate infographics directly from raw text prompts as a black box, offering no user control over visual choices or layout logic.

### 2. ❓ Problem Statement & Research Gap
Direct LLM generation lacks transparency, reproducibility, and user control.

### 3. 🎯 Key Objectives & Scope
- Define a structured 'Infographic Intent Language' (goal, target audience, rhetoric, layout).
- Develop an LLM translator converting natural text briefs into editable intent specs.
- Build a prototype web interface (React/Streamlit) and conduct a user evaluation study.

### 4. 🛠️ Methodology & Technical Approach
- Analyze professional infographics to extract common intent patterns.
- Implement prompt-to-intent LLM parser and layout generator.
- Conduct user study comparing direct prompting vs intent-driven workflow.

### 5. 📊 Datasets & Experimental Environment
Annotated collection of professional infographic briefs.

### 6. 💻 Required Skills & Prerequisites
- Python / JavaScript (React or Streamlit)
- Data visualization principles, LLM APIs
- User-centered study design

### 7. 🏆 Expected Deliverables & Outcomes
- Infographic Intent Language specification
- Interactive web prototype
- Evaluation study research paper

### 8. 📚 Academic References & Recommended Reading
LIDA (Dibia, 2023), Epigraphics (Zhou et al., 2024)

---
## Project TH-02: Can Large Language Models Critique Infographics as Well as Humans?

> [!INFO]
> - **Supervisor / Contact**: **Dr. Tony Huang** (`weidong.huang@uts.edu.au`)
> - **Domain / Area**: **Multimodal AI & Visualization Evaluation**
> - **Core Tech Stack**: Multimodal **LLMs**, Vision-Language Models, **Python**, Benchmark Evaluation, Statistics

### 1. 📖 Background & Context
Multimodal LLMs are increasingly used to review graphic designs, but their agreement with human visual perception and design accuracy remains untested.

### 2. ❓ Problem Statement & Research Gap
Visually appealing infographics may still contain misleading data encodings or poor hierarchy that LLMs fail to flag.

### 3. 🎯 Key Objectives & Scope
- Construct a benchmark dataset of professional vs flawed infographics.
- Evaluate agreement between human design ratings and multimodal LLM critiques.
- Identify systematic bias where LLMs over- or under-estimate graphic quality.

### 4. 🛠️ Methodology & Technical Approach
- Modify infographics to introduce controlled design flaws (misleading charts, bad color contrast).
- Prompt GPT-4V / Claude 3.5 Sonnet to critique visual quality and compare with human scores.

### 5. 📊 Datasets & Experimental Environment
Benchmark dataset of annotated infographics with controlled flaws.

### 6. 💻 Required Skills & Prerequisites
- Python, Multimodal LLM APIs
- Statistical analysis & experimental design
- Data visualization literacy

### 7. 🏆 Expected Deliverables & Outcomes
- Infographic critique benchmark dataset
- Empirical human vs AI agreement study
- Guidelines for AI-assisted design review

### 8. 📚 Academic References & Recommended Reading
VisEval (Chen et al., 2024), LLMs Have Visualization Literacy (Seto et al., 2026)

---
## Project TH-03: Evidence-Grounded Conversational Infographic Design with LLMs

> [!INFO]
> - **Supervisor / Contact**: **Dr. Tony Huang** (`weidong.huang@uts.edu.au`)
> - **Domain / Area**: **Conversational AI & Data Visualization**
> - **Core Tech Stack**: **LLMs**, **RAG**, Conversational AI, Fact Verification, **Python**, **Streamlit**

### 1. 📖 Background & Context
LLMs frequently hallucinate facts, alter numbers, or overstate conclusions when generating visual infographics from reports.

### 2. ❓ Problem Statement & Research Gap
Unverified AI infographic generation reduces public trust in health and policy communications.

### 3. 🎯 Key Objectives & Scope
- Build a multi-turn conversational design assistant with Retrieval-Augmented Generation (RAG).
- Ensure all chart numbers and claims trace back to verified source documents.
- Evaluate factual accuracy, user trust, and verification effort.

### 4. 🛠️ Methodology & Technical Approach
- Implement document parsing and RAG retrieval.
- Build conversational interface highlighting source evidence for every generated chart component.

### 5. 📊 Datasets & Experimental Environment
Annotated corpus of source reports and dataset files.

### 6. 💻 Required Skills & Prerequisites
- Python, RAG architectures (LangChain / LlamaIndex)
- Web UI development (Streamlit / Gradio)
- Fact verification methodologies

### 7. 🏆 Expected Deliverables & Outcomes
- Working evidence-grounded prototype
- Annotated source document corpus
- Empirical evaluation paper

### 8. 📚 Academic References & Recommended Reading
Infogen (Ghosh et al., 2025), LIDA (Dibia, 2023)

---
## Project TH-04: Translating Natural-Language Graph Design Prompts into Layout Transformations

> [!INFO]
> - **Supervisor / Contact**: **Dr. Tony Huang** (`weidong.huang@uts.edu.au`)
> - **Domain / Area**: **Graph Drawing & LLM Parsing**
> - **Core Tech Stack**: **Large Language Models**, Graph Drawing, **NetworkX**, Graphviz, **Python**

### 1. 📖 Background & Context
Users frequently request graph layout changes in plain language ('separate clusters', 'reduce crossings'), but layout algorithms require complex code parameters.

### 2. ❓ Problem Statement & Research Gap
Asking LLMs to generate node coordinates directly is unreliable and produces invalid graph layouts.

### 3. 🎯 Key Objectives & Scope
- Design a 'Graph Layout Intent Language' encoding hard and soft visual constraints.
- Develop an LLM parser converting natural prompts into structured layout specifications.
- Connect specifications to layout engines (NetworkX, Graphviz, D3).

### 4. 🛠️ Methodology & Technical Approach
- Collect natural language graph editing requests.
- Train/prompt LLMs to parse requests into validated JSON layout instructions.

### 5. 📊 Datasets & Experimental Environment
Annotated dataset of natural language graph design prompts.

### 6. 💻 Required Skills & Prerequisites
- Python / JavaScript, Graph Theory & NetworkX
- Prompt engineering & JSON schema validation

### 7. 🏆 Expected Deliverables & Outcomes
- Graph Layout Intent Language specification
- Natural language to graph layout parser codebase
- Empirical evaluation research paper

### 8. 📚 Academic References & Recommended Reading
Ask and You Shall Receive (Di Bartolomeo et al., 2023), Chat2VIS (Maddigan & Susnjak, 2023)

---


# SECTION 3: PROFESSORIAL & ACADEMIC RESEARCH PROJECTS (OTHER FACULTY)

## Project AD-01: AI-Driven Credit / Cyber Risk Modeling

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Financial AI & Cyber Risk**
> - **Core Tech Stack**: **Deep Learning**, **Machine Learning**, Statistical Risk Modeling, Credit Risk, **Python**

### 1. 📖 Background & Context
Financial institutions require high default prediction accuracy without losing the interpretability of traditional credit scoring models.

### 2. ❓ Problem Statement & Research Gap
Pure deep learning models lack interpretability for regulatory credit approval.

### 3. 🎯 Key Objectives & Scope
- Combine predictive machine learning with interpretable statistical models.
- Enhance credit default and cyber risk classification.
- Evaluate risk prediction accuracy and explainability.

### 4. 🛠️ Methodology & Technical Approach
- Train hybrid ML/statistical risk models on financial institution datasets.
- Apply XAI techniques to explain default factors.

### 5. 📊 Datasets & Experimental Environment
Financial risk dataset (available upon request from Dr. Alice Dong).

### 6. 💻 Required Skills & Prerequisites
- Python, statistical risk modeling, ML fundamentals

### 7. 🏆 Expected Deliverables & Outcomes
- Hybrid risk prediction model
- Empirical evaluation report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AD-02: Multimodal Modeling for Financial Time-Series Forecasting (Mamba & TimeSformer)

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Quant Finance & Deep Learning**
> - **Core Tech Stack**: **Mamba**, **TimeSformer**, **PyTorch**, Time-Series Forecasting, Portfolio Optimization

### 1. 📖 Background & Context
Accurate asset return covariance matrix forecasting is vital for mean-variance portfolio optimization and risk management.

### 2. ❓ Problem Statement & Research Gap
Traditional time-series models (GARCH) struggle to capture complex spatial and temporal asset co-movements across large portfolios.

### 3. 🎯 Key Objectives & Scope
- Adapt Mamba (state space models) and TimeSformer (video transformers) to financial return series.
- Model multivariate temporal sequences to forecast time-varying covariance matrices.
- Integrate covariance forecasts into mean-variance portfolio optimization.

### 4. 🛠️ Methodology & Technical Approach
- Represent multivariate asset returns as 2D spatiotemporal tensors.
- Train TimeSformer / Mamba architectures for dynamic covariance matrix prediction.

### 5. 📊 Datasets & Experimental Environment
Financial asset return dataset (available upon request from Dr. Alice Dong).

### 6. 💻 Required Skills & Prerequisites
- PyTorch, deep learning time-series modeling
- Quantitative finance & portfolio theory

### 7. 🏆 Expected Deliverables & Outcomes
- Spatiotemporal covariance forecasting model
- Portfolio backtesting results (Sharpe ratio, max drawdown)

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AD-03: Generative AI-Powered Ambient Eco-Visualization for Sustainability

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Sustainability & AI Art / Viz**
> - **Core Tech Stack**: **Generative AI**, Eco-Visualization, Ambient Intelligence, Web Displays, **Python**

### 1. 📖 Background & Context
Promoting household energy conservation requires continuous, non-intrusive feedback that inspires behavioral changes.

### 2. ❓ Problem Statement & Research Gap
Numeric smart meter dashboards have low long-term user engagement.

### 3. 🎯 Key Objectives & Scope
- Design AI-driven ambient digital visualizations based on simulated household energy usage data.
- Dynamically transform visual art displays to reflect real-time energy conservation patterns.

### 4. 🛠️ Methodology & Technical Approach
- Process smart meter energy datasets into ambient art rendering parameters.

### 5. 📊 Datasets & Experimental Environment
Simulated energy consumption datasets (available upon request).

### 6. 💻 Required Skills & Prerequisites
- Python / JS, web display frameworks, Generative AI art tools

### 7. 🏆 Expected Deliverables & Outcomes
- Ambient eco-visualization digital display prototype
- User engagement study report

### 8. 📚 Academic References & Recommended Reading
Eco-visualization (Holmes, 2007), Smart Home Ambient Intelligence (Makonin et al., 2013)

---
## Project AD-04: Personalized Financial Visualizations via Bayesian Framework

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Explainable AI & Financial Viz**
> - **Core Tech Stack**: **Bayesian Framework**, Adaptive UI, **XAI**, Financial Analytics, **Python**

### 1. 📖 Background & Context
Non-expert investors find complex AI financial predictions difficult to understand.

### 2. ❓ Problem Statement & Research Gap
Fixed financial charts do not adapt explanations based on individual user expertise.

### 3. 🎯 Key Objectives & Scope
- Build a Bayesian framework that updates visual explanations dynamically based on real-time user interaction.
- Personalize complex AI financial insights for varying user knowledge levels.

### 4. 🛠️ Methodology & Technical Approach
- Implement Bayesian parameter update model tracking user comprehension signals.

### 5. 📊 Datasets & Experimental Environment
Financial analytics interaction dataset (available upon request).

### 6. 💻 Required Skills & Prerequisites
- Python, Bayesian statistics, interactive UI design

### 7. 🏆 Expected Deliverables & Outcomes
- Adaptive Bayesian financial visualization prototype
- User comprehension study report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AD-05: Graph-Based XAI for Fraud Detection

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Graph ML & Fraud Detection**
> - **Core Tech Stack**: **Graph Neural Networks** (**GNNs**), **Explainable AI** (**XAI**), Network Visualization, **Python**

### 1. 📖 Background & Context
Financial fraud and money laundering occur across intricate transaction networks that standard tabular ML models fail to detect.

### 2. ❓ Problem Statement & Research Gap
Lack of network visual explainability in fraud detection systems.

### 3. 🎯 Key Objectives & Scope
- Represent financial transactions as graph networks.
- Apply Graph Neural Networks (GNNs) and XAI to highlight suspicious transaction rings.
- Provide interactive graph visualizations for compliance analysts.

### 4. 🛠️ Methodology & Technical Approach
- Train GNN fraud detection models and apply GNNExplainer for subgraph visualization.

### 5. 📊 Datasets & Experimental Environment
Banking transaction dataset (available upon request).

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch Geometric / NetworkX, XAI techniques

### 7. 🏆 Expected Deliverables & Outcomes
- Graph-based fraud detection pipeline
- Interactive network XAI visualization interface

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AD-06: Multi-Dimensional Financial Risk Visualization

> [!INFO]
> - **Supervisor / Contact**: **Dr. Alice Dong** (`xiaodan.dong@uts.edu.au`)
> - **Domain / Area**: **Risk Analytics & Visualization**
> - **Core Tech Stack**: **Explainable AI** (**XAI**), Risk Assessment, Portfolio Management, Multi-Dimensional Viz

### 1. 📖 Background & Context
Portfolio managers struggle to break down complex multi-dimensional risk exposure across market regimes.

### 2. ❓ Problem Statement & Research Gap
Lack of transparent risk factor decomposition in automated portfolio tools.

### 3. 🎯 Key Objectives & Scope
- Develop an XAI multi-dimensional risk visualization framework.
- Break down portfolio risk drivers into interactive visual representations.

### 4. 🛠️ Methodology & Technical Approach
- Process financial risk datasets into multi-dimensional factor models.

### 5. 📊 Datasets & Experimental Environment
Financial Risk dataset (available upon request).

### 6. 💻 Required Skills & Prerequisites
- Python, risk analytics, data visualization

### 7. 🏆 Expected Deliverables & Outcomes
- Multi-dimensional risk dashboard
- Empirical evaluation report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AA-01: Distributed Small Language Models with Federated Learning

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Anaissi** (`ali.anaissi@uts.edu.au`)
> - **Domain / Area**: **Distributed AI & Privacy**
> - **Core Tech Stack**: Small Language Models (SLMs), **Federated Learning**, OpenFedLLM, **Python**, **PyTorch**

### 1. 📖 Background & Context
Organizations want domain-specific AI assistance without centralizing sensitive private data.

### 2. ❓ Problem Statement & Research Gap
Centralized LLM fine-tuning risks private data leaks.

### 3. 🎯 Key Objectives & Scope
- Develop a distributed Small Language Model (SLM) framework using Federated Learning.
- Train models across decentralized nodes while protecting raw text privacy.
- Benchmark decentralized response quality against centralized SLMs.

### 4. 🛠️ Methodology & Technical Approach
- Deploy OpenFedLLM framework across simulated private nodes.

### 5. 📊 Datasets & Experimental Environment
OpenfedLLM datasets & AllenAI open data.

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch, Federated Learning, SLM fine-tuning

### 7. 🏆 Expected Deliverables & Outcomes
- Distributed FL-SLM training framework
- Privacy & response benchmark report

### 8. 📚 Academic References & Recommended Reading
OpenFedLLM (ACM 2024), LLMs + Federated Learning (Patterns 2024)

---
## Project AA-02: Omics Imagification for Cell-Type Classification Using Deep Learning

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Anaissi** (`ali.anaissi@uts.edu.au`)
> - **Domain / Area**: **Bioinformatics & Deep Learning**
> - **Core Tech Stack**: **Deep Learning**, **CNNs**, Omics Imagification, Fotomics, **PyTorch**, **Python**

### 1. 📖 Background & Context
High-dimensional single-cell omics data is difficult to classify using traditional tabular ML.

### 2. ❓ Problem Statement & Research Gap
Tabular ML ignores spatial feature co-expression structures.

### 3. 🎯 Key Objectives & Scope
- Transform 1D single-cell omics vectors into structured 2D RGB images ('imagification').
- Train CNNs on transformed omics images for cell-type classification.
- Benchmark classification performance against standard tabular ML.

### 4. 🛠️ Methodology & Technical Approach
- Implement Fotomics Fourier-transform imagification pipeline.
- Train ResNet / ViT image classifiers on converted omics datasets.

### 5. 📊 Datasets & Experimental Environment
Single-cell omics benchmark datasets (Fotomics GitHub repository).

### 6. 💻 Required Skills & Prerequisites
- Python, PyTorch, Bioinformatics data analysis

### 7. 🏆 Expected Deliverables & Outcomes
- Omics imagification preprocessing library
- Cell-type classification model & evaluation report

### 8. 📚 Academic References & Recommended Reading
Fotomics (Springer 2022)

---
## Project AA-03: Crime Prediction Using SpatioTemporal Data and Machine Learning

> [!INFO]
> - **Supervisor / Contact**: **Dr. Ali Anaissi** (`ali.anaissi@uts.edu.au`)
> - **Domain / Area**: **Spatiotemporal Analytics & Urban AI**
> - **Core Tech Stack**: **Machine Learning**, Spatiotemporal **GNNs**, LSTMs, **Folium**, **QGIS**, **Python**

### 1. 📖 Background & Context
Urban police departments require proactive spatial forecasting of crime hotspots.

### 2. ❓ Problem Statement & Research Gap
Standard spatial regression models miss temporal trends and socioeconomic interactions.

### 3. 🎯 Key Objectives & Scope
- Integrate open crime data with geospatial, weather, and socioeconomic indicators.
- Train Spatiotemporal GNNs, Random Forests, and LSTMs for crime hotspot forecasting.
- Visualize spatial risk maps using Folium / QGIS.

### 4. 🛠️ Methodology & Technical Approach
- Engineer spatial features (population density, police station proximity).
- Train spatiotemporal forecast models.

### 5. 📊 Datasets & Experimental Environment
US Open Crime Data Portal & UK Police Data.

### 6. 💻 Required Skills & Prerequisites
- Python, Geospatial analytics (QGIS, Folium, GeoPandas)
- Spatiotemporal ML / GNNs

### 7. 🏆 Expected Deliverables & Outcomes
- Spatiotemporal crime prediction pipeline
- Interactive crime risk map
- Model benchmark evaluation paper

### 8. 📚 Academic References & Recommended Reading
Deep Learning Spatiotemporal Crime Prediction (arXiv 2024)

---
## Project DHR-01: Empirical Validation of Corporate AI Governance Architectures (CAIGA)

> [!INFO]
> - **Supervisor / Contact**: **Dr. David Hason Rudd** (`david.hasonrudd@uts.edu.au`)
> - **Domain / Area**: **AI Governance & Compliance Modeling**
> - **Core Tech Stack**: **Machine Learning**, Corporate AI Governance, Governance Modeling, **Python**, Statistics

### 1. 📖 Background & Context
Enterprise AI adoption outpaces formal governance frameworks, creating compliance and ethical failure risks.

### 2. ❓ Problem Statement & Research Gap
Lack of empirical data validation for corporate AI risk classification architectures.

### 3. 🎯 Key Objectives & Scope
- Compile structured governance data from AIID, Stanford HAI AI Index, and OECD.
- Quantify the governance implementation gap across corporate sectors.
- Train ML classifiers to predict corporate CAIGA risk tiers and benchmark governance maturity.

### 4. 🛠️ Methodology & Technical Approach
- Harmonize enterprise survey data from EY, McKinsey, PwC.
- Train Gradient Boosted Trees to classify enterprise AI risk levels.

### 5. 📊 Datasets & Experimental Environment
AI Incident Database (AIID), Stanford HAI AI Index, OECD AI Policy Observatory.

### 6. 💻 Required Skills & Prerequisites
- Python, statistical modeling, machine learning classification
- AI ethics & governance policy knowledge

### 7. 🏆 Expected Deliverables & Outcomes
- CAIGA empirical validation dataset
- Corporate AI risk prediction model
- Published governance research report

### 8. 📚 Academic References & Recommended Reading
OECD AI Recommendation (2019), BoE PRA SS1/23 (2023)

---
## Project DHR-02: Generative AI-Enhanced Spatial-Temporal Inference for 3D Indoor 5G Coverage Mapping

> [!INFO]
> - **Supervisor / Contact**: **Dr. David Hason Rudd** (`david.hasonrudd@uts.edu.au`)
> - **Domain / Area**: **Generative AI & 5G Telecom**
> - **Core Tech Stack**: **Generative AI**, GANs, Diffusion Models, Graph Attention Networks (TA-GAT), **PyTorch**

### 1. 📖 Background & Context
80% of 5G data occurs indoors, but high-frequency 5G signals attenuate severely through building materials. Inferring indoor signal maps from outdoor drone scans is a complex inversion problem.

### 2. ❓ Problem Statement & Research Gap
Scarcity of labeled indoor signal strength training data.

### 3. 🎯 Key Objectives & Scope
- Use Generative AI (GANs / Diffusion Models) to synthesize indoor 3D signal propagation data.
- Improve prediction accuracy of Received Signal Strength (RSSI) and Channel Quality (CQI).
- Benchmark model robustness on unseen building layouts.

### 4. 🛠️ Methodology & Technical Approach
- Train GANs conditioned on drone scan seeds and CAD wall structures.
- Augment TA-GAT indoor signal predictor.

### 5. 📊 Datasets & Experimental Environment
5G outdoor drone scan & building layout dataset (available upon request).

### 6. 💻 Required Skills & Prerequisites
- PyTorch, Generative AI (GANs/Diffusion), Graph Neural Networks

### 7. 🏆 Expected Deliverables & Outcomes
- Generative 3D signal augmentation pipeline
- 5G indoor coverage prediction model & paper

### 8. 📚 Academic References & Recommended Reading
Drone-based ML for 5G Coverage (Rudd et al., KES 2025)

---
## Project JZ-01: Large Language Model Chatbots for Mental Health Support

> [!INFO]
> - **Supervisor / Contact**: **Dr. Jianlong Zhou** (`jianlong.zhou@uts.edu.au`)
> - **Domain / Area**: **Healthcare AI & Conversational LLMs**
> - **Core Tech Stack**: **Large Language Models**, Mental Health Chatbots, Conversational UI, User Study, **Python**

### 1. 📖 Background & Context
Conversational LLM chatbots can deliver accessible mental health support, but require tailored interaction features and safety boundaries.

### 2. ❓ Problem Statement & Research Gap
Lack of user study evidence on key LLM UI factors for mental health support.

### 3. 🎯 Key Objectives & Scope
- Conduct a literature review on state-of-the-art mental health LLM chatbots.
- Develop an LLM-powered conversational mental health support chatbot prototype.
- Execute a user evaluation study to test chatbot support effectiveness.

### 4. 🛠️ Methodology & Technical Approach
- Fine-tune / prompt open LLM for supportive dialogue.
- Build web UI and run human participant study.

### 5. 📊 Datasets & Experimental Environment
Mental health dialogue datasets & user study feedback.

### 6. 💻 Required Skills & Prerequisites
- Python, LLM APIs, web UI development
- User study design & HCI evaluation

### 7. 🏆 Expected Deliverables & Outcomes
- Mental health LLM chatbot prototype
- User study evaluation paper

### 8. 📚 Academic References & Recommended Reading
The Typing Cure (arXiv 2024), LLM Workplace Well-being (ACM 2024)

---
## Project JZ-02: Bridging the AI Divide: Empowering Users through AI Literacy

> [!INFO]
> - **Supervisor / Contact**: **Dr. Jianlong Zhou** (`jianlong.zhou@uts.edu.au`)
> - **Domain / Area**: **Human-AI Interaction & AI Literacy**
> - **Core Tech Stack**: **Large Language Models**, AI Literacy, Human-AI Interaction, User Study, **Python**

### 1. 📖 Background & Context
Non-technical communities (e.g. farmers) are excluded from AI conversations, creating a digital AI divide.

### 2. ❓ Problem Statement & Research Gap
Lack of tailored frameworks to explain AI benefits from specific user perspectives.

### 3. 🎯 Key Objectives & Scope
- Explore LLM approaches that translate AI concepts tailored to non-technical user backgrounds.
- Conduct user studies evaluating user AI literacy improvements.

### 4. 🛠️ Methodology & Technical Approach
- Develop LLM explainability prompts customized for specific user archetypes.

### 5. 📊 Datasets & Experimental Environment
User survey & AI literacy evaluation datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, LLM prompting, HCI user study methods

### 7. 🏆 Expected Deliverables & Outcomes
- AI literacy translation framework
- User study evaluation paper

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AB-01: Agentic AI for Early Detection of Weather Extremes

> [!INFO]
> - **Supervisor / Contact**: **Dr. Arnick Abdollahi** (`arnick.abdollahi@uts.edu.au`)
> - **Domain / Area**: **Climate AI & Agentic Systems**
> - **Core Tech Stack**: Agentic AI, **Large Language Models**, Time-Series Analytics, Anomaly Detection, **Python**

### 1. 📖 Background & Context
Climate change creates unprecedented extreme weather events that fall outside historical regression patterns.

### 2. ❓ Problem Statement & Research Gap
Traditional forecasting struggles to identify emerging unobserved extreme climate anomalies.

### 3. 🎯 Key Objectives & Scope
- Develop a multi-agent AI framework to continuously monitor climate streams.
- Identify anomalous weather conditions and compare them against historical norms.
- Generate interpretable early warning risk recommendations for decision-makers.

### 4. 🛠️ Methodology & Technical Approach
- Build multi-agent workflow (Agentic LLMs + time-series anomaly detection).

### 5. 📊 Datasets & Experimental Environment
Historical climate & weather stream datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, Agentic AI frameworks (CrewAI / LangGraph)
- Time-series analytics & anomaly detection

### 7. 🏆 Expected Deliverables & Outcomes
- Multi-agent extreme weather detection system
- Climate risk intelligence benchmark report

### 8. 📚 Academic References & Recommended Reading
N/A

---
## Project AB-02: Data Science & Satellite Approaches for Bushfire Prediction

> [!INFO]
> - **Supervisor / Contact**: **Dr. Arnick Abdollahi** (`arnick.abdollahi@uts.edu.au`)
> - **Domain / Area**: **Remote Sensing & Bushfire Risk**
> - **Core Tech Stack**: **Machine Learning**, Remote Sensing, Satellite Data, **Explainable AI** (**XAI**), **Python**

### 1. 📖 Background & Context
Bushfires pose severe risks across Australia. Effective management requires predicting fire likelihood before ignition occurs.

### 2. ❓ Problem Statement & Research Gap
Complex spatiotemporal interactions between satellite vegetation indices and weather variables.

### 3. 🎯 Key Objectives & Scope
- Combine satellite observations (Sentinel/MODIS) with weather and historical fire records.
- Train predictive ML models to estimate bushfire occurrence likelihood across space and time.
- Apply Explainable AI (XAI) to identify key environmental fire drivers.

### 4. 🛠️ Methodology & Technical Approach
- Engineer spatiotemporal satellite features and train Random Forest / XGBoost classifiers.

### 5. 📊 Datasets & Experimental Environment
Satellite remote sensing imagery & Australian historical bushfire datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, Geospatial remote sensing, ML & XAI

### 7. 🏆 Expected Deliverables & Outcomes
- Bushfire occurrence prediction model
- XAI feature importance report
- Research paper manuscript

### 8. 📚 Academic References & Recommended Reading
XAI for Bushfire Occurrence Prediction (Science of Total Environment 2023)

---
## Project MK-01: Evolutionary Optimization of a Risk-Aware Clinical System for Mental Health Triage

> [!INFO]
> - **Supervisor / Contact**: **Dr. Mir Md Jahangir Kabir** (`mirmdjahangir.kabir@uts.edu.au`)
> - **Domain / Area**: **Healthcare AI & Evolutionary Optimization**
> - **Core Tech Stack**: **Genetic Algorithms**, Evolutionary Optimization, Mental Health Triage, **PyTorch**, **Python**

### 1. 📖 Background & Context
Clinical decision support systems in mental health must simultaneously balance empathy, safety protocols, and structural coherence.

### 2. ❓ Problem Statement & Research Gap
Single-objective ML models produce either rigid or unsafe conversational responses.

### 3. 🎯 Key Objectives & Scope
- Implement a Genetic Algorithm (GA) to evolve an interpretable genome controlling response policies.
- Formulate a constrained multi-objective fitness function with hard safety penalties.
- Evaluate clinical safety and empathy convergence against human clinical standards.

### 4. 🛠️ Methodology & Technical Approach
- Evolve policy parameters over mental health interaction datasets.

### 5. 📊 Datasets & Experimental Environment
DAIC-WOZ, CLPsych Suicide Risk Assessment Datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, Genetic Algorithms / Evolutionary Computation
- NLP & clinical safety metrics

### 7. 🏆 Expected Deliverables & Outcomes
- Evolutionary mental health triage framework
- Clinical safety evaluation report

### 8. 📚 Academic References & Recommended Reading
Promptbreeder (ICML 2024), GenDLN (ACL 2025)

---
## Project MK-02: Financial Text Understanding Using LLMs: Earnings Call Transcripts

> [!INFO]
> - **Supervisor / Contact**: **Dr. Mir Md Jahangir Kabir** (`mirmdjahangir.kabir@uts.edu.au`)
> - **Domain / Area**: **Financial NLP & LLM Evaluation**
> - **Core Tech Stack**: **Large Language Models**, Financial NLP, Sentiment Analysis, Prompt Tuning, **Python**

### 1. 📖 Background & Context
Earnings call transcripts are dense with financial jargon, executive hedging, and forward-looking statements.

### 2. ❓ Problem Statement & Research Gap
Uncertainty regarding LLM interpretability and performance in parsing domain-specific financial earnings calls.

### 3. 🎯 Key Objectives & Scope
- Empirically evaluate LLMs (GPT-4, LLaMA, Claude) on financial sentiment and trend prediction.
- Compare LLM performance against FinBERT baselines.
- Develop domain-specific financial text interpretability metrics.

### 4. 🛠️ Methodology & Technical Approach
- Segment earnings calls into executive vs analyst turns.
- Evaluate prompt tuning strategies for financial sentiment classification.

### 5. 📊 Datasets & Experimental Environment
S&P 500 earnings call transcripts (SeekingAlpha / Bloomberg / EDGAR).

### 6. 💻 Required Skills & Prerequisites
- Python, HuggingFace Transformers, LLM APIs
- Financial text analysis

### 7. 🏆 Expected Deliverables & Outcomes
- Financial LLM benchmark dataset
- Empirical evaluation research paper

### 8. 📚 Academic References & Recommended Reading
FinBERT (Araci, 2019), Financial Prompt Tuning (ACL 2023)

---
## Project MK-03: Evolutionary Reward Shaping for Reinforcement Learning Agents

> [!INFO]
> - **Supervisor / Contact**: **Dr. Mir Md Jahangir Kabir** (`mirmdjahangir.kabir@uts.edu.au`)
> - **Domain / Area**: **Reinforcement Learning & Evolutionary Algos**
> - **Core Tech Stack**: **Reinforcement Learning**, **Genetic Algorithms**, **Gymnasium**, Q-Learning, **PyTorch**, **Python**

### 1. 📖 Background & Context
Poorly designed reward functions lead to slow convergence and unstable learning in RL agents.

### 2. ❓ Problem Statement & Research Gap
Manual reward engineering is time-consuming and prone to unintended agent behaviors.

### 3. 🎯 Key Objectives & Scope
- Apply Genetic Algorithms to automatically generate and optimize reward functions for RL agents.
- Train agents in Gymnasium / MiniGrid benchmark environments.
- Compare learning efficiency between manual and evolved reward functions.

### 4. 🛠️ Methodology & Technical Approach
- Evolve reward function parameters using Genetic Algorithms based on cumulative agent rewards.

### 5. 📊 Datasets & Experimental Environment
Gymnasium & MiniGrid simulated benchmark environments.

### 6. 💻 Required Skills & Prerequisites
- Python, Reinforcement Learning (Gymnasium, Deep Q-Networks)
- Evolutionary algorithms

### 7. 🏆 Expected Deliverables & Outcomes
- Evolutionary reward shaping codebase
- Learning curve benchmark evaluation report

### 8. 📚 Academic References & Recommended Reading
EVO-RL (Hallawa et al., 2020), Sutton & Barto (2018)

---
## Project MK-04: Automated Portfolio Management Using RL and Evolutionary Algorithms

> [!INFO]
> - **Supervisor / Contact**: **Dr. Mir Md Jahangir Kabir** (`mirmdjahangir.kabir@uts.edu.au`)
> - **Domain / Area**: **Quant Trading & RL**
> - **Core Tech Stack**: **Reinforcement Learning**, **Genetic Algorithms**, Portfolio Optimization, **PyTorch**, **Python**

### 1. 📖 Background & Context
Financial markets are highly volatile, making static investment strategies suboptimal.

### 2. ❓ Problem Statement & Research Gap
Balancing multi-objective trade-offs between returns, volatility, and max drawdown under delayed rewards.

### 3. 🎯 Key Objectives & Scope
- Combine Deep Q-Learning / Policy Gradients with Genetic Algorithms for portfolio rebalancing.
- Evolve reward functions and portfolio constraints using market data.
- Benchmark system performance using Sharpe ratio, max drawdown, and cumulative returns.

### 4. 🛠️ Methodology & Technical Approach
- Train RL agents on historical stock price data to dynamically adjust asset weights.

### 5. 📊 Datasets & Experimental Environment
Yahoo Finance Historical Data & Kaggle Financial Datasets.

### 6. 💻 Required Skills & Prerequisites
- Python, Reinforcement Learning, Portfolio Theory

### 7. 🏆 Expected Deliverables & Outcomes
- Automated RL trading & portfolio management system
- Financial backtesting benchmark paper

### 8. 📚 Academic References & Recommended Reading
Learning to Trade via Direct RL (Moody & Saffell, 2001), Twin-System RRL (Wang et al., 2024)

---
