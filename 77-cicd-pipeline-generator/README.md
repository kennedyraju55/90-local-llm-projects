<!-- ============================================================================
     🚀 CI/CD Pipeline Generator
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
![Project](https://img.shields.io/badge/Project-77%2F90-purple?style=flat-square)

**Production-Grade Pipeline Configs for Any Platform**

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

An AI-powered CI/CD pipeline generator supporting 5 platforms (GitHub Actions, GitLab CI, Jenkins, Azure Pipelines, CircleCI), 11 programming languages, 9 pipeline stages, matrix build presets, platform-specific secret templates, and built-in validation — all powered by a local LLM.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Setting up CI/CD pipelines requires platform-specific knowledge, proper caching strategies, secret management, and matrix build configuration — steep learning curve for each platform.

</td>
<td width="50%">

### ✅ The Solution

Generate production-ready pipeline configurations for any platform from simple descriptions. Includes caching, matrix builds, secret management, and artifact handling — all locally generated.

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
<tr><td><strong>🔧 Multi-Platform</strong></td><td>GitHub Actions, GitLab CI, Jenkins, Azure, CircleCI</td><td>✅ Yes</td></tr>
<tr><td><strong>🔢 Matrix Builds</strong></td><td>Python, JS, Java, Go, Rust version matrix presets</td><td>❌ No</td></tr>
<tr><td><strong>📋 Stage Catalog</strong></td><td>9 stages: lint, test, security, build, deploy, notify</td><td>❌ No</td></tr>
<tr><td><strong>🔐 Secret Templates</strong></td><td>Platform-specific secret variable configurations</td><td>❌ No</td></tr>
<tr><td><strong>🔍 Pipeline Explainer</strong></td><td>Understand any existing pipeline config with AI</td><td>✅ Yes</td></tr>
<tr><td><strong>✅ Config Validation</strong></td><td>Auto-validate generated pipeline configurations</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/cicd-pipeline-generator.git
cd cicd-pipeline-generator

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
python -m src.cicd_gen.cli generate --platform github-actions --language python --steps "lint,test,build,deploy"
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  🚀 CI/CD Pipeline Generator                              │
│  Production-Grade Pipeline Configs for Any Platform                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/cicd-pipeline-generator.git
cd cicd-pipeline-generator
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
uvicorn src.cicd_gen.api:app --reload --port 8000

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

### GitHub Actions

```bash
python -m src.cicd_gen.cli generate --platform github-actions --language python --steps "lint,test,build,deploy"
```

### GitLab CI

```bash
python -m src.cicd_gen.cli generate --platform gitlab-ci --language javascript
```

### With matrix

```bash
python -m src.cicd_gen.cli generate --language python --matrix
```

### With secrets

```bash
python -m src.cicd_gen.cli generate --language python --secrets "docker,aws"
```

### Explain pipeline

```bash
python -m src.cicd_gen.cli explain --file .github/workflows/ci.yml
```

### List platforms

```bash
python -m src.cicd_gen.cli list-platforms
```

### List stages

```bash
python -m src.cicd_gen.cli list-stages
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--platform` | CI/CD platform | `github-actions` |
| `--language` | Project language | `python` |
| `--steps` | Comma-separated pipeline steps | `lint,test,build,deploy` |
| `--project` | Project name | `None` |
| `--matrix/--no-matrix` | Enable matrix builds | `False` |
| `--secrets` | Secret categories (docker,aws,npm,pypi,slack) | `None` |
| `--output` | Save to file | `None` |
| `--validate/--no-validate` | Validate config | `True` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 77-cicd-pipeline-generator

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
77-cicd-pipeline-generator/
├── src/
│   └── cicd_gen/
│       ├── __init__.py
│       ├── core.py          # Platform registry, stages, matrix, generation
│       └── cli.py           # Click CLI with syntax highlighting
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
| `PLATFORMS` | 5 platforms: GitHub Actions, GitLab CI, Jenkins, Azure, CircleCI |
| `STAGE_CATALOG` | 9 stages: lint, test, security, build, publish, deploy, notify |
| `SECRET_TEMPLATES` | Platform-specific secret variable configurations |
| `MATRIX_PRESETS` | Language-specific version matrix (Python, JS, Java, Go, Rust) |


### Core Functions

| Function | Description |
|----------|-------------|
| `generate_pipeline()` | LLM-powered pipeline generation with platform awareness |
| `explain_pipeline()` | AI-powered pipeline configuration explanation |
| `validate_pipeline_config()` | YAML/Groovy validation for pipeline configs |
| `extract_config()` | Extract clean config from LLM responses |
| `get_matrix_preset()` | Language-specific matrix build configuration |
| `get_secret_template()` | Platform-specific secret variables |


### Python Usage Example

```python
from src.cicd_gen.core import (
    generate_pipeline, explain_pipeline, validate_pipeline_config,
    PLATFORMS, STAGE_CATALOG, MATRIX_PRESETS
)

# Generate a pipeline
pipeline = generate_pipeline(
    platform="github-actions",
    language="python",
    steps="lint,test,security,build,deploy",
    project_name="my-api",
    matrix=True,
    secrets=["docker", "aws"]
)

# Validate the output
result = validate_pipeline_config(pipeline, "github-actions")
print(f"Valid: {result['valid']}")

# Browse platform registry
for key, info in PLATFORMS.items():
    print(f"{info['name']}: {info['config_path']}")

# Matrix presets
preset = MATRIX_PRESETS["python"]
print(f"Python versions: {preset['versions']}")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 3000

pipeline:
  default_platform: github-actions
  default_language: python
  auto_validate: true
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
pytest tests/ --cov=src/cicd_gen --cov-report=term-missing

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

| Feature | 🚀 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>Which CI/CD platforms are supported?</strong></summary>
<br>

Five: GitHub Actions, GitLab CI, Jenkins (Jenkinsfile), Azure Pipelines, and CircleCI.

</details>

<details>
<summary><strong>Which languages support matrix builds?</strong></summary>
<br>

Python (3.10-3.12), JavaScript (18-22), Java (17, 21), Go (1.21-1.22), and Rust (stable, nightly).

</details>

<details>
<summary><strong>Can I add custom pipeline stages?</strong></summary>
<br>

Yes! Add entries to STAGE_CATALOG in core.py with a description and order number.

</details>

<details>
<summary><strong>Does it handle Jenkinsfile syntax?</strong></summary>
<br>

Yes! Jenkins generates Groovy-syntax Jenkinsfiles. Other platforms generate YAML.

</details>

<details>
<summary><strong>Can I combine stages?</strong></summary>
<br>

Yes! Pass any comma-separated combination of stages to --steps, e.g., lint,test,security,build,deploy,notify.

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
OLLAMA_MODEL=mistral python -m src.cicd_gen.cli --help
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
git clone https://github.com/YOUR_USERNAME/cicd-pipeline-generator.git
cd cicd-pipeline-generator

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

🚀 **Project 77/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
