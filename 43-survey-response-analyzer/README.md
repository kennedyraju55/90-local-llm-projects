<div align="center">

<img src="docs/images/banner.svg" alt="Survey Response Analyzer Banner" width="800" />

<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma_3-ff6f00?style=for-the-badge&logo=google&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-2ec4b6?style=for-the-badge)](LICENSE)
[![Click CLI](https://img.shields.io/badge/Click-CLI-4caf50?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)

[![GitHub stars](https://img.shields.io/github/stars/kennedyraju55/survey-response-analyzer?style=flat-square&color=2ec4b6)](https://github.com/kennedyraju55/survey-response-analyzer/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/kennedyraju55/survey-response-analyzer?style=flat-square&color=30363d)](https://github.com/kennedyraju55/survey-response-analyzer/network)
[![GitHub issues](https://img.shields.io/github/issues/kennedyraju55/survey-response-analyzer?style=flat-square&color=d73a49)](https://github.com/kennedyraju55/survey-response-analyzer/issues)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-2ec4b6.svg?style=flat-square)](https://github.com/kennedyraju55/survey-response-analyzer/pulls)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

**Extract themes, insights, and actionable recommendations from survey data — 100% local, powered by Ollama**

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection (#43)</strong>

<br/>

[Features](#-features) · [Quick Start](#-quick-start) · [CLI Usage](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [FAQ](#-faq) · [Contributing](#-contributing)

</div>

---

## 🤔 Why Survey Response Analyzer?

| Challenge | Without This Tool | With Survey Response Analyzer |
|-----------|-------------------|-------------------------------|
| **Reading 500+ responses** | Hours of manual reading | Automated theme extraction in seconds |
| **Identifying patterns** | Subjective and inconsistent | LLM-powered consistent theme discovery |
| **Demographic insights** | Requires pivot tables in Excel | Automatic cross-tabulation by any column |
| **Finding key quotes** | Scrolling through spreadsheets | Impact-scored verbatim highlighting |
| **Making recommendations** | Gut feeling and guesswork | Data-driven priority/effort/impact matrix |
| **Privacy concerns** | Cloud APIs see your data | 100% local — data never leaves your machine |

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800" />
</div>

<br/>

### 🔍 Smart Column Detection

Automatically distinguishes free-text response columns from categorical/demographic columns. Uses average character length heuristics (>20 chars = text) and keyword matching for demographics (`age`, `gender`, `department`, `location`, `role`, `region`, `country`, `group`).

```python
text_cols = identify_text_columns(data)       # ["feedback", "comments", "suggestions"]
demo_cols = identify_demographic_columns(data) # ["age_group", "department", "gender"]
```

### 🎯 Theme Extraction

LLM-powered theme discovery analyzes up to 50 responses and returns structured JSON with:
- **Theme name** and estimated response count
- **Sentiment label** — `positive`, `negative`, or `mixed`
- **Description** of the theme
- **Representative quotes** from actual responses

### 🏗️ Theme Clustering

Groups related themes into higher-level clusters for executive-level reporting. Each cluster includes:
- Grouped theme names
- Overall sentiment assessment
- Priority ranking (`high` / `medium` / `low`)

### 📊 Demographic Cross-tabulation

Cross-tabulate themes by any demographic column to reveal group-level patterns:
- Response counts per demographic group
- Average response length per group
- Identify which groups feel most strongly about each topic

### 📌 Verbatim Highlighting

Surface the 5–8 most impactful quotes from survey responses with:
- **Theme tag** linking the quote to a discovered theme
- **Impact score** — `high` or `medium`
- **Reason** explaining why the quote is notable

### 💡 Actionable Recommendations

Generate 5–7 strategic recommendations based on the full analysis:
- **Priority** — `high` / `medium` / `low`
- **Effort** — `low` / `medium` / `high`
- **Expected impact** — description of anticipated outcomes

### 📈 Visual Insights Report

Generate a comprehensive markdown insights report including:
- Executive summary
- Key findings
- Theme-by-theme analysis
- Actionable recommendations

### 🖥️ Streamlit Web Dashboard

Interactive web interface with:
- CSV file uploader with column selector
- Theme cards with counts, sentiment, and representative quotes
- Theme distribution bar chart
- Recommendations panel with priority/effort/impact
- Notable verbatim quotes viewer

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.10+ | Runtime |
| **Ollama** | Latest | Local LLM inference |
| **gemma3:4b** | Latest | Language model for analysis |

### 1. Install Ollama & Pull Model

```bash
# Install Ollama (https://ollama.ai)
# Then pull the model:
ollama pull gemma3:4b
```

### 2. Clone & Install

```bash
git clone https://github.com/kennedyraju55/survey-response-analyzer.git
cd survey-response-analyzer

# Install dependencies
pip install -r requirements.txt

# Or install as editable package
pip install -e .
```

### 3. Run Your First Analysis

```bash
python -m src.survey_analyzer.cli --file survey.csv
```

### Expected Output

```
╭──────────────────────────────────────╮
│  📋 Survey Response Analyzer         │
╰──────────────────────────────────────╯
✓ Loaded 247 responses from survey.csv

Analyzing columns: feedback, comments

Column: feedback (247 responses)

┌────┬──────────────────────┬───────────┬───────────┬──────────────────────────────────┐
│ #  │ Theme                │ Responses │ Sentiment │ Description                      │
├────┼──────────────────────┼───────────┼───────────┼──────────────────────────────────┤
│ 1  │ Work-Life Balance    │ 62        │ Negative  │ Employees report excessive       │
│    │                      │           │           │ overtime and burnout concerns     │
├────┼──────────────────────┼───────────┼───────────┼──────────────────────────────────┤
│ 2  │ Career Growth        │ 45        │ Mixed     │ Mixed feelings about promotion   │
│    │                      │           │           │ paths and learning opportunities  │
├────┼──────────────────────┼───────────┼───────────┼──────────────────────────────────┤
│ 3  │ Team Collaboration   │ 38        │ Positive  │ Strong appreciation for team     │
│    │                      │           │           │ culture and cross-team projects   │
└────┴──────────────────────┴───────────┴───────────┴──────────────────────────────────┘

💡 Recommendations
┌────┬────────────────────────┬──────────┬────────┬──────────────────────────────────┐
│ #  │ Title                  │ Priority │ Effort │ Description                      │
├────┼────────────────────────┼──────────┼────────┼──────────────────────────────────┤
│ 1  │ Flexible Work Policy   │ HIGH     │ Medium │ Implement hybrid work schedule   │
│ 2  │ Mentorship Program     │ MEDIUM   │ Low    │ Pair junior staff with seniors   │
│ 3  │ Recognition Framework  │ MEDIUM   │ Low    │ Quarterly team awards program    │
└────┴────────────────────────┴──────────┴────────┴──────────────────────────────────┘
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/survey-response-analyzer.git
cd survey-response-analyzer
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
uvicorn src.survey_analyzer.api:app --reload --port 8000

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

### Basic Usage

```bash
# Analyze all text columns automatically
python -m src.survey_analyzer.cli --file survey.csv

# Analyze a specific column
python -m src.survey_analyzer.cli --file survey.csv --column feedback

# Detailed report (includes executive summary & markdown insights)
python -m src.survey_analyzer.cli --file survey.csv --report detailed
```

### Full Feature Analysis

```bash
# Everything enabled: clusters + verbatims + recommendations + detailed report
python -m src.survey_analyzer.cli \
  --file survey.csv \
  --report detailed \
  --show-clusters \
  --show-verbatims \
  --show-recommendations \
  --verbose
```

### CLI Options Reference

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | `PATH` | *required* | Path to survey responses CSV file |
| `--report` | `-r` | `brief\|detailed` | `brief` | Report detail level. `detailed` adds executive summary and markdown insights |
| `--column` | `-c` | `TEXT` | *auto-detect* | Specific text column to analyze. If omitted, all text columns are analyzed |
| `--show-clusters` | | `flag` | `off` | Enable theme clustering into higher-level groups |
| `--no-clusters` | | `flag` | `on` | Disable theme clustering (default) |
| `--show-verbatims` | | `flag` | `off` | Show notable verbatim quotes with impact scoring |
| `--no-verbatims` | | `flag` | `on` | Hide verbatim quotes (default) |
| `--show-recommendations` | | `flag` | `on` | Show actionable recommendations (default) |
| `--no-recommendations` | | `flag` | `off` | Disable recommendation generation |
| `--verbose` | `-v` | `flag` | `off` | Enable verbose/debug logging |

### Usage Examples

```bash
# Quick theme scan (minimal output)
python -m src.survey_analyzer.cli -f data.csv --no-recommendations

# Focus on a single column with full analysis
python -m src.survey_analyzer.cli -f data.csv -c "open_feedback" --show-clusters --show-verbatims

# Verbose mode for debugging
python -m src.survey_analyzer.cli -f data.csv -v

# Using Make
make run FILE=survey.csv
```

---

## 🌐 Web UI

The Streamlit-based web dashboard provides an interactive point-and-click interface.

### Launch

```bash
# Direct launch
streamlit run src/survey_analyzer/web_ui.py

# Or via Makefile
make web
```

### Web UI Features

| Feature | Description |
|---------|-------------|
| 📁 **CSV Uploader** | Drag-and-drop or browse to upload survey CSV files |
| 🔍 **Column Selector** | Choose which text column to analyze from a dropdown |
| 🎯 **Theme Cards** | Visual cards showing theme name, count, sentiment badge, and quotes |
| 📊 **Distribution Chart** | Bar chart showing response count per theme |
| 📌 **Verbatim Viewer** | Expandable panels for notable quotes with impact indicators |
| 💡 **Recommendations** | Priority-ranked cards with effort and expected impact |
| 📈 **Sentiment Breakdown** | Per-theme sentiment visualization |

### Web UI Workflow

1. **Upload** your CSV file using the file uploader
2. **Select** the text column to analyze (auto-detected suggestions shown)
3. **Click Analyze** to run theme extraction
4. **Explore** themes, clusters, verbatims, and recommendations in the dashboard
5. **Export** the insights report as markdown

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800" />
</div>

<br/>

### Processing Pipeline

```
┌─────────────┐     ┌──────────────────┐     ┌──────────────────┐     ┌────────────────┐
│  Survey CSV  │────▶│ Column Detection  │────▶│ Text Extraction  │────▶│  Theme Engine   │
│  (Input)     │     │ Text vs Demo cols │     │ Free-text values │     │  (LLM-Powered)  │
└─────────────┘     └──────────────────┘     └──────────────────┘     └───────┬────────┘
                                                                              │
                    ┌──────────────────────────────────────────────────────────┘
                    │
          ┌─────────▼─────────┐  ┌─────────────────┐  ┌──────────────────┐  ┌───────────────┐
          │ Theme Clustering   │  │ Demo Crosstabs   │  │ Verbatim Scoring │  │ Recommendations│
          │ Higher-level groups│  │ Group analysis   │  │ Impact quotes    │  │ Priority/Effort│
          └─────────┬─────────┘  └────────┬────────┘  └────────┬─────────┘  └───────┬───────┘
                    │                     │                     │                    │
                    └─────────────────────┴─────────────────────┴────────────────────┘
                                                    │
                                          ┌─────────▼─────────┐
                                          │   Rich Report      │
                                          │ CLI · Web · Markdown│
                                          └────────────────────┘
```

### Project Structure

```
43-survey-response-analyzer/
├── src/
│   └── survey_analyzer/
│       ├── __init__.py          # Package metadata & version
│       ├── core.py              # Core analysis engine
│       │   ├── load_config()            # YAML configuration loader
│       │   ├── get_llm_client()         # Ollama LLM client setup
│       │   ├── load_survey_data()       # CSV parser (list of dicts)
│       │   ├── identify_text_columns()  # Free-text column detection
│       │   ├── identify_demographic_columns()  # Categorical column detection
│       │   ├── extract_themes()         # LLM theme extraction
│       │   ├── cluster_themes()         # Theme grouping
│       │   ├── compute_demographic_crosstabs()  # Group-level analysis
│       │   ├── highlight_verbatims()    # Impact-scored quotes
│       │   ├── generate_recommendations() # Strategic recommendations
│       │   └── generate_insights()      # Markdown insights report
│       ├── cli.py               # Click CLI with Rich display
│       │   ├── display_themes()         # Theme table renderer
│       │   ├── display_clusters()       # Cluster table renderer
│       │   ├── display_recommendations() # Recommendations table
│       │   ├── display_verbatims()      # Verbatim panels
│       │   └── main()                   # CLI entry point
│       └── web_ui.py            # Streamlit dashboard
├── tests/
│   ├── conftest.py              # Shared pytest fixtures
│   ├── test_core.py             # Core logic unit tests
│   └── test_cli.py              # CLI integration tests
├── common/                      # Shared LLM client (from parent project)
├── docs/
│   └── images/                  # SVG assets (banner, architecture, features)
├── config.yaml                  # Application configuration
├── setup.py                     # Package setup & entry points
├── Makefile                     # Development automation
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

---

## 📚 API Reference

### `load_survey_data(file_path: str) -> list[dict]`

Load survey responses from a CSV file into a list of dictionaries.

```python
from src.survey_analyzer.core import load_survey_data

data = load_survey_data("survey_results.csv")
# Returns: [{"id": "1", "feedback": "Great experience...", "age": "25-34"}, ...]
print(f"Loaded {len(data)} responses")
```

**Parameters:**
- `file_path` — Path to the CSV file

**Returns:** List of dictionaries, one per row

**Raises:** `FileNotFoundError` if file doesn't exist, `ValueError` if CSV is empty or malformed

---

### `identify_text_columns(data: list[dict]) -> list[str]`

Identify columns containing free-text responses by checking average character length.

```python
from src.survey_analyzer.core import identify_text_columns

text_cols = identify_text_columns(data)
# Returns: ["feedback", "comments", "suggestions"]
```

**Logic:** Columns with average length > 20 characters (across first 10 rows) are classified as text columns.

---

### `identify_demographic_columns(data: list[dict]) -> list[str]`

Identify categorical/demographic columns using keyword matching and cardinality analysis.

```python
from src.survey_analyzer.core import identify_demographic_columns

demo_cols = identify_demographic_columns(data)
# Returns: ["age_group", "department", "gender", "region"]
```

**Detection criteria:**
- Column name contains demographic keywords (`age`, `gender`, `location`, `department`, `role`, `region`, `country`, `group`)
- Low cardinality ratio (<10% unique values) with fewer than 15 unique values

---

### `extract_themes(responses: list[str]) -> dict`

Extract major themes from survey responses using LLM analysis.

```python
from src.survey_analyzer.core import extract_themes

responses = [row["feedback"] for row in data if row.get("feedback")]
themes = extract_themes(responses)

# Returns:
# {
#     "themes": [
#         {
#             "name": "Work-Life Balance",
#             "count": 62,
#             "description": "Concerns about overtime and burnout",
#             "sentiment": "negative",
#             "representative_quotes": ["I feel overworked..."]
#         }
#     ],
#     "total_responses": 247
# }
```

**Parameters:**
- `responses` — List of text responses (up to 50 are sent to the LLM)

**Returns:** Dictionary with `themes` list and `total_responses` count

---

### `cluster_themes(themes: dict) -> list[dict]`

Group related themes into higher-level clusters.

```python
from src.survey_analyzer.core import cluster_themes

clusters = cluster_themes(themes)

# Returns:
# [
#     {
#         "cluster_name": "Employee Wellbeing",
#         "themes": ["Work-Life Balance", "Mental Health Support"],
#         "overall_sentiment": "negative",
#         "priority": "high"
#     }
# ]
```

---

### `compute_demographic_crosstabs(data, text_col, demo_col, themes) -> dict`

Cross-tabulate themes by a demographic column.

```python
from src.survey_analyzer.core import compute_demographic_crosstabs

crosstabs = compute_demographic_crosstabs(data, "feedback", "department", themes)

# Returns:
# {
#     "demographic_column": "department",
#     "groups": {
#         "Engineering": {"count": 85, "avg_length": 142.3},
#         "Marketing": {"count": 42, "avg_length": 98.7}
#     }
# }
```

---

### `highlight_verbatims(responses: list[str], themes: dict) -> list[dict]`

Identify the most impactful verbatim quotes from responses.

```python
from src.survey_analyzer.core import highlight_verbatims

verbatims = highlight_verbatims(responses, themes)

# Returns:
# [
#     {
#         "text": "I've been working 60-hour weeks for 3 months straight...",
#         "theme": "Work-Life Balance",
#         "impact": "high",
#         "reason": "Specific quantitative detail illustrating severity"
#     }
# ]
```

---

### `generate_recommendations(responses: list[str], themes: dict) -> list[dict]`

Generate actionable recommendations based on survey analysis.

```python
from src.survey_analyzer.core import generate_recommendations

recs = generate_recommendations(responses, themes)

# Returns:
# [
#     {
#         "title": "Implement Flexible Work Policy",
#         "description": "Allow 2-3 remote days per week...",
#         "priority": "high",
#         "effort": "medium",
#         "expected_impact": "Reduce burnout complaints by 40%"
#     }
# ]
```

---

### `generate_insights(responses: list[str], themes: dict) -> str`

Generate a comprehensive markdown insights report.

```python
from src.survey_analyzer.core import generate_insights

report = generate_insights(responses, themes)
print(report)  # Full markdown report with headings and bullet points
```

**Returns:** Markdown-formatted string with executive summary, key findings, theme analysis, and recommendations

---

## ⚙️ Configuration

Configuration is managed through `config.yaml` in the project root:

```yaml
# Survey Response Analyzer Configuration
# ========================================

llm:
  model: "gemma3:4b"            # Ollama model to use
  temperature: 0.3               # Lower = more focused, higher = more creative
  max_tokens: 4000               # Maximum response length
  base_url: "http://localhost:11434"  # Ollama API endpoint

analysis:
  max_responses_for_themes: 50   # Max responses sent to LLM for theme extraction
  max_responses_for_insights: 30 # Max responses for insights generation
  theme_min_count: 2             # Minimum responses for a theme to be reported

clustering:
  enabled: true                  # Enable theme clustering by default
  max_clusters: 10               # Maximum number of clusters to generate

logging:
  level: "INFO"                  # Logging level (DEBUG, INFO, WARNING, ERROR)
  file: null                     # Log file path (null = console only)
```

### Configuration Options

| Section | Key | Default | Description |
|---------|-----|---------|-------------|
| `llm.model` | `gemma3:4b` | Ollama model name | Any Ollama model works: `llama3`, `mistral`, `phi3` |
| `llm.temperature` | `0.3` | LLM temperature | `0.1`–`0.5` recommended for analysis tasks |
| `llm.max_tokens` | `4000` | Max output tokens | Increase for longer reports |
| `llm.base_url` | `http://localhost:11434` | Ollama URL | Change if Ollama runs on different host/port |
| `analysis.max_responses_for_themes` | `50` | Theme sample size | More = better coverage, slower analysis |
| `analysis.max_responses_for_insights` | `30` | Insights sample size | Responses sent for detailed insights |
| `analysis.theme_min_count` | `2` | Minimum theme count | Filter out themes with very few responses |
| `clustering.enabled` | `true` | Auto-cluster | Enable/disable automatic theme clustering |
| `clustering.max_clusters` | `10` | Cluster limit | Cap the number of clusters generated |

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=src/survey_analyzer --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_core.py -v

# Run specific test
python -m pytest tests/test_core.py::test_load_survey_data -v

# Using Makefile
make test          # Run all tests
make test-cov      # Run with coverage
make lint          # Run linters
```

### Test Structure

```
tests/
├── conftest.py      # Shared fixtures (sample data, mock LLM responses)
├── test_core.py     # Unit tests for core analysis functions
└── test_cli.py      # Integration tests for CLI interface
```

---

## 🏠 Local vs ☁️ Cloud

| Aspect | Survey Response Analyzer (Local) | Cloud Survey Tools |
|--------|----------------------------------|-------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Data sent to cloud servers |
| **Cost** | ✅ Free (after hardware) | ❌ Per-response or subscription fees |
| **Speed** | ⚡ Depends on local GPU/CPU | ⚡ Generally fast with cloud GPUs |
| **Customization** | ✅ Full control over prompts & model | ❌ Limited to vendor features |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Model Choice** | ✅ Any Ollama model | ❌ Vendor-locked model |
| **Data Volume** | ⚠️ Limited by local RAM | ✅ Scales with cloud resources |
| **Setup** | ⚠️ Requires Ollama install | ✅ Usually no setup needed |

---

## ❓ FAQ

<details>
<summary><strong>What CSV format does it expect?</strong></summary>

Any standard CSV with a header row. The tool automatically detects which columns contain free-text responses (average length > 20 characters) and which are demographic/categorical. No specific column names are required.

```csv
id,feedback,department,rating
1,"The onboarding process was excellent...",Engineering,5
2,"I wish we had more team events...",Marketing,3
```

</details>

<details>
<summary><strong>Can I use a different LLM model?</strong></summary>

Yes! Change the `llm.model` field in `config.yaml` to any model available in your Ollama installation:

```yaml
llm:
  model: "llama3:8b"      # Or "mistral", "phi3", "gemma:7b", etc.
```

Pull the model first: `ollama pull llama3:8b`

</details>

<details>
<summary><strong>How many responses can it handle?</strong></summary>

The tool samples up to 50 responses for theme extraction and 30 for insights generation (configurable in `config.yaml`). The CSV itself can contain thousands of rows — only the sample is sent to the LLM, while demographic crosstabs process all rows.

</details>

<details>
<summary><strong>Why are themes sometimes inconsistent between runs?</strong></summary>

LLMs are non-deterministic by nature. Lower the `temperature` in `config.yaml` (e.g., `0.1`) for more consistent results. Theme names may vary slightly, but the underlying patterns should remain stable.

</details>

<details>
<summary><strong>Can I export the analysis results?</strong></summary>

Use `--report detailed` to generate a full markdown insights report displayed in the terminal. The Web UI also displays the full analysis. You can pipe CLI output to a file:

```bash
python -m src.survey_analyzer.cli -f survey.csv --report detailed > report.md
```

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/survey-response-analyzer.git
cd survey-response-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -e .

# Run tests to verify setup
python -m pytest tests/ -v
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Write tests** for new functionality
4. **Ensure** all tests pass (`python -m pytest tests/ -v`)
5. **Follow** the existing code style (Black formatting)
6. **Commit** with descriptive messages
7. **Push** to your fork and open a **Pull Request**

### Areas for Contribution

- 🌍 Multi-language survey support
- 📊 Additional visualization types
- 🔌 Export to PDF/DOCX formats
- 🧪 More comprehensive test coverage
- 📖 Documentation improvements
- 🐛 Bug fixes and error handling

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**📋 Survey Response Analyzer** — Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

Built with ❤️ using Python, Ollama, Click, Rich, and Streamlit

<sub>If this project helped you, consider giving it a ⭐ on <a href="https://github.com/kennedyraju55/survey-response-analyzer">GitHub</a></sub>

<img src="https://img.shields.io/badge/Made_with-Local_LLM-2ec4b6?style=flat-square" alt="Made with Local LLM" />
<img src="https://img.shields.io/badge/Privacy-100%25_Local-2ec4b6?style=flat-square" alt="Privacy First" />
<img src="https://img.shields.io/badge/Project-43%2F90-2ec4b6?style=flat-square" alt="Project 43/90" />

</div>
