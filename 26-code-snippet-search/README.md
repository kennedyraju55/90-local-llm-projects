<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img alt="Code Snippet Search — AI-Powered Semantic Code Search with Local LLMs" src="docs/images/banner.svg" width="800">
</picture>

<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-06d6a0?style=for-the-badge&logo=llama&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-f0c929?style=for-the-badge)](../../LICENSE)
[![Click CLI](https://img.shields.io/badge/Click-CLI-4ecca3?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com/)
[![Tests](https://img.shields.io/badge/Tests-Passing-06d6a0?style=for-the-badge&logo=pytest&logoColor=white)](tests/)
[![Code style: black](https://img.shields.io/badge/Code_Style-Black-000000?style=for-the-badge)](https://github.com/psf/black)
[![Version](https://img.shields.io/badge/Version-1.0.0-06d6a0?style=for-the-badge)](setup.py)

<br/>

**Search your codebase using natural language queries powered by a local LLM.**
<br/>
No data leaves your machine. 100% private. 100% local.

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[FAQ](#-frequently-asked-questions)

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

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
- [Local vs Cloud](#-local-vs-cloud-comparison)
- [FAQ](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Modern codebases are massive. Finding the right snippet — the authentication handler, the database migration, the error boundary — often means jumping between `grep`, file trees, and IDE search. These tools find **exact matches**, but they can't understand **what code does**.

**Code Snippet Search** bridges this gap by combining:

- 🧠 **Local LLM understanding** — powered by Ollama, your queries are interpreted semantically
- 📊 **Relevance scoring** — keyword-based pre-ranking ensures the LLM sees the most relevant files first
- 💾 **Smart caching** — MD5 hashing means repeated searches are near-instant
- 🔒 **Complete privacy** — everything runs on your machine, no API keys, no cloud, no telemetry

> **Example:** Instead of `grep -r "jwt" .`, ask:
> *"Where is the authentication logic that validates user tokens?"*

The LLM understands context, variable names, function purposes, and code patterns — returning exactly what you need with file paths, line numbers, and explanations.

---

## ✨ Features

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg">
  <img alt="Key Features of Code Snippet Search" src="docs/images/features.svg" width="800">
</picture>

</div>

<br/>

| Feature | Description | Details |
|---------|-------------|---------|
| 🔍 **Semantic Search** | Search code using natural language queries | Powered by local Ollama LLM — understands intent, not just keywords |
| 📊 **Relevance Ranking** | Pre-LLM keyword scoring ranks files | Path matches score +3.0, content matches +0.5 each (capped at 5.0) |
| 💾 **Index Caching** | MD5 hash-based file caching | Skip re-reading unchanged files for faster repeated searches |
| 🔖 **Bookmarks** | Save and manage search results | JSON-based persistence — never lose a useful code snippet again |
| 🌐 **Multi-Language** | 24+ file types supported | Python, JS, TS, Java, Go, Rust, C/C++, Ruby, PHP, SQL, and more |
| 🖥️ **Rich CLI** | Beautiful terminal output | Tables, panels, syntax highlighting, progress spinners via Rich |
| 🌍 **Web UI** | Full Streamlit web interface | Interactive search, file browser, and bookmark management |
| ⚙️ **Configurable** | YAML + environment config | Control extensions, limits, model, temperature, and more |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Python](https://www.python.org/downloads/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai) | Latest | Local LLM inference |
| [Gemma 3 1B](https://ollama.ai/library/gemma3) | 1B+ | Default search model |

### Step 1: Install Ollama & Pull the Model

```bash
# Install Ollama (see https://ollama.ai for your platform)
# Then pull the default model:
ollama pull gemma3:1b

# Verify Ollama is running:
ollama list
```

### Step 2: Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/code-snippet-search.git
cd code-snippet-search

# Install dependencies
pip install -r requirements.txt

# Or install as an editable package with dev tools
pip install -e ".[dev]"
```

### Step 3: Configure

```bash
# Copy the environment template
cp .env.example .env

# (Optional) Edit config.yaml for advanced settings
```

### Step 4: Search!

```bash
# CLI search
python -m src.code_search.cli search --dir ./your-project --query "authentication logic"

# Or launch the Web UI
streamlit run src/code_search/web_ui.py
```

### Using Make Targets

```bash
make install        # Install dependencies
make dev            # Install in development mode
make run-cli ARGS="search --dir . --query 'test'"
make run-web        # Launch Streamlit UI
make test           # Run test suite
make test-cov       # Tests with coverage
make clean          # Clean build artifacts
make help           # Show all targets
```

---

## 🖥️ CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and [Rich](https://rich.readthedocs.io/) for a beautiful terminal experience.

### Global Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--verbose` | `-v` | `False` | Enable debug-level logging |
| `--config` | | `config.yaml` | Path to configuration file |

### `search` — Search a Directory

Search your codebase using a natural language query.

```bash
python -m src.code_search.cli search \
  --dir ./my-project \
  --query "database connection pooling" \
  --max-files 50 \
  --ext .py --ext .sql \
  --bookmark
```

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--dir` | `-d` | *(required)* | Directory to search |
| `--query` | `-q` | *(required)* | Natural language search query |
| `--max-files` | | `100` | Maximum number of files to index |
| `--ext` | | *(from config)* | File extensions to include (repeatable) |
| `--bookmark` | `-b` | `False` | Save this result as a bookmark |

**What happens:**

1. 📂 Scans the target directory for matching files
2. 📊 Ranks files by keyword relevance score
3. 🔗 Builds a context window from the top-ranked files
4. 🤖 Sends the context + query to the local LLM
5. 📋 Displays formatted results with file paths and explanations
6. 🔖 Optionally bookmarks the result

### `bookmarks` — View Saved Bookmarks

```bash
python -m src.code_search.cli bookmarks
```

Displays a Rich table with all saved bookmarks:

| Column | Description |
|--------|-------------|
| `#` | Bookmark index (use for removal) |
| `Query` | The original search query |
| `Directory` | Directory that was searched |
| `Preview` | First ~200 characters of the result |

### `remove-bookmark` — Delete a Bookmark

```bash
python -m src.code_search.cli remove-bookmark 0
```

| Argument | Description |
|----------|-------------|
| `INDEX` | Zero-based index of the bookmark to remove |

### Example Session

```bash
# Search for auth logic
$ python -m src.code_search.cli search --dir ./myapp --query "JWT token validation"

╭──────────────────────────────────────────────╮
│  🔎 Code Snippet Search                     │
│  Searching with natural language + LLM       │
╰──────────────────────────────────────────────╯

⠋ Indexing files...

Indexed 23 file(s)

┌───┬──────────────────────────┬──────────┬───────┐
│ # │ File                     │ Language │ Lines │
├───┼──────────────────────────┼──────────┼───────┤
│ 1 │ auth/jwt_handler.py      │ python   │ 87    │
│ 2 │ middleware/auth.py        │ python   │ 45    │
│ 3 │ utils/tokens.py           │ python   │ 32    │
│ …│ (20 more files)           │          │       │
└───┴──────────────────────────┴──────────┴───────┘

╭── 🎯 Search Results ─────────────────────────╮
│                                               │
│  ## auth/jwt_handler.py (Lines 15-42)         │
│  JWT token validation and refresh logic.      │
│  The `validate_token()` function checks       │
│  expiration, signature, and issuer claims.    │
│                                               │
│  ## middleware/auth.py (Lines 5-18)            │
│  Authentication middleware that intercepts     │
│  requests and validates the Bearer token.     │
│                                               │
╰───────────────────────────────────────────────╯

# Bookmark it for later
$ python -m src.code_search.cli search --dir ./myapp --query "JWT token validation" --bookmark
✅ Result bookmarked!

# View saved bookmarks
$ python -m src.code_search.cli bookmarks

┌───┬─────────────────────────┬──────────┬──────────────────────┐
│ # │ Query                   │ Dir      │ Preview              │
├───┼─────────────────────────┼──────────┼──────────────────────┤
│ 0 │ JWT token validation    │ ./myapp  │ auth/jwt_handler.py… │
└───┴─────────────────────────┴──────────┴──────────────────────┘

# Remove a bookmark
$ python -m src.code_search.cli remove-bookmark 0
✅ Removed bookmark #0
```

---

## 🌐 Web UI

The Streamlit-based web interface provides a browser-friendly search experience.

### Launch

```bash
# Start the web UI
streamlit run src/code_search/web_ui.py

# Or via Make
make run-web
```

Opens at **http://localhost:8501**

### Web UI Features

| Area | Feature | Description |
|------|---------|-------------|
| **Sidebar** | Directory Input | Set the target directory (defaults to `cwd`) |
| **Sidebar** | Max Files Slider | Adjust 10–500 files to index |
| **Sidebar** | Bookmarks Panel | View, re-run, or delete saved bookmarks |
| **Main** | Search Box | Enter natural language queries |
| **Main** | File Index | Expandable list of indexed files (first 30) |
| **Main** | Search Results | LLM-generated results in Markdown |
| **Main** | Code Preview | Syntax-highlighted top 5 matching files |
| **Main** | Bookmark Button | Save the current result |

### Ollama Health Check

The Web UI automatically checks if Ollama is running on startup. If not:

```
⚠️ Ollama is not running. Start it with: ollama serve
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

### Project Structure

```
26-code-snippet-search/
├── src/
│   ├── __init__.py                 # Source root
│   └── code_search/               # Main package
│       ├── __init__.py             # Package metadata (v1.0.0)
│       ├── core.py                 # 🧠 Business logic (275 lines)
│       │   ├── load_config()       #    YAML config loading
│       │   ├── scan_directory()    #    Filesystem traversal
│       │   ├── score_relevance()   #    Keyword scoring
│       │   ├── rank_files()        #    File ranking
│       │   ├── build_search_context()  # Context window builder
│       │   ├── search_code()       #    Main search orchestrator
│       │   ├── save_index_cache()  #    Cache persistence
│       │   ├── load_index_cache()  #    Cache loading
│       │   ├── load_bookmarks()    #    Bookmark loading
│       │   ├── save_bookmark()     #    Bookmark saving
│       │   └── remove_bookmark()   #    Bookmark removal
│       ├── cli.py                  # 🖥️  CLI interface (160 lines)
│       │   ├── cli()               #    Click group (--verbose, --config)
│       │   ├── search()            #    Search command
│       │   ├── bookmarks()         #    List bookmarks command
│       │   └── remove_bookmark_cmd() # Remove bookmark command
│       └── web_ui.py               # 🌍 Streamlit web UI (115 lines)
│           └── main()              #    Streamlit app entry
├── common/
│   └── llm_client.py               # 🤖 Ollama client (202 lines)
│       ├── check_ollama_running()  #    Health check
│       ├── list_models()           #    Available models
│       ├── chat()                  #    Chat completion
│       ├── chat_stream()           #    Streaming chat
│       ├── generate()              #    Text generation
│       └── embed()                 #    Embeddings
├── tests/
│   ├── __init__.py
│   ├── test_core.py                # ✅ Core logic tests (175 lines, 25 tests)
│   └── test_cli.py                 # ✅ CLI tests (37 lines, 4 tests)
├── config.yaml                     # ⚙️  Configuration (42 lines)
├── .env.example                    # 🔑 Environment template
├── setup.py                        # 📦 Package setup
├── requirements.txt                # 📋 Dependencies
├── Makefile                        # 🔧 Task automation
└── README.md                       # 📖 This file
```

### Search Pipeline

The search pipeline follows a clear data flow:

```
┌─────────────┐    ┌─────────────┐    ┌──────────────┐    ┌───────────────┐
│   Query +   │ -> │  Directory  │ -> │  Relevance   │ -> │   Context     │
│  Directory  │    │   Scanner   │    │   Scoring    │    │   Builder     │
└─────────────┘    └─────────────┘    └──────────────┘    └───────────────┘
                         │                                       │
                    ┌────▼────┐                            ┌─────▼─────┐
                    │  Index  │                            │  Ollama   │
                    │  Cache  │                            │    LLM    │
                    └─────────┘                            └─────┬─────┘
                                                                 │
                                                     ┌───────────▼───────────┐
                                                     │   Search Results +   │
                                                     │   Optional Bookmark  │
                                                     └──────────────────────┘
```

**1. Directory Scanning** — Walks the filesystem, reads files, computes MD5 hashes, detects language
**2. Relevance Scoring** — Pre-LLM keyword scoring: path match = +3.0, content match = +0.5 (capped at 5.0 per term)
**3. Context Building** — Concatenates top-ranked files into a context string (max 8000 chars by default)
**4. LLM Search** — Sends system prompt + context + query to Ollama for semantic analysis
**5. Results** — Returns file paths, line numbers, and natural language explanations

---

## 📚 API Reference

### Core Module (`src/code_search/core.py`)

#### Configuration

```python
load_config(config_path: str = "config.yaml") -> dict
```

Loads YAML configuration with sensible defaults. Merges user config over defaults.

**Returns:** Configuration dictionary with keys: `ollama_base_url`, `model`, `max_files`, `max_context_chars`, `temperature`, `cache_dir`, `bookmarks_file`, `extensions`, `ignore_dirs`

---

#### File Utilities

```python
get_file_hash(filepath: str) -> str
```

Computes MD5 hash of a file for cache invalidation.

```python
detect_language(filepath: str) -> str
```

Maps file extension to syntax highlighting language name. Returns `"text"` for unknown extensions.

**Supported mappings:** `.py` → `python`, `.js` → `javascript`, `.ts` → `typescript`, `.java` → `java`, `.go` → `go`, `.rs` → `rust`, `.cpp`/`.c`/`.h` → `c`, `.rb` → `ruby`, `.php` → `php`, `.sh` → `bash`, `.sql` → `sql`, `.yaml`/`.yml` → `yaml`, `.json` → `json`, `.html` → `html`, `.css` → `css`, and more.

---

#### Directory Scanning

```python
scan_directory(
    directory: str,
    extensions: Optional[set] = None,
    max_files: int = 100,
    ignore_dirs: Optional[set] = None,
) -> list[dict]
```

Walks the filesystem and returns file metadata.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `directory` | `str` | *(required)* | Root directory to scan |
| `extensions` | `set` | `DEFAULT_EXTENSIONS` | File extensions to include |
| `max_files` | `int` | `100` | Max files to return |
| `ignore_dirs` | `set` | `IGNORE_DIRS` | Directory names to skip |

**Returns:** List of file dictionaries:

```python
{
    "path": str,        # Relative path from scan root
    "full_path": str,   # Absolute path
    "content": str,     # Full file content
    "lines": int,       # Line count
    "language": str,    # Detected language ("python", "javascript", etc.)
    "size": int,        # File size in bytes
    "hash": str,        # MD5 hash of content
}
```

---

#### Relevance Scoring

```python
score_relevance(query: str, file_info: dict) -> float
```

Computes keyword-based relevance score for a file against a query.

**Scoring algorithm:**
- Query term found in file path: **+3.0**
- Query term found in content N times: **+min(N × 0.5, 5.0)**
- Total = sum of all term scores

```python
rank_files(files: list[dict], query: str) -> list[dict]
```

Sorts files by descending relevance score.

---

#### Search Context

```python
build_search_context(files: list[dict], max_chars: int = 8000) -> str
```

Builds the LLM prompt context from top-ranked files. Each file contributes up to 500 characters. Concatenation stops at `max_chars`.

**Context format per file:**
```
--- path/to/file.py (42 lines, python) ---
<first 500 chars of file content>
```

```python
search_code(
    directory: str,
    query: str,
    chat_fn: Callable,
    config: Optional[dict] = None,
) -> str
```

Main search orchestrator. Scans → Ranks → Builds Context → Queries LLM.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `directory` | `str` | Directory to search |
| `query` | `str` | Natural language query |
| `chat_fn` | `Callable` | LLM chat function `(messages, system_prompt, temperature) -> str` |
| `config` | `dict` | Optional config override |

**Returns:** LLM response string with file paths, line numbers, and explanations.

---

#### Caching

```python
save_index_cache(files: list[dict], cache_path: str) -> None
```

Saves file index metadata to JSON for faster subsequent searches.

**Cache format:**
```json
{
    "timestamp": 1700000000.0,
    "files": [
        {"path": "src/main.py", "hash": "abc123", "lines": 42, "language": "python"}
    ]
}
```

```python
load_index_cache(cache_path: str) -> Optional[dict]
```

Loads cached index. Returns `None` if cache doesn't exist.

---

#### Bookmarks

```python
load_bookmarks(bookmarks_file: str = "bookmarks.json") -> list[dict]
```

Loads all saved bookmarks from JSON file.

```python
save_bookmark(bookmark: dict, bookmarks_file: str = "bookmarks.json") -> None
```

Appends a new bookmark with auto-generated timestamp.

**Bookmark structure:**
```python
{
    "query": "authentication logic",
    "directory": "./myapp",
    "result_preview": "First 200 chars of result...",
    "timestamp": 1700000000.0,      # Auto-added
}
```

```python
remove_bookmark(index: int, bookmarks_file: str = "bookmarks.json") -> bool
```

Removes bookmark at the specified index. Returns `True` on success, `False` if index is invalid.

---

### LLM Client (`common/llm_client.py`)

```python
check_ollama_running() -> bool        # Health check (5s timeout)
list_models() -> list                  # Available Ollama models
chat(messages, model, system_prompt, temperature, max_tokens) -> str
chat_stream(messages, model, system_prompt, temperature, max_tokens) -> Generator[str]
generate(prompt, model, system_prompt, temperature, max_tokens) -> str
embed(text, model) -> list[float]      # Text embeddings
```

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# LLM Configuration
ollama_base_url: "http://localhost:11434"
model: "gemma3:1b"
temperature: 0.3

# Search Configuration
max_files: 100                    # Max files to index per search
max_context_chars: 8000           # Max chars sent to LLM
cache_dir: ".cache"               # Index cache directory
bookmarks_file: "bookmarks.json"  # Bookmarks storage

# Supported file extensions
extensions:
  - .py
  - .js
  - .ts
  - .jsx
  - .tsx
  - .java
  - .go
  - .rs
  - .cpp
  - .c
  - .h
  - .rb
  - .php
  - .sh
  - .sql
  - .yaml
  - .yml
  - .json
  - .html
  - .css

# Directories to ignore during scanning
ignore_dirs:
  - .git
  - __pycache__
  - node_modules
  - .venv
  - venv
  - dist
  - build
```

### `.env` Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama API endpoint |
| `OLLAMA_MODEL` | `gemma3:1b` | Model for search queries |
| `MAX_FILES` | `100` | Max files to index |
| `MAX_CONTEXT_CHARS` | `8000` | Max context window size |
| `TEMPERATURE` | `0.3` | LLM temperature (lower = more focused) |
| `CACHE_DIR` | `.cache` | Cache directory path |
| `BOOKMARKS_FILE` | `bookmarks.json` | Bookmarks file path |

### Configuration Priority

```
CLI flags  >  Environment variables  >  config.yaml  >  Built-in defaults
```

---

## 🧪 Testing

### Run All Tests

```bash
# Full test suite
python -m pytest tests/ -v

# With coverage report
python -m pytest tests/ -v --cov=src/code_search --cov-report=term-missing

# Via Make
make test
make test-cov
```

### Test Suite Overview

| Test Class | File | Tests | Description |
|------------|------|-------|-------------|
| `TestScanDirectory` | `test_core.py` | 7 | File scanning, filtering, limits |
| `TestBuildSearchContext` | `test_core.py` | 2 | Context building, char limits |
| `TestRelevanceScoring` | `test_core.py` | 3 | Keyword scoring algorithm |
| `TestRankFiles` | `test_core.py` | 1 | File ranking by relevance |
| `TestDetectLanguage` | `test_core.py` | 3 | Extension-to-language mapping |
| `TestSearchCode` | `test_core.py` | 2 | End-to-end search (mocked LLM) |
| `TestBookmarks` | `test_core.py` | 3 | Save, load, remove bookmarks |
| `TestIndexCache` | `test_core.py` | 2 | Cache persistence |
| `TestLoadConfig` | `test_core.py` | 1 | Config loading with defaults |
| `TestCLI` | `test_cli.py` | 4 | CLI commands and error handling |

**Total: 28 tests** across 10 test classes.

### Running Specific Tests

```bash
# Single test class
python -m pytest tests/test_core.py::TestScanDirectory -v

# Single test method
python -m pytest tests/test_core.py::TestScanDirectory::test_scans_python_files -v

# CLI tests only
python -m pytest tests/test_cli.py -v
```

---

## 🔒 Local vs Cloud Comparison

| Feature | Code Snippet Search | Cloud-Based Tools |
|---------|--------------------|--------------------|
| **Privacy** | ✅ 100% local — no data leaves your machine | ❌ Code sent to external servers |
| **Cost** | ✅ Free forever — runs on your hardware | ❌ API costs per query ($0.01–$0.10+) |
| **Speed** | ✅ No network latency for repeated searches | ❌ Depends on internet + API latency |
| **Offline** | ✅ Works completely offline | ❌ Requires internet connection |
| **Setup** | ⚠️ Requires Ollama + model download | ✅ Usually just an API key |
| **Accuracy** | ⚠️ Depends on local model quality | ✅ Large cloud models (GPT-4, etc.) |
| **Codebase Limit** | ⚠️ Context window limited (configurable) | ✅ Often supports larger contexts |
| **Customization** | ✅ Full control over model, config, prompts | ❌ Limited to provider options |

**Bottom line:** Use Code Snippet Search when privacy, cost, and offline capability matter. Use cloud tools when you need maximum accuracy on very large codebases.

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>1. Which Ollama models work best?</strong></summary>

The default model is **Gemma 3 1B** (`gemma3:1b`), which provides a good balance of speed and accuracy for code search. For better results on complex queries, try larger models:

```bash
ollama pull gemma3:4b      # Better accuracy, slower
ollama pull codellama:7b    # Code-specialized model
ollama pull llama3:8b       # General-purpose, good quality
```

Update `config.yaml` or set `OLLAMA_MODEL` in `.env` to switch models.

</details>

<details>
<summary><strong>2. How do I search only Python files?</strong></summary>

Use the `--ext` flag (repeatable):

```bash
python -m src.code_search.cli search --dir . --query "error handling" --ext .py

# Multiple extensions
python -m src.code_search.cli search --dir . --query "API routes" --ext .py --ext .js
```

Or set `extensions` in `config.yaml` to change the default.

</details>

<details>
<summary><strong>3. What if Ollama is not running?</strong></summary>

Start the Ollama service:

```bash
# macOS / Linux
ollama serve

# Windows (usually auto-starts)
# Check task manager or start from system tray
```

Both the CLI and Web UI will display a clear error message if Ollama is unreachable.

</details>

<details>
<summary><strong>4. How does caching work?</strong></summary>

When you search a directory, Code Snippet Search computes an **MD5 hash** for each file. This hash is stored in `.cache/` along with file metadata (path, language, line count).

On subsequent searches:
- Files with unchanged hashes are loaded from cache
- Modified files are re-read and re-hashed
- New files are added; deleted files are removed

This makes repeated searches significantly faster, especially for large codebases.

</details>

<details>
<summary><strong>5. Can I use this with remote repositories?</strong></summary>

Yes! Clone the repository locally first, then point Code Snippet Search at it:

```bash
git clone https://github.com/user/repo.git
python -m src.code_search.cli search --dir ./repo --query "authentication middleware"
```

Since everything runs locally, the repository contents never leave your machine.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and install in development mode
git clone https://github.com/kennedyraju55/code-snippet-search.git
cd code-snippet-search
pip install -e ".[dev]"

# Run tests to verify setup
make test
```

### Guidelines

1. **Fork** the repository and create a feature branch
2. **Write tests** for new functionality
3. **Run the test suite** before submitting: `make test`
4. **Follow existing code style** (Black formatting)
5. **Update documentation** if your changes affect the API or CLI
6. **Submit a Pull Request** with a clear description of changes

### Project Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `requests` | ≥2.31.0 | HTTP client for Ollama API |
| `rich` | ≥13.0.0 | CLI formatting (tables, panels, syntax highlighting) |
| `click` | ≥8.1.0 | CLI framework (commands, options, groups) |
| `pyyaml` | ≥6.0 | YAML config parsing |
| `streamlit` | ≥1.28.0 | Web UI framework |
| `pytest` | ≥7.4.0 | Testing framework *(dev)* |
| `pytest-cov` | ≥4.0.0 | Coverage reporting *(dev)* |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](../../LICENSE) file for details.

---

<div align="center">

<br/>

**Built with ❤️ as part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<br/>

<sub>
🔍 <strong>Code Snippet Search</strong> — AI-Powered Semantic Code Search with Local LLMs
<br/>
Made with Python • Ollama • Rich • Click • Streamlit
</sub>

<br/><br/>

[⬆ Back to Top](#)

</div>
