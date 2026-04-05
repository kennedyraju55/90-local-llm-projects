<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# 💰 Household Budget Analyzer

A comprehensive household budget management tool with AI-powered spending analysis, auto-categorization, budget vs. actual comparison, recurring expense detection, savings goal tracking, and monthly trend analysis — all private.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-ff6b35.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/household-budget-analyzer/pulls)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

---

[Features](#-features) •
[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[Architecture](#-architecture) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[Testing](#-testing) •
[FAQ](#-faq) •
[Contributing](#-contributing)

</div>

---

## 🤔 Why Household Budget Analyzer?

| Problem | Solution |
|---------|----------|
| No idea where money goes | Automatic category breakdown with percentages |
| Surprise subscriptions | Recurring expense detection catches hidden charges |
| Overspending categories | Budget vs. actual shows exactly where you're over |
| No savings progress | SavingsGoal tracks progress with completion dates |
| Month-to-month blindness | Trend analysis reveals spending patterns over time |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Budget Analysis
AI-powered spending pattern analysis with savings tips

### Auto-Categorization
Rule-based expense categorization from descriptions

</td>
<td width="50%">

### Budget vs Actual
Compare spending against budget limits by category

### Savings Goals
Track progress with completion date estimation (SavingsGoal)

</td>
</tr>
<tr>
<td width="50%">

### Recurring Detection
Identify subscriptions and recurring charges automatically

</td>
<td width="50%">

### Monthly Trends
Chronological spending trends with month-over-month comparison

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.11+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | Via Ollama | AI model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/household-budget-analyzer.git
cd household-budget-analyzer

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m budget_analyzer.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m budget_analyzer.cli analyze --file expenses.csv --month 'March 2024'
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
💰 Household Budget Analyzer v1.0.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Connected to Ollama (Gemma 4)
✓ Processing...
✓ Done! Results displayed below.
```

</details>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/household-budget-analyzer.git
cd household-budget-analyzer
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
uvicorn src.budget_analyzer.api:app --reload --port 8000

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

## 📟 CLI Reference

All commands are available via the Click-based CLI:

```bash
python -m budget_analyzer.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `analyze` | AI budget analysis | `--file expenses.csv --month 'March 2024'` |
| `breakdown` | Category spending breakdown | `--file expenses.csv` |
| `compare` | Month-over-month comparison | `--file expenses.csv` |
| `budget-check` | Budget vs actual comparison | `--file expenses.csv` |
| `recurring` | Detect recurring expenses | `--file expenses.csv` |
| `top` | Show top N expenses | `--file expenses.csv --top 10` |
| `trends` | Monthly spending trends | `--file expenses.csv` |

### Global Options

| Option | Description | Default |
|--------|-------------|---------|
| `--config` | Path to config.yaml | `config.yaml` |
| `--verbose` / `-v` | Enable debug logging | `false` |
| `--help` | Show help message | — |

---

## 🌐 Web UI

Launch the Streamlit web interface:

```bash
streamlit run src/budget_analyzer/web_ui.py
```

The web UI provides:
- 🎨 **Interactive dashboard** with rich visualizations
- 📊 **Real-time results** with formatted output
- 🔧 **Point-and-click** configuration — no CLI needed
- 📱 **Responsive design** — works on desktop and mobile

> Access at `http://localhost:8501` after launching.

---

## 🏗️ Architecture

![Architecture](docs/images/architecture.svg)

### Project Structure

```
64-household-budget-analyzer/
├── src/
│   └── budget_analyzer/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Business logic & AI features
│       ├── cli.py               # Click CLI interface
│       └── web_ui.py            # Streamlit web interface
├── data/                        # Data storage (JSON/CSV)
├── tests/
│   ├── test_core.py             # Core logic tests
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/                  # SVG documentation images
├── config.yaml                  # Application configuration
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

### Data Flow

```
User Input → CLI/Web UI → Core Engine → Local LLM (Ollama/Gemma 4) → Formatted Output
                              ↓
                        JSON/CSV Storage
```

---

## 📖 API Reference

Import and use the core module directly in Python:

```python
from budget_analyzer.core import *
```

### Load and analyze expenses

```python
from budget_analyzer.core import load_expenses, compute_category_breakdown, compute_total

expenses = load_expenses('data/expenses.csv')
categories = compute_category_breakdown(expenses)
total = compute_total(expenses)
print(f'Total spending: ${total:,.2f}')
```

### Detect recurring expenses

```python
from budget_analyzer.core import detect_recurring

recurring = detect_recurring(expenses)
for item in recurring:
    print(f'{item["description"]}: ${item["avg_amount"]:.2f}/mo')
```

### Track savings goals

```python
from budget_analyzer.core import SavingsGoal

goal = SavingsGoal(
    name='Emergency Fund',
    target_amount=5000,
    current_amount=2000,
    monthly_contribution=500
)
print(goal.track_progress())
print(f'Est. completion: {goal.estimate_completion()}')
```

### Budget vs actual

```python
from budget_analyzer.core import compare_budget_vs_actual

results = compare_budget_vs_actual(categories)
for r in results:
    print(f'{r["category"]}: ${r["actual"]:.2f} / ${r["budget"]} ({r["status"]})')
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
app:
  name: "Household Budget Analyzer"
  version: "1.0.0"
  data_dir: "./data"

budget:
  categories:
    Groceries: 600
    Utilities: 200
    Entertainment: 150
  category_rules:
    Groceries: ["walmart", "kroger", "whole foods"]
    Utilities: ["electric", "water", "internet"]

llm:
  model: "gemma3"
  temperature: 0.5
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |
| `DATA_DIR` | Data storage directory | `./data` |

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=budget_analyzer --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=budget_analyzer --cov-report=html
open htmlcov/index.html
```

### Test Coverage

| Module | Statements | Miss | Coverage | Key Tests |
|--------|-----------|------|----------|-----------|
| `core.py` | ~150 | ~22 | 85%+ | Unit tests for all public functions |
| `cli.py` | ~100 | ~20 | 80%+ | Click runner integration tests |
| `web_ui.py` | ~80 | ~24 | 70%+ | Streamlit component tests |
| **Total** | **~330** | **~66** | **80%+** | **Full regression suite** |

### Writing Tests

```python
# tests/test_core.py
import pytest
from budget_analyzer.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Household Budget Analyzer | Cloud Alternatives |
|---------|---------|-------------------|
| **Privacy** | ✅ 100% local — data never leaves your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free forever — no API keys needed | ❌ $10-50/month subscription fees |
| **Speed** | ✅ No network latency — instant responses | ❌ 500ms-2s API round-trip delay |
| **Offline** | ✅ Works without internet connection | ❌ Requires constant internet access |
| **Customization** | ✅ Full source code control | ❌ Limited by provider's API |
| **Data Ownership** | ✅ Your machine, your data, your rules | ❌ Stored on corporate servers |
| **Model Choice** | ✅ Swap models freely (Gemma, Llama, Mistral) | ❌ Locked to provider's model |
| **Compliance** | ✅ GDPR/HIPAA friendly — no data transfer | ❌ May violate data regulations |

---

## 🔧 Troubleshooting

<details>
<summary><strong>Ollama not connecting</strong></summary>

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Start Ollama if needed
ollama serve

# Verify model is available
ollama list
```

</details>

<details>
<summary><strong>Model not found</strong></summary>

```bash
# Pull the required model
ollama pull gemma3

# Or use a different model — update config.yaml:
# llm:
#   model: "llama3"
```

</details>

<details>
<summary><strong>Import errors</strong></summary>

```bash
# Ensure you're in the project root
cd 64-household-budget-analyzer

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from budget_analyzer.core import *; print('OK')"
```

</details>

<details>
<summary><strong>Slow responses</strong></summary>

The first request may take longer as the model loads into memory. Subsequent requests will be much faster. For better performance:

- Use a smaller model: `ollama pull gemma3:2b`
- Ensure sufficient RAM (8GB+ recommended)
- Use GPU acceleration if available

</details>

---

## ❓ FAQ

<details>
<summary><strong>What CSV format is expected?</strong></summary>

CSV files with columns: date, description, category, amount. Dates can be YYYY-MM-DD, MM/DD/YYYY, or DD/MM/YYYY. Amounts can include $ and commas.

</details>

<details>
<summary><strong>How does auto-categorization work?</strong></summary>

Keyword rules in config.yaml map description keywords to categories. E.g., 'walmart' → Groceries. Falls back to 'Other' if no match.

</details>

<details>
<summary><strong>What is the SavingsGoal class?</strong></summary>

A Python dataclass that tracks savings progress with track_progress() returning percentage complete and estimate_completion() predicting the finish date.

</details>

<details>
<summary><strong>How is recurring expense detection done?</strong></summary>

Groups transactions by description, checks if amounts are within 10% tolerance of average, and verifies they appear across 2+ months.

</details>

<details>
<summary><strong>Can I customize budget limits?</strong></summary>

Yes! Set per-category budget limits in config.yaml under budget.categories. The budget-check command compares actual spending against these limits.

</details>

---

## 🗺️ Roadmap

- [ ] Add more AI model support (Phi-3, CodeGemma)
- [ ] Docker containerization for easy deployment
- [ ] Plugin system for custom extensions
- [ ] REST API endpoint for programmatic access
- [ ] Enhanced web UI with data visualizations
- [ ] Multi-language support (i18n)
- [ ] Automated backup and restore
- [ ] CI/CD pipeline with GitHub Actions

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/household-budget-analyzer.git
cd household-budget-analyzer

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov black ruff

# Run linting
ruff check src/
black --check src/

# Run tests before submitting
pytest tests/ -v --cov=budget_analyzer
```

### Code Style

- Follow PEP 8 conventions
- Use type hints for all function signatures
- Write docstrings for all public functions
- Keep functions focused and under 50 lines
- Add tests for all new features

---

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 kennedyraju55

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

<div align="center">

**Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — Building the future of private, local AI applications.

💰 **Project 64 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-ff6b35.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
