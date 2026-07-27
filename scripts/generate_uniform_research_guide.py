#!/usr/bin/env python3
"""
Generates a 100% standardized, uniform, highly detailed research project guide
where every project shares the exact same 8-section template for easy comparison.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "llm-wiki" / "02-subjects" / "36126-innovation-lab-research-project" / "sources" / "raw"
OUT_FILE = ROOT / "llm-wiki" / "02-subjects" / "36126-innovation-lab-research-project" / "sources" / "research-projects-detailed-guide-2026.md"

def clean(text: str) -> str:
    text = text.replace('\r\n', '\n').replace('\r', '\n').replace('\u2028', '\n').replace('\u2029', '\n').replace('\x0c', '\n')
    text = re.sub(r'[ \t]+', ' ', text)
    return text.strip()

def bold_terms(text: str) -> str:
    terms = [
        "Large Language Models", "Large Language Model", "LLMs", "LLM",
        "Generative AI", "GenAI", "Deep Learning", "Machine Learning",
        "Reinforcement Learning", "Federated Learning", "Vision Transformers", "ViT",
        "Convolutional Neural Networks", "CNNs", "CNN", "Graph Neural Networks", "GNNs", "GNN",
        "Explainable AI", "XAI", "Retrieval-Augmented Generation", "RAG", "Mamba", "TimeSformer",
        "Genetic Algorithms", "Evolutionary Algorithms", "OpenCV", "PyTorch", "TensorFlow",
        "Python", "Streamlit", "React", "Gymnasium", "OpenAI Gym", "Ollama", "LM Studio",
        "YOLO", "Mask R-CNN", "Bayesian Framework", "S&P 500", "SeekingAlpha", "Bloomberg",
        "EDGAR", "DAIC-WOZ", "National Construction Code", "NCC 2025", "QGIS", "Folium", "NetworkX"
    ]
    for t in sorted(terms, key=len, reverse=True):
        pattern = re.compile(r'(?<!\*\*)\b(' + re.escape(t) + r')\b(?!\*\*)', re.IGNORECASE)
        text = pattern.sub(r'**\1**', text)
    return text

def format_project_block(pid, title, supervisor, email, domain, tech, bg, problem, obj, method, data, skills, deliv, refs):
    bg_str = bg if bg else 'This research project explores recent advancements in applied data science and artificial intelligence to address key domain challenges.'
    prob_str = problem if problem else 'Traditional techniques struggle with complex, non-linear, high-dimensional, or un-grounded inputs. This project addresses the gap by leveraging modern AI architectures.'
    obj_str = obj if obj else '- Evaluate baseline performance.\n- Implement proposed model architecture.\n- Perform experimental validation and benchmark reporting.'
    method_str = method if method else 'Combines data wrangling, model training, feature engineering, and evaluation using state-of-the-art frameworks.'
    data_str = data if data else 'Relevant datasets available upon request or via public repositories.'
    skills_str = skills if skills else '- **Python** programming\n- Basic machine learning / deep learning knowledge\n- Data analysis and experimental evaluation'
    deliv_str = deliv if deliv else '- Trained model / algorithmic pipeline\n- Experimental evaluation report\n- Code repository and documentation'
    refs_str = refs if refs else 'N/A'
    tech_str = bold_terms(tech)

    return f"""## {pid}: {title}

> [!INFO]
> - **Supervisor / Contact**: **{supervisor}** (`{email}`)
> - **Domain / Area**: **{domain}**
> - **Core Tech Stack**: {tech_str}

### 1. 📖 Background & Context
{bg_str}

### 2. ❓ Problem Statement & Research Gap
{prob_str}

### 3. 🎯 Key Objectives & Scope
{obj_str}

### 4. 🛠️ Methodology & Technical Approach
{method_str}

### 5. 📊 Datasets & Experimental Environment
{data_str}

### 6. 💻 Required Skills & Prerequisites
{skills_str}

### 7. 🏆 Expected Deliverables & Outcomes
{deliv_str}

### 8. 📚 Academic References & Recommended Reading
{refs_str}

---
"""

def parse_and_build():
    txt1 = (RAW_DIR / 'Project_List_s2_2026.txt').read_text(encoding='utf-8')
    txt2 = (RAW_DIR / 'MDSI_research_projects_tony_huang.txt').read_text(encoding='utf-8')
    txt3 = (RAW_DIR / 'MDSI_research_projects_other_professors.txt').read_text(encoding='utf-8')

    doc = """---
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

"""

    # We will build uniform blocks for each project.
    # -------------------------------------------------------------
    # 1. Rhinoplasty AI (Dr Ali Anaissi)
    doc += format_project_block(
        "Project #01",
        "Predicting Rhinoplasty Outcomes Using AI and Facial Image Analysis",
        "Dr. Ali Anaissi",
        "ali.anaissi@uts.edu.au",
        "Healthcare & Computer Vision",
        "Deep Learning, Generative AI, GANs, Diffusion Models, PyTorch, Desktop UI",
        """This project focuses on developing deep learning models that predict post-operative facial outcomes using pre-operative photographs to assist facial reconstructive and cosmetic surgery consultations.""",
        """Surgeons and patients lack realistic, data-driven pre-visualization of surgical outcomes, leading to misaligned expectations.""",
        """- Model expected facial changes in nasal shape and profile.
- Develop a desktop application UI for photo upload and post-operative visualization generation.
- Evaluate visualization accuracy and user consultation satisfaction.""",
        """- Train conditional GANs (Pix2Pix, CycleGAN) or Diffusion Models on before-and-after facial image pairs.
- Implement facial landmark alignment for structural normalization.
- Optimize inference for CPU desktop execution.""",
        """Before-and-after facial photograph dataset of rhinoplasty cases (provided by supervisor).""",
        """- Python programming, PyTorch / TensorFlow
- Computer vision (OpenCV, landmark detection)
- Desktop GUI development (PyQt, Tkinter, or web wrapper)""",
        """- Trained generative deep learning model
- Desktop application GUI for clinical use
- Empirical evaluation report""",
        """N/A"""
    )

    # 2. Medical Federated Learning (Dr Junaid Akram)
    doc += format_project_block(
        "Project #02",
        "Privacy-Preserving Medical Vision-Language AI Assistant using Federated Learning",
        "Dr. Junaid Akram",
        "junaid.akram@uts.edu.au",
        "Medical AI & Privacy-Preserving ML",
        "Federated Learning, Vision-Language Models, PyTorch, FedAvg, Flower",
        """Sharing medical images between hospital nodes is restricted due to HIPAA/privacy regulations. Federated Learning allows multi-institutional collaboration without sharing raw patient data.""",
        """Centralized medical AI training violates patient privacy, while siloed hospital models suffer from small sample sizes.""",
        """- Develop a federated vision-language framework across simulated hospital clients.
- Compare federated aggregation algorithms (FedAvg, FedProx, SCAFFOLD).
- Evaluate privacy preservation and diagnostic explanation quality.""",
        """- Integrate chest X-rays / ultrasound images with clinical text notes.
- Implement federated training across decentralized nodes using Flower / PySyft.
- Measure diagnostic accuracy against centralized baselines.""",
        """- MIMIC-CXR / MIMIC-CXR-JPG
- Breast Cancer Ultrasound Dataset
- PathVQA""",
        """- Python, PyTorch / TensorFlow
- Federated Learning principles
- Multi-modal / Vision-Language Model architectures""",
        """- Open-source federated medical AI framework
- Comparative benchmark report of FL algorithms
- Diagnostic accuracy and privacy assessment""",
        """Nature Scientific Reports: Federated Learning in Medicine (https://www.nature.com/articles/s41598-020-69250-1)"""
    )

    # 3. Explainable Fake Image Detection (Dr Junaid Akram)
    doc += format_project_block(
        "Project #03",
        "Explainable Fake Image Detection using Large Multimodal Models",
        "Dr. Junaid Akram",
        "junaid.akram@uts.edu.au",
        "Computer Vision & Explainable AI",
        "Generative AI, Large Multimodal Models (LMMs), Explainable AI, Heatmaps",
        """Generative AI image models produce hyper-realistic synthetic images. Existing detectors operate as black boxes without explaining why an image is fake.""",
        """Lack of explainability and visual heatmaps in deepfake detection limits user trust and forensic utility.""",
        """- Develop a multimodal framework that detects synthetic images AND generates natural language explanations.
- Provide visual evidence heatmaps indicating manipulated regions.
- Evaluate robustness across diverse generative architectures (Midjourney, Stable Diffusion, DALL-E).""",
        """- Fine-tune Large Multimodal Models (LMMs) on real vs fake image pairs.
- Generate attention heatmaps and text explanations highlighting artifact inconsistencies.""",
        """Public deepfake datasets (FaceForensics++, GenImage, FakeAVCeleb).""",
        """- Python, PyTorch / Transformers
- Computer vision & XAI techniques
- Large Multimodal Model APIs""",
        """- Explainable deepfake detection codebase
- Heatmap visualization module
- Evaluation paper on multi-model detection performance""",
        """N/A"""
    )

    # 4. LLM Audio Dialogues for Crisis Detection (Dr Junaid Akram)
    doc += format_project_block(
        "Project #04",
        "LLM-Generated Audio Dialogues for Crisis Detection in Speech",
        "Dr. Junaid Akram",
        "junaid.akram@uts.edu.au",
        "Speech Processing & LLMs",
        "Large Language Models, Speech Synthesis, Fine-Tuning, Crisis Detection, Audio NLP",
        """Speech carries essential vocal cues (hesitation, tremor, silence) for crisis detection, but real crisis-call recordings cannot be released due to strict privacy rules.""",
        """No open audio-text benchmark exists for turn-level speech crisis detection.""",
        """- Fine-tune an open LLM to generate spoken-register crisis dialogues with turn-level Alert/Confirm labels.
- Synthesize audio via TTS with controlled acoustic parameters (emotion, tremor, pauses).
- Validate corpus scale with automated LLM-judge ensembles and release an open audio benchmark.""",
        """- Fine-tune LLM on CRADLE-Dialogue text corpus.
- Synthesize multi-speaker audio with acoustic perturbations.
- Evaluate audio-LLM crisis classification performance.""",
        """CRADLE-Dialogue dataset & companion training corpus.""",
        """- Python, HuggingFace Transformers, Audio Processing (torchaudio / Librosa)
- LLM fine-tuning and prompt engineering""",
        """- First open synthetic audio-text crisis dialogue benchmark corpus
- Generation pipeline codebase
- Baseline classification evaluation paper""",
        """CRADLE-Dialogue (Byun et al., 2026)"""
    )

    # 5. Vehicle Metadata Identification (Dr Ali Haidar / NSW Police)
    doc += format_project_block(
        "Project #05",
        "Vehicle Metadata Identification Using Machine Learning",
        "Dr. Ali Haidar (NSW Police)",
        "ali.haidar@uts.edu.au",
        "Computer Vision & Traffic Analytics",
        "Machine Learning, CNNs, Vision Transformers, YOLO, OpenCV",
        """Extracting detailed vehicle metadata (make, model, color, roof racks, damage, decals) from traffic camera feeds is vital for law enforcement and traffic management.""",
        """Low resolution, occlusions, and varied camera angles make fine-grained vehicle attribute extraction difficult.""",
        """- Develop ML/CV models to classify vehicle make, model, body type, color, and accessories.
- Utilize object detection (YOLO) to isolate damage, roof racks, and decals.
- Benchmark classification accuracy across real traffic camera footage.""",
        """- Preprocess and annotate traffic image datasets.
- Train multi-task CNNs / ViTs for simultaneous attribute prediction.""",
        """Public and police traffic camera image datasets.""",
        """- Python, OpenCV, PyTorch / TensorFlow
- YOLO / Object Detection frameworks""",
        """- Multi-attribute vehicle metadata classifier pipeline
- Performance evaluation report across attributes""",
        """N/A"""
    )

    # 6. Multi-Camera Vehicle Re-ID (Dr Ali Haidar & Dr Ali Anaissi)
    doc += format_project_block(
        "Project #06",
        "Vehicle Reidentification Using Deep Learning for Scalable Search",
        "Dr. Ali Haidar (NSW Police) / Dr. Ali Anaissi",
        "ali.haidar@uts.edu.au",
        "Deep Learning & Video Analytics",
        "Deep Learning, Deep Metric Learning, Contrastive Learning, PyTorch, Re-ID",
        """Tracking specific vehicles across multi-camera CCTV networks without license plates requires matching subtle visual features across different angles and lighting.""",
        """Standard object classifiers fail when license plates are obscured or camera perspectives vary significantly.""",
        """- Develop deep metric learning models (triplet loss, contrastive learning) for vehicle re-identification.
- Extract robust embedding vectors for fast similarity search across video streams.
- Benchmark re-identification precision (mAP, Rank-1 accuracy).""",
        """- Train ResNet / ViT feature extractors with metric learning loss functions.
- Build vector indexing for fast vehicle retrieval across multi-camera feeds.""",
        """VeRi-776, VehicleID, CityFlow multi-camera datasets.""",
        """- Python, PyTorch, OpenCV
- Metric learning & vector search experience""",
        """- Vehicle Re-ID feature extraction codebase
- Multi-camera search benchmark evaluation report""",
        """N/A"""
    )

    # 7. Interactive Surveillance Video Querying (Dr Ali Haidar)
    doc += format_project_block(
        "Project #07",
        "Interactive Surveillance Video Querying Using LLMs and Multi-Camera CCTV",
        "Dr. Ali Haidar (NSW Police)",
        "ali.haidar@uts.edu.au",
        "Vision-Language & Video Retrieval",
        "Large Language Models, Vision-Language Models, Streamlit, Vector Databases, Python",
        """Security personnel spend hours manually reviewing CCTV footage. Natural language search allows asking questions like 'Show all red cars entering after 5 PM'.""",
        """Bridging raw video streams with natural language text queries requires structured spatiotemporal indexing and LLM query translation.""",
        """- Convert CCTV video metadata into structured spatiotemporal graph indexes.
- Use LLMs to convert natural language user questions into database search filters.
- Build an interactive Streamlit/React web dashboard for video retrieval.""",
        """- Process MEVA/DIVA CCTV datasets into vector/graph metadata.
- Connect LLM prompt parser to Milvus/Weaviate vector database.
- Render interactive timeline video player.""",
        """MEVA, DIVA, VIRAT multi-camera CCTV video datasets.""",
        """- Python, LLM APIs (GPT-4 / LLaMA)
- Vector databases, Streamlit / React frontend""",
        """- Interactive CCTV video query dashboard
- Spatiotemporal metadata indexing pipeline
- System benchmark report""",
        """N/A"""
    )

    # 8. Local Small LLMs for Coding (Dr Pouya Salpour)
    doc += format_project_block(
        "Project #08",
        "Reproducible, Fully-Local Comparison of Small Free LLMs for Coding",
        "Dr. Pouya Salpour",
        "pouya.salpour@uts.edu.au",
        "LLMs & Software Engineering",
        "Large Language Models, LM Studio, Ollama, Python, Benchmarking",
        """Commercial coding LLMs (GPT-4) are expensive and privacy-restricted. Small open-weights models (7-9B) can run locally on consumer hardware, but lack independent benchmarks.""",
        """Lack of reproducible local evaluation under identical hardware/software constraints.""",
        """- Build a reproducible local benchmarking suite using LM Studio and Ollama.
- Evaluate 7B-9B open-weights coding LLMs across HumanEval, MBPP, and code repair benchmarks.
- Publish an open leaderboard of local model performance.""",
        """- Script local inference execution via Ollama/LM Studio REST APIs.
- Measure pass@1, execution speed, RAM usage, and code correctness.""",
        """HumanEval, MBPP, MultiPL-E coding benchmarks.""",
        """- Python, REST API scripting
- Familiarity with Ollama, LM Studio, local LLM execution""",
        """- Automated local LLM benchmarking suite
- Open performance leaderboard & comparative paper""",
        """N/A"""
    )

    # 9. Automated LLM Verification (Dr Pouya Salpour)
    doc += format_project_block(
        "Project #09",
        "Automated LLM Verification and Assurance",
        "Dr. Pouya Salpour",
        "pouya.salpour@uts.edu.au",
        "AI Safety & Software Testing",
        "Large Language Models, Automated Testing, Synthetic Data, Causal Consistency",
        """LLMs often produce correct answers for the wrong reasons, making standard accuracy metrics insufficient for safety-critical enterprise deployment.""",
        """Existing evaluation methods fail to test causal consistency and robustness under minor input perturbations.""",
        """- Build an automated testing framework for causal consistency using paired-input testing.
- Generate a synthetic evaluation dataset for LLM verification.
- Benchmark consistency and robustness of open-source LLMs.""",
        """- Construct paired prompt variations (altering non-essential vs essential context).
- Measure response output divergence and causal reliance.""",
        """Synthetic paired evaluation dataset (to be generated).""",
        """- Python, automated software testing
- LLM API integration and prompt engineering""",
        """- Automated LLM verification framework
- Synthetic assurance dataset
- Evaluation report on LLM consistency""",
        """N/A"""
    )

    # 10. National Construction Code RAG Assistant (Magtech.ai)
    doc += format_project_block(
        "Project #10",
        "Grounded AI Assistant for Navigating the National Construction Code 2025",
        "Magtech.ai (Mr. Mutaz Abu Ghazaleh)",
        "mutaz@magtech.ai",
        "Enterprise RAG & Knowledge Graphs",
        "Retrieval-Augmented Generation, XML/XSD, Knowledge Graphs, LLMs, Python",
        """Navigating Australia's National Construction Code (NCC 2025) is complex. Builders require precise compliance answers backed by exact clause citations.""",
        """Standard RAG over unstructured PDF text loses structural clause hierarchies, resulting in hallucinated or incomplete compliance answers.""",
        """- Parse NCC 2025 Volume One XML/XSD into a 17,000-node structural knowledge graph.
- Build a graph-grounded RAG retrieval pipeline.
- Benchmark answer accuracy and citation precision against naive RAG.""",
        """- Parse `contents.xml` and `ncc.xsd` into GraphX / NetworkX nodes and edges.
- Build LLM orchestration tool to traverse graph hierarchies for compliance answering.""",
        """NCC 2025 Volume One XML corpus (5.5 MB), 17,012 nodes, 41,146 edges (provided).""",
        """- Python, XML/XSD parsing
- Graph modeling (NetworkX / Neo4j)
- RAG, LLM orchestration, evaluation design""",
        """- Graph-grounded RAG query backend
- Interactive prototype UI
- Comparative retrieval accuracy report""",
        """N/A"""
    )

    # 11. Floor Slab Vision Detection (Magtech.ai)
    doc += format_project_block(
        "Project #11",
        "AI Detection of Floor Slabs from Architectural and Structural Drawings",
        "Magtech.ai (Mr. Mutaz Abu Ghazaleh)",
        "mutaz@magtech.ai",
        "Computer Vision & Construction Tech",
        "Computer Vision, Semantic Segmentation, PyTorch, OpenCV, YOLO, MLStructFP",
        """Structural floor plan analysis research focuses heavily on wall detection, but automatic detection of floor slab regions remains unsolved.""",
        """Slab detection from CAD/PDF architectural blueprints is unaddressed in public ML pipelines, impeding automated cost estimation.""",
        """- Extend the MLStructFP benchmark dataset from wall segmentation to floor slab detection.
- Train semantic segmentation models (U-Net, Mask R-CNN) for slab region polygon extraction.
- Benchmark slab detection using IoU and Dice score metrics.""",
        """- Preprocess MLStructFP vector dataset and slab annotations.
- Train segmentation networks and post-process polygon boundaries with Shapely.""",
        """MLStructFP public structural floor plan dataset and slab annotations (provided).""",
        """- Python, Computer Vision (OpenCV, PyTorch)
- Semantic segmentation, Shapely / GeoJSON geometry""",
        """- Floor slab segmentation model pipeline
- Evaluation benchmark paper (IoU, Dice score)
- Polygon vectorization tool""",
        """MLStructFP research benchmark repository"""
    )

    # 12. Household Item Image Recognition (MyVal)
    doc += format_project_block(
        "Project #12",
        "Using Advanced Image Recognition to Identify Household Items for Property Valuation",
        "MyVal (https://www.myval.au/)",
        "contact@myval.au",
        "Insurtech & Computer Vision",
        "Computer Vision, Image Classification, Data Analysis, Python, Visual Dashboards",
        """Homeowners struggle to accurately document household contents for insurance policies, leading to under-insurance or missed claims.""",
        """Manual inventory entry has low customer engagement and lacks automated warranty/recall tracking.""",
        """- Use computer vision image recognition to detect and classify household items from photos.
- Pattern-match documented items against insurance limits, warranties, and replacement values.
- Build an interactive customer recommendation dashboard.""",
        """- Train object recognition model on household asset categories.
- Link item metadata to warranty and valuation APIs.""",
        """MyVal customer inventory image dataset (anonymized).""",
        """- Python, basic image recognition / ML
- Data visualization and analytics""",
        """- Household item recognition module
- Customer insight dashboard prototype
- Project research report""",
        """N/A"""
    )

    # 13. Decidr Organisational Knowledge Credibility (Decidr)
    doc += format_project_block(
        "Project #13",
        "Assessing the Credibility of Organisational Knowledge from Fragmented Data",
        "Decidr (Bianca Hill & Tom Allen)",
        "tom.allen@decidr.ai",
        "Enterprise Knowledge & LLMs",
        "LLMs, Information Retrieval, Knowledge Graphs, Bayesian Reasoning, Python",
        """Enterprise knowledge is fragmented across email, Slack, and documents. Existing search tools return outdated or unverified claims without credibility scoring.""",
        """Lack of confidence calibration and truthfulness scoring when synthesizing fragmented business records.""",
        """- Develop probabilistic / Bayesian models to score data credibility, recency, and source authority.
- Build an explainable knowledge synthesis pipeline over fragmented enterprise records.
- Evaluate confidence calibration against human ground-truth labels.""",
        """- Combine NLP embeddings, graph relations, and Bayesian confidence scoring.
- Benchmark system accuracy on Decidr's synthetic business dataset.""",
        """Decidr synthetic/anonymized enterprise knowledge dataset (provided).""",
        """- Python, NLP, Information Retrieval
- Knowledge graphs or Bayesian reasoning
- LLMs & RAG evaluation""",
        """- Knowledge credibility scoring engine
- Evaluation report & benchmark analysis
- Technical documentation for Decidr platform""",
        """N/A"""
    )

    # -------------------------------------------------------------
    # Section 2: Dr Tony Huang Projects (4 Projects)
    doc += "\n\n# SECTION 2: INFOGRAPHICS & HUMAN-AI VISUALIZATION RESEARCH (DR TONY HUANG)\n\n"

    doc += format_project_block(
        "Project TH-01",
        "Infographic Intent Language: Translating Communication Goals into Design Decisions",
        "Dr. Tony Huang",
        "weidong.huang@uts.edu.au",
        "Human-AI Interaction & Visualization",
        "Large Language Models, Intent Translation, React, Streamlit, Python, UI/UX",
        """LLMs currently generate infographics directly from raw text prompts as a black box, offering no user control over visual choices or layout logic.""",
        """Direct LLM generation lacks transparency, reproducibility, and user control.""",
        """- Define a structured 'Infographic Intent Language' (goal, target audience, rhetoric, layout).
- Develop an LLM translator converting natural text briefs into editable intent specs.
- Build a prototype web interface (React/Streamlit) and conduct a user evaluation study.""",
        """- Analyze professional infographics to extract common intent patterns.
- Implement prompt-to-intent LLM parser and layout generator.
- Conduct user study comparing direct prompting vs intent-driven workflow.""",
        """Annotated collection of professional infographic briefs.""",
        """- Python / JavaScript (React or Streamlit)
- Data visualization principles, LLM APIs
- User-centered study design""",
        """- Infographic Intent Language specification
- Interactive web prototype
- Evaluation study research paper""",
        """LIDA (Dibia, 2023), Epigraphics (Zhou et al., 2024)"""
    )

    doc += format_project_block(
        "Project TH-02",
        "Can Large Language Models Critique Infographics as Well as Humans?",
        "Dr. Tony Huang",
        "weidong.huang@uts.edu.au",
        "Multimodal AI & Visualization Evaluation",
        "Multimodal LLMs, Vision-Language Models, Python, Benchmark Evaluation, Statistics",
        """Multimodal LLMs are increasingly used to review graphic designs, but their agreement with human visual perception and design accuracy remains untested.""",
        """Visually appealing infographics may still contain misleading data encodings or poor hierarchy that LLMs fail to flag.""",
        """- Construct a benchmark dataset of professional vs flawed infographics.
- Evaluate agreement between human design ratings and multimodal LLM critiques.
- Identify systematic bias where LLMs over- or under-estimate graphic quality.""",
        """- Modify infographics to introduce controlled design flaws (misleading charts, bad color contrast).
- Prompt GPT-4V / Claude 3.5 Sonnet to critique visual quality and compare with human scores.""",
        """Benchmark dataset of annotated infographics with controlled flaws.""",
        """- Python, Multimodal LLM APIs
- Statistical analysis & experimental design
- Data visualization literacy""",
        """- Infographic critique benchmark dataset
- Empirical human vs AI agreement study
- Guidelines for AI-assisted design review""",
        """VisEval (Chen et al., 2024), LLMs Have Visualization Literacy (Seto et al., 2026)"""
    )

    doc += format_project_block(
        "Project TH-03",
        "Evidence-Grounded Conversational Infographic Design with LLMs",
        "Dr. Tony Huang",
        "weidong.huang@uts.edu.au",
        "Conversational AI & Data Visualization",
        "LLMs, RAG, Conversational AI, Fact Verification, Python, Streamlit",
        """LLMs frequently hallucinate facts, alter numbers, or overstate conclusions when generating visual infographics from reports.""",
        """Unverified AI infographic generation reduces public trust in health and policy communications.""",
        """- Build a multi-turn conversational design assistant with Retrieval-Augmented Generation (RAG).
- Ensure all chart numbers and claims trace back to verified source documents.
- Evaluate factual accuracy, user trust, and verification effort.""",
        """- Implement document parsing and RAG retrieval.
- Build conversational interface highlighting source evidence for every generated chart component.""",
        """Annotated corpus of source reports and dataset files.""",
        """- Python, RAG architectures (LangChain / LlamaIndex)
- Web UI development (Streamlit / Gradio)
- Fact verification methodologies""",
        """- Working evidence-grounded prototype
- Annotated source document corpus
- Empirical evaluation paper""",
        """Infogen (Ghosh et al., 2025), LIDA (Dibia, 2023)"""
    )

    doc += format_project_block(
        "Project TH-04",
        "Translating Natural-Language Graph Design Prompts into Layout Transformations",
        "Dr. Tony Huang",
        "weidong.huang@uts.edu.au",
        "Graph Drawing & LLM Parsing",
        "Large Language Models, Graph Drawing, NetworkX, Graphviz, Python",
        """Users frequently request graph layout changes in plain language ('separate clusters', 'reduce crossings'), but layout algorithms require complex code parameters.""",
        """Asking LLMs to generate node coordinates directly is unreliable and produces invalid graph layouts.""",
        """- Design a 'Graph Layout Intent Language' encoding hard and soft visual constraints.
- Develop an LLM parser converting natural prompts into structured layout specifications.
- Connect specifications to layout engines (NetworkX, Graphviz, D3).""",
        """- Collect natural language graph editing requests.
- Train/prompt LLMs to parse requests into validated JSON layout instructions.""",
        """Annotated dataset of natural language graph design prompts.""",
        """- Python / JavaScript, Graph Theory & NetworkX
- Prompt engineering & JSON schema validation""",
        """- Graph Layout Intent Language specification
- Natural language to graph layout parser codebase
- Empirical evaluation research paper""",
        """Ask and You Shall Receive (Di Bartolomeo et al., 2023), Chat2VIS (Maddigan & Susnjak, 2023)"""
    )

    # -------------------------------------------------------------
    # Section 3: Professorial Projects (15 Projects)
    doc += "\n\n# SECTION 3: PROFESSORIAL & ACADEMIC RESEARCH PROJECTS (OTHER FACULTY)\n\n"

    doc += format_project_block(
        "Project AD-01",
        "AI-Driven Credit / Cyber Risk Modeling",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Financial AI & Cyber Risk",
        "Deep Learning, Machine Learning, Statistical Risk Modeling, Credit Risk, Python",
        """Financial institutions require high default prediction accuracy without losing the interpretability of traditional credit scoring models.""",
        """Pure deep learning models lack interpretability for regulatory credit approval.""",
        """- Combine predictive machine learning with interpretable statistical models.
- Enhance credit default and cyber risk classification.
- Evaluate risk prediction accuracy and explainability.""",
        """- Train hybrid ML/statistical risk models on financial institution datasets.
- Apply XAI techniques to explain default factors.""",
        """Financial risk dataset (available upon request from Dr. Alice Dong).""",
        """- Python, statistical risk modeling, ML fundamentals""",
        """- Hybrid risk prediction model
- Empirical evaluation report""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AD-02",
        "Multimodal Modeling for Financial Time-Series Forecasting (Mamba & TimeSformer)",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Quant Finance & Deep Learning",
        "Mamba, TimeSformer, PyTorch, Time-Series Forecasting, Portfolio Optimization",
        """Accurate asset return covariance matrix forecasting is vital for mean-variance portfolio optimization and risk management.""",
        """Traditional time-series models (GARCH) struggle to capture complex spatial and temporal asset co-movements across large portfolios.""",
        """- Adapt Mamba (state space models) and TimeSformer (video transformers) to financial return series.
- Model multivariate temporal sequences to forecast time-varying covariance matrices.
- Integrate covariance forecasts into mean-variance portfolio optimization.""",
        """- Represent multivariate asset returns as 2D spatiotemporal tensors.
- Train TimeSformer / Mamba architectures for dynamic covariance matrix prediction.""",
        """Financial asset return dataset (available upon request from Dr. Alice Dong).""",
        """- PyTorch, deep learning time-series modeling
- Quantitative finance & portfolio theory""",
        """- Spatiotemporal covariance forecasting model
- Portfolio backtesting results (Sharpe ratio, max drawdown)""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AD-03",
        "Generative AI-Powered Ambient Eco-Visualization for Sustainability",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Sustainability & AI Art / Viz",
        "Generative AI, Eco-Visualization, Ambient Intelligence, Web Displays, Python",
        """Promoting household energy conservation requires continuous, non-intrusive feedback that inspires behavioral changes.""",
        """Numeric smart meter dashboards have low long-term user engagement.""",
        """- Design AI-driven ambient digital visualizations based on simulated household energy usage data.
- Dynamically transform visual art displays to reflect real-time energy conservation patterns.""",
        """- Process smart meter energy datasets into ambient art rendering parameters.""",
        """Simulated energy consumption datasets (available upon request).""",
        """- Python / JS, web display frameworks, Generative AI art tools""",
        """- Ambient eco-visualization digital display prototype
- User engagement study report""",
        """Eco-visualization (Holmes, 2007), Smart Home Ambient Intelligence (Makonin et al., 2013)"""
    )

    doc += format_project_block(
        "Project AD-04",
        "Personalized Financial Visualizations via Bayesian Framework",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Explainable AI & Financial Viz",
        "Bayesian Framework, Adaptive UI, XAI, Financial Analytics, Python",
        """Non-expert investors find complex AI financial predictions difficult to understand.""",
        """Fixed financial charts do not adapt explanations based on individual user expertise.""",
        """- Build a Bayesian framework that updates visual explanations dynamically based on real-time user interaction.
- Personalize complex AI financial insights for varying user knowledge levels.""",
        """- Implement Bayesian parameter update model tracking user comprehension signals.""",
        """Financial analytics interaction dataset (available upon request).""",
        """- Python, Bayesian statistics, interactive UI design""",
        """- Adaptive Bayesian financial visualization prototype
- User comprehension study report""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AD-05",
        "Graph-Based XAI for Fraud Detection",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Graph ML & Fraud Detection",
        "Graph Neural Networks (GNNs), Explainable AI (XAI), Network Visualization, Python",
        """Financial fraud and money laundering occur across intricate transaction networks that standard tabular ML models fail to detect.""",
        """Lack of network visual explainability in fraud detection systems.""",
        """- Represent financial transactions as graph networks.
- Apply Graph Neural Networks (GNNs) and XAI to highlight suspicious transaction rings.
- Provide interactive graph visualizations for compliance analysts.""",
        """- Train GNN fraud detection models and apply GNNExplainer for subgraph visualization.""",
        """Banking transaction dataset (available upon request).""",
        """- Python, PyTorch Geometric / NetworkX, XAI techniques""",
        """- Graph-based fraud detection pipeline
- Interactive network XAI visualization interface""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AD-06",
        "Multi-Dimensional Financial Risk Visualization",
        "Dr. Alice Dong",
        "xiaodan.dong@uts.edu.au",
        "Risk Analytics & Visualization",
        "Explainable AI (XAI), Risk Assessment, Portfolio Management, Multi-Dimensional Viz",
        """Portfolio managers struggle to break down complex multi-dimensional risk exposure across market regimes.""",
        """Lack of transparent risk factor decomposition in automated portfolio tools.""",
        """- Develop an XAI multi-dimensional risk visualization framework.
- Break down portfolio risk drivers into interactive visual representations.""",
        """- Process financial risk datasets into multi-dimensional factor models.""",
        """Financial Risk dataset (available upon request).""",
        """- Python, risk analytics, data visualization""",
        """- Multi-dimensional risk dashboard
- Empirical evaluation report""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AA-01",
        "Distributed Small Language Models with Federated Learning",
        "Dr. Ali Anaissi",
        "ali.anaissi@uts.edu.au",
        "Distributed AI & Privacy",
        "Small Language Models (SLMs), Federated Learning, OpenFedLLM, Python, PyTorch",
        """Organizations want domain-specific AI assistance without centralizing sensitive private data.""",
        """Centralized LLM fine-tuning risks private data leaks.""",
        """- Develop a distributed Small Language Model (SLM) framework using Federated Learning.
- Train models across decentralized nodes while protecting raw text privacy.
- Benchmark decentralized response quality against centralized SLMs.""",
        """- Deploy OpenFedLLM framework across simulated private nodes.""",
        """OpenfedLLM datasets & AllenAI open data.""",
        """- Python, PyTorch, Federated Learning, SLM fine-tuning""",
        """- Distributed FL-SLM training framework
- Privacy & response benchmark report""",
        """OpenFedLLM (ACM 2024), LLMs + Federated Learning (Patterns 2024)"""
    )

    doc += format_project_block(
        "Project AA-02",
        "Omics Imagification for Cell-Type Classification Using Deep Learning",
        "Dr. Ali Anaissi",
        "ali.anaissi@uts.edu.au",
        "Bioinformatics & Deep Learning",
        "Deep Learning, CNNs, Omics Imagification, Fotomics, PyTorch, Python",
        """High-dimensional single-cell omics data is difficult to classify using traditional tabular ML.""",
        """Tabular ML ignores spatial feature co-expression structures.""",
        """- Transform 1D single-cell omics vectors into structured 2D RGB images ('imagification').
- Train CNNs on transformed omics images for cell-type classification.
- Benchmark classification performance against standard tabular ML.""",
        """- Implement Fotomics Fourier-transform imagification pipeline.
- Train ResNet / ViT image classifiers on converted omics datasets.""",
        """Single-cell omics benchmark datasets (Fotomics GitHub repository).""",
        """- Python, PyTorch, Bioinformatics data analysis""",
        """- Omics imagification preprocessing library
- Cell-type classification model & evaluation report""",
        """Fotomics (Springer 2022)"""
    )

    doc += format_project_block(
        "Project AA-03",
        "Crime Prediction Using SpatioTemporal Data and Machine Learning",
        "Dr. Ali Anaissi",
        "ali.anaissi@uts.edu.au",
        "Spatiotemporal Analytics & Urban AI",
        "Machine Learning, Spatiotemporal GNNs, LSTMs, Folium, QGIS, Python",
        """Urban police departments require proactive spatial forecasting of crime hotspots.""",
        """Standard spatial regression models miss temporal trends and socioeconomic interactions.""",
        """- Integrate open crime data with geospatial, weather, and socioeconomic indicators.
- Train Spatiotemporal GNNs, Random Forests, and LSTMs for crime hotspot forecasting.
- Visualize spatial risk maps using Folium / QGIS.""",
        """- Engineer spatial features (population density, police station proximity).
- Train spatiotemporal forecast models.""",
        """US Open Crime Data Portal & UK Police Data.""",
        """- Python, Geospatial analytics (QGIS, Folium, GeoPandas)
- Spatiotemporal ML / GNNs""",
        """- Spatiotemporal crime prediction pipeline
- Interactive crime risk map
- Model benchmark evaluation paper""",
        """Deep Learning Spatiotemporal Crime Prediction (arXiv 2024)"""
    )

    doc += format_project_block(
        "Project DHR-01",
        "Empirical Validation of Corporate AI Governance Architectures (CAIGA)",
        "Dr. David Hason Rudd",
        "david.hasonrudd@uts.edu.au",
        "AI Governance & Compliance Modeling",
        "Machine Learning, Corporate AI Governance, Governance Modeling, Python, Statistics",
        """Enterprise AI adoption outpaces formal governance frameworks, creating compliance and ethical failure risks.""",
        """Lack of empirical data validation for corporate AI risk classification architectures.""",
        """- Compile structured governance data from AIID, Stanford HAI AI Index, and OECD.
- Quantify the governance implementation gap across corporate sectors.
- Train ML classifiers to predict corporate CAIGA risk tiers and benchmark governance maturity.""",
        """- Harmonize enterprise survey data from EY, McKinsey, PwC.
- Train Gradient Boosted Trees to classify enterprise AI risk levels.""",
        """AI Incident Database (AIID), Stanford HAI AI Index, OECD AI Policy Observatory.""",
        """- Python, statistical modeling, machine learning classification
- AI ethics & governance policy knowledge""",
        """- CAIGA empirical validation dataset
- Corporate AI risk prediction model
- Published governance research report""",
        """OECD AI Recommendation (2019), BoE PRA SS1/23 (2023)"""
    )

    doc += format_project_block(
        "Project DHR-02",
        "Generative AI-Enhanced Spatial-Temporal Inference for 3D Indoor 5G Coverage Mapping",
        "Dr. David Hason Rudd",
        "david.hasonrudd@uts.edu.au",
        "Generative AI & 5G Telecom",
        "Generative AI, GANs, Diffusion Models, Graph Attention Networks (TA-GAT), PyTorch",
        """80% of 5G data occurs indoors, but high-frequency 5G signals attenuate severely through building materials. Inferring indoor signal maps from outdoor drone scans is a complex inversion problem.""",
        """Scarcity of labeled indoor signal strength training data.""",
        """- Use Generative AI (GANs / Diffusion Models) to synthesize indoor 3D signal propagation data.
- Improve prediction accuracy of Received Signal Strength (RSSI) and Channel Quality (CQI).
- Benchmark model robustness on unseen building layouts.""",
        """- Train GANs conditioned on drone scan seeds and CAD wall structures.
- Augment TA-GAT indoor signal predictor.""",
        """5G outdoor drone scan & building layout dataset (available upon request).""",
        """- PyTorch, Generative AI (GANs/Diffusion), Graph Neural Networks""",
        """- Generative 3D signal augmentation pipeline
- 5G indoor coverage prediction model & paper""",
        """Drone-based ML for 5G Coverage (Rudd et al., KES 2025)"""
    )

    doc += format_project_block(
        "Project JZ-01",
        "Large Language Model Chatbots for Mental Health Support",
        "Dr. Jianlong Zhou",
        "jianlong.zhou@uts.edu.au",
        "Healthcare AI & Conversational LLMs",
        "Large Language Models, Mental Health Chatbots, Conversational UI, User Study, Python",
        """Conversational LLM chatbots can deliver accessible mental health support, but require tailored interaction features and safety boundaries.""",
        """Lack of user study evidence on key LLM UI factors for mental health support.""",
        """- Conduct a literature review on state-of-the-art mental health LLM chatbots.
- Develop an LLM-powered conversational mental health support chatbot prototype.
- Execute a user evaluation study to test chatbot support effectiveness.""",
        """- Fine-tune / prompt open LLM for supportive dialogue.
- Build web UI and run human participant study.""",
        """Mental health dialogue datasets & user study feedback.""",
        """- Python, LLM APIs, web UI development
- User study design & HCI evaluation""",
        """- Mental health LLM chatbot prototype
- User study evaluation paper""",
        """The Typing Cure (arXiv 2024), LLM Workplace Well-being (ACM 2024)"""
    )

    doc += format_project_block(
        "Project JZ-02",
        "Bridging the AI Divide: Empowering Users through AI Literacy",
        "Dr. Jianlong Zhou",
        "jianlong.zhou@uts.edu.au",
        "Human-AI Interaction & AI Literacy",
        "Large Language Models, AI Literacy, Human-AI Interaction, User Study, Python",
        """Non-technical communities (e.g. farmers) are excluded from AI conversations, creating a digital AI divide.""",
        """Lack of tailored frameworks to explain AI benefits from specific user perspectives.""",
        """- Explore LLM approaches that translate AI concepts tailored to non-technical user backgrounds.
- Conduct user studies evaluating user AI literacy improvements.""",
        """- Develop LLM explainability prompts customized for specific user archetypes.""",
        """User survey & AI literacy evaluation datasets.""",
        """- Python, LLM prompting, HCI user study methods""",
        """- AI literacy translation framework
- User study evaluation paper""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AB-01",
        "Agentic AI for Early Detection of Weather Extremes",
        "Dr. Arnick Abdollahi",
        "arnick.abdollahi@uts.edu.au",
        "Climate AI & Agentic Systems",
        "Agentic AI, Large Language Models, Time-Series Analytics, Anomaly Detection, Python",
        """Climate change creates unprecedented extreme weather events that fall outside historical regression patterns.""",
        """Traditional forecasting struggles to identify emerging unobserved extreme climate anomalies.""",
        """- Develop a multi-agent AI framework to continuously monitor climate streams.
- Identify anomalous weather conditions and compare them against historical norms.
- Generate interpretable early warning risk recommendations for decision-makers.""",
        """- Build multi-agent workflow (Agentic LLMs + time-series anomaly detection).""",
        """Historical climate & weather stream datasets.""",
        """- Python, Agentic AI frameworks (CrewAI / LangGraph)
- Time-series analytics & anomaly detection""",
        """- Multi-agent extreme weather detection system
- Climate risk intelligence benchmark report""",
        """N/A"""
    )

    doc += format_project_block(
        "Project AB-02",
        "Data Science & Satellite Approaches for Bushfire Prediction",
        "Dr. Arnick Abdollahi",
        "arnick.abdollahi@uts.edu.au",
        "Remote Sensing & Bushfire Risk",
        "Machine Learning, Remote Sensing, Satellite Data, Explainable AI (XAI), Python",
        """Bushfires pose severe risks across Australia. Effective management requires predicting fire likelihood before ignition occurs.""",
        """Complex spatiotemporal interactions between satellite vegetation indices and weather variables.""",
        """- Combine satellite observations (Sentinel/MODIS) with weather and historical fire records.
- Train predictive ML models to estimate bushfire occurrence likelihood across space and time.
- Apply Explainable AI (XAI) to identify key environmental fire drivers.""",
        """- Engineer spatiotemporal satellite features and train Random Forest / XGBoost classifiers.""",
        """Satellite remote sensing imagery & Australian historical bushfire datasets.""",
        """- Python, Geospatial remote sensing, ML & XAI""",
        """- Bushfire occurrence prediction model
- XAI feature importance report
- Research paper manuscript""",
        """XAI for Bushfire Occurrence Prediction (Science of Total Environment 2023)"""
    )

    doc += format_project_block(
        "Project MK-01",
        "Evolutionary Optimization of a Risk-Aware Clinical System for Mental Health Triage",
        "Dr. Mir Md Jahangir Kabir",
        "mirmdjahangir.kabir@uts.edu.au",
        "Healthcare AI & Evolutionary Optimization",
        "Genetic Algorithms, Evolutionary Optimization, Mental Health Triage, PyTorch, Python",
        """Clinical decision support systems in mental health must simultaneously balance empathy, safety protocols, and structural coherence.""",
        """Single-objective ML models produce either rigid or unsafe conversational responses.""",
        """- Implement a Genetic Algorithm (GA) to evolve an interpretable genome controlling response policies.
- Formulate a constrained multi-objective fitness function with hard safety penalties.
- Evaluate clinical safety and empathy convergence against human clinical standards.""",
        """- Evolve policy parameters over mental health interaction datasets.""",
        """DAIC-WOZ, CLPsych Suicide Risk Assessment Datasets.""",
        """- Python, Genetic Algorithms / Evolutionary Computation
- NLP & clinical safety metrics""",
        """- Evolutionary mental health triage framework
- Clinical safety evaluation report""",
        """Promptbreeder (ICML 2024), GenDLN (ACL 2025)"""
    )

    doc += format_project_block(
        "Project MK-02",
        "Financial Text Understanding Using LLMs: Earnings Call Transcripts",
        "Dr. Mir Md Jahangir Kabir",
        "mirmdjahangir.kabir@uts.edu.au",
        "Financial NLP & LLM Evaluation",
        "Large Language Models, Financial NLP, Sentiment Analysis, Prompt Tuning, Python",
        """Earnings call transcripts are dense with financial jargon, executive hedging, and forward-looking statements.""",
        """Uncertainty regarding LLM interpretability and performance in parsing domain-specific financial earnings calls.""",
        """- Empirically evaluate LLMs (GPT-4, LLaMA, Claude) on financial sentiment and trend prediction.
- Compare LLM performance against FinBERT baselines.
- Develop domain-specific financial text interpretability metrics.""",
        """- Segment earnings calls into executive vs analyst turns.
- Evaluate prompt tuning strategies for financial sentiment classification.""",
        """S&P 500 earnings call transcripts (SeekingAlpha / Bloomberg / EDGAR).""",
        """- Python, HuggingFace Transformers, LLM APIs
- Financial text analysis""",
        """- Financial LLM benchmark dataset
- Empirical evaluation research paper""",
        """FinBERT (Araci, 2019), Financial Prompt Tuning (ACL 2023)"""
    )

    doc += format_project_block(
        "Project MK-03",
        "Evolutionary Reward Shaping for Reinforcement Learning Agents",
        "Dr. Mir Md Jahangir Kabir",
        "mirmdjahangir.kabir@uts.edu.au",
        "Reinforcement Learning & Evolutionary Algos",
        "Reinforcement Learning, Genetic Algorithms, Gymnasium, Q-Learning, PyTorch, Python",
        """Poorly designed reward functions lead to slow convergence and unstable learning in RL agents.""",
        """Manual reward engineering is time-consuming and prone to unintended agent behaviors.""",
        """- Apply Genetic Algorithms to automatically generate and optimize reward functions for RL agents.
- Train agents in Gymnasium / MiniGrid benchmark environments.
- Compare learning efficiency between manual and evolved reward functions.""",
        """- Evolve reward function parameters using Genetic Algorithms based on cumulative agent rewards.""",
        """Gymnasium & MiniGrid simulated benchmark environments.""",
        """- Python, Reinforcement Learning (Gymnasium, Deep Q-Networks)
- Evolutionary algorithms""",
        """- Evolutionary reward shaping codebase
- Learning curve benchmark evaluation report""",
        """EVO-RL (Hallawa et al., 2020), Sutton & Barto (2018)"""
    )

    doc += format_project_block(
        "Project MK-04",
        "Automated Portfolio Management Using RL and Evolutionary Algorithms",
        "Dr. Mir Md Jahangir Kabir",
        "mirmdjahangir.kabir@uts.edu.au",
        "Quant Trading & RL",
        "Reinforcement Learning, Genetic Algorithms, Portfolio Optimization, PyTorch, Python",
        """Financial markets are highly volatile, making static investment strategies suboptimal.""",
        """Balancing multi-objective trade-offs between returns, volatility, and max drawdown under delayed rewards.""",
        """- Combine Deep Q-Learning / Policy Gradients with Genetic Algorithms for portfolio rebalancing.
- Evolve reward functions and portfolio constraints using market data.
- Benchmark system performance using Sharpe ratio, max drawdown, and cumulative returns.""",
        """- Train RL agents on historical stock price data to dynamically adjust asset weights.""",
        """Yahoo Finance Historical Data & Kaggle Financial Datasets.""",
        """- Python, Reinforcement Learning, Portfolio Theory""",
        """- Automated RL trading & portfolio management system
- Financial backtesting benchmark paper""",
        """Learning to Trade via Direct RL (Moody & Saffell, 2001), Twin-System RRL (Wang et al., 2024)"""
    )

    OUT_FILE.write_text(doc, encoding='utf-8')
    print(f"Successfully generated 100% uniform detailed guide at: {OUT_FILE} ({len(doc)} bytes)")

if __name__ == '__main__':
    parse_and_build()
