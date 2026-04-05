<div align="center">

  <img src="docs/images/banner.svg" alt="Support Ticket Classifier Banner" width="800" />

  <br/><br/>

  <!-- Badges -->
  <a href="https://github.com/kennedyraju55/support-ticket-classifier/actions"><img src="https://img.shields.io/github/actions/workflow/status/kennedyraju55/support-ticket-classifier/ci.yml?branch=master&style=for-the-badge&logo=github-actions&logoColor=white&label=CI&color=06d6a0" alt="CI" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python" /></a>
  <a href="https://ollama.ai"><img src="https://img.shields.io/badge/Ollama-Local_LLM-06d6a0?style=for-the-badge&logo=llama&logoColor=white" alt="Ollama" /></a>
  <a href="https://streamlit.io"><img src="https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
  <a href="https://click.palletsprojects.com"><img src="https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Click CLI" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-eab308?style=for-the-badge" alt="License" /></a>

  <br/><br/>

  <strong>AI-powered support ticket classification with priority queues, SLA tracking, team routing, auto-responses, and analytics — 100 % local via Ollama.</strong>

  <br/>

  [Features](#-features) · [Quick Start](#-quick-start) · [CLI](#-cli-reference) · [Web UI](#-web-ui) · [Architecture](#-architecture) · [API](#-api-reference) · [Config](#%EF%B8%8F-configuration) · [FAQ](#-faq) · [Contributing](#-contributing)

  <br/>

  <sub>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects"><strong>90 Local LLM Projects</strong></a> collection · Project #46</sub>

</div>

<br/>

---

## 🤔 Why Support Ticket Classifier?

| Pain Point | How This Project Solves It |
|---|---|
| **Manual ticket triage wastes hours** | LLM classifies tickets into categories and priorities in seconds |
| **Missed SLA deadlines** | Automatic SLA computation with per-priority hour limits |
| **Tickets routed to the wrong team** | Rule-based routing maps each category to the correct team |
| **Slow first responses to customers** | Auto-generated, context-aware response drafts |
| **No visibility into ticket trends** | Analytics dashboard with distribution charts and confidence metrics |
| **Privacy concerns with cloud AI** | Runs entirely on your machine — zero data leaves localhost |

---

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Core Features" width="800" />
</div>

<br/>

<table>
<tr>
<td width="50%">

### 🤖 Smart Classification
- Classifies tickets into **5 default categories** (billing, technical, account, feature_request, general)
- Assigns **4 priority levels** — critical, high, medium, low
- Returns a **confidence score** (0.0–1.0) for every classification
- Produces a **suggested customer response** alongside the classification
- Fully **customisable categories** via config or CLI flags

</td>
<td width="50%">

### 🚨 Priority Queue Management
- Builds a **weighted priority queue** sorted by urgency
- Default weights: critical=4, high=3, medium=2, low=1
- **Confidence-based tiebreaker** when weights are equal
- Each item tracks position, ticket text, category, priority, confidence, and weight
- Configurable weights via `config.yaml` or programmatic API

</td>
</tr>
<tr>
<td width="50%">

### ⏱️ SLA Deadline Tracking
- Computes a **deadline timestamp** per ticket based on priority
- Default SLA windows: critical=1 h, high=4 h, medium=8 h, low=24 h
- Calculates **remaining hours** until breach in real time
- Feeds into analytics for **SLA compliance percentage**
- Fully configurable via `sla_hours` in config

</td>
<td width="50%">

### 🏢 Team Routing Engine
- Maps each **category → responsible team** automatically
- Default routes: billing→finance-team, technical→engineering-team, account→account-management, feature_request→product-team, general→support-team
- Override via `team_routing` config section
- Falls back to `support-team` for unknown categories

</td>
</tr>
<tr>
<td width="50%">

### 💬 Auto-Response Generator
- Drafts a **customer-facing reply** for every classified ticket
- Incorporates the **category**, **priority**, and **SLA window**
- Uses the LLM-suggested response as a starting point
- Enriches with SLA timeframe and support hotline call-to-action
- Ready to send or edit before sending

</td>
<td width="50%">

### 📊 Analytics Dashboard
- **Total ticket count** with breakdown by category and priority
- **Category distribution** across all classifications
- **Priority distribution** — low, medium, high, critical counts
- **Average confidence** across the batch
- **SLA compliance** percentage and high-priority ticket count

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Minimum Version | Purpose |
|---|---|---|
| **Python** | 3.10+ | Runtime |
| **Ollama** | Latest | Local LLM inference |
| **pip** | 22+ | Package management |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/support-ticket-classifier.git
cd support-ticket-classifier

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# .venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Or install as editable package with dev tools
pip install -e ".[dev]"
```

### 2. Start Ollama

```bash
# Start the Ollama server
ollama serve

# Pull the default model
ollama pull gemma3
```

### 3. Prepare a Ticket CSV

```csv
id,subject,description,customer_email
1,Login broken,"Cannot log in since yesterday, password reset not working",alice@example.com
2,Double charged,"I was charged twice for my monthly subscription",bob@example.com
3,Feature idea,"Would love to see a dark-mode option in the dashboard",carol@example.com
4,Account locked,"My account was locked after too many attempts",dave@example.com
5,Server error,"Getting 500 errors on the /api/reports endpoint",eve@example.com
```

### 4. Classify!

```bash
python -m ticket_classifier.cli classify --file tickets.csv
```

### Example Output

```
╭──────────────────────────────────────╮
│  🎫 Support Ticket Classifier        │
╰──────────────────────────────────────╯
✓ Loaded 5 tickets from tickets.csv
Categories: billing, technical, account, feature_request, general
Text column: description

Classifying tickets... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%

┌────┬─────────────────────────┬────────────────┬──────────┬────────────┬─────────────────────┬─────────────────────────────┐
│ #  │ Ticket                  │ Category       │ Priority │ Confidence │ Team                │ Suggested Response          │
├────┼─────────────────────────┼────────────────┼──────────┼────────────┼─────────────────────┼─────────────────────────────┤
│ 1  │ Cannot log in since ... │ technical      │ 🟠 High  │ 93%        │ engineering-team    │ We're investigating the ... │
│ 2  │ I was charged twice ... │ billing        │ 🔴 Crit  │ 96%        │ finance-team        │ We're reviewing your ch ... │
│ 3  │ Would love to see a ... │ feature_request│ 🟢 Low   │ 89%        │ product-team        │ Thank you for your sugg ... │
│ 4  │ My account was locke .. │ account        │ 🟠 High  │ 91%        │ account-management  │ We'll unlock your accou ... │
│ 5  │ Getting 500 errors o .. │ technical      │ 🔴 Crit  │ 95%        │ engineering-team    │ Our engineering team is  ... │
└────┴─────────────────────────┴────────────────┴──────────┴────────────┴─────────────────────┴─────────────────────────────┘

╭───────── 📊 Classification Summary ──────────╮
│  Total Tickets: 5                             │
│                                               │
│  By Category:                                 │
│    • billing: 1                               │
│    • technical: 2                             │
│    • account: 1                               │
│    • feature_request: 1                       │
│    • general: 0                               │
│                                               │
│  By Priority:                                 │
│    🟢 Low: 1                                  │
│    🟡 Medium: 0                               │
│    🟠 High: 2                                 │
│    🔴 Critical: 2                             │
│                                               │
│  Average Confidence: 92.8%                    │
│  SLA Compliance: 60.0%                        │
│  High/Critical Tickets: 4                     │
╰───────────────────────────────────────────────╯
```

---

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output.

### Global Options

| Option | Short | Default | Description |
|---|---|---|---|
| `--config` | `-cfg` | `config.yaml` | Path to YAML configuration file |

### `classify` — Classify Tickets

Classify support tickets from a CSV file, display results in a table, and show a summary panel.

```bash
python -m ticket_classifier.cli classify [OPTIONS]
```

| Option | Short | Required | Description |
|---|---|---|---|
| `--file` | `-f` | ✅ | Path to the tickets CSV file |
| `--categories` | `-c` | ❌ | Comma-separated category list (overrides config) |
| `--column` | `-col` | ❌ | Column name containing ticket text (auto-detected if omitted) |

**Examples:**

```bash
# Use defaults from config.yaml
python -m ticket_classifier.cli classify -f tickets.csv

# Override categories
python -m ticket_classifier.cli classify -f tickets.csv -c "bug,feature,billing,other"

# Specify the text column
python -m ticket_classifier.cli classify -f tickets.csv --column message

# Custom config + categories
python -m ticket_classifier.cli --config prod.yaml classify -f data/export.csv -c "urgent,normal"
```

### `analytics` — Analytics Summary

Classify tickets then display only the analytics summary (category distribution, priority breakdown, confidence, SLA compliance).

```bash
python -m ticket_classifier.cli analytics [OPTIONS]
```

| Option | Short | Required | Description |
|---|---|---|---|
| `--file` | `-f` | ✅ | Path to the tickets CSV file |
| `--categories` | `-c` | ❌ | Comma-separated category list |
| `--column` | `-col` | ❌ | Column name containing ticket text |

```bash
python -m ticket_classifier.cli analytics -f tickets.csv
python -m ticket_classifier.cli analytics -f tickets.csv -c "billing,technical,account"
```

### `priority-queue` — Priority Queue

Classify tickets, build a weighted priority queue, and display it alongside SLA tracking information.

```bash
python -m ticket_classifier.cli priority-queue [OPTIONS]
```

| Option | Short | Required | Description |
|---|---|---|---|
| `--file` | `-f` | ✅ | Path to the tickets CSV file |
| `--categories` | `-c` | ❌ | Comma-separated category list |
| `--column` | `-col` | ❌ | Column name containing ticket text |

```bash
python -m ticket_classifier.cli priority-queue -f tickets.csv
```

**Example Priority Queue Output:**

```
┌─────┬────────────────────────────────────┬────────────────┬──────────┬────────────┬────────┐
│ Pos │ Ticket                             │ Category       │ Priority │ Confidence │ Weight │
├─────┼────────────────────────────────────┼────────────────┼──────────┼────────────┼────────┤
│ 1   │ I was charged twice for my mont .. │ billing        │ 🔴 Crit  │ 96%        │ 4      │
│ 2   │ Getting 500 errors on the /api/ .. │ technical      │ 🔴 Crit  │ 95%        │ 4      │
│ 3   │ Cannot log in since yesterday,  .. │ technical      │ 🟠 High  │ 93%        │ 3      │
│ 4   │ My account was locked after too .. │ account        │ 🟠 High  │ 91%        │ 3      │
│ 5   │ Would love to see a dark-mode o .. │ feature_request│ 🟢 Low   │ 89%        │ 1      │
└─────┴────────────────────────────────────┴────────────────┴──────────┴────────────┴────────┘

╭──────── ⏱️  SLA Tracking ────────╮
│  SLA Deadlines Computed: 5       │
│  tickets tracked                 │
╰──────────────────────────────────╯
```

---

## 🌐 Web UI

Launch the Streamlit dashboard for a browser-based experience:

```bash
streamlit run src/ticket_classifier/web_ui.py
```

The app opens at **http://localhost:8501** and provides four tabs:

| Tab | Description |
|---|---|
| 📥 **Ticket Input** | Upload CSV files or paste individual tickets for classification |
| 📋 **Results** | View classification results in a colour-coded table with team assignments |
| 🚨 **Priority Queue** | See tickets sorted by urgency with SLA countdown timers |
| 📊 **Analytics** | Interactive charts for category/priority distribution and confidence metrics |

### Sidebar Controls

| Control | Description |
|---|---|
| **Config file** | Load a custom YAML configuration file |
| **Categories** | Edit classification categories on the fly |
| **Temperature** | Adjust LLM creativity (0.0 = deterministic → 1.0 = creative) |
| **SLA Hours** | Configure SLA deadlines per priority level |
| **Ollama Status** | Live connection indicator — shows ✅ or ❌ |

---

## 🏗️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800" />
</div>

<br/>

### Data Flow

```
1. CSV File ──► load_tickets()
2.            ──► find_text_column()     # auto-detect the text column
3.            ──► classify_tickets_batch()
4.                  └── classify_ticket() # LLM call per ticket (Ollama)
5.            ──► build_priority_queue()  # weighted sorting
6.            ──► compute_sla_deadlines() # deadline + remaining hours
7.            ──► route_to_team()         # category → team mapping
8.            ──► generate_auto_response()# customer-facing draft
9.            ──► compute_analytics()     # distribution & compliance
10.           ──► Display (CLI table / Streamlit dashboard)
```

### Project Structure

```
46-support-ticket-classifier/
│
├── src/
│   └── ticket_classifier/
│       ├── __init__.py            # Package metadata & version
│       ├── core.py                # All business logic
│       │   ├── load_config()      # YAML config loader with defaults
│       │   ├── load_tickets()     # CSV reader with validation
│       │   ├── find_text_column() # Heuristic column detection
│       │   ├── classify_ticket()  # Single-ticket LLM classification
│       │   ├── classify_tickets_batch()  # Batch with progress callback
│       │   ├── build_priority_queue()    # Weighted priority sorting
│       │   ├── compute_sla_deadlines()   # SLA deadline computation
│       │   ├── route_to_team()           # Category → team routing
│       │   ├── generate_auto_response()  # Customer reply generation
│       │   └── compute_analytics()       # Aggregate statistics
│       │
│       ├── cli.py                 # Click CLI interface
│       │   ├── main (group)       # --config / -cfg global option
│       │   ├── classify           # --file, --categories, --column
│       │   ├── analytics          # --file, --categories, --column
│       │   └── priority-queue     # --file, --categories, --column
│       │
│       └── web_ui.py              # Streamlit web dashboard
│
├── tests/
│   ├── test_core.py               # Unit tests for core logic
│   └── test_cli.py                # CLI integration tests
│
├── common/
│   └── llm_client.py              # Shared Ollama client (chat, check)
│
├── docs/
│   └── images/
│       ├── banner.svg             # Project banner
│       ├── architecture.svg       # Architecture diagram
│       └── features.svg           # Feature grid
│
├── config.yaml                    # Runtime configuration
├── setup.py                       # Package setup / entry points
├── requirements.txt               # Dependencies
├── Makefile                       # Dev workflow commands
├── .env.example                   # Environment template
└── README.md                      # This file
```

---

## 📚 API Reference

All public functions live in `ticket_classifier.core`. Import them directly:

```python
from ticket_classifier.core import (
    load_config,
    load_tickets,
    find_text_column,
    classify_ticket,
    classify_tickets_batch,
    build_priority_queue,
    compute_sla_deadlines,
    route_to_team,
    generate_auto_response,
    compute_analytics,
)
```

### `load_config(path="config.yaml") → dict`

Load a YAML configuration file and merge with sensible defaults.

```python
config = load_config("config.yaml")
# config["categories"]       → ["billing", "technical", "account", ...]
# config["sla_hours"]        → {"critical": 1, "high": 4, ...}
# config["team_routing"]     → {"billing": "finance-team", ...}
# config["priority_weights"] → {"critical": 4, "high": 3, ...}
# config["model"]            → {"name": "gemma3", "temperature": 0.2, ...}
```

### `load_tickets(file_path) → list[dict]`

Load tickets from a CSV file. Raises `FileNotFoundError`, `ValueError` (empty), or `RuntimeError`.

```python
tickets = load_tickets("tickets.csv")
# [{"id": "1", "description": "Cannot log in ...", "customer": "alice@example.com"}, ...]
```

### `find_text_column(data) → str`

Auto-detect the column containing ticket descriptions. Checks known names first (`description`, `subject`, `message`, `text`, `content`, `body`, `issue`, `summary`), then falls back to the column with the longest average text.

```python
text_col = find_text_column(tickets)
# "description"
```

### `classify_ticket(ticket_text, categories, *, temperature=0.2) → dict`

Classify a single ticket using the local LLM. Returns structured JSON with fallback handling.

```python
result = classify_ticket(
    "I was charged twice for my subscription",
    ["billing", "technical", "account", "feature_request", "general"],
)
# {
#     "category": "billing",
#     "priority": "high",
#     "confidence": 0.94,
#     "suggested_response": "We're reviewing your recent charges ..."
# }
```

### `classify_tickets_batch(tickets, categories, text_col, *, temperature=0.2, on_progress=None) → list[dict]`

Batch-classify a list of ticket dicts. Accepts an optional progress callback `(current, total) → None`.

```python
def show_progress(current, total):
    print(f"  {current}/{total}")

classifications = classify_tickets_batch(
    tickets, categories, "description",
    temperature=0.2, on_progress=show_progress,
)
```

### `build_priority_queue(tickets, classifications, text_col, priority_weights=None) → list[dict]`

Build a priority-sorted queue. Each item contains: `position`, `ticket_text`, `category`, `priority`, `confidence`, `suggested_response`, `weight`.

```python
queue = build_priority_queue(tickets, classifications, "description")
# Sorted by (-weight, -confidence)
# queue[0]["position"] == 1   (highest priority)
```

### `compute_sla_deadlines(classifications, sla_hours=None, *, created_at=None) → list[dict]`

Compute SLA deadline and remaining hours for each classification.

```python
sla = compute_sla_deadlines(classifications)
# [
#     {"priority": "high", "sla_hours": 4, "deadline": "2025-01-15T14:30:00", "remaining_hours": 3.2},
#     ...
# ]
```

### `route_to_team(classification, routing_rules=None) → str`

Map a classification to the responsible team.

```python
team = route_to_team({"category": "billing", "priority": "high"})
# "finance-team"
```

### `generate_auto_response(ticket_text, classification) → str`

Generate a polished customer-facing auto-response that includes the category, priority, and SLA window.

```python
response = generate_auto_response("I was charged twice", {"category": "billing", "priority": "high"})
# "Thank you for contacting us regarding your billing issue.\n\n..."
```

### `compute_analytics(classifications, categories) → dict`

Compute aggregate analytics over a batch of classifications.

```python
analytics = compute_analytics(classifications, categories)
# {
#     "total_tickets": 50,
#     "category_distribution": {"billing": 12, "technical": 18, ...},
#     "priority_distribution": {"low": 8, "medium": 20, "high": 15, "critical": 7},
#     "avg_confidence": 0.891,
#     "sla_compliance": 86.0,
#     "high_priority_count": 22
# }
```

---

## ⚙️ Configuration

All settings are managed via `config.yaml`. The system loads defaults for any missing key.

```yaml
# ─── LLM Model Settings ───────────────────────────────────────
model:
  name: "gemma3"             # Ollama model name
  temperature: 0.2           # LLM temperature (0.0 = deterministic, 1.0 = creative)
  max_tokens: 2000           # Maximum response tokens

# ─── Classification Categories ────────────────────────────────
categories:
  - billing
  - technical
  - account
  - feature_request
  - general

# ─── SLA Deadlines (hours per priority) ───────────────────────
sla_hours:
  critical: 1                # 1 hour to respond
  high: 4                    # 4 hours to respond
  medium: 8                  # 8 hours to respond
  low: 24                    # 24 hours to respond

# ─── Team Routing (category → team) ──────────────────────────
team_routing:
  billing: "finance-team"
  technical: "engineering-team"
  account: "account-management"
  feature_request: "product-team"
  general: "support-team"

# ─── Priority Queue Weights ──────────────────────────────────
priority_weights:
  critical: 4                # Highest weight
  high: 3
  medium: 2
  low: 1                     # Lowest weight

# ─── Logging ─────────────────────────────────────────────────
logging:
  level: "INFO"              # DEBUG, INFO, WARNING, ERROR
  file: "ticket_classifier.log"
```

### Configuration Defaults

If `config.yaml` is missing or incomplete, these defaults are used:

| Setting | Default Value |
|---|---|
| `model.name` | `gemma3` |
| `model.temperature` | `0.2` |
| `model.max_tokens` | `2000` |
| `categories` | `billing, technical, account, feature_request, general` |
| `sla_hours.critical` | `1` |
| `sla_hours.high` | `4` |
| `sla_hours.medium` | `8` |
| `sla_hours.low` | `24` |
| `priority_weights.critical` | `4` |
| `priority_weights.high` | `3` |
| `priority_weights.medium` | `2` |
| `priority_weights.low` | `1` |

---

## 📁 Input Format

The classifier expects a **CSV file** with at least one text column. The column is auto-detected or can be specified with `--column`.

### Supported Column Names (Auto-Detected)

`description` · `subject` · `message` · `text` · `content` · `body` · `issue` · `summary`

If none of these names match, the system picks the column with the **longest average text** across the first 5 rows.

### Example CSV

```csv
id,subject,description,customer_email,created_at
1,Login broken,"Cannot log in since yesterday, password reset not working",alice@example.com,2025-01-15T10:30:00
2,Double charged,"I was charged twice for my monthly subscription",bob@example.com,2025-01-15T11:00:00
3,Feature idea,"Would love to see a dark-mode option in the dashboard",carol@example.com,2025-01-15T11:30:00
4,Account locked,"My account was locked after too many failed login attempts",dave@example.com,2025-01-15T12:00:00
5,Server error,"Getting 500 errors on the /api/reports endpoint since 9am",eve@example.com,2025-01-15T12:30:00
```

---

## 🧪 Testing

The project includes unit tests for core logic and integration tests for the CLI.

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=ticket_classifier --cov-report=term-missing

# Run only core logic tests
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v

# Quick syntax check
python -m py_compile src/ticket_classifier/core.py
python -m py_compile src/ticket_classifier/cli.py
```

### What's Tested

| Test File | Scope |
|---|---|
| `test_core.py` | `load_tickets`, `find_text_column`, `classify_ticket`, `build_priority_queue`, `compute_sla_deadlines`, `route_to_team`, `generate_auto_response`, `compute_analytics` |
| `test_cli.py` | CLI invocation, `classify` command, `analytics` command, `priority-queue` command, error handling |

---

## 🏠 Local vs ☁️ Cloud

| Aspect | Local (This Project) | Cloud-Based |
|---|---|---|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to external servers |
| **Cost** | ✅ Free after hardware | ❌ Per-token API charges |
| **Latency** | ⚡ Low (no network round-trip) | 🐌 Variable (network dependent) |
| **Offline** | ✅ Works without internet | ❌ Requires connectivity |
| **Model Choice** | 🔄 Any Ollama model | 🔒 Limited to provider's models |
| **Setup** | 🛠️ Requires Ollama installation | ✅ API key and go |
| **Scalability** | ⚠️ Limited by local hardware | ✅ Scales with provider |

---

## ❓ FAQ

<details>
<summary><strong>1. Which LLM models are supported?</strong></summary>

Any model available through [Ollama](https://ollama.ai) works out of the box. The default is `gemma3`, but you can change it in `config.yaml` under `model.name`. Popular alternatives include `llama3`, `mistral`, `phi3`, and `codellama`. Simply run `ollama pull <model>` and update your config.

</details>

<details>
<summary><strong>2. How do I add custom categories?</strong></summary>

Edit the `categories` list in `config.yaml`:

```yaml
categories:
  - billing
  - technical
  - account
  - feature_request
  - general
  - compliance        # ← new category
  - security          # ← new category
```

Or pass them via CLI: `--categories "billing,technical,security,compliance"`. Don't forget to add corresponding entries in `team_routing` for automatic team assignment.

</details>

<details>
<summary><strong>3. What happens if the LLM returns an invalid response?</strong></summary>

The classifier includes robust fallback handling. If the LLM response cannot be parsed as JSON, or if the category/priority is invalid, the system returns a default classification: `category=<first_category>`, `priority=medium`, `confidence=0.5`, and a generic suggested response. This ensures the pipeline never breaks.

</details>

<details>
<summary><strong>4. Can I process thousands of tickets?</strong></summary>

Yes. The `classify_tickets_batch()` function processes tickets sequentially with an optional progress callback. The CLI shows a progress bar via Rich. For very large batches, consider lowering the temperature for faster inference and using a lighter model like `phi3`.

</details>

<details>
<summary><strong>5. How is SLA compliance calculated?</strong></summary>

The current implementation uses a simplified metric: SLA compliance = percentage of tickets that are **not** classified as `critical`. In a production deployment, you would replace this with actual response-time tracking against the computed deadlines. The deadline computation itself (`compute_sla_deadlines`) is fully accurate and based on configurable per-priority hour windows.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and install in development mode
git clone https://github.com/kennedyraju55/support-ticket-classifier.git
cd support-ticket-classifier
pip install -e ".[dev]"
```

### Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes and add tests
4. **Run** the test suite: `python -m pytest tests/ -v`
5. **Lint** your code: `python -m py_compile src/ticket_classifier/core.py`
6. **Commit** with a descriptive message
7. **Push** and open a Pull Request

### Code Style

- Follow **PEP 8** conventions
- Use **type hints** for all function signatures
- Add **docstrings** to all public functions
- Keep functions focused — one responsibility per function

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

<div align="center">

  <br/>

  <sub>Built with ❤️ using <a href="https://ollama.ai">Ollama</a> and local LLMs</sub>

  <br/>

  <a href="https://github.com/kennedyraju55/support-ticket-classifier">
    <img src="https://img.shields.io/badge/⭐_Star_this_repo-06d6a0?style=for-the-badge" alt="Star" />
  </a>

  <br/><br/>

  <sub><strong>Project #46</strong> of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</sub>

  <br/>

  <img src="https://img.shields.io/badge/Made_with-Python-3776ab?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Powered_by-Ollama-06d6a0?style=flat-square" alt="Ollama" />
  <img src="https://img.shields.io/badge/UI-Streamlit-ff4b4b?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/CLI-Click-4EAA25?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click" />

</div>
