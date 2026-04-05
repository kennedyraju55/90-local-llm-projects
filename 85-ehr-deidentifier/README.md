<div align="center">

![EHR De-identifier Banner](docs/images/banner.svg)

# 🏥 EHR De-identifier

### AI-Powered HIPAA-Compliant Data De-identification

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-7209b7?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-7209b7?style=for-the-badge&logo=heart&logoColor=white)]()
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

A powerful EHR (Electronic Health Record) de-identification tool that removes Protected Health Information (PHI) using a dual-layer approach: configurable regex pattern matching followed by LLM-powered analysis — with full audit logging and validation reporting.

Built as part of the **Local LLM Projects** series (Project #85/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🔐 | **HIPAA Safe Harbor** | Targets all 18 HIPAA Safe Harbor identifier types |
| 🔍 | **Dual-Layer Detection** | Regex preprocessing + LLM analysis for thorough de-identification |
| ⚙️ | **Configurable Rules** | 9 toggleable PII detection rules (SSN, phone, email, dates, etc.) |
| 📁 | **Batch Processing** | De-identify entire directories with pattern matching |
| 📋 | **Audit Logging** | Complete audit trail with PII counts and detection types |
| ✅ | **Validation Reports** | Verify de-identification completeness with detailed reports |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **18 HIPAA Identifiers** | Targets all Safe Harbor identifier types: names, dates, SSNs, addresses, and more |
| **Configurable Regex Rules** | 9 toggleable detection rules: SSN, phone, email, dates, MRN, IP, URL, zip codes |
| **Dual-Layer Pipeline** | Step 1: Regex preprocessing catches known patterns; Step 2: LLM catches remaining PHI |
| **Audit Logging** | Complete audit trail tracking operations, PII counts, status, and types detected |
| **Validation Reports** | Verify completeness of de-identification with detailed validation checks |
| **Batch Processing** | Process entire directories with file pattern matching and output organization |

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
git clone https://github.com/kennedyraju55/ehr-deidentifier.git
cd 85-ehr-deidentifier

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
ehr-deidentifier --help

# Run your first command
ehr-deidentifier deidentify --file patient_note.txt --output clean_note.txt
`

### Expected Output

```
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
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/ehr-deidentifier.git
cd ehr-deidentifier
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
uvicorn src.ehr_deidentifier.api:app --reload --port 8000

# Or with Docker
docker compose up
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/docs` | Interactive Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |
| `POST` | `/deidentify` | AI-powered de-identification |
| `POST` | `/deidentify/regex` | Regex-only de-identification |
| `POST` | `/deidentify/configurable` | Configurable regex de-identification |
| `GET` | `/hipaa-identifiers` | List HIPAA identifier categories |
| `GET` | `/disclaimer` | HIPAA disclaimer |

### Example Request

```bash
curl -X POST http://localhost:8000/deidentify \
  -H "Content-Type: application/json" \
  -d '{"text": "Patient John Smith, SSN 123-45-6789"}'
```

> 📖 Visit `http://localhost:8000/docs` for the full interactive API documentation.

## 💻 CLI Reference

| Command | Description |
|---------|-------------|
| deidentify | De-identify a single file |
| text | De-identify inline text |
| batch | Batch de-identify a directory |
| audit | Show audit log with summary statistics |
| validate | Validation report for a file |
| rules | List all PII detection rules with status |

### deidentify

`ash
ehr-deidentifier deidentify --file patient_note.txt --output clean_note.txt
`

### text

`ash
ehr-deidentifier text --input "Patient John Smith, SSN 123-45-6789"
`

### batch

`ash
ehr-deidentifier batch --directory ./records/ --output-dir ./clean/ --pattern "*.txt"
`

### audit

`ash
ehr-deidentifier audit
`

### validate

`ash
ehr-deidentifier validate --file clean_note.txt
`

### rules

`ash
ehr-deidentifier rules
`

### Global Options

`ash
ehr-deidentifier --help          # Show all commands and options
ehr-deidentifier --version       # Show version information
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

```
85-ehr-deidentifier/
├── src/
│   └── ehr_deidentifier/
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
```

### Data Flow

```
User Input → CLI/Web Interface → Core Engine → LLM (Ollama) → Response
                                      ↓
                              Built-in Databases
                              (patterns, rules, references)
```

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

```python
from ehr_deidentifier.core import deidentify_text, regex_preprocess, AuditLog, ValidationReport

# De-identify text (dual-layer)
clean_text = deidentify_text("Patient John Smith, DOB 01/15/1990, SSN 123-45-6789")
print(clean_text)

# Regex-only preprocessing
detections = regex_preprocess("Call 555-123-4567, email john@example.com")
# Returns: {"phone": ["555-123-4567"], "email": ["john@example.com"]}

# Audit and validate
audit = AuditLog()
report = ValidationReport(clean_text)
print(report.generate())
```

### Configuration

```yaml
# config.yaml
model: llama3.2
temperature: 0.1
max_tokens: 2048
base_url: http://localhost:11434

# PII Detection Rules
rules:
  ssn: true
  phone: true
  email: true
  dates: true
  mrn: true
  ip_address: true
  url: true
  zip_code: true
```

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
pytest --cov=src/ehr_deidentifier --cov-report=html

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
<summary><strong>Is this HIPAA compliant?</strong></summary>
<br>

This tool is for EDUCATIONAL PURPOSES ONLY. It demonstrates de-identification concepts but has NOT been certified for HIPAA compliance. Never use this for actual patient data without proper compliance review and certification.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>What types of PII does it detect?</strong></summary>
<br>

It targets all 18 HIPAA Safe Harbor identifiers through 9 configurable regex rules (SSN, phone, email, dates, MRN, IP, URL, zip codes) plus LLM-based detection for names, addresses, and other contextual identifiers.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I trust the LLM to catch all PHI?</strong></summary>
<br>

No single tool is 100% reliable for PHI detection. The dual-layer approach (regex + LLM) improves coverage, but manual review is always necessary. In production environments, use certified de-identification tools.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Does it handle structured EHR formats?</strong></summary>
<br>

Currently optimized for unstructured clinical text (notes, reports). Structured formats like HL7 or FHIR would need additional parsing logic.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I add custom detection rules?</strong></summary>
<br>

Yes. The configurable regex system allows enabling/disabling built-in rules. For custom patterns, extend the regex_preprocess function in core.py.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## HIPAA Safe Harbor Reference

### 18 HIPAA Identifier Types

The HIPAA Safe Harbor method requires removal of these 18 types of identifiers:

| # | Identifier Type | Regex Coverage | Example |
|---|----------------|---------------|---------|
| 1 | Names | LLM-based | John Smith -> [NAME] |
| 2 | Geographic data | Partial (zip) | 12345 -> [ZIP] |
| 3 | Dates | Regex | 01/15/1990 -> [DATE] |
| 4 | Phone numbers | Regex | 555-123-4567 -> [PHONE] |
| 5 | Fax numbers | Regex | Similar to phone |
| 6 | Email addresses | Regex | john@email.com -> [EMAIL] |
| 7 | Social Security numbers | Regex | 123-45-6789 -> [SSN] |
| 8 | Medical record numbers | Regex | MRN-12345 -> [MRN] |
| 9 | Health plan numbers | LLM-based | [HEALTH_PLAN] |
| 10 | Account numbers | LLM-based | [ACCOUNT] |
| 11 | Certificate/license numbers | LLM-based | [LICENSE] |
| 12 | Vehicle identifiers | LLM-based | [VEHICLE] |
| 13 | Device identifiers | LLM-based | [DEVICE] |
| 14 | Web URLs | Regex | http://... -> [URL] |
| 15 | IP addresses | Regex | 192.168.1.1 -> [IP] |
| 16 | Biometric identifiers | LLM-based | [BIOMETRIC] |
| 17 | Photos | N/A (text only) | N/A |
| 18 | Unique identifying numbers | LLM-based | [UNIQUE_ID] |

### Detection Pipeline

```
Step 1: Configurable Regex Preprocessing
  SSN patterns (XXX-XX-XXXX)
  Phone patterns (XXX-XXX-XXXX, (XXX) XXX-XXXX)
  Email patterns (user@domain.com)
  Date patterns (MM/DD/YYYY, YYYY-MM-DD, etc.)
  MRN patterns (MRN-XXXXX)
  IP address patterns (X.X.X.X)
  URL patterns (http://, https://)
  Zip code patterns (XXXXX, XXXXX-XXXX)
  Custom patterns (extensible)

Step 2: LLM Analysis
  Contextual name detection
  Address identification
  Remaining PHI patterns
  Semantic understanding of clinical context
```

### Audit Log Fields

| Field | Description |
|-------|-------------|
| 	imestamp | When the operation was performed |
| operation | Type of operation (deidentify, validate, batch) |
| pii_count | Number of PII instances detected |
| pii_types | Categories of PII found |
| status | Success, partial, or failure |
| ile_path | Source file (if applicable) |

> This tool is for EDUCATIONAL PURPOSES ONLY. It has NOT been certified for HIPAA compliance. Never use for actual patient data without proper compliance review.


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
git clone https://github.com/YOUR_USERNAME/ehr-deidentifier.git
cd 85-ehr-deidentifier

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #85/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
