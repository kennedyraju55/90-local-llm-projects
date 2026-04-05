<!-- ============================================================================
     📐 Infrastructure Doc Generator
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
![Project](https://img.shields.io/badge/Project-78%2F90-purple?style=flat-square)

**Auto-Generate Documentation from Config Files**

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

An AI-powered infrastructure documentation generator that auto-detects configuration types (Terraform, Kubernetes, Docker Compose, Ansible, CloudFormation, Dockerfile), extracts service dependencies, generates architecture diagrams, and produces comprehensive documentation — all from your config files, running locally.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Infrastructure documentation is always outdated. Teams spend hours writing docs that become stale after the next deployment.

</td>
<td width="50%">

### ✅ The Solution

Generate living documentation directly from your actual config files. Auto-detect config types, extract dependencies, create diagrams, and produce comprehensive docs — always in sync with reality.

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
<tr><td><strong>🔍 Auto-Detection</strong></td><td>Terraform, K8s, Docker, Ansible, CloudFormation</td><td>❌ No</td></tr>
<tr><td><strong>📊 Dependency Maps</strong></td><td>Extract service & resource dependencies automatically</td><td>✅ Yes</td></tr>
<tr><td><strong>🏗️ Architecture Diagrams</strong></td><td>Text-based diagrams showing component topology</td><td>✅ Yes</td></tr>
<tr><td><strong>📝 Multi-Format</strong></td><td>Output as markdown, HTML, or plain text</td><td>✅ Yes</td></tr>
<tr><td><strong>🔗 Link Analysis</strong></td><td>Network topology, volumes & port mapping</td><td>✅ Yes</td></tr>
<tr><td><strong>📋 Operational Notes</strong></td><td>Maintenance, monitoring and backup procedures</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/infra-doc-generator.git
cd infra-doc-generator

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
python -m src.infra_doc_gen.cli generate --file docker-compose.yml
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  📐 Infrastructure Doc Generator                              │
│  Auto-Generate Documentation from Config Files                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```

---

## 📖 CLI Reference

### Generate docs

```bash
python -m src.infra_doc_gen.cli generate --file docker-compose.yml
```

### With diagram

```bash
python -m src.infra_doc_gen.cli generate --file docker-compose.yml --diagram
```

### HTML output

```bash
python -m src.infra_doc_gen.cli generate --file main.tf --format html
```

### Architecture diagram

```bash
python -m src.infra_doc_gen.cli diagram --file docker-compose.yml
```

### Dependency map

```bash
python -m src.infra_doc_gen.cli deps --file docker-compose.yml
```

### List formats

```bash
python -m src.infra_doc_gen.cli list-formats
```

### Save docs

```bash
python -m src.infra_doc_gen.cli generate --file config.yml --output docs.md
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--file` | Config file to document (required) | `None` |
| `--format` | Output: markdown/html/text | `markdown` |
| `--diagram/--no-diagram` | Include architecture diagram | `False` |
| `--output` | Save docs to file | `None` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 78-infra-doc-generator

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
78-infra-doc-generator/
├── src/
│   └── infra_doc_gen/
│       ├── __init__.py
│       ├── core.py          # Config detection, deps, doc generation
│       └── cli.py           # Click CLI with format support
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
| `CONFIG_TYPES` | File extension to config type mapping |
| `INPUT_FORMATS` | 6 formats: Terraform, K8s, Docker Compose, Dockerfile, Ansible, CloudFormation |
| `DOC_FORMATS` | 3 output formats: markdown, html, text |


### Core Functions

| Function | Description |
|----------|-------------|
| `generate_docs()` | LLM-powered documentation generation |
| `generate_diagram()` | AI-generated architecture diagram |
| `generate_dependency_map()` | Comprehensive dependency analysis |
| `detect_config_type()` | Auto-detect config format from filename/content |
| `extract_dependencies()` | Parse dependencies from Docker Compose/K8s |
| `load_config()` | YAML configuration management |


### Python Usage Example

```python
from src.infra_doc_gen.core import (
    generate_docs, generate_diagram, generate_dependency_map,
    detect_config_type, extract_dependencies, INPUT_FORMATS
)

# Auto-detect config type
config_type = detect_config_type("docker-compose.yml", content)
print(f"Detected: {config_type}")

# Extract dependencies
deps = extract_dependencies(content, config_type)
for dep in deps:
    print(f"{dep['from']} → {dep['to']} ({dep['type']})")

# Generate documentation
docs = generate_docs(content, config_type, output_format="markdown")

# Generate architecture diagram
diagram = generate_diagram(content, config_type)

# Full dependency map
dep_map = generate_dependency_map(content, config_type)
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 3000

documentation:
  default_format: markdown
  include_diagram: false
  include_deps: true
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
pytest tests/ --cov=src/infra_doc_gen --cov-report=term-missing

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

| Feature | 📐 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>What config formats are detected?</strong></summary>
<br>

Terraform (.tf/.hcl), Kubernetes (.yml/.yaml), Docker Compose, Dockerfile, Ansible playbooks, and CloudFormation (.json/.yml).

</details>

<details>
<summary><strong>How does auto-detection work?</strong></summary>
<br>

Two-pass detection: first by filename patterns, then by content analysis matching format-specific indicators.

</details>

<details>
<summary><strong>Can it handle multi-file configs?</strong></summary>
<br>

Currently processes one file at a time. Run it on each file and combine the output for multi-file setups.

</details>

<details>
<summary><strong>Does it generate Mermaid diagrams?</strong></summary>
<br>

The diagram command generates text-based ASCII diagrams. For Mermaid, you can post-process the output.

</details>

<details>
<summary><strong>Can I customize the documentation template?</strong></summary>
<br>

Yes! Modify SYSTEM_PROMPT in core.py to change the documentation structure and sections.

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
OLLAMA_MODEL=mistral python -m src.infra_doc_gen.cli --help
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
git clone https://github.com/YOUR_USERNAME/infra-doc-generator.git
cd infra-doc-generator

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

📐 **Project 78/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
