<div align="center">

![First Aid Guide Bot Banner](docs/images/banner.svg)

# 🏥 First Aid Guide Bot

### AI-Powered Emergency First Aid Assistant

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-f72585?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-f72585?style=for-the-badge&logo=heart&logoColor=white)]()
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

A comprehensive first aid guide featuring emergency triage assessment, CPR instructions, supply checklists, 15 common emergency scenarios, and emergency contact management — all powered by local LLMs with prominent emergency number display.

Built as part of the **Local LLM Projects** series (Project #90/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🚨 | **Emergency Triage** | Decision-tree assessment based on consciousness, breathing, bleeding |
| ❤️ | **CPR Guide** | 8-step CPR instructions with timing and detailed technique |
| 🩹 | **Supply Checklist** | 20 first aid supplies organized by priority level |
| 📋 | **15 Scenarios** | Common first-aid situations with severity levels |
| 📞 | **Contact Manager** | Store and manage emergency contacts with defaults |
| 💬 | **AI Chat** | Interactive first aid Q&A with local LLM |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Emergency Triage** | Decision-tree assessment: conscious/breathing/bleeding status → action plan |
| **8-Step CPR Guide** | Complete CPR instructions with timing, hand placement, and compression details |
| **Supply Checklist** | 20 items organized by priority: essential, recommended, optional |
| **15 Emergency Scenarios** | Common situations (burns, fractures, choking, etc.) with severity levels |
| **Contact Manager** | In-memory emergency contact storage with name, number, relationship, defaults |
| **Interactive Chat** | Multi-turn first aid Q&A with AI-powered responses |

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
git clone https://github.com/kennedyraju55/first-aid-guide-bot.git
cd 90-first-aid-guide-bot

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
first-aid-guide-bot --help

# Run your first command
first-aid-guide-bot guide --situation "chemical burn on hand"
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
git clone https://github.com/kennedyraju55/first-aid-guide-bot.git
cd first-aid-guide-bot
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
uvicorn src.first_aid.api:app --reload --port 8000

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
| guide | Get first aid guide for a situation |
| chat | Interactive first aid Q&A conversation |
| list | List 15 common emergency scenarios |
| triage | Emergency triage assessment |
| supplies | Show supply checklist by priority |
| cpr | Display 8-step CPR guide |
| contacts | Manage emergency contacts |

### guide

`ash
first-aid-guide-bot guide --situation "chemical burn on hand"
`

### chat

`ash
first-aid-guide-bot chat
`

### list

`ash
first-aid-guide-bot list
`

### triage

`ash
first-aid-guide-bot triage --conscious --breathing --bleeding
`

### supplies

`ash
first-aid-guide-bot supplies --priority essential
`

### cpr

`ash
first-aid-guide-bot cpr
`

### contacts

`ash
first-aid-guide-bot contacts --add "Dr. Smith" --number "555-0123"
`

### Global Options

`ash
first-aid-guide-bot --help          # Show all commands and options
first-aid-guide-bot --version       # Show version information
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
90-first-aid-guide-bot/
├── src/
│   └── first_aid_guide_bot/
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
from first_aid_guide_bot.core import evaluate_emergency, get_cpr_steps, get_supply_checklist

# Triage assessment
result = evaluate_emergency(conscious=True, breathing=True, bleeding=True)
print(result)  # Returns action plan based on assessment

# Get CPR steps
steps = get_cpr_steps()
# Returns: 8 steps with timing and technique details

# Get supply checklist
supplies = get_supply_checklist(priority="essential")
# Returns: Essential first aid supplies list
`

### Configuration

`yaml
# config.yaml
model: llama3.2
temperature: 0.2
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
pytest --cov=src/first_aid_guide_bot --cov-report=html

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
<summary><strong>Can this replace first aid training?</strong></summary>
<br>

NO. This tool is an educational reference only. Proper first aid requires hands-on training from certified organizations like the American Red Cross or American Heart Association. Take a certified first aid/CPR course.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Should I follow these instructions in a real emergency?</strong></summary>
<br>

In a real emergency, ALWAYS call 911 first. This tool provides general first aid information but cannot assess the specific situation. Trained emergency responders should guide care.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is the CPR guide current with latest guidelines?</strong></summary>
<br>

The CPR steps are based on general guidelines but may not reflect the very latest AHA updates. Always take a current CPR certification course for the most up-to-date techniques.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use this for pediatric emergencies?</strong></summary>
<br>

Pediatric first aid differs significantly from adult care (different CPR ratios, medication doses, etc.). This tool provides general adult-oriented information. For children, follow pediatric-specific training.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Does this cover all emergency situations?</strong></summary>
<br>

No. The tool covers 15 common scenarios but emergencies are unpredictable. For situations not covered, call 911 immediately and follow dispatcher instructions.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Emergency Triage Decision Tree

`
Is the person CONSCIOUS?
  YES -> Are they BREATHING normally?
    YES -> Is there SEVERE BLEEDING?
      YES -> Apply direct pressure, call 911
      NO -> Assess for other injuries, monitor
    NO -> Open airway, begin rescue breathing, call 911
  NO -> Check for BREATHING
    BREATHING -> Recovery position, call 911, monitor
    NOT BREATHING -> Begin CPR immediately, call 911
`

### 8-Step CPR Guide

| Step | Action | Duration/Detail |
|------|--------|----------------|
| 1 | **Check Safety** | Ensure scene is safe for you |
| 2 | **Check Responsiveness** | Tap shoulders, shout Are you okay? |
| 3 | **Call 911** | Or direct someone to call |
| 4 | **Open Airway** | Head-tilt, chin-lift maneuver |
| 5 | **Check Breathing** | Look, listen, feel for 10 seconds |
| 6 | **Begin Compressions** | 30 compressions, 2 inches deep, 100-120/min |
| 7 | **Rescue Breaths** | 2 breaths after every 30 compressions |
| 8 | **Continue** | 30:2 ratio until help arrives or person responds |

> **Hands-only CPR** (compressions without breaths) is recommended for untrained bystanders.

### First Aid Supply Checklist

<details>
<summary><strong>Essential Supplies (Priority 1)</strong></summary>

| Item | Quantity | Purpose |
|------|----------|---------|
| Adhesive bandages (assorted) | 20+ | Minor cuts and scrapes |
| Gauze pads (3x3, 4x4) | 10+ | Wound coverage |
| Medical tape | 1 roll | Securing bandages |
| Elastic bandage (ACE) | 2 | Sprains, compression |
| Antiseptic wipes | 20+ | Wound cleaning |
| Antibiotic ointment | 1 tube | Infection prevention |
| Disposable gloves | 4 pairs | Personal protection |
| Scissors | 1 pair | Cutting bandages/tape |
| Tweezers | 1 pair | Splinter/tick removal |
| CPR face shield | 1 | Rescue breathing barrier |

</details>

<details>
<summary><strong>Recommended Supplies (Priority 2)</strong></summary>

| Item | Quantity | Purpose |
|------|----------|---------|
| Triangular bandage | 2 | Sling, tourniquet |
| Cold pack (instant) | 2 | Swelling reduction |
| Burn gel | 1 tube | Minor burn treatment |
| Eye wash solution | 1 bottle | Eye irrigation |
| Thermometer | 1 | Temperature check |

</details>

<details>
<summary><strong>Optional Supplies (Priority 3)</strong></summary>

| Item | Quantity | Purpose |
|------|----------|---------|
| Emergency blanket | 1 | Shock/hypothermia |
| Flashlight | 1 | Low-light situations |
| Whistle | 1 | Signaling for help |
| First aid manual | 1 | Quick reference guide |
| Medications (OTC) | Various | Pain, allergy, etc. |

</details>

### 15 Common Emergency Scenarios

| Scenario | Severity | First Action |
|----------|----------|-------------|
| Minor cuts/scrapes | Low | Clean, apply antibiotic, bandage |
| Nosebleed | Low | Lean forward, pinch soft part |
| Minor burns | Moderate | Cool water 10-20 min |
| Sprains/strains | Moderate | RICE: Rest, Ice, Compress, Elevate |
| Bee stings | Moderate | Remove stinger, ice, monitor for allergy |
| Choking | High | Heimlich maneuver / back blows |
| Severe bleeding | High | Direct pressure, call 911 |
| Fractures | High | Immobilize, do not move, call 911 |
| Seizures | High | Protect head, do not restrain, call 911 |
| Heart attack signs | Emergency | Call 911, aspirin if not allergic |
| Stroke signs | Emergency | FAST test, call 911 immediately |
| Anaphylaxis | Emergency | EpiPen, call 911 |
| Drowning | Emergency | Remove from water, CPR if needed |
| Electric shock | Emergency | Disconnect power, call 911 |
| Poisoning | Emergency | Call Poison Control: 1-800-222-1222 |

> In ANY emergency, ALWAYS call 911 first. These guides are for educational reference only and cannot replace professional emergency medical training.


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
git clone https://github.com/YOUR_USERNAME/first-aid-guide-bot.git
cd 90-first-aid-guide-bot

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #90/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
