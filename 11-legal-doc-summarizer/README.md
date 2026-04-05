<!-- ═══════════════════════════════════════════════════════════════════════
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()
     ⚖️  LEGAL DOCUMENT SUMMARIZER — README
     AI-Powered Contract Analysis • Clause Extraction • Risk Scoring
     ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

![Banner](docs/images/banner.svg)

<br/>

<!-- ─── Badge Row 1: Core Technologies ─── -->

![Gemma 4](https://img.shields.io/badge/Gemma_4-Local_LLM-e94560?style=for-the-badge&logo=google&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Inference-16213e?style=for-the-badge&logo=ollama&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=for-the-badge&logo=python&logoColor=white)
![Privacy](https://img.shields.io/badge/100%25-Private-2ec4b6?style=for-the-badge&logo=lock&logoColor=white)

<!-- ─── Badge Row 2: Ecosystem ─── -->

![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Click](https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnubash&logoColor=white)
![pytest](https://img.shields.io/badge/pytest-Tests-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)

<br/>

**AI-powered legal document analysis that runs 100% locally on your machine.**
**Summarize contracts, extract clauses, score risks — all without sending a single byte to the cloud.**

<br/>

[Features](#-features) •
[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[Architecture](#-architecture) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[FAQ](#-faq)

</div>

<br/>

> **Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection** — a curated series of production-grade applications powered entirely by local language models. No API keys. No cloud dependencies. No data leakage.

---

## 💡 Why This Project?

Legal professionals and businesses deal with contracts every day, but reviewing them is tedious, expensive, and error-prone. This tool brings AI-powered analysis to your local machine — keeping sensitive legal documents **completely private**.

| Problem | Solution |
|:--------|:---------|
| 📄 Manual contract review takes **hours** | ⚡ AI summarizes in **seconds** |
| 💰 Legal review services cost **$200–500/hour** | 🆓 Unlimited analysis, **zero cost** |
| 🔓 Cloud AI tools require uploading **sensitive data** | 🔒 100% local — data **never leaves** your machine |
| 📋 Missed clauses create **legal liability** | 🔍 Systematic extraction of **all 7 clause categories** |
| 🎯 Risk assessment depends on **subjective judgment** | 📊 Quantified risk scores across **5 dimensions** |

---

## ✨ Features

<div align="center">

![Features](docs/images/features.svg)

</div>

<br/>

<table>
<tr>
<td width="50%">

### 📋 Multi-Format Summarization
Generate summaries in **3 output formats** tailored to your needs:
- **Bullet** — Quick-scan key points
- **Narrative** — Flowing prose summary
- **Detailed** — Comprehensive analysis

Automatically extracts: parties involved, key clauses, obligations, important dates, termination conditions, and penalties.

</td>
<td width="50%">

### 🔍 Clause Extraction & Categorization
Identifies and categorizes clauses into **7 distinct types**:
- 💰 Payment Terms
- 🚪 Termination Conditions
- 🤫 Confidentiality & NDA
- ⚖️ Liability Limitations
- 🧠 Intellectual Property
- 📜 Regulatory Compliance
- 📦 Other / Miscellaneous

Each clause is assigned a risk level: **Low**, **Medium**, or **High**.

</td>
</tr>
<tr>
<td width="50%">

### ⚠️ Risk Scoring Engine
Quantified risk assessment across **5 dimensions**, each scored **0–10**:

| Dimension | What It Measures |
|:----------|:-----------------|
| Financial | Payment terms, penalties, liability caps |
| Termination | Exit clauses, notice periods, auto-renewal |
| Intellectual Property | IP ownership, licensing, work-for-hire |
| Compliance | Regulatory requirements, audit rights |
| Confidentiality | Data protection, NDA scope, breach remedies |

**Overall score: 0–100** (sum of all dimensions × 2).

</td>
<td width="50%">

### 📑 Document Comparison
Compare **multiple legal documents** side by side:
- Highlights differences in key clauses
- Identifies missing protections across documents
- Compares risk profiles
- Surfaces conflicting terms

### 💾 Export Engine
Generate **PDF-ready markdown reports** with:
- Formatted summary sections
- Clause categorization tables
- Risk score visualizations
- All findings in a single exportable document

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://python.org) | 3.11+ | Runtime |
| [Ollama](https://ollama.ai) | Latest | Local LLM inference engine |
| [Gemma 4](https://ollama.com/library/gemma4) | Latest | Language model for analysis |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/legal-doc-summarizer.git
cd legal-doc-summarizer

# 2. Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install and start Ollama
# Visit https://ollama.ai for installation instructions

# 5. Pull the Gemma 4 model
ollama pull gemma4
```

### First Run

```bash
# Summarize a sample contract
python -m legal_summarizer.cli summarize --file sample_contract.pdf

# Try a detailed summary with export
python -m legal_summarizer.cli summarize \
    --file contract.pdf \
    --format detailed \
    --export summary_report.md
```

<details>
<summary><b>📋 Example Output (click to expand)</b></summary>

```
╭──────────────────────────────────────────────────────────────╮
│                  ⚖️  Document Summary                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  📌 Parties:                                                 │
│     • Acme Corporation (Provider)                            │
│     • GlobalTech Inc. (Client)                               │
│                                                              │
│  📋 Key Clauses:                                             │
│     • Service Level Agreement (99.9% uptime)                 │
│     • Payment: Net-30, $50,000/month                         │
│     • Term: 24 months, auto-renewal                          │
│     • Liability cap: 12 months of fees                       │
│                                                              │
│  📅 Important Dates:                                         │
│     • Effective: January 1, 2025                             │
│     • Renewal deadline: December 1, 2026                     │
│                                                              │
│  ⚠️  Termination Conditions:                                 │
│     • 90-day written notice required                         │
│     • Immediate termination for material breach              │
│                                                              │
│  💰 Penalties:                                               │
│     • Late payment: 1.5% per month                           │
│     • Early termination: 6 months of fees                    │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

</details>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/legal-doc-summarizer.git
cd legal-doc-summarizer
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
uvicorn src.legal_summarizer.api:app --reload --port 8000

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

## 🖥️ CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://rich.readthedocs.io/) for beautiful terminal output.

```bash
python -m legal_summarizer.cli [GLOBAL OPTIONS] COMMAND [COMMAND OPTIONS]
```

### Global Options

| Option | Short | Description |
|:-------|:------|:------------|
| `--verbose` | `-v` | Enable verbose/debug output |
| `--config` | | Path to custom `config.yaml` file |

---

### `summarize` — Summarize a Legal Document

Analyzes a legal document and produces a structured summary with parties, clauses, obligations, dates, termination conditions, and penalties.

```bash
python -m legal_summarizer.cli summarize --file contract.pdf --format bullet
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--file` | `-f` | *(required)* | Path to the legal document (PDF or TXT) |
| `--format` | `-fmt` | `bullet` | Output format: `bullet`, `narrative`, or `detailed` |
| `--export` | `-e` | | Export results to a markdown file |

**Output formats explained:**

| Format | Best For | Description |
|:-------|:---------|:------------|
| `bullet` | Quick review | Concise bullet-point list of key findings |
| `narrative` | Presentations | Flowing paragraph-style summary |
| `detailed` | Deep analysis | Comprehensive breakdown with all extracted data |

---

### `clauses` — Extract & Categorize Clauses

Identifies all clauses in a document, categorizes them, and assigns risk levels.

```bash
python -m legal_summarizer.cli clauses --file agreement.pdf
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--file` | `-f` | *(required)* | Path to the legal document (PDF or TXT) |

**Clause categories:**

| Category | Icon | Examples |
|:---------|:-----|:---------|
| Payment | 💰 | Net terms, late fees, payment schedules |
| Termination | 🚪 | Notice periods, exit clauses, auto-renewal |
| Confidentiality | 🤫 | NDA terms, data handling, disclosure limits |
| Liability | ⚖️ | Liability caps, indemnification, warranties |
| Intellectual Property | 🧠 | IP ownership, licensing, work-for-hire |
| Compliance | 📜 | Regulatory requirements, audit rights |
| Other | 📦 | Force majeure, dispute resolution, amendments |

---

### `risks` — Score Risk Factors

Performs a quantified risk assessment across 5 dimensions, each scored 0–10, with an overall score of 0–100.

```bash
python -m legal_summarizer.cli risks --file lease_agreement.pdf
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--file` | `-f` | *(required)* | Path to the legal document (PDF or TXT) |

<details>
<summary><b>⚠️ Example Risk Output (click to expand)</b></summary>

```
╭──────────────────────────────────────────────────────────────╮
│                  ⚠️  Risk Assessment                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Financial Risk        ████████░░  8/10   HIGH               │
│  Termination Risk      ██████░░░░  6/10   MEDIUM             │
│  IP Risk               ███░░░░░░░  3/10   LOW                │
│  Compliance Risk       █████░░░░░  5/10   MEDIUM             │
│  Confidentiality Risk  ████░░░░░░  4/10   LOW                │
│                                                              │
│  ────────────────────────────────────────────                 │
│  Overall Risk Score:   52/100   ⚠️  MODERATE                 │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

</details>

---

### `compare` — Compare Multiple Documents

Performs side-by-side comparison of multiple legal documents, highlighting differences in clauses, terms, and risk profiles.

```bash
python -m legal_summarizer.cli compare \
    --files vendor_a.pdf \
    --files vendor_b.pdf \
    --files vendor_c.pdf
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--files` | `-f` | *(required, multiple)* | Paths to documents to compare (specify multiple times) |

---

### `export` — Generate a Full Report

Combines summarization, clause extraction, and risk scoring into a single PDF-ready markdown report.

```bash
python -m legal_summarizer.cli export \
    --file contract.pdf \
    --output analysis_report.md \
    --format detailed
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--file` | `-f` | *(required)* | Path to the legal document (PDF or TXT) |
| `--output` | `-o` | *(required)* | Output filepath for the markdown report |
| `--format` | `-fmt` | `bullet` | Summary format: `bullet`, `narrative`, or `detailed` |

---

## 🌐 Web UI

A full-featured **Streamlit** web interface is included for visual, interactive analysis.

```bash
streamlit run src/legal_summarizer/web_ui.py
```

The web UI provides:

| Feature | Description |
|:--------|:------------|
| 📁 **File Uploader** | Drag & drop PDF or TXT files |
| 📋 **Summary Panel** | Formatted document summary with format selector |
| 📄 **Clause Table** | Interactive, categorized clause listing with risk badges |
| ⚠️ **Risk Meter** | Visual risk score gauges for each dimension |
| 📊 **Comparison View** | Upload multiple files for side-by-side analysis |
| 📥 **Export** | Download markdown reports directly from the browser |

---

## 🏗️ Architecture

<div align="center">

![Architecture](docs/images/architecture.svg)

</div>

<br/>

### Data Flow

```
📄 Input Document (PDF/TXT)
    │
    ▼
📝 Text Extraction (PyPDF2 / pdfplumber)
    │   └─ Truncated to max 12,000 characters
    │
    ▼
🤖 Gemma 4 via Ollama (temperature: 0.3)
    │
    ├── 📋 summarize_document()  →  Structured summary
    ├── 🔍 extract_clauses()     →  Categorized clause table
    ├── ⚠️ score_risks()         →  5-dimension risk scores
    └── 📑 compare_documents()   →  Multi-doc comparison
    │
    ▼
📊 Structured Output (Rich tables / JSON)
    │
    ▼
💾 generate_export_markdown()  →  PDF-ready report
```

### Project Structure

```
11-legal-doc-summarizer/
│
├── src/
│   └── legal_summarizer/
│       ├── __init__.py           # Package initialization
│       ├── core.py               # Core business logic (5 main functions)
│       ├── cli.py                # Click CLI interface (5 commands)
│       ├── web_ui.py             # Streamlit web interface
│       ├── config.py             # Configuration management (YAML + env)
│       └── utils.py              # Shared utilities & helpers
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py              # Core logic unit tests
│   └── test_cli.py               # CLI integration tests
│
├── docs/
│   └── images/
│       ├── banner.svg            # README hero banner
│       ├── architecture.svg      # Architecture diagram
│       └── features.svg          # Feature highlights graphic
│
├── config.yaml                   # Default configuration
├── setup.py                      # Package setup
├── requirements.txt              # Python dependencies
├── Makefile                      # Development shortcuts
├── .env.example                  # Environment variable template
└── README.md                     # You are here
```

---

## 🔌 API Reference

All core functions are available for programmatic use in your own Python scripts.

### Import

```python
from legal_summarizer.core import (
    summarize_document,
    extract_clauses,
    score_risks,
    compare_documents,
    generate_export_markdown,
)
```

---

### `summarize_document(text, output_format="bullet", config=None)`

Analyzes a legal document and returns a structured summary.

```python
from legal_summarizer.core import summarize_document

with open("contract.txt", "r") as f:
    text = f.read()

# Bullet-point summary (default)
summary = summarize_document(text)
print(summary)

# Narrative summary
summary = summarize_document(text, output_format="narrative")

# Detailed summary with custom config
summary = summarize_document(text, output_format="detailed", config=my_config)
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `text` | `str` | *(required)* | Raw text content of the legal document |
| `output_format` | `str` | `"bullet"` | One of `"bullet"`, `"narrative"`, `"detailed"` |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** Structured summary dict with parties, clauses, obligations, dates, termination conditions, and penalties.

---

### `extract_clauses(text, config=None)`

Identifies, categorizes, and risk-scores all clauses in a document.

```python
from legal_summarizer.core import extract_clauses

clauses = extract_clauses(document_text)

for clause in clauses:
    print(f"[{clause['category']}] {clause['text']}")
    print(f"  Risk Level: {clause['risk_level']}")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `text` | `str` | *(required)* | Raw text content of the legal document |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** List of clause dicts with `category` (Payment, Termination, Confidentiality, Liability, IP, Compliance, Other), `text`, and `risk_level` (Low, Medium, High).

---

### `score_risks(text, config=None)`

Performs quantified risk assessment across 5 dimensions.

```python
from legal_summarizer.core import score_risks

risk_analysis = score_risks(document_text)

print(f"Overall Risk: {risk_analysis['overall_score']}/100")
for dimension, score in risk_analysis['dimensions'].items():
    print(f"  {dimension}: {score}/10")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `text` | `str` | *(required)* | Raw text content of the legal document |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** Dict with `dimensions` (Financial, Termination, IP, Compliance, Confidentiality — each 0–10) and `overall_score` (0–100).

---

### `compare_documents(file_paths, config=None)`

Compares multiple legal documents side by side.

```python
from legal_summarizer.core import compare_documents

comparison = compare_documents(
    file_paths=["vendor_a.pdf", "vendor_b.pdf", "vendor_c.pdf"]
)

for doc_name, analysis in comparison.items():
    print(f"\n--- {doc_name} ---")
    print(analysis)
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `file_paths` | `list[str]` | *(required)* | List of file paths to compare |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** Comparison dict with per-document analysis and cross-document insights.

---

### `generate_export_markdown(summary, clauses, risk_analysis, filepath)`

Generates a comprehensive, PDF-ready markdown report.

```python
from legal_summarizer.core import (
    summarize_document,
    extract_clauses,
    score_risks,
    generate_export_markdown,
)

# Run all analyses
summary = summarize_document(text, output_format="detailed")
clauses = extract_clauses(text)
risk_analysis = score_risks(text)

# Export to markdown
generate_export_markdown(
    summary=summary,
    clauses=clauses,
    risk_analysis=risk_analysis,
    filepath="full_report.md"
)

print("✅ Report saved to full_report.md")
```

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `summary` | `dict` | Output from `summarize_document()` |
| `clauses` | `list` | Output from `extract_clauses()` |
| `risk_analysis` | `dict` | Output from `score_risks()` |
| `filepath` | `str` | Destination file path for the markdown report |

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# ─── LLM Settings ───────────────────────────────────────────
llm:
  model: "gemma4"
  temperature: 0.3          # Lower = more deterministic
  max_tokens: 4096          # Max response length
  host: "http://localhost:11434"

# ─── Processing Settings ────────────────────────────────────
processing:
  max_document_chars: 12000  # Truncate input beyond this limit
  supported_formats:
    - ".pdf"
    - ".txt"

# ─── Output Settings ────────────────────────────────────────
output:
  default_format: "bullet"   # bullet | narrative | detailed
  export_dir: "./exports"
  include_timestamps: true

# ─── Logging ─────────────────────────────────────────────────
logging:
  level: "INFO"              # DEBUG | INFO | WARNING | ERROR
  file: "legal_summarizer.log"
```

### Environment Variable Overrides

Environment variables take precedence over `config.yaml` settings:

| Variable | Config Key | Default | Description |
|:---------|:-----------|:--------|:------------|
| `LEGAL_SUMMARIZER_MODEL` | `llm.model` | `gemma4` | Ollama model name |
| `LEGAL_SUMMARIZER_TEMPERATURE` | `llm.temperature` | `0.3` | LLM temperature |
| `LEGAL_SUMMARIZER_MAX_TOKENS` | `llm.max_tokens` | `4096` | Max response tokens |
| `LEGAL_SUMMARIZER_MAX_CHARS` | `processing.max_document_chars` | `12000` | Input truncation limit |
| `LEGAL_SUMMARIZER_HOST` | `llm.host` | `http://localhost:11434` | Ollama server URL |

---

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=legal_summarizer --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_core.py -v
python -m pytest tests/test_cli.py -v
```

### Test Coverage

| Module | Coverage | Description |
|:-------|:---------|:------------|
| `core.py` | Core | Summarization, clause extraction, risk scoring, comparison |
| `cli.py` | CLI | All 5 commands, option parsing, error handling |
| `config.py` | Config | YAML loading, env var overrides, defaults |
| `utils.py` | Utils | Text extraction, file handling, helpers |

---

## 🔒 Local vs Cloud — Why Local Wins

| Feature | ⚖️ This Tool (Local) | ☁️ Cloud AI Services |
|:--------|:---------------------|:---------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Documents uploaded to third-party servers |
| **Cost** | ✅ Free — unlimited usage | ❌ $0.01–0.06 per 1K tokens |
| **Internet Required** | ✅ No — fully offline capable | ❌ Yes — always online |
| **Speed** | ✅ No network latency | ⚠️ Depends on API response time |
| **Data Retention** | ✅ Nothing stored externally | ❌ May be stored for training |
| **Compliance** | ✅ Meets strict data residency requirements | ⚠️ Varies by provider |
| **Customization** | ✅ Full control over model & prompts | ⚠️ Limited to provider's API |

---

## ❓ FAQ

<details>
<summary><b>What models are supported besides Gemma 4?</b></summary>

<br/>

Any model available through Ollama can be used. Update the `llm.model` field in `config.yaml` or set the `LEGAL_SUMMARIZER_MODEL` environment variable. Popular alternatives include `llama3`, `mistral`, and `phi3`. However, **Gemma 4 is recommended** for the best balance of speed and legal document comprehension.

```bash
# Use a different model
export LEGAL_SUMMARIZER_MODEL=llama3
```

</details>

<details>
<summary><b>What is the maximum document size?</b></summary>

<br/>

By default, documents are truncated to **12,000 characters** (`processing.max_document_chars`). This limit ensures reliable LLM performance. You can increase it in `config.yaml`, but be aware that larger inputs may affect response quality and speed depending on your hardware.

```yaml
processing:
  max_document_chars: 24000  # Double the default
```

</details>

<details>
<summary><b>Can I use this for non-English legal documents?</b></summary>

<br/>

Gemma 4 has multilingual capabilities and can process documents in many languages. However, the **best results are with English documents**. For other languages, you may need to adjust the LLM temperature or use a model specifically fine-tuned for that language.

</details>

<details>
<summary><b>How do I process scanned PDF documents (images)?</b></summary>

<br/>

The current version supports **text-based PDFs** via PyPDF2 and pdfplumber. Scanned PDFs (image-based) require OCR preprocessing. You can use [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) to convert scanned PDFs to text first, then feed the text to this tool:

```bash
# Convert scanned PDF to text (requires tesseract)
tesseract scanned_doc.pdf output_text -l eng
python -m legal_summarizer.cli summarize --file output_text.txt
```

</details>

<details>
<summary><b>What hardware do I need to run this locally?</b></summary>

<br/>

| Component | Minimum | Recommended |
|:----------|:--------|:------------|
| RAM | 8 GB | 16 GB+ |
| GPU | Not required (CPU works) | NVIDIA GPU with 8 GB+ VRAM |
| Storage | 5 GB (for model) | 10 GB+ |
| CPU | 4 cores | 8+ cores |

Ollama handles model loading and inference. GPU acceleration is automatic if a compatible NVIDIA GPU is detected.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make** your changes and add tests
4. **Run** the test suite:
   ```bash
   python -m pytest tests/ -v
   ```
5. **Commit** your changes:
   ```bash
   git commit -m "feat: add amazing feature"
   ```
6. **Push** to your fork and open a **Pull Request**

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements.txt
pip install -e ".[dev]"

# Run linter
flake8 src/ tests/

# Run formatter
black src/ tests/

# Run tests with coverage
pytest tests/ -v --cov=legal_summarizer
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, including commercial use.

---

<div align="center">

<br/>

Built with ❤️ by [Kennedy Raju](https://github.com/kennedyraju55)

⚖️ **Legal Document Summarizer** — Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

<br/>

⭐ **Star this repo** if you find it useful!

<br/>

[⬆ Back to Top](#)

</div>
