<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img src="docs/images/banner.svg" alt="SQL Query Generator — Natural Language to SQL Queries with Local LLMs" width="800">
</picture>

<br/>
<br/>

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-fb8500?style=flat-square)](../../LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-00C244?style=flat-square&logo=ollama&logoColor=white)](https://ollama.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000?style=flat-square)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-fb8500?style=flat-square)](https://github.com/kennedyraju55/sql-query-generator/pulls)

**Convert natural language questions into production-ready SQL queries — 100% locally.**
<br/>
No API keys. No cloud dependencies. No data leaves your machine.

<br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Reference](#-api-reference) · [FAQ](#-frequently-asked-questions)

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

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
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Local vs Cloud](#-local-vs-cloud)
- [Frequently Asked Questions](#-frequently-asked-questions)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Writing SQL by hand is tedious, error-prone, and requires memorizing dialect-specific syntax. Most AI-powered SQL tools send your **schema and data descriptions** to cloud APIs — exposing table structures, column names, and business logic to third parties.

**SQL Query Generator** solves both problems:

| Problem | Our Solution |
|---------|-------------|
| 🔒 **Privacy concerns** with cloud AI | Runs 100% locally via Ollama — nothing leaves your machine |
| 🧠 **Forgetting SQL syntax** across dialects | Supports PostgreSQL, MySQL, SQLite & standard SQL |
| 📐 **Understanding complex schemas** | Parses & visualizes schemas as ASCII art |
| 🐌 **Slow, unoptimized queries** | AI-powered optimization suggestions |
| 🔄 **Repeating the same queries** | JSON-based query history with instant recall |

> **Who is this for?** Backend developers, data engineers, DBAs, students, and anyone who writes SQL and values data privacy.

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

| Feature | Description | Details |
|---------|-------------|---------|
| 🗣️ **Natural Language → SQL** | Describe what you want in plain English | Uses an expert SQL developer system prompt with 6-step reasoning |
| 🗄️ **Multi-Dialect Support** | Generate dialect-specific SQL | `standard` · `postgresql` · `mysql` · `sqlite` |
| 📋 **Schema Parsing** | Auto-extract tables and columns from `.sql` files | Handles `CREATE TABLE` statements with all column types |
| 📊 **Schema Visualization** | ASCII art rendering of your database schema | Box-drawing characters for a clean terminal display |
| ⚡ **Query Optimization** | AI-powered performance analysis | Index suggestions, query restructuring, best practices |
| 📚 **Query History** | Track and review past generated queries | JSON persistence, max 100 entries, timestamp tracking |
| 🚀 **No-Schema Mode** | Generate SQL without providing a schema file | LLM infers table structures from your natural language description |
| 🌐 **Streamlit Web UI** | Full browser-based interface | Schema editor, syntax highlighting, one-click optimization |
| 🖥️ **Rich CLI** | Beautiful terminal output | Panels, syntax highlighting (Monokai), markdown rendering |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Install |
|-------------|---------|---------|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| Ollama | Latest | [ollama.ai](https://ollama.ai) |
| LLM Model | Any | `ollama pull gemma3:1b` |

### 1. Clone & Install

```bash
git clone https://github.com/kennedyraju55/sql-query-generator.git
cd sql-query-generator

# Install dependencies
pip install -r requirements.txt

# Or install as a package (development mode)
pip install -e ".[dev]"
```

### 2. Start Ollama

```bash
# Make sure Ollama is running
ollama serve

# Pull the default model
ollama pull gemma3:1b
```

### 3. Generate Your First Query

```bash
# With a schema file
python -m src.sql_gen.cli generate \
  --schema schema.sql \
  --query "show top 10 customers by total revenue"
```

**Example output:**

```
╭──────────────────────────────────────────╮
│  🗃️  SQL Query Generator               │
│  Convert natural language to SQL         │
╰──────────────────────────────────────────╯

Tables found: customers, orders, products

╭── 📝 Generated SQL ───────────────────────╮
│                                            │
│  SELECT c.name,                            │
│         c.email,                           │
│         SUM(o.amount) AS total_revenue     │
│  FROM customers c                          │
│  JOIN orders o ON c.id = o.customer_id     │
│  WHERE o.status = 'completed'              │
│  GROUP BY c.name, c.email                  │
│  ORDER BY total_revenue DESC               │
│  LIMIT 10;                                 │
│                                            │
╰────────────────────────────────────────────╯
```

### 4. Try Without a Schema

```bash
python -m src.sql_gen.cli generate \
  --query "find all employees hired in the last 6 months with salary above 50000"
```

**Example output:**

```sql
SELECT employee_id,
       first_name,
       last_name,
       hire_date,
       salary
FROM employees
WHERE hire_date >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
  AND salary > 50000
ORDER BY hire_date DESC;
```

### 5. Try Different Dialects

```bash
# PostgreSQL-specific syntax
python -m src.sql_gen.cli generate \
  --schema schema.sql \
  --query "monthly sales report for 2024" \
  --dialect postgresql

# MySQL-specific syntax
python -m src.sql_gen.cli generate \
  --schema schema.sql \
  --query "monthly sales report for 2024" \
  --dialect mysql

# SQLite-specific syntax
python -m src.sql_gen.cli generate \
  --schema schema.sql \
  --query "monthly sales report for 2024" \
  --dialect sqlite
```

---

## 🖥️ CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and outputs using [Rich](https://rich.readthedocs.io/).

### Global Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--verbose` | `-v` | `false` | Enable DEBUG-level logging |
| `--config` | | `config.yaml` | Path to configuration file |
| `--help` | | | Show help message and exit |

### `generate` — Convert Natural Language to SQL

```bash
python -m src.sql_gen.cli generate [OPTIONS]
```

| Option | Short | Type | Required | Description |
|--------|-------|------|----------|-------------|
| `--schema` | `-s` | `PATH` | No | Path to SQL schema file |
| `--schema-text` | | `TEXT` | No | Inline schema definition string |
| `--query` | `-q` | `TEXT` | **Yes** | Natural language question |
| `--dialect` | `-d` | `CHOICE` | No | SQL dialect: `standard`, `postgresql`, `mysql`, `sqlite` |

**Examples:**

```bash
# Basic usage with a schema file
python -m src.sql_gen.cli generate -s schema.sql -q "list all active users"

# Inline schema definition
python -m src.sql_gen.cli generate \
  --schema-text "CREATE TABLE users (id INT, name VARCHAR(100), active BOOL)" \
  --query "count active users"

# PostgreSQL dialect
python -m src.sql_gen.cli generate -s schema.sql -q "sales by month" -d postgresql

# No-schema mode
python -m src.sql_gen.cli generate -q "find duplicate email addresses in users table"
```

### `history` — View Query History

```bash
python -m src.sql_gen.cli history
```

Displays the last **20 queries** in a formatted Rich table with columns for timestamp, query text, dialect, and result preview.

### `clear-history` — Clear Query History

```bash
python -m src.sql_gen.cli clear-history
```

Removes all entries from the `query_history.json` file.

### Using the Installed Entry Point

If you installed the package with `pip install -e .`, you can use the `sql-gen` command directly:

```bash
sql-gen generate -s schema.sql -q "top customers by revenue"
sql-gen history
sql-gen clear-history
```

---

## 🌐 Web UI

Launch the Streamlit-based web interface:

```bash
streamlit run src/sql_gen/web_ui.py
```

### Web UI Layout

| Section | Location | Features |
|---------|----------|----------|
| **Dialect Selector** | Sidebar | Dropdown for `standard`, `postgresql`, `mysql`, `sqlite` |
| **Query History** | Sidebar | Last 10 queries with click-to-reload buttons |
| **Schema Editor** | Left column | Textarea for pasting `CREATE TABLE` statements |
| **Schema Preview** | Left column | Auto-detected tables and ASCII visualization |
| **Query Input** | Right column | Natural language textarea |
| **Generate Button** | Right column | `🚀 Generate SQL` — full width, primary style |
| **SQL Output** | Right column | Syntax-highlighted generated SQL |
| **Optimizer** | Right column | Expandable section with `💡 Optimization Suggestions` |

### Web UI Features

- 📊 **Interactive schema editor** — paste your `CREATE TABLE` statements and see tables auto-detected
- 📐 **Live schema visualization** — ASCII art rendering updates as you type
- 🎨 **Syntax-highlighted SQL** — generated queries with Markdown code blocks
- 📜 **Session history** — click any past query to reload it instantly
- 💡 **One-click optimization** — expand the optimizer panel and analyze any query
- ⚡ **Spinner feedback** — visual loading indicator during LLM generation
- 🛡️ **Error handling** — clear error messages when Ollama is not running

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

### Project Structure

```
27-sql-query-generator/
│
├── src/
│   ├── __init__.py
│   └── sql_gen/                    # Main package
│       ├── __init__.py             # Package metadata (v1.0.0)
│       ├── core.py                 # 🧠 Schema parsing, SQL generation, optimization
│       ├── cli.py                  # 🖥️  CLI interface (Rich + Click)
│       └── web_ui.py              # 🌐 Streamlit web interface
│
├── tests/
│   ├── __init__.py
│   ├── test_core.py               # Core module tests (14 tests)
│   └── test_cli.py                # CLI tests (5 tests)
│
├── common/
│   └── llm_client.py              # 🔌 Shared Ollama client utility
│
├── config.yaml                    # ⚙️  Configuration defaults
├── setup.py                       # 📦 Package setup & entry points
├── requirements.txt               # 📋 Dependencies
├── Makefile                       # 🔧 Task automation
├── .env.example                   # 🔑 Environment variable template
├── query_history.json             # 📚 Query history database
├── docs/
│   └── images/                    # 🎨 SVG documentation images
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
└── README.md                      # 📖 This file
```

### Data Flow

1. **Input** — User provides a natural language question and (optionally) a SQL schema file
2. **Schema Parser** — `parse_schema_text()` extracts table names and column definitions
3. **Table Extractor** — `get_table_names()` identifies all tables in the schema
4. **Schema Visualizer** — `visualize_schema()` generates an ASCII art representation
5. **Prompt Builder** — Combines the system prompt, schema context, dialect, and user question
6. **Ollama LLM** — Local model generates the SQL query with explanation
7. **SQL Output** — Generated query is displayed with Rich formatting
8. **Query Optimizer** — `optimize_query()` provides performance improvement suggestions
9. **History** — `save_to_history()` persists the query for future reference

### Module Responsibilities

| Module | Lines | Responsibility |
|--------|-------|---------------|
| `core.py` | ~270 | Schema parsing, SQL generation, optimization, history management |
| `cli.py` | ~144 | Click commands, Rich output formatting, Ollama health check |
| `web_ui.py` | ~110 | Streamlit layout, session state, interactive schema editor |
| `llm_client.py` | ~202 | Ollama API wrapper (chat, streaming, embeddings) |

---

## 📖 API Reference

### Schema Functions

#### `read_schema(schema_path: str) → str`

Read a SQL schema from a file on disk.

```python
from sql_gen.core import read_schema

schema = read_schema("database/schema.sql")
print(schema)
# CREATE TABLE customers (id INTEGER PRIMARY KEY, name VARCHAR(100), ...);
```

#### `parse_schema_text(schema_text: str) → list[dict]`

Parse raw SQL text and extract table structures.

```python
from sql_gen.core import parse_schema_text

schema_text = """
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    created_at TIMESTAMP
);
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    amount DECIMAL(10,2),
    status VARCHAR(50)
);
"""

tables = parse_schema_text(schema_text)
# [
#   {"name": "customers", "columns": ["id INTEGER PRIMARY KEY", "name VARCHAR(100)", ...]},
#   {"name": "orders", "columns": ["id INTEGER PRIMARY KEY", "customer_id INTEGER REFERENCES customers(id)", ...]}
# ]
```

#### `get_table_names(schema_text: str) → list[str]`

Extract only table names from a schema string.

```python
from sql_gen.core import get_table_names

names = get_table_names(schema_text)
# ["customers", "orders"]
```

#### `visualize_schema(tables: list[dict]) → str`

Generate an ASCII art visualization of the parsed schema.

```python
from sql_gen.core import parse_schema_text, visualize_schema

tables = parse_schema_text(schema_text)
print(visualize_schema(tables))
# ┌─────────────────────────────┐
# │ customers                   │
# ├─────────────────────────────┤
# │ id INTEGER PRIMARY KEY      │
# │ name VARCHAR(100)           │
# │ email VARCHAR(255)          │
# │ created_at TIMESTAMP        │
# └─────────────────────────────┘
```

### SQL Generation Functions

#### `generate_sql(schema, query, chat_fn, dialect="standard", config=None) → str`

Generate a SQL query from a natural language question using a schema for context.

```python
from sql_gen.core import generate_sql, load_config
from common.llm_client import chat

config = load_config()
schema = "CREATE TABLE users (id INT, name VARCHAR(100), email VARCHAR(255));"

result = generate_sql(
    schema=schema,
    query="find all users with gmail addresses",
    chat_fn=chat,
    dialect="postgresql",
    config=config
)
print(result)
# SELECT id, name, email
# FROM users
# WHERE email LIKE '%@gmail.com'
# ORDER BY name;
```

#### `generate_sql_no_schema(query, chat_fn, dialect="standard", config=None) → str`

Generate SQL without providing a schema — the LLM infers table structures.

```python
from sql_gen.core import generate_sql_no_schema
from common.llm_client import chat

result = generate_sql_no_schema(
    query="find all products cheaper than $20 sorted by price",
    chat_fn=chat,
    dialect="mysql"
)
```

#### `optimize_query(sql, chat_fn, dialect="standard") → str`

Get AI-powered optimization suggestions for a SQL query.

```python
from sql_gen.core import optimize_query
from common.llm_client import chat

sql = "SELECT * FROM orders WHERE customer_id IN (SELECT id FROM customers WHERE city = 'NYC')"
suggestions = optimize_query(sql, chat_fn, dialect="postgresql")
print(suggestions)
# 1. Replace SELECT * with specific columns
# 2. Consider using JOIN instead of subquery
# 3. Add index on customers.city
```

### History Functions

#### `load_history(history_file="query_history.json") → list[dict]`

Load the query history from disk.

```python
from sql_gen.core import load_history

history = load_history()
for entry in history[-5:]:
    print(f"[{entry['timestamp']}] {entry['query']} ({entry['dialect']})")
```

#### `save_to_history(entry, history_file, max_history=100) → None`

Save a query result to the history file.

```python
from sql_gen.core import save_to_history

save_to_history(
    entry={
        "query": "top customers by revenue",
        "dialect": "postgresql",
        "result_preview": "SELECT c.name, SUM(o.amount)...",
        "timestamp": 1700000000.0
    },
    history_file="query_history.json",
    max_history=100
)
```

#### `clear_history(history_file="query_history.json") → None`

Remove all entries from the history file.

```python
from sql_gen.core import clear_history

clear_history()
```

### Configuration

#### `load_config(config_path="config.yaml") → dict`

Load configuration from a YAML file with sensible defaults.

```python
from sql_gen.core import load_config

config = load_config("config.yaml")
# {
#     "ollama_base_url": "http://localhost:11434",
#     "model": "gemma3:1b",
#     "temperature": 0.3,
#     "default_dialect": "standard",
#     "history_file": "query_history.json",
#     "max_history": 100,
#     "max_schema_chars": 4000
# }
```

---

## ⚙️ Configuration

### config.yaml

```yaml
# Ollama server connection
ollama_base_url: "http://localhost:11434"

# Model selection (any Ollama-compatible model)
model: "gemma3:1b"

# Generation temperature (lower = more deterministic)
temperature: 0.3

# Default SQL dialect
default_dialect: "standard"

# Query history settings
history_file: "query_history.json"
max_history: 100

# Max characters from schema sent to LLM (prevents token overflow)
max_schema_chars: 4000
```

### Configuration Options

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `ollama_base_url` | `string` | `http://localhost:11434` | Ollama server URL |
| `model` | `string` | `gemma3:1b` | LLM model name |
| `temperature` | `float` | `0.3` | Generation randomness (0.0–1.0) |
| `default_dialect` | `string` | `standard` | Default SQL dialect |
| `history_file` | `string` | `query_history.json` | Path to history JSON file |
| `max_history` | `int` | `100` | Maximum stored history entries |
| `max_schema_chars` | `int` | `4000` | Schema truncation limit (prevents token overflow) |

### Environment Variables (.env)

```bash
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=gemma3:1b
DEFAULT_DIALECT=standard
TEMPERATURE=0.3
HISTORY_FILE=query_history.json
MAX_HISTORY=100
```

### Supported Models

Any model available through Ollama works. Recommended options:

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| `gemma3:1b` | 1B | ⚡⚡⚡ | ★★★ | Quick queries, simple schemas |
| `gemma3:4b` | 4B | ⚡⚡ | ★★★★ | Complex joins, subqueries |
| `llama3.2:3b` | 3B | ⚡⚡ | ★★★★ | General purpose |
| `codellama:7b` | 7B | ⚡ | ★★★★★ | Complex optimization |
| `deepseek-coder:6.7b` | 6.7B | ⚡ | ★★★★★ | Advanced SQL patterns |

---

## 🧪 Testing

### Run All Tests

```bash
# Basic test run
python -m pytest tests/ -v

# With coverage report
python -m pytest tests/ -v --cov=src/sql_gen --cov-report=term-missing
```

### Using Make

```bash
make test          # Run all tests
make test-cov      # Run with coverage report
```

### Test Structure

| Test File | Tests | Covers |
|-----------|-------|--------|
| `test_core.py` | 14 | Schema parsing, table extraction, visualization, SQL generation, history management, config loading |
| `test_cli.py` | 5 | CLI commands, schema file handling, error states, help output, empty history display |

### Test Schema Used

```sql
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255),
    created_at TIMESTAMP
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    amount DECIMAL(10,2),
    status VARCHAR(50),
    created_at TIMESTAMP
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(200),
    price DECIMAL(10,2),
    category VARCHAR(100)
);
```

---

## 🔒 Local vs Cloud

| Feature | SQL Query Generator (Local) | Cloud AI Tools |
|---------|---------------------------|----------------|
| **Privacy** | ✅ Schema never leaves your machine | ❌ Schema sent to cloud servers |
| **Cost** | ✅ Free forever | ❌ Per-token pricing |
| **Internet** | ✅ Works offline | ❌ Requires internet |
| **Speed** | ✅ Low latency (local inference) | ⚠️ Variable (network dependent) |
| **Data Control** | ✅ Full control | ❌ Third-party data policies |
| **Customization** | ✅ Any Ollama model | ⚠️ Limited to provider models |
| **Rate Limits** | ✅ None | ❌ API rate limits apply |
| **Compliance** | ✅ Easy (data stays local) | ⚠️ May require DPA agreements |

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>1. What models work best for SQL generation?</strong></summary>

Any Ollama-compatible model works. For the best balance of speed and quality, we recommend **gemma3:1b** for simple queries and **codellama:7b** or **deepseek-coder:6.7b** for complex schemas with many tables and relationships. Update the `model` field in `config.yaml` to switch models.

</details>

<details>
<summary><strong>2. Can I use this without a schema file?</strong></summary>

Yes! The **no-schema mode** lets you generate SQL by describing your question in natural language. The LLM will infer reasonable table and column names. Just omit the `--schema` flag:

```bash
python -m src.sql_gen.cli generate --query "find users who haven't logged in for 30 days"
```

</details>

<details>
<summary><strong>3. How do I connect to a remote Ollama instance?</strong></summary>

Update the `ollama_base_url` in `config.yaml`:

```yaml
ollama_base_url: "http://192.168.1.100:11434"
```

Or set the environment variable:

```bash
export OLLAMA_BASE_URL=http://192.168.1.100:11434
```

</details>

<details>
<summary><strong>4. What SQL dialects are supported?</strong></summary>

Four dialects are supported:

- **`standard`** — ANSI SQL (default)
- **`postgresql`** — PostgreSQL-specific syntax (e.g., `ILIKE`, `SERIAL`, array types)
- **`mysql`** — MySQL-specific syntax (e.g., `LIMIT`, `AUTO_INCREMENT`, backtick quoting)
- **`sqlite`** — SQLite-specific syntax (e.g., `AUTOINCREMENT`, `datetime()` functions)

</details>

<details>
<summary><strong>5. How large of a schema can I use?</strong></summary>

By default, schemas are truncated to **4000 characters** to prevent token overflow. You can increase this limit in `config.yaml`:

```yaml
max_schema_chars: 8000
```

For very large schemas (50+ tables), consider splitting them into domain-specific files and using the `--schema` flag with the relevant subset.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Install** dev dependencies: `pip install -e ".[dev]"`
4. **Make** your changes
5. **Run** the tests: `python -m pytest tests/ -v`
6. **Commit** with a descriptive message: `git commit -m "feat: add new feature"`
7. **Push** to your fork: `git push origin feature/my-feature`
8. **Open** a Pull Request

### Development Commands

```bash
make install       # Install dependencies
make dev           # Install in development mode
make test          # Run tests
make test-cov      # Run tests with coverage
make lint          # Run linter
make run-cli       # Run CLI (use ARGS="generate -q 'test'")
make run-web       # Launch Streamlit web UI
make clean         # Remove build artifacts
```

### Code Style

This project uses [Black](https://github.com/psf/black) for code formatting. Please format your code before submitting a PR:

```bash
black src/ tests/
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](../../LICENSE) file for details.

---

<div align="center">

<br/>

**Built with ❤️ using [Ollama](https://ollama.ai) · [Click](https://click.palletsprojects.com/) · [Rich](https://rich.readthedocs.io/) · [Streamlit](https://streamlit.io)**

Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection

<br/>

<sub>If this project helped you, consider giving it a ⭐</sub>

</div>
