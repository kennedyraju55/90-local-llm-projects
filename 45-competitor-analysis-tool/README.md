<div align="center">

<img src="docs/images/banner.svg" alt="Competitor Analysis Tool - AI-Powered Competitive Intelligence & Strategy" width="800" />

<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-7209b7?style=for-the-badge)](LICENSE)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-FF6F00?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Web_UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge)](https://github.com/psf/black)

[![GitHub Stars](https://img.shields.io/github/stars/kennedyraju55/competitor-analysis-tool?style=flat-square&color=7209b7)](https://github.com/kennedyraju55/competitor-analysis-tool/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/kennedyraju55/competitor-analysis-tool?style=flat-square&color=9d4edd)](https://github.com/kennedyraju55/competitor-analysis-tool/network)
[![GitHub Issues](https://img.shields.io/github/issues/kennedyraju55/competitor-analysis-tool?style=flat-square&color=c77dff)](https://github.com/kennedyraju55/competitor-analysis-tool/issues)
[![Last Commit](https://img.shields.io/github/last-commit/kennedyraju55/competitor-analysis-tool?style=flat-square&color=7209b7)](https://github.com/kennedyraju55/competitor-analysis-tool/commits)

**SWOT analysis, feature comparison, pricing analysis, market positioning &amp; strategic recommendations — powered entirely by local LLM**

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

<br/>

[Features](#-features) · [Quick Start](#-quick-start) · [CLI Usage](#-cli-usage) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [Configuration](#-configuration) · [FAQ](#-frequently-asked-questions) · [Contributing](#-contributing)

</div>

<br/>

---

## 🤔 Why Competitor Analysis Tool?

<table>
<tr>
<td width="50%">

### ❌ Without This Tool

- Hours of **manual research** across competitor websites
- Subjective, **inconsistent** SWOT assessments
- No structured **feature-by-feature** comparison
- Pricing data scattered across **spreadsheets**
- Market positioning based on **gut feeling**
- Action items that are **vague** and unactionable
- Sensitive competitive data sent to **cloud APIs**

</td>
<td width="50%">

### ✅ With This Tool

- **Instant** AI-generated competitive intelligence
- Structured, **repeatable** SWOT with 4-quadrant display
- **Emoji-coded** feature matrix (✅❌🔶) at a glance
- Pricing tiers classified as **budget/mid-range/premium**
- Market positioning on **Price×Quality** axes (1-10 scale)
- **5-8 prioritized** action items with timeline & outcomes
- **100% local** — your data never leaves your machine

</td>
</tr>
</table>

---

## ✨ Features

<div align="center">

<img src="docs/images/features.svg" alt="Key Features Overview" width="800" />

</div>

<br/>

<table>
<tr>
<td align="center" width="33%">

### 📊 SWOT Analysis

Generate comprehensive **Strengths, Weaknesses, Opportunities & Threats** with color-coded 4-quadrant Rich panels. Each quadrant contains 3+ actionable insights from the LLM.

</td>
<td align="center" width="33%">

### 📋 Feature Matrix

Side-by-side **feature comparison** across 8-10 key industry features. Visual indicators: ✅ (yes), ❌ (no), 🔶 (partial) with summary analysis.

</td>
<td align="center" width="33%">

### 💰 Pricing Analysis

Compare **pricing models, price ranges, value propositions** and tier classifications. Auto-categorized as budget (🟢), mid-range (🟡), or premium (🔴).

</td>
</tr>
<tr>
<td align="center" width="33%">

### 🗺️ Market Positioning

Map competitors on **Price × Quality** axes (1-10 scale). Identifies market quadrants, gap opportunities, and positioning summary.

</td>
<td align="center" width="33%">

### 🎯 Action Items

**5-8 prioritized** strategic action items with priority level (critical/high/medium/low), timeline, category, and expected outcomes.

</td>
<td align="center" width="33%">

### 📝 Recommendations

Top **5 strategic recommendations** with detailed rationale, priority levels, and markdown-formatted insights from the LLM.

</td>
</tr>
</table>

<br/>

### Additional Capabilities

| Capability | Description |
|:-----------|:------------|
| 🖥️ **Rich CLI** | Beautiful terminal output with Rich tables, panels, and color-coded SWOT grids |
| 🌐 **Streamlit Web UI** | Interactive dashboard with input forms, SWOT cards, scatter charts |
| 📄 **Full Report Mode** | Comprehensive competitive comparison with markdown-formatted analysis |
| ⚡ **100% Local Processing** | All LLM inference runs locally via Ollama — zero cloud dependencies |
| 🔧 **Configurable** | YAML-based config for model, temperature, max competitors, feature limits |
| 🧪 **Fully Tested** | pytest suite with fixtures, core logic tests, and CLI integration tests |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://www.python.org/downloads/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai) | Latest | Local LLM inference |
| [gemma3:4b](https://ollama.ai/library/gemma3) | 4B params | Default language model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/competitor-analysis-tool.git
cd competitor-analysis-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Or install as editable package
pip install -e .

# 4. Pull the LLM model (if not already available)
ollama pull gemma3:4b

# 5. Ensure Ollama is running
ollama serve
```

### Your First Analysis

```bash
python -m src.competitor_analyzer.cli \
  --company "Acme Corp" \
  --competitors "TechRival,CloudCompete,DataStar" \
  --industry "Cloud Computing"
```

<details>
<summary>📋 <strong>Example Output</strong> (click to expand)</summary>

```
┌──────────────────────────────────────┐
│ 🏢 Competitor Analysis Tool          │
└──────────────────────────────────────┘
Company:     Acme Corp
Competitors: TechRival, CloudCompete, DataStar
Industry:    Cloud Computing

╭────────── 💪 Strengths ──────────╮╭────────── ⚠️ Weaknesses ──────────╮
│ • Strong brand recognition       ││ • Limited global data centers     │
│ • Competitive pricing model      ││ • Smaller enterprise sales team   │
│ • Advanced API integrations      ││ • Narrow product portfolio        │
╰──────────────────────────────────╯╰──────────────────────────────────╯
╭───────── 🎯 Opportunities ──────╮╭────────── 🔥 Threats ────────────╮
│ • Edge computing expansion       ││ • Aggressive pricing from rivals  │
│ • AI/ML integration demand       ││ • Market consolidation trends     │
│ • Hybrid cloud adoption growth   ││ • Regulatory compliance costs     │
╰──────────────────────────────────╯╰──────────────────────────────────╯

┌─────────────────── 📋 Feature Comparison Matrix ───────────────────┐
│ Feature          │ Acme Corp │ TechRival │ CloudCompete │ DataStar │
├──────────────────┼───────────┼───────────┼──────────────┼──────────┤
│ Auto-scaling     │    ✅     │    ✅     │     ✅       │    🔶    │
│ Multi-region     │    ✅     │    ✅     │     ✅       │    ❌    │
│ Serverless       │    🔶     │    ✅     │     ❌       │    ✅    │
│ Edge Computing   │    ❌     │    🔶     │     ✅       │    ❌    │
│ AI/ML Platform   │    ✅     │    ✅     │     🔶       │    ✅    │
└──────────────────┴───────────┴───────────┴──────────────┴──────────┘

┌──────────────────── 💰 Pricing Comparison ────────────────────────┐
│ Company      │ Model          │ Price Range │ Tier     │ Value    │
├──────────────┼────────────────┼─────────────┼──────────┼──────────┤
│ Acme Corp    │ Pay-as-you-go  │ $50-500/mo  │ Mid-Range│ Flexible │
│ TechRival    │ Subscription   │ $99-999/mo  │ Premium  │ Full-svc │
│ CloudCompete │ Freemium       │ $0-200/mo   │ Budget   │ Entry    │
│ DataStar     │ Usage-based    │ $30-300/mo  │ Budget   │ Scale    │
└──────────────┴────────────────┴─────────────┴──────────┴──────────┘

┌────────────────────── 🎯 Action Items ────────────────────────────┐
│ # │ Title                      │ Priority │ Timeline   │ Category │
├───┼────────────────────────────┼──────────┼────────────┼──────────┤
│ 1 │ Launch edge computing      │ CRITICAL │ Immediate  │ Product  │
│ 2 │ Expand enterprise sales    │ HIGH     │ Short-term │ Strategy │
│ 3 │ Develop AI/ML toolkit      │ HIGH     │ Short-term │ Product  │
│ 4 │ Implement freemium tier    │ MEDIUM   │ Long-term  │ Strategy │
│ 5 │ Regional compliance plan   │ MEDIUM   │ Short-term │ Ops      │
└───┴────────────────────────────┴──────────┴────────────┴──────────┘
```

</details>

---

## 🖥️ CLI Usage

### Basic Commands

```bash
# Full analysis (default: all sections enabled)
python -m src.competitor_analyzer.cli \
  --company "Acme" \
  --competitors "Comp1,Comp2,Comp3" \
  --industry "SaaS"

# SWOT analysis only
python -m src.competitor_analyzer.cli \
  -c "Acme" -comp "Comp1,Comp2" -i "SaaS" \
  --swot-only

# With feature matrix and pricing only
python -m src.competitor_analyzer.cli \
  -c "Acme" -comp "Comp1" -i "tech" \
  --show-features --show-pricing --swot-only

# Full report with action items and verbose logging
python -m src.competitor_analyzer.cli \
  -c "Acme" -comp "Comp1,Comp2" -i "tech" \
  --show-actions --verbose
```

### CLI Options Reference

| Option | Short | Required | Default | Description |
|:-------|:------|:---------|:--------|:------------|
| `--company` | `-c` | ✅ | — | Your company or product name |
| `--competitors` | `-comp` | ✅ | — | Comma-separated list of competitor names |
| `--industry` | `-i` | ✅ | — | Industry sector for context |
| `--full-report` | — | ❌ | `True` | Generate complete competitive comparison report |
| `--swot-only` | — | ❌ | `False` | Generate only the SWOT analysis |
| `--show-features` | — | ❌ | `True` | Include feature comparison matrix |
| `--no-features` | — | ❌ | — | Skip feature comparison matrix |
| `--show-pricing` | — | ❌ | `True` | Include pricing comparison table |
| `--no-pricing` | — | ❌ | — | Skip pricing comparison |
| `--show-actions` | — | ❌ | `True` | Include prioritized action items |
| `--no-actions` | — | ❌ | — | Skip action items |
| `--verbose` | `-v` | ❌ | `False` | Enable debug-level logging output |

### CLI Analysis Modes

| Mode | Command | Output |
|:-----|:--------|:-------|
| **Full Report** | `--full-report` (default) | SWOT + Features + Pricing + Actions + Comparison + Recommendations |
| **SWOT Only** | `--swot-only` | Only the 4-quadrant SWOT analysis |
| **Custom Mix** | `--swot-only --show-features` | SWOT + Feature matrix only |
| **Quick Scan** | `--swot-only --no-features --no-pricing --no-actions` | Minimal SWOT output |

### Using the Entry Point

```bash
# If installed with pip install -e .
competitor-analyzer -c "Acme" -comp "Rival1,Rival2" -i "FinTech"
```

---

## 🌐 Web UI

The Streamlit-based web interface provides an interactive dashboard for competitor analysis.

### Launching the Web UI

```bash
# Direct launch
streamlit run src/competitor_analyzer/web_ui.py

# Using Makefile
make web
```

### Web UI Features

| Feature | Description |
|:--------|:------------|
| 🏢 **Input Form** | Company name, competitor list, and industry selector |
| 📊 **SWOT Cards** | Color-coded quadrant cards (green/red/blue/yellow) |
| 📋 **Feature Table** | Interactive feature matrix with emoji indicators |
| 💰 **Pricing Table** | Side-by-side pricing comparison with tier badges |
| 🗺️ **Position Chart** | Scatter plot on Price × Quality axes |
| 🎯 **Action Items** | Sortable list with priority and timeline columns |
| 📝 **Full Report** | Markdown-rendered competitive comparison report |

---

## 🏗️ Architecture

<div align="center">

<img src="docs/images/architecture.svg" alt="Architecture Flow Diagram" width="800" />

</div>

<br/>

### Pipeline Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────────────┐
│  Company     │───▶│  SWOT       │───▶│  Feature    │───▶│  Pricing     │
│  Info Input  │    │  Engine     │    │  Matrix     │    │  Analyzer    │
└─────────────┘    └─────────────┘    └─────────────┘    └──────┬───────┘
                                                                │
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────▼───────┐
│  Rich       │◀───│  Strategic  │◀───│  Action     │◀───│  Market      │
│  Report     │    │  Recommend. │    │  Items      │    │  Positioning │
└─────────────┘    └─────────────┘    └─────────────┘    └──────────────┘
```

### Project Structure

```
45-competitor-analysis-tool/
├── src/
│   └── competitor_analyzer/
│       ├── __init__.py            # Package metadata & version
│       ├── core.py                # Core analysis engine
│       │   ├── load_config()      # YAML configuration loader
│       │   ├── get_llm_client()   # Ollama LLM client setup
│       │   ├── generate_swot()    # SWOT analysis generation
│       │   ├── generate_feature_matrix()     # Feature comparison
│       │   ├── generate_pricing_comparison() # Pricing analysis
│       │   ├── generate_market_positioning() # Market mapping
│       │   ├── generate_comparison()         # Full comparison report
│       │   ├── generate_action_items()       # Prioritized actions
│       │   └── generate_recommendations()    # Strategic recommendations
│       ├── cli.py                 # Rich CLI interface
│       │   ├── display_swot()     # 4-quadrant SWOT panels
│       │   ├── display_feature_matrix()  # Feature comparison table
│       │   ├── display_pricing()  # Pricing comparison table
│       │   ├── display_action_items()    # Action items table
│       │   └── main()             # Click CLI entry point
│       └── web_ui.py              # Streamlit web dashboard
├── tests/
│   ├── conftest.py                # Shared pytest fixtures
│   ├── test_core.py               # Core logic unit tests
│   └── test_cli.py                # CLI integration tests
├── common/                        # Shared LLM client utilities
├── docs/
│   └── images/
│       ├── banner.svg             # Project banner
│       ├── architecture.svg       # Architecture diagram
│       └── features.svg           # Features overview
├── config.yaml                    # Application configuration
├── setup.py                       # Package setup & entry points
├── Makefile                       # Development commands
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variable template
└── README.md                      # This file
```

### How It Works

1. **Input Validation** — CLI/Web UI collects company name, competitors, and industry sector
2. **LLM Connection** — Connects to local Ollama instance running `gemma3:4b` model
3. **SWOT Generation** — Sends structured prompts; parses JSON response for S/W/O/T arrays
4. **Feature Matrix** — Generates 8-10 feature comparisons with yes/no/partial classifications
5. **Pricing Analysis** — Compares pricing models and classifies into budget/mid-range/premium tiers
6. **Market Positioning** — Maps companies on Price×Quality axes (1-10), identifies market gaps
7. **Action Items** — Generates 5-8 prioritized actions with timeline, category, and expected outcomes
8. **Recommendations** — Top 5 strategic recommendations with rationale and priority levels
9. **Rich Display** — Output rendered via Rich panels/tables (CLI) or Streamlit components (Web)

---

## 📚 API Reference

### Core Functions

All core functions are in `src/competitor_analyzer/core.py`.

#### `generate_swot(company, competitors, industry)`

Generate a comprehensive SWOT analysis for the company vs competitors.

```python
from competitor_analyzer.core import generate_swot

swot = generate_swot(
    company="Acme Corp",
    competitors=["TechRival", "CloudCompete"],
    industry="Cloud Computing"
)

# Returns:
# {
#     "strengths": ["Strong brand recognition", "Competitive pricing", ...],
#     "weaknesses": ["Limited data centers", "Small sales team", ...],
#     "opportunities": ["Edge computing expansion", "AI/ML demand", ...],
#     "threats": ["Aggressive rival pricing", "Market consolidation", ...]
# }
```

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `company` | `str` | Your company or product name |
| `competitors` | `list[str]` | List of competitor names |
| `industry` | `str` | Industry sector for context |

**Returns:** `dict` with keys `strengths`, `weaknesses`, `opportunities`, `threats` (each a list of strings)

---

#### `generate_feature_matrix(company, competitors, industry)`

Generate a feature-by-feature comparison matrix.

```python
from competitor_analyzer.core import generate_feature_matrix

features = generate_feature_matrix(
    company="Acme Corp",
    competitors=["TechRival", "CloudCompete"],
    industry="Cloud Computing"
)

# Returns:
# {
#     "features": ["Auto-scaling", "Multi-region", "Serverless", ...],
#     "matrix": {
#         "Acme Corp": {"Auto-scaling": "yes", "Multi-region": "yes", ...},
#         "TechRival": {"Auto-scaling": "yes", "Multi-region": "partial", ...},
#         "CloudCompete": {"Auto-scaling": "no", "Multi-region": "yes", ...}
#     },
#     "summary": "Acme Corp leads in core features..."
# }
```

**Returns:** `dict` with `features` (list), `matrix` (nested dict with yes/no/partial), `summary` (str)

---

#### `generate_pricing_comparison(company, competitors, industry)`

Compare pricing strategies across companies.

```python
from competitor_analyzer.core import generate_pricing_comparison

pricing = generate_pricing_comparison(
    company="Acme Corp",
    competitors=["TechRival", "CloudCompete"],
    industry="Cloud Computing"
)

# Returns:
# {
#     "companies": [
#         {
#             "name": "Acme Corp",
#             "pricing_model": "Pay-as-you-go",
#             "price_range": "$50-500/month",
#             "value_proposition": "Flexible scaling",
#             "tier": "mid-range"
#         },
#         ...
#     ],
#     "recommendation": "Consider introducing a freemium tier..."
# }
```

**Returns:** `dict` with `companies` (list of pricing objects) and `recommendation` (str)

---

#### `generate_market_positioning(company, competitors, industry)`

Map competitors on Price × Quality axes.

```python
from competitor_analyzer.core import generate_market_positioning

positioning = generate_market_positioning(
    company="Acme Corp",
    competitors=["TechRival", "CloudCompete"],
    industry="Cloud Computing"
)

# Returns:
# {
#     "positions": [
#         {"company": "Acme Corp", "x_axis": 5, "y_axis": 7,
#          "x_label": "Price (Low→High)", "y_label": "Quality (Low→High)",
#          "quadrant": "Mid-price, High-quality"},
#         ...
#     ],
#     "market_gaps": ["Low-price premium quality gap", ...],
#     "positioning_summary": "Market shows clear segmentation..."
# }
```

**Returns:** `dict` with `positions` (list), `market_gaps` (list), `positioning_summary` (str)

---

#### `generate_action_items(company, competitors, industry, swot, features=None)`

Generate 5-8 prioritized strategic action items based on SWOT results.

```python
from competitor_analyzer.core import generate_swot, generate_action_items

swot = generate_swot("Acme", ["Rival"], "SaaS")
actions = generate_action_items("Acme", ["Rival"], "SaaS", swot)

# Returns:
# [
#     {
#         "title": "Launch edge computing platform",
#         "description": "Develop and launch edge computing...",
#         "priority": "critical",
#         "timeline": "immediate",
#         "category": "product",
#         "expected_outcome": "Capture 15% of edge market..."
#     },
#     ...
# ]
```

**Returns:** `list[dict]` — each item has `title`, `description`, `priority`, `timeline`, `category`, `expected_outcome`

---

#### `generate_comparison(company, competitors, industry)`

Generate a full markdown-formatted competitive comparison report.

```python
from competitor_analyzer.core import generate_comparison

report = generate_comparison("Acme", ["Rival1", "Rival2"], "FinTech")
# Returns: str (markdown-formatted comparison report)
```

---

#### `generate_recommendations(company, competitors, industry, swot)`

Generate top 5 strategic recommendations with rationale.

```python
from competitor_analyzer.core import generate_swot, generate_recommendations

swot = generate_swot("Acme", ["Rival"], "SaaS")
recs = generate_recommendations("Acme", ["Rival"], "SaaS", swot)
# Returns: str (markdown-formatted strategic recommendations)
```

---

### Configuration Function

#### `load_config(config_path=None)`

Load application configuration from YAML file.

```python
from competitor_analyzer.core import load_config

config = load_config()  # Loads from default config.yaml
config = load_config("/path/to/custom-config.yaml")  # Custom path
```

---

## ⚙️ Configuration

Configuration is managed via `config.yaml` in the project root:

```yaml
# Competitor Analysis Tool Configuration
# ========================================

llm:
  model: "gemma3:4b"       # Ollama model to use
  temperature: 0.4          # LLM creativity (0.0-1.0)
  max_tokens: 4000          # Maximum response tokens
  base_url: "http://localhost:11434"  # Ollama API endpoint

analysis:
  max_competitors: 10              # Maximum competitors to analyze
  feature_matrix_max_features: 15  # Max features in comparison matrix

output:
  default_format: "rich"    # Output format: "rich" for CLI tables
  export_format: "json"     # Export format for data

logging:
  level: "INFO"             # Logging level: DEBUG, INFO, WARNING, ERROR
  file: null                # Log file path (null = console only)
```

### Configuration Options

| Section | Key | Default | Description |
|:--------|:----|:--------|:------------|
| `llm.model` | `model` | `gemma3:4b` | Ollama model name |
| `llm.temperature` | `temperature` | `0.4` | Creativity level (lower = more focused) |
| `llm.max_tokens` | `max_tokens` | `4000` | Maximum LLM response length |
| `llm.base_url` | `base_url` | `http://localhost:11434` | Ollama API endpoint |
| `analysis.max_competitors` | `max_competitors` | `10` | Max number of competitors |
| `analysis.feature_matrix_max_features` | `feature_matrix_max_features` | `15` | Max features in matrix |
| `output.default_format` | `default_format` | `rich` | CLI output format |
| `output.export_format` | `export_format` | `json` | Data export format |
| `logging.level` | `level` | `INFO` | Logging verbosity |

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/competitor_analyzer --cov-report=term-missing

# Using Makefile
make test          # Run tests
make test-cov      # Run tests with coverage
```

### Test Structure

| File | Tests | Description |
|:-----|:------|:------------|
| `tests/conftest.py` | — | Shared fixtures: mock LLM responses, sample data |
| `tests/test_core.py` | Core logic | SWOT generation, feature matrix, pricing, positioning |
| `tests/test_cli.py` | CLI integration | Click command parsing, output formatting, error handling |

### Development Commands

```bash
make install       # Install package in editable mode
make dev           # Install with dev dependencies
make test          # Run pytest
make test-cov      # Run pytest with coverage
make lint          # Run flake8 + mypy
make format        # Run black formatter
make clean         # Remove __pycache__ and build artifacts
make run           # Show CLI help
make web           # Launch Streamlit web UI
```

---

## 🏠 Local vs Cloud

| Aspect | This Tool (Local) | Cloud Alternatives |
|:-------|:-------------------|:-------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after setup | ❌ Pay per API call |
| **Speed** | 🔶 Depends on local hardware | ✅ Fast cloud GPUs |
| **Internet** | ✅ Works fully offline | ❌ Requires internet connection |
| **Model** | Gemma 3 4B via Ollama | GPT-4, Claude, etc. |
| **Customization** | ✅ Full control over prompts & config | 🔶 Limited by API constraints |
| **Data Retention** | ✅ Nothing stored externally | ❌ May be used for training |
| **Setup** | 🔶 Requires Ollama install | ✅ Just an API key |

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>1. What LLM models are supported?</strong></summary>

Any model available through Ollama can be used. The default is `gemma3:4b`, but you can change it in `config.yaml` under `llm.model`. Popular alternatives include `llama3:8b`, `mistral:7b`, and `phi3:mini`. Larger models produce better analysis but require more RAM and are slower.

</details>

<details>
<summary><strong>2. How many competitors can I analyze at once?</strong></summary>

The default limit is 10 competitors (configurable via `analysis.max_competitors` in `config.yaml`). In practice, 3-5 competitors produce the best results since the LLM can give more detailed per-competitor analysis. Each competitor adds to the prompt length and processing time.

</details>

<details>
<summary><strong>3. Can I use this without Ollama?</strong></summary>

The tool is designed to work with Ollama for local LLM inference. To use a different LLM backend, you would need to modify the `get_llm_client()` function in `core.py` and the shared `common/llm_client.py` module to point to your preferred API. The prompt structure and JSON parsing will work with any model that follows instructions.

</details>

<details>
<summary><strong>4. How accurate are the analyses?</strong></summary>

The accuracy depends on the LLM's training data. The tool works best with well-known companies and industries. For niche or very recent competitors, the LLM may generate generic or inaccurate insights. Always treat the output as a **starting point** for your own research, not as a definitive analysis. The SWOT and feature comparisons are structured to be directionally useful.

</details>

<details>
<summary><strong>5. Why do I get "Analysis unavailable" in the output?</strong></summary>

This happens when the LLM response cannot be parsed as valid JSON. Common causes:
- **Ollama not running** — start it with `ollama serve`
- **Model not pulled** — run `ollama pull gemma3:4b`
- **Model overloaded** — the model may generate malformed JSON under heavy load
- **Temperature too high** — try lowering `llm.temperature` in `config.yaml` to `0.3`

The tool gracefully falls back to "Analysis unavailable" rather than crashing.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/competitor-analysis-tool.git
cd competitor-analysis-tool

# Install with dev dependencies
pip install -e ".[dev]"
# Or
make dev

# Run tests to verify setup
make test

# Format code
make format

# Run linters
make lint
```

### Contribution Guidelines

1. **Fork** the repository and create a feature branch
2. **Write tests** for any new functionality
3. **Run** `make lint` and `make test` before submitting
4. **Follow** the existing code style (Black formatter, type hints)
5. **Submit** a pull request with a clear description

### Areas for Contribution

- 🌍 Additional output formats (PDF, HTML, Excel export)
- 📊 More visualization types in the Web UI
- 🔌 Support for additional LLM backends (OpenAI, Anthropic, etc.)
- 🧪 Expanded test coverage
- 📖 Documentation improvements
- 🐛 Bug fixes and performance improvements

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ as part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<sub>Powered by Ollama · Built with Rich & Streamlit · Made for competitive intelligence</sub>

<br/>

[![Star this repo](https://img.shields.io/badge/⭐_Star_this_repo-7209b7?style=for-the-badge)](https://github.com/kennedyraju55/competitor-analysis-tool)
[![90 LLM Projects](https://img.shields.io/badge/90_LLM_Projects-Collection-9d4edd?style=for-the-badge)](https://github.com/kennedyraju55/90-local-llm-projects)

</div>
