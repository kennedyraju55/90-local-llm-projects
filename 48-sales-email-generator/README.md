<div align="center">

<img src="docs/images/banner.svg" alt="Sales Email Generator Banner" width="800"/>

<br/>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-e63946?style=for-the-badge&logo=llama&logoColor=white)](https://ollama.ai/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Click CLI](https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-f1c40f?style=for-the-badge)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

[![Tests](https://img.shields.io/github/actions/workflow/status/kennedyraju55/sales-email-generator/tests.yml?label=tests&style=flat-square)](https://github.com/kennedyraju55/sales-email-generator/actions)
[![GitHub stars](https://img.shields.io/github/stars/kennedyraju55/sales-email-generator?style=flat-square&color=e63946)](https://github.com/kennedyraju55/sales-email-generator/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/kennedyraju55/sales-email-generator?style=flat-square)](https://github.com/kennedyraju55/sales-email-generator/issues)
[![GitHub last commit](https://img.shields.io/github/last-commit/kennedyraju55/sales-email-generator?style=flat-square&color=e63946)](https://github.com/kennedyraju55/sales-email-generator/commits)

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection — Project #48**

[Features](#-features) · [Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [FAQ](#-faq)

</div>

---

## 🤔 Why Sales Email Generator?

| Challenge | Without This Tool | With Sales Email Generator |
|-----------|-------------------|----------------------------|
| **Personalization** | Generic copy-paste emails that prospects ignore | AI-powered personalization scored 0–100 with improvement suggestions |
| **Follow-Up Cadence** | Inconsistent timing, forgotten prospects | Automated multi-step sequences: intro → value-add → case-study → break-up |
| **A/B Testing** | One version, no optimization data | Generate multiple variants instantly for split testing |
| **Prospect Research** | Hours of manual LinkedIn/Google research | LLM-driven research profiles: pain points, talking points, industry context |
| **Tone Consistency** | Emails vary wildly across reps | Four calibrated tones: professional, casual, persuasive, consultative |
| **Privacy** | Sensitive prospect data sent to cloud APIs | 100% local — Ollama runs on your machine, zero data leaves your network |

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Feature | Description |
|---------|-------------|
| 📧 **Smart Email Generation** | Personalized emails tailored to prospect role, company, and industry using local LLMs |
| 🎨 **Multi-Tone Engine** | Four distinct tones — professional, casual, persuasive, consultative — each with calibrated guidelines |
| 🔄 **Follow-Up Sequences** | Multi-step drip campaigns with configurable delays: intro → value-add → case-study → break-up |
| 🧪 **A/B Test Variants** | Generate multiple email variants with different hooks/angles for split testing |
| 🔍 **Prospect Research** | AI-powered prospect profiling returning structured pain points, talking points, and industry context |
| 📊 **Personalization Scoring** | Score any email 0–100 on personalization quality with actionable improvement suggestions |
| 📋 **Template Library** | Five production-ready templates: cold outreach, follow-up, demo request, case study, break-up |
| 🖥️ **Streamlit Web UI** | Full-featured dashboard with tabs for generation, sequences, scoring, and template browsing |
| ⚡ **Click CLI** | Fast terminal interface with Rich formatting, progress spinners, and colored output |
| ⚙️ **YAML Configuration** | Config-driven setup for model, tones, sequence timing, scoring thresholds, and logging |
| 🔒 **100% Local** | Ollama-powered — no API keys, no cloud, your data never leaves your machine |
| 📝 **Structured Logging** | Timestamped, leveled logging across the full pipeline for debugging and auditing |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Python](https://www.python.org/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai/) | Latest | Local LLM inference |
| [Git](https://git-scm.com/) | Any | Clone the repository |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/sales-email-generator.git
cd sales-email-generator

# Install dependencies
pip install -r requirements.txt

# Or install as editable package (recommended)
pip install -e ".[dev]"
```

### 2. Start Ollama

```bash
# Pull the default model
ollama pull gemma3

# Verify it's running
ollama list
```

### 3. Generate Your First Email

```bash
sales-email generate \
  -p "CTO at a Series B fintech startup, 150 employees" \
  -pr "AI-powered code review platform" \
  -t professional
```

<details>
<summary>📨 <strong>Example Output</strong></summary>

```
╭─ ✉️  Generated Email ─────────────────────────────────────────────────╮
│                                                                       │
│  Subject: Accelerating Code Quality at Scale — A Quick Thought        │
│                                                                       │
│  ─────────────────────────────────────────────────────────────────     │
│                                                                       │
│  Hi [Name],                                                           │
│                                                                       │
│  As CTO of a rapidly scaling fintech company, you're likely           │
│  balancing speed of delivery with code quality — especially with      │
│  150+ engineers pushing code daily.                                   │
│                                                                       │
│  Our AI-powered code review platform has helped similar Series B      │
│  companies reduce critical bugs by 40% while cutting review cycles    │
│  from hours to minutes. It integrates directly into your existing     │
│  CI/CD pipeline — no workflow disruption.                             │
│                                                                       │
│  Would a 15-minute walkthrough be worth your time this week?          │
│                                                                       │
│  Best regards,                                                        │
│  [Your Name]                                                          │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
```

</details>

### 4. Try A/B Variants

```bash
sales-email variants \
  -p "VP Engineering at enterprise SaaS" \
  -pr "DevOps Automation Platform" \
  -t persuasive \
  -n 3
```

### 5. Build a Follow-Up Sequence

```bash
sales-email sequence \
  -p "Head of Sales at mid-market company" \
  -pr "CRM Analytics Suite" \
  -t consultative \
  -n 4
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/sales-email-generator.git
cd sales-email-generator
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
uvicorn src.sales_email_gen.api:app --reload --port 8000

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

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output.

### Command Overview

```
sales-email [OPTIONS] COMMAND [ARGS]...

Commands:
  generate   Generate a single sales email
  variants   Generate A/B test email variants
  sequence   Generate a multi-email follow-up sequence
  templates  List available email templates
  research   Research a prospect and generate a sales profile
```

### `generate` — Single Email

Generate a personalized sales email for a specific prospect.

```bash
sales-email generate [OPTIONS]
```

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--prospect` | `-p` | ✅ | — | Prospect description (role, company, context) |
| `--product` | `-pr` | ✅ | — | Product or service being offered |
| `--tone` | `-t` | ❌ | `professional` | Email tone: professional, casual, persuasive, consultative |
| `--context` | `-c` | ❌ | `""` | Additional context (e.g., "Met at conference") |
| `--follow-up` | — | ❌ | `False` | Generate a follow-up instead of initial outreach |

```bash
# Basic professional email
sales-email generate -p "CTO at startup" -pr "AI Platform" -t professional

# Follow-up with context
sales-email generate -p "VP Engineering at Acme" -pr "Dev Tools" -t casual \
  --follow-up -c "Met at KubeCon last week"

# Persuasive cold outreach
sales-email generate -p "CMO at D2C brand, 50 employees" -pr "Marketing Analytics" -t persuasive
```

### `variants` — A/B Testing

Generate multiple email variants with different angles for split testing.

```bash
sales-email variants [OPTIONS]
```

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--prospect` | `-p` | ✅ | — | Prospect description |
| `--product` | `-pr` | ✅ | — | Product or service |
| `--tone` | `-t` | ❌ | `professional` | Email tone |
| `--count` | `-n` | ❌ | `3` | Number of variants to generate |

```bash
# Generate 3 variants (default)
sales-email variants -p "CTO at fintech" -pr "API Gateway" -t professional

# Generate 5 variants for extensive testing
sales-email variants -p "VP Sales at SaaS" -pr "Sales Intelligence" -n 5
```

### `sequence` — Follow-Up Sequence

Build a complete multi-email drip campaign.

```bash
sales-email sequence [OPTIONS]
```

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--prospect` | `-p` | ✅ | — | Prospect description |
| `--product` | `-pr` | ✅ | — | Product or service |
| `--tone` | `-t` | ❌ | `professional` | Email tone |
| `--count` | `-n` | ❌ | `4` | Number of emails in sequence |

The sequence follows this proven cadence:

| Step | Type | Day | Purpose |
|------|------|-----|---------|
| 1 | **Intro** | 0 | Initial outreach with value proposition |
| 2 | **Value-Add** | 3 | Share relevant insight or resource |
| 3 | **Case Study** | 7 | Social proof with metrics and results |
| 4 | **Break-Up** | 14 | Final follow-up, leave door open |

```bash
# Default 4-email sequence
sales-email sequence -p "VP Sales at Corp" -pr "CRM Tool" -n 4

# Shorter 2-email sequence
sales-email sequence -p "CEO at startup" -pr "HR Platform" -t casual -n 2
```

### `templates` — Browse Templates

List all available email templates from the template library.

```bash
sales-email templates
```

<details>
<summary>📋 <strong>Example Output</strong></summary>

```
            📋 Email Templates
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Name           ┃ Description                       ┃ Word Count ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ cold_outreach  │ First contact with a new prospect │   150-200  │
├────────────────┼───────────────────────────────────┼────────────┤
│ follow_up      │ Follow up after initial contact   │   100-150  │
├────────────────┼───────────────────────────────────┼────────────┤
│ demo_request   │ Invite prospect to a product demo │   120-180  │
├────────────────┼───────────────────────────────────┼────────────┤
│ case_study     │ Share relevant case study         │   150-200  │
├────────────────┼───────────────────────────────────┼────────────┤
│ break_up       │ Final follow-up before closing    │    80-120  │
┗━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━┛
```

</details>

### `research` — Prospect Research

Generate an AI-powered research profile for a prospect.

```bash
sales-email research [OPTIONS]
```

| Option | Short | Required | Default | Description |
|--------|-------|----------|---------|-------------|
| `--prospect` | `-p` | ✅ | — | Prospect info to research |

```bash
# Research a prospect
sales-email research -p "CTO at AI startup, Series B, 200 employees, healthcare vertical"
```

<details>
<summary>🔍 <strong>Example Output</strong></summary>

```
╭─ 📊 Prospect Profile ─────────────────────────────────────────────────╮
│                                                                       │
│  ## Pain Points                                                       │
│  • Scaling ML infrastructure while maintaining HIPAA compliance       │
│  • Recruiting and retaining specialized AI/ML talent                  │
│  • Managing technical debt from rapid Series A growth                 │
│                                                                       │
│  ## Talking Points                                                    │
│  • Healthcare AI market projected to reach $45B by 2030               │
│  • Series B focus: proving unit economics and path to profitability   │
│  • 200-person teams need robust engineering processes                 │
│                                                                       │
│  ## Industry Context                                                  │
│  The healthcare AI sector is experiencing rapid growth with           │
│  increasing regulatory scrutiny. Companies at Series B stage          │
│  must balance innovation velocity with compliance requirements.       │
│                                                                       │
╰───────────────────────────────────────────────────────────────────────╯
```

</details>

### Global Options

```bash
sales-email --help        # Show all commands and options
sales-email --version     # Show version number
```

---

## 🖥️ Web UI

The Streamlit-based web dashboard provides a visual interface for all email generation features.

### Launch

```bash
streamlit run src/sales_email_gen/web_ui.py
```

### Dashboard Tabs

| Tab | Description | Key Features |
|-----|-------------|--------------|
| **📝 Prospect Form** | Enter prospect details and generate emails | Tone selector, context fields, follow-up toggle |
| **✉️ Generated Emails** | View and manage generated emails | Copy to clipboard, personalization scoring |
| **📧 Sequence Builder** | Build multi-email drip sequences | Timeline visualization, delay configuration |
| **📋 Template Browser** | Browse and preview templates | Template details, structure breakdown, word counts |

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800"/>
</div>

<br/>

### Pipeline Flow

```
Prospect Info ──→ Research Engine ──→ Tone Selector ──→ Template Library
                                                              │
                                                              ▼
                  config.yaml ─ ─ ─ ─→ LLM Email Generator ←─ ─ ─ Ollama LLM
                                              │
                           ┌──────────────────┼──────────────────┐
                           ▼                  ▼                  ▼
                    Variant Creator   Sequence Builder   Personalization Scorer
                           │                  │                  │
                           └──────────────────┼──────────────────┘
                                              ▼
                                  Rich Output (CLI / Web UI)
```

### Project Structure

```
48-sales-email-generator/
├── src/
│   └── sales_email_gen/
│       ├── __init__.py              # Package metadata & version
│       ├── core.py                  # Business logic — all generation functions
│       ├── cli.py                   # Click CLI with Rich output formatting
│       └── web_ui.py               # Streamlit web dashboard
├── tests/
│   ├── test_core.py                # Core logic unit tests
│   └── test_cli.py                 # CLI integration tests
├── common/
│   └── llm_client.py               # Shared Ollama client (chat, check_ollama_running)
├── docs/
│   └── images/
│       ├── banner.svg              # Project banner
│       ├── architecture.svg        # Architecture diagram
│       └── features.svg            # Features overview
├── config.yaml                     # Model, tone, sequence, scoring configuration
├── setup.py                        # Package setup & entry points
├── requirements.txt                # Python dependencies
├── Makefile                        # Build, test, lint targets
├── .env.example                    # Environment variable template
└── README.md                       # This file
```

### Component Responsibilities

| Component | File | Purpose |
|-----------|------|---------|
| **Core Engine** | `core.py` | All business logic: email generation, research, scoring, templates |
| **CLI Interface** | `cli.py` | Terminal commands with Click + Rich formatting |
| **Web Dashboard** | `web_ui.py` | Streamlit UI with tabs for every workflow |
| **LLM Client** | `common/llm_client.py` | Ollama API wrapper: `chat()`, `check_ollama_running()` |
| **Configuration** | `config.yaml` | Model settings, tone descriptions, sequence timing, scoring |

---

## 📚 API Reference

### Core Functions

#### `generate_email(prospect, product, tone, context, follow_up)`

Generate a single personalized sales email.

```python
from sales_email_gen.core import generate_email

email = generate_email(
    prospect="CTO at Series B fintech startup",
    product="AI Code Review Platform",
    tone="professional",        # professional | casual | persuasive | consultative
    context="Met at KubeCon",   # optional additional context
    follow_up=False             # True for follow-up emails
)

print(email["subject"])  # "Accelerating Code Quality at Scale"
print(email["body"])     # Full email body text
```

**Returns:** `{"subject": str, "body": str}`

---

#### `generate_variants(prospect, product, tone, count)`

Generate multiple email variants for A/B testing. Each variant uses a different hook/angle.

```python
from sales_email_gen.core import generate_variants

variants = generate_variants(
    prospect="VP Engineering at enterprise",
    product="DevOps Platform",
    tone="persuasive",
    count=3                     # number of variants
)

for i, variant in enumerate(variants, 1):
    print(f"Variant {i}: {variant['subject']}")
    print(variant["body"])
    print("---")
```

**Returns:** `[{"subject": str, "body": str}, ...]`

---

#### `research_prospect(prospect_info)`

Generate an AI-powered research profile with structured intelligence.

```python
from sales_email_gen.core import research_prospect

profile = research_prospect(
    "CTO at healthcare AI startup, Series B, 200 employees"
)

print(profile["pain_points"])       # ["Scaling ML infra...", "HIPAA compliance...", ...]
print(profile["talking_points"])    # ["Healthcare AI market...", "Series B focus...", ...]
print(profile["industry_context"])  # "The healthcare AI sector is experiencing..."
```

**Returns:** `{"pain_points": [str], "talking_points": [str], "industry_context": str}`

---

#### `generate_follow_up_sequence(prospect, product, tone, num_emails)`

Generate a complete multi-email follow-up sequence with delay scheduling.

```python
from sales_email_gen.core import generate_follow_up_sequence

sequence = generate_follow_up_sequence(
    prospect="Head of Sales at mid-market SaaS",
    product="CRM Analytics Suite",
    tone="consultative",
    num_emails=4                # intro → value_add → case_study → break_up
)

for email in sequence:
    print(f"Day {email['delay_days']} — {email['step']}: {email['subject']}")
    # Day 0  — intro: "Unlocking Sales Insights..."
    # Day 3  — value_add: "3 Metrics Your CRM Is Missing..."
    # Day 7  — case_study: "How Acme Increased Pipeline by 40%..."
    # Day 14 — break_up: "Should I Close Your File?"
```

**Returns:** `[{"step": str, "subject": str, "body": str, "delay_days": int}, ...]`

---

#### `score_personalization(email_body, prospect_info)`

Score how personalized an email is on a 0–100 scale with improvement suggestions.

```python
from sales_email_gen.core import score_personalization

result = score_personalization(
    email_body="Hi, I noticed your company is growing fast...",
    prospect_info="CTO at fintech startup, 150 employees"
)

print(result["score"])        # 72
print(result["suggestions"])  # ["Reference specific company name", "Mention their role...", ...]
```

**Returns:** `{"score": int, "suggestions": [str]}`

---

#### `get_template(template_name)` / `list_templates()`

Access the built-in template library.

```python
from sales_email_gen.core import get_template, list_templates

# List all templates
templates = list_templates()
# ["cold_outreach", "follow_up", "demo_request", "case_study", "break_up"]

# Get template details
tmpl = get_template("cold_outreach")
print(tmpl["description"])   # "First contact with a new prospect"
print(tmpl["word_count"])    # "150-200"
print(tmpl["structure"])     # "1. Attention-grabbing opener..."
```

**Returns:** `{"description": str, "word_count": str, "structure": str}`

---

### Constants

```python
from sales_email_gen.core import TONE_DESCRIPTIONS, TEMPLATE_LIBRARY, SEQUENCE_TYPES

# Available tones
TONE_DESCRIPTIONS = {
    "professional": "Formal, business-appropriate, respectful",
    "casual":       "Friendly, conversational, approachable",
    "persuasive":   "Compelling, benefit-focused, action-oriented",
    "consultative": "Advisory, problem-solving, thought-leadership",
}

# Template names
TEMPLATE_LIBRARY.keys()  # cold_outreach, follow_up, demo_request, case_study, break_up

# Sequence step order
SEQUENCE_TYPES = ["intro", "value_add", "case_study", "break_up"]
```

---

### Helper Functions

#### `_parse_email_response(response, fallback_subject)`

Parse raw LLM text into structured email format. Extracts subject line and body.

```python
from sales_email_gen.core import _parse_email_response

raw = "Subject: Quick Question\n\nHi there,\nI wanted to reach out..."
parsed = _parse_email_response(raw, fallback_subject="Follow Up")
# {"subject": "Quick Question", "body": "Hi there,\nI wanted to reach out..."}
```

#### `load_config(path)`

Load configuration from YAML. Falls back to sensible defaults if file not found.

```python
from sales_email_gen.core import load_config

config = load_config()                    # uses default config.yaml
config = load_config("custom.yaml")       # uses custom path
```

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# LLM Model Settings
model:
  name: "gemma3"           # Ollama model name
  temperature: 0.7         # Creativity level (0.0 = deterministic, 1.0 = creative)
  max_tokens: 2000         # Maximum response length

# Tone Definitions
tones:
  professional: "Formal, business-appropriate, respectful"
  casual: "Friendly, conversational, approachable"
  persuasive: "Compelling, benefit-focused, action-oriented"
  consultative: "Advisory, problem-solving, thought-leadership"

# Template Settings
templates:
  cold_outreach:
    description: "First contact with a new prospect"
    word_count: "150-200"
  follow_up:
    description: "Follow up after initial contact"
    word_count: "100-150"
  demo_request:
    description: "Invite prospect to a product demo"
    word_count: "120-180"
  case_study:
    description: "Share relevant case study"
    word_count: "150-200"
  break_up:
    description: "Final follow-up before closing"
    word_count: "80-120"

# Sequence Configuration
sequence:
  default_emails: 4                # Number of emails in a sequence
  delay_days: [0, 3, 7, 14]       # Days between each email

# Personalization Scoring
personalization:
  min_score: 60                    # Minimum acceptable score
  target_score: 80                 # Target personalization score

# Logging
logging:
  level: "INFO"                    # DEBUG, INFO, WARNING, ERROR
  file: "sales_email_gen.log"      # Log file path
```

### Environment Variables

Set these in `.env` or export them (see `.env.example`):

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `gemma3` | Default LLM model |
| `LOG_LEVEL` | `INFO` | Logging level |
| `CONFIG_PATH` | `config.yaml` | Path to configuration file |

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=src/sales_email_gen --cov-report=term-missing

# Run specific test files
pytest tests/test_core.py -v    # Core business logic tests
pytest tests/test_cli.py -v     # CLI integration tests

# Syntax validation
python -m py_compile src/sales_email_gen/core.py
python -m py_compile src/sales_email_gen/cli.py
python -m py_compile src/sales_email_gen/web_ui.py
```

### Test Structure

| File | Tests | What It Covers |
|------|-------|----------------|
| `test_core.py` | Unit tests | `generate_email`, `generate_variants`, `research_prospect`, `generate_follow_up_sequence`, `score_personalization`, `get_template`, `list_templates`, `_parse_email_response` |
| `test_cli.py` | Integration tests | CLI commands (`generate`, `variants`, `sequence`, `templates`, `research`), option parsing, Rich output |

---

## 🏠 Local vs Cloud

| Aspect | Sales Email Generator (Local) | Cloud API Solutions |
|--------|-------------------------------|---------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Prospect data sent to third-party servers |
| **Cost** | ✅ Free after hardware | ❌ Per-token pricing adds up fast |
| **Latency** | ✅ No network round-trips | ❌ API latency + rate limits |
| **Customization** | ✅ Full control over prompts, models, config | ⚠️ Limited to API parameters |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Model Choice** | ✅ Any Ollama-compatible model | ❌ Locked to provider's models |
| **Rate Limits** | ✅ None — limited only by hardware | ❌ API rate limits and quotas |
| **Setup** | ⚠️ Requires Ollama installation | ✅ Just an API key |

---

## ❓ FAQ

<details>
<summary><strong>1. Which Ollama models work best?</strong></summary>

The default model is `gemma3`, which provides a good balance of quality and speed. Other recommended models:

- **`llama3`** — Excellent for professional/formal emails
- **`mistral`** — Fast generation with good quality
- **`gemma3`** — Strong at following structured output formats
- **`qwen2`** — Good multilingual support

Change the model in `config.yaml`:

```yaml
model:
  name: "llama3"
```

</details>

<details>
<summary><strong>2. How do I improve personalization scores?</strong></summary>

The personalization scorer evaluates emails on a 0–100 scale. To improve scores:

1. **Include specific details** — Mention the prospect's company name, role, and industry
2. **Reference their challenges** — Use the research profile's pain points
3. **Add context** — Use the `--context` flag with relevant information
4. **Use research first** — Run `sales-email research -p "..."` before generating emails

Target score is configurable in `config.yaml` under `personalization.target_score`.

</details>

<details>
<summary><strong>3. Can I customize the sequence timing?</strong></summary>

Yes. Edit the `delay_days` array in `config.yaml`:

```yaml
sequence:
  default_emails: 4
  delay_days: [0, 3, 7, 14]    # Day 0, Day 3, Day 7, Day 14
```

For more aggressive follow-ups: `[0, 1, 3, 7]`
For longer cadences: `[0, 5, 14, 30]`

</details>

<details>
<summary><strong>4. How do I add custom templates?</strong></summary>

Add a new entry to the `TEMPLATE_LIBRARY` dict in `core.py`:

```python
TEMPLATE_LIBRARY["partnership"] = {
    "description": "Propose a strategic partnership",
    "word_count": "150-200",
    "structure": (
        "1. Reference mutual benefit\n"
        "2. Outline partnership opportunity\n"
        "3. Share relevant success metrics\n"
        "4. Suggest exploratory call"
    ),
}
```

The template will automatically appear in `sales-email templates` and the Web UI.

</details>

<details>
<summary><strong>5. Does it work offline?</strong></summary>

Yes, 100%. The entire pipeline runs locally:

- **Ollama** runs the LLM on your machine (CPU or GPU)
- **No API keys** required
- **No internet** needed after initial model download
- **No telemetry** or data collection

Just make sure to pull your model before going offline: `ollama pull gemma3`

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/sales-email-generator.git
cd sales-email-generator

# 3. Install in development mode
pip install -e ".[dev]"

# 4. Create a feature branch
git checkout -b feature/your-feature-name

# 5. Make your changes and add tests
pytest tests/ -v

# 6. Commit and push
git add .
git commit -m "feat: add your feature description"
git push origin feature/your-feature-name

# 7. Open a Pull Request
```

### Development Guidelines

- Write tests for new features in `tests/`
- Follow existing code style (type hints, docstrings)
- Keep `core.py` free of UI dependencies
- Update `config.yaml` if adding new configurable options

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**[⬆ Back to Top](#)**

Built with ❤️ using [Ollama](https://ollama.ai/) · [Click](https://click.palletsprojects.com/) · [Streamlit](https://streamlit.io/) · [Rich](https://github.com/Textualize/rich)

Part of the **[90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)** collection

<img src="https://img.shields.io/badge/Project_%2348-Sales_Email_Generator-e63946?style=for-the-badge" alt="Project #48"/>

</div>
