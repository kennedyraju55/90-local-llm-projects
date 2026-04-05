<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img src="docs/images/banner.svg" alt="Regex Generator — Natural Language to Regular Expressions with Local LLMs" width="800">
</picture>

<br/>
<br/>

[![Gemma 4](https://img.shields.io/badge/Gemma_4-Ollama-ff6b35?style=flat-square&logo=google&logoColor=white)](#prerequisites)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776ab?style=flat-square&logo=python&logoColor=white)](#prerequisites)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=flat-square&logo=streamlit&logoColor=white)](#-web-ui)
[![CLI](https://img.shields.io/badge/Click-CLI-44cc11?style=flat-square&logo=gnu-bash&logoColor=white)](#-cli-reference)
[![License: MIT](https://img.shields.io/badge/License-MIT-ffa62b?style=flat-square)](#-license)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square)](#-testing)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

**Describe what you need in plain English — get a production-ready regex instantly.**<br/>
Powered by a **100 % local** Ollama LLM. No data ever leaves your machine.

<br/>

<em>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</em>

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
- [Pattern Library](#-pattern-library)
- [Configuration](#%EF%B8%8F-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Regular expressions are one of the most powerful — and most hated — tools in a
developer's toolbox. You *know* the pattern you need, you just can't remember
whether it's `(?:…)` or `(?=…)` or `\b` or `\B`.

**Regex Generator** fixes that by letting you talk to a local LLM in plain
English:

```
"match email addresses"         →  [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
"US phone numbers with dashes"  →  \(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
"ISO 8601 dates"                →  \d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])
```

Everything runs **locally** — your prompts, your patterns, and the model weights
never leave your machine. No API keys. No usage limits. No privacy concerns.

---

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Key Features" width="800">
</div>

<br/>

| Feature | Description |
|:--------|:------------|
| 💬 **Natural Language → Regex** | Describe what you want to match in plain English and get a working regex pattern |
| 📖 **Pattern Explanation** | Paste any regex and get a component-by-component breakdown in plain English |
| 🧪 **Live Regex Tester** | Test patterns against multiple strings with match highlighting and group extraction |
| 📚 **Built-in Pattern Library** | 13+ pre-built, battle-tested patterns for common use cases |
| 🌐 **Multi-Flavor Support** | Generate patterns for Python, JavaScript, PCRE, POSIX, Java, .NET, Go, and Rust |
| ✅ **Automatic Validation** | Every generated pattern is validated for syntax, groups, and compilability |
| 🎯 **Smart Extraction** | Automatically parses the primary regex from LLM response text and markdown code blocks |
| 🖥️ **Streamlit Web UI** | Interactive three-tab web interface — Generate, Explain, and Test |
| ⚙️ **YAML + Env Configuration** | Flexible YAML config with environment variable overrides |
| 🎨 **Rich Terminal Output** | Beautiful colored CLI output with panels, tables, and spinners |
| 🔒 **100 % Local** | No data ever leaves your machine — complete privacy |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| **Python** | 3.10+ | Runtime |
| **Ollama** | Latest | Local LLM server |
| **Gemma 4** | — | Default generation model |

### 1. Clone and install

```bash
git clone https://github.com/kennedyraju55/regex-generator.git
cd regex-generator

pip install -r requirements.txt
pip install -e .
```

### 2. Start Ollama and pull the model

```bash
ollama serve                  # Start the Ollama server
ollama pull gemma4            # Pull the Gemma 4 model (~5 GB)
```

### 3. Generate your first regex

```bash
python -m regex_gen.cli generate "match email addresses"
```

**Expected output:**

```
╭──────────────────────────────────────────────────╮
│  🔤 Regex Generator                              │
│  Generate regex from natural language             │
╰──────────────────────────────────────────────────╯

  Description : match email addresses
  Flavor      : python

╭── 🎯 Generated Regex ───────────────────────────╮
│                                                  │
│  [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,} │
│                                                  │
╰──────────────────────────────────────────────────╯
```

### 4. Generate and test in one step

```bash
python -m regex_gen.cli generate "US phone numbers" \
    --flavor python \
    -t "(555) 123-4567" \
    -t "not-a-phone" \
    -t "555-867-5309"
```

```
╭── 🎯 Generated Regex ─────────────────────────────╮
│  \(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}              │
╰────────────────────────────────────────────────────╯

┌──────────────────────────────────────────────────┐
│ String           │ Match │ Matched Text           │
├──────────────────┼───────┼────────────────────────┤
│ (555) 123-4567   │  ✅   │ (555) 123-4567         │
│ not-a-phone      │  ❌   │ —                      │
│ 555-867-5309     │  ✅   │ 555-867-5309           │
└──────────────────────────────────────────────────┘
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/regex-generator.git
cd regex-generator
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
uvicorn src.regex_gen.api:app --reload --port 8000

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

The CLI is built with [Click](https://click.palletsprojects.com/) and uses
[Rich](https://rich.readthedocs.io/) for beautiful terminal output.

### Commands at a Glance

| Command | Syntax | Description |
|:--------|:-------|:------------|
| **generate** | `generate DESCRIPTION [--flavor FLAVOR] [-t STRING]…` | Generate a regex from a natural language description |
| **explain** | `explain PATTERN` | Explain a regex pattern in plain English |
| **test** | `test PATTERN STRING [STRING]…` | Test a pattern against one or more strings |
| **library** | `library [NAME]` | Browse or look up a specific pattern from the built-in library |

### `generate` — Natural Language → Regex

```bash
# Basic generation (default flavor: python)
python -m regex_gen.cli generate "match IPv4 addresses"

# Specify a target regex flavor
python -m regex_gen.cli generate "valid hex color codes" --flavor javascript

# Generate and immediately test against sample strings
python -m regex_gen.cli generate "ISO 8601 dates" \
    -t "2024-01-15" \
    -t "2024-13-40" \
    -t "not a date"
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--flavor` | `-f` | `python` | Target regex flavor (`python`, `javascript`, `pcre`, `ruby`, `go`, `java`) |
| `--test` | `-t` | — | Test string (repeatable). Pattern is tested against each provided string |

### `explain` — Pattern Explanation

```bash
python -m regex_gen.cli explain "^(?:[a-zA-Z0-9._%+-]+)@(?:[a-zA-Z0-9.-]+)\.[a-zA-Z]{2,}$"
```

```
╭── 📖 Regex Explanation ──────────────────────────╮
│                                                  │
│  ^               Start of string                 │
│  (?:…)           Non-capturing group             │
│  [a-zA-Z0-9…]+   One or more word/special chars  │
│  @               Literal "@"                     │
│  (?:…)           Non-capturing group             │
│  [a-zA-Z0-9.-]+  Domain characters               │
│  \.              Escaped dot                     │
│  [a-zA-Z]{2,}   TLD — 2 or more letters          │
│  $               End of string                   │
│                                                  │
╰──────────────────────────────────────────────────╯
```

### `test` — Pattern Testing

```bash
python -m regex_gen.cli test "\d{3}-\d{4}" "555-1234" "hello" "123-4567"
```

```
┌────────────────────────────────────────────┐
│ String     │ Match │ Text      │ Span      │
├────────────┼───────┼───────────┼───────────┤
│ 555-1234   │  ✅   │ 555-1234  │ (0, 8)    │
│ hello      │  ❌   │ —         │ —         │
│ 123-4567   │  ✅   │ 123-4567  │ (0, 8)    │
└────────────────────────────────────────────┘
```

### `library` — Pattern Library

```bash
# List all available patterns
python -m regex_gen.cli library

# Look up a specific pattern
python -m regex_gen.cli library email
python -m regex_gen.cli library uuid
```

---

## 🌐 Web UI

Regex Generator includes a full **Streamlit** web interface with three
interactive tabs.

### Launch

```bash
streamlit run src/regex_gen/web_ui.py
# → Opens at http://localhost:8501
```

### Tabs

| Tab | Purpose |
|:----|:--------|
| ✨ **Generate** | Enter a natural language description, pick a flavor, and generate a regex. Optionally test inline |
| 📖 **Explain** | Paste any regex pattern and get a detailed, human-readable explanation plus validation status |
| 🧪 **Test** | Enter a pattern and a list of test strings to see matches, groups, and span positions |

### Sidebar

- **Model selector** — choose any Ollama model available on your machine
- **Temperature slider** — control creativity vs determinism (0.0–1.0)
- **Pattern library quick access** — click any built-in pattern to auto-fill

---

## 🏗️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="Architecture Overview" width="800">
</div>

<br/>

The project follows a clean layered architecture with three entry points
(CLI, Web UI, Python API) that all flow through the same core engine.

### Project Structure

```
24-regex-generator/
├── src/
│   └── regex_gen/
│       ├── __init__.py            # Package metadata & version
│       ├── core.py                # Core engine — generate, explain, library
│       ├── cli.py                 # Click CLI — 4 commands
│       ├── web_ui.py              # Streamlit web interface — 3 tabs
│       ├── config.py              # RegexConfig dataclass, YAML loader,
│       │                          #   PATTERN_LIBRARY, REGEX_FLAVORS
│       └── utils.py               # run_regex_test, validate_regex,
│                                  #   extract_regex_from_text, highlight_matches
├── common/
│   └── llm_client.py              # Shared Ollama HTTP client (chat, stream,
│                                  #   generate, embed, health check)
├── tests/
│   ├── __init__.py
│   ├── test_core.py               # 13 test classes — core logic
│   └── test_cli.py                # 6 tests — CLI invocations
├── docs/
│   └── images/
│       ├── banner.svg             # Project banner
│       ├── architecture.svg       # Architecture diagram
│       └── features.svg           # Feature cards
├── config.yaml                    # Default YAML configuration
├── setup.py                       # Package setup (entry point: regex-gen)
├── requirements.txt               # Runtime + dev dependencies
├── Makefile                       # Dev workflow shortcuts
├── .env.example                   # Environment variable template
└── README.md                      # ← You are here
```

### Data Flow

1. **Generate mode** — A natural language description is combined with
   flavor-specific context by the **Prompt Builder**, sent to the **Ollama LLM**,
   and the raw response is parsed by the **Pattern Extractor** to isolate the
   regex. The pattern is then validated and optionally tested.

2. **Explain mode** — An existing regex pattern is sent to the LLM with an
   explanation system prompt. The response is formatted and displayed.

3. **Library mode** — A pattern name is looked up in the built-in
   `PATTERN_LIBRARY` dictionary. No LLM call is needed.

---

## 🔌 API Reference

Use Regex Generator as a Python library in your own projects.

### `generate_regex`

Generate a regex pattern from a natural language description.

```python
from regex_gen.core import generate_regex
from regex_gen.config import load_config

config = load_config()

result = generate_regex(
    description="match email addresses",
    flavor="python",
    config=config
)

print(result)
# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `description` | `str` | *required* | Natural language description of the desired pattern |
| `flavor` | `str` | `"python"` | Regex flavor — `python`, `javascript`, `pcre`, `ruby`, `go`, `java` |
| `config` | `RegexConfig` | `None` | Configuration object (uses defaults if `None`) |

### `explain_regex`

Explain an existing regex pattern in plain English.

```python
from regex_gen.core import explain_regex
from regex_gen.config import load_config

config = load_config()

explanation = explain_regex(
    pattern=r"^(?:\+1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$",
    config=config
)

print(explanation)
# This pattern matches US phone numbers in various formats:
# - (555) 123-4567
# - 555-123-4567
# - +1 555.123.4567
# ...
```

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `pattern` | `str` | *required* | The regex pattern to explain |
| `config` | `RegexConfig` | `None` | Configuration object |

### `get_pattern_from_library`

Retrieve a pre-built regex pattern by name.

```python
from regex_gen.core import get_pattern_from_library

pattern = get_pattern_from_library("email")
print(pattern)
# [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

### `list_library_patterns`

List all available patterns in the built-in library.

```python
from regex_gen.core import list_library_patterns

patterns = list_library_patterns()
for name in patterns:
    print(name)
```

### Utility Functions

```python
from regex_gen.utils import run_regex_test, validate_regex, extract_regex_from_text

# Test a pattern against strings
results = run_regex_test(r"\d+", ["abc123", "hello", "42"])
# [{'string': 'abc123', 'matches': True, 'match': '123', ...}, ...]

# Validate regex syntax
info = validate_regex(r"[a-z]+")
# {'valid': True, 'groups': 0, 'error': None}

# Extract regex from LLM markdown output
pattern = extract_regex_from_text("Here is the pattern: ```regex\n\\d+\n```")
# \d+
```

---

## 📚 Pattern Library

The built-in pattern library provides instant access to 13 commonly needed
regex patterns — no LLM call required.

| Name | Pattern | Example Match |
|:-----|:--------|:--------------|
| `email` | `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` | `user@example.com` |
| `url` | `https?://[^\s/$.?#].[^\s]*` | `https://example.com/path` |
| `ipv4` | `\b(?:\d{1,3}\.){3}\d{1,3}\b` | `192.168.1.1` |
| `phone_us` | `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` | `(555) 123-4567` |
| `date_iso` | `\d{4}-(?:0[1-9]\|1[0-2])-(?:0[1-9]\|[12]\d\|3[01])` | `2024-01-15` |
| `hex_color` | `#(?:[0-9a-fA-F]{3}){1,2}\b` | `#ff6b35` |
| `uuid` | `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}` | `550e8400-e29b-41d4-a716-446655440000` |
| `credit_card` | `\b(?:\d{4}[-\s]?){3}\d{4}\b` | `4111-1111-1111-1111` |
| `ssn` | `\b\d{3}-\d{2}-\d{4}\b` | `123-45-6789` |
| `zip_us` | `\b\d{5}(?:-\d{4})?\b` | `90210` |
| `username` | `^[a-zA-Z][a-zA-Z0-9._-]{2,29}$` | `john_doe99` |
| `password_strong` | `^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$` | `P@ssw0rd!` |

### Usage

```bash
# List all patterns
python -m regex_gen.cli library

# Get a specific pattern
python -m regex_gen.cli library email
python -m regex_gen.cli library uuid
```

---

## ⚙️ Configuration

### `config.yaml`

```yaml
ollama_base_url: "http://localhost:11434"
model: "gemma4"
temperature: 0.3
max_tokens: 2048
default_flavor: "python"
log_level: "INFO"
```

| Key | Default | Description |
|:----|:--------|:------------|
| `ollama_base_url` | `http://localhost:11434` | Ollama server URL |
| `model` | `gemma4` | Model to use for generation and explanation |
| `temperature` | `0.3` | LLM temperature (0.0 = deterministic, 1.0 = creative) |
| `max_tokens` | `2048` | Maximum token length for LLM responses |
| `default_flavor` | `python` | Default regex flavor when none is specified |
| `log_level` | `INFO` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |

### Environment Variable Overrides

Environment variables take precedence over `config.yaml`.

```bash
export OLLAMA_BASE_URL=http://localhost:11434
export OLLAMA_MODEL=gemma4
export LOG_LEVEL=DEBUG
export REGEX_GEN_CONFIG=config.yaml      # Path to config file
```

### Supported Regex Flavors

| Flavor | Flag | Notes |
|:-------|:-----|:------|
| Python | `python` | Default. Uses `re` module syntax |
| JavaScript | `javascript` | ECMAScript compatible |
| PCRE | `pcre` | Perl Compatible Regular Expressions |
| POSIX | `posix` | Basic/Extended POSIX syntax |
| Java | `java` | `java.util.regex` compatible |
| .NET | `dotnet` | .NET `Regex` class syntax |
| Go | `go` | RE2 syntax (no backreferences) |
| Rust | `rust` | `regex` crate syntax |

---

## 🧪 Testing

The project includes comprehensive tests covering core logic, CLI commands,
and utility functions.

### Run all tests

```bash
python -m pytest tests/ -v
```

### Run with coverage

```bash
python -m pytest tests/ -v --cov=src/regex_gen --cov-report=term-missing
```

### Using Make

```bash
make test           # Run tests with verbose output
make test-cov       # Run tests with coverage report
make lint           # Syntax check on core modules
```

### Test Structure

| File | Tests | Covers |
|:-----|:------|:-------|
| `tests/test_core.py` | 13 test classes | Regex testing, validation, extraction, generation (mocked), explanation (mocked), pattern library |
| `tests/test_cli.py` | 6 test methods | CLI command invocations, Ollama availability checks |

---

## 🔒 Local vs Cloud

| | Regex Generator (Local) | Cloud-Based Alternatives |
|:-|:------------------------|:-------------------------|
| **Privacy** | ✅ 100 % local — nothing leaves your machine | ❌ Prompts sent to third-party servers |
| **Cost** | ✅ Free forever | ❌ Pay-per-token API pricing |
| **Latency** | ✅ No network round-trip | ❌ Depends on API latency |
| **Rate Limits** | ✅ None | ❌ Throttled by provider |
| **Offline** | ✅ Works without internet | ❌ Requires connectivity |
| **Customization** | ✅ Swap models freely | ❌ Locked to provider's models |
| **Setup** | ⚠️ Requires Ollama + model download | ✅ Just an API key |

---

## ❓ FAQ

<details>
<summary><strong>1. Which models work best?</strong></summary>

The default **Gemma 4** model provides excellent regex generation.
Any instruction-tuned model available through Ollama will work — simply change
the `model` field in `config.yaml`. Larger models like `llama3` or `mistral`
can also produce good results.
</details>

<details>
<summary><strong>2. Can I use this without Ollama for the pattern library?</strong></summary>

Yes! The `library` command and `get_pattern_from_library()` function work
entirely offline with no LLM required. Only the `generate` and `explain`
commands need a running Ollama instance.
</details>

<details>
<summary><strong>3. How do I add custom patterns to the library?</strong></summary>

Edit the `PATTERN_LIBRARY` dictionary in `src/regex_gen/config.py`. Add your
pattern with a descriptive key:

```python
PATTERN_LIBRARY = {
    # ... existing patterns ...
    "my_custom_pattern": r"your-regex-here",
}
```
</details>

<details>
<summary><strong>4. The generated regex doesn't match what I expected. What can I do?</strong></summary>

Try being more specific in your description. Instead of *"match dates"*, try
*"match dates in MM/DD/YYYY format"*. You can also lower the `temperature` in
`config.yaml` for more deterministic output, or try a different `--flavor`.
</details>

<details>
<summary><strong>5. Does it support regex flags like case-insensitive or multiline?</strong></summary>

Yes. Include the requirement in your description:
*"match email addresses, case insensitive"*. The LLM will include the
appropriate flags (`re.IGNORECASE`, `/i`, etc.) based on the target flavor.
</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Install** dev dependencies (`pip install -r requirements.txt && pip install -e .`)
4. **Make** your changes
5. **Run** the test suite (`python -m pytest tests/ -v`)
6. **Commit** your changes (`git commit -m 'Add amazing feature'`)
7. **Push** to the branch (`git push origin feature/amazing-feature`)
8. **Open** a Pull Request

### Development Commands

```bash
make install        # Install dependencies
make install-dev    # Install with editable mode
make test           # Run test suite
make test-cov       # Run tests with coverage
make lint           # Syntax-check core modules
make run DESC="…"   # Quick generate from CLI
make web            # Launch Streamlit web UI
make clean          # Clean cache and temp files
```

---

## 📄 License

This project is licensed under the **MIT License**.

Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)
collection. See the root [LICENSE](../LICENSE) for details.

---

<div align="center">

<br/>

**[⬆ Back to Top](#)**

<br/>

Made with 🔥 and local LLMs

<sub>Built with <a href="https://ollama.com">Ollama</a> · <a href="https://ai.google.dev/gemma">Gemma 4</a> · <a href="https://click.palletsprojects.com">Click</a> · <a href="https://rich.readthedocs.io">Rich</a> · <a href="https://streamlit.io">Streamlit</a></sub>

</div>
