<div align="center">

<img src="docs/images/banner.svg" alt="CSV Data Analyzer Banner" width="800" />

<br/><br/>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-e94560?style=for-the-badge)](LICENSE)
[![LLM Powered](https://img.shields.io/badge/LLM-Powered-ff6b81?style=for-the-badge&logo=openai&logoColor=white)](https://ollama.ai)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](https://github.com/kennedyraju55/csv-data-analyzer/pulls)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br/>

**Drop a CSV. Ask a question. Get insights — powered entirely by a local LLM.**

<br/>

[Why This Tool](#-why-this-tool) · [Features](#-features) · [Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [Configuration](#-configuration) · [Testing](#-testing) · [FAQ](#-faq) · [Contributing](#-contributing)

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

---

## 📑 Table of Contents

- [Why This Tool](#-why-this-tool)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Web UI](#-web-ui)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Local LLM vs Cloud](#-local-llm-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🤔 Why This Tool

Data analysis shouldn't require writing boilerplate pandas code every time you open a CSV. Here's how CSV Data Analyzer compares to the manual approach:

| Aspect | Manual (pandas + matplotlib) | CSV Data Analyzer |
|--------|------------------------------|-------------------|
| **Setup time** | 10–30 min writing imports, loading, cleaning | `--file data.csv` — zero boilerplate |
| **Column type detection** | Manual `dtypes` inspection + guessing | Auto-detected: numeric, categorical, datetime, text, boolean |
| **Statistical summary** | Write `describe()`, compute skewness manually | One command — shape, nulls, skewness, kurtosis, distributions |
| **Correlation analysis** | `df.corr()` + manual threshold filtering | Automatic matrix + strong correlation flagging (>0.5) |
| **Chart selection** | Trial-and-error choosing chart types | AI-suggested: scatter, histogram, bar, line, pie |
| **Natural language** | Not possible without custom code | `--query "What drives revenue?"` — plain English |
| **Export** | Custom JSON serialization code | `--export insights.json` — structured, ready to use |
| **Privacy** | Cloud notebooks may expose data | 100% local — data never leaves your machine |
| **Reproducibility** | Jupyter notebooks drift over time | Deterministic CLI pipeline, same input → same output |

> 💡 **Bottom line:** Go from CSV to comprehensive analysis in seconds, not hours.

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800" />
</div>

<br/>

### 🔍 Smart Column Detection

Automatically classifies every column in your dataset using intelligent heuristics:

- **Numeric** — integers, floats, currency values
- **Categorical** — columns with limited unique values relative to row count
- **Datetime** — date strings, timestamps, ISO formats
- **Text** — free-form strings, descriptions, comments
- **Boolean** — true/false, yes/no, 0/1 patterns

```python
from src.csv_analyzer.core import load_csv, detect_column_types

df = load_csv("sales.csv")
types = detect_column_types(df)
# {'revenue': 'numeric', 'region': 'categorical', 'date': 'datetime', ...}
```

### 📈 Statistical Analysis

Generates comprehensive statistics for every column, with proper null handling:

- **Shape & size** — rows, columns, memory usage
- **Dtype distribution** — count of each pandas dtype
- **Null analysis** — missing values per column with percentages
- **Numeric stats** — mean, median, std, min, max, quartiles, skewness, kurtosis
- **Categorical stats** — unique counts, top values, frequency distributions

### 🔗 Correlation Engine

Computes the full Pearson correlation matrix across all numeric columns and flags notable relationships:

- Strong correlations (|r| > 0.5) highlighted automatically
- Configurable threshold via `config.yaml`
- Matrix output suitable for heatmap visualization

### 📊 Chart Suggestions

Recommends the most appropriate visualization types based on your data's characteristics:

| Data Pattern | Suggested Chart |
|-------------|-----------------|
| Two numeric columns | Scatter plot |
| Single numeric column | Histogram |
| Categorical + numeric | Bar chart |
| Datetime + numeric | Line chart |
| Categorical with few values | Pie chart |

### 💬 Natural Language Queries

Ask questions about your data in plain English. The tool formats a rich data summary — including column types, statistics, and sample rows — and sends it to a local LLM for analysis:

```bash
python -m src.csv_analyzer.cli -f sales.csv -q "Which region had the highest growth rate?"
```

### 📥 JSON Export

Export all computed insights to a structured JSON file for programmatic access, downstream pipelines, or archival:

```bash
python -m src.csv_analyzer.cli -f data.csv --export insights.json
```

The exported JSON includes column types, statistical summaries, correlation data, and chart suggestions.

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Runtime |
| pip | latest | Package management |
| Ollama | latest | Local LLM inference |
| gemma3:4b | — | Default LLM model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/csv-data-analyzer.git
cd csv-data-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Or install as an editable package
pip install -e .

# 4. Or use the Makefile
make install

# 5. Pull the LLM model (if not already available)
ollama pull gemma3:4b
```

### Your First Analysis

```bash
python -m src.csv_analyzer.cli --file sales_data.csv --query "What are the top trends?"
```

### Example Output

```
╭──────────────────────────────────────────────────────────╮
│                   📊 Data Preview                        │
╰──────────────────────────────────────────────────────────╯
┌────────┬──────────┬─────────┬────────┬───────────┐
│ month  │ region   │ revenue │ units  │ category  │
├────────┼──────────┼─────────┼────────┼───────────┤
│ Jan    │ North    │ 45200   │ 312    │ Electronics│
│ Feb    │ South    │ 38900   │ 275    │ Clothing  │
│ Mar    │ East     │ 52100   │ 401    │ Electronics│
│ Apr    │ West     │ 41800   │ 290    │ Food      │
│ May    │ North    │ 61300   │ 489    │ Electronics│
└────────┴──────────┴─────────┴────────┴───────────┘

╭──────────────────────────────────────────────────────────╮
│                  🔍 Column Types                         │
╰──────────────────────────────────────────────────────────╯
  month      → categorical
  region     → categorical
  revenue    → numeric
  units      → numeric
  category   → categorical

╭──────────────────────────────────────────────────────────╮
│               📈 Statistical Summary                     │
╰──────────────────────────────────────────────────────────╯
  Shape: (120, 5)
  Null values: 0
  ─────────────────────────────────────
  revenue:  mean=47,860  std=12,340  skew=0.42  kurt=-0.18
  units:    mean=353     std=98      skew=0.31  kurt=-0.52

╭──────────────────────────────────────────────────────────╮
│               🔗 Strong Correlations                     │
╰──────────────────────────────────────────────────────────╯
  revenue ↔ units:  r = 0.94 ★★★

╭──────────────────────────────────────────────────────────╮
│              📊 Chart Suggestions                        │
╰──────────────────────────────────────────────────────────╯
  • Scatter: revenue vs units
  • Bar: category × revenue
  • Line: month × revenue
  • Pie: region distribution

╭──────────────────────────────────────────────────────────╮
│              💬 LLM Analysis                             │
╰──────────────────────────────────────────────────────────╯
  Based on the data, the top trends are:

  1. Electronics dominates revenue, contributing 52% of total sales
  2. Revenue and units show a strong positive correlation (r=0.94)
  3. North region leads with the highest average monthly revenue
  4. A clear upward trend is visible from January through May
  5. Food category has the most stable month-over-month performance
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/csv-data-analyzer.git
cd csv-data-analyzer
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
uvicorn src.csv_analyzer.api:app --reload --port 8000

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

### Usage

```bash
python -m src.csv_analyzer.cli [OPTIONS]
```

### Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | `PATH` | *(required)* | Path to the CSV file to analyze |
| `--query` | `-q` | `TEXT` | `None` | Natural language question about the data |
| `--show-preview / --no-preview` | — | `BOOL` | `True` | Display a preview table of the first N rows |
| `--show-types / --no-types` | — | `BOOL` | `True` | Display auto-detected column types |
| `--show-correlations / --no-correlations` | — | `BOOL` | `True` | Display correlation analysis and strong pairs |
| `--show-charts / --no-charts` | — | `BOOL` | `True` | Display chart type suggestions |
| `--export` | `-e` | `PATH` | `None` | Export all insights to a JSON file |
| `--verbose` | `-v` | `FLAG` | `False` | Enable verbose/debug logging output |

### Example Commands

```bash
# Full analysis with all panels visible
python -m src.csv_analyzer.cli -f data.csv

# Ask a specific question — hide everything else
python -m src.csv_analyzer.cli -f data.csv -q "What is the average salary by department?" \
  --no-preview --no-types --no-correlations --no-charts

# Export insights without displaying anything
python -m src.csv_analyzer.cli -f data.csv --export report.json \
  --no-preview --no-types --no-correlations --no-charts

# Verbose mode for debugging
python -m src.csv_analyzer.cli -f data.csv --verbose

# Combine query and export
python -m src.csv_analyzer.cli -f sales.csv \
  -q "Which product has the highest margin?" \
  -e sales_insights.json

# Correlations only
python -m src.csv_analyzer.cli -f metrics.csv \
  --no-preview --no-types --show-correlations --no-charts

# Quick type check on a new dataset
python -m src.csv_analyzer.cli -f unknown_data.csv \
  --show-types --no-preview --no-correlations --no-charts
```

---

## 🌐 Web UI

CSV Data Analyzer also ships with a **Streamlit-based web dashboard** for interactive, browser-based analysis.

### Launch

```bash
# Using Streamlit directly
streamlit run src/csv_analyzer/web_ui.py

# Or via Makefile
make web
```

The dashboard opens at **`http://localhost:8501`** by default.

### Web UI Capabilities

| Feature | Description |
|---------|-------------|
| 📁 **CSV Upload** | Drag-and-drop or browse file uploader |
| 📋 **Data Preview** | Interactive, scrollable data table |
| 🔍 **Column Types** | Visual cards showing detected type per column |
| 📈 **Statistics** | Tabbed view — numeric stats and categorical stats |
| 🔗 **Correlation Heatmap** | Visual heatmap with strong correlation highlights |
| 📊 **Chart Suggestions** | Rendered interactive charts (Plotly-powered) |
| 💬 **Query Box** | Type questions and get LLM-powered answers |
| 📥 **Export** | One-click JSON download of all insights |

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800" />
</div>

<br/>

### Pipeline Flow

```
CSV File
  │
  ▼
load_csv()                    ← Parse CSV into pandas DataFrame
  │
  ▼
detect_column_types()         ← Classify columns: numeric, categorical, datetime, text, boolean
  │
  ├──▶ generate_statistical_summary()   ← Compute stats: shape, nulls, skew, kurtosis
  │
  ├──▶ compute_correlations()           ← Pearson matrix + strong correlation flagging
  │
  ├──▶ suggest_charts()                 ← Recommend visualization types
  │
  ▼
generate_data_summary()       ← Format everything for LLM context
  │
  ▼
analyze_data(df, query)       ← Send to local LLM (Ollama) for NL analysis
  │
  ├──▶ Rich Console Output    ← Colored tables, panels via Rich library
  │
  └──▶ export_insights()      ← Structured JSON file
```

### Project Structure

```
41-csv-data-analyzer/
├── src/
│   └── csv_analyzer/
│       ├── __init__.py          # Package metadata & version
│       ├── core.py              # Core analysis engine
│       │                          ├─ load_csv()
│       │                          ├─ detect_column_types()
│       │                          ├─ generate_statistical_summary()
│       │                          ├─ compute_correlations()
│       │                          ├─ suggest_charts()
│       │                          ├─ generate_data_summary()
│       │                          ├─ analyze_data()
│       │                          └─ export_insights()
│       ├── cli.py               # Click CLI with Rich output
│       └── web_ui.py            # Streamlit web dashboard
├── tests/
│   ├── conftest.py              # Shared pytest fixtures
│   ├── test_core.py             # Unit tests for core functions
│   └── test_cli.py              # CLI integration tests
├── common/                      # Shared utilities
├── docs/
│   └── images/                  # SVG assets (banner, architecture, features)
├── config.yaml                  # Application configuration
├── setup.py                     # Package setup & entry points
├── Makefile                     # Development shortcuts
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Data Processing | **pandas** | CSV parsing, DataFrame operations, statistics |
| CLI Framework | **Click** | Command-line argument parsing and help |
| Console Output | **Rich** | Colored tables, panels, progress bars |
| Web UI | **Streamlit** | Interactive browser-based dashboard |
| LLM Inference | **Ollama** | Local LLM hosting and API |
| LLM Model | **Gemma 3 4B** | Natural language understanding |
| Configuration | **PyYAML** | YAML config file parsing |
| Testing | **pytest** | Unit and integration testing |

---

## 📚 API Reference

All core functions live in `src/csv_analyzer/core.py`. Below is the complete public API.

### `load_csv(file_path: str) → pd.DataFrame`

Load a CSV file into a pandas DataFrame.

```python
from src.csv_analyzer.core import load_csv

df = load_csv("data/sales_2024.csv")
print(df.shape)  # (1200, 8)
```

**Parameters:**
- `file_path` — Path to the CSV file

**Returns:** `pd.DataFrame`

**Raises:** `FileNotFoundError` if the file does not exist

---

### `detect_column_types(df: pd.DataFrame) → dict`

Analyze each column and classify it as numeric, categorical, datetime, text, or boolean.

```python
from src.csv_analyzer.core import load_csv, detect_column_types

df = load_csv("employees.csv")
types = detect_column_types(df)
print(types)
# {
#   'employee_id': 'numeric',
#   'name': 'text',
#   'department': 'categorical',
#   'hire_date': 'datetime',
#   'is_active': 'boolean',
#   'salary': 'numeric'
# }
```

**Parameters:**
- `df` — Input DataFrame

**Returns:** `dict[str, str]` mapping column names to type labels

---

### `generate_statistical_summary(df: pd.DataFrame) → dict`

Compute a comprehensive statistical summary including shape, dtypes, null counts, numeric descriptive statistics, categorical value counts, skewness, and kurtosis.

```python
from src.csv_analyzer.core import load_csv, generate_statistical_summary

df = load_csv("metrics.csv")
summary = generate_statistical_summary(df)

print(summary['shape'])         # (500, 12)
print(summary['null_counts'])   # {'col_a': 3, 'col_b': 0, ...}
print(summary['numeric_stats']) # {'revenue': {'mean': 45000, 'std': 12000, ...}}
```

**Parameters:**
- `df` — Input DataFrame

**Returns:** `dict` with keys: `shape`, `dtypes`, `null_counts`, `numeric_stats`, `categorical_stats`, `skewness`, `kurtosis`

---

### `compute_correlations(df: pd.DataFrame) → dict`

Compute the Pearson correlation matrix for all numeric columns and identify strong correlations above the configured threshold.

```python
from src.csv_analyzer.core import load_csv, compute_correlations

df = load_csv("housing.csv")
result = compute_correlations(df)

print(result['matrix'])
# DataFrame with correlation coefficients

print(result['strong_correlations'])
# [('sqft', 'price', 0.89), ('bedrooms', 'bathrooms', 0.72)]
```

**Parameters:**
- `df` — Input DataFrame

**Returns:** `dict` with keys: `matrix` (correlation DataFrame), `strong_correlations` (list of tuples)

---

### `suggest_charts(df: pd.DataFrame, column_types: dict) → list`

Suggest appropriate chart types based on detected column types and data characteristics.

```python
from src.csv_analyzer.core import load_csv, detect_column_types, suggest_charts

df = load_csv("weather.csv")
types = detect_column_types(df)
charts = suggest_charts(df, types)

for chart in charts:
    print(f"{chart['type']}: {chart['columns']}")
# scatter: ['temperature', 'humidity']
# line: ['date', 'temperature']
# bar: ['city', 'rainfall']
# histogram: ['temperature']
```

**Parameters:**
- `df` — Input DataFrame
- `column_types` — Dictionary from `detect_column_types()`

**Returns:** `list[dict]` — Each dict has `type` and `columns` keys

---

### `generate_data_summary(df: pd.DataFrame) → str`

Create a formatted text summary of the dataset suitable for LLM context. Includes column info, sample rows, basic statistics, and data characteristics.

```python
from src.csv_analyzer.core import load_csv, generate_data_summary

df = load_csv("products.csv")
summary_text = generate_data_summary(df)
print(summary_text[:200])
# "Dataset has 450 rows and 7 columns. Columns: product_id (int64), ..."
```

**Parameters:**
- `df` — Input DataFrame

**Returns:** `str` — Formatted text summary

---

### `analyze_data(df: pd.DataFrame, query: str) → str`

Send the data summary and a natural language query to the local LLM for analysis.

```python
from src.csv_analyzer.core import load_csv, analyze_data

df = load_csv("financials.csv")
answer = analyze_data(df, "What quarter had the highest profit margin?")
print(answer)
# "Based on the data, Q3 2024 had the highest profit margin at 23.4%..."
```

**Parameters:**
- `df` — Input DataFrame
- `query` — Natural language question

**Returns:** `str` — LLM-generated analysis

**Requires:** Ollama running locally with the configured model

---

### `export_insights(df: pd.DataFrame, output_path: str) → None`

Export all computed insights — column types, statistical summary, correlations, and chart suggestions — to a JSON file.

```python
from src.csv_analyzer.core import load_csv, export_insights

df = load_csv("survey.csv")
export_insights(df, "survey_insights.json")
# Creates survey_insights.json with all analysis results
```

**Parameters:**
- `df` — Input DataFrame
- `output_path` — Path for the output JSON file

**Returns:** `None`

---

## ⚙️ Configuration

All settings are defined in `config.yaml` at the project root:

```yaml
# CSV Data Analyzer Configuration
# ================================

llm:
  model: "gemma3:4b"           # Ollama model to use for analysis
  temperature: 0.3             # LLM creativity (0.0 = deterministic, 1.0 = creative)
  max_tokens: 4000             # Maximum tokens in LLM response
  base_url: "http://localhost:11434"  # Ollama API endpoint

analysis:
  max_preview_rows: 5          # Number of rows shown in data preview
  correlation_threshold: 0.5   # Minimum |r| to flag as "strong" correlation
  max_sample_rows_for_llm: 50  # Max rows included in LLM context

export:
  default_format: "json"       # Export format (currently only JSON)
  include_raw_data: false      # Whether to include raw data in exports

logging:
  level: "INFO"                # Logging level: DEBUG, INFO, WARNING, ERROR
  file: null                   # Log file path (null = console only)
```

### Configuration Options Explained

| Section | Key | Description | Values |
|---------|-----|-------------|--------|
| `llm` | `model` | Ollama model name | Any Ollama model (e.g., `gemma3:4b`, `llama3:8b`, `mistral`) |
| `llm` | `temperature` | Response randomness | `0.0` – `1.0` (lower = more focused) |
| `llm` | `max_tokens` | Max response length | Integer (e.g., `2000`, `4000`, `8000`) |
| `llm` | `base_url` | Ollama API URL | URL string (default: `http://localhost:11434`) |
| `analysis` | `max_preview_rows` | Preview table rows | Integer (e.g., `5`, `10`, `20`) |
| `analysis` | `correlation_threshold` | Strong correlation cutoff | `0.0` – `1.0` (default: `0.5`) |
| `analysis` | `max_sample_rows_for_llm` | Rows sent to LLM | Integer (e.g., `25`, `50`, `100`) |
| `export` | `default_format` | Export file format | `"json"` |
| `export` | `include_raw_data` | Include raw rows in export | `true` / `false` |
| `logging` | `level` | Minimum log level | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `logging` | `file` | Log output file | File path or `null` |

### Swapping LLM Models

```bash
# Pull a different model
ollama pull llama3:8b

# Update config.yaml
# llm:
#   model: "llama3:8b"

# Or use any Ollama-compatible model
ollama pull mistral
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run only core logic tests
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v

# Run with coverage report
python -m pytest tests/ --cov=src/csv_analyzer --cov-report=term-missing

# Or use the Makefile shortcut
make test        # Run tests
make test-cov    # Run with coverage
```

### Test Structure

```
tests/
├── conftest.py      # Shared fixtures (sample DataFrames, temp CSV files)
├── test_core.py     # Tests for load_csv, detect_column_types,
│                    #   generate_statistical_summary, compute_correlations,
│                    #   suggest_charts, export_insights
└── test_cli.py      # CLI integration tests using Click's CliRunner
```

### Writing New Tests

```python
# tests/test_core.py
import pandas as pd
from src.csv_analyzer.core import detect_column_types

def test_detect_numeric_columns():
    df = pd.DataFrame({'price': [10.5, 20.3, 30.1], 'qty': [1, 2, 3]})
    types = detect_column_types(df)
    assert types['price'] == 'numeric'
    assert types['qty'] == 'numeric'

def test_detect_categorical_columns():
    df = pd.DataFrame({'color': ['red', 'blue', 'red', 'green', 'blue']})
    types = detect_column_types(df)
    assert types['color'] == 'categorical'
```

---

## ☁️ Local LLM vs Cloud

| Factor | Local LLM (Ollama) | Cloud LLM (OpenAI, etc.) |
|--------|-------------------|--------------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after hardware investment | ❌ Pay per token / API call |
| **Latency** | ⚡ Low (no network round-trip) | 🐌 Depends on network & API load |
| **Model quality** | 🟡 Good (Gemma 4B, Llama 8B) | ✅ Excellent (GPT-4, Claude) |
| **Offline usage** | ✅ Works without internet | ❌ Requires active connection |
| **Setup** | 🟡 Install Ollama + pull model | ✅ Just an API key |
| **Scalability** | 🟡 Limited by local GPU/CPU | ✅ Scales elastically |
| **Customization** | ✅ Fine-tune, swap models freely | 🟡 Limited to provider's offerings |
| **Reproducibility** | ✅ Same model version always | 🟡 Models updated without notice |

> 💡 **This project defaults to local LLM** for maximum privacy. Your CSV data — which may contain sensitive business metrics, personal information, or proprietary data — never leaves your machine.

---

## ❓ FAQ

### 1. What CSV formats are supported?

CSV Data Analyzer uses `pandas.read_csv()` under the hood, so it supports standard comma-separated files with headers. Files must be UTF-8 encoded. For other delimiters (tab, semicolon), you may need to preprocess the file or modify `load_csv()`.

### 2. How large can my CSV files be?

The tool loads the entire CSV into memory as a pandas DataFrame. As a rule of thumb:
- **< 100 MB** — works seamlessly
- **100 MB – 1 GB** — works but may be slow; consider sampling
- **> 1 GB** — not recommended; use chunked processing or a database

The LLM context is limited to `max_sample_rows_for_llm` rows (default: 50), so even large files won't overwhelm the model.

### 3. Do I need a GPU for the local LLM?

A GPU is recommended but not required. Ollama can run models on CPU, though inference will be slower. For the default `gemma3:4b` model:
- **With GPU (4GB+ VRAM):** ~2–5 seconds per query
- **CPU only:** ~15–30 seconds per query

### 4. Can I use a different LLM model?

Yes! Any model available through Ollama works. Simply update `config.yaml`:

```yaml
llm:
  model: "llama3:8b"    # or "mistral", "phi3", "gemma2:9b", etc.
```

Then pull the model: `ollama pull llama3:8b`

### 5. How do I add support for new chart types?

Chart suggestions are generated by `suggest_charts()` in `core.py`. To add a new chart type, add a new condition that checks column types and data characteristics. For example, to add a heatmap suggestion:

```python
# In suggest_charts()
if len(numeric_cols) >= 3:
    suggestions.append({
        'type': 'heatmap',
        'columns': numeric_cols[:5],
        'reason': 'Multiple numeric columns suitable for correlation heatmap'
    })
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/<your-username>/csv-data-analyzer.git
cd csv-data-analyzer

# 2. Install dev dependencies
pip install -e ".[dev]"

# 3. Run tests to verify setup
python -m pytest tests/ -v
```

### Contribution Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes with tests
4. **Run** the test suite: `python -m pytest tests/ -v`
5. **Commit** with a descriptive message: `git commit -m "feat: add heatmap chart suggestion"`
6. **Push** to your fork: `git push origin feature/my-feature`
7. **Open** a Pull Request against `master`

### Code Style

- Follow [PEP 8](https://pep8.org/) conventions
- Use [Black](https://github.com/psf/black) for formatting
- Add docstrings to all public functions
- Write tests for new features

### Areas for Contribution

- 🆕 New chart type suggestions
- 🌐 Additional export formats (CSV summary, HTML report)
- 🧠 Support for more LLM providers
- 📊 Advanced statistical tests (t-test, chi-square)
- 🎨 Web UI improvements and new visualizations
- 📖 Documentation and examples
- 🐛 Bug fixes and performance improvements

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, commercial or non-commercial.

---

<div align="center">

<br/>

Built with ❤️ using Python, pandas, and local LLMs

<br/>

⭐ **If this tool saved you time, consider [starring the repo](https://github.com/kennedyraju55/csv-data-analyzer)!** ⭐

<br/>

<sub>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</sub>

</div>
