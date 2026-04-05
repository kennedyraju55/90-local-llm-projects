<div align="center">

![Drug Interaction Checker Banner](docs/images/banner.svg)

# 🏥 Drug Interaction Checker

### AI-Powered Medication Safety Analysis

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-00b4d8?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-00b4d8?style=for-the-badge&logo=heart&logoColor=white)]()
[![Privacy](https://img.shields.io/badge/Privacy-100%25_Local-success?style=for-the-badge&logo=lock&logoColor=white)]()

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

A comprehensive drug interaction analysis tool that checks medication combinations for potential interactions, food-drug conflicts, dosage information, and alternative medications — all powered by local LLMs for complete privacy.

Built as part of the **Local LLM Projects** series (Project #82/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 💊 | **Interaction Detection** | Check 2+ medications for potential dangerous interactions |
| 🍎 | **Food-Drug Warnings** | Built-in database of 10+ food-drug interaction pairs |
| 📋 | **Dosage Reference** | Common adult dosage information for popular medications |
| 🔄 | **Alternative Finder** | Discover substitute medications for common drugs |
| ⚠️ | **Severity Scoring** | 5-level severity from None to Contraindicated |
| 🔒 | **Private & Secure** | All medication data processed locally — never uploaded |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Severity Classification** | 5 levels: None, Mild, Moderate, Severe, Contraindicated with visual indicators |
| **Food-Drug Interactions** | Database of 10+ medications with food/substance warnings (warfarin+vitamin K, etc.) |
| **Dosage Notes** | Common adult dosages for 10+ frequently prescribed medications |
| **Alternative Medications** | Substitute medication suggestions for 10+ common drug classes |
| **Interactive Session** | Multi-command session: check, food, alt, dose in one workflow |
| **Rich Results Display** | Formatted tables with medications, severity, food warnings, alternatives |

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
git clone https://github.com/kennedyraju55/drug-interaction-checker.git
cd 82-drug-interaction-checker

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
drug-interaction-checker --help

# Run your first command
drug-interaction-checker check --medications "aspirin, ibuprofen, warfarin"
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

---

## 💻 CLI Reference

| Command | Description |
|---------|-------------|
| check | Check interactions between 2+ medications |
| food | Show food interactions for a specific drug |
| alternatives | Show alternative medications |
| interactive | Interactive session with multiple commands |

### check

`ash
drug-interaction-checker check --medications "aspirin, ibuprofen, warfarin"
`

### food

`ash
drug-interaction-checker food --drug "warfarin"
`

### alternatives

`ash
drug-interaction-checker alternatives --drug "ibuprofen"
`

### interactive

`ash
drug-interaction-checker interactive
`

### Global Options

`ash
drug-interaction-checker --help          # Show all commands and options
drug-interaction-checker --version       # Show version information
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
82-drug-interaction-checker/
├── src/
│   └── drug_interaction_checker/
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
from drug_interaction_checker.core import check_interactions, get_food_interactions, get_alternatives

# Check drug interactions
result = check_interactions(["aspirin", "warfarin", "ibuprofen"])
print(result)

# Get food interactions for a medication
foods = get_food_interactions("warfarin")
# Returns: ["Vitamin K rich foods", "Cranberry juice", "Alcohol", ...]

# Find alternative medications
alts = get_alternatives("ibuprofen")
# Returns: ["acetaminophen", "naproxen", "celecoxib"]
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
pytest --cov=src/drug_interaction_checker --cov-report=html

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
<summary><strong>Can I rely on this for my medication safety?</strong></summary>
<br>

NO. This tool is for educational exploration only. Always consult your pharmacist or prescribing physician about drug interactions. They have access to your complete medical history and can provide personalized guidance.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How comprehensive is the drug database?</strong></summary>
<br>

The built-in database covers common medications. The LLM provides broader knowledge but may not be current with the latest drug approvals or recalls. Always verify with official sources like FDA or your pharmacist.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Does this check dosage interactions?</strong></summary>
<br>

The tool provides general dosage information but does NOT account for your specific conditions, weight, kidney/liver function, or other factors that affect dosing. Your doctor determines proper dosing.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use this for veterinary medications?</strong></summary>
<br>

No. This tool is designed for human medications only. Veterinary pharmacology differs significantly. Consult your veterinarian for animal medication questions.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>What about herbal supplement interactions?</strong></summary>
<br>

The LLM may provide some herbal interaction information, but the built-in database focuses on prescription/OTC medications. Herbal interactions are complex — discuss supplements with your healthcare provider.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Built-in Drug Database

### Food-Drug Interactions Reference

| Medication | Food/Substance | Interaction |
|------------|----------------|-------------|
| **Warfarin** | Vitamin K foods (leafy greens) | Reduces anticoagulant effect |
| **Warfarin** | Cranberry juice | May increase bleeding risk |
| **Warfarin** | Alcohol | Unpredictable effect on INR |
| **Metformin** | Alcohol | Risk of lactic acidosis |
| **Lisinopril** | Potassium-rich foods | Risk of hyperkalemia |
| **Ciprofloxacin** | Dairy products | Reduced absorption |
| **Levothyroxine** | Calcium/iron supplements | Reduced absorption |
| **MAOIs** | Tyramine-rich foods | Hypertensive crisis risk |
| **Statins** | Grapefruit | Increased drug concentration |
| **Tetracycline** | Dairy products | Chelation reduces efficacy |

### Severity Classification System

| Level | Indicator | Description | Action Required |
|-------|-----------|-------------|-----------------|
| **None** | Safe | No known interaction | Safe to use together |
| **Mild** | Caution | Minor interaction possible | Monitor for side effects |
| **Moderate** | Warning | Significant interaction | Doctor should evaluate |
| **Severe** | Danger | Dangerous interaction | Avoid combination if possible |
| **Contraindicated** | Prohibited | Must NEVER be combined | Absolute prohibition |

### Common Medication Alternatives

<details>
<summary><strong>Pain Relievers</strong></summary>

| If you take... | Alternatives include... |
|----------------|------------------------|
| Ibuprofen | Acetaminophen, Naproxen, Celecoxib |
| Aspirin | Acetaminophen (for pain only) |
| Oxycodone | Tramadol, Gabapentin (for neuropathic) |

</details>

<details>
<summary><strong>Blood Pressure Medications</strong></summary>

| If you take... | Alternatives include... |
|----------------|------------------------|
| Lisinopril | Losartan, Amlodipine, Metoprolol |
| Metoprolol | Atenolol, Carvedilol, Propranolol |

</details>

<details>
<summary><strong>Cholesterol Medications</strong></summary>

| If you take... | Alternatives include... |
|----------------|------------------------|
| Atorvastatin | Rosuvastatin, Simvastatin, Pravastatin |
| Simvastatin | Atorvastatin, Rosuvastatin |

</details>

> **NEVER switch medications without consulting your prescribing physician or pharmacist.**


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
git clone https://github.com/YOUR_USERNAME/drug-interaction-checker.git
cd 82-drug-interaction-checker

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #82/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
