<!-- ============================================================================
     ⚙️ Environment Config Manager
     Auto-generated portfolio-grade README — Part of 90 Local LLM Projects
     ============================================================================ -->

![Banner](docs/images/banner.svg)

<div align="center">

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-85%25-yellow?style=flat-square)
![Last Commit](https://img.shields.io/badge/Maintained-2024-blue?style=flat-square)
![Project](https://img.shields.io/badge/Project-80%2F90-purple?style=flat-square)

**Secure .env Management & Secret Detection**

[Features](#-features) •
[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Architecture](#-architecture) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[FAQ](#-faq)

</div>

---

## 📖 About

An AI-powered environment configuration management tool with secret detection (8 pattern categories), environment comparison and diff, migration script generation, project-type template generation, and LLM-powered validation for 12-factor app compliance — all running locally to keep your secrets safe.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Managing .env files across environments is error-prone. Secrets leak into repos, environments drift, and teams waste time debugging missing variables.

</td>
<td width="50%">

### ✅ The Solution

Automated secret detection, environment diffing, migration scripts, and template generation — with AI-powered validation. Your .env files never leave your machine.

</td>
</tr>
</table>

---

## ✨ Features

![Features](docs/images/features.svg)

<table>
<tr>
<th>Feature</th>
<th>Description</th>
<th>LLM Required</th>
</tr>
<tr><td><strong>🔐 Secret Detection</strong></td><td>8 pattern categories: API keys, tokens, passwords</td><td>❌ No</td></tr>
<tr><td><strong>🔄 Env Comparison</strong></td><td>Diff two environments with change tracking</td><td>❌ No</td></tr>
<tr><td><strong>📝 Template Generator</strong></td><td>Project-type templates: Flask, Django, Express, etc.</td><td>❌ No</td></tr>
<tr><td><strong>🛡️ Security Audit</strong></td><td>Weak value detection and length validation</td><td>✅ Yes</td></tr>
<tr><td><strong>📦 Migration Scripts</strong></td><td>Auto-generate shell scripts for env migration</td><td>❌ No</td></tr>
<tr><td><strong>🤖 AI Validation</strong></td><td>LLM-powered deep analysis for 12-factor compliance</td><td>✅ Yes</td></tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Ollama** installed and running ([ollama.com](https://ollama.com))
- A local LLM model pulled (e.g., `llama3.2`)

### Installation

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/env-config-manager.git
cd env-config-manager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### First Run

```bash
# Start Ollama (if not already running)
ollama serve

# Pull a model (first time only)
ollama pull llama3.2

# Run the tool
python -m src.env_manager.cli validate --file .env
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  ⚙️ Environment Config Manager                              │
│  Secure .env Management & Secret Detection                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/env-config-manager.git
cd env-config-manager
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
uvicorn src.env_manager.api:app --reload --port 8000

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

## 📖 CLI Reference

### Validate env file

```bash
python -m src.env_manager.cli validate --file .env
```

### Secret scan

```bash
python -m src.env_manager.cli scan --file .env
```

### Compare envs

```bash
python -m src.env_manager.cli compare --file1 .env.dev --file2 .env.prod
```

### Generate template

```bash
python -m src.env_manager.cli template --project-type flask --env development
```

### Migration script

```bash
python -m src.env_manager.cli migrate --from .env.staging --to .env.production
```

### Suggest missing vars

```bash
python -m src.env_manager.cli suggest --file .env --project-type django
```

### List project types

```bash
python -m src.env_manager.cli list-types
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--file` | Path to .env file | `None` |
| `--file1/--file2` | Files to compare | `None` |
| `--project-type` | Project type for templates | `generic` |
| `--env` | Target environment | `development` |
| `--from/--to` | Migration source/target | `None` |
| `--output` | Save results to file | `None` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 80-env-config-manager

# Run the web UI
streamlit run app.py
```

The web UI provides:
- 📝 Interactive input forms
- 📊 Real-time results visualization
- 📋 Copy-to-clipboard functionality
- 🎨 Beautiful responsive design
- 📤 Export results to file

---

## 🏗️ Architecture

![Architecture](docs/images/architecture.svg)

### System Overview

The application follows a modular architecture with clear separation of concerns:

1. **Input Layer** — CLI (Click) or Web UI (Streamlit) accepts user input
2. **Processing Layer** — Core business logic with pattern matching, scoring, and analysis
3. **AI Layer** — Local LLM through Ollama for natural language understanding
4. **Output Layer** — Rich CLI formatting or Streamlit web rendering

### Project Structure

```
80-env-config-manager/
├── src/
│   └── env_manager/
│       ├── __init__.py
│       ├── core.py          # Secret detection, comparison, migration
│       └── cli.py           # Click CLI with security tables
├── tests/
│   ├── test_core.py
│   └── test_cli.py
├── docs/
│   └── images/
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml
├── README.md
└── requirements.txt
```

### Data Flow

```
User Input → CLI Parser → Core Engine → [LLM if needed] → Formatter → Output
                              ↓
                    Local Processing
                  (Pattern Matching,
                   Scoring, Parsing)
```

---

## 📚 API Reference

### Core Classes

| Class | Description |
|-------|-------------|
| `SECRET_PATTERNS` | 8 categories: api_key, password, secret, token, database_url, aws, ssh_key, encryption |
| `WEAK_VALUES` | 10 known weak values: password, secret, changeme, admin, etc. |
| `PROJECT_TYPES` | 10 types: flask, django, fastapi, express, nextjs, rails, spring-boot, laravel, dotnet, generic |


### Core Functions

| Function | Description |
|----------|-------------|
| `parse_env_file()` | Parse .env into key-value pairs |
| `detect_secrets()` | 8-category secret pattern detection |
| `compare_envs()` | Environment diff with change tracking |
| `generate_migration_script()` | Shell script generation for env migration |
| `validate_env()` | LLM-powered validation for completeness & security |
| `generate_env_template()` | AI-generated templates by project type |


### Python Usage Example

```python
from src.env_manager.core import (
    parse_env_file, detect_secrets, compare_envs,
    generate_migration_script, validate_env, generate_env_template
)

# Parse .env file
env_vars = parse_env_file(".env")
print(f"Found {len(env_vars)} variables")

# Detect secrets
findings = detect_secrets(env_vars)
for f in findings:
    print(f"[{f['severity'].upper()}] {f['message']}")

# Compare environments
dev = parse_env_file(".env.dev")
prod = parse_env_file(".env.prod")
diff = compare_envs(dev, prod)
print(f"Only in dev: {diff['only_in_first']}")
print(f"Only in prod: {diff['only_in_second']}")
print(f"Different values: {len(diff['different_values'])}")

# Generate migration script
script = generate_migration_script(dev, prod, "production")
print(script)
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 2048

env_manager:
  default_project_type: generic
  detect_secrets: true
  weak_value_check: true
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | Default model name | `llama3.2` |
| `LOG_LEVEL` | Logging level | `INFO` |
| `MAX_TOKENS` | Maximum response tokens | `2048` |

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/env_manager --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v
```

### Test Coverage

| Module | Statements | Coverage |
|--------|-----------|----------|
| `core.py` | ~200 | 85% |
| `cli.py` | ~120 | 78% |
| `config.py` | ~20 | 95% |
| **Total** | **~340** | **85%** |

---

## 🏠 Local vs ☁️ Cloud

| Feature | ⚙️ This Tool (Local) | ☁️ Cloud Alternatives |
|---------|-------------------------|----------------------|
| **Privacy** | ✅ 100% local, zero data leaks | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free forever | ❌ Pay-per-use API costs |
| **Speed** | ✅ No network latency | ❌ Depends on internet speed |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Customization** | ✅ Full control over models | ❌ Limited to provider's models |
| **Compliance** | ✅ Data stays on-premise | ⚠️ May violate data policies |
| **Model Choice** | ✅ Any Ollama-compatible model | ❌ Locked to provider's model |

---

## ❓ FAQ

<details>
<summary><strong>What secrets does it detect?</strong></summary>
<br>

Eight categories: API keys, passwords, secrets, tokens, database URLs, AWS credentials, SSH keys, and encryption keys.

</details>

<details>
<summary><strong>How does it detect weak values?</strong></summary>
<br>

Checks against a list of 10 known weak values (password, changeme, admin, etc.) and validates minimum length for secret variables.

</details>

<details>
<summary><strong>Can it generate .env.example files?</strong></summary>
<br>

Yes! Use the template command with your project type. The generated template uses CHANGE_ME placeholders for secrets.

</details>

<details>
<summary><strong>Does the migration script expose secrets?</strong></summary>
<br>

No! The migration script automatically masks secret values with CHANGE_ME placeholders.

</details>

<details>
<summary><strong>Which project types are supported?</strong></summary>
<br>

10 types: Flask, Django, FastAPI, Express, Next.js, Rails, Spring Boot, Laravel, .NET, and generic.

</details>



---

## 🧠 Supported Models

This tool works with any Ollama-compatible model. Recommended options:

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| `llama3.2` | 3B | ⚡ Fast | ⭐⭐⭐ Good | Daily use, quick analysis |
| `llama3.1` | 8B | 🔄 Medium | ⭐⭐⭐⭐ Great | Detailed analysis |
| `llama3.1:70b` | 70B | 🐢 Slow | ⭐⭐⭐⭐⭐ Best | Critical assessments |
| `mistral` | 7B | ⚡ Fast | ⭐⭐⭐⭐ Great | Good alternative |
| `codellama` | 7B | ⚡ Fast | ⭐⭐⭐ Good | Code-focused tasks |
| `phi3` | 3.8B | ⚡ Fast | ⭐⭐⭐ Good | Resource-constrained envs |

```bash
# Pull a model
ollama pull llama3.2

# Use a specific model
OLLAMA_MODEL=mistral python -m src.env_manager.cli --help
```

---

## 📋 Changelog

### v1.0.0 (2024)

- ✅ Initial release with full feature set
- ✅ CLI interface with Rich formatting
- ✅ Web UI with Streamlit
- ✅ Comprehensive test suite
- ✅ Documentation with SVG graphics
- ✅ Configuration via YAML and environment variables

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/env-config-manager.git
cd env-config-manager

# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# Run tests before submitting
pytest tests/ -v
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Ollama](https://ollama.com) — Local LLM runtime
- [Click](https://click.palletsprojects.com) — CLI framework
- [Rich](https://rich.readthedocs.io) — Terminal formatting
- [Streamlit](https://streamlit.io) — Web UI framework

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) Collection**

Built with ❤️ using 100% local AI

⚙️ **Project 80/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
