<!-- ═══════════════════════════════════════════════════════════════════════
     API Doc Generator — README
     Auto-Generate API Documentation from Python Source Code
     ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

<!-- Banner -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg"/>
  <img src="docs/images/banner.svg" alt="API Doc Generator — Auto-Generate API Documentation from Python Source Code" width="720"/>
</picture>

<br/><br/>

<!-- Badges -->
<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"/>
<img src="https://img.shields.io/badge/Ollama-Local_LLM-7209b7?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"/>
<img src="https://img.shields.io/badge/Gemma_4-Default_Model-ff6f00?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"/>
<img src="https://img.shields.io/badge/OpenAPI-3.0-6BA539?style=flat-square&logo=openapiinitiative&logoColor=white" alt="OpenAPI 3.0"/>
<img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/><br/>

**Point it at your Python code → get professional API docs in seconds.**<br/>
100 % local · AST-powered extraction · Markdown + OpenAPI output

<br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API Reference](#-api-reference) · [FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Writing API documentation is tedious.
Keeping it in sync with code is even worse.

**API Doc Generator** solves both problems:

1. **Parse** — the tool reads your Python files with the `ast` module, so it never
   misses a function, class, decorator, or type hint.
2. **Generate** — the extracted structure is sent to a **local** LLM (Ollama) that
   writes rich, human-readable documentation.
3. **Export** — output lands as Markdown (for GitHub/docs sites) or OpenAPI 3.0
   YAML (for Swagger UI, Redoc, Postman, …).

Everything runs **on your machine** — no API keys, no cloud, no data leakage.

<br/>

---

<br/>

## ✨ Features

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg"/>
  <img src="docs/images/features.svg" alt="Key Features" width="720"/>
</picture>
</div>

<br/>

| Feature | Description |
|:--------|:------------|
| 🌳 **AST-Powered Parsing** | Uses Python's `ast` module — no regex, no guessing. Extracts functions, classes, arguments, return types, decorators, docstrings, and async markers. |
| 📋 **OpenAPI 3.0 Generation** | Automatically builds an OpenAPI 3.0 skeleton from your code structure, then enhances it with the LLM. |
| 📝 **Markdown Documentation** | Produces rich Markdown with parameter tables, return types, examples, and cross-references. |
| 🔍 **Structure Inspection** | Inspect your codebase structure in a clean Rich table — no LLM call required. |
| 📁 **File & Directory Support** | Pass a single `.py` file or an entire directory; the tool finds and processes all Python files recursively. |
| 💾 **Flexible Export** | Export to `.md` or `.yaml` with customizable output paths. |
| 🖥️ **Streamlit Web UI** | Upload files or point at a local directory — preview and download docs from your browser. |
| ⚡ **Async Detection** | Correctly identifies `async def` functions and marks them in the output. |
| 🎨 **Decorator Support** | Captures all decorators (e.g. `@app.route`, `@staticmethod`) and includes them in the docs. |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Why |
|:------------|:--------|:----|
| Python | 3.10+ | Language runtime |
| Ollama | latest | Local LLM inference |
| Gemma 4 | (pulled via Ollama) | Default doc-generation model |

### 1 — Install Ollama & pull a model

```bash
# Install Ollama — https://ollama.com/download
curl -fsSL https://ollama.com/install.sh | sh

# Pull the default model
ollama pull gemma4
```

### 2 — Clone & install the project

```bash
git clone https://github.com/kennedyraju55/api-doc-generator.git
cd api-doc-generator

# Install in editable mode
pip install -e .

# — or —
pip install -r requirements.txt
```

### 3 — Generate docs 🎉

Suppose you have a file called `example.py`:

```python
# example.py
from typing import Optional

def fetch_users(limit: int = 10, offset: int = 0) -> list[dict]:
    """Fetch users from the database.

    Args:
        limit:  Maximum number of users to return.
        offset: Number of users to skip.

    Returns:
        A list of user dictionaries.
    """
    ...

class UserService:
    """Service layer for user operations."""

    def create_user(self, name: str, email: str, role: Optional[str] = None) -> dict:
        """Create a new user and return the created record."""
        ...

    async def delete_user(self, user_id: int) -> bool:
        """Soft-delete a user by ID."""
        ...
```

Run the generator:

```bash
# Generate Markdown docs
api-doc-gen generate --source example.py

# Save to a file
api-doc-gen generate --source example.py --output docs/api.md

# Generate OpenAPI YAML
api-doc-gen openapi --source example.py --output openapi.yaml

# Inspect structure (no LLM needed)
api-doc-gen inspect --source example.py
```

#### Example output — Markdown

````markdown
# API Documentation — `example.py`


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/api-doc-generator.git
cd api-doc-generator
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

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.api_doc_gen.api:app --reload --port 8000

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

## Functions

### `fetch_users`

Fetch users from the database.

| Parameter | Type  | Default | Description                        |
|:----------|:------|:--------|:-----------------------------------|
| `limit`   | `int` | `10`    | Maximum number of users to return. |
| `offset`  | `int` | `0`     | Number of users to skip.           |

**Returns** → `list[dict]` — A list of user dictionaries.

---

## Classes

### `UserService`

Service layer for user operations.

#### Methods

| Method        | Async | Parameters                      | Returns |
|:--------------|:------|:--------------------------------|:--------|
| `create_user` | No    | `name: str, email: str, role`   | `dict`  |
| `delete_user` | Yes   | `user_id: int`                  | `bool`  |
````

#### Example output — OpenAPI YAML

```yaml
openapi: "3.0.0"
info:
  title: "example API"
  version: "1.0.0"
paths:
  /fetch_users:
    get:
      summary: "Fetch users from the database."
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
          description: "Maximum number of users to return."
        - name: offset
          in: query
          schema:
            type: integer
          description: "Number of users to skip."
      responses:
        "200":
          description: "Successful response"
```

#### Example output — Inspect table

```
┌───────────────┬──────────┬──────┬───────────────────────────┬─────────────┐
│ Name          │ Type     │ Line │ Args                      │ Returns     │
├───────────────┼──────────┼──────┼───────────────────────────┼─────────────┤
│ fetch_users   │ function │ 4    │ limit: int, offset: int   │ list[dict]  │
│ UserService   │ class    │ 17   │ —                         │ —           │
│  create_user  │ method   │ 20   │ name: str, email: str, …  │ dict        │
│  delete_user  │ method   │ 24   │ user_id: int              │ bool        │
└───────────────┴──────────┴──────┴───────────────────────────┴─────────────┘
```

<br/>

---

<br/>

## 📖 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and exposes three
commands under the `api-doc-gen` entry point.

### Global options

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--config` | | `config.yaml` | Path to YAML configuration file |
| `--verbose` | `-v` | `false` | Enable debug logging |

### `generate` — Markdown documentation

```bash
api-doc-gen generate --source <path> [--output <file>]
```

| Option | Short | Required | Description |
|:-------|:------|:---------|:------------|
| `--source` | `-s` | ✅ | Path to a Python file or directory |
| `--output` | `-o` | ❌ | Save Markdown output to this file |

**Examples:**

```bash
# Single file → stdout
api-doc-gen generate -s src/api_doc_gen/core.py

# Directory → file
api-doc-gen generate -s src/ -o docs/api-reference.md

# With custom config + verbose
api-doc-gen --config my-config.yaml -v generate -s app.py
```

### `openapi` — OpenAPI 3.0 specification

```bash
api-doc-gen openapi --source <path> [--output <file>]
```

| Option | Short | Required | Description |
|:-------|:------|:---------|:------------|
| `--source` | `-s` | ✅ | Path to a Python file or directory |
| `--output` | `-o` | ❌ | Save YAML output to this file |

**Examples:**

```bash
# Generate and print to terminal
api-doc-gen openapi -s src/api_doc_gen/utils.py

# Save to file
api-doc-gen openapi -s src/ -o openapi.yaml
```

### `inspect` — Code structure inspection

```bash
api-doc-gen inspect --source <path>
```

| Option | Short | Required | Description |
|:-------|:------|:---------|:------------|
| `--source` | `-s` | ✅ | Path to a Python file or directory |

> 💡 **Tip:** `inspect` does **not** call the LLM — it only uses the AST parser,
> so it works instantly and without Ollama running.

**Examples:**

```bash
# Inspect a single file
api-doc-gen inspect -s src/api_doc_gen/core.py

# Inspect an entire package
api-doc-gen inspect -s src/
```

### Alternative invocation

If you haven't installed the package, you can run the CLI as a module:

```bash
python -m api_doc_gen.cli generate --source example.py
python -m api_doc_gen.cli openapi  --source example.py
python -m api_doc_gen.cli inspect  --source example.py
```

<br/>

---

<br/>

## 🖥️ Web UI

API Doc Generator ships with a **Streamlit** web interface for interactive use.

### Launch

```bash
streamlit run src/api_doc_gen/web_ui.py
```

The UI opens at **http://localhost:8501**.

### Capabilities

| Feature | Details |
|:--------|:--------|
| 📁 File upload | Upload one or more `.py` files directly from your browser |
| 📂 Directory path | Point at a local directory to scan recursively |
| ⚙️ Settings sidebar | Adjust model, temperature, max tokens, and toggle OpenAPI generation |
| 👁️ Live preview | View generated Markdown or YAML in-browser before downloading |
| ⬇️ Download | Export as `.md` or `.yaml` with one click |

> The Web UI uses the same `generate_docs` and `generate_openapi` core functions
> as the CLI, so output is identical.

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg"/>
  <img src="docs/images/architecture.svg" alt="Architecture Overview" width="720"/>
</picture>
</div>

<br/>

### How it works

```
Python Source ──► AST Parser ──► Extractor ──► Formatter ──► Ollama LLM
                                                               │
                                              ┌────────────────┼────────────────┐
                                              ▼                ▼                ▼
                                        Markdown Docs    OpenAPI YAML    Inspect Table
```

1. **`find_python_files()`** discovers `.py` files (single file or recursive directory walk).
2. **`extract_functions()`** uses `ast.parse()` to build a list of functions, classes,
   arguments, return types, decorators, and docstrings.
3. **`format_extracted_info()`** converts the structured data into a text block the
   LLM can understand.
4. **Ollama LLM** (via `common/llm_client.py`) generates the final documentation
   using a carefully crafted system prompt.
5. **`export_docs()`** writes the output to the requested format.

### Project tree

```
25-api-doc-generator/
├── src/
│   └── api_doc_gen/
│       ├── __init__.py          # Package metadata (v1.0.0)
│       ├── core.py              # generate_docs · generate_openapi · export_docs
│       ├── cli.py               # Click CLI — generate / openapi / inspect
│       ├── config.py            # DocGenConfig dataclass + loader
│       ├── utils.py             # AST extraction + OpenAPI skeleton builder
│       └── web_ui.py            # Streamlit interface
├── common/
│   └── llm_client.py            # Shared Ollama HTTP client
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # 19 unit tests
│   └── test_cli.py              # 4 CLI tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # Data-flow diagram
│       └── features.svg         # Feature cards
├── config.yaml                  # Default configuration
├── requirements.txt             # Runtime + dev dependencies
├── setup.py                     # Package definition (pip install -e .)
├── Makefile                     # Dev shortcuts
├── .env.example                 # Environment variable template
└── README.md                    # ← You are here
```

<br/>

---

<br/>

## 📚 API Reference

### `api_doc_gen.core`

#### `generate_docs(source_path, config)`

Generate Markdown API documentation from Python source files.

```python
from api_doc_gen.core import generate_docs
from api_doc_gen.config import DocGenConfig

config = DocGenConfig(model="gemma4", temperature=0.3, max_tokens=4096)
result = generate_docs("src/", config)

print(result["docs"])        # Markdown string
print(result["files"])       # List of processed files
print(result["items_count"]) # Number of extracted items
print(result["all_items"])   # Raw extracted data
```

**Parameters:**

| Name | Type | Description |
|:-----|:-----|:------------|
| `source_path` | `str` | Path to a `.py` file or directory |
| `config` | `DocGenConfig` | Configuration object |

**Returns:** `dict` with keys `docs`, `files`, `items_count`, `all_items`.

---

#### `generate_openapi(source_path, config)`

Generate an OpenAPI 3.0 specification from Python source files.

```python
from api_doc_gen.core import generate_openapi
from api_doc_gen.config import DocGenConfig

config = DocGenConfig(model="gemma4", temperature=0.2)
result = generate_openapi("src/api_doc_gen/utils.py", config)

print(result["openapi_yaml"])  # YAML string
print(result["skeleton"])      # Raw OpenAPI dict before LLM enhancement
```

**Parameters:**

| Name | Type | Description |
|:-----|:-----|:------------|
| `source_path` | `str` | Path to a `.py` file or directory |
| `config` | `DocGenConfig` | Configuration object |

**Returns:** `dict` with keys `openapi_yaml`, `skeleton`.

---

#### `export_docs(content, output_path, fmt)`

Write generated documentation to a file.

```python
from api_doc_gen.core import export_docs

path = export_docs(markdown_string, "docs/api.md", "markdown")
path = export_docs(yaml_string, "openapi.yaml", "yaml")
```

**Parameters:**

| Name | Type | Description |
|:-----|:-----|:------------|
| `content` | `str` | Documentation content to write |
| `output_path` | `str` | Destination file path |
| `fmt` | `str` | Output format — `"markdown"` or `"yaml"` |

**Returns:** `str` — the path to the exported file.

---

### `api_doc_gen.utils`

#### `find_python_files(source_path)`

Discover Python files at the given path.

```python
from api_doc_gen.utils import find_python_files

files = find_python_files("src/")
# ['src/api_doc_gen/__init__.py', 'src/api_doc_gen/core.py', ...]
```

---

#### `extract_functions(filepath)`

Parse a Python file and extract all functions, classes, and their metadata.

```python
from api_doc_gen.utils import extract_functions

items = extract_functions("example.py")
for item in items:
    print(item["type"], item["name"], item.get("args"))
```

**Returns:** `list[dict]` — each dict has keys:

| Key | Type | Present on |
|:----|:-----|:-----------|
| `type` | `str` | all — `"function"` or `"class"` |
| `name` | `str` | all |
| `lineno` | `int` | all |
| `docstring` | `str \| None` | all |
| `args` | `list[dict]` | functions |
| `returns` | `str \| None` | functions |
| `decorators` | `list[str]` | functions |
| `is_async` | `bool` | functions |
| `bases` | `list[str]` | classes |
| `methods` | `list[dict]` | classes |

---

#### `format_extracted_info(filepath, items)`

Convert extracted items into a human-readable text block for the LLM prompt.

```python
from api_doc_gen.utils import format_extracted_info, extract_functions

items = extract_functions("example.py")
text  = format_extracted_info("example.py", items)
```

---

#### `generate_openapi_skeleton(items, title)`

Build a minimal OpenAPI 3.0 dict from extracted items.

```python
from api_doc_gen.utils import generate_openapi_skeleton

skeleton = generate_openapi_skeleton(items, title="My API")
```

---

### `api_doc_gen.config`

#### `DocGenConfig`

Configuration dataclass.

```python
from dataclasses import dataclass

@dataclass
class DocGenConfig:
    ollama_base_url: str  = "http://localhost:11434"
    model: str            = "gemma4"
    temperature: float    = 0.3
    max_tokens: int       = 4096
    output_format: str    = "markdown"
    include_examples: bool = True
    include_openapi: bool  = False
    log_level: str        = "INFO"
```

#### `load_config(config_path)`

Load configuration from a YAML file, with environment variable overrides.

```python
from api_doc_gen.config import load_config

config = load_config("config.yaml")
```

Environment variables that override YAML values:

| Variable | Overrides |
|:---------|:----------|
| `OLLAMA_BASE_URL` | `ollama_base_url` |
| `OLLAMA_MODEL` | `model` |
| `LOG_LEVEL` | `log_level` |

<br/>

---

<br/>

## ⚙️ Configuration

### `config.yaml` (default)

```yaml
ollama_base_url: "http://localhost:11434"
model: "gemma4"
temperature: 0.3
max_tokens: 4096
output_format: "markdown"
include_examples: true
include_openapi: false
log_level: "INFO"
```

### Configuration options

| Key | Type | Default | Description |
|:----|:-----|:--------|:------------|
| `ollama_base_url` | `str` | `http://localhost:11434` | Base URL for the Ollama API |
| `model` | `str` | `gemma4` | LLM model name (any model available in Ollama) |
| `temperature` | `float` | `0.3` | Sampling temperature (lower = more deterministic) |
| `max_tokens` | `int` | `4096` | Maximum tokens in the LLM response |
| `output_format` | `str` | `markdown` | Default output format (`markdown` or `yaml`) |
| `include_examples` | `bool` | `true` | Include usage examples in generated docs |
| `include_openapi` | `bool` | `false` | Also generate OpenAPI spec with `generate` command |
| `log_level` | `str` | `INFO` | Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`) |

### Using a custom config

```bash
api-doc-gen --config my-config.yaml generate -s src/
```

### Environment variable overrides

```bash
export OLLAMA_BASE_URL=http://192.168.1.100:11434
export OLLAMA_MODEL=llama3
export LOG_LEVEL=DEBUG

api-doc-gen generate -s src/
```

<br/>

---

<br/>

## 🧪 Testing

The project uses **pytest** with **pytest-cov** for coverage.

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=api_doc_gen --cov-report=term-missing

# Run a specific test file
pytest tests/test_core.py

# Run tests in verbose mode
pytest -v
```

### Using `make`

```bash
make test        # Run pytest
make coverage    # Run with coverage
make lint        # Run linter
make clean       # Remove build artifacts
```

### Test summary

| File | Tests | Coverage |
|:-----|:------|:---------|
| `tests/test_core.py` | 19 | AST extraction, file discovery, formatting, OpenAPI skeleton, doc generation (mocked), export, config |
| `tests/test_cli.py` | 4 | CLI invocation, file output, error handling, inspect command |

<br/>

---

<br/>

## 🏠 Local vs Cloud

| Aspect | API Doc Generator (Local) | Cloud-based alternatives |
|:-------|:--------------------------|:-------------------------|
| **Privacy** | ✅ Code never leaves your machine | ❌ Code uploaded to third-party servers |
| **Cost** | ✅ Free (after hardware) | 💰 Per-token / per-request pricing |
| **Latency** | ⚡ Low — local inference | 🌐 Network round-trip |
| **Offline** | ✅ Works without internet | ❌ Requires connectivity |
| **Customisation** | ✅ Swap any Ollama model | 🔒 Limited to provider's models |
| **Data control** | ✅ Full control | ⚠️ Governed by provider ToS |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>1. Which LLM models work?</strong></summary>

Any model available through Ollama works. The default is **Gemma 4**, but you can
switch to `llama3`, `mistral`, `codellama`, `deepseek-coder`, or any other model
by changing the `model` field in `config.yaml` or setting `OLLAMA_MODEL`.

</details>

<details>
<summary><strong>2. Do I need Ollama running for the <code>inspect</code> command?</strong></summary>

**No.** The `inspect` command uses only the AST parser — it never calls the LLM.
Ollama is only required for `generate` and `openapi`.

</details>

<details>
<summary><strong>3. Can I document an entire project at once?</strong></summary>

Yes. Pass a directory path to `--source` and the tool will recursively find and
process every `.py` file:

```bash
api-doc-gen generate -s my_project/ -o docs/full-api.md
```

</details>

<details>
<summary><strong>4. How does the tool handle syntax errors?</strong></summary>

If a file contains a syntax error, `extract_functions()` catches the `SyntaxError`
exception, logs a warning, and returns an empty list for that file. Other files in
the same run are unaffected.

</details>

<details>
<summary><strong>5. Can I use this in a CI/CD pipeline?</strong></summary>

Absolutely. As long as Ollama is accessible (e.g., running on the CI host or a
sidecar container), you can add a step like:

```yaml
- name: Generate API docs
  run: |
    api-doc-gen generate -s src/ -o docs/api.md
    git add docs/api.md
```

For the `inspect` command (no LLM required), you don't even need Ollama installed.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork and clone
git clone https://github.com/<your-username>/api-doc-generator.git
cd api-doc-generator

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows

# Install in dev mode
pip install -e ".[dev]"

# Run tests to make sure everything works
pytest -v

# Create a feature branch
git checkout -b feat/my-feature
```

### Guidelines

- Follow the existing code style.
- Add tests for new features.
- Update the README if your change affects usage.
- Keep commits focused and well-described.

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file
for details.

<br/>

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55) collection**

<br/>

Built with 💜 using Python, Ollama, and local LLMs

<br/>

<sub>
<a href="#top">↑ Back to top</a>
</sub>

</div>
