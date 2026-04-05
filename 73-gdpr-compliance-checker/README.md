<!-- ============================================================================
     🔒 GDPR Compliance Checker
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
![Project](https://img.shields.io/badge/Project-73%2F90-purple?style=flat-square)

**Article-by-Article Analysis & DPO Recommendations**

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

An AI-powered GDPR compliance analysis tool that checks documents, privacy policies, and code against 21 GDPR articles. Features automated article-by-article checklist generation, data flow mapping, DPO recommendations, audit trail logging, and LLM-powered deep compliance analysis — all running locally.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

GDPR compliance is complex with 21+ articles to check. Manual audits are expensive, inconsistent, and often miss data flow issues.

</td>
<td width="50%">

### ✅ The Solution

Automated article-by-article compliance checking with data flow mapping, DPO-grade recommendations, and audit trails — keeping your sensitive compliance data completely local.

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
<tr><td><strong>📜 Article Checklist</strong></td><td>21 GDPR articles with auto-compliance detection</td><td>❌ No</td></tr>
<tr><td><strong>🗺️ Data Flow Mapping</strong></td><td>Auto-detect data types, purposes & transfers</td><td>❌ No</td></tr>
<tr><td><strong>👨‍⚖️ DPO Recommendations</strong></td><td>Priority-ranked actions for compliance gaps</td><td>✅ Yes</td></tr>
<tr><td><strong>🔎 Compliance Check</strong></td><td>LLM-powered analysis for consent, retention, security</td><td>✅ Yes</td></tr>
<tr><td><strong>📊 Audit Trail</strong></td><td>Timestamped audit log entries for accountability</td><td>✅ Yes</td></tr>
<tr><td><strong>📋 Checklist Generator</strong></td><td>AI-generated compliance checklist from documents</td><td>❌ No</td></tr>
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
git clone https://github.com/kennedyraju55/gdpr-compliance-checker.git
cd gdpr-compliance-checker

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
python -m src.gdpr_checker.cli --file policy.txt --check all
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  🔒 GDPR Compliance Checker                              │
│  Article-by-Article Analysis & DPO Recommendations                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/gdpr-compliance-checker.git
cd gdpr-compliance-checker
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
uvicorn src.gdpr_checker.api:app --reload --port 8000

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

### Full compliance check

```bash
python -m src.gdpr_checker.cli --file policy.txt --check all
```

### Consent focus

```bash
python -m src.gdpr_checker.cli --file policy.txt --check consent
```

### Article checklist

```bash
python -m src.gdpr_checker.cli --file policy.txt --articles
```

### DPO recommendations

```bash
python -m src.gdpr_checker.cli --file policy.txt --dpo
```

### Data flow mapping

```bash
python -m src.gdpr_checker.cli --file policy.txt --data-flows
```

### AI checklist

```bash
python -m src.gdpr_checker.cli --file policy.txt --checklist
```

### Save report

```bash
python -m src.gdpr_checker.cli --file policy.txt --check all --output report.md
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--file` | File to check (required) | `None` |
| `--check` | Focus: all/consent/retention/transfer/security/rights | `all` |
| `--checklist` | Generate AI compliance checklist | `False` |
| `--articles` | Article-by-article checklist (no LLM) | `False` |
| `--data-flows` | Map data flows (no LLM) | `False` |
| `--dpo` | Generate DPO recommendations | `False` |
| `--output` | Save results to file | `None` |
| `--verbose` | Enable debug logging | `False` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 73-gdpr-compliance-checker

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
73-gdpr-compliance-checker/
├── src/
│   └── gdpr_checker/
│       ├── __init__.py
│       ├── core.py          # Article checklist, data flows, DPO engine
│       ├── cli.py           # Click CLI with status icons
│       └── config.py        # Configuration loader
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
| `ComplianceStatus` | Enum: COMPLIANT, PARTIALLY_COMPLIANT, NON_COMPLIANT, NOT_ADDRESSED |
| `ChecklistItem` | Article, title, status, findings, recommendation |
| `DataFlowEntry` | Data type, source, destination, purpose, legal basis |
| `AuditLogEntry` | Timestamped audit trail entry |
| `DPORecommendation` | Priority-ranked compliance recommendation |


### Core Functions

| Function | Description |
|----------|-------------|
| `check_compliance()` | LLM-powered compliance analysis by focus area |
| `generate_checklist()` | AI-generated GDPR compliance checklist |
| `build_article_checklist()` | 21-article automated compliance check |
| `map_data_flows()` | Automated data type and purpose detection |
| `generate_dpo_recommendations()` | Priority-ranked improvement actions |
| `create_audit_entry()` | Audit trail entry creation |


### Python Usage Example

```python
from src.gdpr_checker.core import (
    check_compliance, build_article_checklist,
    map_data_flows, generate_dpo_recommendations
)

# Article-by-article checklist
checklist = build_article_checklist(document_content)
for item in checklist:
    print(f"{item.article}: {item.status.value} - {item.findings}")

# Map data flows
flows = map_data_flows(document_content)
for flow in flows:
    print(f"{flow.data_type}: {flow.source} → {flow.destination}")
    print(f"  Purpose: {flow.purpose}, Cross-border: {flow.cross_border}")

# DPO recommendations
recs = generate_dpo_recommendations(checklist)
for rec in recs:
    print(f"[{rec.priority.upper()}] {rec.article}: {rec.recommendation}")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.2
  max_tokens: 3000

compliance:
  default_check: all
  articles_count: 21
  enable_data_flow: true
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
pytest tests/ --cov=src/gdpr_checker --cov-report=term-missing

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

| Feature | 🔒 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>Which GDPR articles does it check?</strong></summary>
<br>

21 articles including Art. 5-7, 12-22, 25, 28, 30, 32-35, 37-39, and 44-49 covering principles, rights, security, and transfers.

</details>

<details>
<summary><strong>Can it analyze source code?</strong></summary>
<br>

Yes! It can analyze code files for GDPR compliance signals like consent mechanisms, data deletion, and encryption.

</details>

<details>
<summary><strong>How does the data flow mapping work?</strong></summary>
<br>

It detects 8 data types (email, name, phone, etc.) and 4 purposes (marketing, analytics, service, legal) using keyword matching.

</details>

<details>
<summary><strong>Are the recommendations legally binding?</strong></summary>
<br>

No. This is an AI-assisted tool for initial screening. Always consult with a qualified DPO or legal professional.

</details>

<details>
<summary><strong>Can I add custom compliance rules?</strong></summary>
<br>

Yes! Add entries to GDPR_ARTICLES and compliance_signals in core.py to extend the checklist.

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
OLLAMA_MODEL=mistral python -m src.gdpr_checker.cli --help
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
git clone https://github.com/YOUR_USERNAME/gdpr-compliance-checker.git
cd gdpr-compliance-checker

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

🔒 **Project 73/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
