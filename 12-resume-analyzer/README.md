<div align="center">

<img src="docs/images/banner.svg" alt="Resume Analyzer Banner" width="800"/>

<br/><br/>

<img src="https://img.shields.io/badge/Gemma_4-Local_LLM-E8710A?style=for-the-badge&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Ollama-Inference-00b4d8?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/>
<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+"/>
<img src="https://img.shields.io/badge/100%25-Private-533483?style=for-the-badge&logo=lock&logoColor=white" alt="100% Private"/>

<br/>

<img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/Click-CLI-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/pytest-Tests-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="pytest"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT License"/>
<img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/><br/>

**[Features](#-features)** · **[Quick Start](#-quick-start)** · **[CLI Reference](#-cli-reference)** · **[Web UI](#-web-ui)** · **[API Reference](#-api-reference)** · **[Architecture](#-architecture)** · **[FAQ](#-faq)**

<br/>

*Production-grade resume analysis toolkit with ATS score simulation, keyword gap analysis,*
*multi-resume comparison, and actionable improvement suggestions — all powered by a local LLM via Ollama.*

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

---

## 🤔 Why This Project?

> Resumes are the first impression — but most people have no idea how theirs actually performs.

| The Problem | Our Solution |
|:---|:---|
| Hiring managers spend **6 seconds** scanning a resume | AI gives a **detailed 0–100 score** with breakdown |
| ATS systems silently reject **75%** of resumes | **ATS simulation** reveals exactly why you'd be filtered out |
| Applicants guess which keywords matter | **Keyword gap analysis** shows precisely what's missing |
| Cloud resume tools **harvest your data** | **100% local** — your resume never leaves your machine |
| Comparing candidates is manual and biased | **Side-by-side comparison** with objective ranking |

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

<table>
<tr>
<td width="50%">

### 📊 Resume Analysis
Deep analysis returning skills extraction, experience summary, education details, achievements, strengths, weaknesses, and an **overall score (0–100)** with formatting and content suggestions.

### 🤖 ATS Simulation
Simulates Applicant Tracking System scoring across **5 dimensions**: keyword match, experience alignment, education fit, formatting compliance — each scored 0–100.

### ⚖️ Multi-Resume Compare
Compare multiple candidates side-by-side with objective ranking, comparison tables, key differences, and a final recommendation. Optionally score against a JD.

</td>
<td width="50%">

### 🎯 JD Matching
Scores your resume against a specific job description. Returns **match percentage**, matching/missing skills, experience alignment, keyword gaps, and priority improvements.

### 💡 Improvement Engine
Section-by-section improvement suggestions covering summary, experience, skills, and education. Recommends **power words** to add and **sections** your resume is missing.

### 🔒 100% Private
All processing happens locally via Ollama. Zero cloud API calls, zero data collection, zero tracking. Your resume and career data **never leave your machine**.

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:---|:---|:---|
| [Python](https://python.org) | 3.11+ | Runtime |
| [Ollama](https://ollama.com) | Latest | Local LLM inference |
| [Gemma 4](https://ollama.com/library/gemma4) | Latest | Language model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/resume-analyzer.git
cd resume-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama and pull the model
ollama serve
ollama pull gemma4

# 4. (Optional) Install as a package
pip install -e .
```

### Your First Analysis

```bash
# Analyze a resume
python -m src.resume_analyzer.cli analyze --resume my_resume.txt

# Score against a job description
python -m src.resume_analyzer.cli score --resume my_resume.txt --jd job_posting.txt

# Simulate ATS scoring
python -m src.resume_analyzer.cli ats --resume my_resume.txt --jd job_posting.txt

# Get improvement suggestions
python -m src.resume_analyzer.cli improve --resume my_resume.txt

# Use verbose mode for debug output
python -m src.resume_analyzer.cli -v analyze --resume my_resume.txt

# Use a custom config file
python -m src.resume_analyzer.cli --config custom_config.yaml analyze --resume my_resume.txt
```

<details>
<summary><strong>📋 Example Output — Resume Analysis</strong></summary>

```
╭─────────────────────────────────────────────────────╮
│              📊 Resume Analysis Report              │
╰─────────────────────────────────────────────────────╯

  Overall Score: 72/100

  ┌─────────────────┬────────────────────────────────┐
  │ Category        │ Details                        │
  ├─────────────────┼────────────────────────────────┤
  │ Skills          │ Python, SQL, AWS, Docker,      │
  │                 │ Machine Learning, REST APIs    │
  │ Experience      │ 4 years — Backend & ML         │
  │ Education       │ B.S. Computer Science          │
  │ Achievements    │ 3 quantified accomplishments   │
  ├─────────────────┼────────────────────────────────┤
  │ Strengths       │ Strong technical skills,       │
  │                 │ quantified impact metrics      │
  │ Weaknesses      │ Missing summary section,       │
  │                 │ no leadership examples         │
  └─────────────────┴────────────────────────────────┘

  Formatting Suggestions:
    • Add a professional summary at the top
    • Use consistent date formatting (MMM YYYY)
    • Add 2-3 more quantified achievements

  Content Suggestions:
    • Include leadership or mentoring examples
    • Add relevant certifications section
    • Expand project descriptions with impact metrics
```

</details>

<details>
<summary><strong>📋 Example Output — ATS Simulation</strong></summary>

```
╭─────────────────────────────────────────────────────╮
│            🤖 ATS Score Simulation                  │
╰─────────────────────────────────────────────────────╯

  ATS Score: 61/100

  ┌──────────────────────┬────────────┐
  │ Dimension            │ Score      │
  ├──────────────────────┼────────────┤
  │ Keyword Match        │ 55/100     │
  │ Experience Match     │ 70/100     │
  │ Education Match      │ 80/100     │
  │ Formatting           │ 45/100     │
  └──────────────────────┴────────────┘

  Matched Keywords: Python, REST API, SQL, Docker
  Missing Keywords: GraphQL, Redis, Kubernetes, Terraform

  Formatting Issues:
    ⚠ Inconsistent date format across sections
    ⚠ Non-standard section headers detected
    ⚠ Missing bullet point consistency

  Recommendations:
    • Use standard headers: "Experience", "Education", "Skills"
    • Standardize dates to "MMM YYYY" format
    • Add missing keywords naturally in context
```

</details>

<details>
<summary><strong>📋 Example Output — JD Matching</strong></summary>

```
╭─────────────────────────────────────────────────────╮
│            🎯 Job Description Match                 │
╰─────────────────────────────────────────────────────╯

  Match Percentage: 68/100

  ┌─────────────────┬────────────────────────────────┐
  │ Category        │ Details                        │
  ├─────────────────┼────────────────────────────────┤
  │ Matching Skills │ Python, AWS, Docker, SQL       │
  │ Missing Skills  │ Kubernetes, Terraform, Go      │
  │ Keyword Gaps    │ CI/CD, microservices, agile    │
  │ Experience      │ Partially aligned              │
  └─────────────────┴────────────────────────────────┘

  Priority Improvements:
    1. Add Kubernetes experience or personal project
    2. Mention CI/CD pipeline contributions
    3. Highlight microservices architecture work
```

</details>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/resume-analyzer.git
cd resume-analyzer
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
uvicorn src.resume_analyzer.api:app --reload --port 8000

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

## 📋 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output.

### Global Options

| Option | Short | Description |
|:---|:---|:---|
| `--verbose` | `-v` | Enable verbose output with debug information |
| `--config` | | Path to custom configuration file (default: `config.yaml`) |

---

### `analyze` — General Resume Analysis

Performs a comprehensive analysis of a resume, returning skills, experience, education, strengths, weaknesses, and an overall score.

```bash
python -m src.resume_analyzer.cli analyze --resume <file>
```

| Option | Required | Description |
|:---|:---|:---|
| `--resume` | ✅ Yes | Path to the resume text file |

**Returns:** `skills`, `experience_summary`, `education`, `achievements`, `strengths`, `weaknesses`, `formatting_suggestions`, `content_suggestions`, `overall_score` (0–100)

---

### `score` — Score Against Job Description

Compares a resume against a specific job description and identifies skill gaps.

```bash
python -m src.resume_analyzer.cli score --resume <file> --jd <file>
```

| Option | Required | Description |
|:---|:---|:---|
| `--resume` | ✅ Yes | Path to the resume text file |
| `--jd` | ✅ Yes | Path to the job description text file |

**Returns:** `match_percentage` (0–100), `matching_skills`, `missing_skills`, `experience_alignment`, `suggestions`, `keyword_gaps`, `overall_assessment`, `priority_improvements`

---

### `ats` — ATS Score Simulation

Simulates how an Applicant Tracking System would score the resume against a job description.

```bash
python -m src.resume_analyzer.cli ats --resume <file> --jd <file>
```

| Option | Required | Description |
|:---|:---|:---|
| `--resume` | ✅ Yes | Path to the resume text file |
| `--jd` | ✅ Yes | Path to the job description text file |

**Returns:** `ats_score` (0–100) with sub-scores — `keyword_match_score`, `experience_match_score`, `education_match_score`, `formatting_score` (each 0–100), plus `matched_keywords`, `missing_keywords`, `formatting_issues`, `recommendations`

---

### `improve` — Generate Improvement Suggestions

Generates detailed, section-by-section improvement suggestions for a resume.

```bash
python -m src.resume_analyzer.cli improve --resume <file>
```

| Option | Required | Description |
|:---|:---|:---|
| `--resume` | ✅ Yes | Path to the resume text file |

**Returns:** Section improvements for `summary`, `experience`, `skills`, `education`, plus `power_words_to_add`, `sections_to_add`

---

### CLI Examples Cheat Sheet

```bash
# Basic analysis
python -m src.resume_analyzer.cli analyze --resume resume.txt

# Score against JD with verbose output
python -m src.resume_analyzer.cli -v score --resume resume.txt --jd senior_backend.txt

# ATS simulation with custom config
python -m src.resume_analyzer.cli --config ats_strict.yaml ats --resume resume.txt --jd job.txt

# Quick improvement check
python -m src.resume_analyzer.cli improve --resume resume.txt

# Using the installed package (after pip install -e .)
resume-analyzer analyze --resume resume.txt
resume-analyzer score --resume resume.txt --jd job.txt
resume-analyzer ats --resume resume.txt --jd job.txt
resume-analyzer improve --resume resume.txt
```

---

## 🌐 Web UI

Launch the Streamlit-powered web interface for a visual, interactive experience:

```bash
streamlit run src/resume_analyzer/web_ui.py
```

**Web UI Features:**

- 📤 **Resume Upload** — Drag-and-drop or paste resume text
- 📝 **Job Description Input** — Paste JD for matching and ATS simulation
- 📊 **Score Dashboard** — Visual gauges and breakdowns for all scores
- 💡 **Suggestions Panel** — Actionable improvement recommendations
- ⚖️ **Multi-Resume Comparison** — Upload multiple resumes for side-by-side ranking
- 🎨 **Rich Visualizations** — Charts, tables, and color-coded results

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="System Architecture" width="800"/>
</div>

<br/>

### Project Structure

```
12-resume-analyzer/
├── src/
│   └── resume_analyzer/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Core analysis functions (5 main functions)
│       ├── cli.py               # Click CLI interface (4 commands)
│       ├── web_ui.py            # Streamlit web interface
│       ├── config.py            # Configuration loader (YAML + env)
│       └── utils.py             # Shared utilities & helpers
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core function tests
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # README banner graphic
│       ├── architecture.svg     # System architecture diagram
│       └── features.svg         # Feature overview graphic
├── common/                      # Shared utilities across projects
├── config.yaml                  # Default configuration
├── .env.example                 # Environment variable template
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup (pip install -e .)
├── Makefile                     # Development shortcuts
└── README.md                   # This file
```

### How It Works

```
1. INPUT         User provides resume text (+ optional JD)
                      │
2. INTERFACE     CLI (Click) or Web UI (Streamlit) parses input
                      │
3. CORE          core.py builds structured prompts for the LLM
                      │
4. LLM           Gemma 4 via Ollama (localhost:11434) processes prompts
                      │
5. PARSE         JSON response is extracted and validated
                      │
6. OUTPUT        Rich tables (CLI) or Streamlit dashboard (Web)
```

---

## 🔌 API Reference

Use the core functions directly in your Python code:

### `analyze_resume`

```python
from resume_analyzer.core import analyze_resume

result = analyze_resume(resume_text, config=None)

# result = {
#     "skills": ["Python", "SQL", "AWS", ...],
#     "experience_summary": "4 years in backend development...",
#     "education": "B.S. Computer Science, ...",
#     "achievements": ["Reduced latency by 40%", ...],
#     "strengths": ["Strong technical depth", ...],
#     "weaknesses": ["No leadership examples", ...],
#     "formatting_suggestions": ["Add professional summary", ...],
#     "content_suggestions": ["Include certifications", ...],
#     "overall_score": 72
# }
```

### `score_against_jd`

```python
from resume_analyzer.core import score_against_jd

result = score_against_jd(resume_text, jd_text, config=None)

# result = {
#     "match_percentage": 68,
#     "matching_skills": ["Python", "AWS", "Docker"],
#     "missing_skills": ["Kubernetes", "Terraform"],
#     "experience_alignment": "Partially aligned — ...",
#     "suggestions": ["Add cloud infrastructure experience", ...],
#     "keyword_gaps": ["CI/CD", "microservices"],
#     "overall_assessment": "Good fit with gaps in...",
#     "priority_improvements": ["Add Kubernetes project", ...]
# }
```

### `simulate_ats_score`

```python
from resume_analyzer.core import simulate_ats_score

result = simulate_ats_score(resume_text, jd_text, config=None)

# result = {
#     "ats_score": 61,
#     "keyword_match_score": 55,
#     "experience_match_score": 70,
#     "education_match_score": 80,
#     "formatting_score": 45,
#     "matched_keywords": ["Python", "REST API", ...],
#     "missing_keywords": ["GraphQL", "Redis", ...],
#     "formatting_issues": ["Inconsistent date format", ...],
#     "recommendations": ["Use standard section headers", ...]
# }
```

### `compare_resumes`

```python
from resume_analyzer.core import compare_resumes

resume_texts = [
    ("Alice", "Alice's resume text..."),
    ("Bob", "Bob's resume text..."),
    ("Carol", "Carol's resume text..."),
]

result = compare_resumes(resume_texts, jd_text=None, config=None)

# result = {
#     "ranking": [{"name": "Alice", "score": 82}, ...],
#     "comparison_table": {...},
#     "recommendation": "Alice is the strongest candidate...",
#     "key_differences": ["Alice has more leadership...", ...]
# }
```

### `generate_improvement_suggestions`

```python
from resume_analyzer.core import generate_improvement_suggestions

result = generate_improvement_suggestions(resume_text, config=None)

# result = {
#     "summary": "Add a 2-3 sentence professional summary...",
#     "experience": "Quantify achievements with metrics...",
#     "skills": "Group skills by category...",
#     "education": "Add relevant coursework...",
#     "power_words_to_add": ["Spearheaded", "Orchestrated", ...],
#     "sections_to_add": ["Certifications", "Projects", ...]
# }
```

---

## 📦 Dependencies

| Package | Purpose |
|:---|:---|
| `requests` | HTTP client for Ollama API communication |
| `rich` | Beautiful terminal output with tables, panels, and colors |
| `click` | CLI framework with argument parsing and help generation |
| `pyyaml` | YAML configuration file parsing |
| `streamlit` | Interactive web UI framework |
| `python-dotenv` | Environment variable loading from `.env` files |
| `pytest` | Testing framework (dev dependency) |
| `pytest-cov` | Coverage reporting (dev dependency) |

---

## ⚙️ Configuration

### Configuration File (`config.yaml`)

```yaml
# Resume Analyzer Configuration
llm:
  model: "gemma4"           # Ollama model name
  temperature: 0.3          # Lower = more deterministic
  max_tokens: 4096          # Maximum response length

ats:
  keyword_weight: 0.4       # Weight for keyword matching
  experience_weight: 0.3    # Weight for experience alignment
  education_weight: 0.15    # Weight for education matching
  formatting_weight: 0.15   # Weight for formatting quality

output:
  default_format: "rich"    # Output format: "rich" or "json"
```

### Environment Variables (`.env`)

```bash
RESUME_ANALYZER_MODEL=gemma4           # Override model name
RESUME_ANALYZER_TEMPERATURE=0.3        # Override temperature
OLLAMA_BASE_URL=http://localhost:11434  # Ollama server URL
```

> **Priority:** Environment variables override `config.yaml` values. CLI `--config` flag overrides both.

---

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/resume_analyzer --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_core.py -v
python -m pytest tests/test_cli.py -v

# Using Makefile shortcuts
make test          # Run tests
make test-cov      # Run with coverage
```

### Test Structure

| File | What It Tests |
|:---|:---|
| `tests/test_core.py` | Core analysis functions — `analyze_resume`, `score_against_jd`, `simulate_ats_score`, `compare_resumes`, `generate_improvement_suggestions` |
| `tests/test_cli.py` | CLI commands — argument parsing, output formatting, error handling |

### Makefile Commands

| Command | Description |
|:---|:---|
| `make install` | Install production dependencies |
| `make install-dev` | Install with dev dependencies (pytest, coverage) |
| `make test` | Run all tests with verbose output |
| `make test-cov` | Run tests with coverage report |
| `make run-cli ARGS="..."` | Run CLI with arguments (e.g., `ARGS="analyze --resume r.txt"`) |
| `make run-web` | Launch Streamlit web UI |
| `make clean` | Remove `__pycache__` and `.pytest_cache` directories |

---

## 🏠 Local vs. Cloud

| Feature | Resume Analyzer (Local) | Cloud Services |
|:---|:---|:---|
| **Privacy** | ✅ 100% local — data never leaves your machine | ❌ Data uploaded to third-party servers |
| **Cost** | ✅ Free forever (after hardware) | ❌ Per-use or subscription fees |
| **Speed** | ✅ No network latency | ❌ Depends on internet & server load |
| **Customization** | ✅ Full control over model & prompts | ❌ Limited to provider's API |
| **Offline** | ✅ Works without internet | ❌ Requires constant connection |
| **Model Choice** | ✅ Swap models freely via Ollama | ❌ Locked to provider's models |
| **Data Retention** | ✅ Nothing stored unless you save it | ❌ May retain data for training |

---

## ❓ FAQ

<details>
<summary><strong>What resume formats are supported?</strong></summary>

Currently, the tool accepts **plain text (`.txt`)** input. You can paste resume text directly or provide a file path. For PDF or DOCX resumes, convert them to text first using tools like `pdftotext` or paste the content directly into the Web UI.

</details>

<details>
<summary><strong>Which Ollama models work besides Gemma 4?</strong></summary>

Any Ollama-compatible model works. Update `config.yaml` or set the `RESUME_ANALYZER_MODEL` environment variable. Popular alternatives: `llama3.1`, `mistral`, `phi3`, `qwen2`. Gemma 4 is recommended for the best balance of quality and speed.

</details>

<details>
<summary><strong>How accurate is the ATS simulation?</strong></summary>

The ATS simulation approximates how real ATS systems (Taleo, Workday, Greenhouse) parse and score resumes. It checks keyword matching, formatting compliance, and section structure. While not identical to any specific ATS, it identifies the same issues that cause real rejections — missing keywords, poor formatting, and content gaps.

</details>

<details>
<summary><strong>Can I compare more than 2 resumes at once?</strong></summary>

Yes! The `compare_resumes` function accepts a list of `(name, text)` tuples, so you can compare as many candidates as needed. Each resume is analyzed individually, then compared side-by-side with ranking and recommendations.

</details>

<details>
<summary><strong>How much RAM / GPU does this need?</strong></summary>

Gemma 4 via Ollama typically requires **8–16 GB RAM** (CPU inference) or **6+ GB VRAM** (GPU inference). The resume analyzer itself uses minimal memory. For lower-resource machines, try smaller models like `gemma2:2b` or `phi3:mini`.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork and clone
git clone https://github.com/<your-username>/resume-analyzer.git
cd resume-analyzer

# 2. Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make changes and run tests
python -m pytest tests/ -v

# 5. Submit a pull request
```

**Guidelines:**
- Follow existing code style and patterns
- Add tests for new features
- Update documentation for API changes
- Keep PRs focused on a single feature or fix

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

<br/>

**📋 Resume Analyzer** — AI-powered career optimization, 100% private.

Built with ❤️ as part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

<br/>

<img src="https://img.shields.io/badge/Powered_by-Gemma_4-E8710A?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Runs_on-Ollama-00b4d8?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"/>
<img src="https://img.shields.io/badge/Made_with-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>

<br/><br/>

⭐ **Star this repo** if you found it useful! ⭐

</div>
