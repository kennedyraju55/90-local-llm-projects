<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img alt="Code Translator Banner" src="docs/images/banner.svg" width="800">
</picture>

<br/>

# 🔄 Code Translator

**Translate code between programming languages using local LLMs — 100% private, 100% offline.**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776ab?logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-e63946?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iMTAiIGZpbGw9IndoaXRlIi8+PC9zdmc+)](https://ollama.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Click CLI](https://img.shields.io/badge/Click-Rich%20CLI-4EAA25?logo=gnubash&logoColor=white)](https://click.palletsprojects.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![10 Languages](https://img.shields.io/badge/Languages-10-e63946)](https://github.com/kennedyraju55/code-translator)

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[Architecture](#-architecture) •
[API Reference](#-api-reference) •
[FAQ](#-faq)

</div>

---

## 📑 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Supported Languages](#-supported-languages)
- [CLI Reference](#-cli-reference)
  - [translate](#translate-command)
  - [batch](#batch-command)
  - [notes](#notes-command)
- [Web UI](#-web-ui)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Configuration](#️-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Modern development often requires translating code between languages — porting a Python prototype to Go for performance, converting JavaScript utilities to TypeScript for type safety, or migrating legacy PHP to modern alternatives.

**Cloud-based translation tools** send your proprietary code to external servers. That's a non-starter for many teams.

**Code Translator** solves this by running **entirely on your machine** using [Ollama](https://ollama.com) and local LLMs. Your code never leaves your computer.

### The Problem

| Challenge | Code Translator Solution |
|-----------|--------------------------|
| Code privacy concerns with cloud APIs | 🔒 100% local — code never leaves your machine |
| Manual translation is slow and error-prone | 🤖 LLM-powered automatic translation |
| No validation of translated output | ✅ Built-in syntax validation |
| Hard to compare source vs translated | 📊 Side-by-side comparison metrics |
| One file at a time is tedious | 📦 Batch translation for entire directories |
| Language differences are confusing | 📝 Auto-generated translation notes |

---

## ✨ Features

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg">
  <img alt="Features Overview" src="docs/images/features.svg" width="800">
</picture>

</div>

<br/>

| Feature | Description |
|---------|-------------|
| 🌐 **10 Language Support** | Python, JavaScript, TypeScript, Java, Go, Rust, C#, C++, Ruby, PHP |
| ✅ **Syntax Validation** | Automatic bracket, quote, and keyword validation on translated output |
| 📊 **Comparison Metrics** | Line count, character count, and size ratio between source and target |
| 📦 **Batch Translation** | Translate multiple files at once with organized output directories |
| 📝 **Translation Notes** | Detailed notes on syntax, type system, and pattern differences |
| 🔍 **Auto-Detection** | Automatically detect source language from file extension |
| 🌐 **Web UI** | Beautiful Streamlit interface with split-pane editor |
| 🖥️ **Rich CLI** | Syntax-highlighted terminal output with Click + Rich |
| 🔒 **100% Local** | No API keys, no cloud — runs entirely on your machine |
| ⚙️ **Configurable** | YAML-based configuration for model, temperature, and more |

---

## 🚀 Quick Start

### Prerequisites

1. **Python 3.10+** installed
2. **Ollama** installed and running ([download](https://ollama.com/download))
3. **Gemma 3 1B** model pulled:

```bash
ollama pull gemma3:1b
```

### Translate Your First File

**1. Install Code Translator:**

```bash
git clone https://github.com/kennedyraju55/code-translator.git
cd code-translator
pip install -r requirements.txt
pip install -e .
```

**2. Create a sample Python file:**

```python
# hello.py
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to Code Translator."

def fibonacci(n: int) -> list[int]:
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

if __name__ == "__main__":
    print(greet("World"))
    print(fibonacci(10))
```

**3. Translate Python → JavaScript:**

```bash
code-translate translate --file hello.py --target javascript --output hello.js
```

**Expected output:**

```
╭──────────────────────────────────────────────╮
│           🔄 Code Translator                 │
╰──────────────────────────────────────────────╯

📄 Source: hello.py (python)
🎯 Target: javascript

✅ Translation complete!

📊 Comparison:
  Source: 16 lines, 412 chars
  Target: 18 lines, 486 chars
  Ratio:  1.18x

💾 Saved to: hello.js
```

**Translated JavaScript:**

```javascript
function greet(name) {
    return `Hello, ${name}! Welcome to Code Translator.`;
}

function fibonacci(n) {
    if (n <= 0) return [];
    if (n === 1) return [0];

    const fib = [0, 1];
    for (let i = 2; i < n; i++) {
        fib.push(fib[i - 1] + fib[i - 2]);
    }
    return fib;
}

console.log(greet("World"));
console.log(fibonacci(10));
```

---

## 📥 Installation

### Standard Installation

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/code-translator.git
cd code-translator

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### Development Installation

```bash
# Install with dev dependencies (pytest, coverage)
pip install -e ".[dev]"
```

### Verify Installation

```bash
# Check CLI is available
code-translate --help

# Check Ollama is running
curl http://localhost:11434/api/tags
```

---

## 🌐 Supported Languages

Code Translator supports **10 programming languages** with automatic detection from file extensions:

| Language | Extension | Identifier | Example Use Case |
|----------|-----------|------------|------------------|
| 🐍 Python | `.py` | `python` | Prototyping, data science, scripting |
| 🟨 JavaScript | `.js` | `javascript` | Web frontend, Node.js backends |
| 🔷 TypeScript | `.ts` | `typescript` | Type-safe JavaScript applications |
| ☕ Java | `.java` | `java` | Enterprise applications, Android |
| 🐹 Go | `.go` | `go` | Cloud services, CLI tools |
| 🦀 Rust | `.rs` | `rust` | Systems programming, performance |
| 🟣 C# | `.cs` | `csharp` | .NET applications, Unity games |
| ⚡ C++ | `.cpp` | `cpp` | Systems, game engines, embedded |
| 💎 Ruby | `.rb` | `ruby` | Web apps (Rails), scripting |
| 🐘 PHP | `.php` | `php` | Web backends, CMS platforms |

> **Tip:** When using the CLI, pass the language identifier (e.g., `--target rust`) not the display name.

---

## 📖 CLI Reference

Code Translator provides three CLI commands through the `code-translate` entry point.

### Global Options

| Option | Short | Description |
|--------|-------|-------------|
| `--verbose` | `-v` | Enable verbose/debug logging |
| `--config` | | Path to config file (default: `config.yaml`) |
| `--help` | | Show help message |

---

### `translate` Command

Translate a single source file to a target language.

```bash
code-translate translate [OPTIONS]
```

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--file` | `-f` | ✅ | Path to the source code file |
| `--target` | `-t` | ✅ | Target programming language |
| `--source-lang` | `-s` | ❌ | Source language (auto-detected from extension if omitted) |
| `--output` | `-o` | ❌ | Output file path (prints to console if omitted) |

**Examples:**

```bash
# Basic translation (auto-detect source language)
code-translate translate -f app.py -t javascript

# Specify source language explicitly
code-translate translate -f utils.py -t go -s python

# Save output to a file
code-translate translate -f server.js -t typescript -o server.ts

# With verbose logging
code-translate -v translate -f main.go -t rust -o main.rs
```

---

### `batch` Command

Translate multiple files to a target language at once.

```bash
code-translate batch [OPTIONS]
```

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--files` | `-f` | ✅ | Source files (can specify multiple times) |
| `--target` | `-t` | ✅ | Target programming language |
| `--output-dir` | `-o` | ❌ | Output directory (default: `translations`) |

**Examples:**

```bash
# Translate multiple Python files to JavaScript
code-translate batch -f app.py -f utils.py -f models.py -t javascript

# Custom output directory
code-translate batch -f src/main.go -f src/utils.go -t rust -o rust_output

# Translate an entire directory (with shell expansion)
code-translate batch -f *.py -t typescript -o ts_output
```

**Output structure:**

```
translations/
├── app.js
├── utils.js
└── models.js
```

---

### `notes` Command

Generate translation notes comparing two languages.

```bash
code-translate notes [OPTIONS]
```

| Option | Short | Required | Description |
|--------|-------|----------|-------------|
| `--source` | `-s` | ✅ | Source programming language |
| `--target` | `-t` | ✅ | Target programming language |

**Examples:**

```bash
# Get notes for Python → Rust translation
code-translate notes -s python -t rust

# Compare JavaScript and TypeScript differences
code-translate notes -s javascript -t typescript

# Understand Go → Java translation considerations
code-translate notes -s go -t java
```

**Sample output:**

```
╭──────────────────────────────────────────────╮
│       📝 Translation Notes                   │
│       Python → Rust                          │
╰──────────────────────────────────────────────╯

Key Differences:
• Type System: Python is dynamically typed; Rust uses strict static typing
• Memory: Python uses garbage collection; Rust uses ownership/borrowing
• Error Handling: Python uses exceptions; Rust uses Result<T, E>
• Concurrency: Python has GIL limitations; Rust has fearless concurrency
• Syntax: Python uses indentation; Rust uses braces and semicolons
```

---

## 🌐 Web UI

Code Translator includes a **Streamlit-based web interface** for interactive code translation.

### Launch the Web UI

```bash
# Using Make
make run-web

# Or directly with Streamlit
streamlit run src/code_translator/web_ui.py
```

### Web UI Features

| Feature | Description |
|---------|-------------|
| **Split-Pane Editor** | Side-by-side source and translated code panels |
| **Language Selectors** | Dropdown menus for source and target languages |
| **File Upload** | Upload source files directly with drag-and-drop |
| **Auto-Detection** | Detects language from uploaded filename |
| **Translation Metrics** | Source lines, target lines, and line ratio |
| **Syntax Validation** | Shows syntax issues in the translated output |
| **Translation Notes** | Expandable section with language comparison notes |
| **Code Input** | Paste code directly or upload files |

### Web UI Workflow

1. **Select** source and target languages from the dropdowns
2. **Paste** code into the source panel or **upload** a file
3. Click **Translate** to run the translation
4. **Review** translated code, metrics, and validation results
5. Optionally **generate translation notes** for deeper insights

---

## 🏗 Architecture

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg">
  <img alt="Architecture Overview" src="docs/images/architecture.svg" width="800">
</picture>

</div>

<br/>

### Translation Pipeline

```
Source File → Language Detector → Code Reader → Prompt Builder → Ollama LLM
                                                                      │
Output/Export ← Comparison Metrics ← Syntax Validator ← Translated Code
```

### Project Structure

```
code-translator/
├── src/
│   ├── __init__.py
│   └── code_translator/
│       ├── __init__.py          # Package metadata (v1.0.0)
│       ├── core.py              # Core translation logic (219 lines)
│       ├── cli.py               # Click CLI interface (170 lines)
│       └── web_ui.py            # Streamlit web UI (107 lines)
├── common/
│   └── llm_client.py            # Shared Ollama client utilities
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core function tests (141 lines)
│   └── test_cli.py              # CLI command tests (48 lines)
├── docs/
│   └── images/                  # SVG assets for README
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml                  # Default configuration
├── .env.example                 # Environment variable template
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup with entry points
└── Makefile                     # Common development commands
```

### Component Overview

| Component | File | Responsibility |
|-----------|------|----------------|
| **Core Engine** | `core.py` | Language detection, translation, validation, comparison |
| **CLI Interface** | `cli.py` | Click-based commands with Rich formatting |
| **Web Interface** | `web_ui.py` | Streamlit app with split-pane editor |
| **LLM Client** | `common/llm_client.py` | Ollama HTTP API wrapper (chat, generate, embed) |
| **Configuration** | `config.yaml` | Model, temperature, limits, output settings |

---

## 📚 API Reference

### Core Functions (`code_translator.core`)

#### `detect_source_language(filepath: str) -> str`

Detect the programming language from a file's extension.

```python
from code_translator.core import detect_source_language

lang = detect_source_language("app.py")       # Returns "python"
lang = detect_source_language("server.ts")    # Returns "typescript"
lang = detect_source_language("main.rs")      # Returns "rust"
```

#### `get_language_name(lang: str) -> str`

Get the display name for a language identifier.

```python
from code_translator.core import get_language_name

name = get_language_name("csharp")  # Returns "C#"
name = get_language_name("cpp")     # Returns "C++"
```

#### `get_language_ext(lang: str) -> str`

Get the file extension for a language identifier.

```python
from code_translator.core import get_language_ext

ext = get_language_ext("python")      # Returns ".py"
ext = get_language_ext("javascript")  # Returns ".js"
```

#### `read_source_file(filepath: str) -> str`

Read and return the contents of a source file.

```python
from code_translator.core import read_source_file

code = read_source_file("app.py")
```

#### `translate_code(code, source_lang, target_lang, chat_fn, config=None) -> str`

Translate code from one language to another using the LLM.

```python
from code_translator.core import translate_code
from common.llm_client import chat

translated = translate_code(
    code="def add(a, b): return a + b",
    source_lang="python",
    target_lang="javascript",
    chat_fn=chat,
    config={"model": "gemma3:1b", "temperature": 0.3}
)
```

#### `validate_syntax(code: str, language: str) -> dict`

Perform basic syntax validation on translated code.

```python
from code_translator.core import validate_syntax

result = validate_syntax("function add(a, b) { return a + b; }", "javascript")
# Returns: {"valid": True, "issues": []}

result = validate_syntax("function add(a, b { return a + b; }", "javascript")
# Returns: {"valid": False, "issues": ["Mismatched brackets"]}
```

#### `compare_codes(source: str, translated: str) -> dict`

Compare source and translated code with metrics.

```python
from code_translator.core import compare_codes

metrics = compare_codes(source_code, translated_code)
# Returns: {
#     "source_lines": 16,
#     "target_lines": 18,
#     "source_chars": 412,
#     "target_chars": 486,
#     "line_ratio": 1.125,
#     "char_ratio": 1.18
# }
```

#### `batch_translate_files(file_paths, target_lang, chat_fn, output_dir="translations", config=None) -> list[dict]`

Translate multiple files in batch mode.

```python
from code_translator.core import batch_translate_files
from common.llm_client import chat

results = batch_translate_files(
    file_paths=["app.py", "utils.py", "models.py"],
    target_lang="javascript",
    chat_fn=chat,
    output_dir="js_output"
)
# Returns list of dicts with translation results per file
```

#### `generate_translation_notes(source_lang: str, target_lang: str, chat_fn) -> str`

Generate detailed translation notes comparing two languages.

```python
from code_translator.core import generate_translation_notes
from common.llm_client import chat

notes = generate_translation_notes("python", "rust", chat)
print(notes)
```

### LLM Client (`common.llm_client`)

| Function | Description |
|----------|-------------|
| `check_ollama_running() -> bool` | Check if Ollama server is accessible |
| `list_models() -> list` | List available Ollama models |
| `chat(messages, model, ...) -> str` | Send chat messages to LLM |
| `chat_stream(messages, ...) -> Generator` | Stream chat responses |
| `generate(prompt, model, ...) -> str` | Generate text from a prompt |
| `embed(text, model) -> list[float]` | Generate text embeddings |

---

## ⚙️ Configuration

### Config File (`config.yaml`)

```yaml
# Ollama server URL
ollama_base_url: "http://localhost:11434"

# LLM model to use for translation
model: "gemma3:1b"

# Temperature for LLM generation (0.0 = deterministic, 1.0 = creative)
temperature: 0.3

# Maximum characters of source code to send to LLM
max_code_chars: 5000

# Default output directory for batch translations
batch_output_dir: "translations"
```

### Environment Variables (`.env.example`)

```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
TEMPERATURE=0.3
MAX_CODE_CHARS=5000
BATCH_OUTPUT_DIR=translations
```

### Configuration Options

| Option | Default | Description |
|--------|---------|-------------|
| `ollama_base_url` | `http://localhost:11434` | Ollama server endpoint |
| `model` | `gemma3:1b` | LLM model for translation |
| `temperature` | `0.3` | Generation temperature (lower = more deterministic) |
| `max_code_chars` | `5000` | Max source code characters sent to LLM |
| `batch_output_dir` | `translations` | Default batch output directory |

> **Tip:** Use a lower temperature (0.1–0.3) for code translation to get more consistent, deterministic results.

---

## 🧪 Testing

### Run All Tests

```bash
# Using Make
make test

# Using pytest directly
pytest tests/ -v
```

### Run with Coverage

```bash
# Using Make
make test-cov

# Using pytest directly
pytest tests/ --cov=code_translator --cov-report=term-missing -v
```

### Test Structure

| Test File | Tests | Description |
|-----------|-------|-------------|
| `test_core.py` | 21 | Language detection, helpers, file reading, translation, validation, comparison, batch, config |
| `test_cli.py` | 4 | CLI translate, batch, notes commands, help output |

### Run Specific Tests

```bash
# Run only core tests
pytest tests/test_core.py -v

# Run only CLI tests
pytest tests/test_cli.py -v

# Run a specific test class
pytest tests/test_core.py::TestValidateSyntax -v

# Run a single test
pytest tests/test_core.py::TestDetectSourceLanguage::test_python_detection -v
```

### Linting

```bash
# Check syntax with py_compile
make lint
```

---

## 🔒 Local vs Cloud

| Feature | Code Translator (Local) | Cloud APIs (GPT, Claude, etc.) |
|---------|------------------------|-------------------------------|
| **Privacy** | ✅ Code never leaves your machine | ❌ Code sent to external servers |
| **Cost** | ✅ Free (after hardware) | ❌ Per-token pricing adds up |
| **Internet** | ✅ Works fully offline | ❌ Requires internet connection |
| **Speed** | ⚡ Depends on local hardware | ⚡ Generally fast (network latency) |
| **Quality** | 🟡 Good for most translations | 🟢 Often higher quality |
| **Models** | Ollama ecosystem (Gemma, Llama, etc.) | GPT-4, Claude, Gemini, etc. |
| **Setup** | Install Ollama + pull model | Get API key + configure |
| **Data Control** | ✅ Full control | ❌ Subject to provider policies |

> **Bottom line:** Use Code Translator when code privacy matters more than marginal quality improvements.

---

## ❓ FAQ

<details>
<summary><strong>1. Which LLM model works best for code translation?</strong></summary>

The default `gemma3:1b` works well for simple translations. For more complex code, try larger models:

```bash
# Pull a larger model
ollama pull gemma3:4b

# Update config.yaml
model: "gemma3:4b"
```

Larger models produce higher quality translations but require more RAM and are slower.

</details>

<details>
<summary><strong>2. Can I translate between any two supported languages?</strong></summary>

Yes! Code Translator supports translation between **any combination** of the 10 supported languages. That's 90 possible translation pairs (10 × 9).

```bash
# Python → Rust
code-translate translate -f app.py -t rust

# Go → Java
code-translate translate -f main.go -t java

# Ruby → TypeScript
code-translate translate -f app.rb -t typescript
```

</details>

<details>
<summary><strong>3. What happens if the translated code has syntax errors?</strong></summary>

Code Translator runs automatic syntax validation on every translation. If issues are detected, they're displayed in the output:

- **Mismatched brackets** (parentheses, braces, square brackets)
- **Unclosed strings** (quotes)
- **Missing language keywords** (e.g., `func` in Go, `fn` in Rust)

The validation is basic — always review and test translated code before using it in production.

</details>

<details>
<summary><strong>4. How do I handle large files?</strong></summary>

By default, Code Translator truncates source code to **5000 characters** to stay within LLM context limits. You can increase this in `config.yaml`:

```yaml
max_code_chars: 10000
```

For very large files, consider splitting them into smaller modules before translating.

</details>

<details>
<summary><strong>5. Is Ollama required, or can I use other LLM providers?</strong></summary>

Currently, Code Translator is designed for **Ollama** as the LLM backend. The `common/llm_client.py` module handles all Ollama communication. To use a different provider, you would need to modify the `chat_fn` interface in the core module.

Make sure Ollama is running before using Code Translator:

```bash
# Start Ollama (if not running as a service)
ollama serve

# Verify it's running
curl http://localhost:11434/api/tags
```

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/code-translator.git
cd code-translator

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify setup
make test
```

### Making Changes

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Make** your changes
4. **Run** tests (`make test`)
5. **Lint** your code (`make lint`)
6. **Commit** your changes (`git commit -m 'Add amazing feature'`)
7. **Push** to the branch (`git push origin feature/amazing-feature`)
8. **Open** a Pull Request

### Code Style

- Follow **PEP 8** for Python code
- Use **type hints** for function signatures
- Add **docstrings** to public functions
- Write **tests** for new features

### Areas for Contribution

- 🌐 Add support for more languages
- 🧪 Improve syntax validation rules
- 📊 Add more comparison metrics
- 🎨 Enhance the Web UI
- 📖 Improve documentation
- 🐛 Fix bugs and edge cases

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### 🔄 Code Translator

**Translate code between languages — locally, privately, and freely.**

Built with ❤️ using [Python](https://python.org) • [Ollama](https://ollama.com) • [Streamlit](https://streamlit.io) • [Click](https://click.palletsprojects.com) • [Rich](https://rich.readthedocs.io)

[⬆ Back to Top](#-code-translator)

</div>
