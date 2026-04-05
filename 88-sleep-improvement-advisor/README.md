<div align="center">

![Sleep Improvement Advisor Banner](docs/images/banner.svg)

# 🏥 Sleep Improvement Advisor

### AI-Powered Sleep Analysis & Optimization

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-e63946?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-e63946?style=for-the-badge&logo=heart&logoColor=white)]()
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

A comprehensive sleep improvement tool that analyzes sleep logs, calculates sleep scores, builds bedtime routines, assesses sleep environments, identifies weekly patterns, and provides AI-powered recommendations — all running privately on your machine.

Built as part of the **Local LLM Projects** series (Project #88/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 📊 | **Sleep Scoring** | 0-100 composite score based on duration, quality, consistency, and wake count |
| 📈 | **Pattern Analysis** | Day-of-week analysis, weekday vs weekend comparison, trend detection |
| 🌙 | **Bedtime Routines** | Personalized 2-hour wind-down routine with 9 timed activities |
| 🏠 | **Environment Check** | 11-item checklist across Light, Sound, Temperature, Bedding, Air, Electronics |
| 📋 | **Sleep Assessment** | 10-question interactive assessment covering all sleep factors |
| 📉 | **Sleep Statistics** | Average, min, max duration and quality from CSV sleep logs |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **Sleep Score Calculator** | Composite 0-100 score weighing duration, quality, consistency, and wake frequency |
| **Weekly Pattern Analysis** | Day-of-week breakdown, weekday vs weekend comparison, and trend detection |
| **Bedtime Routine Builder** | Personalized 2-hour routine with 9 activities timed from your wake time |
| **Environment Checklist** | 11 optimization items: Light, Sound, Temperature, Bedding, Air Quality, Electronics |
| **10-Question Assessment** | Comprehensive sleep assessment covering bedtime, wake time, quality, caffeine, screens, exercise |
| **CSV Sleep Log Analysis** | Parse and analyze sleep logs with date, bedtime, waketime, quality, and notes |

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
git clone https://github.com/kennedyraju55/sleep-improvement-advisor.git
cd 88-sleep-improvement-advisor

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
sleep-improvement-advisor --help

# Run your first command
sleep-improvement-advisor analyze --log sleep_data.csv
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
| analyze | Analyze a sleep log CSV file |
| tips | Get tips for a specific sleep issue |
| assess | Interactive 10-question sleep assessment |
| score | Calculate your sleep score from a log |
| checklist | Display sleep environment optimization checklist |
| routine | Build personalized bedtime routine |
| patterns | Analyze weekly sleep patterns |

### analyze

`ash
sleep-improvement-advisor analyze --log sleep_data.csv
`

### tips

`ash
sleep-improvement-advisor tips --issue "difficulty falling asleep"
`

### assess

`ash
sleep-improvement-advisor assess
`

### score

`ash
sleep-improvement-advisor score --log sleep_data.csv
`

### checklist

`ash
sleep-improvement-advisor checklist
`

### routine

`ash
sleep-improvement-advisor routine --wake-time "7:00 AM" --duration 120
`

### patterns

`ash
sleep-improvement-advisor patterns --log sleep_data.csv
`

### Global Options

`ash
sleep-improvement-advisor --help          # Show all commands and options
sleep-improvement-advisor --version       # Show version information
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
88-sleep-improvement-advisor/
├── src/
│   └── sleep_improvement_advisor/
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
from sleep_improvement_advisor.core import parse_sleep_log, calculate_sleep_score, build_bedtime_routine

# Parse and analyze sleep log
entries = parse_sleep_log("sleep_data.csv")
stats = compute_sleep_stats(entries)
print(f"Avg duration: {stats['avg_duration']}h, Avg quality: {stats['avg_quality']}")

# Calculate composite sleep score
score = calculate_sleep_score(entries)
# Returns: 72 (out of 100)

# Build bedtime routine
routine = build_bedtime_routine(wake_time="7:00 AM", duration=120)
# Returns: 9 timed activities for 2-hour wind-down
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
pytest --cov=src/sleep_improvement_advisor --cov-report=html

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
<summary><strong>Can this diagnose sleep disorders?</strong></summary>
<br>

Absolutely NOT. This tool provides general sleep hygiene suggestions. Sleep disorders like sleep apnea, insomnia, or narcolepsy require professional diagnosis through sleep studies conducted by certified sleep medicine physicians.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How reliable is the sleep score?</strong></summary>
<br>

The sleep score is a general wellness indicator based on self-reported data. It is NOT a clinical measurement. Factors like sleep stages, breathing patterns, and neurological activity require medical-grade sleep monitoring.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Should I stop my sleep medication based on this advice?</strong></summary>
<br>

NEVER change or stop medication without consulting your prescribing physician. This tool provides general sleep hygiene tips, not medical treatment plans.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use the CSV format with my sleep tracker?</strong></summary>
<br>

The tool expects CSV with columns: date, bedtime, waketime, quality_rating, notes. You may need to export and format data from commercial sleep trackers to match this format.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Is the bedtime routine evidence-based?</strong></summary>
<br>

The routine activities are based on general sleep hygiene principles widely recommended by sleep researchers. However, individual effectiveness varies. Consult a sleep specialist for persistent sleep issues.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## Sleep Science Reference

### Sleep Score Components

| Factor | Weight | Measurement | Optimal Range |
|--------|--------|-------------|---------------|
| **Duration** | 35% | Hours of sleep per night | 7-9 hours |
| **Quality** | 30% | Self-reported quality (1-10) | 7+ rating |
| **Consistency** | 20% | Variation in bed/wake times | Less than 30 min variation |
| **Wake Count** | 15% | Night awakenings | 0-1 per night |

### Environment Optimization Checklist

| Category | Item | Recommendation |
|----------|------|----------------|
| **Light** | Blackout curtains | Block all external light |
| **Light** | Blue light filter | Enable 2+ hours before bed |
| **Light** | Night light | Amber/red only if needed |
| **Sound** | White noise machine | Consistent background sound |
| **Sound** | Earplugs | If noisy environment |
| **Temperature** | Room temp | 65-68F (18-20C) |
| **Temperature** | Breathable bedding | Cotton or bamboo sheets |
| **Bedding** | Mattress age | Replace every 7-10 years |
| **Bedding** | Pillow support | Proper neck alignment |
| **Air** | Ventilation | Fresh air circulation |
| **Electronics** | Device-free zone | No screens in bedroom |

### Bedtime Routine Timeline (2-Hour Example)

| Time Before Bed | Activity | Duration |
|----------------|----------|----------|
| -120 min | Last caffeine cutoff | - |
| -90 min | Dim lights, relax | 15 min |
| -75 min | Light stretching or yoga | 15 min |
| -60 min | Warm bath or shower | 20 min |
| -40 min | Reading (physical book) | 20 min |
| -20 min | Journaling or gratitude | 10 min |
| -10 min | Breathing exercises | 5 min |
| -5 min | Set alarm, final prep | 5 min |
| 0 min | Lights out | - |

### CSV Sleep Log Format

`csv
date,bedtime,waketime,quality_rating,notes
2024-01-01,22:30,06:45,7,Slept well
2024-01-02,23:15,07:00,5,Woke up twice
2024-01-03,22:00,06:30,8,Great sleep
`

> Persistent sleep problems may indicate a sleep disorder. If you regularly struggle with sleep despite good sleep hygiene, consult a sleep medicine specialist.


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
git clone https://github.com/YOUR_USERNAME/sleep-improvement-advisor.git
cd 88-sleep-improvement-advisor

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #88/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
