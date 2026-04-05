<!-- ============================================================================
     🛡️ Cybersecurity Alert Summarizer
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
![Project](https://img.shields.io/badge/Project-71%2F90-purple?style=flat-square)

**AI-Powered Threat Analysis & Triage**

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

An AI-powered cybersecurity tool that analyzes security alerts, extracts Indicators of Compromise (IOCs), looks up CVE databases, calculates threat scores, correlates multiple alerts, and generates comprehensive threat summaries — all powered by a local LLM running through Ollama.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Security teams are overwhelmed with thousands of alerts daily. Manual triage is slow, error-prone, and leads to alert fatigue.

</td>
<td width="50%">

### ✅ The Solution

Automate alert triage with local AI — extract IOCs, score threats, correlate alerts, and generate executive summaries in seconds, with zero data leaving your network.

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
<tr><td><strong>🔍 IOC Extraction</strong></td><td>Auto-detect IPs, domains, hashes, URLs, file paths</td><td>❌ No</td></tr>
<tr><td><strong>📊 Threat Scoring</strong></td><td>Weighted scoring with CVE, IOC density & keyword analysis</td><td>✅ Yes</td></tr>
<tr><td><strong>🗂️ CVE Lookup</strong></td><td>Local CVE database with CVSS scores & vectors</td><td>✅ Yes</td></tr>
<tr><td><strong>⚡ Alert Prioritization</strong></td><td>LLM-powered ranking by risk level</td><td>❌ No</td></tr>
<tr><td><strong>🔗 Alert Correlation</strong></td><td>Cross-alert IOC and CVE correlation engine</td><td>❌ No</td></tr>
<tr><td><strong>📋 Rich Reports</strong></td><td>Beautiful CLI output with Rich tables & panels</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/cybersecurity-alert-summarizer.git
cd cybersecurity-alert-summarizer

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
python -m src.cyber_alert.cli --alert alerts/sample.txt
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  🛡️ Cybersecurity Alert Summarizer                              │
│  AI-Powered Threat Analysis & Triage                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/cybersecurity-alert-summarizer.git
cd cybersecurity-alert-summarizer
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
uvicorn src.cyber_alert.api:app --reload --port 8000

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

### Summarize alert

```bash
python -m src.cyber_alert.cli --alert alerts/sample.txt
```

### Filter by severity

```bash
python -m src.cyber_alert.cli --alert alerts/sample.txt --severity critical
```

### Prioritize alerts

```bash
python -m src.cyber_alert.cli --alert alerts/multi.txt --prioritize
```

### Extract IOCs

```bash
python -m src.cyber_alert.cli --alert alerts/sample.txt --iocs
```

### Lookup CVEs

```bash
python -m src.cyber_alert.cli --alert alerts/sample.txt --cves
```

### Threat scoring

```bash
python -m src.cyber_alert.cli --alert alerts/sample.txt --score
```

### Inline text

```bash
python -m src.cyber_alert.cli --text "CVE-2024-3094 XZ backdoor detected"
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--alert` | Path to alert text file | `None` |
| `--severity` | Filter: all/critical/high/medium/low | `all` |
| `--prioritize` | Prioritize multiple alerts | `False` |
| `--text` | Inline alert text | `None` |
| `--iocs` | Extract IOCs (no LLM) | `False` |
| `--cves` | Look up CVEs (no LLM) | `False` |
| `--score` | Calculate threat score (no LLM) | `False` |
| `--verbose` | Enable debug logging | `False` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 71-cybersecurity-alert-summarizer

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
71-cybersecurity-alert-summarizer/
├── src/
│   └── cyber_alert/
│       ├── __init__.py
│       ├── core.py          # IOC extraction, CVE lookup, threat scoring
│       ├── cli.py           # Click CLI with Rich output
│       └── config.py        # YAML configuration loader
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
| `Severity` | Enum: CRITICAL, HIGH, MEDIUM, LOW, INFO |
| `IOCResult` | Extracted IOC with type, value, context |
| `CVEInfo` | CVE lookup result with CVSS, severity, vector |
| `ThreatScore` | Composite threat scoring with factors |
| `AlertCorrelation` | Cross-alert correlation result |


### Core Functions

| Function | Description |
|----------|-------------|
| `summarize_alert()` | LLM-powered alert summarization with severity filtering |
| `prioritize_alerts()` | Risk-based prioritization of multiple alerts |
| `extract_iocs()` | Regex-based IOC extraction (9 types) |
| `extract_cves()` | CVE ID extraction and database lookup |
| `calculate_threat_score()` | Weighted threat scoring algorithm |
| `correlate_alerts()` | Cross-alert IOC and CVE correlation |


### Python Usage Example

```python
from src.cyber_alert.core import (
    summarize_alert, extract_iocs, extract_cves,
    calculate_threat_score, correlate_alerts
)

# Extract IOCs from alert text
iocs = extract_iocs(alert_text)
for ioc in iocs:
    print(f"[{ioc.ioc_type}] {ioc.value}")

# Look up CVEs
cves = extract_cves(alert_text)
for cve in cves:
    print(f"{cve.cve_id}: CVSS {cve.cvss} ({cve.severity})")

# Calculate threat score
score = calculate_threat_score(alert_text)
print(f"Score: {score.overall_score}/10 ({score.label})")
print(f"Confidence: {score.confidence * 100:.0f}%")

# Correlate multiple alerts
correlations = correlate_alerts([alert1, alert2, alert3])
for corr in correlations:
    print(f"Alerts {corr.alert_ids}: {corr.description}")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 2048

analysis:
  severity_filter: all
  enable_ioc_extraction: true
  enable_cve_lookup: true
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
pytest tests/ --cov=src/cyber_alert --cov-report=term-missing

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

| Feature | 🛡️ This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>Does this send my alerts to the cloud?</strong></summary>
<br>

No. Everything runs 100% locally through Ollama. Your sensitive security data never leaves your machine.

</details>

<details>
<summary><strong>Which LLM models work best?</strong></summary>
<br>

We recommend llama3.2 for a good balance of speed and quality. For maximum accuracy on complex alerts, try llama3.1:70b.

</details>

<details>
<summary><strong>Can I add custom CVEs to the database?</strong></summary>
<br>

Yes! Edit the CVE_DATABASE dictionary in core.py to add your organization's tracked CVEs.

</details>

<details>
<summary><strong>How accurate is the threat scoring?</strong></summary>
<br>

The scoring uses a weighted algorithm combining CVE severity (40%), IOC density (20%), and keyword analysis (40%). It's designed for triage, not definitive assessment.

</details>

<details>
<summary><strong>Can I process alerts in batch?</strong></summary>
<br>

Yes, use the --prioritize flag with a file containing multiple alerts. The correlate_alerts() API also accepts lists of alerts.

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
OLLAMA_MODEL=mistral python -m src.cyber_alert.cli --help
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
git clone https://github.com/YOUR_USERNAME/cybersecurity-alert-summarizer.git
cd cybersecurity-alert-summarizer

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

🛡️ **Project 71/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
