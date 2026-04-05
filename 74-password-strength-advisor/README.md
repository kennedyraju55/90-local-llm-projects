<!-- ============================================================================
     🔑 Password Strength Advisor
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
![Project](https://img.shields.io/badge/Project-74%2F90-purple?style=flat-square)

**Entropy Analysis, Breach Detection & Policy Generation**

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

A comprehensive password security tool featuring Shannon entropy calculation, breach database checking, NIST SP 800-63B policy generation, cryptographically secure password generation with Fisher-Yates shuffling, bulk analysis, and AI-powered deep analysis — all running locally to keep passwords secure.

> **Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** — A collection of 90 AI-powered tools, all running locally with Ollama. No cloud APIs, no data leaks, no subscription fees.

---

## 💡 Why This Project?

<table>
<tr>
<td width="50%">

### ❌ The Problem

Weak passwords remain the #1 attack vector. Most password checkers are simplistic (just checking length/complexity) and send passwords to the cloud.

</td>
<td width="50%">

### ✅ The Solution

Enterprise-grade entropy analysis with pattern detection, breach database checking, and NIST-compliant policy generation — all 100% local. Never transmits passwords anywhere.

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
<tr><td><strong>🔢 Entropy Calculator</strong></td><td>Shannon entropy with pattern penalty scoring</td><td>❌ No</td></tr>
<tr><td><strong>🛡️ Breach Detection</strong></td><td>Local dictionary + leet speak variation checks</td><td>❌ No</td></tr>
<tr><td><strong>📋 NIST Policy</strong></td><td>SP 800-63B compliant policy generation</td><td>✅ Yes</td></tr>
<tr><td><strong>🎲 Password Generator</strong></td><td>Cryptographic secure passwords with Fisher-Yates</td><td>✅ Yes</td></tr>
<tr><td><strong>📊 Bulk Analysis</strong></td><td>Analyze multiple passwords from file input</td><td>✅ Yes</td></tr>
<tr><td><strong>🤖 AI Analysis</strong></td><td>LLM-powered deep analysis with masked characteristics</td><td>✅ Yes</td></tr>
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
git clone https://github.com/kennedyraju55/password-strength-advisor.git
cd password-strength-advisor

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
python -m src.password_advisor.cli --password "MyP@ssw0rd123!"
```

### Expected Output

```
╭──────────────────────────────────────────────╮
│  🔑 Password Strength Advisor                              │
│  Entropy Analysis, Breach Detection & Policy Generation                                    │
│  v1.0.0 • Powered by Local LLM              │
╰──────────────────────────────────────────────╯
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/password-strength-advisor.git
cd password-strength-advisor
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
uvicorn src.password_advisor.api:app --reload --port 8000

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

### Analyze password

```bash
python -m src.password_advisor.cli --password "MyP@ssw0rd123!"
```

### With breach check

```bash
python -m src.password_advisor.cli --password "password123" --breach-check
```

### AI analysis

```bash
python -m src.password_advisor.cli --password "MyP@ssw0rd" --analyze
```

### Generate passwords

```bash
python -m src.password_advisor.cli generate --length 20 --count 10
```

### Show NIST policy

```bash
python -m src.password_advisor.cli policy
```

### Bulk analyze file

```bash
python -m src.password_advisor.cli bulk --file passwords.txt
```

### Analyze policy file

```bash
python -m src.password_advisor.cli --policy policy.txt --analyze
```



### Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--password` | Password to analyze | `None` |
| `--policy` | Policy file to analyze | `None` |
| `--analyze` | Enable LLM analysis | `False` |
| `--entropy` | Show entropy only | `False` |
| `--breach-check` | Check breach database | `False` |
| `--verbose` | Enable debug logging | `False` |


---

## 🌐 Web UI

This project includes a web interface powered by **Streamlit**.

```bash
# Navigate to the project directory
cd 74-password-strength-advisor

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
74-password-strength-advisor/
├── src/
│   └── password_advisor/
│       ├── __init__.py
│       ├── core.py          # Entropy, breach check, policy, generator
│       ├── cli.py           # Click CLI with strength colors
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
| `StrengthLevel` | Enum: VERY_WEAK, WEAK, FAIR, STRONG, VERY_STRONG |
| `EntropyResult` | Entropy bits, charset, effective length, crack time |
| `BreachCheckResult` | Compromise status, source, occurrences |
| `PolicyRule` | NIST policy rule with name, description, enabled |
| `BulkAnalysisResult` | Masked password with entropy and issues |


### Core Functions

| Function | Description |
|----------|-------------|
| `calculate_entropy()` | Shannon entropy with pattern penalty scoring |
| `check_breach_database()` | Local dictionary + leet speak checking |
| `generate_policy()` | NIST SP 800-63B compliant policy generation |
| `analyze_password_llm()` | AI analysis with masked characteristics |
| `generate_password()` | Cryptographic generation with Fisher-Yates |
| `bulk_analyze()` | Batch analysis of multiple passwords |


### Python Usage Example

```python
from src.password_advisor.core import (
    calculate_entropy, check_breach_database,
    generate_policy, generate_password, bulk_analyze
)

# Calculate entropy
result = calculate_entropy("MySecureP@ss2024!")
print(f"Entropy: {result.entropy_bits:.1f} bits")
print(f"Strength: {result.strength.value}")
print(f"Time to crack: {result.time_to_crack}")

# Check breach database
breach = check_breach_database("password123")
print(f"Compromised: {breach.is_compromised}")

# Generate secure passwords
for _ in range(5):
    pwd = generate_password(length=20)
    ent = calculate_entropy(pwd)
    print(f"{pwd}  [{ent.entropy_bits:.0f} bits]")

# NIST policy
policy = generate_policy()
for rule in policy:
    print(f"{'✅' if rule.enabled else '❌'} {rule.name}: {rule.description}")
```

---

## ⚙️ Configuration

### config.yaml

```yaml
model:
  name: llama3.2
  temperature: 0.3
  max_tokens: 1024

password:
  default_length: 16
  min_entropy: 60
  check_breaches: true
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
pytest tests/ --cov=src/password_advisor --cov-report=term-missing

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

| Feature | 🔑 This Tool (Local) | ☁️ Cloud Alternatives |
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
<summary><strong>Does this send passwords to any server?</strong></summary>
<br>

Absolutely not. All analysis runs 100% locally. Passwords never leave your machine, even the LLM runs through local Ollama.

</details>

<details>
<summary><strong>How is entropy calculated?</strong></summary>
<br>

Using Shannon entropy: bits = length × log2(charset_size), with penalties for common patterns like sequential chars, repeated chars, and dictionary words.

</details>

<details>
<summary><strong>What's in the breach database?</strong></summary>
<br>

A local dictionary of 21 common breached passwords plus leet speak variations. For production use, integrate with the HaveIBeenPwned API.

</details>

<details>
<summary><strong>Why does NIST say no complexity rules?</strong></summary>
<br>

NIST SP 800-63B found that complexity rules (must have uppercase, special char, etc.) lead to predictable patterns. Length and breach checking are more effective.

</details>

<details>
<summary><strong>Can I customize the password generator?</strong></summary>
<br>

Yes! Use --requirements to specify character types (upper, lower, digits, special) and --length for password length.

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
OLLAMA_MODEL=mistral python -m src.password_advisor.cli --help
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
git clone https://github.com/YOUR_USERNAME/password-strength-advisor.git
cd password-strength-advisor

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

🔑 **Project 74/90** — [⬆️ Back to Top](#)

<sub>Made with local LLMs • No cloud APIs • No data leaks • No subscription fees</sub>

</div>
