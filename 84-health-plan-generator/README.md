<div align="center">

![Health Plan Generator Banner](docs/images/banner.svg)

# 🏥 Health Plan Generator

### AI-Powered Personalized Wellness Planning

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-ff6b35?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-ff6b35?style=for-the-badge&logo=heart&logoColor=white)]()
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

A personalized health and wellness plan generator that creates adaptive plans based on your goals, age, and lifestyle — with progress tracking, weekly check-ins, and milestone-based recommendations, all powered by local LLMs.

Built as part of the **Local LLM Projects** series (Project #84/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🎯 | **5 Goal Types** | Weight loss, better sleep, fitness, stress management, general wellness |
| 📈 | **Progress Tracking** | Serializable ProgressTracker with JSON persistence |
| ✅ | **Weekly Check-ins** | 9-question questionnaire for adaptive plan adjustment |
| 🏆 | **Milestones** | Week-by-week milestone tracking for each goal type |
| 🤖 | **Adaptive AI** | Plans evolve based on your progress and feedback |
| 👤 | **Personalized** | Tailored to age, lifestyle, duration, and specific goals |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **5 Goal Presets** | Weight loss, better sleep, fitness, stress management, general wellness with milestones |
| **Progress Tracker** | Persistent JSON-based tracking with start date, current week, and goal status |
| **Weekly Check-ins** | 9-question assessment covering energy, meals, exercise, sleep, stress, symptoms |
| **Adaptive Recommendations** | AI generates updated recommendations based on check-in progress |
| **Milestone System** | Week-by-week milestones customized for each goal type |
| **Guided Questionnaire** | Interactive interview for generating personalized wellness plans |

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
git clone https://github.com/kennedyraju55/health-plan-generator.git
cd 84-health-plan-generator

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
health-plan-generator --help

# Run your first command
health-plan-generator generate --goal weight_loss --age 35 --lifestyle active --duration 12
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
| generate | Generate a wellness plan |
| interactive | Guided questionnaire for personalized plan |
| milestones | Show milestones for a specific goal |
| checkin | Weekly progress check-in |
| progress | Show progress with adaptive recommendations |

### generate

`ash
health-plan-generator generate --goal weight_loss --age 35 --lifestyle active --duration 12
`

### interactive

`ash
health-plan-generator interactive
`

### milestones

`ash
health-plan-generator milestones --goal fitness
`

### checkin

`ash
health-plan-generator checkin
`

### progress

`ash
health-plan-generator progress
`

### Global Options

`ash
health-plan-generator --help          # Show all commands and options
health-plan-generator --version       # Show version information
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
84-health-plan-generator/
├── src/
│   └── health_plan_generator/
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
from health_plan_generator.core import generate_plan, get_milestones_for_goal, ProgressTracker

# Generate a personalized plan
plan = generate_plan(goal="weight_loss", age=35, lifestyle="active", duration=12)
print(plan)

# Get milestones for a goal
milestones = get_milestones_for_goal("fitness")
# Returns week-by-week milestone list

# Track progress
tracker = ProgressTracker(goal="better_sleep")
tracker.add_checkin(week=1, responses={...})
recommendation = generate_adaptive_recommendation(tracker)
`

### Configuration

`yaml
# config.yaml
model: llama3.2
temperature: 0.4
max_tokens: 2048
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
pytest --cov=src/health_plan_generator --cov-report=html

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
<summary><strong>Can this replace a personal trainer or dietitian?</strong></summary>
<br>

No. This tool generates general wellness suggestions using AI. It cannot account for medical conditions, injuries, allergies, or other personal factors. Always consult qualified professionals for personalized health plans.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How are the plans personalized?</strong></summary>
<br>

Plans consider your stated age, lifestyle (sedentary/moderate/active), goal type, and duration. However, they don't account for medical history, medications, or physical limitations.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is the progress tracking medically validated?</strong></summary>
<br>

No. The check-in questions and progress metrics are general wellness indicators, not clinical assessments. They help track subjective progress but are not medical measurements.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use this with a medical condition?</strong></summary>
<br>

If you have any medical condition, consult your healthcare provider BEFORE following any wellness plan. Some exercises or dietary changes may be contraindicated for certain conditions.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How often should I do check-ins?</strong></summary>
<br>

The tool suggests weekly check-ins for best results. However, this is a general guideline — adjust based on your comfort level and your healthcare provider's recommendations.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Goal Types and Milestones

### Available Goal Presets

<details>
<summary><strong>Weight Loss</strong></summary>

| Week | Milestone |
|------|-----------|
| 1-2 | Establish baseline, food diary, identify triggers |
| 3-4 | Introduce portion control, meal planning basics |
| 5-6 | Add structured exercise 3x/week, hydration goals |
| 7-8 | Build consistent routine, manage cravings |
| 9-10 | Increase exercise intensity, refine meal plans |
| 11-12 | Evaluate progress, set maintenance strategy |

</details>

<details>
<summary><strong>Better Sleep</strong></summary>

| Week | Milestone |
|------|-----------|
| 1-2 | Sleep diary, identify current patterns |
| 3-4 | Establish consistent sleep/wake times |
| 5-6 | Optimize bedroom environment |
| 7-8 | Develop wind-down routine |
| 9-10 | Address remaining sleep disruptors |
| 11-12 | Evaluate and maintain improvements |

</details>

<details>
<summary><strong>Fitness</strong></summary>

| Week | Milestone |
|------|-----------|
| 1-2 | Fitness assessment, set SMART goals |
| 3-4 | Beginner exercise routine, learn proper form |
| 5-6 | Progressive overload, add variety |
| 7-8 | Increase frequency and intensity |
| 9-10 | Introduce advanced techniques |
| 11-12 | Evaluate gains, plan next phase |

</details>

<details>
<summary><strong>Stress Management</strong></summary>

| Week | Milestone |
|------|-----------|
| 1-2 | Stress inventory, identify triggers |
| 3-4 | Learn breathing and relaxation techniques |
| 5-6 | Develop daily mindfulness practice |
| 7-8 | Build social support strategies |
| 9-10 | Cognitive reframing practice |
| 11-12 | Maintain toolkit, evaluate progress |

</details>

<details>
<summary><strong>General Wellness</strong></summary>

| Week | Milestone |
|------|-----------|
| 1-2 | Comprehensive health assessment |
| 3-4 | Nutrition and hydration improvements |
| 5-6 | Exercise and movement goals |
| 7-8 | Sleep and recovery optimization |
| 9-10 | Mental health and social connections |
| 11-12 | Holistic review and maintenance plan |

</details>

### Weekly Check-in Questions

The 9-question check-in covers:

| # | Category | Question Focus |
|---|----------|---------------|
| 1 | Energy | Overall energy levels this week |
| 2 | Meals | Healthy eating adherence |
| 3 | Exercise | Physical activity frequency |
| 4 | Sleep | Sleep quality and duration |
| 5 | Stress | Stress levels and management |
| 6 | Hydration | Water intake |
| 7 | Mood | Emotional well-being |
| 8 | Symptoms | Any new or worsening symptoms |
| 9 | Goals | Progress toward weekly goals |

> If you experience any concerning symptoms during your wellness plan, stop and consult a healthcare provider immediately.


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
git clone https://github.com/YOUR_USERNAME/health-plan-generator.git
cd 84-health-plan-generator

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #84/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
