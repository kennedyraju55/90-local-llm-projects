<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img alt="Stack Trace Explainer — AI-Powered Error Analysis & Fix Suggestions with Local LLMs" src="docs/images/banner.svg" width="800">
</picture>

<br/>

[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-2ec4b6?style=flat-square&logo=llama&logoColor=white)](https://ollama.com)
[![Gemma 4](https://img.shields.io/badge/Gemma_4-Model-ff6f00?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click CLI](https://img.shields.io/badge/Click-CLI-44cc11?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-ffd43b?style=flat-square)](../LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-2ec4b6?style=flat-square&logo=pytest&logoColor=white)](tests/)

<br/>

**Paste a stack trace. Get a plain-English explanation, a working fix, and similar errors — all powered by a local LLM.**

<sub>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection · Project #23</sub>

</div>

<br/>

---

## 📖 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Web UI](#-web-ui)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Configuration](#%EF%B8%8F-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Every developer has stared at a cryptic stack trace and thought: **"What does this even mean?"**

Stack Trace Explainer turns that frustration into a **30-second fix** by combining:

- **Pattern-matching** against a built-in database of common error types
- **Language auto-detection** across 11 programming languages
- **Local LLM analysis** via Ollama — your code never leaves your machine
- **Actionable output** — not just an explanation, but working fix code

```
You get a KeyError in production at 2 AM.
Instead of Googling for 20 minutes, you run:

  $ stack-explainer explain --trace crash.log --fix

And get:
  ✅ Root cause: dictionary key "user_id" missing from API response
  ✅ Fix code: use .get() with a default fallback
  ✅ Similar errors: KeyError vs AttributeError vs TypeError
```

> **Zero cloud dependency.** Your stack traces, error logs, and proprietary code stay on your machine.

---

## ✨ Features

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg">
  <img alt="Key Features" src="docs/images/features.svg" width="800">
</picture>
</div>

<br/>

| Feature | Description |
|:--------|:------------|
| 🌐 **Multi-Language Detection** | Auto-detect Python, JavaScript, Java, C#, Go, Rust, Ruby, PHP, Kotlin, Swift, C++ from trace format |
| 💡 **Plain English Explanations** | LLM-powered 5-point analysis: error summary, root cause, call chain walkthrough, fix steps, prevention tips |
| 🔧 **Fix Code Generation** | Generate corrected code with explanatory comments using `--fix` |
| 🔗 **Similar Error Finder** | Discover 3-5 related error types and learn to distinguish between them using `--similar` |
| 📚 **Built-in Error Database** | Instant hints for 20+ common error types across Python, JavaScript, and Java |
| 📥 **Flexible Input** | Read from files (`--trace`), inline text (`--text`), or piped stdin |
| 🖥️ **Rich Terminal Output** | Beautiful panels, syntax highlighting, and colored output via the Rich library |
| 🌐 **Streamlit Web UI** | Browser-based interface with trace input, settings sidebar, and downloadable results |
| ⚙️ **YAML + Env Config** | Layered configuration: defaults → `config.yaml` → environment variables → CLI args |
| 🔒 **100% Local** | All processing happens on your machine via Ollama — no data ever leaves |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://python.org) | 3.10+ | Runtime |
| [Ollama](https://ollama.com) | Latest | Local LLM server |
| [Gemma 4](https://ollama.com/library/gemma4) | Latest | Default analysis model |

### 1 · Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/stack-trace-explainer.git
cd stack-trace-explainer

# Install dependencies
pip install -r requirements.txt
pip install -e .

# Pull the default model
ollama serve          # Start Ollama (if not already running)
ollama pull gemma4    # Download the model (~5 GB)
```

### 2 · Explain Your First Stack Trace

Save a traceback to a file (or use one from your own project):

```python
# buggy.py — run this to generate a real traceback
import json

def load_user_config(path):
    with open(path) as f:
        config = json.load(f)
    return config["database"]["host"]

def main():
    settings = load_user_config("settings.json")  # file doesn't exist
    print(f"Connecting to {settings}...")

main()
```

```bash
# Generate the traceback
python buggy.py 2> error.txt

# Explain it
stack-explainer explain --trace error.txt
```

**Expected output:**

```
╭──────────────────────────────────────────────────────────╮
│  🔥 Stack Trace Explainer                                │
╰──────────────────────────────────────────────────────────╯

 Language: python
 Quick hint: The file you're trying to open doesn't exist at that path

╭── 📜 Stack Trace Preview ───────────────────────────────╮
│ Traceback (most recent call last):                       │
│   File "buggy.py", line 11, in <module>                  │
│     main()                                               │
│   File "buggy.py", line 8, in main                       │
│     settings = load_user_config("settings.json")         │
│   File "buggy.py", line 4, in load_user_config           │
│     with open(path) as f:                                │
│ FileNotFoundError: [Errno 2] No such file or directory:  │
│   'settings.json'                                        │
╰──────────────────────────────────────────────────────────╯

╭── 💡 Explanation ───────────────────────────────────────╮
│ ## Error Summary                                         │
│ A FileNotFoundError was raised because the file          │
│ "settings.json" does not exist in the current working    │
│ directory.                                               │
│                                                          │
│ ## Root Cause                                            │
│ The function `load_user_config` uses a relative path     │
│ "settings.json". If the script is run from a different   │
│ directory, the file won't be found.                      │
│                                                          │
│ ## Call Chain                                             │
│ main() → load_user_config("settings.json") → open(path) │
│                                                          │
│ ## Suggested Fix                                         │
│ 1. Check if the file exists before opening               │
│ 2. Use an absolute path or Path(__file__).parent         │
│ 3. Wrap in try/except FileNotFoundError                  │
│                                                          │
│ ## Prevention                                            │
│ Always validate file paths and provide clear error       │
│ messages when configuration files are missing.           │
╰──────────────────────────────────────────────────────────╯
```

### 3 · Generate a Fix

```bash
stack-explainer explain --trace error.txt --fix
```

```python
# ✅ Generated Fix
import json
from pathlib import Path

def load_user_config(path):
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found: {config_path.resolve()}\n"
            f"Create it or pass a valid path."
        )
    with open(config_path) as f:
        config = json.load(f)
    return config.get("database", {}).get("host", "localhost")
```

### 4 · Find Similar Errors

```bash
stack-explainer explain --trace error.txt --similar
```

```
🔗 Similar Errors:
  1. FileNotFoundError vs IsADirectoryError — path exists but is a directory
  2. FileNotFoundError vs PermissionError — file exists but can't be read
  3. FileNotFoundError vs FileExistsError — opposite case, file already exists
  4. FileNotFoundError vs OSError — parent class, more general I/O errors
```

### 5 · Pipe Directly from a Failing Command

```bash
python buggy.py 2>&1 | stack-explainer explain
python buggy.py 2>&1 | stack-explainer explain --fix --similar
```

---

## 📋 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com) and installed as the `stack-explainer` console script.

### Global Options

| Option | Short | Description |
|:-------|:------|:------------|
| `--config` | | Path to YAML config file (default: `config.yaml`) |
| `--verbose` | `-v` | Enable verbose/debug logging |

### `explain` Command

```bash
stack-explainer [--config FILE] [-v] explain [OPTIONS]
```

| Option | Short | Type | Description |
|:-------|:------|:-----|:------------|
| `--trace` | `-t` | `FILE` | Read stack trace from a file |
| `--text` | | `STRING` | Pass stack trace as inline text |
| `--lang` | `-l` | `STRING` | Language hint (e.g. `python`, `java`, `javascript`) — auto-detected if omitted |
| `--fix` | | `FLAG` | Generate corrected code with explanatory comments |
| `--similar` | | `FLAG` | Find 3-5 similar/related error types |

> **Input priority:** `--trace` file > `--text` string > stdin pipe. At least one input source is required.

### Usage Examples

```bash
# Basic — explain a trace file
stack-explainer explain --trace error.txt

# Inline text
stack-explainer explain --text "Traceback (most recent call last):
  File \"app.py\", line 10, in <module>
    x = int(\"hello\")
ValueError: invalid literal for int() with base 10: 'hello'"

# Force a specific language
stack-explainer explain --trace crash.log --lang java

# Full analysis — explanation + fix + similar errors
stack-explainer explain --trace error.txt --fix --similar

# Pipe from a failing test suite
python -m pytest tests/ 2>&1 | stack-explainer explain --fix

# Pipe from any command
node server.js 2>&1 | stack-explainer explain --lang javascript

# Verbose mode for debugging
stack-explainer -v explain --trace error.txt

# Custom config file
stack-explainer --config my-config.yaml explain --trace error.txt
```

---

## 🌐 Web UI

Stack Trace Explainer includes a full [Streamlit](https://streamlit.io) web interface for browser-based analysis.

### Launch

```bash
streamlit run src/stack_explainer/web_ui.py
# Opens at http://localhost:8501
```

### Web UI Features

| Area | Features |
|:-----|:---------|
| **Sidebar** | Model selector, temperature slider (0.0–1.0), max tokens (512–8192), language dropdown, fix/similar toggles, common error reference browser |
| **Input** | Paste tab (textarea) or Upload tab (`.txt`, `.log`, `.err` files) |
| **Output** | Detected language & error type metrics, markdown explanation, fix code block, similar errors list |
| **Export** | Download full analysis as a Markdown file |

### Running with Make

```bash
make web    # Shortcut for streamlit run src/stack_explainer/web_ui.py
```

---

## 🏗️ Architecture

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg">
  <img alt="Architecture Overview" src="docs/images/architecture.svg" width="800">
</picture>
</div>

<br/>

### Data Flow

```
Input (file / text / stdin)
  │
  ├─▶ Language Detector ─── keyword matching across 11 language indicator sets
  │
  ├─▶ Error Type Extractor ─── regex extraction of final error line
  │       │
  │       └─▶ Hint Matcher ─── lookup in built-in COMMON_ERRORS database
  │
  └─▶ Prompt Builder ─── assembles system prompt + trace + language + hints
          │
          ▼
      Ollama LLM (Gemma 4) ─── local inference, no cloud calls
          │
          ├─▶ Explanation ─── 5-point structured analysis
          ├─▶ Fix Code ─── corrected source with comments (optional)
          └─▶ Similar Errors ─── 3-5 related error types (optional)
```

### Project Structure

```
23-stack-trace-explainer/
│
├── src/stack_explainer/           # Main package
│   ├── __init__.py                # v1.0.0, app name
│   ├── core.py                    # explain_trace, generate_fix_code, find_similar_errors
│   ├── cli.py                     # Click CLI — explain command with all options
│   ├── web_ui.py                  # Streamlit web interface
│   ├── config.py                  # ExplainerConfig dataclass, YAML + env loading
│   └── utils.py                   # detect_language, extract_error_type, error database
│
├── common/
│   └── llm_client.py              # Shared Ollama client (chat, stream, embed, health check)
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py               # Unit tests: detection, extraction, config, explain
│   └── test_cli.py                # CLI integration tests with CliRunner
│
├── docs/
│   └── images/                    # SVG diagrams for README
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
│
├── config.yaml                    # Default configuration
├── .env.example                   # Environment variable template
├── requirements.txt               # Runtime + dev dependencies
├── setup.py                       # Installable package with console_scripts entry point
├── Makefile                       # Dev shortcuts (test, lint, run, web, clean)
└── README.md                      # This file
```

### Module Responsibilities

| Module | Responsibility |
|:-------|:---------------|
| `core.py` | LLM interaction — sends structured prompts to Ollama and parses responses. Contains `SYSTEM_PROMPT`, `FIX_CODE_PROMPT`, `SIMILAR_ERRORS_PROMPT` templates |
| `cli.py` | Click command group with `explain` sub-command. Handles input routing, Ollama health checks, Rich console output, and status spinners |
| `web_ui.py` | Streamlit app with sidebar settings, paste/upload input tabs, analysis display, and Markdown export |
| `config.py` | `ExplainerConfig` dataclass with layered loading: hardcoded defaults → YAML file → environment variables |
| `utils.py` | Language detection via keyword scoring, error type regex extraction, `COMMON_ERRORS` hint database, trace truncation |
| `llm_client.py` | Shared Ollama HTTP client used across all 90 projects — `chat()`, `chat_stream()`, `generate()`, `embed()`, `check_ollama_running()` |

---

## 📚 API Reference

### `core.explain_trace(trace, language, config)`

Analyze a stack trace and return a structured explanation.

```python
from stack_explainer.core import explain_trace
from stack_explainer.config import load_config

config = load_config()
result = explain_trace(
    trace="Traceback (most recent call last):\n  File \"app.py\", line 5\nKeyError: 'id'",
    language=None,   # auto-detect
    config=config
)

print(result["explanation"])   # Full LLM-generated explanation
print(result["language"])      # "python"
print(result["error_type"])    # "KeyError: 'id'"
print(result["error_hint"])    # "Accessing a dictionary key that doesn't exist"
```

**Returns:** `dict` with keys `explanation`, `language`, `error_type`, `error_hint`, `trace_preview`

---

### `core.generate_fix_code(trace, explanation, config)`

Generate corrected code based on the trace and explanation.

```python
from stack_explainer.core import generate_fix_code

fix = generate_fix_code(
    trace="...",
    explanation="The KeyError occurs because...",
    config=config
)
print(fix)  # Corrected Python code with comments
```

**Returns:** `str` — corrected code with inline comments explaining each change

---

### `core.find_similar_errors(trace, config)`

Find 3-5 error types commonly confused with the one in the trace.

```python
from stack_explainer.core import find_similar_errors

similar = find_similar_errors(trace="...", config=config)
print(similar)  # Markdown list of related errors with distinctions
```

**Returns:** `str` — Markdown-formatted list of similar errors with explanations

---

### `utils.detect_language(trace)`

Auto-detect the programming language from a stack trace string.

```python
from stack_explainer.utils import detect_language

lang = detect_language('Traceback (most recent call last):\n  File "app.py"')
# Returns: "python"
```

**Returns:** `str` — language name or `"unknown"`. Requires ≥2 keyword matches from the language indicator set.

---

### `utils.extract_error_type(trace)`

Extract the error type string from the last line of a trace.

```python
from stack_explainer.utils import extract_error_type

err = extract_error_type("...\nKeyError: 'missing_key'")
# Returns: "KeyError: 'missing_key'"
```

---

### `utils.get_error_hint(language, error_type)`

Look up a quick human-readable hint for a known error type.

```python
from stack_explainer.utils import get_error_hint

hint = get_error_hint("python", "KeyError")
# Returns: "Accessing a dictionary key that doesn't exist"
```

**Returns:** `str | None` — hint text or `None` if error type is not in the database.

---

### `config.load_config(config_path)`

Load configuration from a YAML file with environment variable overrides.

```python
from stack_explainer.config import load_config

config = load_config("config.yaml")
print(config.model)          # "gemma4"
print(config.temperature)    # 0.3
print(config.max_tokens)     # 4096
```

**Returns:** `ExplainerConfig` dataclass

---

## ⚙️ Configuration

### `config.yaml` (defaults)

```yaml
ollama_base_url: "http://localhost:11434"
model: "gemma4"
temperature: 0.3
max_tokens: 4096
max_trace_chars: 5000
log_level: "INFO"
```

### Configuration Precedence

Settings are resolved in this order (highest priority first):

| Priority | Source | Example |
|:---------|:-------|:--------|
| 1 (highest) | CLI arguments | `--config custom.yaml` |
| 2 | Environment variables | `OLLAMA_MODEL=llama3` |
| 3 | `config.yaml` file | `model: "gemma4"` |
| 4 (lowest) | Hardcoded defaults | `ExplainerConfig()` defaults |

### Environment Variables

| Variable | Description | Default |
|:---------|:------------|:--------|
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | LLM model to use | `gemma4` |
| `LOG_LEVEL` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`) | `INFO` |
| `STACK_EXPLAINER_CONFIG` | Path to config file | `config.yaml` |

### `.env.example`

```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma4
LOG_LEVEL=INFO
STACK_EXPLAINER_CONFIG=config.yaml
```

### ExplainerConfig Fields

| Field | Type | Default | Description |
|:------|:-----|:--------|:------------|
| `ollama_base_url` | `str` | `http://localhost:11434` | Ollama API endpoint |
| `model` | `str` | `gemma4` | Model name for inference |
| `temperature` | `float` | `0.3` | LLM creativity (0.0 = deterministic, 1.0 = creative) |
| `max_tokens` | `int` | `4096` | Maximum response tokens |
| `max_trace_chars` | `int` | `5000` | Truncate traces longer than this |
| `log_level` | `str` | `INFO` | Python logging level |

---

## 🧪 Testing

### Run All Tests

```bash
python -m pytest tests/ -v
```

### Run with Coverage

```bash
python -m pytest tests/ -v --cov=src/stack_explainer --cov-report=term-missing
```

### Using Make

```bash
make test       # pytest tests/ -v --tb=short
make test-cov   # pytest with coverage report
make lint       # py_compile check on core modules
```

### Test Structure

| File | Tests | What's Covered |
|:-----|:------|:---------------|
| `test_core.py` | 15 tests | Language detection (Python/Java/JS/unknown), error type extraction, error hint lookup, file reading, trace truncation, `explain_trace` with mocked LLM, config loading |
| `test_cli.py` | 4 tests | CLI with `--trace` file, `--text` input, Ollama-down error handling, missing input validation |

### Test Examples

```python
# Language detection
def test_detect_python():
    trace = 'Traceback (most recent call last):\n  File "app.py", line 5\nKeyError: "x"'
    assert detect_language(trace) == "python"

# Error extraction
def test_extract_error_type():
    trace = "...\njava.lang.NullPointerException: Cannot invoke method"
    assert "NullPointerException" in extract_error_type(trace)

# CLI integration
def test_cli_with_trace_file(tmp_path):
    trace_file = tmp_path / "error.txt"
    trace_file.write_text("Traceback...\nKeyError: 'x'")
    result = runner.invoke(cli, ["explain", "--trace", str(trace_file)])
    assert result.exit_code == 0
```

---

## 🔐 Local vs Cloud

| Aspect | Stack Trace Explainer (Local) | Cloud-Based Tools |
|:-------|:------------------------------|:------------------|
| **Privacy** | ✅ All data stays on your machine | ❌ Traces sent to third-party servers |
| **Cost** | ✅ Free after model download | ❌ Per-token API charges |
| **Speed** | ⚡ No network latency (after model load) | 🐌 Depends on network + API load |
| **Offline** | ✅ Works without internet | ❌ Requires active connection |
| **Customization** | ✅ Swap models, adjust prompts | ❌ Limited to provider's model |
| **Data Retention** | ✅ Nothing logged or stored remotely | ❓ Check provider's data policy |
| **Model Quality** | 🟡 Smaller models vs frontier | ✅ Access to largest models |
| **Setup** | 🟡 Requires Ollama + model download | ✅ API key and go |

> **Bottom line:** Use local when privacy, cost, or offline access matters. Use cloud when you need the absolute best model quality for complex traces.

---

## ❓ FAQ

<details>
<summary><strong>1. Which Ollama models work best?</strong></summary>

The default model is **Gemma 4** (`gemma4`), which provides an excellent balance of speed and quality for error analysis. Other good options:

| Model | Speed | Quality | Notes |
|:------|:------|:--------|:------|
| `gemma4` | ⚡⚡ | ⭐⭐⭐⭐ | Default — fast and accurate |
| `llama3` | ⚡⚡ | ⭐⭐⭐⭐ | Great alternative |
| `codellama` | ⚡⚡⚡ | ⭐⭐⭐ | Optimized for code tasks |
| `mistral` | ⚡⚡⚡ | ⭐⭐⭐ | Fast, good for simple traces |
| `deepseek-coder` | ⚡⚡ | ⭐⭐⭐⭐ | Strong at code generation |

To switch models:
```bash
ollama pull llama3
export OLLAMA_MODEL=llama3
# or edit config.yaml: model: "llama3"
```
</details>

<details>
<summary><strong>2. What languages are supported for auto-detection?</strong></summary>

The language detector supports **11 languages** via keyword matching:

Python · JavaScript · Java · C# · Go · Rust · Ruby · PHP · Kotlin · Swift · C++

Each language has a set of indicator keywords (e.g., `Traceback`, `File "..."` for Python; `at com.`, `java.lang.` for Java). The detector requires at least 2 keyword matches to identify a language. You can always override with `--lang`.
</details>

<details>
<summary><strong>3. What if Ollama isn't running?</strong></summary>

The CLI performs a health check before analysis. If Ollama is unreachable, you'll see:

```
❌ Ollama is not running at http://localhost:11434
   Start it with: ollama serve
```

Quick fix:
```bash
ollama serve &          # Start Ollama in background
ollama list             # Verify models are available
stack-explainer explain --trace error.txt   # Try again
```
</details>

<details>
<summary><strong>4. Can I use this in CI/CD pipelines?</strong></summary>

Yes! The stdin pipe support makes it perfect for CI integration:

```yaml
# GitHub Actions example
- name: Explain test failures
  run: |
    python -m pytest tests/ 2>&1 | stack-explainer explain --fix || true
```

```bash
# Jenkins / shell script
./run_tests.sh 2>&1 | stack-explainer explain --fix > analysis.md
```
</details>

<details>
<summary><strong>5. How do I add support for a new language?</strong></summary>

Add keyword indicators in `src/stack_explainer/utils.py`:

```python
# In LANGUAGE_INDICATORS dict
"kotlin": ["at ", "kotlin.", "KotlinNullPointerException", ".kt:"],

# In COMMON_ERRORS dict
"kotlin": {
    "KotlinNullPointerException": "Accessing a null reference in Kotlin",
    "UninitializedPropertyAccessException": "Accessing a lateinit property before initialization",
}
```

Then add a test case in `tests/test_core.py` and submit a PR!
</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and install in development mode
git clone https://github.com/kennedyraju55/stack-trace-explainer.git
cd stack-trace-explainer
pip install -r requirements.txt
pip install -e .

# Run tests
make test

# Run linter
make lint
```

### Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes with tests
4. **Test**: `make test`
5. **Commit**: `git commit -m 'feat: add amazing feature'`
6. **Push**: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

### Areas for Contribution

- 🌐 Add new language detection keywords
- 📚 Expand the error hint database
- 🧪 Add more test cases
- 📖 Improve documentation
- 🔧 Add new output formats (JSON, HTML)
- 🌍 Internationalization support

---

## 📄 License

This project is part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection.

See the root [LICENSE](../LICENSE) file for details. MIT License.

---

<div align="center">

<sub>

**[Stack Trace Explainer](https://github.com/kennedyraju55/stack-trace-explainer)** · Project #23 of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

Built with ❤️ using [Ollama](https://ollama.com) · [Gemma 4](https://ai.google.dev/gemma) · [Click](https://click.palletsprojects.com) · [Streamlit](https://streamlit.io) · [Rich](https://github.com/Textualize/rich)

</sub>

</div>
