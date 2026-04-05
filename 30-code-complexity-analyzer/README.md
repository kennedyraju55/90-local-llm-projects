<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg"/>
  <img src="docs/images/banner.svg" alt="Code Complexity Analyzer Banner" width="800"/>
</picture>

<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-f72585?style=flat-square&logo=llama&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click](https://img.shields.io/badge/Click-CLI-58a6ff?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![Rich](https://img.shields.io/badge/Rich-Terminal-f0883e?style=flat-square)](https://github.com/Textualize/rich)
[![License: MIT](https://img.shields.io/badge/License-MIT-ffd60a?style=flat-square)](../../LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)

**Analyze code complexity · Track trends over time · Get AI-powered refactoring suggestions**

*100% local — your code never leaves your machine.*

<br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Reference](#-api-reference) · [Configuration](#%EF%B8%8F-configuration)

</div>

<br/>

---

## 📑 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Web UI](#-web-ui)
- [Architecture](#-architecture)
- [Complexity Metrics Reference](#-complexity-metrics-reference)
- [API Reference](#-api-reference)
- [Configuration](#%EF%B8%8F-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Code complexity is **the #1 predictor of bugs**. Research shows that functions with cyclomatic complexity above 10 have **40% more defects** than simpler alternatives. Yet most developers rely on gut feeling rather than hard metrics.

**Code Complexity Analyzer** solves this by combining five industry-standard metrics with AI-powered refactoring suggestions — all running **100% locally** on your machine via [Ollama](https://ollama.ai).

| Problem | Solution |
|---------|----------|
| "Is this function too complex?" | Cyclomatic & Cognitive complexity scores with thresholds |
| "How maintainable is this code?" | Maintainability Index (0-100 scale) |
| "What should I refactor?" | AI-powered suggestions with specific code examples |
| "Is our code getting worse?" | Trend tracking with historical analysis |
| "I don't want to send code to the cloud" | Everything runs locally — Ollama + AST analysis |

> **Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection** — exploring practical applications of local language models.

---

## ✨ Features

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg"/>
  <img src="docs/images/features.svg" alt="Key Features" width="800"/>
</picture>
</div>

<br/>

| Feature | Description | Details |
|---------|-------------|---------|
| 🔄 **Cyclomatic Complexity** | Independent paths through code | Counts `if`, `while`, `for`, boolean operators, `except`, comprehensions |
| 🧠 **Cognitive Complexity** | Mental effort to understand code | Depth-weighted scoring for nested structures |
| 📐 **Halstead Volume** | Code vocabulary and size | `N × log₂(η)` — operators and operands analysis |
| 📊 **Maintainability Index** | Overall score from 0-100 | Industry-standard formula combining CC, Halstead, and LOC |
| 📏 **Line Counting** | Code, blank, and comment lines | Separate counts for total, code, blank, and comment lines |
| 📦 **Dependency Analysis** | Import graph extraction | Discovers `import` and `from...import` statements |
| 🤖 **AI Suggestions** | LLM-powered refactoring advice | Specific improvements via Ollama (Gemma 3 1B default) |
| 📈 **Trend Tracking** | Monitor complexity over time | JSON-based persistence with historical data |
| 🔍 **Function-Level Detail** | Per-function metrics breakdown | Name, line, size, CC, cognitive, argument count |
| 🌐 **Web UI** | Streamlit dashboard | File upload, charts, dependency visualization |
| 🖥️ **Rich CLI** | Beautiful terminal output | Rich tables, panels, color-coded ratings |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **[Ollama](https://ollama.ai)** installed and running (for AI suggestions)
- **Gemma 3 1B** model pulled (`ollama pull gemma3:1b`)

> **Note:** Ollama is only required for AI suggestions. All metrics work without it — use `--no-ai`.

### Installation

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/code-complexity-analyzer.git
cd code-complexity-analyzer

# Install dependencies
pip install -r requirements.txt

# Install in development mode (optional)
pip install -e ".[dev]"
```

### Your First Analysis

```bash
# Analyze any Python file (metrics only, no AI needed)
python -m src.complexity_analyzer.cli analyze --file your_script.py --no-ai
```

### Example Output

```
File: your_script.py
Report: summary

           📏 Line Counts
┌───────────────┬───────┐
│ Metric        │ Count │
├───────────────┼───────┤
│ Total Lines   │   285 │
│ Code Lines    │   198 │
│ Blank Lines   │    42 │
│ Comment Lines │    45 │
└───────────────┴───────┘

                  📊 Overall Metrics
┌─────────────────────────────┬────────┬──────────┐
│ Metric                      │ Value  │  Rating  │
├─────────────────────────────┼────────┼──────────┤
│ Maintainability Index       │ 62/100 │ Moderate │
│ Avg Cyclomatic Complexity   │ 4.5    │   LOW    │
│ Halstead Volume             │ 245.3  │  MEDIUM  │
│ Dependencies                │ 5      │          │
└─────────────────────────────┴────────┴──────────┘

                   🔍 Function Complexity
┌──────────────────┬──────┬───────┬───────────┬───────────┬──────┬────────┐
│ Function         │ Line │ Lines │ Cyclomatic│ Cognitive │ Args │ Rating │
├──────────────────┼──────┼───────┼───────────┼───────────┼──────┼────────┤
│ validate_input   │   42 │    28 │        12 │        18 │    3 │  HIGH  │
│ process_data     │   85 │    35 │         8 │        12 │    2 │ MEDIUM │
│ format_output    │  130 │    15 │         3 │         2 │    1 │  LOW   │
│ helper           │  155 │     8 │         2 │         1 │    1 │  LOW   │
└──────────────────┴──────┴───────┴───────────┴───────────┴──────┴────────┘

Dependencies: os, sys, json, logging, typing
```

### Full Analysis with AI

```bash
# Start Ollama first
ollama serve

# Pull the model (one-time)
ollama pull gemma3:1b

# Run with AI suggestions
python -m src.complexity_analyzer.cli analyze --file your_script.py --report detailed
```

```
╭─ 💡 AI Suggestions ────────────────────────────────────────────────────────╮
│                                                                            │
│  ## Overall Assessment: 6/10                                               │
│                                                                            │
│  ### High Complexity Areas                                                 │
│  - `validate_input()` (CC=12): Too many conditional branches               │
│  - `process_data()` (CC=8): Deeply nested loops                            │
│                                                                            │
│  ### Refactoring Suggestions                                               │
│  1. **Extract validation rules** into a dictionary-based lookup            │
│  2. **Use early returns** to reduce nesting in `validate_input()`          │
│  3. **Apply Strategy pattern** for `process_data()` branches               │
│                                                                            │
│  ### Design Patterns                                                       │
│  - Strategy Pattern for conditional processing                             │
│  - Guard Clauses for input validation                                      │
│                                                                            │
╰────────────────────────────────────────────────────────────────────────────╯
```

---

## 📖 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com) and [Rich](https://github.com/Textualize/rich).

### Commands

| Command | Description |
|---------|-------------|
| `analyze` | Analyze code complexity of a Python file |
| `trends` | View complexity trends over time |

### `analyze` Command

```bash
python -m src.complexity_analyzer.cli analyze [OPTIONS]
```

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | `PATH` | *(required)* | Python file to analyze |
| `--report` | `-r` | `summary\|detailed` | `summary` | Report detail level |
| `--no-ai` | — | flag | `false` | Skip AI suggestions, metrics only |
| `--track` | — | flag | `false` | Save metrics for trend tracking |

### `trends` Command

```bash
python -m src.complexity_analyzer.cli trends
```

Displays the last 10 data points for each tracked file, showing:

| Column | Description |
|--------|-------------|
| Date | Timestamp of the analysis |
| MI | Maintainability Index at that point |
| Avg CC | Average cyclomatic complexity |
| Lines | Total line count |
| Functions | Number of functions |

### Global Options

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--verbose` | `-v` | flag | `false` | Enable verbose/debug logging |
| `--config` | — | `PATH` | `config.yaml` | Path to configuration file |

### Usage Examples

```bash
# Quick metrics check (no Ollama needed)
python -m src.complexity_analyzer.cli analyze -f src/complexity_analyzer/core.py --no-ai

# Detailed analysis with AI suggestions
python -m src.complexity_analyzer.cli analyze -f app.py -r detailed

# Track metrics for trend analysis
python -m src.complexity_analyzer.cli analyze -f app.py --no-ai --track

# View historical trends
python -m src.complexity_analyzer.cli trends

# Use a custom config file
python -m src.complexity_analyzer.cli --config custom.yaml analyze -f app.py

# Verbose mode for debugging
python -m src.complexity_analyzer.cli -v analyze -f app.py --no-ai
```

### Using `make` Shortcuts

```bash
make run-cli ARGS="analyze --file mycode.py --no-ai"
make run-cli ARGS="trends"
```

---

## 🌐 Web UI

The Streamlit web interface provides an interactive dashboard for code analysis.

### Launch

```bash
streamlit run src/complexity_analyzer/web_ui.py

# Or use make
make run-web
```

### Web UI Features

- 📂 **File Uploader** — drag-and-drop Python files for instant analysis
- 📊 **Metrics Dashboard** — visual charts for all complexity metrics
- 🔍 **Function Breakdown** — sortable table of per-function complexity
- 📦 **Dependency Graph** — visualize import relationships
- 💡 **AI Suggestions** — one-click refactoring advice via Ollama
- 📈 **Trend Charts** — track complexity changes over time
- ⚙️ **Configuration** — adjust thresholds and model settings in the sidebar

---

## 🏗️ Architecture

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg"/>
  <img src="docs/images/architecture.svg" alt="Architecture Overview" width="800"/>
</picture>
</div>

<br/>

### Data Flow

```
Python Source → AST Parser → ┬─ Cyclomatic Complexity ─┐
                             ├─ Cognitive Complexity   ├─→ Maintainability Index → Reports
                             ├─ Halstead Volume ───────┘
                             ├─ Line Counter ──────────────→ Reports
                             └─ Dependency Analyzer ───────→ Reports
                                       │
                                       ↓
                              AI Suggestions (Ollama)
                                       │
                                       ↓
                                 Trend Tracking
```

### Project Structure

```
30-code-complexity-analyzer/
├── src/
│   └── complexity_analyzer/      # Main package
│       ├── __init__.py           # Package metadata (__version__, __author__)
│       ├── core.py               # 🧠 All metrics, dependencies, AI, trends
│       ├── cli.py                # 🖥️  Click CLI with Rich output
│       └── web_ui.py             # 🌐 Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── test_core.py              # Core logic unit tests
│   └── test_cli.py               # CLI integration tests
├── common/                       # Shared utilities (LLM client)
├── docs/
│   └── images/                   # SVG diagrams
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml                   # ⚙️  Default configuration
├── setup.py                      # 📦 Package setup (pip install -e .)
├── Makefile                      # 🔧 Task runner (make test, make run-cli)
├── requirements.txt              # 📋 Python dependencies
├── .env.example                  # 🔑 Environment variable template
└── README.md                     # 📖 This file
```

### Module Responsibilities

| Module | Responsibility |
|--------|---------------|
| `core.py` | All computation — metrics, AST parsing, dependencies, AI integration, trend I/O |
| `cli.py` | User-facing CLI — argument parsing, Rich output formatting, Ollama health checks |
| `web_ui.py` | Streamlit dashboard — file upload, charts, interactive analysis |
| `common/` | Shared LLM client (`chat`, `check_ollama_running`) used across projects |

---

## 📏 Complexity Metrics Reference

### 1. Cyclomatic Complexity (CC)

**What it measures:** The number of independent execution paths through a function.

**Formula:**

```
CC = 1 + (number of decision points)
```

Decision points counted:
- `if` / `elif` statements
- `while` loops
- `for` loops
- Boolean operators (`and`, `or`) — each adds `len(values) - 1`
- `except` handlers
- List/set/dict comprehensions and generator expressions
- `assert` statements

**Rating thresholds:**

| Score | Rating | Interpretation |
|-------|--------|----------------|
| 1–4 | 🟢 **LOW** | Simple, low risk |
| 5–10 | 🟡 **MEDIUM** | Moderate complexity, consider refactoring |
| 11+ | 🔴 **HIGH** | Complex, high risk — refactor recommended |

**Example:**

```python
def example(x, y):       # CC starts at 1
    if x > 0:            # +1 → CC = 2
        for i in range(y):   # +1 → CC = 3
            if i > 5 or x < 10:  # +1 (if) +1 (or) → CC = 5
                pass
    return x              # CC = 5
```

---

### 2. Cognitive Complexity

**What it measures:** The mental effort required to understand a function, accounting for nesting depth.

**Formula:**

```
Score += (1 + current_nesting_depth) for each control structure
```

Unlike cyclomatic complexity, cognitive complexity penalizes deeply nested code more heavily. A triply-nested `if` contributes more than three flat `if` statements.

**Counted structures:**
- `if`, `while`, `for` — base increment of 1 + nesting depth
- Boolean operators (`and`, `or`) — increment of 1 (no depth penalty)
- `except` handlers — increment of 1 + nesting depth

**Example:**

```python
def example(data):            # depth = 0
    if data:                  # +1 (1 + 0) → score = 1
        for item in data:     # +2 (1 + 1) → score = 3
            if item > 0:      # +3 (1 + 2) → score = 6
                pass
    return data               # Total cognitive = 6
```

---

### 3. Halstead Volume

**What it measures:** The "information content" of a program based on operators and operands.

**Formula:**

```
N = N₁ + N₂          (total occurrences: operators + operands)
η = η₁ + η₂          (unique vocabulary: distinct operators + distinct operands)
Volume = N × log₂(η)
```

| Symbol | Meaning |
|--------|---------|
| `η₁` | Number of distinct operators |
| `η₂` | Number of distinct operands |
| `N₁` | Total operator occurrences |
| `N₂` | Total operand occurrences |

**Operators include:** binary operations (`+`, `-`, `*`, etc.), comparison operations (`==`, `<`, `>`, etc.)

**Operands include:** variable names (`ast.Name`), constants/literals (`ast.Constant`)

---

### 4. Maintainability Index (MI)

**What it measures:** An overall score from 0 to 100 indicating how maintainable the code is.

**Formula:**

```
MI = max(0, 171 − 5.2 × ln(H + 1) − 0.23 × CC − 16.2 × ln(LOC))
MI = min(MI, 100)
```

| Variable | Meaning |
|----------|---------|
| `H` | Halstead Volume |
| `CC` | Average cyclomatic complexity |
| `LOC` | Lines of code (excluding blanks and comments) |

**Rating thresholds:**

| Score | Rating | Interpretation |
|-------|--------|----------------|
| 65–100 | 🟢 **Good** | Highly maintainable |
| 35–64 | 🟡 **Moderate** | Reasonably maintainable, room for improvement |
| 0–34 | 🔴 **Poor** | Difficult to maintain — refactoring needed |

---

### 5. Line Counting

**What it measures:** Breakdown of source lines by type.

| Metric | Definition |
|--------|-----------|
| **Total Lines** | All lines in the file |
| **Code Lines** | Total − blank − comment lines |
| **Blank Lines** | Lines with only whitespace |
| **Comment Lines** | Lines starting with `#` (after stripping whitespace) |

---

### 6. Dependency Analysis

**What it measures:** External and internal module dependencies.

Extracts all `import X` and `from X import Y` statements, returning the list of module names. Useful for understanding coupling and identifying unused or excessive imports.

---

## 🔌 API Reference

All core functions are in `src/complexity_analyzer/core.py`.

### Configuration

```python
from complexity_analyzer.core import load_config

config = load_config("config.yaml")
# Returns dict with all settings and defaults
```

### File Analysis

```python
from complexity_analyzer.core import analyze_file

metrics = analyze_file("your_script.py")
# Returns:
# {
#     "filepath": "your_script.py",
#     "lines": {"total": 285, "code": 198, "blank": 42, "comments": 45},
#     "functions": [
#         {"name": "func", "lineno": 10, "lines": 25,
#          "cyclomatic": 5, "cognitive": 8, "args_count": 3},
#         ...
#     ],
#     "halstead_volume": 245.3,
#     "maintainability_index": 62.15,
#     "avg_cyclomatic": 4.5,
#     "dependencies": ["os", "sys", "json"],
# }
```

### Individual Metrics

```python
import ast
from complexity_analyzer.core import (
    calculate_cyclomatic_complexity,
    calculate_cognitive_complexity,
    count_lines,
    calculate_halstead_volume,
    analyze_dependencies,
)

source = open("script.py").read()
tree = ast.parse(source)

# Cyclomatic complexity for a specific function node
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        cc = calculate_cyclomatic_complexity(node)
        cog = calculate_cognitive_complexity(node, depth=0)
        print(f"{node.name}: CC={cc}, Cognitive={cog}")

# Halstead volume for entire source
volume = calculate_halstead_volume(source)

# Line counts
lines = count_lines(source)
# {"total": 285, "code": 198, "blank": 42, "comments": 45}

# Dependency extraction
deps = analyze_dependencies(source)
# ["os", "sys", "json"]
```

### Rating Functions

```python
from complexity_analyzer.core import get_complexity_rating, get_mi_rating

# Cyclomatic complexity rating (returns Rich-formatted string)
rating = get_complexity_rating(8, thresholds=(5, 10))
# "[yellow]MEDIUM[/yellow]"

# Maintainability index rating
mi_rating = get_mi_rating(72.5)
# "[green]Good[/green]"
```

### AI Suggestions

```python
from complexity_analyzer.core import get_llm_suggestions, load_config
from common.llm_client import chat

config = load_config()
metrics = analyze_file("script.py")

suggestions = get_llm_suggestions(
    filepath="script.py",
    metrics=metrics,
    chat_fn=chat,          # LLM chat function
    config=config,
)
print(suggestions)
```

### Trend Tracking

```python
from complexity_analyzer.core import save_trend, load_trends

# Save a data point
save_trend("script.py", metrics, trends_file="complexity_trends.json")

# Load all trend data
trends = load_trends("complexity_trends.json")
# {
#     "script.py": [
#         {"timestamp": 1700000000, "maintainability_index": 62.15,
#          "avg_cyclomatic": 4.5, "total_lines": 285, "functions_count": 12},
#         ...
#     ]
# }
```

---

## ⚙️ Configuration

Configuration is stored in `config.yaml`. All settings have sensible defaults.

```yaml
# Code Complexity Analyzer Configuration

ollama_base_url: "http://localhost:11434"
model: "gemma3:1b"
temperature: 0.3
max_code_chars: 5000
trends_file: "complexity_trends.json"
cc_threshold_low: 5
cc_threshold_high: 10
mi_threshold_good: 65
mi_threshold_moderate: 35
```

### Configuration Reference

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `ollama_base_url` | `string` | `http://localhost:11434` | Ollama API endpoint |
| `model` | `string` | `gemma3:1b` | LLM model name for AI suggestions |
| `temperature` | `float` | `0.3` | LLM sampling temperature (0.0–1.0) |
| `max_code_chars` | `int` | `5000` | Max source characters sent to LLM |
| `trends_file` | `string` | `complexity_trends.json` | Path for trend data persistence |
| `cc_threshold_low` | `int` | `5` | Cyclomatic complexity: below this = LOW |
| `cc_threshold_high` | `int` | `10` | Cyclomatic complexity: above this = HIGH |
| `mi_threshold_good` | `int` | `65` | Maintainability Index: above this = Good |
| `mi_threshold_moderate` | `int` | `35` | Maintainability Index: above this = Moderate |

### Using a Custom Config

```bash
python -m src.complexity_analyzer.cli --config my_config.yaml analyze -f app.py
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/complexity_analyzer --cov-report=term-missing

# Run a specific test file
python -m pytest tests/test_core.py -v

# Using make
make test
make test-cov
```

### Test Structure

| File | Covers |
|------|--------|
| `tests/test_core.py` | Metrics calculation, line counting, dependency analysis, trend I/O |
| `tests/test_cli.py` | CLI commands, argument parsing, output formatting |

### Linting

```bash
# Compile-check all modules
make lint

# Manual check
python -m py_compile src/complexity_analyzer/core.py
python -m py_compile src/complexity_analyzer/cli.py
```

---

## 🔒 Local vs Cloud

| Aspect | Code Complexity Analyzer | Cloud Services |
|--------|--------------------------|----------------|
| **Privacy** | ✅ 100% local — code never leaves your machine | ❌ Code sent to external servers |
| **Cost** | ✅ Free forever (Ollama is open-source) | ❌ Per-request or subscription pricing |
| **Latency** | ✅ No network round-trips for metrics | ❌ Depends on API availability |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Customization** | ✅ Full control over model, thresholds, config | ❌ Limited to provider's options |
| **AI Quality** | ⚠️ Smaller local models (1B–8B) | ✅ Larger cloud models (70B+) |
| **Setup** | ⚠️ Requires Ollama installation | ✅ Just an API key |

> **Best of both worlds:** All five complexity metrics work without AI. Use `--no-ai` for instant, zero-setup analysis. Add Ollama when you want refactoring suggestions.

---

## ❓ FAQ

<details>
<summary><strong>1. Do I need Ollama installed to use this tool?</strong></summary>

No. All complexity metrics (cyclomatic, cognitive, Halstead, maintainability index, line counting, dependencies) work without Ollama. Use the `--no-ai` flag to skip AI suggestions. Ollama is only required for the AI-powered refactoring recommendations.

</details>

<details>
<summary><strong>2. Can I use a different LLM model?</strong></summary>

Yes. Edit `model` in `config.yaml` to any model available in your Ollama installation. For example:

```yaml
model: "llama3.2:3b"    # Larger, more detailed suggestions
model: "codellama:7b"   # Code-specialized model
model: "mistral:7b"     # Alternative general model
```

Run `ollama list` to see your available models.

</details>

<details>
<summary><strong>3. What Python versions are supported?</strong></summary>

Python 3.10 or newer is required. The tool uses modern Python features including `ast.AST` type annotations and structural pattern matching support in the AST parser.

</details>

<details>
<summary><strong>4. Can I analyze non-Python files?</strong></summary>

Currently, only Python (`.py`) files are supported. The analyzer uses Python's built-in `ast` module for parsing, which is Python-specific. Support for other languages would require additional parsers.

</details>

<details>
<summary><strong>5. How does trend tracking work?</strong></summary>

When you use the `--track` flag, metrics are appended to a JSON file (`complexity_trends.json` by default). Each entry includes a timestamp, maintainability index, average CC, total lines, and function count. Use the `trends` command to view the last 10 data points per file. This lets you monitor whether your refactoring efforts are improving code quality over time.

</details>

---

## 🤝 Contributing

Contributions are welcome! This project is part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection.

### Getting Started

```bash
# Fork and clone the repository
git clone https://github.com/kennedyraju55/code-complexity-analyzer.git
cd code-complexity-analyzer

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify setup
make test
```

### Guidelines

1. **Fork** the repository and create a feature branch
2. **Write tests** for any new functionality
3. **Run the test suite** before submitting: `make test`
4. **Follow existing code style** (Black formatting)
5. **Update documentation** if adding new features
6. **Submit a Pull Request** with a clear description

### Development Commands

```bash
make help       # Show all available commands
make install    # Install dependencies
make dev        # Install in development mode
make test       # Run tests
make test-cov   # Run tests with coverage
make lint       # Compile-check modules
make run-cli    # Run CLI (use ARGS="...")
make run-web    # Launch Streamlit web UI
make clean      # Clean build artifacts
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](../../LICENSE) file for details.

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

Built with ❤️ using Python, Ollama, Click, Rich, and Streamlit

<br/>

<sub>📊 Analyze · 📈 Track · 🤖 Improve — all locally, all privately</sub>

</div>
