<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# 🧠 Personal Knowledge Base

A private, AI-enhanced knowledge management system featuring semantic search, automatic backlink discovery, tag clouds, note templates, and Markdown import/export — your second brain, powered by local AI.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-00b4d8.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/personal-knowledge-base/pulls)

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

## 🤔 Why Personal Knowledge Base?

| Problem | Solution |
|---------|----------|
| Notes scattered everywhere | Single searchable knowledge base with tags |
| Can't find related info | AI semantic search finds conceptual matches |
| No connections between notes | Automatic backlink discovery links related ideas |
| Starting from scratch every time | Templates for meetings, reviews, and projects |
| Cloud privacy concerns | 100% local storage — your data never leaves your machine |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Semantic Search
AI-powered search finds conceptually related notes

### Backlink Discovery
Automatic cross-reference detection between notes

</td>
<td width="50%">

### Tag Cloud
Visual tag frequency analysis across your knowledge base

### Note Templates
Pre-built templates: meeting notes, book review, project plan

</td>
</tr>
<tr>
<td width="50%">

### Full-Text Search
Fast keyword search across titles, content, and tags

</td>
<td width="50%">

### Markdown Export
Export/import entire knowledge base as Markdown

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
git clone https://github.com/kennedyraju55/personal-knowledge-base.git
cd personal-knowledge-base

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m knowledge_base.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m knowledge_base.cli add --title 'My Note' --tags python,ai
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
🧠 Personal Knowledge Base v1.0.0
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
python -m knowledge_base.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `add` | Add a new note | `--title 'My Note' --tags python,ai` |
| `search` | AI semantic search | `--query 'machine learning concepts'` |
| `list` | List all notes | — |
| `tags` | Show tag cloud | — |
| `backlinks` | Find note references | `--id 5` |
| `export` | Export to Markdown | `--output kb_export.md` |
| `import` | Import from Markdown | `--file kb_export.md` |
| `summarize` | AI knowledge base summary | — |

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
streamlit run src/knowledge_base/web_ui.py
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
62-personal-knowledge-base/
├── src/
│   └── knowledge_base/
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
from knowledge_base.core import *
```

### Add a note

```python
from knowledge_base.core import add_note

note = add_note(
    title='Python Decorators',
    content='Decorators wrap functions to extend behavior...',
    tags=['python', 'patterns']
)
print(f'Created note #{note["id"]}')
```

### Semantic search

```python
from knowledge_base.core import search_notes

results = search_notes('design patterns in Python')
print(results)
```

### Find backlinks

```python
from knowledge_base.core import find_backlinks

refs = find_backlinks(note_id=3)
for ref in refs:
    print(f'Referenced by: {ref["title"]}')
```

### Use templates

```python
from knowledge_base.core import apply_template

note = apply_template('meeting_notes', date='2024-03-15')
print(note['title'])  # 'Meeting Notes - 2024-03-15'
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
app:
  name: "Personal Knowledge Base"
  version: "1.0.0"
  data_dir: "./data"

knowledge_base:
  max_notes: 10000
  default_tags: []
  search_limit: 20
  backup_enabled: true
  backup_interval_hours: 24

templates:
  meeting_notes:
    title: "Meeting Notes - {date}"
    content: "## Attendees\n\n## Agenda\n\n## Action Items"

llm:
  model: "gemma3"
  temperature: 0.3
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
pytest tests/ --cov=knowledge_base --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=knowledge_base --cov-report=html
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
from knowledge_base.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Personal Knowledge Base | Cloud Alternatives |
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
cd 62-personal-knowledge-base

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from knowledge_base.core import *; print('OK')"
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
<summary><strong>How does semantic search differ from full-text search?</strong></summary>

Full-text search matches exact keywords. Semantic search uses AI to understand meaning — searching 'design patterns' can find notes about 'factory method' or 'singleton'.

</details>

<details>
<summary><strong>What are backlinks?</strong></summary>

Backlinks are automatic cross-references. If Note A mentions Note B's title in its content, Note B will show Note A as a backlink — like a wiki.

</details>

<details>
<summary><strong>Can I create custom templates?</strong></summary>

Yes! Add templates to config.yaml under the 'templates' section with 'title' and 'content' keys using {placeholder} syntax.

</details>

<details>
<summary><strong>What's the storage format?</strong></summary>

Notes are stored as JSON in data/knowledge_base.json. Each note has id, title, content, tags, created, and updated fields.

</details>

<details>
<summary><strong>How do I migrate from other tools?</strong></summary>

Export your notes as Markdown, then use the import command. The importer parses the standard export format with ## headers and metadata.

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
git clone https://github.com/YOUR_USERNAME/personal-knowledge-base.git
cd personal-knowledge-base

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
pytest tests/ -v --cov=knowledge_base
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

🧠 **Project 62 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-00b4d8.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
