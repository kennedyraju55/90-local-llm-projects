<div align="center">

![Symptom Checker Bot Banner](docs/images/banner.svg)

# 🏥 Symptom Checker Bot

### AI-Powered Symptom Analysis & Triage

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-e94560?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-e94560?style=for-the-badge&logo=heart&logoColor=white)]()
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

An intelligent symptom analysis tool that leverages local LLMs to assess symptoms, identify affected body regions, determine urgency levels, and provide preliminary health guidance — all running privately on your machine.

Built as part of the **Local LLM Projects** series (Project #81/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🔒 | **Complete Privacy** | All symptom data stays on your machine — no cloud uploads |
| ⚡ | **Instant Triage** | 5-level urgency scoring from Low to Emergency in seconds |
| 🧠 | **Body Region Mapping** | Automatic identification of 7 affected body regions |
| 📊 | **Session History** | Track all symptom checks with timestamps and urgency |
| 💬 | **Multi-Turn Chat** | Interactive conversation for deeper symptom exploration |
| 🏥 | **Medical Knowledge** | Built-in symptom databases organized by body system |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Urgency Scoring** | 5-level triage system (Low → Emergency) with keyword-based classification |
| **Body Region Mapping** | Automatic detection of 7 body regions: head, chest, abdomen, limbs, general, skin, mental |
| **Symptom Database** | Comprehensive symptom lists organized by body system for quick reference |
| **Medical History Tracking** | Session-based history with timestamps, urgency levels, and LLM responses |
| **Interactive Chat** | Multi-turn conversational interface for detailed symptom exploration |
| **Rich Terminal UI** | Beautiful formatted output with color-coded urgency panels |

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
git clone https://github.com/kennedyraju55/symptom-checker-bot.git
cd 81-symptom-checker-bot

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
symptom-checker-bot --help

# Run your first command
symptom-checker-bot check --symptoms "severe headache with blurred vision"
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
git clone https://github.com/kennedyraju55/symptom-checker-bot.git
cd symptom-checker-bot
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
uvicorn src.symptom_checker.api:app --reload --port 8000

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
| check | Analyze symptoms with urgency scoring and body region mapping |
| chat | Interactive multi-turn symptom conversation |
| history | Display session symptom history table |
| regions | Show all symptom databases by body region |

### check

`ash
symptom-checker-bot check --symptoms "severe headache with blurred vision"
`

### chat

`ash
symptom-checker-bot chat
`

### history

`ash
symptom-checker-bot history
`

### regions

`ash
symptom-checker-bot regions
`

### Global Options

`ash
symptom-checker-bot --help          # Show all commands and options
symptom-checker-bot --version       # Show version information
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
81-symptom-checker-bot/
├── src/
│   └── symptom_checker_bot/
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
from symptom_checker_bot.core import check_symptoms, assess_urgency, get_body_regions

# Analyze symptoms
result = check_symptoms("persistent headache with nausea and light sensitivity")
print(result)

# Get urgency level (1-5)
urgency = assess_urgency("chest pain difficulty breathing")
# Returns: 5 (Emergency)

# Identify affected body regions
regions = get_body_regions("headache with stomach pain")
# Returns: ["head", "abdomen"]
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
pytest --cov=src/symptom_checker_bot --cov-report=html

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
<summary><strong>Can this replace a doctor visit?</strong></summary>
<br>

Absolutely NOT. This is an educational tool only. It provides preliminary symptom analysis to help you prepare for a doctor visit, but it cannot diagnose conditions. Always consult a licensed healthcare provider for medical concerns.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How accurate is the urgency scoring?</strong></summary>
<br>

The urgency scoring uses keyword-based classification as a rough guide. It may miss nuances. If you're unsure, always err on the side of caution and seek immediate medical attention.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is my symptom data stored anywhere?</strong></summary>
<br>

No. All data stays in your current session memory and is never transmitted to any server. When you close the application, session history is cleared.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>What LLM models work best?</strong></summary>
<br>

We recommend llama3.2 or mistral for best medical knowledge. Larger models (13B+) tend to provide more detailed and accurate symptom analysis.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use this offline?</strong></summary>
<br>

Yes! Once you have Ollama installed with a downloaded model, the entire application runs 100% offline with no internet required.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## 🏥 Symptom Database Reference

The built-in symptom database covers **7 body regions** with common symptoms:

<details>
<summary><strong>Head and Neurological</strong></summary>

- Headache (tension, migraine, cluster)
- Dizziness and vertigo
- Blurred or double vision
- Memory issues and confusion
- Tinnitus (ringing in ears)
- Facial pain or numbness

</details>

<details>
<summary><strong>Chest and Cardiovascular</strong></summary>

- Chest pain or tightness
- Shortness of breath
- Heart palpitations
- Persistent cough
- Wheezing

</details>

<details>
<summary><strong>Abdomen and Digestive</strong></summary>

- Abdominal pain (upper, lower, generalized)
- Nausea and vomiting
- Diarrhea or constipation
- Bloating and gas
- Loss of appetite

</details>

<details>
<summary><strong>Limbs and Musculoskeletal</strong></summary>

- Joint pain or swelling
- Muscle weakness
- Numbness or tingling
- Limited range of motion
- Cramping

</details>

<details>
<summary><strong>General and Systemic</strong></summary>

- Fever and chills
- Fatigue and malaise
- Unexplained weight changes
- Night sweats
- Swollen lymph nodes

</details>

<details>
<summary><strong>Skin and Dermatological</strong></summary>

- Rashes and hives
- Itching (pruritus)
- Skin discoloration
- Wound healing issues
- Unusual moles or growths

</details>

<details>
<summary><strong>Mental Health</strong></summary>

- Persistent sadness or anxiety
- Sleep disturbances
- Difficulty concentrating
- Loss of interest in activities
- Irritability or mood swings

> If experiencing thoughts of self-harm, call **988** immediately.

</details>

### Urgency Level Reference

| Level | Indicator | Examples | Action |
|-------|-----------|----------|--------|
| 1 | Low | Mild headache, minor rash | Self-care, monitor |
| 2 | Mild | Persistent cough, mild fever | Schedule appointment |
| 3 | Moderate | High fever, severe pain | See doctor soon |
| 4 | High | Chest pain, difficulty breathing | Urgent care / ER |
| 5 | Emergency | Loss of consciousness, severe bleeding | **Call 911 NOW** |

> The urgency scoring is a rough guide only. When in doubt, always seek immediate medical attention.


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
git clone https://github.com/YOUR_USERNAME/symptom-checker-bot.git
cd 81-symptom-checker-bot

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #81/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
