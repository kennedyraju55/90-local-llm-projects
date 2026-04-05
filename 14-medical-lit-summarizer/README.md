<div align="center">

<picture>
  <img src="docs/images/banner.svg" alt="Medical Literature Summarizer — AI-Powered Research Analysis, PICO Extraction & Evidence Grading" width="900"/>
</picture>

<br/>

<img src="https://img.shields.io/badge/Gemma_4-Ollama-ff6b35?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.9+-3572A5?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Click-CLI-238636?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/Rich-Terminal_UI-ff6b35?style=flat-square" alt="Rich"/>
<img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/><br/>

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

</div>

<br/>

---

## Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [CLI Usage](#-cli-usage)
- [Python API](#-python-api)
- [Web UI](#-web-ui-streamlit)
- [Configuration](#%EF%B8%8F-configuration)
- [Project Structure](#-project-structure)
- [Core Functions Reference](#-core-functions-reference)
- [Detail Levels](#-detail-levels)
- [Evidence Grading System](#-evidence-grading-system)
- [PICO Framework](#-pico-framework)
- [Citation Formats](#-citation-formats)
- [Running Tests](#-running-tests)
- [Makefile Commands](#-makefile-commands)
- [FAQ](#-frequently-asked-questions)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🩺 Why This Project?

Medical researchers, clinicians, and evidence-based practitioners spend **hours** reviewing
published literature. A single systematic review can involve screening hundreds of papers,
extracting study characteristics, grading evidence quality, and formatting citations — all
before the actual synthesis begins.

**The problem is real:**

- A typical systematic review takes **6–18 months** to complete.
- Clinicians read an average of **3–5 papers per week**, yet thousands are published daily.
- Manual PICO extraction from a single RCT can take **20–30 minutes**.
- Evidence quality assessment requires cross-referencing multiple rubrics (GRADE, Oxford CEBM, Jadad).
- Citation formatting across APA, Vancouver, and other styles is tedious and error-prone.

**Medical Literature Summarizer** automates the most time-consuming parts of this workflow.
It runs **entirely on your local machine** using Gemma 4 through Ollama — no cloud APIs,
no data leaving your network, no patient-data concerns. Paste or upload a research paper and
receive a structured 8-section summary, PICO extraction, evidence grading across 6 dimensions,
and properly formatted citations in seconds.

This is not a replacement for expert clinical judgment. It is a **force multiplier** that lets
researchers focus on interpretation and synthesis rather than mechanical extraction.

---

## ✨ Features

<div align="center">

<picture>
  <img src="docs/images/features.svg" alt="Core capabilities — 8-Section Analysis, PICO Framework, Evidence Grading, Citation Generator, 3 Detail Levels, 100% Private" width="800"/>
</picture>

</div>

<br/>

| Capability | Description |
|---|---|
| **8-Section Structured Summary** | Extracts title/authors, abstract summary, methodology, key findings, statistical results, conclusions, limitations, and future work from any medical paper |
| **PICO Framework Extraction** | Identifies Population, Intervention, Comparison, and Outcome — the gold standard for clinical question formulation |
| **Evidence Quality Rating** | Grades papers across 6 dimensions (study design, sample size, methodology rigor, statistical analysis, bias risk) with an overall Oxford CEBM level from 1a to 5 |
| **Citation Formatting** | Generates properly formatted references in APA 7th, MLA 9th, Chicago 17th, and Vancouver (ICMJE) styles |
| **3 Detail Levels** | Choose `brief` for quick screening, `standard` for regular review, or `comprehensive` for deep analysis |
| **Dual Interface** | Full-featured CLI with Rich terminal formatting and a Streamlit web UI for interactive use |
| **100% Local & Private** | All inference runs through Ollama on your machine — zero data leaves your network |

---

## 🏗 Architecture

<div align="center">

<picture>
  <img src="docs/images/architecture.svg" alt="System architecture — Research Paper → Section Extraction → Gemma 4 via Ollama → Structured Medical Report" width="800"/>
</picture>

</div>

<br/>

The pipeline follows a four-stage flow:

1. **Input** — Raw paper text (pasted, file path, or uploaded via web UI) is read into memory.
2. **Parse** — `extract_section()` isolates logical sections from the unstructured text using LLM-guided prompts tailored to each of the 8 target sections.
3. **Analyze** — Gemma 4 (running locally via Ollama) processes each section through specialized prompts for summarization, PICO extraction, evidence rating, and citation formatting.
4. **Output** — Results are returned as structured Python dictionaries and rendered as Rich tables (CLI) or interactive panels (Streamlit).

All communication with the LLM happens over Ollama's local HTTP API (`http://localhost:11434`). No internet connection is required after initial model download.

---

## ⚡ Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/medical-lit-summarizer.git
cd medical-lit-summarizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama and pull the model
ollama serve &
ollama pull gemma4

# 4. Summarize your first paper
python -m medical_summarizer.cli summarize --paper sample_paper.txt --detail standard
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/medical-lit-summarizer.git
cd medical-lit-summarizer
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
uvicorn src.medical_summarizer.api:app --reload --port 8000

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

## 📦 Installation

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | 3.9+ | Runtime |
| [Ollama](https://ollama.com) | Latest | Local LLM inference |
| Gemma 4 | Via Ollama | Language model |

### Step-by-Step

```bash
# Clone
git clone https://github.com/kennedyraju55/medical-lit-summarizer.git
cd medical-lit-summarizer

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows

# Install Python dependencies
pip install -r requirements.txt

# Install the package in editable mode (optional, for development)
pip install -e .
```

### Ollama Setup

```bash
# Install Ollama (see https://ollama.com/download)
# Then start the server and pull the model:
ollama serve
ollama pull gemma4
```

Verify the model is available:

```bash
ollama list
# Should show: gemma4:latest
```

### Environment Configuration

Copy the example environment file and adjust if needed:

```bash
cp .env.example .env
```

The default configuration in `config.yaml` works out of the box. See the
[Configuration](#%EF%B8%8F-configuration) section for customization options.

---

## 📋 CLI Usage

The CLI is built with [Click](https://click.palletsprojects.com/) and uses
[Rich](https://rich.readthedocs.io/) for formatted terminal output. All commands
accept `--verbose / -v` for debug output and `--config` to specify a custom
configuration file.

### Summarize a Paper

```bash
# Standard detail (default)
python -m medical_summarizer.cli summarize --paper research.txt

# Brief summary for quick screening
python -m medical_summarizer.cli summarize --paper research.txt --detail brief

# Comprehensive deep-dive
python -m medical_summarizer.cli summarize --paper research.txt --detail comprehensive

# With verbose logging
python -m medical_summarizer.cli summarize --paper research.txt --detail standard -v
```

**Output** — A Rich-formatted table with 8 sections:

```
┌──────────────────────┬─────────────────────────────────────────────┐
│ Section              │ Content                                     │
├──────────────────────┼─────────────────────────────────────────────┤
│ Title & Authors      │ "Efficacy of Drug X in Type 2 Diabetes..."  │
│ Abstract Summary     │ This randomized controlled trial evaluated…  │
│ Methodology          │ Double-blind RCT, n=450, 12-week follow-up… │
│ Key Findings         │ HbA1c reduced by 1.2% (p<0.001)…            │
│ Statistical Results  │ Primary endpoint met; OR 2.3 (95% CI 1.8…   │
│ Conclusions          │ Drug X demonstrates superior glycemic…       │
│ Limitations          │ Single-center, short follow-up, industry…    │
│ Future Work          │ Multi-center trials, long-term outcomes…     │
└──────────────────────┴─────────────────────────────────────────────┘
```

### PICO Extraction

```bash
python -m medical_summarizer.cli pico --paper research.txt
```

**Output:**

```
┌─────────────┬───────────────────────────────────────────────┐
│ Component   │ Extraction                                    │
├─────────────┼───────────────────────────────────────────────┤
│ Population  │ Adults aged 40-65 with Type 2 Diabetes,       │
│             │ HbA1c > 7.5%, BMI 25-35                       │
│ Intervention│ Drug X 10mg daily for 12 weeks                 │
│ Comparison  │ Placebo control group matched for age/sex      │
│ Outcome     │ Change in HbA1c from baseline at 12 weeks      │
└─────────────┴───────────────────────────────────────────────┘
```

### Evidence Quality Rating

```bash
python -m medical_summarizer.cli evidence --paper research.txt
```

**Output:**

```
┌───────────────────────┬────────┬─────────────────────────────────┐
│ Dimension             │ Rating │ Notes                           │
├───────────────────────┼────────┼─────────────────────────────────┤
│ Study Design          │ 4/5    │ Double-blind RCT                │
│ Sample Size           │ 3/5    │ n=450, adequate for primary EP  │
│ Methodology Rigor     │ 4/5    │ Proper randomization, ITT       │
│ Statistical Analysis  │ 4/5    │ Pre-registered, Bonferroni adj. │
│ Bias Risk             │ 3/5    │ Industry-funded, single-center  │
├───────────────────────┼────────┼─────────────────────────────────┤
│ Overall Evidence Level│ 1b     │ Individual RCT (Oxford CEBM)    │
└───────────────────────┴────────┴─────────────────────────────────┘
```

### Citation Formatting

```bash
# APA 7th edition (default)
python -m medical_summarizer.cli cite --paper research.txt --style APA

# MLA 9th edition
python -m medical_summarizer.cli cite --paper research.txt --style MLA

# Chicago 17th edition
python -m medical_summarizer.cli cite --paper research.txt --style Chicago

# Vancouver / ICMJE
python -m medical_summarizer.cli cite --paper research.txt --style Vancouver
```

**Example APA output:**

```
Smith, J. A., & Doe, R. B. (2024). Efficacy of Drug X in glycemic control
    among adults with Type 2 Diabetes: A randomized controlled trial.
    Journal of Clinical Endocrinology, 109(3), 456-471.
    https://doi.org/10.xxxx/jce.2024.xxxxx
```

### Global Options

| Flag | Short | Description |
|---|---|---|
| `--verbose` | `-v` | Enable debug-level logging with Rich tracebacks |
| `--config` | | Path to a custom `config.yaml` file |

---

## 🐍 Python API

All functionality is available as importable Python functions in the `medical_summarizer` package.

### `summarize_paper()`

```python
from medical_summarizer.core import summarize_paper

with open("research.txt") as f:
    paper_text = f.read()

result = summarize_paper(paper_text, detail_level="standard", config=None)

# result is a dict with 8 keys:
# {
#     "title_authors": "...",
#     "abstract_summary": "...",
#     "methodology": "...",
#     "key_findings": "...",
#     "statistical_results": "...",
#     "conclusions": "...",
#     "limitations": "...",
#     "future_work": "..."
# }

for section, content in result.items():
    print(f"\n## {section}\n{content}")
```

### `extract_section()`

Extract a single section with fine-grained control:

```python
from medical_summarizer.core import extract_section

methodology = extract_section(
    paper_text,
    section_key="methodology",
    section_prompt="Extract the study methodology, including design, participants, and procedures.",
    detail_level="comprehensive",
    config=None
)
print(methodology)
```

### `extract_pico()`

```python
from medical_summarizer.core import extract_pico

pico = extract_pico(paper_text, config=None)

# pico = {
#     "population": "Adults aged 40-65 with Type 2 Diabetes...",
#     "intervention": "Drug X 10mg daily...",
#     "comparison": "Placebo control...",
#     "outcome": "Change in HbA1c at 12 weeks..."
# }
```

### `rate_evidence_quality()`

```python
from medical_summarizer.core import rate_evidence_quality

evidence = rate_evidence_quality(paper_text, config=None)

# evidence = {
#     "study_design": {"rating": 4, "notes": "Double-blind RCT"},
#     "sample_size": {"rating": 3, "notes": "n=450, adequate..."},
#     "methodology_rigor": {"rating": 4, "notes": "Proper randomization..."},
#     "statistical_analysis": {"rating": 4, "notes": "Pre-registered..."},
#     "bias_risk": {"rating": 3, "notes": "Industry-funded..."},
#     "overall_evidence_level": "1b"
# }
```

### `format_citation()`

```python
from medical_summarizer.core import format_citation

apa_citation = format_citation(paper_text, style="APA", config=None)
vancouver_citation = format_citation(paper_text, style="Vancouver", config=None)

print(apa_citation)
print(vancouver_citation)
```

---

## 🌐 Web UI (Streamlit)

The Streamlit web interface provides an interactive way to analyze papers:

```bash
streamlit run src/medical_summarizer/web_ui.py
```

**Features:**

- **Paper upload** — Drag and drop a `.txt` or `.pdf` file, or paste text directly
- **Tabbed results** — Switch between Summary, PICO, Evidence Rating, and Citation tabs
- **Detail level selector** — Toggle between brief, standard, and comprehensive
- **Citation style picker** — Generate citations in any of the 4 supported formats
- **Export** — Copy results to clipboard or download as JSON
- **Evidence dashboard** — Visual bar chart of the 6 evidence dimensions

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# LLM settings
llm:
  model: "gemma4"
  base_url: "http://localhost:11434"
  temperature: 0.3          # Lower = more deterministic medical output
  max_tokens: 4096
  timeout: 120              # Seconds to wait for LLM response

# Summarization defaults
summarization:
  default_detail_level: "standard"    # brief | standard | comprehensive
  sections:
    - title_authors
    - abstract_summary
    - methodology
    - key_findings
    - statistical_results
    - conclusions
    - limitations
    - future_work

# Citation defaults
citation:
  default_style: "APA"     # APA | MLA | Chicago | Vancouver

# Evidence rating
evidence:
  dimensions:
    - study_design
    - sample_size
    - methodology_rigor
    - statistical_analysis
    - bias_risk
  scale: 5                  # 1-5 rating scale
  cebm_levels:              # Oxford CEBM hierarchy
    - "1a"                   # Systematic review of RCTs
    - "1b"                   # Individual RCT
    - "2a"                   # Systematic review of cohort studies
    - "2b"                   # Individual cohort study
    - "3a"                   # Systematic review of case-control studies
    - "3b"                   # Individual case-control study
    - "4"                    # Case series
    - "5"                    # Expert opinion
```

### Environment Variables (`.env`)

```bash
# Override Ollama endpoint (default: http://localhost:11434)
OLLAMA_BASE_URL=http://localhost:11434

# Override model name
OLLAMA_MODEL=gemma4
```

### Custom Config File

Pass a custom configuration to any CLI command:

```bash
python -m medical_summarizer.cli summarize --paper paper.txt --config my_config.yaml
```

Or in Python:

```python
from medical_summarizer.config import load_config

config = load_config("my_config.yaml")
result = summarize_paper(paper_text, config=config)
```

---

## 📁 Project Structure

```
14-medical-lit-summarizer/
├── src/
│   └── medical_summarizer/
│       ├── __init__.py          # Package initialization, version
│       ├── core.py              # Core functions: summarize_paper, extract_pico,
│       │                        #   rate_evidence_quality, format_citation,
│       │                        #   extract_section
│       ├── cli.py               # Click CLI: summarize, pico, evidence, cite
│       ├── config.py            # Configuration loading and validation
│       ├── utils.py             # Text preprocessing, prompt templates
│       └── web_ui.py            # Streamlit web interface
├── common/
│   └── llm_client.py           # Shared Ollama client wrapper
├── tests/
│   ├── __init__.py
│   ├── test_core.py            # Unit tests for core functions
│   └── test_cli.py             # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # System architecture diagram
│       └── features.svg         # Feature overview graphic
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup
├── requirements.txt             # Python dependencies
├── Makefile                     # Development shortcuts
├── .env.example                 # Environment variable template
├── .gitignore
└── README.md                    # This file
```

---

## 📖 Core Functions Reference

### `extract_section(paper_text, section_key, section_prompt, detail_level, config=None)`

Extracts a specific section from a medical paper using a targeted LLM prompt.

| Parameter | Type | Description |
|---|---|---|
| `paper_text` | `str` | Full text of the research paper |
| `section_key` | `str` | Identifier for the section (e.g., `"methodology"`) |
| `section_prompt` | `str` | Custom prompt guiding extraction for this section |
| `detail_level` | `str` | One of `"brief"`, `"standard"`, `"comprehensive"` |
| `config` | `dict \| None` | Optional configuration override |

**Returns:** `str` — Extracted and summarized section text.

---

### `summarize_paper(paper_text, detail_level="standard", config=None)`

Produces a structured 8-section summary of a medical research paper.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `paper_text` | `str` | — | Full text of the research paper |
| `detail_level` | `str` | `"standard"` | `"brief"`, `"standard"`, or `"comprehensive"` |
| `config` | `dict \| None` | `None` | Optional configuration override |

**Returns:** `dict` with 8 keys:

| Key | Content |
|---|---|
| `title_authors` | Paper title, author list, affiliations, journal, year |
| `abstract_summary` | Condensed abstract with study purpose and main findings |
| `methodology` | Study design, population, procedures, measurements |
| `key_findings` | Primary and secondary outcomes, notable observations |
| `statistical_results` | P-values, confidence intervals, effect sizes, odds ratios |
| `conclusions` | Authors' conclusions and clinical implications |
| `limitations` | Study limitations, potential biases, generalizability issues |
| `future_work` | Suggested follow-up studies and open research questions |

---

### `extract_pico(paper_text, config=None)`

Extracts the PICO (Population, Intervention, Comparison, Outcome) framework
components from a clinical research paper.

| Parameter | Type | Description |
|---|---|---|
| `paper_text` | `str` | Full text of the research paper |
| `config` | `dict \| None` | Optional configuration override |

**Returns:** `dict` with keys `population`, `intervention`, `comparison`, `outcome`.

---

### `rate_evidence_quality(paper_text, config=None)`

Rates the evidence quality of a medical paper across 6 dimensions on a 1–5 scale
and assigns an overall Oxford CEBM evidence level.

| Parameter | Type | Description |
|---|---|---|
| `paper_text` | `str` | Full text of the research paper |
| `config` | `dict \| None` | Optional configuration override |

**Returns:** `dict` with:

| Key | Type | Description |
|---|---|---|
| `study_design` | `dict` | `{"rating": int, "notes": str}` |
| `sample_size` | `dict` | `{"rating": int, "notes": str}` |
| `methodology_rigor` | `dict` | `{"rating": int, "notes": str}` |
| `statistical_analysis` | `dict` | `{"rating": int, "notes": str}` |
| `bias_risk` | `dict` | `{"rating": int, "notes": str}` |
| `overall_evidence_level` | `str` | Oxford CEBM level (`"1a"` through `"5"`) |

---

### `format_citation(paper_text, style="APA", config=None)`

Generates a formatted citation string from a research paper.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `paper_text` | `str` | — | Full text of the research paper |
| `style` | `str` | `"APA"` | `"APA"`, `"MLA"`, `"Chicago"`, or `"Vancouver"` |
| `config` | `dict \| None` | `None` | Optional configuration override |

**Returns:** `str` — Formatted citation.

---

## 📊 Detail Levels

The `detail_level` parameter controls the granularity of extraction across all sections:

| Level | Use Case | Output Length | Best For |
|---|---|---|---|
| `brief` | Quick screening | ~50–100 words per section | Triaging large paper sets, initial relevance checks |
| `standard` | Regular review | ~150–300 words per section | Day-to-day literature review, journal club prep |
| `comprehensive` | Deep analysis | ~400–800 words per section | Systematic reviews, grant writing, detailed critique |

```bash
# Quick screening of multiple papers
for paper in papers/*.txt; do
    echo "=== $paper ==="
    python -m medical_summarizer.cli summarize --paper "$paper" --detail brief
done
```

---

## 🏅 Evidence Grading System

Evidence quality is assessed using a framework inspired by the
[Oxford Centre for Evidence-Based Medicine (CEBM)](https://www.cebm.ox.ac.uk/resources/levels-of-evidence/oxford-centre-for-evidence-based-medicine-levels-of-evidence-march-2009)
levels of evidence.

### 6 Rating Dimensions (1–5 scale)

| Dimension | What It Measures | Example Scoring |
|---|---|---|
| **Study Design** | Type of study (RCT, cohort, case-control, etc.) | 5 = SR of RCTs, 4 = RCT, 3 = Cohort, 2 = Case-control, 1 = Case report |
| **Sample Size** | Statistical power and participant count | 5 = >1000, 4 = 500–1000, 3 = 100–500, 2 = 30–100, 1 = <30 |
| **Methodology Rigor** | Randomization, blinding, control groups | 5 = Double-blind + ITT, 4 = Single-blind, 3 = Open-label, 2 = No control |
| **Statistical Analysis** | Appropriateness of tests, pre-registration | 5 = Pre-registered + multiple corrections, 3 = Standard tests, 1 = Descriptive only |
| **Bias Risk** | Funding, conflicts, selection bias | 5 = Independent + multi-center, 3 = Single-center, 1 = Major conflicts |

### Oxford CEBM Overall Levels

| Level | Study Type |
|---|---|
| **1a** | Systematic review of randomized controlled trials |
| **1b** | Individual randomized controlled trial |
| **2a** | Systematic review of cohort studies |
| **2b** | Individual cohort study |
| **3a** | Systematic review of case-control studies |
| **3b** | Individual case-control study |
| **4** | Case series, poor-quality cohort/case-control |
| **5** | Expert opinion without critical appraisal |

---

## 🎯 PICO Framework

The [PICO framework](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6148624/) is the
standard method for formulating clinical questions in evidence-based medicine:

| Component | Definition | Example |
|---|---|---|
| **P** — Population | Who was studied? Demographics, conditions, inclusion/exclusion criteria | Adults aged 40–65 with Type 2 Diabetes, HbA1c >7.5% |
| **I** — Intervention | What treatment, exposure, or action was applied? | Drug X 10mg orally once daily for 12 weeks |
| **C** — Comparison | What was the control or alternative? | Placebo matched for appearance and dose schedule |
| **O** — Outcome | What was measured? Primary and secondary endpoints | Change in HbA1c from baseline at 12 weeks |

Use `extract_pico()` or the `pico` CLI command to automatically extract these
components from any clinical research paper.

---

## 📝 Citation Formats

### APA 7th Edition

```
Smith, J. A., & Doe, R. B. (2024). Efficacy of Drug X in glycemic control
    among adults with Type 2 Diabetes: A randomized controlled trial.
    Journal of Clinical Endocrinology, 109(3), 456-471.
    https://doi.org/10.xxxx/jce.2024.xxxxx
```

### MLA 9th Edition

```
Smith, John A., and Robert B. Doe. "Efficacy of Drug X in Glycemic Control
    Among Adults with Type 2 Diabetes: A Randomized Controlled Trial."
    Journal of Clinical Endocrinology, vol. 109, no. 3, 2024, pp. 456-471.
```

### Chicago 17th Edition

```
Smith, John A., and Robert B. Doe. "Efficacy of Drug X in Glycemic Control
    Among Adults with Type 2 Diabetes: A Randomized Controlled Trial."
    Journal of Clinical Endocrinology 109, no. 3 (2024): 456-471.
```

### Vancouver (ICMJE)

```
Smith JA, Doe RB. Efficacy of Drug X in glycemic control among adults with
    Type 2 Diabetes: a randomized controlled trial. J Clin Endocrinol.
    2024;109(3):456-71.
```

---

## 🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run only core function tests
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v

# Run with coverage
python -m pytest tests/ -v --cov=src/medical_summarizer --cov-report=term-missing
```

---

## 🛠 Makefile Commands

```bash
make install        # Install dependencies from requirements.txt
make test           # Run pytest with verbose output
make lint           # Run linter checks
make run            # Launch CLI with default options
make web            # Start Streamlit web UI
make clean          # Remove __pycache__ and .pytest_cache
```

---

## ❓ Frequently Asked Questions

### Is this tool a substitute for clinical judgment?

**No.** Medical Literature Summarizer is a productivity tool for researchers and clinicians.
It accelerates the mechanical aspects of literature review — extraction, grading, formatting —
but all outputs should be verified by a qualified professional. The LLM can misinterpret
statistical nuances or miss context that a domain expert would catch.

### How accurate is the evidence grading?

The evidence grading uses structured prompts aligned with the Oxford CEBM framework, but the
ratings are LLM-generated approximations. For formal systematic reviews or clinical guidelines,
use validated tools like the Cochrane Risk of Bias tool or GRADE alongside this tool. Think of
the output as a **first-pass triage** rather than a definitive assessment.

### Does this tool handle HIPAA-protected data?

Because all processing runs **locally** through Ollama, no data is transmitted to external
servers. However, this tool is not certified as HIPAA-compliant software. If you are processing
papers that contain protected health information (PHI), ensure your local environment meets
your organization's security requirements. The tool itself does not store, log, or transmit
any input data beyond the current session.

### What types of papers work best?

The tool works best with:

- **Randomized controlled trials (RCTs)** — strongest PICO and evidence extraction
- **Cohort and case-control studies** — good structured extraction
- **Systematic reviews and meta-analyses** — excellent summary extraction

It can process any medical text, but extraction quality naturally varies with paper structure.
Narrative reviews and editorials produce less structured output.

### Can I use a different LLM instead of Gemma 4?

Yes. Update the `model` field in `config.yaml` to any model available in your Ollama instance:

```yaml
llm:
  model: "llama3.1"    # or mistral, phi3, etc.
```

Gemma 4 is recommended because it handles medical terminology and structured extraction well
at its parameter size, but any instruction-tuned model should work.

### What is the Oxford CEBM scale?

The Oxford Centre for Evidence-Based Medicine levels of evidence rank study types by their
susceptibility to bias:

- **Level 1** (highest): Systematic reviews of RCTs (1a) and individual RCTs (1b)
- **Level 2**: Systematic reviews of cohort studies (2a) and individual cohort studies (2b)
- **Level 3**: Case-control studies
- **Level 4**: Case series
- **Level 5** (lowest): Expert opinion

This hierarchy helps clinicians quickly assess how much weight to give a study's conclusions.

### How long does analysis take?

Typical processing times with Gemma 4 on consumer hardware:

| Operation | Time (approx.) |
|---|---|
| `summarize_paper` (standard) | 30–60 seconds |
| `extract_pico` | 10–20 seconds |
| `rate_evidence_quality` | 15–25 seconds |
| `format_citation` | 5–10 seconds |

Times vary with paper length, detail level, and hardware (GPU vs. CPU inference).

---

## 🔧 Troubleshooting

### Ollama connection refused

```
Error: Could not connect to Ollama at http://localhost:11434
```

**Fix:** Ensure Ollama is running:

```bash
ollama serve
```

### Model not found

```
Error: model "gemma4" not found
```

**Fix:** Pull the model:

```bash
ollama pull gemma4
```

### Slow inference

If analysis is taking several minutes per section:

- Ensure you have GPU acceleration enabled in Ollama
- Use `brief` detail level for faster results
- Check that no other processes are consuming GPU memory

### Empty or poor-quality output

- Verify the input text is clean and contains actual paper content (not just references or headers)
- Try `comprehensive` detail level for more thorough extraction
- Ensure the paper text is in English (other languages may produce lower quality results)

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and add tests
4. Run the test suite: `python -m pytest tests/ -v`
5. Submit a pull request

Please ensure all tests pass before submitting.

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

Built with [Ollama](https://ollama.com) · [Click](https://click.palletsprojects.com/) · [Rich](https://rich.readthedocs.io/) · [Streamlit](https://streamlit.io)

</div>
