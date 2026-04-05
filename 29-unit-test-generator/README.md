<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img src="docs/images/banner.svg" alt="Unit Test Generator — AI-Powered Test Generation with AST Analysis & Local LLMs" width="800">
</picture>

<br/>
<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-4361ee?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![pytest](https://img.shields.io/badge/pytest-Supported-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](../../LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br/>

**Automatically generate comprehensive unit tests for Python code using a local LLM.**<br/>
AST-powered analysis · Edge case detection · pytest & unittest · 100% local & private

<br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Reference](#-api-reference) · [Architecture](#-architecture)

<br/>
<strong>Part of <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

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
- [API Reference](#-api-reference)
- [Edge Case Detection](#-edge-case-detection)
- [Configuration](#%EF%B8%8F-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Writing unit tests is essential but tedious. Most developers skip edge cases, forget error paths,
and struggle to maintain test coverage as code evolves. Existing tools either require cloud APIs
(sending your proprietary code to third-party servers) or generate superficial tests that miss
the nuances of your codebase.

**Unit Test Generator** solves this by combining:

- 🌳 **AST-level code understanding** — not regex or string matching, but actual Python abstract
  syntax tree parsing that understands your functions, classes, arguments, decorators, and
  return types
- 🔍 **Intelligent edge case detection** — automatically identifies `None` handling, division by
  zero, empty collections, negative numbers, exception handling patterns, and more
- 🤖 **Local LLM generation** — uses Ollama with models like Gemma 3 1B to generate tests
  entirely on your machine, keeping your code private
- 📊 **Pre-generation analysis** — shows you exactly what needs testing before generating a
  single line of test code

> **Your code never leaves your machine.** Zero cloud dependencies. Zero API keys. Zero data leaks.

---

## ✨ Features

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg">
  <img src="docs/images/features.svg" alt="Key Features" width="800">
</picture>

</div>

<br/>

| Feature | Description |
|:--------|:------------|
| 🌳 **AST Code Analysis** | Deep parsing with Python's `ast` module to extract functions, classes, methods, arguments, decorators, docstrings, and return types |
| 🔍 **Edge Case Detection** | Auto-detect `None` checks, zero/negative values, empty collections, falsy checks, exception handling, and error patterns |
| 📊 **Coverage Analysis** | Pre-generation coverage estimation — know how many testable items exist before generating |
| 🧪 **Framework Support** | Generate idiomatic tests for **pytest** (with `@pytest.mark.parametrize`, fixtures) or **unittest** (`TestCase` subclasses) |
| 📁 **Test Organization** | Automatic test file and directory structure suggestions matching your source layout |
| 👁️ **Source Preview** | View extracted source code with `--show-source` before generating tests |
| 🌐 **Web UI** | Interactive Streamlit interface with file upload, metrics dashboard, and one-click download |
| 🖥️ **Rich CLI** | Beautiful terminal output with Rich tables, panels, and syntax highlighting |
| 🔒 **100% Local** | All processing happens on your machine — code never leaves your environment |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://www.python.org/downloads/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai) | Latest | Local LLM server |
| Gemma 3 1B | — | Default model (configurable) |

### 1. Install Ollama & Pull the Model

```bash
# Install Ollama (visit https://ollama.ai for your OS)
# Then pull the default model:
ollama pull gemma3:1b
```

### 2. Clone & Install

```bash
git clone https://github.com/kennedyraju55/unit-test-generator.git
cd unit-test-generator

pip install -r requirements.txt
pip install -e ".[dev]"  # Development mode with test dependencies
```

### 3. Generate Your First Tests

Given a Python source file like this:

```python
# calculator.py
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    def __init__(self):
        self.history = []

    def calculate(self, operation: str, a: float, b: float) -> float:
        """Perform a calculation and store in history."""
        if operation == "add":
            result = add(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")
        self.history.append((operation, a, b, result))
        return result
```

Run the generator:

```bash
python -m src.test_gen.cli generate --file calculator.py
```

**Generated output (pytest):**

```python
import pytest
from calculator import add, divide, Calculator


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_numbers(self):
        assert add(2.0, 3.0) == 5.0

    def test_add_negative_numbers(self):
        assert add(-1.0, -2.0) == -3.0

    def test_add_zero(self):
        assert add(0.0, 5.0) == 5.0

    @pytest.mark.parametrize("a, b, expected", [
        (1.0, 1.0, 2.0),
        (0.0, 0.0, 0.0),
        (-1.0, 1.0, 0.0),
        (100.5, 200.3, 300.8),
    ])
    def test_add_parametrized(self, a, b, expected):
        assert add(a, b) == expected


class TestDivide:
    """Tests for the divide function."""

    def test_divide_normal(self):
        assert divide(10.0, 2.0) == 5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10.0, 0.0)

    def test_divide_negative(self):
        assert divide(-10.0, 2.0) == -5.0

    def test_divide_result_is_float(self):
        assert isinstance(divide(7.0, 2.0), float)


class TestCalculator:
    """Tests for the Calculator class."""

    @pytest.fixture
    def calc(self):
        return Calculator()

    def test_calculate_add(self, calc):
        assert calc.calculate("add", 2.0, 3.0) == 5.0

    def test_calculate_divide(self, calc):
        assert calc.calculate("divide", 10.0, 2.0) == 5.0

    def test_calculate_unknown_operation(self, calc):
        with pytest.raises(ValueError, match="Unknown operation"):
            calc.calculate("multiply", 2.0, 3.0)

    def test_history_tracking(self, calc):
        calc.calculate("add", 1.0, 2.0)
        assert len(calc.history) == 1
        assert calc.history[0] == ("add", 1.0, 2.0, 3.0)
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/unit-test-generator.git
cd unit-test-generator
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
uvicorn src.test_gen.api:app --reload --port 8000

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

The CLI is built with [Click](https://click.palletsprojects.com/) and [Rich](https://rich.readthedocs.io/)
for a beautiful terminal experience.

### Global Options

| Option | Short | Description | Default |
|:-------|:------|:------------|:--------|
| `--verbose` | `-v` | Enable debug logging | `False` |
| `--config` | | Path to config file | `config.yaml` |

### `generate` — Generate Unit Tests

Generate comprehensive unit tests for a Python source file.

```bash
python -m src.test_gen.cli generate [OPTIONS]
```

| Option | Short | Description | Default |
|:-------|:------|:------------|:--------|
| `--file` | `-f` | **(required)** Path to the Python source file | — |
| `--framework` | `-F` | Test framework: `pytest` or `unittest` | `pytest` |
| `--output` | `-o` | Save generated tests to a file | — (prints to stdout) |
| `--show-source` | | Display source code before generating | `False` |

**Examples:**

```bash
# Basic generation with pytest (default)
python -m src.test_gen.cli generate --file src/utils.py

# Generate unittest-style tests
python -m src.test_gen.cli generate --file src/utils.py --framework unittest

# Save to a file
python -m src.test_gen.cli generate --file src/utils.py --output tests/test_utils.py

# Preview source code before generating
python -m src.test_gen.cli generate --file src/utils.py --show-source

# With verbose logging and custom config
python -m src.test_gen.cli -v --config my_config.yaml generate --file src/utils.py
```

### `analyze` — Analyze Coverage Requirements

Analyze a Python file and display coverage requirements without generating tests.

```bash
python -m src.test_gen.cli analyze [OPTIONS]
```

| Option | Short | Description | Default |
|:-------|:------|:------------|:--------|
| `--file` | `-f` | **(required)** Path to the Python source file | — |

**Example:**

```bash
python -m src.test_gen.cli analyze --file src/utils.py
```

**Sample output:**

```
╭── 📊 Code Structure ──────────────────────────────────────────╮
│ Type     │ Name        │ Details          │ Edge Cases         │
├──────────┼─────────────┼──────────────────┼────────────────────┤
│ Function │ add         │ (a, b)           │ —                  │
│ Function │ divide      │ (a, b)           │ Zero handling      │
│ Class    │ Calculator  │ 1 method         │                    │
│ Method   │ calculate   │ (operation,a,b)  │ Error handling     │
╰────────────────────────────────────────────────────────────────╯

📈 Coverage Analysis:
  Testable units: 4 │ Estimated tests: 14 │ Edge cases: 3

📁 Suggested Test Structure:
  tests/test_calculator.py
    ├── TestAdd
    ├── TestDivide
    └── TestCalculator
```

---

## 🌐 Web UI

Launch the interactive Streamlit web interface:

```bash
streamlit run src/test_gen/web_ui.py
```

Or using the Makefile:

```bash
make run-web
```

### Web UI Features

| Feature | Description |
|:--------|:------------|
| 📄 **Code Input** | Paste code or upload `.py` files directly |
| 📊 **Metrics Dashboard** | Real-time display of functions, methods, and edge case counts |
| 🧪 **Framework Selector** | Toggle between pytest and unittest generation |
| ✨ **Syntax Highlighting** | Generated tests displayed with Python syntax highlighting |
| 📥 **One-Click Download** | Download generated test files instantly |
| 📁 **Structure Preview** | Expandable section showing suggested test organization |

---

## 🏗️ Architecture

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg">
  <img src="docs/images/architecture.svg" alt="Architecture Overview" width="800">
</picture>

</div>

<br/>

### Data Flow

```
Python Source File
        │
        ▼
   ┌─────────────┐
   │  AST Parser  │  ← Python's ast module
   └──────┬──────┘
          │
          ▼
   ┌─────────────────┐
   │  Code Extractor  │  ← Functions, classes, methods, args, decorators
   └──────┬──────────┘
          │
     ┌────┴────┐
     ▼         ▼
┌─────────┐ ┌──────────┐
│  Edge   │ │ Coverage │
│  Cases  │ │ Analyzer │
└────┬────┘ └────┬─────┘
     │           │
     └─────┬─────┘
           ▼
   ┌───────────────┐
   │ Prompt Builder │  ← Framework-specific context
   └───────┬───────┘
           ▼
   ┌───────────────┐
   │  Ollama LLM   │  ← Local inference (Gemma 3 1B)
   └───────┬───────┘
           ▼
   ┌───────────────┐
   │  Test Output   │  ← pytest / unittest code
   └───────────────┘
```

### Project Structure

```
29-unit-test-generator/
├── src/
│   ├── __init__.py                 # Package root
│   └── test_gen/
│       ├── __init__.py             # Package metadata (v1.0.0)
│       ├── core.py                 # 🧠 Core logic — AST analysis, coverage, generation
│       ├── cli.py                  # 🖥️  Click CLI with Rich formatting
│       └── web_ui.py               # 🌐 Streamlit web interface
├── common/
│   └── llm_client.py               # 🤖 Shared Ollama client (used across all 90 projects)
├── tests/
│   ├── __init__.py
│   ├── test_core.py                # Core module unit tests
│   └── test_cli.py                 # CLI integration tests
├── docs/
│   └── images/                     # SVG assets for documentation
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml                     # ⚙️  Configuration file
├── setup.py                        # 📦 Package setup & entry points
├── requirements.txt                # 📋 Runtime + dev dependencies
├── Makefile                        # 🔧 Task runner (install, test, lint, run)
├── .env.example                    # 🔑 Environment variable template
└── README.md                       # 📖 This file
```

---

## 📚 API Reference

### `extract_code_info(filepath: str) -> dict`

Parse a Python source file using the AST module and extract all testable code elements.

```python
from src.test_gen.core import extract_code_info

info = extract_code_info("calculator.py")
```

**Returns:**

```python
{
    "filepath": "calculator.py",
    "functions": [
        {
            "name": "add",
            "args": ["a", "b"],
            "decorators": [],
            "docstring": "Add two numbers.",
            "edge_cases": []
        },
        {
            "name": "divide",
            "args": ["a", "b"],
            "decorators": [],
            "docstring": "Divide a by b.",
            "edge_cases": ["zero_handling", "error_handling"]
        }
    ],
    "classes": [
        {
            "name": "Calculator",
            "methods": ["calculate"],
            "bases": []
        }
    ]
}
```

---

### `analyze_coverage(code_info: dict) -> dict`

Analyze coverage requirements from extracted code information.

```python
from src.test_gen.core import extract_code_info, analyze_coverage

info = extract_code_info("calculator.py")
coverage = analyze_coverage(info)
```

**Returns:**

```python
{
    "total_functions": 2,
    "total_methods": 1,
    "total_testable": 3,
    "estimated_tests": 14,
    "edge_cases_found": 3
}
```

---

### `generate_tests(filepath, chat_fn, framework, config) -> str`

Generate comprehensive unit tests using the local LLM.

```python
from src.test_gen.core import generate_tests, load_config
from common.llm_client import chat

config = load_config()
tests = generate_tests(
    filepath="calculator.py",
    chat_fn=chat,
    framework="pytest",    # or "unittest"
    config=config
)
print(tests)
```

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `filepath` | `str` | Path to the Python source file |
| `chat_fn` | `callable` | LLM chat function (e.g., `common.llm_client.chat`) |
| `framework` | `str` | `"pytest"` or `"unittest"` |
| `config` | `dict` | Configuration dictionary (from `load_config()`) |

**Returns:** `str` — Generated test code as a string.

---

### `organize_test_structure(code_info: dict) -> list`

Suggest a test file and directory structure for the analyzed code.

```python
from src.test_gen.core import extract_code_info, organize_test_structure

info = extract_code_info("calculator.py")
structure = organize_test_structure(info)
```

**Returns:**

```python
[
    {
        "test_file": "tests/test_calculator.py",
        "test_classes": ["TestAdd", "TestDivide", "TestCalculator"]
    }
]
```

---

### `load_config(config_path: str = "config.yaml") -> dict`

Load configuration from a YAML file with sensible defaults.

```python
from src.test_gen.core import load_config

config = load_config()                    # Uses config.yaml
config = load_config("my_config.yaml")    # Custom path
```

---

### Internal Functions

| Function | Description |
|:---------|:------------|
| `_detect_edge_cases(func_node)` | Analyze an AST function node to identify edge case patterns |
| `_get_decorator_name(decorator)` | Extract the string name from a decorator AST node |

---

## 🔍 Edge Case Detection

The AST analyzer automatically detects common edge case patterns in your source code. These
detected patterns are used to generate more comprehensive tests.

### Detected Patterns

| Pattern | Detection Method | Example Code |
|:--------|:-----------------|:-------------|
| **None handling** | `if x is None`, `if x is not None` | `if value is None: return default` |
| **Zero / negative** | Comparisons with `0`, division operations | `if b == 0: raise ValueError(...)` |
| **Empty collections** | `if not x`, length checks, empty literals | `if not items: return []` |
| **Falsy values** | Boolean checks on variables | `if not name: raise ValueError(...)` |
| **Exception handling** | `try/except` blocks, `raise` statements | `try: ... except KeyError: ...` |
| **Error patterns** | Functions with "error" or "exception" in name | `def handle_error(self, err): ...` |

### Example: Edge Case Detection in Action

Given this source code:

```python
def process_data(items, default=None):
    """Process a list of data items."""
    if items is None:
        raise TypeError("items cannot be None")
    if not items:
        return default or []
    try:
        return [transform(item) for item in items]
    except ValueError as e:
        return {"error": str(e)}
```

The analyzer detects:

```
Edge Cases Found:
  ├── none_handling     → "items is None" check detected
  ├── empty_collection  → "not items" falsy check on collection
  ├── error_handling    → try/except ValueError block
  └── falsy_values      → "default or []" falsy fallback
```

Generated tests will include:

```python
def test_process_data_none_input(self):
    with pytest.raises(TypeError, match="items cannot be None"):
        process_data(None)

def test_process_data_empty_list(self):
    assert process_data([]) == []

def test_process_data_empty_list_with_default(self):
    assert process_data([], default="fallback") == "fallback"

def test_process_data_value_error_handling(self):
    # Test that ValueError is caught and returned as dict
    ...
```

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# Ollama server configuration
ollama_base_url: "http://localhost:11434"

# Model settings
model: "gemma3:1b"           # LLM model to use
temperature: 0.3             # Creativity level (0.0 = deterministic, 1.0 = creative)
max_tokens: 4096             # Maximum response length

# Test generation settings
default_framework: "pytest"  # Default test framework (pytest | unittest)
max_code_chars: 5000         # Maximum source code characters sent to LLM
```

### Environment Variables (`.env`)

You can also configure via environment variables (see `.env.example`):

```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
TEMPERATURE=0.3
MAX_TOKENS=4096
DEFAULT_FRAMEWORK=pytest
MAX_CODE_CHARS=5000
```

### Configuration Precedence

1. CLI flags (highest priority)
2. Environment variables
3. `config.yaml` file
4. Built-in defaults (lowest priority)

### Default Values

If no configuration is provided, these defaults are used:

| Setting | Default |
|:--------|:--------|
| `ollama_base_url` | `http://localhost:11434` |
| `model` | `gemma3:1b` |
| `temperature` | `0.3` |
| `max_tokens` | `4096` |
| `default_framework` | `pytest` |
| `max_code_chars` | `5000` |

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/test_gen --cov-report=term-missing

# Using the Makefile
make test          # Basic test run
make test-cov      # With coverage report
```

### Test Suite Overview

| Test File | Module | Tests |
|:----------|:-------|:------|
| `tests/test_core.py` | `src.test_gen.core` | `extract_code_info`, `analyze_coverage`, `organize_test_structure`, `generate_tests`, `load_config`, `_detect_edge_cases` |
| `tests/test_cli.py` | `src.test_gen.cli` | `generate` command, `analyze` command, output-to-file, error handling |

### Test Categories

- **Unit tests** — Core logic (AST parsing, coverage analysis, edge detection)
- **Integration tests** — CLI commands with mocked LLM calls
- **Error handling** — Syntax errors, missing files, Ollama not running

---

## 🔒 Local vs Cloud

| Aspect | Unit Test Generator (Local) | Cloud-Based Tools |
|:-------|:---------------------------|:------------------|
| **Privacy** | ✅ Code never leaves your machine | ❌ Code sent to third-party servers |
| **Cost** | ✅ Free (runs on your hardware) | ❌ Per-token API costs |
| **Speed** | ✅ No network latency | ❌ Depends on API availability |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Customization** | ✅ Swap any Ollama model | ❌ Limited to provider models |
| **Data retention** | ✅ No data stored externally | ❌ May log/store your code |
| **Model quality** | ⚡ Smaller local models | ⚡ Larger cloud models |

---

## ❓ FAQ

<details>
<summary><b>1. Which Ollama models work best for test generation?</b></summary>
<br/>

The default model is **Gemma 3 1B**, which provides a good balance of speed and quality for test
generation. You can use any Ollama-compatible model by changing the `model` setting in
`config.yaml`. Larger models (e.g., `gemma3:4b`, `llama3:8b`) may produce higher-quality tests
but will be slower.

```yaml
# config.yaml
model: "gemma3:4b"  # Upgrade for better quality
```

</details>

<details>
<summary><b>2. Can I generate tests for a whole directory?</b></summary>
<br/>

Currently, the tool processes one file at a time. To generate tests for multiple files, you can
use a simple shell loop:

```bash
for file in src/**/*.py; do
    python -m src.test_gen.cli generate --file "$file" --output "tests/test_$(basename $file)"
done
```

</details>

<details>
<summary><b>3. Why are generated tests not always perfect?</b></summary>
<br/>

The quality of generated tests depends on the LLM model and the complexity of your source code.
The tool provides a strong starting point with edge case detection and proper structure, but you
should always review and refine generated tests. Think of it as a **test scaffold generator**
that saves you 80% of the boilerplate work.

</details>

<details>
<summary><b>4. How do I use a different test framework?</b></summary>
<br/>

Use the `--framework` flag to switch between pytest and unittest:

```bash
# pytest (default) — uses fixtures, parametrize, pytest.raises
python -m src.test_gen.cli generate --file app.py --framework pytest

# unittest — uses TestCase, setUp, assertRaises
python -m src.test_gen.cli generate --file app.py --framework unittest
```

</details>

<details>
<summary><b>5. What happens if Ollama is not running?</b></summary>
<br/>

The CLI will display a clear error message asking you to start Ollama:

```
❌ Ollama is not running. Please start it with: ollama serve
```

Make sure Ollama is running on `http://localhost:11434` (or your configured URL) before using the
generate command. The `analyze` command works without Ollama since it only performs AST analysis.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/unit-test-generator.git
   cd unit-test-generator
   ```
3. **Install** in development mode:
   ```bash
   make dev
   ```
4. **Create** a feature branch:
   ```bash
   git checkout -b feature/my-feature
   ```
5. **Make** your changes and add tests
6. **Run** the test suite:
   ```bash
   make test-cov
   ```
7. **Submit** a pull request

### Development Commands

```bash
make install     # Install dependencies
make dev         # Install in development mode
make test        # Run tests
make test-cov    # Run tests with coverage
make lint        # Compile check
make clean       # Remove build artifacts
make run-cli ARGS="generate --file mycode.py"   # Run CLI
make run-web     # Launch Streamlit UI
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](../../LICENSE) file for details.

---

<div align="center">

<br/>

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

Built with ❤️ using Python, Ollama, Click, Rich, and Streamlit

<br/>

[⬆ Back to Top](#)

</div>
