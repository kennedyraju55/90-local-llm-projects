<!-- ============================================================================
     📊 Log File Analyzer
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
![Project](https://img.shields.io/badge/Project-75%2F90-purple?style=flat-square)

**Pattern Detection, Error Clustering & Anomaly Analysis**

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

An AI-powered log analysis tool with 10 built-in pattern detectors (database errors, auth failures, HTTP errors, timeouts, memory issues, disk problems, connection errors, SSL/TLS issues, crashes, rate limiting), error clustering, configurable alert thresholds, and LLM-powered root cause analysis.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Production logs contain thousands of lines. Finding the needle in the haystack — the root cause — requires expertise and hours of manual analysis.

</td>
<td width="50%">

### ✅ The Solution

Automated pattern matching across 10 categories, intelligent error clustering, configurable alerting, and AI-powered root cause analysis — all without sending your logs to the cloud.

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
<tr><td><strong>🔍 Pattern Matching</strong></td><td>10 built-in patterns: DB, auth, HTTP, timeout, etc.</td><td>❌ No</td></tr>
<tr><td><strong>🗂️ Error Clustering</strong></td><td>Group similar errors by pattern similarity</td><td>❌ No</td></tr>
<tr><td><strong>📈 Log Statistics</strong></td><td>Level distribution, line counts & timestamps</td><td>❌ No</td></tr>
<tr><td><strong>🚨 Alert Engine</strong></td><td>Configurable thresholds for auto-alerting</td><td>❌ No</td></tr>
<tr><td><strong>⏱️ Time Analysis</strong></td><td>Timestamp extraction and temporal patterns</td><td>✅ Yes</td></tr>
<tr><td><strong>🤖 AI Root Cause</strong></td><td>LLM-powered analysis for root cause detection</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/log-file-analyzer.git
cd log-file-analyzer

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
python -m src.log_analyzer.cli --file logs/app.log --focus all
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  📊 Log File Analyzer                              │
│  Pattern Detection, Error Clustering & Anomaly Analysis                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```

---

## 📖 CLI Reference

### Full analysis

```bash
python -m src.log_analyzer.cli --file logs/app.log --focus all
```

### Errors only

```bash
python -m src.log_analyzer.cli --file logs/app.log --focus errors
```

### Security focus

```bash
python -m src.log_analyzer.cli --file logs/app.log --focus security
```

### Pattern matching

```bash
python -m src.log_analyzer.cli --file logs/app.log --patterns
```

### Error clusters

```bash
python -m src.log_analyzer.cli --file logs/app.log --clusters
```

### Log statistics

```bash
python -m src.log_analyzer.cli --file logs/app.log --stats
```

### Alert check

```bash
python -m src.log_analyzer.cli --file logs/app.log --alerts
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--file` | Path to log file (required) | `None` |
| `--focus` | Focus: errors/warnings/security/performance/all | `all` |
| `--patterns` | Run pattern matching (no LLM) | `False` |
| `--clusters` | Cluster similar errors (no LLM) | `False` |
| `--stats` | Show log statistics (no LLM) | `False` |
| `--alerts` | Check alert thresholds (no LLM) | `False` |
| `--output` | Save results to file | `None` |
| `--verbose` | Enable debug logging | `False` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 75-log-file-analyzer

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
75-log-file-analyzer/
├── src/
│   └── log_analyzer/
│       ├── __init__.py
│       ├── core.py          # Pattern matching, clustering, alerts
│       ├── cli.py           # Click CLI with Rich tables
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
| `LogLevel` | Enum: CRITICAL, ERROR, WARNING, INFO, DEBUG |
| `PatternMatch` | Matched pattern with category, severity, line number |
| `ErrorCluster` | Cluster of similar errors with count and frequency |
| `LogStats` | Level distribution, line counts, timestamps |
| `AlertResult` | Triggered alert rule with threshold and count |


### Core Functions

| Function | Description |
|----------|-------------|
| `analyze_logs()` | LLM-powered comprehensive log analysis |
| `match_patterns()` | 10 built-in pattern matchers |
| `cluster_errors()` | Group similar errors by pattern |
| `calculate_stats()` | Log level distribution and metrics |
| `generate_alerts()` | Threshold-based alert generation |
| `parse_timestamps()` | Multi-format timestamp extraction |


### Python Usage Example

```python
from src.log_analyzer.core import (
    match_patterns, cluster_errors,
    calculate_stats, generate_alerts
)

# Pattern matching
matches = match_patterns(log_content)
for m in matches:
    print(f"[{m.severity.value}] {m.category}: {m.description}")
    print(f"  Line {m.line_number}: {m.line_text[:80]}")

# Cluster errors
clusters = cluster_errors(log_content)
for c in clusters:
    print(f"Cluster #{c.cluster_id}: {c.count}x {c.severity.value}")
    print(f"  Pattern: {c.pattern}")

# Statistics
stats = calculate_stats(log_content)
print(f"Total lines: {stats.total_lines}")
print(f"Error rate: {stats.error_rate:.1f}%")

# Alert check
alerts = generate_alerts(log_content)
for alert in alerts:
    print(f"🚨 {alert.rule}: {alert.message}")
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
  focus: all
  alert_thresholds:
    critical: 1
    error_rate: 10
    auth_failures: 5
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
pytest tests/ --cov=src/log_analyzer --cov-report=term-missing

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

| Feature | 📊 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>What log formats are supported?</strong></summary>
<br>

Any text-based log format. The pattern engine uses regex for common patterns, and the LLM can analyze any format.

</details>

<details>
<summary><strong>How does error clustering work?</strong></summary>
<br>

Errors are grouped by matching regex patterns and similar keywords, then ranked by frequency and severity.

</details>

<details>
<summary><strong>Can I add custom patterns?</strong></summary>
<br>

Yes! Add entries to PATTERN_LIBRARY in core.py with a regex pattern, severity, category, and description.

</details>

<details>
<summary><strong>What are the default alert thresholds?</strong></summary>
<br>

Critical: 1 occurrence, Error rate: >10, Auth failures: >5, Timeouts: >3. All configurable.

</details>

<details>
<summary><strong>Can I analyze compressed logs?</strong></summary>
<br>

Not directly. Decompress first with gunzip/unzip, then pass the text file to the analyzer.

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
OLLAMA_MODEL=mistral python -m src.log_analyzer.cli --help
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
git clone https://github.com/YOUR_USERNAME/log-file-analyzer.git
cd log-file-analyzer

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

📊 **Project 75/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
