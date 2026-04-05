<div align="center">

![Nutrition Label Analyzer Banner](docs/images/banner.svg)

# 🏥 Nutrition Label Analyzer

### AI-Powered Nutrition Analysis & Meal Tracking

[![Python](https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-06d6a0?style=for-the-badge)](LICENSE)
[![Healthcare](https://img.shields.io/badge/Healthcare-AI_Tool-06d6a0?style=for-the-badge&logo=heart&logoColor=white)]()
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

A comprehensive nutrition analysis tool that evaluates foods, analyzes nutrition labels, compares multiple foods, tracks daily meals, checks allergens, and calculates FDA daily values — all powered by local LLMs for complete dietary privacy.

Built as part of the **Local LLM Projects** series (Project #86/90), this tool demonstrates how AI can be applied to healthcare education while maintaining complete data privacy through local model inference.

### Why This Project?

| | Feature | Description |
|---|---------|-------------|
| 🥗 | **Food Analysis** | AI-powered nutritional breakdown of any food item |
| 📊 | **Daily Values** | Calculate %DV against FDA reference values for 13 nutrients |
| 🍽️ | **Meal Tracking** | Track daily meals with nutrient totals and remaining budget |
| ⚠️ | **Allergen Check** | Scan foods against FDA Big 9 common allergens |
| 🥊 | **Food Comparison** | Compare nutritional profiles of multiple foods side-by-side |
| 🎯 | **5 Diet Presets** | Balanced, low-carb, high-protein, keto, weight-loss goals |

---

## ✨ Features

<div align="center">

![Features Overview](docs/images/features.svg)

</div>

| Feature | Details |
|---------|---------|
| **FDA Daily Values** | Calculate %DV for 13 nutrients: calories, fats, cholesterol, sodium, carbs, fiber, sugars, protein, vitamins |
| **Big 9 Allergens** | Check against FDA major allergens: milk, eggs, fish, shellfish, tree nuts, peanuts, wheat, soy, sesame |
| **5 Diet Presets** | Balanced, low-carb, high-protein, keto, weight-loss with macro percentages |
| **Meal Tracker** | Daily meal tracking with nutrient totals, remaining budget, and meal history |
| **Food Comparison** | Side-by-side nutritional comparison of multiple food items |
| **Label Analysis** | Parse and analyze nutrition label text from files |

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
git clone https://github.com/kennedyraju55/nutrition-label-analyzer.git
cd 86-nutrition-label-analyzer

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
nutrition-label-analyzer --help

# Run your first command
nutrition-label-analyzer analyze --food "grilled chicken breast 6oz"
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
| analyze | Analyze a single food item |
| label | Analyze nutrition label from file |
| compare | Compare multiple foods |
| daily-values | Calculate %DV for nutrients |
| track | Track meals throughout the day |
| allergen-check | Check food for allergens |
| goals | Show dietary goal presets |

### analyze

`ash
nutrition-label-analyzer analyze --food "grilled chicken breast 6oz"
`

### label

`ash
nutrition-label-analyzer label --file nutrition_label.txt
`

### compare

`ash
nutrition-label-analyzer compare --foods "apple, banana, orange"
`

### daily-values

`ash
nutrition-label-analyzer daily-values --food "calories=250 fat=12 protein=20"
`

### track

`ash
nutrition-label-analyzer track --meal "lunch: grilled salmon with rice"
`

### allergen-check

`ash
nutrition-label-analyzer allergen-check --food "pad thai" --allergens "peanuts,shellfish"
`

### goals

`ash
nutrition-label-analyzer goals --preset keto
`

### Global Options

`ash
nutrition-label-analyzer --help          # Show all commands and options
nutrition-label-analyzer --version       # Show version information
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
86-nutrition-label-analyzer/
├── src/
│   └── nutrition_label_analyzer/
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
from nutrition_label_analyzer.core import analyze_food, check_allergens, MealTracker, DietaryGoal

# Analyze a food item
analysis = analyze_food("grilled chicken breast 6oz")
print(analysis)

# Check for allergens
allergens = check_allergens("pad thai with shrimp and peanuts")
# Returns: ["shellfish", "peanuts"]

# Track daily meals
tracker = MealTracker(goal=DietaryGoal.HIGH_PROTEIN)
tracker.add_meal("lunch", "grilled salmon with quinoa")
print(tracker.get_summary())
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
pytest --cov=src/nutrition_label_analyzer --cov-report=html

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
<summary><strong>Can I use this for managing a medical diet?</strong></summary>
<br>

No. This tool provides general nutritional information but cannot account for medical conditions (diabetes, kidney disease, etc.). Always work with a registered dietitian or your healthcare provider for medical dietary needs.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>How accurate are the nutrition estimates?</strong></summary>
<br>

AI-generated nutrition estimates are approximations. Actual values depend on preparation methods, portion sizes, brands, and ingredients. For precise values, use verified nutrition databases or product labels.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Does it account for food allergies?</strong></summary>
<br>

The allergen checker scans against FDA Big 9 allergens but may miss unlisted ingredients or cross-contamination risks. Always read actual product labels and consult your allergist.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Can I use the meal tracker for calorie counting?</strong></summary>
<br>

The tracker provides rough estimates. For medical weight management, use validated calorie-counting tools recommended by your healthcare provider.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

<details>
<summary><strong>Are the dietary presets medically approved?</strong></summary>
<br>

The presets (keto, low-carb, etc.) are general guidelines. Some diets may not be appropriate for your health condition. Consult a healthcare provider before starting any new diet.

> ⚠️ **Reminder**: This tool is for educational purposes only. Always consult qualified healthcare professionals.

</details>

---



## FDA Daily Reference Values

### 13 Tracked Nutrients

| Nutrient | Daily Reference Value | Unit |
|----------|----------------------|------|
| Calories | 2,000 | kcal |
| Total Fat | 78 | g |
| Saturated Fat | 20 | g |
| Trans Fat | 0 | g |
| Cholesterol | 300 | mg |
| Sodium | 2,300 | mg |
| Total Carbohydrate | 275 | g |
| Dietary Fiber | 28 | g |
| Total Sugars | 50 | g |
| Added Sugars | 50 | g |
| Protein | 50 | g |
| Vitamin D | 20 | mcg |
| Calcium | 1,300 | mg |

### Dietary Goal Presets

| Preset | Calories | Protein | Carbs | Fat |
|--------|----------|---------|-------|-----|
| **Balanced** | 2,000 | 20% | 50% | 30% |
| **Low Carb** | 1,800 | 30% | 25% | 45% |
| **High Protein** | 2,200 | 35% | 40% | 25% |
| **Keto** | 1,800 | 20% | 5% | 75% |
| **Weight Loss** | 1,500 | 30% | 40% | 30% |

### FDA Big 9 Allergens

| Allergen | Common Sources |
|----------|---------------|
| Milk | Cheese, yogurt, butter, whey, casein |
| Eggs | Baked goods, mayonnaise, pasta |
| Fish | Sauces, supplements, imitation crab |
| Shellfish | Shrimp, crab, lobster, crawfish |
| Tree Nuts | Almonds, walnuts, cashews, pecans |
| Peanuts | Peanut butter, sauces, baked goods |
| Wheat | Bread, pasta, cereals, soy sauce |
| Soy | Tofu, soy sauce, edamame, many processed foods |
| Sesame | Tahini, hummus, bread, bagels |

> Food allergy information from this tool is NOT exhaustive. Cross-contamination risks are NOT assessed. Always read actual product labels and consult your allergist for serious food allergies.


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
git clone https://github.com/YOUR_USERNAME/nutrition-label-analyzer.git
cd 86-nutrition-label-analyzer

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

**Part of the [Local LLM Projects](https://github.com/kennedyraju55) Series — Project #86/90**

Built with ❤️ using [Ollama](https://ollama.com) · [Python](https://python.org) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

*⭐ Star this repo if you find it useful!*

</div>
