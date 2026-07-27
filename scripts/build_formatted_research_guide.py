#!/usr/bin/env python3
"""
Script to format and structure 36126 Innovation Lab Research Projects Detailed Guide.
Cleans raw text, formats headings, structures project metadata, and bolds key technical terms.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "llm-wiki" / "02-subjects" / "36126-innovation-lab-research-project" / "sources" / "raw"
OUT_FILE = ROOT / "llm-wiki" / "02-subjects" / "36126-innovation-lab-research-project" / "sources" / "research-projects-detailed-guide-2026.md"

def clean_text(text: str) -> str:
    # Remove weird non-printable / control chars (like \u2028 \u2029 \r)
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = text.replace('\u2028', '\n').replace('\u2029', '\n').replace('\x0c', '\n')
    # Clean multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def bold_keywords(text: str) -> str:
    # List of key technologies and terms to highlight
    keywords = [
        r"Large Language Models?", r"LLMs?", r"Generative AI", r"GenAI", r"Deep Learning",
        r"Machine Learning", r"Reinforcement Learning", r"Federated Learning", r"Vision Transformers?",
        r"ViT", r"Convolutional Neural Networks?", r"CNNs?", r"Graph Neural Networks?", r"GNNs?",
        r"Explainable AI", r"XAI", r"Retrieval-Augmented Generation", r"RAG", r"Mamba", r"TimeSformer",
        r"Genetic Algorithms?", r"Evolutionary Algorithms?", r"OpenCV", r"PyTorch", r"TensorFlow",
        r"Python", r"Streamlit", r"React", r"Gymnasium", r"OpenAI Gym", r"Ollama", r"LM Studio",
        r"YOLO", r"Mask R-CNN", r"Bayesian [Ff]ramework", r"S&P 500", r"SeekingAlpha", r"Bloomberg",
        r"EDGAR", r"DAIC-WOZ", r"National Construction Code", r"NCC 2025"
    ]
    
    # Avoid bolding inside markdown links or existing bolding
    for kw in keywords:
        pattern = re.compile(r'(?<!\*\*)\b(' + kw + r')\b(?!\*\*)', re.IGNORECASE)
        # Replacing carefully
        text = pattern.sub(r'**\1**', text)
        
    return text

def main():
    p1_raw = (RAW_DIR / 'Project_List_s2_2026.txt').read_text(encoding='utf-8')
    p2_raw = (RAW_DIR / 'MDSI_research_projects_tony_huang.txt').read_text(encoding='utf-8')
    p3_raw = (RAW_DIR / 'MDSI_research_projects_other_professors.txt').read_text(encoding='utf-8')

    c1 = clean_text(p1_raw)
    c2 = clean_text(p2_raw)
    c3 = clean_text(p3_raw)

    header = """---
type: research-projects-guide
status: active
code: "36126"
name: "36126 Innovation Lab: Research Project Topics Detailed Guide"
---

# 36126 Innovation Lab: Research Project Topics Detailed Guide (Spring 2026)

This document contains the complete, formatted, in-depth specifications for all research projects available for **36126 Innovation Lab: Research Project** (Spring 2026).

> [!NOTE]
> All project specifications below include full supervisor contact info, research objectives, background context, dataset availability, required skill prerequisites, and academic reference literature.

---

## 📋 Quick Supervisor Directory

| Supervisor / Partner | Contact Email | Core Domain |
|---|---|---|
| **Dr. Alice Dong** | `xiaodan.dong@uts.edu.au` | Credit/Cyber Risk, Financial Time-Series, Eco-Visualization, Graph XAI |
| **Dr. Ali Anaissi** | `ali.anaissi@uts.edu.au` | Rhinoplasty AI, Omics Deep Learning, Spatiotemporal Crime Prediction |
| **Dr. Arnick Abdollahi** | `arnick.abdollahi@uts.edu.au` | Agentic Weather AI, Satellite Bushfire Prediction |
| **Dr. David Hason Rudd** | `david.hasonrudd@uts.edu.au` | Corporate AI Governance (CAIGA), 3D 5G Spatial Inference |
| **Dr. Jianlong Zhou** | `jianlong.zhou@uts.edu.au` | Human-AI Interaction, XAI, AI Literacy |
| **Dr. Mir Md Jahangir Kabir** | `mirmdjahangir.kabir@uts.edu.au` | Mental Health Triage, Financial LLMs, Evolutionary RL, Quant Portfolio |
| **Dr. Tony Huang** | `weidong.huang@uts.edu.au` | Infographics, Intent Language, LLM Design Critiques, Graph Prompts |
| **Dr. Junaid Akram** | `junaid.akram@uts.edu.au` | Federated Medical Vision-Language, Fake Image Detection, Speech Crisis |
| **Dr. Ali Haidar** (NSW Police) | `ali.haidar@uts.edu.au` | Vehicle Re-ID, Surveillance Video Querying, Traffic Metadata |
| **Dr. Pouya Salpour** | `pouya.salpour@uts.edu.au` | Local Coding LLMs, Automated LLM Assurance |
| **Magtech.ai** | `Mutaz Abu Ghazaleh` | RAG Construction Code Assistant, CAD Floor Slab Vision |
| **MyVal** | `https://www.myval.au/` | Household Asset Image Recognition & Valuation |
| **Decidr** | `tom.allen@decidr.ai` | Enterprise Knowledge Credibility & Fragmented Data |

---

# SECTION 1: FACULTY & INDUSTRY RESEARCH PROJECTS (OFFICIAL PROJECT LIST S2 2026)

"""

    body1 = bold_keywords(c1)
    body2 = bold_keywords(c2)
    body3 = bold_keywords(c3)

    sec2_title = "\n\n---\n\n# SECTION 2: INFOGRAPHICS & HUMAN-AI VISUALIZATION RESEARCH (DR TONY HUANG)\n\n"
    sec3_title = "\n\n---\n\n# SECTION 3: PROFESSORIAL & ACADEMIC RESEARCH PROJECTS (OTHER FACULTY)\n\n"

    full_text = header + body1 + sec2_title + body2 + sec3_title + body3
    
    OUT_FILE.write_text(full_text, encoding='utf-8')
    print(f"Successfully formatted detailed guide at {OUT_FILE} ({len(full_text)} bytes)")

if __name__ == "__main__":
    main()
