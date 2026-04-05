<!-- DO NOT EDIT — Auto-generated portfolio README -->
<div align="center">

![Banner](docs/images/banner.svg)

# 🏠 Home Automation Scripter

Generate production-ready home automation scripts from natural language descriptions. Supports Home Assistant, IFTTT, openHAB, Node-RED, and SmartThings with 6 pre-built templates, script validation, and AI-powered suggestions.

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_AI-06d6a0.svg?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000.svg?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Private](https://img.shields.io/badge/100%25-Private-2ea043.svg?style=for-the-badge&logo=shield&logoColor=white)](#-local-vs-cloud)

[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B.svg?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-4EAA25.svg?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![pytest](https://img.shields.io/badge/pytest-tested-009688.svg?style=flat-square&logo=pytest&logoColor=white)](https://pytest.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/kennedyraju55/home-automation-scripter/pulls)

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

## 🤔 Why Home Automation Scripter?

| Problem | Solution |
|---------|----------|
| YAML syntax is confusing | Describe automations in plain English |
| Starting from scratch | 6 pre-built templates with parameter fill-in |
| Debugging automation scripts | AI explains what any script does in plain language |
| Don't know what's possible | AI suggests automations based on your devices |
| Script errors | Platform-specific validation catches issues before deployment |

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<td width="50%">

### Multi-Platform
Generate scripts for Home Assistant, IFTTT, openHAB, Node-RED, SmartThings

### Template Library
6 pre-built templates: motion light, thermostat, security, morning, energy, bedtime

</td>
<td width="50%">

### Natural Language
Describe automations in plain English — AI generates the code

### Script Validation
Platform-specific validation with error and warning reporting

</td>
</tr>
<tr>
<td width="50%">

### Script Explanation
AI explains what any automation script does in plain language

</td>
<td width="50%">

### Device Suggestions
AI suggests useful automations based on your device list

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
git clone https://github.com/kennedyraju55/home-automation-scripter.git
cd home-automation-scripter

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull the AI model
ollama pull gemma3

# 5. Verify setup
python -m home_automation.cli --help
```

### First Run

```bash
# Start Ollama (if not running)
ollama serve &

# Run your first command
python -m home_automation.cli generate --rule 'Turn on lights at sunset' --platform homeassistant
```

<details>
<summary><strong>📋 Example Output</strong></summary>

```
🏠 Home Automation Scripter v1.0.0
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
python -m home_automation.cli [COMMAND] [OPTIONS]
```

### Commands

| Command | Description | Key Options |
|---------|-------------|-------------|
| `generate` | Generate automation from description | `--rule 'Turn on lights at sunset' --platform homeassistant` |
| `explain` | Explain an existing script | `--file script.yaml --platform homeassistant` |
| `suggest` | Suggest automations | `--devices 'motion sensor, smart bulb, thermostat'` |
| `templates` | List available templates | `--category lighting` |
| `from-template` | Generate from template | `--template motion_light --platform homeassistant` |
| `validate` | Validate a script | `--file script.yaml --platform homeassistant` |
| `rules` | List saved rules | — |

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
streamlit run src/home_automation/web_ui.py
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
66-home-automation-scripter/
├── src/
│   └── home_automation/
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
from home_automation.core import *
```

### Generate automation

```python
from home_automation.core import generate_automation

script = generate_automation(
    rule_description='Turn on porch light at sunset',
    platform='homeassistant'
)
print(script)
```

### Use a template

```python
from home_automation.core import generate_from_template

script = generate_from_template(
    template_id='motion_light',
    platform='homeassistant',
    params={'motion_sensor': 'binary_sensor.hallway',
            'light_entity': 'light.hallway',
            'delay_minutes': '5'}
)
print(script)
```

### Validate a script

```python
from home_automation.core import validate_script

result = validate_script(script, platform='homeassistant')
print(f'Valid: {result["valid"]}')
for err in result['errors']:
    print(f'Error: {err}')
```

### Suggest automations

```python
from home_automation.core import suggest_automations

suggestions = suggest_automations(
    devices='motion sensor, smart thermostat, door lock'
)
print(suggestions)
```

---

## ⚙️ Configuration

Create a `config.yaml` in the project root:

```yaml
llm:
  model: "gemma3"
  temperature: 0.4
  max_tokens: 2000

platforms:
  - homeassistant
  - ifttt
  - smartthings
  - openhab
  - nodered

default_platform: homeassistant
rules_file: automation_rules.json

scheduling:
  enabled: false
  cron_format: true
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
pytest tests/ --cov=home_automation --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run only unit tests (fast)
pytest tests/test_core.py -v -k "not integration"

# Generate HTML coverage report
pytest tests/ --cov=home_automation --cov-report=html
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
from home_automation.core import *

def test_basic_functionality():
    """Test core function returns expected output."""
    result = load_config()
    assert isinstance(result, dict)
    assert "llm" in result
```

---

## 🔒 Local vs Cloud

| Feature | Home Automation Scripter | Cloud Alternatives |
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
cd 66-home-automation-scripter

# Reinstall dependencies
pip install -r requirements.txt

# Verify the package is importable
python -c "from home_automation.core import *; print('OK')"
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
<summary><strong>Which platforms are supported?</strong></summary>

Home Assistant (YAML), IFTTT (applet rules), openHAB (DSL), Node-RED (JSON flows), and SmartThings (Rules API/Groovy).

</details>

<details>
<summary><strong>What templates are available?</strong></summary>

6 templates: motion_light (lighting), thermostat_schedule (climate), security_alert (security), good_morning (routine), energy_saver (energy), bedtime (routine).

</details>

<details>
<summary><strong>How does validation work?</strong></summary>

Platform-specific regex patterns check for required structural elements. E.g., Home Assistant scripts must contain 'automation:', 'trigger:', and 'action:' keys.

</details>

<details>
<summary><strong>Can I save and reuse rules?</strong></summary>

Yes! Rules are persisted to automation_rules.json with auto-incrementing IDs and timestamps. Use save_rule() and load_rules().

</details>

<details>
<summary><strong>How does natural language generation work?</strong></summary>

Your description is sent to the local LLM with platform-specific instructions. The AI generates complete, production-ready automation code.

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
git clone https://github.com/YOUR_USERNAME/home-automation-scripter.git
cd home-automation-scripter

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
pytest tests/ -v --cov=home_automation
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

🏠 **Project 66 of 90** — Made with ❤️ and local AI

[![Back to Main](https://img.shields.io/badge/← Back_to-90_Projects-06d6a0.svg?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
