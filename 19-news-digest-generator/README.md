<div align="center">

<img src="docs/images/banner.svg" alt="News Digest Generator Banner" width="800" />

<br/>
<br/>

<img src="https://img.shields.io/badge/Gemma_4-Ollama-orange?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/Rich-Terminal_UI-purple?style=flat-square" alt="Rich"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/>
<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

<br/>
<br/>

[Features](#-features) · [Quick Start](#-quick-start) · [Usage](#-usage) · [Architecture](#-architecture) · [Configuration](#%EF%B8%8F-configuration) · [API Reference](#-api-reference) · [FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

We are drowning in information but starving for insight. Every morning brings hundreds
of headlines across dozens of sources — technology breakthroughs, policy changes,
market shifts, scientific discoveries — all competing for your attention. Manually
reading, categorizing, and making sense of it all is a full-time job.

**News Digest Generator** solves this by putting a local LLM to work as your personal
news editor. Drop a folder of `.txt` articles on it and get back a structured,
categorized digest with sentiment analysis and trend detection — all processed
**100% locally** on your machine. No API keys. No cloud services. No data leaving
your network.

### The Problem

- 📰 **Information overload** — too many articles, not enough time
- 🔍 **No structure** — raw articles lack categorization and priority
- 🎭 **Hidden sentiment** — hard to gauge the tone across many articles at once
- 📊 **Missed trends** — overarching themes get lost in individual stories
- 🔒 **Privacy concerns** — sending proprietary or sensitive news to cloud APIs

### The Solution

A single CLI command that reads your news files, groups them by topic, generates
a polished daily or weekly digest, analyzes sentiment per article, and surfaces
trending themes — all powered by Gemma 4 running locally via Ollama.

<br/>

---

<br/>

## ✨ Features

<div align="center">

<img src="docs/images/features.svg" alt="Features Overview" width="800" />

</div>

<br/>

| Feature | Description |
|---|---|
| 🗂️ **Smart Categorization** | Auto-groups articles into exactly *N* topic categories using LLM-powered classification. Each group includes a topic name, category label, article list, and a 2–3 sentence summary. |
| 📋 **Daily / Weekly Digests** | Generates a professional digest with Key Headlines (3–5), Topic Summaries (paragraph per topic), optional Sentiment Analysis, optional Trending Themes, and a forward-looking Outlook section. |
| 🎭 **Sentiment Analysis** | Per-article sentiment scoring (Positive / Negative / Neutral) with a brief explanation for each, plus an overall sentiment summary across all articles. |
| 📈 **Trend Detection** | Identifies overarching themes and emerging trends that span multiple articles, helping you see the bigger picture. |
| 📂 **Batch Processing** | Point the CLI at any folder — every `.txt` file is automatically discovered via glob, read, and processed in a single run. |
| 🔒 **100% Private** | Everything runs locally through Ollama. Your news sources, article content, and generated digests never leave your machine. |
| 💾 **Markdown Export** | Save the full digest (categorization + digest body) to a Markdown file for archiving, sharing, or further editing. |
| ⚙️ **YAML Configuration** | Customize default categories, topic count, digest format, sentiment/trend toggles, LLM temperature, and token limits via `config.yaml`. |
| 🖥️ **Rich Terminal UI** | Beautiful console output with tables, panels, trees, and progress spinners powered by the Rich library. |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Minimum Version | Purpose |
|---|---|---|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | — | Language model |

### 1. Clone the Repository

```bash
git clone https://github.com/kennedyraju55/news-digest-generator.git
cd news-digest-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

The project uses the following Python libraries:

| Library | Role |
|---|---|
| `click` | CLI framework — argument parsing, option handling, help text |
| `rich` | Terminal formatting — tables, panels, trees, spinners |
| `glob` (stdlib) | File discovery — finds all `.txt` files in the source folder |
| `pyyaml` | Configuration — loads and merges `config.yaml` settings |
| `requests` | HTTP — communicates with the Ollama API |

### 3. Start Ollama and Pull the Model

```bash
ollama serve
ollama pull gemma4
```

### 4. Run Your First Digest

```bash
python -m src.news_digest.cli --sources path/to/news_folder/
```

That's it. The CLI reads every `.txt` file in the folder, categorizes articles into
5 topic groups (default), generates a daily digest, and renders the results in the
terminal with Rich formatting.

<br/>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/news-digest-generator.git
cd news-digest-generator
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

<br/>


---

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.news_digest.api:app --reload --port 8000

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

## 📖 Usage

### CLI Command

The project exposes a **single CLI command** with multiple options:

```bash
python -m src.news_digest.cli [OPTIONS]
```

### Options Reference

| Option | Required | Default | Description |
|---|---|---|---|
| `--sources` | **Yes** | — | Path to folder containing `.txt` news article files |
| `--topics` | No | `5` | Number of topic groups for categorization |
| `--output` | No | — | File path to save the digest as Markdown |
| `--format` | No | `daily` | Digest format: `daily` or `weekly` |
| `--sentiment` | No | — | Flag — include per-article sentiment analysis |
| `--config` | No | — | Path to a custom `config.yaml` file |
| `--verbose` | No | — | Flag — enable debug-level logging |

### Usage Examples

#### Basic Daily Digest

```bash
python -m src.news_digest.cli --sources ./news/
```

Reads all `.txt` files from `./news/`, groups them into 5 topics, and prints a
daily digest to the terminal.

#### Weekly Digest with Sentiment

```bash
python -m src.news_digest.cli \
    --sources ./news/ \
    --format weekly \
    --sentiment
```

Generates a weekly-format digest and appends a full sentiment analysis section
showing per-article mood (Positive / Negative / Neutral) with explanations.

#### Custom Topic Count with Export

```bash
python -m src.news_digest.cli \
    --sources ./news/ \
    --topics 3 \
    --output reports/digest-2025-01-15.md
```

Groups articles into exactly 3 topics and saves the complete output (categorization
+ digest) to a Markdown file.

#### Full Options

```bash
python -m src.news_digest.cli \
    --sources ./news/ \
    --topics 8 \
    --format weekly \
    --sentiment \
    --output weekly-digest.md \
    --config custom-config.yaml \
    --verbose
```

Uses a custom config file, requests 8 topic groups, weekly format, includes
sentiment analysis, saves to a file, and enables debug logging.

### Web UI

```bash
streamlit run src/news_digest/web_ui.py
```

The Streamlit interface provides a browser-based experience with source folder
selection, digest preview, category filters, and sentiment charts.

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">

<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800" />

</div>

<br/>

### Processing Pipeline

The digest generation follows a linear pipeline:

```
News Articles (.txt)
    │
    ▼
┌──────────────────┐
│  read_news_files │  ← Glob-based file discovery & reading
│  (sources_dir)   │
└──────┬───────────┘
       │ list of {filename, content} dicts
       ▼
┌───────────────────────┐
│  categorize_articles  │  ← LLM groups into N topic categories
│  (articles, num_topics│
│   config=None)        │
└──────┬────────────────┘
       │ categorization text (Markdown)
       ▼
┌───────────────────────┐
│  generate_digest      │  ← LLM produces structured digest
│  (articles,           │
│   categorization,     │
│   digest_format,      │
│   config=None)        │
└──────┬────────────────┘
       │ digest text (Markdown)
       ▼
┌───────────────────────┐
│  save_output          │  ← Write to Markdown file
│  (filepath,           │
│   categorization,     │
│   digest)             │
└───────────────────────┘
```

### Module Breakdown

| Module | File | Responsibility |
|---|---|---|
| **Core Logic** | `src/news_digest/core.py` | `read_news_files`, `categorize_articles`, `generate_digest`, `analyze_sentiment`, `save_output` |
| **CLI Interface** | `src/news_digest/cli.py` | Click command definition, Rich console rendering, orchestration flow |
| **Configuration** | `src/news_digest/config.py` | YAML loading, deep merge with defaults, environment variable overrides |
| **Utilities** | `src/news_digest/utils.py` | Logging setup, `sys.path` management, digest header formatting |
| **Web UI** | `src/news_digest/web_ui.py` | Streamlit interface with folder picker, digest preview, filters |

### How the LLM Is Used

All LLM interactions go through the shared `common.llm_client` module, which
communicates with a locally running Ollama instance. The project uses Gemma 4 as its
default model, but any Ollama-compatible model can be swapped in via `config.yaml`
or the `LLM_MODEL` environment variable.

Each core function constructs a task-specific prompt:

- **`categorize_articles`** — instructs the LLM to act as a news editor, grouping
  articles into exactly `num_topics` categories with structured output
  (`## Topic:`, `**Category:**`, `**Articles:**`, `**Summary:**`)
- **`generate_digest`** — asks the LLM to produce a professional digest with
  Key Headlines, Topic Summaries, and optional Sentiment / Trending Themes / Outlook
  sections
- **`analyze_sentiment`** — sends article excerpts (first 500 chars each) for
  per-article Positive / Negative / Neutral classification with explanations

<br/>

---

<br/>

## ⚙️ Configuration

### config.yaml

```yaml
# News Digest Generator Configuration
llm:
  model: gemma4
  temperature: 0.4
  max_tokens: 4096

digest:
  default_topics: 5
  formats:
    - daily
    - weekly
  default_format: daily
  categories:
    - Technology
    - Business
    - Politics
    - Science
    - Sports
    - Health
    - Entertainment
    - World
  enable_sentiment: true
  enable_trends: true
```

### Configuration Options Explained

| Key | Type | Default | Description |
|---|---|---|---|
| `llm.model` | string | `gemma4` | Ollama model name |
| `llm.temperature` | float | `0.4` | Controls response creativity (0.0–1.0) |
| `llm.max_tokens` | int | `4096` | Maximum tokens per LLM response |
| `digest.default_topics` | int | `5` | Default number of topic groups |
| `digest.formats` | list | `[daily, weekly]` | Available digest formats |
| `digest.default_format` | string | `daily` | Format used when `--format` is omitted |
| `digest.categories` | list | 8 categories | Suggested category labels for the LLM |
| `digest.enable_sentiment` | bool | `true` | Include sentiment section in digest |
| `digest.enable_trends` | bool | `true` | Include trending themes section in digest |

### Environment Variable Overrides

| Variable | Overrides | Example |
|---|---|---|
| `LLM_MODEL` | `llm.model` | `export LLM_MODEL=llama3` |
| `LLM_TEMPERATURE` | `llm.temperature` | `export LLM_TEMPERATURE=0.7` |

### Configuration Resolution Order

1. **Defaults** — hardcoded in `config.py` via `DEFAULT_CONFIG`
2. **YAML file** — deep-merged on top of defaults (auto-discovered or via `--config`)
3. **Environment variables** — override specific LLM settings

<br/>

---

<br/>

## 📚 API Reference

### `read_news_files(sources_dir)`

Reads all `.txt` files from the specified directory using `glob`.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `sources_dir` | `str` | Path to the folder containing `.txt` news files |

**Returns:** `list[dict]` — each dict has `filename` (str) and `content` (str) keys.

**Raises:**

| Exception | When |
|---|---|
| `FileNotFoundError` | `sources_dir` does not exist |
| `ValueError` | No `.txt` files found, or all files are empty |

**Example:**

```python
from news_digest.core import read_news_files

articles = read_news_files("./news_folder/")
# [
#     {"filename": "tech-ai-breakthrough.txt", "content": "OpenAI announced..."},
#     {"filename": "market-update.txt", "content": "Markets rallied today..."},
# ]
```

---

### `categorize_articles(articles, num_topics, config=None)`

Groups articles into exactly `num_topics` categories using the LLM.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `articles` | `list[dict]` | — | Article dicts from `read_news_files` |
| `num_topics` | `int` | — | Exact number of topic groups to create |
| `config` | `dict \| None` | `None` | Optional configuration dictionary |

**Returns:** `str` — Markdown-formatted categorization with the following structure
for each topic:

```markdown
## Topic: <topic name>
**Category:** <category label>
**Articles:** <comma-separated filenames>
**Summary:** <2-3 sentence summary>
```

**Example:**

```python
from news_digest.core import read_news_files, categorize_articles

articles = read_news_files("./news/")
categorization = categorize_articles(articles, num_topics=3)
print(categorization)
```

---

### `generate_digest(articles, categorization, digest_format="daily", config=None)`

Generates a structured news digest from the categorized articles.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `articles` | `list[dict]` | — | Article dicts from `read_news_files` |
| `categorization` | `str` | — | Output from `categorize_articles` |
| `digest_format` | `str` | `"daily"` | Either `"daily"` or `"weekly"` |
| `config` | `dict \| None` | `None` | Optional configuration dictionary |

**Returns:** `str` — Markdown digest containing:

| Section | Always Included | Description |
|---|---|---|
| **Key Headlines** | ✅ | The 3–5 most important headlines |
| **Topic Summaries** | ✅ | A polished paragraph for each topic group |
| **Sentiment Analysis** | When `digest.enable_sentiment` is `true` | Overall sentiment per topic |
| **Trending Themes** | When `digest.enable_trends` is `true` | Overarching themes and emerging trends |
| **Outlook** | ✅ | A forward-looking paragraph |

**Example:**

```python
from news_digest.core import read_news_files, categorize_articles, generate_digest

articles = read_news_files("./news/")
categorization = categorize_articles(articles, num_topics=5)
digest = generate_digest(articles, categorization, digest_format="weekly")
print(digest)
```

---

### `analyze_sentiment(articles, config=None)`

Performs per-article sentiment analysis and produces an overall summary.

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `articles` | `list[dict]` | — | Article dicts from `read_news_files` |
| `config` | `dict \| None` | `None` | Optional configuration dictionary |

**Returns:** `str` — Markdown-formatted sentiment analysis with:

- Per-article line: `**Filename**: sentiment (Positive/Negative/Neutral) - brief explanation`
- Overall sentiment summary paragraph

**Example:**

```python
from news_digest.core import read_news_files, analyze_sentiment

articles = read_news_files("./news/")
sentiment_report = analyze_sentiment(articles)
print(sentiment_report)
```

---

### `save_output(filepath, categorization, digest)`

Saves the categorization and digest to a Markdown file.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `filepath` | `str` | Destination file path |
| `categorization` | `str` | Output from `categorize_articles` |
| `digest` | `str` | Output from `generate_digest` |

**Returns:** `None`

**Output file structure:**

```markdown
# News Digest

## Topic Categorization

<categorization content>

---

## Full Digest

<digest content>
```

**Example:**

```python
from news_digest.core import save_output

save_output("reports/digest.md", categorization, digest)
```

<br/>

---

<br/>

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src/news_digest --cov-report=term-missing

# Run a specific test file
python -m pytest tests/test_core.py -v
```

<br/>

---

<br/>

## 📁 Project Structure

```
19-news-digest-generator/
├── src/
│   └── news_digest/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Core logic: read, categorize, digest, sentiment, save
│       ├── cli.py               # Click CLI command + Rich console rendering
│       ├── web_ui.py            # Streamlit web interface
│       ├── config.py            # YAML config loading + defaults + env overrides
│       └── utils.py             # Logging setup, sys.path, header formatting
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core functions
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # Pipeline architecture diagram
│       └── features.svg         # Feature highlights grid
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup with entry point
├── requirements.txt             # Python dependencies
├── Makefile                     # Common tasks (test, lint, run)
├── .env.example                 # Environment variable template
├── .gitignore
└── README.md                    # This file
```

<br/>

---

<br/>

## 📋 Preparing News Sources

The generator expects plain-text `.txt` files, one article per file:

```
news_folder/
├── 2025-01-15-ai-regulation.txt
├── 2025-01-15-market-rally.txt
├── 2025-01-15-climate-summit.txt
├── 2025-01-15-space-launch.txt
└── 2025-01-15-health-study.txt
```

### Tips for Best Results

- **One article per file** — each `.txt` file should contain a single news article
- **Include headlines** — start each file with the article headline for better
  categorization accuracy
- **Meaningful filenames** — names like `tech-ai-breakthrough.txt` help the LLM
  associate filenames with categories
- **Consistent encoding** — use UTF-8 encoding (the reader uses `errors="replace"`
  as a fallback)
- **Skip empty files** — the reader automatically filters out empty files, but
  keeping your folder clean helps

### Minimum Requirements

- At least **one non-empty** `.txt` file is required
- The `--topics` count is automatically capped to the number of articles if you
  request more topics than articles

<br/>

---

<br/>

## 🔄 Digest Output Sections

When you generate a digest, the output follows this structure depending on your
configuration:

### Always Included

| Section | Content |
|---|---|
| **Key Headlines** | The 3–5 most important headlines across all articles |
| **Topic Summaries** | One polished paragraph per topic group |
| **Outlook** | A forward-looking paragraph about expected developments |

### Optional (Controlled by Config)

| Section | Config Key | Default |
|---|---|---|
| **Sentiment Analysis** | `digest.enable_sentiment` | `true` |
| **Trending Themes** | `digest.enable_trends` | `true` |

These sections are included in the digest prompt when their respective config
flags are set to `true`. You can also trigger standalone sentiment analysis using
the `--sentiment` CLI flag, which calls `analyze_sentiment` separately and displays
the results in a dedicated Rich panel.

<br/>

---

<br/>

## ❓ FAQ

### What news sources does this support?

Any plain-text `.txt` files. The generator does not fetch news from the internet —
you provide the article files. This makes it compatible with any source: RSS feed
exports, copy-pasted articles, web scraper output, internal company reports, or
research papers.

### How often should I run it?

That's up to you. Use `--format daily` for a morning briefing from overnight news,
or `--format weekly` for an end-of-week recap. The format flag changes the LLM
prompt to produce a style appropriate for the cadence.

### Can it detect bias in news articles?

Not directly. The sentiment analysis identifies the **tone** of each article
(Positive / Negative / Neutral) with a brief explanation, which can surface
biased framing. However, it is not a dedicated bias-detection tool. The LLM
interprets tone, not journalistic objectivity.

### Does this require an internet connection?

Only for the initial setup (cloning the repo, installing dependencies, and pulling
the Gemma 4 model). After that, everything runs **100% offline**. Ollama serves the
model locally, and no data is sent to any external service.

### How many articles can it handle at once?

There's no hard limit in the code. The practical limit depends on your LLM's context
window. With Gemma 4's default context size, processing 20–50 articles in a single
run works well. For larger collections, consider splitting into subfolders and
running multiple digests.

### Can I use a different LLM model?

Yes. Change the model in `config.yaml`:

```yaml
llm:
  model: llama3    # or any model available via `ollama list`
```

Or override at runtime:

```bash
export LLM_MODEL=mistral
python -m src.news_digest.cli --sources ./news/
```

### What happens if the sources folder is empty?

The `read_news_files` function raises a `ValueError` with the message
*"No .txt files found in: <path>"*. The CLI catches this and displays a
user-friendly error via Rich.

### Can I customize the topic categories?

Yes. The `digest.categories` list in `config.yaml` provides **suggested** category
labels to the LLM. The model uses them if applicable but is not strictly limited
to them — it can create new category names if the articles don't fit the suggestions.

```yaml
digest:
  categories:
    - Artificial Intelligence
    - Cybersecurity
    - Cloud Computing
    - DevOps
    - Open Source
```

### How does the topic count work?

The `--topics` flag (or `digest.default_topics` in config) tells the LLM to
create **exactly** that many groups. If you request more topics than articles,
the CLI automatically adjusts the count down to match the article count and
prints a warning.

### Where are the digests saved?

Only when you use the `--output` flag. The `save_output` function writes a
Markdown file with two sections: *Topic Categorization* and *Full Digest*,
separated by a horizontal rule.

<br/>

---

<br/>

## 🛠️ Development

### Setting Up for Development

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Or install dev requirements directly
pip install -r requirements.txt
pip install pytest pytest-cov
```

### Running Tests

```bash
# All tests with verbose output
python -m pytest tests/ -v

# With coverage report
python -m pytest tests/ --cov=src/news_digest --cov-report=term-missing
```

### Using the Makefile

```bash
make test        # Run test suite
make lint        # Run linters
make run         # Run with default settings
```

### Entry Point

The package defines a console script entry point in `setup.py`:

```python
entry_points={
    "console_scripts": [
        "news-digest=news_digest.cli:main",
    ],
}
```

After `pip install -e .`, you can run:

```bash
news-digest --sources ./news/ --topics 3 --sentiment
```

<br/>

---

<br/>

## 🔒 Privacy & Security

This project is designed with privacy as a core principle:

- **No cloud APIs** — all LLM processing happens locally via Ollama
- **No telemetry** — the application does not phone home or collect usage data
- **No network access** — after initial setup, the tool works fully offline
- **Your data stays yours** — article content is never transmitted outside your machine
- **Open source** — every line of code is auditable

This makes it suitable for processing sensitive or proprietary news sources,
internal company communications, or any content you don't want leaving your
network.

<br/>

---

<br/>

## 📄 License

This project is part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection.

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

<br/>

---

<br/>

<div align="center">

**Built with** 🧠 **Gemma 4** + 🦙 **Ollama** + 🐍 **Python**

<br/>

<sub>
📰 News Digest Generator — Transform raw articles into structured intelligence.<br/>
Part of <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> by <a href="https://github.com/kennedyraju55">kennedyraju55</a>
</sub>

</div>
