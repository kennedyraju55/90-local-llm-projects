<div align="center">

![Medical Terms Explainer Banner](docs/images/banner.svg)

# 🏥 Medical Terms Explainer

### AI-Powered Medical Terminology Decoder

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-2ec4b6?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-2ec4b6?style=for-the-badge&logo=heart&logoColor=white)]()
[![Privacy](https://img.shields.io/badge/Privacy-100%25_Local-success?style=for-the-badge&logo=lock&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

</div>

---

> ## ⚠️ Medical Disclaimer
>
> **This tool is for educational purposes only. It is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns. Never disregard professional medical advice or delay seeking it because of information from this tool.**
>
> - 🚨 **Call 911** for medical emergencies
> - 📞 **Call 988** for mental health crises (Suicide & Crisis Lifeline)
> - 💬 **Text HOME to 741741** for Crisis Text Line
>
> *The developers assume no liability for any actions taken based on this tool's output.*

---

<div align="center">

[✨ Features](#-features) · [🚀 Quick Start](#-quick-start) · [💻 CLI Reference](#-cli-reference) · [🏗️ Architecture](#️-architecture) · [📖 API Reference](#-api-reference) · [❓ FAQ](#-faq)

</div>

---

## 📋 Overview

A comprehensive medical terminology tool that explains complex medical terms in plain language, provides pronunciation guides, visual aids, related conditions, and decodes 50+ common medical abbreviations — all powered by local LLMs.

Built as part of the **Local LLM Projects** series (Project #83/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 📖 | **Plain Language** | Complex medical terms explained in everyday language |
| 🗣️ | **Pronunciation Guide** | Phonetic pronunciations for 20+ medical terms |
| 🔬 | **Visual Aids** | Anatomy diagram references for organs and systems |
| 🔗 | **Related Conditions** | Discover related conditions and comorbidities |
| 📝 | **50+ Abbreviations** | Decode common medical abbreviations (BP, MRI, ECG, etc.) |
| 📚 | **3 Detail Levels** | Brief, standard, or comprehensive explanations |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Multi-Level Explanations** | Three detail levels: brief, standard, comprehensive for any medical term |
| **Pronunciation Guide** | Phonetic pronunciations for 20+ commonly mispronounced medical terms |
| **Visual Aid References** | Anatomy diagram references for heart, brain, lungs, and more |
| **Related Conditions** | Maps 8+ conditions to related conditions and comorbidities |
| **Abbreviation Decoder** | 50+ medical abbreviations with full meanings and search capability |
| **Batch Processing** | Explain multiple medical terms in a single command |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.10+ | Runtime environment |
| **Ollama** | Latest | Local LLM inference engine |
| **LLM Model** | llama3.2 | AI model (downloaded via Ollama) |

### Installation

`ash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/medical-terms-explainer.git
cd 83-medical-terms-explainer

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure Ollama is running with a model
ollama pull llama3.2
ollama serve
`

### First Run

`ash
# Verify installation
medical-terms-explainer --help

# Run your first command
medical-terms-explainer explain --term "myocardial infarction"
`

### Expected Output

`
╭─────────────────────────────────────────────────────────────╮
│  ⚠️  MEDICAL DISCLAIMER                                     │
│  This tool is for educational purposes only.                │
│  Always consult a qualified healthcare provider.            │
╰─────────────────────────────────────────────────────────────╯

⏳ Analyzing with local LLM...

╭─────────────────────────────────────────────────────────────╮
│  ✅ Analysis Complete                                        │
│                                                             │
│  [AI-generated response based on your input]                │
│                                                             │
│  ⚠️  Remember: This is not medical advice.                  │
╰─────────────────────────────────────────────────────────────╯
`


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/medical-terms-explainer.git
cd medical-terms-explainer
docker compose up

# Access the web UI
open http://localhost:8501
```

### Docker Commands

| Command | Description |
|---------|-------------|
| `docker compose up` | Start app + Ollama |
| `docker compose up -d` | Start in background |
| `docker compose down` | Stop all services |
| `docker compose logs -f` | View live logs |
| `docker compose build --no-cache` | Rebuild from scratch |

### Architecture

```
┌─────────────────┐     ┌─────────────────┐
│   Streamlit UI  │────▶│   Ollama + LLM  │
│   Port 8501     │     │   Port 11434    │
└─────────────────┘     └─────────────────┘
```

> **Note:** First run will download the Gemma 4 model (~5GB). Subsequent starts are instant.

---


---


---

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.medical_terms.api:app --reload --port 8000

# Or with Docker
docker compose up
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |
| `POST` | `/analyze` | Main analysis endpoint |

### Example Request

```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "your input here"}'
```

> 📖 Visit `http://localhost:8000/docs` for the full interactive API documentation.

## 💻 CLI Reference

| Command | Description |
|---------|-------------|
| explain | Explain a medical term with pronunciation and visual aids |
| batch | Explain multiple terms at once |
| abbreviation | Decode a single medical abbreviation |
| abbreviations | List all 50+ medical abbreviations |
| search | Search abbreviations by keyword |
| pronounce | Show pronunciation for a medical term |

### explain

`ash
medical-terms-explainer explain --term "myocardial infarction"
`

### batch

`ash
medical-terms-explainer batch --terms "hypertension, tachycardia, edema"
`

### abbreviation

`ash
medical-terms-explainer abbreviation --abbr "MRI"
`

### abbreviations

`ash
medical-terms-explainer abbreviations
`

### search

`ash
medical-terms-explainer search --query "blood"
`

### pronounce

`ash
medical-terms-explainer pronounce --term "pneumonia"
`

### Global Options

`ash
medical-terms-explainer --help          # Show all commands and options
medical-terms-explainer --version       # Show version information
`

---

## 🌐 Web UI

This project includes a web-based interface for browser-based interaction.

`ash
# Start the web server
cd web
python app.py

# Open in browser
# http://localhost:5000
`

| Feature | Description |
|---------|-------------|
| **Responsive Design** | Works on desktop and mobile browsers |
| **Real-Time Analysis** | Live streaming responses from local LLM |
| **Dark Mode** | Easy on the eyes with dark theme support |
| **Export Results** | Download analysis results as text files |

> ⚠️ **Note**: The web UI connects to your local Ollama instance. No data leaves your machine.

---

## 🏗️ Architecture

<div align="center">

![Architecture Diagram](docs/images/architecture.svg)

</div>

### Project Structure

`
83-medical-terms-explainer/
├── src/
│   └── medical_terms_explainer/
│       ├── __init__.py
│       ├── core.py          # Core logic and LLM integration
│       └── cli.py           # Click CLI commands
├── tests/
│   ├── __init__.py
│   └── test_core.py         # Unit tests
├── docs/
│   └── images/
│       ├── banner.svg        # Project banner
│       ├── architecture.svg  # Architecture diagram
│       └── features.svg      # Feature grid
├── config.yaml              # Model configuration
├── requirements.txt         # Python dependencies
└── README.md                # This file
`

### Data Flow

`
User Input → CLI/Web Interface → Core Engine → LLM (Ollama) → Response
                                      ↓
                              Built-in Databases
                              (patterns, rules, references)
`

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **CLI** | Click | Command-line interface framework |
| **UI** | Rich | Beautiful terminal formatting |
| **AI** | Ollama | Local LLM inference |
| **Web** | Flask | Web interface (optional) |
| **Config** | YAML | Configuration management |
| **Testing** | pytest | Unit and integration tests |

---

## 📖 API Reference

### Core Functions

`python
from medical_terms_explainer.core import explain_term, get_pronunciation, decode_abbreviation

# Explain a medical term
explanation = explain_term("myocardial infarction", detail_level="comprehensive")
print(explanation)

# Get pronunciation
pronunciation = get_pronunciation("pneumothorax")
# Returns: "noo-moh-THOR-aks"

# Decode abbreviation
meaning = decode_abbreviation("ECG")
# Returns: "Electrocardiogram"
`

### Configuration

`yaml
# config.yaml
model: llama3.2
temperature: 0.3
max_tokens: 1024
base_url: http://localhost:11434
`

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| OLLAMA_BASE_URL | http://localhost:11434 | Ollama API endpoint |
| OLLAMA_MODEL | llama3.2 | Default LLM model |
| LOG_LEVEL | INFO | Logging verbosity |

---

## 🧪 Testing

`ash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src/medical_terms_explainer --cov-report=html

# Run specific test file
pytest tests/test_core.py -v

# Run with verbose output
pytest -v --tb=short
`

### Test Categories

| Category | Description | Command |
|----------|-------------|---------|
| **Unit Tests** | Core logic validation | pytest tests/test_core.py |
| **CLI Tests** | Command-line interface tests | pytest tests/test_cli.py |
| **Integration** | End-to-end with LLM | pytest tests/test_integration.py |

---

## 🔄 Local vs Cloud Comparison

| Aspect | Local LLM (This Tool) | Cloud API |
|--------|----------------------|-----------|
| **Privacy** | ✅ 100% local — data never leaves your machine | ❌ Data sent to external servers |
| **Cost** | ✅ Free after setup | ❌ Pay per API call |
| **Speed** | ⚡ Depends on hardware | ⚡ Generally fast |
| **Internet** | ✅ Works offline | ❌ Requires connection |
| **Data Control** | ✅ Complete control | ❌ Third-party storage |
| **HIPAA Concerns** | ✅ No data transmission | ⚠️ BAA required |
| **Model Updates** | 🔄 Manual model pulls | ✅ Automatic updates |
| **Scalability** | ⚠️ Limited by hardware | ✅ Cloud-scale |

> 🔒 **For healthcare data, local LLM inference eliminates the risk of sensitive information exposure through network transmission.**

---

## ❓ FAQ

<details>
<summary><strong>Can I use this to understand my medical reports?</strong></summary>
<br>

This tool can help you understand medical terminology in your reports, but it cannot interpret your specific results. Always discuss your medical reports with your healthcare provider who understands your complete medical context.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How accurate are the explanations?</strong></summary>
<br>

Explanations are generated by an AI model and may contain inaccuracies. They are meant as educational starting points. For clinical accuracy, refer to medical textbooks or consult healthcare professionals.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Are the pronunciation guides reliable?</strong></summary>
<br>

The pronunciation guides cover commonly mispronounced terms using simplified phonetics. Medical pronunciation can vary by region. When in doubt, ask your healthcare provider.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can medical students use this for studying?</strong></summary>
<br>

It can be a helpful supplementary study tool, but should NOT replace medical textbooks, lectures, or clinical training. Always cross-reference with authoritative medical sources.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Does it cover specialized medical terminology?</strong></summary>
<br>

The LLM can explain terms across many specialties, but depth varies. Common terms are well-covered; rare or highly specialized terms may have less accurate explanations.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Abbreviation Quick Reference

### Common Medical Abbreviations (Built-in Database)

<details>
<summary><strong>Diagnostic and Imaging (15 abbreviations)</strong></summary>

| Abbreviation | Full Meaning |
|-------------|-------------|
| MRI | Magnetic Resonance Imaging |
| CT | Computed Tomography |
| ECG/EKG | Electrocardiogram |
| EEG | Electroencephalogram |
| PET | Positron Emission Tomography |
| CBC | Complete Blood Count |
| BMP | Basic Metabolic Panel |
| CMP | Comprehensive Metabolic Panel |
| A1C | Glycated Hemoglobin |
| TSH | Thyroid-Stimulating Hormone |
| PSA | Prostate-Specific Antigen |
| BMI | Body Mass Index |
| BP | Blood Pressure |
| HR | Heart Rate |
| SpO2 | Peripheral Oxygen Saturation |

</details>

<details>
<summary><strong>Clinical Terms (15 abbreviations)</strong></summary>

| Abbreviation | Full Meaning |
|-------------|-------------|
| Dx | Diagnosis |
| Tx | Treatment |
| Rx | Prescription |
| Hx | History |
| Sx | Symptoms |
| Fx | Fracture |
| PRN | As Needed (Pro Re Nata) |
| BID | Twice Daily |
| TID | Three Times Daily |
| QID | Four Times Daily |
| QD | Once Daily |
| NPO | Nothing By Mouth |
| STAT | Immediately |
| PO | By Mouth (Per Os) |
| IV | Intravenous |

</details>

<details>
<summary><strong>Conditions and Departments (20 abbreviations)</strong></summary>

| Abbreviation | Full Meaning |
|-------------|-------------|
| CHF | Congestive Heart Failure |
| COPD | Chronic Obstructive Pulmonary Disease |
| DVT | Deep Vein Thrombosis |
| PE | Pulmonary Embolism |
| MI | Myocardial Infarction |
| CVA | Cerebrovascular Accident (Stroke) |
| DM | Diabetes Mellitus |
| HTN | Hypertension |
| UTI | Urinary Tract Infection |
| URI | Upper Respiratory Infection |
| ED/ER | Emergency Department/Room |
| ICU | Intensive Care Unit |
| OR | Operating Room |
| OB/GYN | Obstetrics and Gynecology |
| ENT | Ear, Nose, and Throat |
| GI | Gastrointestinal |
| Ortho | Orthopedics |
| Neuro | Neurology |
| Peds | Pediatrics |
| Psych | Psychiatry |

</details>

### Detail Level Comparison

| Level | Output Style | Best For |
|-------|-------------|----------|
| **Brief** | 1-2 sentence definition | Quick lookups |
| **Standard** | Paragraph with context | General understanding |
| **Comprehensive** | Full explanation with examples, causes, treatments | Deep learning |

> AI-generated explanations may contain inaccuracies. Always verify with authoritative medical sources.


---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (git checkout -b feature/amazing-feature)
3. **Commit** your changes (git commit -m 'Add amazing feature')
4. **Push** to the branch (git push origin feature/amazing-feature)
5. **Open** a Pull Request

### Development Setup

`ash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/medical-terms-explainer.git
cd 83-medical-terms-explainer

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black flake8

# Run linting
black src/
flake8 src/

# Run tests before submitting
pytest -v
`

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⚠️ Important Reminder

**This tool is for educational and informational purposes only.**
**It is NOT a substitute for professional medical advice, diagnosis, or treatment.**
**Always seek the advice of your physician or other qualified health provider.**

---

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #83/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
