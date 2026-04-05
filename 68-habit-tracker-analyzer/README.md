<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# 🎯 Habit Tracker Analyzer

A comprehensive habit tracking system with streak computation, completion rate analytics, habit correlation discovery, gamified achievements (6 types), calendar heatmaps, weekly/monthly reports, and AI-powered behavioral analysis.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-e63946.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/habit-tracker-analyzer/pulls)

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

## 🤔 Why Habit Tracker Analyzer?

| Problem | Solution |
|---------|----------|
| Habits don't stick | Streak tracking and achievements provide motivation |
| No data on consistency | Completion rates show exactly how you're doing |
| Don't know what works | Correlation analysis reveals habit synergies |
| Generic habit apps | AI provides personalized behavioral insights |
| Privacy with habit data | 100% local — your habits stay your business |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Streak Tracking
Current and best streak computation for every habit

### Completion Rates
Percentage-based tracking over configurable time periods

</td>
<td width="50%">

### Habit Correlations
Discover which habits you tend to do together

### Achievements System
6 gamified achievements: First Step 🌱 to Consistency King 👑

</td>
</tr>
<tr>
<td width="50%">

### Calendar Heatmap
Date-based completion data for visual heatmap rendering

</td>
<td width="50%">

### AI Analysis
Behavioral science insights with habit stacking suggestions

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
git clone https://github.com/kennedyraju55/habit-tracker-analyzer.git
cd habit-tracker-analyzer

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m habit_tracker.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m habit_tracker.cli log --habit 'Exercise' --notes 'Morning run 5km'
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
🎯 Habit Tracker Analyzer v1.0.0
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Connected to Ollama (Gemma 4)
✓ Processing...
✓ Done! Results displayed below.
```

</details>

---

## 📟 CLI Reference

All commands are available via the Click-based CLI:

```bash
python -m habit_tracker.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `log` | Log a habit | `--habit 'Exercise' --notes 'Morning run 5km'` |
| `add` | Add new habit | `--name 'Meditation' --category health --target daily` |
| `streak` | Show streaks | — |
| `rate` | Show completion rates | `--days 30` |
| `report` | Generate report | `--type weekly` |
| `analyze` | AI habit analysis | `--period month` |
| `achievements` | Show earned achievements | — |
| `correlations` | Show habit correlations | — |

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
streamlit run src/habit_tracker/web_ui.py
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
68-habit-tracker-analyzer/
├── src/
│   └── habit_tracker/
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
from habit_tracker.core import *
```

### Log a habit

```python
from habit_tracker.core import log_habit

entry = log_habit(
    habit_name='Exercise',
    done=True,
    notes='Morning run - 5km in 28 minutes'
)
print(f'Logged: {entry["habit"]} on {entry["date"]}')
```

### Check streaks

```python
from habit_tracker.core import load_habits, compute_streaks

data = load_habits()
streaks = compute_streaks(data)
for habit, info in streaks.items():
    print(f'{habit}: {info["current"]} days (best: {info["best"]})')
```

### Find correlations

```python
from habit_tracker.core import compute_correlations

correlations = compute_correlations(data)
for pair, info in correlations.items():
    print(f'{pair}: {info["rate"]}% co-occurrence')
```

### Check achievements

```python
from habit_tracker.core import check_achievements

achievements = check_achievements(data)
for ach in achievements:
    print(f'{ach["icon"]} {ach["name"]}: {ach["description"]}')
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
llm:
  model: "gemma3"
  temperature: 0.6
  max_tokens: 2000

habits_file: habits.json
default_target: daily

achievements:
  enabled: true
  notifications: true

reports:
  weekly: true
  monthly: true

logging:
  level: INFO
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
pytest tests/ --cov=habit_tracker --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=habit_tracker --cov-report=html
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
from habit_tracker.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Habit Tracker Analyzer | Cloud Alternatives |
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
cd 68-habit-tracker-analyzer

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from habit_tracker.core import *; print('OK')"
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
<summary><strong>What achievements can I earn?</strong></summary>

6 achievements: First Step 🌱 (first log), Week Warrior 🔥 (7-day streak), Monthly Master ⭐ (30-day streak), Century Club 💯 (100-day streak), Perfect Week 🏆 (all habits 7 days), Consistency King 👑 (90%+ for 30 days).

</details>

<details>
<summary><strong>How are correlations calculated?</strong></summary>

The system checks which habits are completed on the same day using combinatorial pair analysis. Co-occurrence rate = (days both done / total tracked days) × 100.

</details>

<details>
<summary><strong>How does streak tracking work?</strong></summary>

Current streak counts backwards from today. Best streak uses a sweep across all logged dates. Both are computed per-habit independently.

</details>

<details>
<summary><strong>Can I track non-daily habits?</strong></summary>

Yes! Set target to 'weekly' or custom. The system is flexible — log_habit() records completions regardless of target frequency.

</details>

<details>
<summary><strong>How does AI analysis help?</strong></summary>

The AI analyzes streaks, rates, and correlations to provide behavioral insights, habit stacking suggestions, and personalized improvement tips.

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
git clone https://github.com/YOUR_USERNAME/habit-tracker-analyzer.git
cd habit-tracker-analyzer

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
pytest tests/ -v --cov=habit_tracker
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

🎯 **Project 68 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-e63946.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
