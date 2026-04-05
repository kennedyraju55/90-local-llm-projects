<div align="center">

<img src="docs/images/banner.svg" alt="PDF Report Generator Banner" width="800"/>

<br/><br/>

<img src="https://img.shields.io/badge/Gemma_4-Ollama-orange?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/Rich-Terminal_UI-purple?style=flat-square" alt="Rich"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Privacy-100%25_Local-06d6a0?style=flat-square" alt="100% Local"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/><br/>

**Turn raw CSV data into polished, professional reports — powered entirely by a local LLM.**
<br/>
No API keys. No cloud. Your business data never leaves your machine.

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

<br/>

---

## Table of Contents

- [Why This Project?](#why-this-project)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
  - [CLI Reference](#cli-reference)
  - [CLI Options](#cli-options)
  - [Examples](#examples)
- [Report Templates](#-report-templates)
  - [Executive Template](#executive-template)
  - [Technical Template](#technical-template)
  - [Summary Template](#summary-template)
- [Output Formats](#-output-formats)
- [API Reference](#-api-reference)
  - [read_csv_data()](#read_csv_datafilepath)
  - [summarize_data()](#summarize_dataheaders-rows)
  - [generate_report()](#generate_reporttopic-data_summary-templateexecutive-confignone)
  - [save_report()](#save_reportcontent-output_path-topic-fmtmarkdown)
- [Configuration](#%EF%B8%8F-configuration)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Testing](#-testing)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## Why This Project?

Writing reports is one of the most time-consuming tasks in any data-driven role. Analysts spend hours every week copying numbers from spreadsheets, formatting tables in Word, writing summaries that rehash the same patterns, and making sure nothing was missed. Meanwhile, the actual insights — the part that matters — take a backseat to formatting and boilerplate.

**The problem is clear:**

- Manual report writing is slow, error-prone, and repetitive
- Copy-pasting statistics from CSV files into documents leads to mistakes
- Every team has slightly different formatting requirements (executive summaries vs. technical deep-dives vs. quick briefs)
- Cloud-based AI tools like ChatGPT or Claude require uploading sensitive business data to third-party servers
- Most report generators are either too rigid (static templates) or too complex (enterprise BI platforms)

**PDF Report Generator solves all of these problems:**

1. **Feed it a CSV, get a report.** No manual number-crunching — `summarize_data()` automatically computes min, max, mean, median, standard deviation, and sum for every numeric column, plus unique value counts and frequency distributions for text columns.

2. **Choose your format.** Need a polished executive summary for leadership? A technical analysis for your engineering team? A quick 3-sentence brief for a standup? Pick a template and go.

3. **100% private.** Every byte of processing happens on your machine via Ollama + Gemma 4. Your quarterly revenue data, employee performance metrics, or customer analytics never touch the internet.

4. **Developer-friendly.** Four clean Python functions (`read_csv_data`, `summarize_data`, `generate_report`, `save_report`) that you can import and compose in your own scripts, or just use the CLI.

If you've ever spent 45 minutes writing a report that a machine could have drafted in 30 seconds, this project is for you.

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Feature | Description |
|---------|-------------|
| **Template System** | Three built-in templates — executive, technical, and summary — each with distinct section structures tailored for different audiences |
| **Statistical Analysis** | Automatic column profiling: min, max, mean, median, stdev, and sum for numeric data; unique values and frequency counts for text data |
| **Multi-Format Output** | Export reports as Markdown (with YAML frontmatter), self-contained HTML, or plain text |
| **Chart Descriptions** | AI-generated recommendations for data visualizations — bar charts, line graphs, pie charts — with axis labels and data mappings |
| **YAML Frontmatter** | Every Markdown report includes professional metadata headers (title, timestamp, generator) compatible with static site generators |
| **100% Private** | Runs entirely on your machine via Ollama — zero cloud dependencies, zero API keys, zero data exfiltration risk |
| **Rich CLI** | Beautiful terminal interface with progress spinners, colored output, data preview tables, and report previews powered by Rich |
| **Configurable** | YAML-based configuration for LLM parameters (temperature, max tokens), data preview limits, and output settings |
| **Error Handling** | Clear error messages for missing files, empty CSVs, malformed data, and Ollama connection issues |

---

## 🏗 Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800"/>
</div>

<br/>

The pipeline follows a clean four-stage flow:

1. **CSV Ingestion** — `read_csv_data(filepath)` reads and validates the input file, returning column headers and row dictionaries
2. **Statistical Profiling** — `summarize_data(headers, rows)` computes comprehensive statistics for every column, building the context window for the LLM
3. **LLM Report Generation** — `generate_report(topic, data_summary, template, config)` sends the statistical summary to Gemma 4 via Ollama with a template-specific system prompt
4. **Multi-Format Export** — `save_report(content, output_path, topic, fmt)` serializes the report to Markdown (with YAML frontmatter), HTML, or plain text

Each function is independently testable and composable — you can use them individually in scripts or let the CLI orchestrate the full pipeline.

---

## 🚀 Quick Start

Get a report in under 2 minutes:

```bash
# 1. Clone and install
git clone https://github.com/kennedyraju55/pdf-report-generator.git
cd pdf-report-generator
pip install -r requirements.txt

# 2. Start Ollama and pull the model
ollama serve &
ollama pull gemma4

# 3. Generate your first report
python -m src.report_generator.cli \
  --topic "Q4 Sales Analysis" \
  --data sales_data.csv

# 4. Open the report
cat report.md
```

That's it. The CLI reads your CSV, profiles every column, sends the statistical summary to Gemma 4, and saves a fully structured Markdown report with YAML frontmatter.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/pdf-report-generator.git
cd pdf-report-generator
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
uvicorn src.report_generator.api:app --reload --port 8000

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
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM inference server |
| Gemma 4 | Latest | Language model for report generation |

### Step 1: Clone the Repository

```bash
git clone https://github.com/kennedyraju55/pdf-report-generator.git
cd pdf-report-generator
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---------|---------|
| `click` | CLI argument parsing and command structure |
| `rich` | Terminal UI — tables, spinners, panels, markdown preview |
| `pyyaml` | Configuration file parsing (`config.yaml`) |
| `requests` | HTTP communication with Ollama API |
| `streamlit` | Web UI (optional) |
| `markdown` | HTML report rendering (optional, install via `pip install markdown`) |

### Step 3: Set Up Ollama

```bash
# Install Ollama (see https://ollama.com for platform-specific instructions)

# Start the Ollama server
ollama serve

# Pull the Gemma 4 model
ollama pull gemma4
```

### Step 4: Verify Installation

```bash
# Check that Ollama is running
curl http://localhost:11434/api/tags

# Run a quick test
python -m pytest tests/ -v
```

---

## 📖 Usage

### CLI Reference

The report generator uses a single command with no subcommands:

```bash
python -m src.report_generator.cli [OPTIONS]
```

### CLI Options

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `--topic` | `TEXT` | ✅ Yes | — | Report topic or title. Used in the report header and YAML frontmatter. |
| `--data` | `PATH` | ✅ Yes | — | Path to the input CSV file. Must exist and contain at least one header row and one data row. |
| `--output` | `PATH` | No | `report.md` | Output file path. Extension is auto-adjusted based on `--format` (e.g., `.html` for HTML). |
| `--template` | `CHOICE` | No | `executive` | Report template: `executive`, `technical`, or `summary`. Controls section structure. |
| `--format` | `CHOICE` | No | `markdown` | Output format: `markdown`, `html`, or `text`. Markdown includes YAML frontmatter. |
| `--config` | `PATH` | No | — | Path to a `config.yaml` file for LLM parameters and output settings. |
| `--verbose` | `FLAG` | No | `false` | Enable debug-level logging to see data summaries, LLM prompts, and timing. |

### Examples

**Basic executive report:**

```bash
python -m src.report_generator.cli \
  --topic "Q4 Sales Performance" \
  --data quarterly_sales.csv
```

**Technical analysis with HTML output:**

```bash
python -m src.report_generator.cli \
  --topic "Server Performance Metrics" \
  --data server_logs.csv \
  --template technical \
  --format html \
  --output reports/server_analysis.html
```

**Quick summary brief:**

```bash
python -m src.report_generator.cli \
  --topic "Customer Satisfaction Survey" \
  --data survey_results.csv \
  --template summary \
  --output survey_brief.md
```

**Full options with custom config and verbose logging:**

```bash
python -m src.report_generator.cli \
  --topic "Annual Revenue Report" \
  --data revenue_2024.csv \
  --template executive \
  --format markdown \
  --output reports/annual_revenue.md \
  --config config.yaml \
  --verbose
```

**Plain text output for email attachments:**

```bash
python -m src.report_generator.cli \
  --topic "Weekly KPI Update" \
  --data weekly_kpis.csv \
  --template summary \
  --format text \
  --output weekly_update.txt
```

---

## 📋 Report Templates

### Executive Template

Best for: leadership presentations, board reports, stakeholder updates.

**Sections generated:**

| # | Section | Content |
|---|---------|---------|
| 1 | **Executive Summary** | 2-3 paragraph overview of key findings and their business implications |
| 2 | **Key Findings** | Bullet-pointed list of the most significant insights from the data |
| 3 | **Data Analysis** | Detailed breakdown with specific numbers, comparisons, and trends |
| 4 | **Chart Descriptions** | AI-generated descriptions of 2-3 charts that would visualize the data |
| 5 | **Recommendations** | Actionable next steps based on the analysis |
| 6 | **Conclusion** | Final summary tying together findings and recommendations |

```bash
python -m src.report_generator.cli --topic "Q4 Revenue" --data data.csv --template executive
```

### Technical Template

Best for: engineering teams, data science reports, methodology documentation.

**Sections generated:**

| # | Section | Content |
|---|---------|---------|
| 1 | **Overview** | Technical summary of the dataset and analysis scope |
| 2 | **Methodology** | How the data was analyzed — statistical methods applied |
| 3 | **Statistical Analysis** | Deep-dive into distributions, correlations, and statistical tests |
| 4 | **Chart Descriptions** | Recommended statistical visualizations (histograms, scatter plots, box plots) |
| 5 | **Findings** | Technical observations with supporting evidence |
| 6 | **Technical Recommendations** | Data-driven suggestions for next steps |

```bash
python -m src.report_generator.cli --topic "API Latency" --data latency.csv --template technical
```

### Summary Template

Best for: daily standups, quick briefs, email digests.

**Sections generated:**

| # | Section | Content |
|---|---------|---------|
| 1 | **Summary** | 3-5 sentence overview — the entire report in a paragraph |
| 2 | **Key Metrics** | Top 5 numbers that matter most |
| 3 | **Action Items** | 3 quick, actionable recommendations |

```bash
python -m src.report_generator.cli --topic "Daily Sales" --data today.csv --template summary
```

---

## 📄 Output Formats

### Markdown (default)

Includes YAML frontmatter for static site generators and documentation tools:

```markdown
---
title: "Q4 Sales Performance"
generated: "2025-01-15 14:30:22"
generator: "report-generator"
---

# Q4 Sales Performance

## Executive Summary
...
```

### HTML

Self-contained HTML with inline CSS. Opens in any browser:

```bash
python -m src.report_generator.cli --topic "Report" --data data.csv --format html
# Output: report.html
```

The HTML output includes:
- Clean sans-serif typography
- Responsive layout (max-width: 800px)
- Styled tables with borders
- Generated timestamp

### Plain Text

Universal format for email bodies, terminal viewing, or legacy systems:

```bash
python -m src.report_generator.cli --topic "Report" --data data.csv --format text
# Output: report.txt
```

---

## 🔧 API Reference

The `report_generator` module exposes four core functions that can be used independently or composed together.

### `read_csv_data(filepath)`

Reads a CSV file and returns parsed headers and row dictionaries.

```python
from report_generator.core import read_csv_data

headers, rows = read_csv_data("sales_data.csv")
# headers: ["Region", "Q1_Revenue", "Q2_Revenue", "Growth"]
# rows: [{"Region": "North", "Q1_Revenue": "125000", ...}, ...]
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `filepath` | `str` | Path to the CSV file |

**Returns:** `tuple[list[str], list[dict]]` — Column names and list of row dictionaries.

**Raises:**
- `FileNotFoundError` — if the CSV file does not exist
- `ValueError` — if the CSV is empty or has no header row

---

### `summarize_data(headers, rows)`

Builds a comprehensive statistical summary of the dataset for LLM context.

```python
from report_generator.core import summarize_data

summary = summarize_data(headers, rows)
print(summary)
```

**Output example:**

```
Dataset Overview:
  - Total rows: 150
  - Columns (4): Region, Q1_Revenue, Q2_Revenue, Growth

  [Q1_Revenue] (numeric, 150 values):
    min=12,500.00, max=890,000.00, mean=245,320.50, sum=36,798,075.00
    median=198,750.00, stdev=142,680.33

  [Region] (text, 150 values, 5 unique):
    'North': 32
    'South': 28
    'East': 35
    'West': 30
    'Central': 25
```

**Parameters:**

| Name | Type | Description |
|------|------|-------------|
| `headers` | `list[str]` | Column names from `read_csv_data()` |
| `rows` | `list[dict]` | Row dictionaries from `read_csv_data()` |

**Returns:** `str` — Formatted statistical summary.

**Behavior:**
- Numeric columns (≥50% parseable as float): computes min, max, mean, sum; if ≥2 values also computes median and stdev
- Text columns: counts unique values; if ≤10 unique values shows frequency distribution, otherwise shows a sample of 5

---

### `generate_report(topic, data_summary, template="executive", config=None)`

Sends the statistical summary to Gemma 4 via Ollama and returns a structured Markdown report.

```python
from report_generator.core import generate_report

report = generate_report(
    topic="Q4 Sales Performance",
    data_summary=summary,
    template="executive",
    config={"llm": {"temperature": 0.5, "max_tokens": 4096}}
)
print(report)  # Full markdown report with all template sections
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `topic` | `str` | — | Report topic/title used in the prompt |
| `data_summary` | `str` | — | Statistical summary from `summarize_data()` |
| `template` | `str` | `"executive"` | Template name: `executive`, `technical`, or `summary` |
| `config` | `dict \| None` | `None` | Optional config with `llm.temperature` and `llm.max_tokens` |

**Returns:** `str` — Markdown-formatted report content.

---

### `save_report(content, output_path, topic, fmt="markdown")`

Saves the generated report to disk with appropriate formatting and metadata.

```python
from report_generator.core import save_report

path = save_report(
    content=report,
    output_path="reports/q4_sales.md",
    topic="Q4 Sales Performance",
    fmt="markdown"
)
print(f"Saved to: {path}")  # Absolute path to the saved file
```

**Parameters:**

| Name | Type | Default | Description |
|------|------|---------|-------------|
| `content` | `str` | — | Markdown report body from `generate_report()` |
| `output_path` | `str` | — | Destination file path |
| `topic` | `str` | — | Report topic for the metadata header |
| `fmt` | `str` | `"markdown"` | Output format: `markdown`, `html`, or `text` |

**Returns:** `str` — Absolute path of the saved file.

**Behavior by format:**
- **markdown**: Prepends YAML frontmatter (`title`, `generated`, `generator`)
- **html**: Converts Markdown to HTML via the `markdown` library, wraps in a styled HTML document
- **text**: Prepends a plain-text header with title and timestamp

---

## ⚙️ Configuration

Create a `config.yaml` to customize behavior:

```yaml
llm:
  model: "gemma4"
  temperature: 0.5      # Lower = more focused, higher = more creative
  max_tokens: 4096       # Maximum response length
  base_url: "http://localhost:11434"  # Ollama server address

data:
  max_rows_preview: 5    # Rows shown in CLI data preview table
  encoding: "utf-8-sig"  # CSV file encoding

output:
  default_format: "markdown"
  default_template: "executive"
```

You can also use environment variables (see `.env.example`):

```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma4
LLM_TEMPERATURE=0.5
LLM_MAX_TOKENS=4096
```

Pass a config file via the CLI:

```bash
python -m src.report_generator.cli \
  --topic "Report" --data data.csv --config config.yaml
```

---

## 📁 Project Structure

```
pdf-report-generator/
├── src/
│   └── report_generator/
│       ├── __init__.py           # Package initialization
│       ├── core.py               # Core logic: read_csv_data, summarize_data,
│       │                         #   generate_report, save_report
│       ├── cli.py                # Click CLI: argument parsing, Rich output,
│       │                         #   progress spinners, data preview
│       ├── web_ui.py             # Streamlit web interface
│       ├── config.py             # YAML + env config loading
│       └── utils.py              # Helpers: logging setup, text truncation,
│                                 #   sys.path management
├── common/
│   └── llm_client.py            # Shared Ollama HTTP client (chat, check_ollama_running)
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core functions
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # Pipeline architecture diagram
│       └── features.svg         # Feature overview grid
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup (pip install -e .)
├── requirements.txt             # Python dependencies
├── Makefile                     # Dev commands (test, lint, clean)
├── .env.example                 # Environment variable template
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

---

## 🔍 How It Works

Here's what happens when you run a report generation command, step by step:

### Step 1: CLI Initialization

The Click command parser validates all arguments. Rich renders a styled header panel showing the topic and selected template. The CLI checks that Ollama is running via `check_ollama_running()`.

### Step 2: CSV Reading

`read_csv_data(filepath)` opens the CSV with `utf-8-sig` encoding (handles BOM characters from Excel exports), validates that headers exist and at least one data row is present, then returns `(headers, rows)`.

### Step 3: Data Preview

The CLI renders a Rich table showing the first N rows of data (configurable via `config.yaml` → `data.max_rows_preview`), giving you a quick visual confirmation of what's being analyzed.

### Step 4: Statistical Profiling

`summarize_data(headers, rows)` iterates every column:

- **Numeric columns** (≥50% of values parse as float): Computes `min`, `max`, `mean`, `sum`, and if there are ≥2 values, `median` and `stdev` using Python's `statistics` module
- **Text columns**: Counts unique values. If ≤10 unique, shows full frequency distribution via `Counter.most_common()`. If >10, shows a 5-value sample

This summary string becomes the LLM's data context.

### Step 5: LLM Report Generation

`generate_report()` selects the appropriate template prompt (executive/technical/summary), injects the topic and data summary, and sends it to Gemma 4 via Ollama with a system prompt that instructs the model to act as an expert business analyst. The model returns structured Markdown.

### Step 6: Report Export

`save_report()` writes the report to disk:

- **Markdown**: Prepends YAML frontmatter with title, generation timestamp, and generator name
- **HTML**: Converts Markdown → HTML via the `markdown` library, wraps in a responsive HTML template with inline CSS
- **Text**: Prepends a plain-text header, writes raw content

### Step 7: Preview

The CLI renders a truncated preview of the generated report inside a Rich panel, so you can see the output without opening the file.

---

## 🧪 Testing

Run the full test suite:

```bash
python -m pytest tests/ -v
```

Run with coverage:

```bash
python -m pytest tests/ -v --cov=src/report_generator --cov-report=term-missing
```

Run specific test modules:

```bash
# Core logic tests (read_csv_data, summarize_data, save_report)
python -m pytest tests/test_core.py -v

# CLI integration tests
python -m pytest tests/test_cli.py -v
```

### What's Tested

| Module | Coverage |
|--------|----------|
| `core.py` | CSV reading, data summarization, report saving, HTML conversion |
| `cli.py` | Argument validation, error handling, end-to-end CLI flow |

---

## ❓ FAQ

### What data formats are supported?

Currently, the tool accepts **CSV files** (`.csv`). The CSV must have a header row as the first line, with data rows below. Both comma-separated and files with BOM markers (common from Excel exports) are handled automatically via `utf-8-sig` encoding.

### Can I customize the report templates?

Yes. The templates are defined as string constants in `REPORT_TEMPLATES` inside `src/report_generator/core.py`. Each template is a prompt string with `{topic}` and `{data_summary}` placeholders. You can modify existing templates or add new ones — just add a new key to the dictionary and pass its name via `--template`.

### How do I change the LLM model?

Edit `config.yaml` and change the `llm.model` field, or set the `OLLAMA_MODEL` environment variable. Any model available in your Ollama installation will work (e.g., `llama3`, `mistral`, `phi3`). Gemma 4 is recommended for its strong instruction-following and structured output.

### What happens with large CSV files?

The tool reads the entire CSV into memory and profiles all columns. For very large files (100k+ rows), the statistical summary remains compact since it only stores aggregate statistics, not raw data. The LLM context window is the practical limit — Gemma 4 handles summaries from datasets with hundreds of columns well.

### Can I use this programmatically?

Absolutely. The four core functions are designed to be imported and composed:

```python
from report_generator.core import (
    read_csv_data,
    summarize_data,
    generate_report,
    save_report,
)

headers, rows = read_csv_data("data.csv")
summary = summarize_data(headers, rows)
report = generate_report("My Analysis", summary, template="technical")
save_report(report, "output.md", "My Analysis", fmt="markdown")
```

### Does my data get sent to the cloud?

**No.** All processing is 100% local. The LLM runs on your machine via Ollama. The only network traffic is between the Python process and the Ollama server on `localhost:11434`. No data is transmitted externally.

### Why Gemma 4 specifically?

Gemma 4 offers an excellent balance of report quality, structured output adherence, and speed on consumer hardware. It follows the template section prompts reliably and produces well-formatted Markdown. That said, any Ollama-compatible model works — just change the config.

### How do I generate reports in batch?

Write a simple loop using the Python API:

```python
import glob
from report_generator.core import read_csv_data, summarize_data, generate_report, save_report

for csv_file in glob.glob("data/*.csv"):
    headers, rows = read_csv_data(csv_file)
    summary = summarize_data(headers, rows)
    report = generate_report(f"Analysis: {csv_file}", summary)
    save_report(report, f"reports/{csv_file.replace('.csv', '.md')}", csv_file)
```

### What's in the YAML frontmatter?

Every Markdown report includes:

```yaml
---
title: "Your Report Topic"
generated: "2025-01-15 14:30:22"
generator: "report-generator"
---
```

This metadata is compatible with Jekyll, Hugo, MkDocs, and other static site generators. The `generated` timestamp is captured at save time.

### Can I pipe output to stdout instead of a file?

The CLI always saves to a file, but you can combine it with `cat`:

```bash
python -m src.report_generator.cli --topic "Report" --data data.csv --output report.md && cat report.md
```

Or use the Python API and print directly:

```python
print(generate_report("Topic", summary))
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Clone and set up development environment
git clone https://github.com/kennedyraju55/pdf-report-generator.git
cd pdf-report-generator
pip install -r requirements.txt

# Run tests to verify everything works
python -m pytest tests/ -v

# Make your changes, then run tests again
python -m pytest tests/ -v
```

### Areas for Contribution

- **New templates** — Add domain-specific templates (financial, healthcare, marketing)
- **Additional formats** — PDF export via WeasyPrint, DOCX via python-docx
- **Data sources** — Support for Excel (`.xlsx`), JSON, or database connections
- **Visualization** — Integrate matplotlib/plotly for actual chart generation
- **Streaming** — Stream LLM output to the terminal in real-time

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Built with ❤️ as part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)**

<br/>

<img src="https://img.shields.io/badge/Project-16%20of%2090-06d6a0?style=for-the-badge&labelColor=0d1117" alt="Project 16 of 90"/>

</div>
