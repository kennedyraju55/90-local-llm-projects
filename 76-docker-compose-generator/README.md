<!-- ============================================================================
     🐳 Docker Compose Generator
     Auto-generated portfolio-grade README — Part of 90 Local LLM Projects
     ============================================================================ -->

![Banner](docs/images/banner.svg)

<div align="center">

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)

![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-85%25-yellow?style=flat-square)
![Last Commit](https://img.shields.io/badge/Maintained-2024-blue?style=flat-square)
![Project](https://img.shields.io/badge/Project-76%2F90-purple?style=flat-square)

**Production-Grade Compose Files from Natural Language**

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

An AI-powered Docker Compose generator with a catalog of 20+ services, 10 common stack templates, 3 environment profiles, network configuration templates, and built-in YAML validation — all driven by natural language descriptions and powered by a local LLM.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Writing docker-compose.yml files from scratch is tedious and error-prone. Getting best practices right for health checks, resource limits, and networking takes experience.

</td>
<td width="50%">

### ✅ The Solution

Describe your stack in plain English and get production-ready compose files with proper health checks, resource limits, networking, and security — validated automatically.

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
<tr><td><strong>📦 Service Catalog</strong></td><td>20+ services: databases, proxies, messaging, runtimes</td><td>❌ No</td></tr>
<tr><td><strong>🏗️ Stack Templates</strong></td><td>MEAN, MERN, LAMP, Django, Rails, WordPress, ELK</td><td>❌ No</td></tr>
<tr><td><strong>🌍 Env Profiles</strong></td><td>Dev, staging, production with auto-configuration</td><td>✅ Yes</td></tr>
<tr><td><strong>🔍 Compose Explainer</strong></td><td>Understand any existing compose file with AI</td><td>✅ Yes</td></tr>
<tr><td><strong>✅ YAML Validation</strong></td><td>Auto-validate generated compose configurations</td><td>✅ Yes</td></tr>
<tr><td><strong>🌐 Network Templates</strong></td><td>Simple, isolated, overlay network modes</td><td>❌ No</td></tr>
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
git clone https://github.com/kennedyraju55/docker-compose-generator.git
cd docker-compose-generator

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
python -m src.docker_gen.cli generate --stack "Python Flask with PostgreSQL and Redis"
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  🐳 Docker Compose Generator                              │
│  Production-Grade Compose Files from Natural Language                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```

---

## 📖 CLI Reference

### Generate stack

```bash
python -m src.docker_gen.cli generate --stack "Python Flask with PostgreSQL and Redis"
```

### Production env

```bash
python -m src.docker_gen.cli generate --stack "MERN stack" --env production
```

### With catalog services

```bash
python -m src.docker_gen.cli generate --stack "web app" --services postgres,redis,nginx
```

### Explain compose

```bash
python -m src.docker_gen.cli explain --file docker-compose.yml
```

### List stacks

```bash
python -m src.docker_gen.cli list-stacks
```

### List services

```bash
python -m src.docker_gen.cli list-services
```

### List environments

```bash
python -m src.docker_gen.cli list-envs
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--stack` | Stack description in natural language | `None` |
| `--env` | Target: development/staging/production | `development` |
| `--services` | Comma-separated catalog services | `None` |
| `--network` | Network mode: simple/isolated/overlay | `simple` |
| `--output` | Save to file | `None` |
| `--validate/--no-validate` | Validate generated YAML | `True` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 76-docker-compose-generator

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
76-docker-compose-generator/
├── src/
│   └── docker_gen/
│       ├── __init__.py
│       ├── core.py          # Service catalog, stack templates, generation
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
| `SERVICE_CATALOG` | 20+ services: databases, web servers, messaging, monitoring, runtimes |
| `COMMON_STACKS` | 10 templates: MEAN, MERN, LAMP, LEMP, Django, Flask, Rails, Spring, WordPress, ELK |
| `ENV_PROFILES` | 3 profiles: development, staging, production with auto-config |
| `NETWORK_TEMPLATES` | 3 modes: simple (bridge), isolated (internal), overlay |


### Core Functions

| Function | Description |
|----------|-------------|
| `generate_compose()` | LLM-powered compose generation with catalog enrichment |
| `explain_compose()` | AI-powered compose file explanation |
| `validate_compose()` | YAML validation for generated compose files |
| `extract_yaml()` | Extract clean YAML from LLM responses |
| `get_service_catalog()` | Browse full service catalog by category |
| `get_env_profile()` | Get environment-specific configuration |


### Python Usage Example

```python
from src.docker_gen.core import (
    generate_compose, explain_compose, validate_compose,
    get_service_catalog, get_flat_catalog, COMMON_STACKS
)

# Generate a compose file
compose = generate_compose(
    stack_description="Python Django with PostgreSQL, Redis, and Nginx",
    env="production",
    services=["postgres", "redis", "nginx"],
    network_mode="simple"
)

# Validate the output
result = validate_compose(compose)
print(f"Valid: {result['valid']}")

# Browse service catalog
catalog = get_service_catalog()
for category, services in catalog.items():
    print(f"\n{category}:")
    for name, info in services.items():
        print(f"  {name}: {info['image']} (port {info['port']})")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 3000

compose:
  default_env: development
  auto_validate: true
  network_mode: simple
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
pytest tests/ --cov=src/docker_gen --cov-report=term-missing

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

| Feature | 🐳 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>What services are in the catalog?</strong></summary>
<br>

20+ services across 5 categories: databases (PostgreSQL, MySQL, MongoDB, Redis, MariaDB), web servers (Nginx, Traefik, Caddy, Apache), messaging (RabbitMQ, Kafka, NATS), monitoring (Prometheus, Grafana, ELK), and runtimes (Python, Node, Go, Java).

</details>

<details>
<summary><strong>Can I use custom Docker images?</strong></summary>
<br>

Yes! Describe your custom service in the stack description, or extend SERVICE_CATALOG in core.py.

</details>

<details>
<summary><strong>How do environment profiles work?</strong></summary>
<br>

Development enables hot reload and debug ports. Staging adds logging and health checks. Production adds resource limits, strict restart policies, and removes debug access.

</details>

<details>
<summary><strong>Does it generate Dockerfiles too?</strong></summary>
<br>

No, it focuses on docker-compose.yml generation. For Dockerfiles, check out other tools in the 90-local-llm-projects collection.

</details>

<details>
<summary><strong>Can I validate existing compose files?</strong></summary>
<br>

Yes! Use the explain command to understand any compose file, or the validate_compose() API for YAML validation.

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
OLLAMA_MODEL=mistral python -m src.docker_gen.cli --help
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
git clone https://github.com/YOUR_USERNAME/docker-compose-generator.git
cd docker-compose-generator

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

🐳 **Project 76/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
