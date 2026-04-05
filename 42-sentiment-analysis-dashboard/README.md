<div align="center">

<img src="docs/images/banner.svg" alt="Sentiment Analysis Dashboard Banner" width="800" />

<br/><br/>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-00b4d8?style=for-the-badge)](LICENSE)
[![LLM Powered](https://img.shields.io/badge/LLM-Powered-ff6b35?style=for-the-badge&logo=google&logoColor=white)](https://ollama.ai)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](https://github.com/kennedyraju55/sentiment-analysis-dashboard/pulls)

<br/>

**Analyze sentiment from text files with AI-powered classification, trend tracking, and word cloud generation — 100% local with Ollama.**

<br/>

[Why This Tool](#-why-this-tool) · [Features](#-features) · [Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [Configuration](#-configuration) · [Testing](#-testing) · [FAQ](#-faq) · [Contributing](#-contributing)

<br/>

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection (#42)**

</div>

---

## 📖 Table of Contents

- [Why This Tool](#-why-this-tool)
- [Features](#-features)
- [Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Your First Analysis](#your-first-analysis)
- [CLI Reference](#-cli-reference)
  - [Options](#options)
  - [Usage Examples](#usage-examples)
  - [Output Formats](#output-formats)
- [Web UI](#-web-ui)
  - [Launching the Dashboard](#launching-the-dashboard)
  - [Web UI Features](#web-ui-features)
- [Architecture](#-architecture)
  - [System Overview](#system-overview)
  - [Project Structure](#project-structure)
  - [Data Flow](#data-flow)
- [API Reference](#-api-reference)
  - [File Operations](#file-operations)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Statistics & Aggregation](#statistics--aggregation)
  - [Export & Reporting](#export--reporting)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Local LLM vs Cloud](#-local-llm-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Tool

Manually reviewing text for sentiment is time-consuming and inconsistent. This tool automates the entire pipeline using a local LLM — no API keys, no cloud dependencies, and your data never leaves your machine.

| | 🔧 Manual Analysis | 🤖 Sentiment Analysis Dashboard |
|---|---|---|
| **Speed** | Minutes per entry | Seconds per entry with batch processing |
| **Consistency** | Varies by reviewer | Consistent LLM-based classification |
| **Confidence Scores** | Subjective gut feeling | Precise 0–1 confidence from the model |
| **Trend Detection** | Requires spreadsheets | Built-in sliding window trend analysis |
| **Key Phrases** | Manual highlighting | Automatic extraction with word cloud data |
| **Multi-File Compare** | Open multiple tabs | Single command compares across sources |
| **Export** | Copy-paste into docs | One-click JSON report with all metrics |
| **Privacy** | Depends on tooling | 100% local — data never leaves your machine |
| **Cost** | Paid APIs or manual labor | Free — runs on Ollama with open models |
| **Visualization** | Build your own charts | Rich CLI tables + Streamlit web dashboard |

---

## ✨ Features

<div align="center">

<img src="docs/images/features.svg" alt="Feature Grid" width="800" />

</div>

<br/>

### 🎯 Sentiment Classification

Classify text as **positive**, **negative**, or **neutral** with a confidence score between 0 and 1. Each analysis also extracts key phrases and generates a brief summary explanation.

```
😊 Positive (92% confidence) — "Great product, highly recommend!"
😞 Negative (87% confidence) — "Terrible experience, waste of money."
😐 Neutral  (74% confidence) — "The product arrived on time."
```

### 📈 Trend Analysis

Track how sentiment evolves over entries using a configurable sliding window (default: 5). This reveals patterns like improving satisfaction or emerging negative trends.

```
Window 1-5:   ██████████░░░░░  60% Positive  20% Negative  20% Neutral
Window 6-10:  ████████████░░░  80% Positive  10% Negative  10% Neutral
Window 11-15: ██████░░░░░░░░░  40% Positive  40% Negative  20% Neutral
```

### ☁️ Word Cloud Data

Extracts the top 50 most frequent words from key phrases across all analyzed entries. Words shorter than 3 characters are excluded for relevance.

### 🔄 Multi-Source Compare

Compare sentiment distributions side by side when analyzing multiple files. Instantly see which data source has more positive or negative sentiment.

### ⚡ Batch Processing

Process multiple files in a single command with real-time progress bars powered by Rich. Each file is processed sequentially with clear progress indicators.

### 📥 Export Reports

Generate comprehensive JSON reports containing:
- **Summary** — Overall sentiment distribution with counts and percentages
- **Trend** — Sliding window sentiment progression
- **Word Cloud Data** — Key phrase frequency map
- **Detailed Results** — Per-entry sentiment, confidence, key phrases, and summary

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| **Python** | 3.10+ | Runtime environment |
| **Ollama** | Latest | Local LLM inference server |
| **gemma3:4b** | Latest | Sentiment analysis model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/sentiment-analysis-dashboard.git
cd sentiment-analysis-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install as editable package (optional)
pip install -e .

# 4. Ensure Ollama is running with the model
ollama serve
ollama pull gemma3:4b
```

### Your First Analysis

Create a sample text file:

```bash
echo "This product is amazing! Best purchase I've ever made." > reviews.txt
echo "Terrible quality, broke after one day. Very disappointed." >> reviews.txt
echo "It's okay, nothing special but gets the job done." >> reviews.txt
echo "Absolutely love it! The design is beautiful and functional." >> reviews.txt
echo "Worst customer service I've ever experienced." >> reviews.txt
```

Run the analysis:

```bash
python -m src.sentiment_analyzer.cli --file reviews.txt
```

**Sample Output:**

```
╭──────────────────────────────────────────────╮
│ 💬 Sentiment Analysis Dashboard              │
╰──────────────────────────────────────────────╯
✓ Loaded 5 entries from reviews.txt
Analyzing reviews.txt... ━━━━━━━━━━━━━━━━━━━━━━ 100% 5/5

┌────────────────────────────────────────────────────────────────────────────────┐
│                        Sentiment Analysis Results                            │
├────┬──────────────────────────────────────┬──────────┬────────────┬───────────┤
│  # │ Text                                 │Sentiment │ Confidence │ Summary   │
├────┼──────────────────────────────────────┼──────────┼────────────┼───────────┤
│  1 │ This product is amazing! Best        │ 😊       │    92%     │ Highly    │
│    │ purchase I've ever made.             │ Positive │            │ positive  │
├────┼──────────────────────────────────────┼──────────┼────────────┼───────────┤
│  2 │ Terrible quality, broke after one    │ 😞       │    87%     │ Negative  │
│    │ day. Very disappointed.              │ Negative │            │ experience│
├────┼──────────────────────────────────────┼──────────┼────────────┼───────────┤
│  3 │ It's okay, nothing special but gets  │ 😐       │    74%     │ Neutral   │
│    │ the job done.                        │ Neutral  │            │ assessment│
├────┼──────────────────────────────────────┼──────────┼────────────┼───────────┤
│  4 │ Absolutely love it! The design is    │ 😊       │    95%     │ Very      │
│    │ beautiful and functional.            │ Positive │            │ positive  │
├────┼──────────────────────────────────────┼──────────┼────────────┼───────────┤
│  5 │ Worst customer service I've ever     │ 😞       │    89%     │ Strongly  │
│    │ experienced.                         │ Negative │            │ negative  │
└────┴──────────────────────────────────────┴──────────┴────────────┴───────────┘

╭───────────── 📊 Overall Summary ──────────────╮
│ Total Entries: 5                               │
│                                                │
│ 😊 Positive: 2 (40.0%)                        │
│ 😞 Negative: 2 (40.0%)                        │
│ 😐 Neutral:  1 (20.0%)                        │
│                                                │
│ Average Confidence: 87%                        │
╰────────────────────────────────────────────────╯
```

---

## 🖥️ CLI Reference

```bash
python -m src.sentiment_analyzer.cli [OPTIONS]
```

### Options

| Option | Short | Type | Default | Required | Description |
|---|---|---|---|---|---|
| `--file` | `-f` | `PATH` | — | ✅ Yes | Path to text file(s). Repeat for multiple files. |
| `--format` | `-fmt` | `Choice` | `table` | No | Output format: `table`, `json`, or `summary`. |
| `--show-trend` | — | `Flag` | `--no-trend` | No | Show sentiment trend over entries. |
| `--no-trend` | — | `Flag` | ✅ Default | No | Hide sentiment trend (default behavior). |
| `--export` | `-e` | `PATH` | `None` | No | Export full report to a JSON file. |
| `--verbose` | `-v` | `Flag` | `False` | No | Enable verbose/debug logging output. |

### Usage Examples

#### Single File Analysis

```bash
# Default table output
python -m src.sentiment_analyzer.cli --file reviews.txt

# With sentiment trend
python -m src.sentiment_analyzer.cli --file reviews.txt --show-trend
```

#### Multi-File Batch Analysis

```bash
# Compare sentiment across two files
python -m src.sentiment_analyzer.cli -f reviews.txt -f feedback.txt

# Analyze three data sources
python -m src.sentiment_analyzer.cli -f product_reviews.txt -f support_tickets.txt -f survey_responses.txt
```

#### JSON Output

```bash
# Print results as JSON
python -m src.sentiment_analyzer.cli --file reviews.txt --format json
```

**Sample JSON Output:**

```json
[
  {
    "text": "This product is amazing! Best purchase I've ever made.",
    "sentiment": "positive",
    "confidence": 0.92,
    "key_phrases": ["amazing", "best purchase"],
    "summary": "Highly positive review expressing strong satisfaction.",
    "source": "reviews.txt",
    "index": 0
  },
  {
    "text": "Terrible quality, broke after one day. Very disappointed.",
    "sentiment": "negative",
    "confidence": 0.87,
    "key_phrases": ["terrible quality", "disappointed"],
    "summary": "Negative review about product quality and durability.",
    "source": "reviews.txt",
    "index": 1
  }
]
```

#### Summary Panel

```bash
# Show only the summary panel
python -m src.sentiment_analyzer.cli --file reviews.txt --format summary
```

#### Export Report

```bash
# Export comprehensive JSON report
python -m src.sentiment_analyzer.cli --file reviews.txt --export report.json

# Full analysis with trend + export
python -m src.sentiment_analyzer.cli -f reviews.txt --show-trend -e full_report.json -v
```

### Output Formats

| Format | Description | Best For |
|---|---|---|
| `table` | Rich colored table with emojis + summary panel | Interactive terminal review |
| `json` | Raw JSON array of all results | Piping to other tools / `jq` |
| `summary` | Summary panel only (counts, percentages, avg confidence) | Quick overview at a glance |

---

## 🌐 Web UI

The Sentiment Analysis Dashboard includes a Streamlit-based web interface for interactive analysis.

### Launching the Dashboard

```bash
# Using Streamlit directly
streamlit run src/sentiment_analyzer/web_ui.py

# Using Makefile
make web
```

The dashboard will open at **http://localhost:8501** in your default browser.

### Web UI Features

| Feature | Description |
|---|---|
| 📁 **Multi-File Upload** | Drag-and-drop uploader supporting TXT and CSV files |
| 📊 **Sentiment Gauge** | Real-time distribution overview with visual metrics |
| 📋 **Results Table** | Detailed per-entry table with emoji sentiment indicators |
| 📈 **Trend Chart** | Configurable sentiment trend visualization |
| ☁️ **Key Phrases Chart** | Bar chart showing top key phrases (word cloud data) |
| 📥 **Report Download** | One-click JSON report download with all analysis data |

---

## 🏗️ Architecture

### System Overview

<div align="center">

<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800" />

</div>

<br/>

### Project Structure

```
42-sentiment-analysis-dashboard/
├── src/
│   └── sentiment_analyzer/
│       ├── __init__.py            # Package metadata and version
│       ├── core.py                # Core analysis engine
│       │                          #   ├── read_text_file()
│       │                          #   ├── read_batch_files()
│       │                          #   ├── analyze_sentiment()
│       │                          #   ├── batch_analyze()
│       │                          #   ├── compute_sentiment_distribution()
│       │                          #   ├── compute_trend_over_time()
│       │                          #   ├── extract_word_cloud_data()
│       │                          #   ├── compare_sources()
│       │                          #   └── export_report()
│       ├── cli.py                 # Click-based CLI with Rich visualization
│       │                          #   ├── display_table()
│       │                          #   ├── display_summary()
│       │                          #   ├── display_trend()
│       │                          #   ├── display_json()
│       │                          #   └── main() — CLI entry point
│       └── web_ui.py              # Streamlit web dashboard
├── tests/
│   ├── conftest.py                # Shared test fixtures
│   ├── test_core.py               # Core logic unit tests
│   └── test_cli.py                # CLI integration tests
├── common/                        # Shared LLM client (project collection)
├── docs/
│   └── images/                    # SVG assets (banner, architecture, features)
├── config.yaml                    # Application configuration
├── setup.py                       # Package setup and entry points
├── Makefile                       # Development commands (test, lint, web)
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variable template
└── README.md                      # This file
```

### Data Flow

The analysis pipeline follows a clear sequential flow:

1. **Input** — One or more text files are loaded via `read_text_file()` or `read_batch_files()`. Each non-empty line becomes an entry to analyze.

2. **LLM Analysis** — Each entry is sent to the local Ollama LLM (`gemma3:4b`) with a structured prompt requesting JSON output containing sentiment, confidence, key phrases, and a summary.

3. **JSON Parsing** — The LLM response is parsed to extract the structured sentiment data. If parsing fails, a safe fallback of `neutral` with `0.5` confidence is returned.

4. **Distribution Calculation** — `compute_sentiment_distribution()` aggregates all results into counts and percentages for positive, negative, and neutral sentiments, plus the average confidence.

5. **Trend Computation** — `compute_trend_over_time()` applies a sliding window (default size 5) across entries to show how sentiment changes over the dataset.

6. **Word Cloud Extraction** — `extract_word_cloud_data()` collects all key phrases, splits them into individual words, filters out words ≤2 characters, and returns the top 50 by frequency.

7. **Output** — Results are rendered via Rich tables/panels in the CLI, as raw JSON, or exported as a comprehensive JSON report.

---

## 📚 API Reference

All core functions are in `src/sentiment_analyzer/core.py`.

### File Operations

#### `read_text_file(file_path: str) -> list[str]`

Read a text file and return a list of non-empty, stripped lines.

```python
from src.sentiment_analyzer.core import read_text_file

lines = read_text_file("reviews.txt")
print(f"Loaded {len(lines)} entries")
# Loaded 5 entries

print(lines[0])
# "This product is amazing! Best purchase I've ever made."
```

**Raises:**
- `FileNotFoundError` — If the file does not exist
- `ValueError` — If the file is empty or has encoding errors

---

#### `read_batch_files(file_paths: list[str]) -> dict[str, list[str]]`

Read multiple text files for batch processing. Skips files that fail to load with a warning.

```python
from src.sentiment_analyzer.core import read_batch_files

all_data = read_batch_files(["reviews.txt", "feedback.txt", "missing.txt"])

for filepath, entries in all_data.items():
    print(f"{filepath}: {len(entries)} entries")
# reviews.txt: 5 entries
# feedback.txt: 12 entries
# missing.txt: 0 entries  (logged warning, skipped)
```

---

### Sentiment Analysis

#### `analyze_sentiment(text: str) -> dict`

Analyze the sentiment of a single text entry using the local LLM.

```python
from src.sentiment_analyzer.core import analyze_sentiment

result = analyze_sentiment("This product is fantastic! I love it.")
print(result)
# {
#     "sentiment": "positive",
#     "confidence": 0.93,
#     "key_phrases": ["fantastic", "love it"],
#     "summary": "Highly positive review expressing enthusiasm."
# }
```

**Returns:** A dictionary with keys:
- `sentiment` — `"positive"`, `"negative"`, or `"neutral"`
- `confidence` — Float between 0.0 and 1.0
- `key_phrases` — List of extracted key phrases
- `summary` — Brief explanation of the classification

---

#### `batch_analyze(texts: list[str], source: str = "default") -> list[dict]`

Analyze sentiment for multiple texts with source tracking.

```python
from src.sentiment_analyzer.core import batch_analyze

texts = [
    "Great quality and fast shipping!",
    "Product broke after a week.",
    "It works as expected, nothing more."
]
results = batch_analyze(texts, source="product_reviews.txt")

for r in results:
    print(f"[{r['index']}] {r['sentiment']} ({r['confidence']:.0%}) — source: {r['source']}")
# [0] positive (91%) — source: product_reviews.txt
# [1] negative (85%) — source: product_reviews.txt
# [2] neutral  (72%) — source: product_reviews.txt
```

---

### Statistics & Aggregation

#### `compute_sentiment_distribution(results: list[dict]) -> dict`

Compute sentiment distribution statistics from analysis results.

```python
from src.sentiment_analyzer.core import compute_sentiment_distribution

dist = compute_sentiment_distribution(results)
print(dist)
# {
#     "total": 5,
#     "positive": 2, "negative": 2, "neutral": 1,
#     "positive_pct": 40.0, "negative_pct": 40.0, "neutral_pct": 20.0,
#     "avg_confidence": 0.874
# }
```

---

#### `compute_trend_over_time(results: list[dict], window: int = 5) -> list[dict]`

Compute sentiment trend using a sliding window approach.

```python
from src.sentiment_analyzer.core import compute_trend_over_time

trend = compute_trend_over_time(results, window=3)
for t in trend:
    print(f"Entries {t['window_start']}-{t['window_end']}: "
          f"+{t['positive_pct']}% / -{t['negative_pct']}% / ={t['neutral_pct']}%")
# Entries 0-3: +66.7% / -33.3% / =0.0%
# Entries 3-5: +0.0% / -50.0% / =50.0%
```

---

#### `extract_word_cloud_data(results: list[dict]) -> dict[str, int]`

Extract word frequency data from key phrases for word cloud generation. Returns the top 50 words (minimum 3 characters).

```python
from src.sentiment_analyzer.core import extract_word_cloud_data

word_freq = extract_word_cloud_data(results)
print(word_freq)
# {
#     "amazing": 4, "quality": 3, "product": 3,
#     "service": 2, "love": 2, "terrible": 1, ...
# }
```

---

#### `compare_sources(source_results: dict[str, list[dict]]) -> dict`

Compare sentiment distributions across multiple data sources.

```python
from src.sentiment_analyzer.core import compare_sources

comparison = compare_sources({
    "reviews.txt": review_results,
    "support.txt": support_results,
})

for source, dist in comparison.items():
    print(f"{source}: +{dist['positive_pct']}% / -{dist['negative_pct']}%")
# reviews.txt: +60.0% / -20.0%
# support.txt: +30.0% / -50.0%
```

---

### Export & Reporting

#### `export_report(results: list[dict], texts: list[str], output_path: str) -> str`

Export a comprehensive sentiment analysis report to JSON.

```python
from src.sentiment_analyzer.core import export_report

path = export_report(results, texts, "report.json")
print(f"Report saved to {path}")
```

**Report structure:**

```json
{
  "summary": {
    "total": 5,
    "positive": 2, "negative": 2, "neutral": 1,
    "positive_pct": 40.0, "negative_pct": 40.0, "neutral_pct": 20.0,
    "avg_confidence": 0.874
  },
  "trend": [
    {
      "window_start": 0, "window_end": 5,
      "positive_pct": 40.0, "negative_pct": 40.0, "neutral_pct": 20.0,
      "avg_confidence": 0.874
    }
  ],
  "word_cloud_data": {
    "amazing": 4, "quality": 3, "product": 3
  },
  "detailed_results": [
    {
      "text": "This product is amazing!",
      "sentiment": "positive",
      "confidence": 0.92,
      "key_phrases": ["amazing", "product"],
      "summary": "Positive review.",
      "source": "reviews.txt",
      "index": 0
    }
  ]
}
```

---

## ⚙️ Configuration

The application is configured via `config.yaml` in the project root:

```yaml
# Sentiment Analysis Dashboard Configuration
# =============================================

llm:
  model: "gemma3:4b"            # Ollama model to use for analysis
  temperature: 0.2               # Lower = more deterministic responses
  max_tokens: 2000               # Maximum response length
  base_url: "http://localhost:11434"  # Ollama API endpoint

analysis:
  batch_size: 10                 # Number of entries per batch
  trend_window: 5                # Sliding window size for trend computation
  word_cloud_max_words: 50       # Maximum words in word cloud output

export:
  default_format: "json"         # Default export format
  include_raw_text: true         # Include original text in reports

logging:
  level: "INFO"                  # Logging level (DEBUG, INFO, WARNING, ERROR)
  file: null                     # Log file path (null = stdout only)
```

### Configuration Options

| Section | Key | Type | Default | Description |
|---|---|---|---|---|
| `llm` | `model` | `string` | `gemma3:4b` | Ollama model name |
| `llm` | `temperature` | `float` | `0.2` | Response randomness (0–1) |
| `llm` | `max_tokens` | `int` | `2000` | Max response tokens |
| `llm` | `base_url` | `string` | `http://localhost:11434` | Ollama server URL |
| `analysis` | `batch_size` | `int` | `10` | Entries per batch |
| `analysis` | `trend_window` | `int` | `5` | Sliding window size |
| `analysis` | `word_cloud_max_words` | `int` | `50` | Max word cloud entries |
| `export` | `default_format` | `string` | `json` | Export format |
| `export` | `include_raw_text` | `bool` | `true` | Include raw text in reports |
| `logging` | `level` | `string` | `INFO` | Log verbosity |
| `logging` | `file` | `string\|null` | `null` | Optional log file |

---

## 🧪 Testing

The project includes unit tests and integration tests using pytest.

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=src/sentiment_analyzer --cov-report=term-missing

# Run specific test file
python -m pytest tests/test_core.py -v
python -m pytest tests/test_cli.py -v

# Using Makefile
make test
make test-cov
```

### Test Structure

| File | Tests | Coverage |
|---|---|---|
| `tests/test_core.py` | Core logic — file reading, distribution, trend, word cloud | Core functions |
| `tests/test_cli.py` | CLI integration — option parsing, output formats, export | CLI entry point |
| `tests/conftest.py` | Shared fixtures — mock LLM responses, sample data | — |

### Writing Tests

Tests mock the LLM client to avoid requiring a running Ollama instance:

```python
from unittest.mock import patch

@patch("src.sentiment_analyzer.core.get_llm_client")
def test_analyze_sentiment(mock_llm):
    mock_chat = lambda msgs, **kw: '{"sentiment":"positive","confidence":0.9,"key_phrases":["great"],"summary":"Positive"}'
    mock_llm.return_value = (mock_chat, lambda: True)

    result = analyze_sentiment("This is great!")
    assert result["sentiment"] == "positive"
    assert result["confidence"] == 0.9
```

---

## ⚖️ Local LLM vs Cloud

| Feature | 🏠 Local LLM (This Tool) | ☁️ Cloud APIs (GPT, Claude) |
|---|---|---|
| **Privacy** | ✅ Data stays on your machine | ❌ Data sent to third party |
| **Cost** | ✅ Free (open models) | ❌ Pay per token / API call |
| **Latency** | ⚡ ~1-3s per entry (local) | 🐢 Network-dependent |
| **Internet** | ✅ Works fully offline | ❌ Requires internet connection |
| **Model Quality** | ⚠️ Good (gemma3:4b) | ✅ State-of-the-art models |
| **Scalability** | ⚠️ Limited by local hardware | ✅ Scales with cloud infra |
| **Customization** | ✅ Full control over prompts | ✅ Via API parameters |
| **Setup** | ⚠️ Install Ollama + model | ✅ Just an API key |
| **Compliance** | ✅ Full data sovereignty | ⚠️ Check provider policies |
| **Reproducibility** | ✅ Same model, same results | ⚠️ Model versions may change |

---

## ❓ FAQ

### Q: What happens if Ollama is not running?

The CLI checks for a running Ollama instance before analysis begins. If Ollama is not detected, you'll see a clear error message:

```
Error: Ollama is not running. Start it with: ollama serve
```

Start Ollama with `ollama serve` and ensure the `gemma3:4b` model is pulled (`ollama pull gemma3:4b`).

---

### Q: Can I use a different LLM model?

Yes! Change the `model` field in `config.yaml`:

```yaml
llm:
  model: "llama3:8b"    # or any Ollama-supported model
```

Any model available through Ollama will work. Larger models may give better results but will be slower.

---

### Q: What file format does the input need to be?

Plain text files (`.txt`) where each line is a separate entry to analyze. Empty lines are automatically skipped. The file must be UTF-8 encoded.

```
This is entry one — it will be analyzed as a single unit.
This is entry two — also analyzed separately.
A third entry with its own sentiment classification.
```

---

### Q: How does the trend window work?

The trend window groups consecutive entries and computes sentiment distribution for each group. With a window size of 5 (default), entries 1–5 form the first window, entries 6–10 the second, and so on:

```
Window 0-5:   40% positive, 40% negative, 20% neutral
Window 5-10:  60% positive, 20% negative, 20% neutral
Window 10-15: 20% positive, 60% negative, 20% neutral
```

This helps identify whether sentiment is improving, declining, or staying stable over the dataset.

---

### Q: What if the LLM returns invalid JSON?

The `analyze_sentiment()` function has built-in fallback handling. If the LLM response cannot be parsed as JSON, the entry is classified as **neutral** with **0.5 confidence**, and the raw response (truncated to 200 characters) is used as the summary. This ensures the pipeline never crashes due to malformed LLM output.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/sentiment-analysis-dashboard.git
   cd sentiment-analysis-dashboard
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Install** development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```
5. **Make** your changes and add tests
6. **Run** the test suite:
   ```bash
   python -m pytest tests/ -v
   ```
7. **Commit** your changes with a descriptive message:
   ```bash
   git commit -m "feat: add your feature description"
   ```
8. **Push** and open a Pull Request:
   ```bash
   git push origin feature/your-feature-name
   ```

### Development Commands

```bash
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run linters
make web           # Launch Streamlit web UI
```

### Code Style

- Follow PEP 8 conventions
- Use type hints for function signatures
- Write docstrings for all public functions
- Add tests for new functionality

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

Built with ❤️ using [Ollama](https://ollama.ai) · [Click](https://click.palletsprojects.com/) · [Rich](https://rich.readthedocs.io/) · [Streamlit](https://streamlit.io/)

**Part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) · Project #42**

<br/>

<sub>⭐ Star this repo if you find it useful!</sub>

</div>
