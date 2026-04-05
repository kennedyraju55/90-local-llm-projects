<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# ⏱️ Time Management Coach

A comprehensive time management system with productivity scoring, Pomodoro planning, time-block scheduling, deep work analytics, weekly reviews, and AI-powered coaching — your personal productivity consultant, running 100% locally.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-f72585.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/time-management-coach/pulls)
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

## 🤔 Why Time Management Coach?

| Problem | Solution |
|---------|----------|
| No idea where time goes | Category breakdown shows exactly how you spend time |
| Low productivity | Scoring system identifies improvement areas |
| Can't focus for long | Pomodoro planning structures deep work sessions |
| Inconsistent schedule | AI time-blocking optimizes your daily plan |
| No weekly reflection | AI reviews with trends and actionable next steps |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Productivity Scoring
Weighted 1-10 score: deep work (40%), consistency (30%), balance (30%)

### Pomodoro Planning
AI-generated Pomodoro schedules with customizable intervals

</td>
<td width="50%">

### Time Blocking
Optimal schedule generation with energy-level matching

### Deep Work Analytics
Focus time stats with deep/shallow/break classification

</td>
</tr>
<tr>
<td width="50%">

### Weekly Reviews
Comprehensive AI reviews with trends and recommendations

</td>
<td width="50%">

### Week-over-Week Trends
Multi-week category breakdowns for trend analysis

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
git clone https://github.com/kennedyraju55/time-management-coach.git
cd time-management-coach

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m time_coach.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m time_coach.cli log --category coding --activity 'Feature dev' --duration 2.5
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
⏱️ Time Management Coach v1.0.0
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
git clone https://github.com/kennedyraju55/time-management-coach.git
cd time-management-coach
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
uvicorn src.time_coach.api:app --reload --port 8000

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
python -m time_coach.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `log` | Log a time entry | `--category coding --activity 'Feature dev' --duration 2.5` |
| `analyze` | AI time analysis | `--file timelog.csv` |
| `score` | Productivity score | `--file timelog.csv` |
| `blocks` | Generate time blocks | `--tasks 'Write docs, Code review, Deploy' --hours 8` |
| `pomodoro` | Pomodoro plan | `--tasks 'Write report, Review PRs' --hours 6` |
| `tips` | Get coaching tips | `--goal 'Increase deep work hours'` |
| `review` | Weekly review | `--file timelog.csv` |
| `trends` | Week-over-week trends | `--file timelog.csv --weeks 4` |

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
streamlit run src/time_coach/web_ui.py
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
70-time-management-coach/
├── src/
│   └── time_coach/
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
from time_coach.core import *
```

### Compute productivity score

```python
from time_coach.core import load_timelog, compute_time_breakdown, compute_productivity_score

entries = load_timelog('data/timelog.csv')
breakdown = compute_time_breakdown(entries)
score_info = compute_productivity_score(breakdown)
print(f'Score: {score_info["score"]}/10')
for s in score_info['suggestions']:
    print(f'  - {s}')
```

### Generate Pomodoro plan

```python
from time_coach.core import generate_pomodoro_plan

plan = generate_pomodoro_plan(
    tasks='Write documentation, Code review, Deploy to staging',
    available_hours=6.0
)
print(plan)
```

### Get focus time stats

```python
from time_coach.core import get_focus_time_stats

focus = get_focus_time_stats(entries)
print(f'Deep work: {focus["deep_work_hours"]}h')
print(f'Focus ratio: {focus["focus_ratio"]:.0%}')
```

### Compute trends

```python
from time_coach.core import compute_trends

trends = compute_trends(entries, weeks=4)
for week, breakdown in trends.items():
    print(f'{week}: {sum(breakdown.values()):.1f}h total')
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
llm:
  model: "gemma3"
  temperature: 0.6
  max_tokens: 2000

time_log: timelog.csv

pomodoro:
  work_minutes: 25
  short_break: 5
  long_break: 15
  sessions_before_long: 4

productivity:
  target_deep_work_hours: 4.0
  target_total_hours: 8.0
  categories:
    deep_work: ["coding", "writing", "design", "research"]
    shallow_work: ["email", "meetings", "admin"]
    breaks: ["lunch", "break", "exercise"]

scoring:
  deep_work_weight: 0.4
  consistency_weight: 0.3
  balance_weight: 0.3
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
pytest tests/ --cov=time_coach --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=time_coach --cov-report=html
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
from time_coach.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Time Management Coach | Cloud Alternatives |
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
cd 70-time-management-coach

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from time_coach.core import *; print('OK')"
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
<summary><strong>How is the productivity score calculated?</strong></summary>

Score = (deep_work_ratio × 0.4 + consistency × 0.3 + balance × 0.3) × 10. Deep work ratio = actual/target hours. Consistency = how close total is to target. Balance = break presence.

</details>

<details>
<summary><strong>What are the Pomodoro defaults?</strong></summary>

25-minute work sessions, 5-minute short breaks, 15-minute long breaks every 4 sessions. All customizable in config.yaml.

</details>

<details>
<summary><strong>What time categories exist?</strong></summary>

Three categories: deep_work (coding, writing, design, research), shallow_work (email, meetings, admin), breaks (lunch, break, exercise).

</details>

<details>
<summary><strong>How does time blocking work?</strong></summary>

generate_time_blocks() uses AI to assign tasks to optimal time blocks based on energy levels. Morning for deep work, mid-morning for meetings, etc.

</details>

<details>
<summary><strong>What CSV format is expected?</strong></summary>

CSV with columns: date, category, activity, duration. Duration can be hours as decimal (2.5) or with 'h' suffix (2.5h).

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
git clone https://github.com/YOUR_USERNAME/time-management-coach.git
cd time-management-coach

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
pytest tests/ -v --cov=time_coach
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

⏱️ **Project 70 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-f72585.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
