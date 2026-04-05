<div align="center">

![Stress Management Bot Banner](docs/images/banner.svg)

# 🏥 Stress Management Bot

### AI-Powered Stress Relief & CBT Tools

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-4361ee?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-4361ee?style=for-the-badge&logo=heart&logoColor=white)]()
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

A comprehensive stress management toolkit featuring guided breathing exercises, CBT worksheets, stress assessments, coping strategies, journaling prompts, and AI-powered conversations — all running privately on your machine with crisis resource information.

Built as part of the **Local LLM Projects** series (Project #89/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🫁 | **Breathing Exercises** | Guided Box Breathing (4-4-4-4) and 4-7-8 technique with progress bars |
| 🧠 | **CBT Worksheets** | 3 templates: Thought Record, Behavioral Activation, Worry Time Scheduler |
| 📊 | **Stress Scoring** | 5-question assessment with category breakdown and recommendations |
| 🛠️ | **Coping Toolkit** | 4 categories: Physical, Cognitive, Social, Creative techniques |
| 📝 | **AI Journaling** | AI-generated reflective prompts with guided freewriting |
| 🆘 | **Crisis Resources** | 988 Suicide & Crisis Lifeline, Crisis Text Line, 911 information |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Guided Breathing** | Box Breathing (4-4-4-4) and 4-7-8 technique with visual progress bars and timing |
| **CBT Worksheets** | 3 evidence-based templates: Thought Record, Behavioral Activation Planner, Worry Time Scheduler |
| **Stress Assessment** | 5-question assessment (stress, sleep, energy, anxiety, concentration) with scoring |
| **Coping Toolkit** | 4 categories of coping strategies: Physical, Cognitive, Social, Creative techniques |
| **AI Journaling** | LLM-generated reflective prompts with guided freewriting and AI feedback |
| **Crisis Resources** | Prominent display of 988 Lifeline, Crisis Text Line, and emergency numbers |

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
git clone https://github.com/kennedyraju55/stress-management-bot.git
cd 89-stress-management-bot

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
stress-management-bot --help

# Run your first command
stress-management-bot chat
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
| chat | Interactive stress management conversation |
| breathe | Guided breathing exercise |
| journal | AI-generated journaling prompt with freewrite |
| assess | Quick stress assessment |
| score | Detailed stress score with breakdown |
| worksheet | Display CBT worksheet template |
| coping | Show coping suggestions by stress level |
| toolkit | Show full coping toolkit by category |

### chat

`ash
stress-management-bot chat
`

### breathe

`ash
stress-management-bot breathe --technique box
`

### journal

`ash
stress-management-bot journal
`

### assess

`ash
stress-management-bot assess
`

### score

`ash
stress-management-bot score
`

### worksheet

`ash
stress-management-bot worksheet --type thought_record
`

### coping

`ash
stress-management-bot coping --level moderate
`

### toolkit

`ash
stress-management-bot toolkit
`

### Global Options

`ash
stress-management-bot --help          # Show all commands and options
stress-management-bot --version       # Show version information
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
89-stress-management-bot/
├── src/
│   └── stress_management_bot/
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
from stress_management_bot.core import run_breathing_exercise, calculate_stress_score, get_cbt_worksheet

# Run guided breathing
run_breathing_exercise("box")  # 4-4-4-4 box breathing with progress bars

# Calculate stress score
score = calculate_stress_score({"stress": 7, "sleep": 4, "energy": 3, "anxiety": 8, "concentration": 5})
# Returns: {"score": 72, "level": "high", "breakdown": {...}, "recommendations": [...]}

# Get CBT worksheet
worksheet = get_cbt_worksheet("thought_record")
# Returns template with situation, automatic_thought, emotion, evidence, balanced_thought
`

### Configuration

`yaml
# config.yaml
model: llama3.2
temperature: 0.4
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
pytest --cov=src/stress_management_bot --cov-report=html

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
<summary><strong>Can this replace therapy or counseling?</strong></summary>
<br>

Absolutely NOT. This tool provides general stress management techniques but is NOT therapy. If you're experiencing significant stress, anxiety, or depression, please seek help from a licensed mental health professional.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>What should I do in a mental health crisis?</strong></summary>
<br>

Call 988 (Suicide & Crisis Lifeline), text HOME to 741741 (Crisis Text Line), or call 911 for immediate danger. This tool is NOT equipped to handle crisis situations.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Are the CBT worksheets clinically validated?</strong></summary>
<br>

The worksheets are based on common CBT techniques but are simplified for self-help use. Clinical CBT should be conducted with a licensed therapist who can guide you through the process properly.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is the breathing exercise safe for everyone?</strong></summary>
<br>

Most people can safely practice breathing exercises. However, if you have respiratory conditions (asthma, COPD), cardiac issues, or experience dizziness during breathing exercises, consult your doctor first.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is my journal data private?</strong></summary>
<br>

Yes. All data stays on your local machine. Nothing is transmitted to external servers. Journal entries exist only in your terminal session.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Breathing Exercise Guide

### Box Breathing (4-4-4-4)

Used by Navy SEALs for stress management:

`
   Inhale (4s)
   +---------+
   |         |
   |  HOLD   | Hold (4s)
   |  (4s)   |
   |         |
   +---------+
   Exhale (4s)
`

| Phase | Duration | Instruction |
|-------|----------|-------------|
| 1. Inhale | 4 seconds | Breathe in slowly through nose |
| 2. Hold | 4 seconds | Hold breath gently |
| 3. Exhale | 4 seconds | Breathe out slowly through mouth |
| 4. Hold | 4 seconds | Hold with empty lungs |
| Repeat | 4-8 cycles | Continue until calm |

### 4-7-8 Breathing

Developed by Dr. Andrew Weil:

| Phase | Duration | Instruction |
|-------|----------|-------------|
| 1. Inhale | 4 seconds | Breathe in quietly through nose |
| 2. Hold | 7 seconds | Hold breath |
| 3. Exhale | 8 seconds | Exhale completely through mouth |
| Repeat | 3-4 cycles | Best done twice daily |

### CBT Worksheet Templates

<details>
<summary><strong>Thought Record</strong></summary>

| Column | Description |
|--------|-------------|
| Situation | What happened? Where? When? |
| Automatic Thought | What went through your mind? |
| Emotion | What did you feel? (Rate 0-100%) |
| Evidence For | What supports this thought? |
| Evidence Against | What contradicts this thought? |
| Balanced Thought | A more realistic perspective |
| Emotion After | How do you feel now? (Rate 0-100%) |

</details>

<details>
<summary><strong>Behavioral Activation Planner</strong></summary>

| Day | Planned Activity | Pleasure (0-10) | Mastery (0-10) | Completed? |
|-----|-----------------|-----------------|----------------|------------|
| Mon | Morning walk | | | |
| Tue | Call a friend | | | |
| Wed | Cook a new recipe | | | |
| Thu | Read for 30 min | | | |
| Fri | Exercise class | | | |

</details>

<details>
<summary><strong>Worry Time Scheduler</strong></summary>

| Field | Description |
|-------|-------------|
| Scheduled Worry Time | Set a fixed 15-20 min daily window |
| Worry Topic | Write each worry during scheduled time |
| Controllable? | Yes/No - can you act on this? |
| Action Step | If yes, what is one small step? |
| Let Go Strategy | If no, how will you release this worry? |

</details>

### Coping Toolkit Categories

| Category | Techniques |
|----------|-----------|
| **Physical** | Walking, stretching, progressive muscle relaxation, yoga |
| **Cognitive** | Journaling, reframing, gratitude practice, mindfulness |
| **Social** | Calling a friend, support groups, volunteering, boundaries |
| **Creative** | Drawing, music, cooking, gardening, photography |

> If you are in crisis: Call 988 (Suicide and Crisis Lifeline), text HOME to 741741 (Crisis Text Line), or call 911 for immediate danger.


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
git clone https://github.com/YOUR_USERNAME/stress-management-bot.git
cd 89-stress-management-bot

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #89/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
