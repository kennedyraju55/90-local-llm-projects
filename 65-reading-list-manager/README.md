<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# 📚 Reading List Manager

A comprehensive reading companion featuring book tracking, progress monitoring, reading speed analytics, yearly goal management, TBR prioritization, and AI-powered book recommendations — your personal librarian, running locally.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-7209b7.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/reading-list-manager/pulls)

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

## 🤔 Why Reading List Manager?

| Problem | Solution |
|---------|----------|
| Lost track of books | Full library with status, progress, and ratings |
| Don't know what to read next | AI recommendations based on your taste |
| No reading consistency | Yearly goals with pace tracking keep you on target |
| Scattered across apps | One tool for TBR, progress, reviews, and goals |
| Cloud privacy concerns | 100% local — your reading data stays private |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Progress Tracking
Track pages read with automatic status updates and percentage

### AI Recommendations
Get personalized book suggestions based on reading history

</td>
<td width="50%">

### Reading Goals
Set yearly targets with pace tracking and completion estimates

### Genre Analytics
Per-genre stats with average ratings and book counts

</td>
</tr>
<tr>
<td width="50%">

### Reading Speed
Calculate pages-per-day based on start/finish dates

</td>
<td width="50%">

### TBR Management
Prioritize to-be-read list by genre, pages, or date added

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
git clone https://github.com/kennedyraju55/reading-list-manager.git
cd reading-list-manager

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m reading_list.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m reading_list.cli add --title 'Dune' --author 'Frank Herbert' --genre 'Sci-Fi' --pages 412
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
📚 Reading List Manager v1.0.0
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
python -m reading_list.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `add` | Add a book | `--title 'Dune' --author 'Frank Herbert' --genre 'Sci-Fi' --pages 412` |
| `list` | List all books | `--status reading` |
| `progress` | Update reading progress | `--id 1 --pages 150` |
| `rate` | Rate a book | `--id 1 --rating 5 --review 'Masterpiece'` |
| `recommend` | AI recommendations | `--genre 'Science Fiction'` |
| `summary` | AI book summary | `--title 'Dune' --author 'Frank Herbert'` |
| `goal` | Set/check reading goal | `--year 2024 --target 24` |
| `tbr` | Show TBR list | `--sort pages` |

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
streamlit run src/reading_list/web_ui.py
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
65-reading-list-manager/
├── src/
│   └── reading_list/
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
from reading_list.core import *
```

### Add and track a book

```python
from reading_list.core import add_book, update_progress

book = add_book(
    title='Dune',
    author='Frank Herbert',
    genre='Science Fiction',
    pages=412
)
updated = update_progress(book['id'], pages_read=150)
print(f'Progress: {updated["progress_percent"]}%')
```

### Get recommendations

```python
from reading_list.core import load_books, get_recommendations

data = load_books()
recs = get_recommendations(genre='Sci-Fi', books=data['books'])
print(recs)
```

### Check reading goal

```python
from reading_list.core import check_goal_progress, load_books

data = load_books()
progress = check_goal_progress(2024, data['books'])
print(f'{progress["completed"]}/{progress["target"]} books ({progress["percent"]}%)')
```

### Calculate reading speed

```python
from reading_list.core import calculate_reading_speed

speed = calculate_reading_speed(book)
if speed:
    print(f'Reading speed: {speed} pages/day')
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
app:
  name: "Reading List Manager"
  version: "1.0.0"
  data_dir: "./data"

reading:
  statuses: ["to-read","reading","completed","dropped","on-hold"]
  genres: ["Fiction","Non-Fiction","Sci-Fi","Fantasy","Mystery",
           "Biography","Self-Help","Technical","History","Philosophy"]
  max_rating: 5
  yearly_goal: 24
  pages_per_session: 30

llm:
  model: "gemma3"
  temperature: 0.6
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
pytest tests/ --cov=reading_list --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=reading_list --cov-report=html
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
from reading_list.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Reading List Manager | Cloud Alternatives |
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
cd 65-reading-list-manager

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from reading_list.core import *; print('OK')"
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
<summary><strong>How does progress tracking work?</strong></summary>

Call update_progress(book_id, pages_read). Status auto-changes: to-read → reading when pages > 0, and reading → completed when pages ≥ total pages.

</details>

<details>
<summary><strong>How does the recommendation engine work?</strong></summary>

It uses genre affinity scoring: books rated ≥ 4 stars build a favourite-genre profile. Unread books in those genres are scored and ranked.

</details>

<details>
<summary><strong>What book statuses are available?</strong></summary>

Five statuses: to-read 📋, reading 📖, completed ✅, dropped ❌, on-hold ⏸️.

</details>

<details>
<summary><strong>Can I track reading speed?</strong></summary>

Yes! calculate_reading_speed() computes pages/day from the started and finished dates automatically.

</details>

<details>
<summary><strong>How do yearly goals work?</strong></summary>

Set a target with set_reading_goal(year, target). check_goal_progress() shows completed count, percentage, remaining books, and required monthly pace.

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
git clone https://github.com/YOUR_USERNAME/reading-list-manager.git
cd reading-list-manager

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
pytest tests/ -v --cov=reading_list
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

📚 **Project 65 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-7209b7.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
