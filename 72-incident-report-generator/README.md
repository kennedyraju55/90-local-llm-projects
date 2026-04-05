<!-- ============================================================================
     📋 Incident Report Generator
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
![Project](https://img.shields.io/badge/Project-72%2F90-purple?style=flat-square)

**Professional Incident Documentation & Analysis**

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

An AI-powered tool that transforms raw security logs into professional, management-ready incident reports. Features priority-based templates (P1-P4), automated timeline extraction, impact assessment scoring, and structured lessons-learned generation — all powered by a local LLM.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Writing incident reports is time-consuming and inconsistent. Teams struggle with proper formatting, miss critical details, and delay post-mortems.

</td>
<td width="50%">

### ✅ The Solution

Generate professional incident reports in seconds from raw logs. Consistent templates, automated timelines, quantified impact, and structured lessons learned — all without exposing sensitive incident data to cloud services.

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
<tr><td><strong>📝 Report Generation</strong></td><td>Priority-based templates P1-P4 with SLA tracking</td><td>✅ Yes</td></tr>
<tr><td><strong>⏱️ Timeline Builder</strong></td><td>Auto-extract chronological events from raw logs</td><td>❌ No</td></tr>
<tr><td><strong>💥 Impact Assessment</strong></td><td>Severity scoring with revenue & user impact</td><td>❌ No</td></tr>
<tr><td><strong>🎓 Lessons Learned</strong></td><td>Structured post-mortem with action items</td><td>✅ Yes</td></tr>
<tr><td><strong>🏷️ Incident Types</strong></td><td>Security, outage, data-breach, malware, phishing, general</td><td>✅ Yes</td></tr>
<tr><td><strong>📤 Export Reports</strong></td><td>Save to file with markdown formatting</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/incident-report-generator.git
cd incident-report-generator

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
python -m src.incident_reporter.cli --logs logs/incident.txt --type security
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  📋 Incident Report Generator                              │
│  Professional Incident Documentation & Analysis                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/incident-report-generator.git
cd incident-report-generator
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
uvicorn src.incident_reporter.api:app --reload --port 8000

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

### Generate report

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --type security
```

### P1 critical

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --type security --priority P1
```

### Timeline only

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --timeline-only
```

### Impact assessment

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --impact --affected-users 5000 --downtime 120
```

### Lessons learned

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --type data-breach --lessons
```

### Save to file

```bash
python -m src.incident_reporter.cli --logs logs/incident.txt --output report.md
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--logs` | Path to log file (required) | `None` |
| `--type` | Incident type: security/outage/data-breach/malware/phishing/general | `security` |
| `--title` | Custom report title | `None` |
| `--priority` | Priority level: P1/P2/P3/P4 | `P2` |
| `--timeline-only` | Only generate timeline | `False` |
| `--impact` | Calculate impact assessment | `False` |
| `--lessons` | Generate lessons learned | `False` |
| `--affected-users` | Number of affected users | `0` |
| `--downtime` | Downtime in minutes | `0` |
| `--output` | Save report to file | `None` |
| `--verbose` | Enable debug logging | `False` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 72-incident-report-generator

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
72-incident-report-generator/
├── src/
│   └── incident_reporter/
│       ├── __init__.py
│       ├── core.py          # Report generation, timeline, impact
│       ├── cli.py           # Click CLI with Rich panels
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
| `Priority` | Enum: P1, P2, P3, P4 with SLA templates |
| `TimelineEntry` | Structured event: timestamp, event, severity, actor |
| `ImpactAssessment` | Severity scoring with user/system/revenue impact |
| `LessonsLearned` | Category, observation, recommendation, owner |


### Core Functions

| Function | Description |
|----------|-------------|
| `generate_report()` | LLM-powered report generation with priority templates |
| `generate_timeline()` | LLM-based timeline extraction from logs |
| `build_timeline()` | Regex-based structured timeline parsing |
| `calculate_impact()` | Automated impact assessment scoring |
| `generate_lessons_learned()` | Post-mortem lessons with action items |
| `get_template()` | Priority-based template retrieval |


### Python Usage Example

```python
from src.incident_reporter.core import (
    generate_report, build_timeline, calculate_impact,
    generate_lessons_learned, Priority
)

# Generate a full incident report
report = generate_report(
    logs=log_data,
    incident_type="security",
    title="Database Breach - Production",
    priority=Priority.P1
)

# Build structured timeline
timeline = build_timeline(log_data)
for entry in timeline:
    print(f"[{entry.timestamp}] {entry.severity}: {entry.event}")

# Calculate impact
impact = calculate_impact(log_data, affected_users=5000, downtime_minutes=120)
print(f"Severity: {impact.severity_label} ({impact.severity_score}/10)")
print(f"Revenue Impact: {impact.revenue_impact}")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 3000

report:
  default_priority: P2
  default_type: security
  include_appendix: true
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
pytest tests/ --cov=src/incident_reporter --cov-report=term-missing

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

| Feature | 📋 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>What incident types are supported?</strong></summary>
<br>

Six types: security, outage, data-breach, malware, phishing, and general. Each type tailors the report structure.

</details>

<details>
<summary><strong>How does priority affect the report?</strong></summary>
<br>

Priority levels P1-P4 determine report sections, response time SLAs, update frequency, and escalation paths.

</details>

<details>
<summary><strong>Can I customize report templates?</strong></summary>
<br>

Yes! Modify PRIORITY_TEMPLATES in core.py to add custom sections, change SLAs, or adjust escalation paths.

</details>

<details>
<summary><strong>Does this parse any log format?</strong></summary>
<br>

The timeline builder handles standard syslog-style timestamps. The LLM can process any log format for summary generation.

</details>

<details>
<summary><strong>Can I integrate this with PagerDuty/Slack?</strong></summary>
<br>

Not directly, but you can pipe the --output file to any webhook integration or build a wrapper script.

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
OLLAMA_MODEL=mistral python -m src.incident_reporter.cli --help
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
git clone https://github.com/YOUR_USERNAME/incident-report-generator.git
cd incident-report-generator

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

📋 **Project 72/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
