<div align="center">

<img src="docs/images/banner.svg" alt="Stock Report Generator — AI-Powered Technical Analysis & Risk Assessment" width="800"/>

<br/>
<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-ff6b35?style=for-the-badge&logo=llama&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Web_UI-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)

[![Tests](https://img.shields.io/github/actions/workflow/status/kennedyraju55/stock-report-generator/tests.yml?label=tests&style=flat-square&logo=githubactions&logoColor=white)](https://github.com/kennedyraju55/stock-report-generator/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-ff6b35?style=flat-square)](https://github.com/kennedyraju55/stock-report-generator/pulls)
[![GitHub Stars](https://img.shields.io/github/stars/kennedyraju55/stock-report-generator?style=flat-square&color=ff6b35)](https://github.com/kennedyraju55/stock-report-generator/stargazers)

**Professional stock analysis reports with technical indicators and risk assessment — powered by local LLM**

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

<br/>

[Features](#-features) · [Quick Start](#-quick-start) · [CLI Usage](#-cli-usage) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [FAQ](#-faq) · [Contributing](#-contributing)

</div>

<br/>

---

<br/>

## 🤔 Why Stock Report Generator?

<table>
<tr>
<td width="50%">

### ❌ Without This Tool

- Manually calculating RSI, MACD, Bollinger Bands in spreadsheets
- Paying for expensive financial API subscriptions
- No unified view across multiple stock holdings
- Writing analysis reports from scratch every time
- Sending sensitive portfolio data to cloud services

</td>
<td width="50%">

### ✅ With Stock Report Generator

- **One command** generates complete technical analysis
- **100% free** — runs entirely on your local machine
- **Multi-ticker comparison** across your entire portfolio
- **AI-powered narrative reports** generated automatically
- **Complete privacy** — your data never leaves your machine

</td>
</tr>
</table>

<br/>

---

<br/>

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Core Features — Smart Price Detection, Technical Indicators, Risk Assessment, Multi-Ticker Comparison, SMA & Volatility, AI Reports" width="800"/>
</div>

<br/>

| Feature | Description | Details |
|---------|-------------|---------|
| 🔍 **Smart Price Detection** | Auto-detect close price columns | Handles `Close`, `Adj Close`, `close_price`, and more CSV formats |
| 📈 **Technical Indicators** | Industry-standard signals | RSI (14-period), Bollinger Bands (20-period), MACD with signal crossover |
| ⚠️ **Risk Assessment** | Composite risk scoring | Score 0–100 based on volatility, price movement, RSI extremes, down-day ratio |
| 🔄 **Multi-Ticker Compare** | Side-by-side portfolio analysis | Compare metrics, indicators, and risk across unlimited tickers |
| 📊 **SMA & Volatility** | Trend and volatility tracking | 5-day & 20-day SMA, daily return distribution, up/down day counts |
| 🤖 **AI Narrative Reports** | LLM-generated analysis | Professional reports with market outlook via Ollama (Gemma 3 4B) |
| 📉 **Interactive Charts** | Visual price analysis | Streamlit-powered charts with trend lines and indicator overlays |
| 🖥️ **Dual Interface** | CLI + Web UI | Rich terminal output with color-coded tables **and** Streamlit dashboard |
| ⚡ **100% Local** | Complete privacy | All processing runs locally — zero data sent to external services |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Python](https://www.python.org/downloads/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai) | Latest | Local LLM backend |
| Gemma 3 4B model | — | AI report generation |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/stock-report-generator.git
cd stock-report-generator

# Install dependencies
pip install -r requirements.txt

# Or install as editable package
pip install -e .
```

### 2. Start Ollama

```bash
# Pull the model (one-time setup)
ollama pull gemma3:4b

# Verify it's running
ollama list
```

### 3. Run Your First Analysis

```bash
# Analyze a single stock
python -m src.stock_reporter.cli --file data/aapl.csv --ticker AAPL
```

### 📊 Example Output

```
╭──────────────────────────────────────────────────────────────╮
│                    📈 AAPL — Stock Metrics                   │
├──────────────────────┬───────────────────────────────────────┤
│ Current Price        │                             $192.53   │
│ Period High          │                             $198.23   │
│ Period Low           │                             $164.08   │
│ Average Price        │                             $181.34   │
│ Price Change         │                             +17.28%   │
│ SMA (5-day)          │                             $191.47   │
│ SMA (20-day)         │                             $186.92   │
│ Volatility           │                               2.14%   │
│ Up Days              │                                  67   │
│ Down Days            │                                  53   │
╰──────────────────────┴───────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────╮
│                 📈 Technical Indicators — AAPL               │
├──────────────────────┬───────────────────────────────────────┤
│ RSI (14)             │  62.4  ■■■■■■░░░░  Neutral            │
│ Bollinger Upper      │                             $196.18   │
│ Bollinger Middle     │                             $186.92   │
│ Bollinger Lower      │                             $177.66   │
│ MACD Line            │                               1.847   │
│ MACD Signal          │                               1.523   │
│ MACD Histogram       │                               0.324   │
│ MACD Signal          │                          ▲ Bullish     │
╰──────────────────────┴───────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────╮
│                    ⚠️  Risk Assessment — AAPL                │
├──────────────────────┬───────────────────────────────────────┤
│ Risk Score           │  38/100  ████████░░░░░░░  Moderate    │
│ Volatility Factor    │                          Low (2.14%)  │
│ RSI Factor           │                         Neutral Zone  │
│ Down Day Ratio       │                               44.2%   │
│ Price Movement       │                         Bullish Trend │
╰──────────────────────┴───────────────────────────────────────╯

╭──────────────────────────────────────────────────────────────╮
│                  🤖 AI Analysis Report — AAPL                │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  AAPL has demonstrated strong bullish momentum over the      │
│  analysis period, gaining 17.28%. The current price of       │
│  $192.53 sits above both the 5-day ($191.47) and 20-day      │
│  ($186.92) moving averages, confirming the uptrend.          │
│                                                              │
│  Technical indicators paint a cautiously optimistic picture: │
│  RSI at 62.4 suggests room for further upside before         │
│  overbought conditions, while the MACD bullish crossover     │
│  reinforces positive momentum. The stock is trading near     │
│  the upper Bollinger Band, indicating strong but potentially │
│  extended price action.                                      │
│                                                              │
│  Risk assessment scores a moderate 38/100, supported by      │
│  low volatility (2.14%) and a favorable up/down day ratio.   │
│                                                              │
│  Outlook: Cautiously bullish with support at $186.92 (SMA20) │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
```

> **Note:** Output is color-coded in the terminal — green for bullish signals, red for bearish, yellow for neutral.

<br/>

---

<br/>

## 🖥️ CLI Usage

### Basic Commands

```bash
# Single stock analysis (full report)
python -m src.stock_reporter.cli --file aapl.csv --ticker AAPL

# Multi-ticker comparison
python -m src.stock_reporter.cli \
  --file aapl.csv --ticker AAPL \
  --file goog.csv --ticker GOOG \
  --file msft.csv --ticker MSFT

# Metrics only (skip indicators and risk)
python -m src.stock_reporter.cli --file aapl.csv --ticker AAPL \
  --no-indicators --no-risk

# Verbose mode for debugging
python -m src.stock_reporter.cli --file aapl.csv --ticker AAPL --verbose
```

### All CLI Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | `PATH` | *required* | Path to stock data CSV file. Repeatable for multiple tickers. |
| `--ticker` | `-t` | `TEXT` | *required* | Stock ticker symbol. Must match the number of `--file` arguments. |
| `--show-indicators` | — | `flag` | `True` | Display technical indicators (RSI, Bollinger Bands, MACD). |
| `--no-indicators` | — | `flag` | — | Hide technical indicators section. |
| `--show-risk` | — | `flag` | `True` | Display risk assessment panel with score and factors. |
| `--no-risk` | — | `flag` | — | Hide risk assessment section. |
| `--verbose` | `-v` | `flag` | `False` | Enable verbose logging output for debugging. |

### CSV File Format

The tool auto-detects price columns. Your CSV should have at minimum a close price column:

```csv
Date,Open,High,Low,Close,Volume
2024-01-02,185.12,186.40,184.03,185.64,45032100
2024-01-03,184.22,185.15,183.89,184.25,42580600
2024-01-04,182.15,183.56,181.91,181.91,49899100
```

**Supported column names:** `Close`, `close`, `Adj Close`, `adj_close`, `close_price`, `closing_price`, `Last`, `last_price`

### Multi-Ticker Comparison Output

When analyzing multiple tickers, the tool generates a comparison table:

```
╭───────────────────────────────────────────────────────────────────╮
│                   📊 Multi-Ticker Comparison                      │
├──────────┬──────────┬──────────┬──────────┬──────────┬────────────┤
│ Ticker   │ Price    │ Change%  │ SMA(20)  │ Vol      │ Risk Score │
├──────────┼──────────┼──────────┼──────────┼──────────┼────────────┤
│ AAPL     │ $192.53  │ +17.28%  │ $186.92  │ 2.14%    │ 38/100     │
│ GOOG     │ $141.80  │ +12.45%  │ $138.64  │ 1.89%    │ 32/100     │
│ MSFT     │ $378.91  │ +21.63%  │ $368.15  │ 1.76%    │ 29/100     │
╰──────────┴──────────┴──────────┴──────────┴──────────┴────────────╯
```

<br/>

---

<br/>

## 🌐 Web UI

Launch the interactive Streamlit dashboard:

```bash
# Start the web UI
streamlit run src/stock_reporter/web_ui.py

# Or use the Makefile shortcut
make web
```

The dashboard opens at `http://localhost:8501` and includes:

| Section | Description |
|---------|-------------|
| 📊 **Key Metrics Dashboard** | Current price, change%, high/low, SMA(5), SMA(20), volatility |
| 📉 **Interactive Price Chart** | Candlestick/line chart with zoom, pan, and hover details |
| 📈 **Technical Indicators** | RSI gauge, Bollinger Band overlay, MACD histogram |
| ⚠️ **Risk Meter** | Visual score bar (0–100) with breakdown of risk factors |
| 🤖 **AI Analysis Panel** | Full narrative report generated by Ollama |
| 🔄 **Comparison Table** | Side-by-side metrics when multiple CSVs are uploaded |

### Web UI Workflow

1. **Upload** one or more stock CSV files via the sidebar
2. **Enter** corresponding ticker symbols
3. **Toggle** indicators and risk assessment on/off
4. **View** the complete analysis dashboard
5. **Compare** multiple tickers in the comparison tab

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Pipeline — CSV Input → Price Detection → Metric Engine → Technical Indicators → Risk Assessment → Multi-Ticker Comparison → LLM Report → Rich Output" width="800"/>
</div>

<br/>

### Pipeline Flow

```
Stock CSV(s) ──→ load_stock_data()
                        │
                        ▼
               _find_close_column()  ──→  Auto-detect price column
                        │
                        ▼
               _extract_prices()     ──→  Clean & parse numeric prices
                        │
                        ▼
               compute_metrics()     ──→  SMA5, SMA20, volatility, returns
                        │
                        ▼
          compute_technical_indicators()
                  │    │    │
                  ▼    ▼    ▼
                RSI  BB   MACD     ──→  Signal interpretation
                        │
                        ▼
               assess_risk()         ──→  Risk score 0-100
                        │
                        ▼
              compare_tickers()      ──→  Multi-stock comparison
                        │
                        ▼
              generate_report()      ──→  Ollama LLM narrative
                        │
                        ▼
               Rich Terminal / Streamlit Output
```

### Project Structure

```
44-stock-report-generator/
├── src/
│   └── stock_reporter/
│       ├── __init__.py              # Package metadata & version
│       ├── core.py                  # Core engine: metrics, indicators, risk, reports
│       ├── cli.py                   # Click CLI with Rich terminal output
│       └── web_ui.py               # Streamlit web dashboard
├── tests/
│   ├── conftest.py                  # Shared pytest fixtures & sample data
│   ├── test_core.py                 # Unit tests for core logic
│   └── test_cli.py                  # Integration tests for CLI
├── docs/
│   └── images/
│       ├── banner.svg               # Project banner graphic
│       ├── architecture.svg         # Architecture diagram
│       └── features.svg             # Feature overview graphic
├── config.yaml                      # LLM & analysis configuration
├── setup.py                         # Package setup & entry points
├── Makefile                         # Development commands
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variable template
└── README.md                        # This file
```

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **LLM Backend** | Ollama + Gemma 3 4B | AI-powered report narrative generation |
| **Core Engine** | Python 3.10+ | Metrics computation, technical indicators, risk scoring |
| **CLI Framework** | Click | Command-line argument parsing & multi-ticker support |
| **Terminal UI** | Rich | Color-coded tables, panels, progress bars |
| **Web UI** | Streamlit | Interactive dashboard with charts & risk meters |
| **Testing** | pytest | Unit & integration test suite |
| **Code Style** | Black + Ruff | Consistent formatting & linting |

<br/>

---

<br/>

## 📖 API Reference

### `load_stock_data(file_path: str) → list[dict]`

Load stock data from a CSV file into a list of dictionaries.

```python
from src.stock_reporter.core import load_stock_data

data = load_stock_data("data/aapl.csv")
# Returns: [{"Date": "2024-01-02", "Close": "185.64", ...}, ...]
```

**Parameters:**
- `file_path` — Path to the CSV file

**Returns:** List of dictionaries, one per row

---

### `compute_metrics(data: list[dict]) → dict`

Calculate core financial metrics from stock data.

```python
from src.stock_reporter.core import compute_metrics

metrics = compute_metrics(data)
print(metrics["current_price"])   # 192.53
print(metrics["sma_5"])           # 191.47
print(metrics["volatility"])      # 2.14
print(metrics["change_percent"])  # 17.28
```

**Returns dictionary with:**

| Key | Type | Description |
|-----|------|-------------|
| `current_price` | `float` | Most recent closing price |
| `high` | `float` | Period high price |
| `low` | `float` | Period low price |
| `average` | `float` | Mean closing price |
| `change_percent` | `float` | Price change percentage over period |
| `sma_5` | `float` | 5-day Simple Moving Average |
| `sma_20` | `float` | 20-day Simple Moving Average |
| `volatility` | `float` | Standard deviation of daily returns (%) |
| `daily_returns` | `list[float]` | List of daily percentage returns |
| `up_days` | `int` | Number of positive return days |
| `down_days` | `int` | Number of negative return days |

---

### `compute_technical_indicators(data: list[dict]) → dict`

Calculate advanced technical indicators with signal interpretation.

```python
from src.stock_reporter.core import compute_technical_indicators

indicators = compute_technical_indicators(data)
print(indicators["rsi"])              # 62.4
print(indicators["macd_signal_text"]) # "Bullish"
```

**Returns dictionary with:**

| Key | Type | Description |
|-----|------|-------------|
| `rsi` | `float` | Relative Strength Index (14-period) |
| `rsi_signal` | `str` | RSI interpretation: `Overbought`, `Oversold`, `Neutral` |
| `bollinger_upper` | `float` | Upper Bollinger Band (20-period, 2 std dev) |
| `bollinger_middle` | `float` | Middle Bollinger Band (= SMA 20) |
| `bollinger_lower` | `float` | Lower Bollinger Band |
| `macd_line` | `float` | MACD line (12-EMA minus 26-EMA) |
| `macd_signal` | `float` | Signal line (9-EMA of MACD) |
| `macd_histogram` | `float` | MACD histogram (MACD minus Signal) |
| `macd_signal_text` | `str` | Signal interpretation: `Bullish`, `Bearish` |

---

### `assess_risk(metrics: dict, indicators: dict) → dict`

Compute a composite risk score based on multiple factors.

```python
from src.stock_reporter.core import assess_risk

risk = assess_risk(metrics, indicators)
print(risk["score"])  # 38
print(risk["level"])  # "Moderate"
```

**Risk scoring factors:**
- **Volatility** — Higher volatility increases risk score
- **Price movement** — Large swings in either direction
- **RSI extremes** — Overbought (>70) or oversold (<30) conditions
- **Down day ratio** — Proportion of negative return days

**Returns dictionary with:**

| Key | Type | Description |
|-----|------|-------------|
| `score` | `int` | Composite risk score (0–100) |
| `level` | `str` | Risk level: `Low`, `Moderate`, `High`, `Very High` |
| `factors` | `list[dict]` | Breakdown of individual risk factor contributions |

---

### `compare_tickers(datasets: list[dict]) → dict`

Compare metrics across multiple stock datasets.

```python
from src.stock_reporter.core import compare_tickers

comparison = compare_tickers([
    {"ticker": "AAPL", "metrics": aapl_metrics},
    {"ticker": "GOOG", "metrics": goog_metrics},
])
```

---

### `generate_report(data, metrics, ticker, indicators, risk) → str`

Generate an AI-powered narrative analysis report using Ollama.

```python
from src.stock_reporter.core import generate_report

report = generate_report(
    data=data,
    metrics=metrics,
    ticker="AAPL",
    indicators=indicators,
    risk=risk,
)
print(report)  # Multi-paragraph professional analysis
```

**Parameters:**
- `data` — Raw stock data (list of dicts)
- `metrics` — Output from `compute_metrics()`
- `ticker` — Stock ticker symbol string
- `indicators` — Output from `compute_technical_indicators()`
- `risk` — Output from `assess_risk()`

**Returns:** Narrative analysis string generated by the LLM

<br/>

---

<br/>

## ⚙️ Configuration

The application reads configuration from `config.yaml`:

```yaml
# config.yaml — Stock Report Generator Configuration

llm:
  model: "gemma3:4b"           # Ollama model to use for report generation
  temperature: 0.4              # LLM creativity (0.0 = deterministic, 1.0 = creative)
  base_url: "http://localhost:11434"  # Ollama API endpoint

analysis:
  rsi_period: 14                # RSI calculation period (standard: 14)
  bollinger_period: 20          # Bollinger Bands period (standard: 20)
  bollinger_std: 2              # Bollinger Bands standard deviations
  sma_short: 5                  # Short-term SMA period
  sma_long: 20                  # Long-term SMA period

risk:
  volatility_high_threshold: 5.0    # Volatility % above which risk increases
  rsi_overbought: 70                # RSI overbought threshold
  rsi_oversold: 30                  # RSI oversold threshold
  down_day_ratio_threshold: 0.55    # Down day ratio above which risk increases
```

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# .env
OLLAMA_BASE_URL=http://localhost:11434    # Ollama server URL
OLLAMA_MODEL=gemma3:4b                    # Default model
LOG_LEVEL=INFO                            # Logging level
```

<br/>

---

<br/>

## 🧪 Testing

### Run Tests

```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run with coverage report
make test-cov

# Run specific test file
python -m pytest tests/test_core.py -v

# Run specific test by name
python -m pytest tests/ -k "test_compute_metrics" -v
```

### Test Structure

```
tests/
├── conftest.py       # Shared fixtures: sample CSV data, mock Ollama responses
├── test_core.py      # Unit tests for core.py functions
│   ├── test_load_stock_data
│   ├── test_find_close_column
│   ├── test_extract_prices
│   ├── test_compute_metrics
│   ├── test_compute_technical_indicators
│   ├── test_assess_risk
│   └── test_compare_tickers
└── test_cli.py       # CLI integration tests using Click's CliRunner
    ├── test_single_ticker
    ├── test_multi_ticker
    ├── test_no_indicators_flag
    └── test_verbose_mode
```

### Makefile Commands

```bash
make test         # Run pytest
make test-cov     # Run pytest with coverage
make lint         # Run linters (black, ruff)
make format       # Auto-format code
make web          # Start Streamlit web UI
make clean        # Remove __pycache__ and .pytest_cache
```

<br/>

---

<br/>

## 🏠 Local vs Cloud

| Aspect | Stock Report Generator (Local) | Cloud Alternatives |
|--------|-------------------------------|-------------------|
| **Cost** | Free forever | $20–200/month subscriptions |
| **Privacy** | Data never leaves your machine | Data sent to external servers |
| **Speed** | Depends on local hardware | Depends on API rate limits |
| **Customization** | Full source code access | Limited to provider's features |
| **Models** | Any Ollama-compatible model | Locked to provider's models |
| **Offline** | Works without internet | Requires internet connection |
| **Dependencies** | Python + Ollama only | Complex API key management |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What CSV format does the tool accept?</strong></summary>

The tool accepts any CSV file with a recognizable close price column. It auto-detects columns named `Close`, `close`, `Adj Close`, `adj_close`, `close_price`, `closing_price`, `Last`, or `last_price`. The CSV should have one row per trading day with at least the close price. Additional columns like `Open`, `High`, `Low`, and `Volume` are optional.

</details>

<details>
<summary><strong>Can I use a different LLM model instead of Gemma 3 4B?</strong></summary>

Yes. Any model available through Ollama works. Update the `model` field in `config.yaml`:

```yaml
llm:
  model: "llama3:8b"   # or "mistral", "phi3", "qwen2", etc.
```

Then pull the model: `ollama pull llama3:8b`

</details>

<details>
<summary><strong>How is the risk score calculated?</strong></summary>

The risk score (0–100) is a weighted composite of four factors:
1. **Volatility** — Standard deviation of daily returns vs. threshold
2. **Price movement** — Magnitude of price change over the analysis period
3. **RSI extremes** — Distance from neutral zone (30–70 range)
4. **Down day ratio** — Proportion of negative return days vs. positive

Scores map to levels: **Low** (0–25), **Moderate** (26–50), **High** (51–75), **Very High** (76–100).

</details>

<details>
<summary><strong>What do the MACD signals mean?</strong></summary>

- **Bullish** — MACD line crosses above the signal line, suggesting upward momentum
- **Bearish** — MACD line crosses below the signal line, suggesting downward momentum

The MACD histogram visualizes the distance between these lines. Growing histogram bars indicate strengthening momentum; shrinking bars indicate weakening momentum.

</details>

<details>
<summary><strong>Can I analyze stocks without an LLM running?</strong></summary>

Yes. The metrics computation, technical indicators, and risk assessment all run without Ollama. Only the AI narrative report section requires a running LLM. Use `--no-indicators` and `--no-risk` flags if you only want raw metrics, or simply run the analysis — it will gracefully handle the case where Ollama is not available by skipping the narrative report.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/stock-report-generator.git
cd stock-report-generator

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify setup
python -m pytest tests/ -v
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Write** tests for new functionality
4. **Ensure** all tests pass: `python -m pytest tests/ -v`
5. **Format** code: `black .` and `ruff check .`
6. **Commit** with a descriptive message
7. **Push** and open a Pull Request

### Areas for Contribution

- 📊 Additional technical indicators (Stochastic, ADX, OBV)
- 📈 Enhanced charting capabilities
- 🌍 International market support
- 📱 Mobile-responsive web UI
- 🔌 Data source integrations (Yahoo Finance, Alpha Vantage)
- 📝 Report export formats (PDF, HTML, Markdown)

<br/>

---

<br/>

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

<br/>

---

<div align="center">

<br/>

**Built with ❤️ as part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<br/>

<sub>

[⬆ Back to Top](#-features) · [Report Bug](https://github.com/kennedyraju55/stock-report-generator/issues) · [Request Feature](https://github.com/kennedyraju55/stock-report-generator/issues)

</sub>

<br/>

<img src="https://img.shields.io/badge/Made_with-Python-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Powered_by-Ollama-ff6b35?style=flat-square" alt="Ollama"/>
<img src="https://img.shields.io/badge/UI-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>

</div>
