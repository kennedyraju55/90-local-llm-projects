<div align="center">

![Exercise Form Guide Banner](docs/images/banner.svg)

# 🏥 Exercise Form Guide

### AI-Powered Exercise Form & Workout Planning

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-fb8500?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-fb8500?style=for-the-badge&logo=heart&logoColor=white)]()
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

A comprehensive exercise form guide that provides detailed movement instructions, muscle group information, progression paths, warm-up/cool-down routines, and weekly workout plans — all powered by local LLMs for personalized fitness guidance.

Built as part of the **Local LLM Projects** series (Project #87/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 💪 | **7 Muscle Groups** | Chest, back, legs, shoulders, arms, core, full body databases |
| 📈 | **Progression Paths** | 5 exercises with beginner → advanced progression variants |
| 🔥 | **Warm-Up Routines** | 4+ warm-up exercises for each of 7 muscle groups |
| ❄️ | **Cool-Down Stretches** | Recovery stretches organized by muscle group |
| 📋 | **Workout Plans** | AI-generated weekly routines for any goal and level |
| 🎯 | **3 Skill Levels** | Beginner, intermediate, and advanced form guidance |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Muscle Group Database** | 7 groups with muscles, descriptions, and exercise lists: chest, back, legs, shoulders, arms, core, full body |
| **Progression Paths** | Step-by-step progressions for push-ups, squats, pull-ups, planks, and deadlifts |
| **Warm-Up Routines** | 4+ warm-up exercises for each muscle group to prevent injury |
| **Cool-Down Stretches** | Recovery stretches and mobility exercises organized by muscle group |
| **3 Skill Levels** | Form guides tailored to beginner, intermediate, and advanced athletes |
| **Weekly Workout Plans** | AI-generated routines based on your fitness goal and experience level |

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
git clone https://github.com/kennedyraju55/exercise-form-guide.git
cd 87-exercise-form-guide

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
exercise-form-guide --help

# Run your first command
exercise-form-guide guide --exercise "deadlift" --level intermediate
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
| guide | Get exercise form guide |
| list | List exercises for a muscle group |
| routine | Generate weekly workout plan |
| warmup | Get warm-up routine |
| cooldown | Get cool-down stretches |
| progression | Show exercise progression path |
| muscles | Show muscle group information |

### guide

`ash
exercise-form-guide guide --exercise "deadlift" --level intermediate
`

### list

`ash
exercise-form-guide list --muscle-group legs
`

### routine

`ash
exercise-form-guide routine --goal "build muscle" --level beginner
`

### warmup

`ash
exercise-form-guide warmup --muscle-group chest
`

### cooldown

`ash
exercise-form-guide cooldown --muscle-group back
`

### progression

`ash
exercise-form-guide progression --exercise "push-up"
`

### muscles

`ash
exercise-form-guide muscles --group legs
`

### Global Options

`ash
exercise-form-guide --help          # Show all commands and options
exercise-form-guide --version       # Show version information
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
87-exercise-form-guide/
├── src/
│   └── exercise_form_guide/
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
from exercise_form_guide.core import generate_guide, get_muscle_info, get_exercise_variations

# Get exercise form guide
guide = generate_guide("deadlift", level="intermediate")
print(guide)

# Get muscle group info
info = get_muscle_info("legs")
# Returns: {"muscles": [...], "exercises": [...], "description": "..."}

# Get progression path
progressions = get_exercise_variations("push-up")
# Returns: ["wall push-up", "knee push-up", "standard", "diamond", "archer"]
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
pytest --cov=src/exercise_form_guide --cov-report=html

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
<summary><strong>Can this replace a personal trainer?</strong></summary>
<br>

No. While this tool provides general form guidance, a personal trainer can observe your movement, correct real-time mistakes, and account for injuries or limitations. This is an educational supplement, not a replacement.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is the form guidance safe for beginners?</strong></summary>
<br>

The guides provide general form cues, but incorrect execution can still cause injury. If you're new to exercise, consider working with a certified trainer initially. Start with lighter weights and focus on form.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use this with a physical injury?</strong></summary>
<br>

DO NOT exercise through pain. If you have any injury or physical limitation, consult a sports medicine doctor or physical therapist before following any exercise program.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How accurate are the progression paths?</strong></summary>
<br>

Progressions follow generally accepted exercise science principles but may not suit everyone. Factors like mobility, strength imbalances, and body proportions affect which progressions are appropriate.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Are the workout plans periodized?</strong></summary>
<br>

AI-generated plans provide general weekly structures. For proper periodization (progressive overload, deload weeks, etc.), work with a certified strength and conditioning specialist.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Muscle Group Database

### 7 Muscle Groups

<details>
<summary><strong>Chest</strong></summary>

**Muscles**: Pectoralis major, pectoralis minor, serratus anterior

**Key Exercises**: Bench press, push-ups, chest fly, dips, cable crossover

**Warm-up**: Arm circles, band pull-aparts, wall push-ups, chest openers

</details>

<details>
<summary><strong>Back</strong></summary>

**Muscles**: Latissimus dorsi, rhomboids, trapezius, erector spinae

**Key Exercises**: Pull-ups, rows, deadlifts, lat pulldowns, face pulls

**Warm-up**: Cat-cow stretches, band rows, arm swings, scapular retractions

</details>

<details>
<summary><strong>Legs</strong></summary>

**Muscles**: Quadriceps, hamstrings, glutes, calves, hip flexors

**Key Exercises**: Squats, lunges, deadlifts, leg press, calf raises

**Warm-up**: Bodyweight squats, leg swings, hip circles, walking lunges

</details>

<details>
<summary><strong>Shoulders</strong></summary>

**Muscles**: Anterior, lateral, and posterior deltoids, rotator cuff

**Key Exercises**: Overhead press, lateral raises, face pulls, Arnold press

**Warm-up**: Arm circles, band dislocates, wall slides, external rotations

</details>

<details>
<summary><strong>Arms</strong></summary>

**Muscles**: Biceps brachii, triceps brachii, brachialis, forearms

**Key Exercises**: Curls, extensions, dips, hammer curls, skull crushers

**Warm-up**: Wrist circles, band curls, light dumbbell rotations

</details>

<details>
<summary><strong>Core</strong></summary>

**Muscles**: Rectus abdominis, obliques, transverse abdominis, erector spinae

**Key Exercises**: Planks, crunches, Russian twists, leg raises, bird dogs

**Warm-up**: Cat-cow, dead bugs, pelvic tilts, gentle twists

</details>

<details>
<summary><strong>Full Body</strong></summary>

**Muscles**: All major muscle groups integrated

**Key Exercises**: Burpees, Turkish get-ups, thrusters, clean and press

**Warm-up**: Dynamic stretching, jumping jacks, high knees, butt kicks

</details>

### Progression Paths

| Exercise | Level 1 | Level 2 | Level 3 | Level 4 | Level 5 |
|----------|---------|---------|---------|---------|---------|
| **Push-up** | Wall push-up | Knee push-up | Standard | Diamond | Archer |
| **Squat** | Chair squat | Bodyweight | Goblet | Barbell | Pistol |
| **Pull-up** | Dead hang | Band-assisted | Negative | Standard | Weighted |
| **Plank** | Knee plank | Standard | Side plank | Plank walk | Plank + row |
| **Deadlift** | Glute bridge | Romanian DL | Conventional | Sumo | Single-leg |

> If you experience pain (not discomfort) during any exercise, STOP immediately. Consult a sports medicine physician or physical therapist before continuing.


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
git clone https://github.com/YOUR_USERNAME/exercise-form-guide.git
cd 87-exercise-form-guide

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #87/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
