<div align="center">

<!-- Hero Banner -->
<img src="assets/banner.png" alt="Mood Journal Bot Banner" width="100%" />

<br/>

# 🧠 Mood Journal Bot

### *Your private, AI-powered mental health companion — powered entirely by local LLMs.*

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Gemma 4](https://img.shields.io/badge/LLM-Gemma_4-f72585?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Local First](https://img.shields.io/badge/Data-100%25_Local-00b894?style=for-the-badge&logo=shield&logoColor=white)](#privacy--security)
[![CLI + Web](https://img.shields.io/badge/Interface-CLI_%2B_Web-6c5ce7?style=for-the-badge&logo=windowsterminal&logoColor=white)](#web-ui)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[FAQ](#-faq)

<br/>

---

<br/>

</div>

## 💭 Why This Project?

Mental health journaling is one of the most effective self-care practices, yet most people struggle to maintain a consistent habit. Existing tools either lack intelligence, compromise privacy, or require expensive subscriptions.

| Challenge | How Mood Journal Bot Solves It |
|---|---|
| **Journaling feels like a chore** | Interactive prompts, gratitude suggestions, and emoji-based mood selection make entries quick and engaging |
| **Insights require a therapist** | Local AI (Gemma 4) analyzes patterns, detects trends, and generates weekly/monthly reports — no appointment needed |
| **Privacy concerns with cloud apps** | 100% local processing and JSON storage — your thoughts never leave your machine |
| **Hard to visualize progress** | Built-in mood and energy charts, distribution graphs, and statistical breakdowns in the Web UI |
| **Data is locked into proprietary formats** | Export anytime to CSV or JSON — your data, your format, your rules |

<br/>

---

## ✨ Features

<div align="center">

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#f72585;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#7209b7;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="200" rx="16" fill="#1a1a2e"/>
  <text x="400" y="60" text-anchor="middle" fill="url(#grad)" font-size="28" font-weight="bold" font-family="sans-serif">Mood Journal Bot — Feature Overview</text>
  <text x="400" y="100" text-anchor="middle" fill="#e0e0e0" font-size="16" font-family="sans-serif">Journal · Analyze · Visualize · Export</text>
  <text x="400" y="140" text-anchor="middle" fill="#888" font-size="14" font-family="sans-serif">10 Moods • Energy Tracking • Gratitude Prompts • Local AI Analysis</text>
  <text x="400" y="175" text-anchor="middle" fill="#f72585" font-size="13" font-family="sans-serif">CLI + Web Interface • Zero Cloud Dependencies</text>
</svg>
```

</div>

<br/>

<table>
<tr>
<td width="50%" valign="top">

### 📝 Journal Entries
- **10 distinct moods** with emoji indicators
- **Energy level tracking** on a 1–10 scale
- **Gratitude prompts** for positive reflection
- **Free-form text** for detailed thoughts
- Automatic timestamping with date and time
- Unique ID generation for every entry

</td>
<td width="50%" valign="top">

### 🤖 AI Insights
- Mood pattern analysis via **Gemma 4** LLM
- **Weekly reports** with trend detection
- **Monthly reports** with long-term insights
- Gratitude prompt generation
- Sentiment scoring and emotional mapping
- All analysis runs **100% locally**

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📊 Visual Charts
- **Mood timeline** line chart (past N days)
- **Energy level** trend visualization
- **Mood distribution** pie/bar chart
- Interactive Web UI with tabbed navigation
- Real-time chart updates on new entries
- Responsive design for any screen size

</td>
<td width="50%" valign="top">

### 📦 Data Export
- Export to **CSV** for spreadsheet analysis
- Export to **JSON** for programmatic use
- Filter by date range (`--days N`)
- Custom output path support
- Download directly from the Web UI
- Lossless export — all fields preserved

</td>
</tr>
</table>

<br/>

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- A local LLM runtime (e.g., Ollama) with the **Gemma 4** model pulled

### Installation

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/mood-journal-bot.git
cd mood-journal-bot

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Pull the Gemma 4 model (if using Ollama)
ollama pull gemma4
```

### Your First Journal Entry

Run the interactive `journal` command to create your first entry:

```bash
python -m mood_journal_bot journal
```

**Interactive session example:**

```
🧠 Mood Journal Bot — New Entry
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Select your mood:
  1. 😊 Happy       6. 😰 Anxious
  2. 😌 Calm        7. 😫 Stressed
  3. 😐 Neutral     8. 🙏 Grateful
  4. 😢 Sad         9. 😴 Tired
  5. 😠 Angry      10. 🤩 Excited

> 1

Energy level (1-10): > 8

How are you feeling? Write your thoughts:
> Had a great morning walk and finished a big project at work.
  Feeling accomplished and energized!

What are you grateful for today?
> My health, my supportive team, and the beautiful weather.

✅ Entry saved!
   Mood: 😊 Happy | Energy: 8/10
   Date: 2025-01-15 09:32:17
```

<br/>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/mood-journal-bot.git
cd mood-journal-bot
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
uvicorn src.mood_journal.api:app --reload --port 8000

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

## 📟 CLI Reference

The Mood Journal Bot CLI exposes **8 commands**, each accessible via `python -m mood_journal_bot <command>`.

<br/>

### 1. `journal` — Interactive Entry

Create a new journal entry with guided prompts.

```bash
python -m mood_journal_bot journal
```

Walks you through mood selection, energy level, free-text journaling, and a gratitude prompt. The entry is saved to `journal_entries.json` with a unique ID and timestamp.

<br/>

### 2. `analyze` — AI Analysis

Run local AI analysis on your recent entries.

```bash
# Analyze the last 7 days (default)
python -m mood_journal_bot analyze

# Analyze the last 30 days
python -m mood_journal_bot analyze --days 30
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--days` | `7` | Number of days to include in analysis |

**Example output:**

```
🤖 AI Mood Analysis (Last 7 Days)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your mood has been predominantly positive this week, with 5 out of 7
entries reflecting happy or calm states. Energy levels peaked mid-week
(avg 7.8) and dipped slightly on Friday (5.0). Consider maintaining
your morning walk routine — entries on those days consistently show
higher mood scores.

Gratitude themes: health, relationships, personal growth.
```

<br/>

### 3. `history` — View Past Entries

Display recent journal entries in a formatted list.

```bash
# View the last 7 days (default)
python -m mood_journal_bot history

# View the last 14 days
python -m mood_journal_bot history --days 14
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--days` | `7` | Number of days of history to display |

**Example output:**

```
📖 Journal History (Last 7 Days)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[2025-01-15 09:32] 😊 Happy | Energy: 8/10
  Had a great morning walk and finished a big project...

[2025-01-14 20:15] 😌 Calm | Energy: 6/10
  Quiet evening at home. Read a few chapters of my book...

[2025-01-13 18:45] 😫 Stressed | Energy: 4/10
  Deadline crunch at work. Skipped lunch again...
```

<br/>

### 4. `stats` — Mood Statistics

Display statistical summaries of your journal data.

```bash
python -m mood_journal_bot stats
```

**Example output:**

```
📊 Mood Statistics
━━━━━━━━━━━━━━━━━━

Total Entries:     42
Date Range:        2024-12-01 → 2025-01-15

Mood Breakdown:
  😊 Happy      12 (28.6%)
  😌 Calm        8 (19.0%)
  😐 Neutral     6 (14.3%)
  😢 Sad         4  (9.5%)
  🙏 Grateful    4  (9.5%)
  😫 Stressed    3  (7.1%)
  🤩 Excited     2  (4.8%)
  😰 Anxious     1  (2.4%)
  😴 Tired       1  (2.4%)
  😠 Angry       1  (2.4%)

Average Energy:    6.7 / 10
Most Common Mood:  😊 Happy
```

<br/>

### 5. `weekly-report` — Weekly Summary

Generate an AI-powered weekly report.

```bash
python -m mood_journal_bot weekly-report
```

Uses `generate_weekly_report(entries)` to produce a narrative summary of the past 7 days, highlighting mood trends, energy patterns, and actionable suggestions.

<br/>

### 6. `monthly-report` — Monthly Summary

Generate a comprehensive monthly report.

```bash
python -m mood_journal_bot monthly-report
```

Calls `generate_monthly_report()` to produce a long-form analysis covering a full month of entries, with comparisons to prior periods and goal recommendations.

<br/>

### 7. `gratitude` — Gratitude Prompt

Get an AI-generated gratitude prompt for reflection.

```bash
python -m mood_journal_bot gratitude
```

**Example output:**

```
🙏 Gratitude Prompt
━━━━━━━━━━━━━━━━━━

Think about a skill you've developed recently.
Who or what helped you learn it? How has it
changed your daily life? Take a moment to
appreciate the growth you've experienced.
```

<br/>

### 8. `export` — Export Data

Export your journal entries to a file.

```bash
# Export all entries as JSON (default)
python -m mood_journal_bot export

# Export last 30 days to a specific path
python -m mood_journal_bot export --output ~/exports/mood_data.csv --days 30

# Export as CSV
python -m mood_journal_bot export --output journal_backup.csv
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--output` | `journal_export.json` | Output file path (extension determines format) |
| `--days` | All entries | Number of days to include in export |

<br/>

---

## 🌐 Web UI

Launch the web interface:

```bash
python -m mood_journal_bot web
```

The Web UI is organized into **4 tabs**:

<br/>

### Tab 1: 📝 Journal

The primary entry interface for creating and reviewing journal entries.

- **Create Entry** — Select mood (emoji grid), set energy level (1–10 slider), write free-text thoughts, add gratitude notes
- **Recent Entries** — Scrollable list of your latest entries with mood emoji, energy, timestamp, and text preview
- Real-time save confirmation
- Responsive layout for desktop and mobile

<br/>

### Tab 2: 📊 Mood Chart

Visual analytics dashboard for tracking mood and energy trends.

- **Mood Line Chart** — Mood score plotted over time with color-coded data points
- **Energy Line Chart** — Energy level trend overlaid or side-by-side with mood
- **Mood Distribution** — Bar or pie chart showing the frequency of each mood type
- Adjustable date range filters
- Hover tooltips with entry details

<br/>

### Tab 3: 🧠 Insights

AI-driven analysis and report generation.

- **AI Analysis** — On-demand mood pattern analysis powered by Gemma 4
- **Weekly Report** — Auto-generated weekly narrative with trends and suggestions
- **Monthly Report** — Comprehensive monthly summary with long-term patterns
- **Statistics** — Numerical breakdown of mood counts, energy averages, and streaks
- All processing happens locally — no data leaves your machine

<br/>

### Tab 4: 📦 Export

Data export controls for backup and external analysis.

- **CSV Download** — One-click export to CSV format for spreadsheet tools
- **JSON Download** — Full-fidelity JSON export preserving all fields
- Date range selector for partial exports
- File size preview before download
- Direct browser download — no server-side storage of exports

<br/>

---

## 🏗️ Architecture

<div align="center">

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 350" width="700" height="350">
  <rect width="700" height="350" rx="12" fill="#0d1117"/>

  <!-- CLI Layer -->
  <rect x="50" y="30" width="130" height="50" rx="8" fill="#f72585" opacity="0.9"/>
  <text x="115" y="60" text-anchor="middle" fill="white" font-size="14" font-weight="bold" font-family="sans-serif">CLI</text>

  <!-- Web UI Layer -->
  <rect x="220" y="30" width="130" height="50" rx="8" fill="#7209b7" opacity="0.9"/>
  <text x="285" y="60" text-anchor="middle" fill="white" font-size="14" font-weight="bold" font-family="sans-serif">Web UI</text>

  <!-- Core Module -->
  <rect x="120" y="120" width="200" height="60" rx="8" fill="#3a0ca3" opacity="0.85"/>
  <text x="220" y="147" text-anchor="middle" fill="white" font-size="13" font-weight="bold" font-family="sans-serif">mood_journal_bot (Core)</text>
  <text x="220" y="167" text-anchor="middle" fill="#ccc" font-size="10" font-family="sans-serif">add_entry · analyze · reports</text>

  <!-- Utils -->
  <rect x="400" y="120" width="160" height="60" rx="8" fill="#4361ee" opacity="0.85"/>
  <text x="480" y="147" text-anchor="middle" fill="white" font-size="13" font-weight="bold" font-family="sans-serif">Utils</text>
  <text x="480" y="167" text-anchor="middle" fill="#ccc" font-size="10" font-family="sans-serif">load · save · export · paths</text>

  <!-- JSON Storage -->
  <rect x="80" y="240" width="170" height="50" rx="8" fill="#4cc9f0" opacity="0.85"/>
  <text x="165" y="270" text-anchor="middle" fill="#0d1117" font-size="13" font-weight="bold" font-family="sans-serif">journal_entries.json</text>

  <!-- Local LLM -->
  <rect x="320" y="240" width="170" height="50" rx="8" fill="#f72585" opacity="0.85"/>
  <text x="405" y="270" text-anchor="middle" fill="white" font-size="13" font-weight="bold" font-family="sans-serif">Gemma 4 (Local LLM)</text>

  <!-- Arrows -->
  <line x1="115" y1="80" x2="180" y2="120" stroke="#f72585" stroke-width="2"/>
  <line x1="285" y1="80" x2="260" y2="120" stroke="#7209b7" stroke-width="2"/>
  <line x1="320" y1="150" x2="400" y2="150" stroke="#666" stroke-width="1.5" stroke-dasharray="5,5"/>
  <line x1="200" y1="180" x2="165" y2="240" stroke="#4cc9f0" stroke-width="2"/>
  <line x1="260" y1="180" x2="405" y2="240" stroke="#f72585" stroke-width="2"/>
</svg>
```

</div>

<br/>

### Data Flow

```
User Input (CLI or Web)
    │
    ▼
┌─────────────────────────┐
│   mood_journal_bot core  │
│   ─────────────────────  │
│   add_entry()            │──▶ save_entries() ──▶ journal_entries.json
│   load_entries()         │◀── load_json_file()
│   analyze_entries()      │──▶ Gemma 4 LLM ──▶ AI Response
│   generate_weekly_report │──▶ Gemma 4 LLM ──▶ Report Text
│   export_entries()       │──▶ export_to_csv() / save_json_file()
└─────────────────────────┘
```

### Project Structure

```
mood-journal-bot/
├── mood_journal_bot/
│   ├── __init__.py
│   ├── __main__.py          # CLI entry point (8 commands)
│   ├── core.py              # Core journal logic (10 functions)
│   ├── utils.py             # File I/O & export utilities
│   ├── web.py               # Web UI server (4 tabs)
│   └── config.py            # Configuration loader
├── data/
│   └── journal_entries.json # Local journal storage
├── config.yaml              # LLM & app configuration
├── requirements.txt
├── tests/
│   ├── test_core.py
│   ├── test_utils.py
│   └── test_cli.py
├── assets/
│   └── banner.png
├── LICENSE
└── README.md
```

<br/>

---

## 📚 API Reference

All core functions live in `mood_journal_bot.core` and utility functions in `mood_journal_bot.utils`.

<br/>

### Core Functions (`mood_journal_bot.core`)

<br/>

#### `add_entry(mood_key, text, energy_level, gratitude)`

Create and persist a new journal entry.

```python
from mood_journal_bot.core import add_entry

entry = add_entry(
    mood_key="happy",
    text="Had an amazing day hiking in the mountains.",
    energy_level=9,
    gratitude="Fresh air and good company"
)

# Returns:
# {
#     "id": "a1b2c3d4-...",
#     "timestamp": "2025-01-15T09:32:17",
#     "date": "2025-01-15",
#     "time": "09:32:17",
#     "mood": "Happy",
#     "mood_emoji": "😊",
#     "mood_score": 9,
#     "energy_level": 9,
#     "text": "Had an amazing day hiking in the mountains.",
#     "gratitude": "Fresh air and good company"
# }
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `mood_key` | `str` | Mood identifier (e.g., `"happy"`, `"sad"`, `"anxious"`) |
| `text` | `str` | Free-form journal text |
| `energy_level` | `int` | Energy level from 1 (lowest) to 10 (highest) |
| `gratitude` | `str` | Gratitude note for the entry |

<br/>

#### `load_entries()`

Load all journal entries from the storage file.

```python
from mood_journal_bot.core import load_entries

entries = load_entries()
# Returns: list[dict] — all stored journal entries
print(f"Total entries: {len(entries)}")
```

<br/>

#### `save_entries()`

Persist the current in-memory entries to `journal_entries.json`.

```python
from mood_journal_bot.core import save_entries

save_entries()
# Writes all entries to the configured storage file
```

<br/>

#### `get_recent_entries(days)`

Retrieve entries from the last N days.

```python
from mood_journal_bot.core import get_recent_entries

# Get entries from the last 7 days
recent = get_recent_entries(days=7)
for entry in recent:
    print(f"{entry['date']} — {entry['mood_emoji']} {entry['mood']}")
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `days` | `int` | `7` | Number of days to look back |

<br/>

#### `analyze_entries(entries)`

Run AI-powered analysis on a set of journal entries.

```python
from mood_journal_bot.core import analyze_entries, get_recent_entries

entries = get_recent_entries(days=14)
analysis = analyze_entries(entries)
print(analysis)
# Prints: AI-generated narrative analysis of mood patterns,
#         energy trends, and personalized suggestions
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `entries` | `list[dict]` | List of journal entry dicts to analyze |

<br/>

#### `generate_weekly_report(entries)`

Generate an AI-powered weekly summary report.

```python
from mood_journal_bot.core import generate_weekly_report, get_recent_entries

entries = get_recent_entries(days=7)
report = generate_weekly_report(entries)
print(report)
# Prints: Narrative weekly report with mood trends,
#         energy highs/lows, and actionable recommendations
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `entries` | `list[dict]` | List of journal entries for the week |

<br/>

#### `generate_monthly_report()`

Generate a comprehensive monthly report from all entries in the past 30 days.

```python
from mood_journal_bot.core import generate_monthly_report

report = generate_monthly_report()
print(report)
# Prints: Long-form monthly analysis with comparisons,
#         patterns, and personalized recommendations
```

<br/>

#### `get_gratitude_prompt()`

Get an AI-generated gratitude reflection prompt.

```python
from mood_journal_bot.core import get_gratitude_prompt

prompt = get_gratitude_prompt()
print(prompt)
# Example: "Think about someone who made you smile this week.
#           What did they do, and how did it affect your day?"
```

<br/>

#### `get_mood_stats()`

Calculate statistical summaries across all journal entries.

```python
from mood_journal_bot.core import get_mood_stats

stats = get_mood_stats()
# Returns:
# {
#     "total_entries": 42,
#     "mood_counts": {"Happy": 12, "Calm": 8, ...},
#     "average_energy": 6.7,
#     "most_common_mood": "Happy",
#     "date_range": {"start": "2024-12-01", "end": "2025-01-15"}
# }
```

<br/>

#### `export_entries(filepath, days)`

Export journal entries to a file in CSV or JSON format.

```python
from mood_journal_bot.core import export_entries

# Export last 30 days to CSV
export_entries(filepath="mood_export.csv", days=30)

# Export all entries to JSON
export_entries(filepath="full_backup.json", days=None)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `filepath` | `str` | `"journal_export.json"` | Output file path; extension determines format |
| `days` | `int \| None` | `None` | Days to include; `None` exports all entries |

<br/>

### Utility Functions (`mood_journal_bot.utils`)

<br/>

#### `load_json_file()`

Load and parse a JSON file from the data directory.

```python
from mood_journal_bot.utils import load_json_file

data = load_json_file()
# Returns: parsed JSON content from journal_entries.json
```

<br/>

#### `save_json_file()`

Write data to a JSON file in the data directory.

```python
from mood_journal_bot.utils import save_json_file

save_json_file()
# Persists current entries to journal_entries.json
```

<br/>

#### `export_to_csv()`

Export entries to CSV format.

```python
from mood_journal_bot.utils import export_to_csv

export_to_csv()
# Writes entries as CSV with headers:
# id, timestamp, date, time, mood, mood_emoji, mood_score,
# energy_level, text, gratitude
```

<br/>

#### `get_data_path()`

Get the absolute path to the data storage directory.

```python
from mood_journal_bot.utils import get_data_path

path = get_data_path()
print(path)
# Output: /home/user/mood-journal-bot/data
```

<br/>

---

## 🎭 Mood Types

The Mood Journal Bot supports **10 distinct mood types**, each with a unique emoji and numerical score used for trend analysis.

| Mood Key | Display Name | Emoji | Score | Description |
|----------|-------------|-------|-------|-------------|
| `happy` | Happy | 😊 | 9 | Feeling joyful, content, or pleased |
| `calm` | Calm | 😌 | 7 | Peaceful, relaxed, at ease |
| `neutral` | Neutral | 😐 | 5 | Neither particularly good nor bad |
| `sad` | Sad | 😢 | 2 | Feeling down, melancholy, or blue |
| `angry` | Angry | 😠 | 2 | Frustrated, irritated, or upset |
| `anxious` | Anxious | 😰 | 3 | Worried, nervous, or uneasy |
| `stressed` | Stressed | 😫 | 3 | Overwhelmed, pressured, or tense |
| `grateful` | Grateful | 🙏 | 8 | Thankful, appreciative, blessed |
| `tired` | Tired | 😴 | 4 | Fatigued, drained, or sleepy |
| `excited` | Excited | 🤩 | 10 | Thrilled, enthusiastic, or pumped |

### Mood Score Scale

Mood scores range from **1 (lowest)** to **10 (highest)** and are used to plot trends over time:

- **8–10** — Positive states (Happy, Grateful, Excited)
- **5–7** — Neutral to mild positive (Neutral, Calm)
- **1–4** — Challenging states (Sad, Angry, Anxious, Stressed, Tired)

These scores drive the mood line charts in the Web UI and factor into the AI analysis narratives.

<br/>

---

## 🔒 Privacy & Security

Mood Journal Bot is built on a **local-first, privacy-by-design** philosophy.

### Your Data Stays Local

- **No cloud storage** — All journal entries are stored in a local `journal_entries.json` file
- **No network requests** — The app makes zero outbound API calls (LLM runs locally via Ollama)
- **No telemetry** — No analytics, tracking, or usage data is collected
- **No accounts** — No sign-up, no login, no authentication servers

### Data Storage

All entries are stored as a JSON array in `data/journal_entries.json`:

```json
[
  {
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "timestamp": "2025-01-15T09:32:17",
    "date": "2025-01-15",
    "time": "09:32:17",
    "mood": "Happy",
    "mood_emoji": "😊",
    "mood_score": 9,
    "energy_level": 8,
    "text": "Had a great morning walk and finished a big project.",
    "gratitude": "My health, my supportive team, and the weather."
  }
]
```

### Security Recommendations

- Keep your `data/` directory excluded from version control (already in `.gitignore`)
- Use disk encryption (BitLocker, FileVault, LUKS) for additional protection
- Regularly back up your `journal_entries.json` to a secure location

<br/>

---

## ⚙️ Configuration

All configuration is managed through `config.yaml` in the project root.

```yaml
# config.yaml

llm:
  model: gemma4               # Local LLM model name
  temperature: 0.7             # Response creativity (0.0 = deterministic, 1.0 = creative)
  max_tokens: 2048             # Maximum tokens per LLM response

journal:
  storage_file: journal_entries.json   # Data file name (stored in data/ directory)

export:
  format: json                 # Default export format (json or csv)
```

### Configuration Options

| Section | Key | Default | Description |
|---------|-----|---------|-------------|
| `llm` | `model` | `gemma4` | The Ollama model to use for AI analysis |
| `llm` | `temperature` | `0.7` | Controls randomness in LLM responses |
| `llm` | `max_tokens` | `2048` | Maximum response length from the LLM |
| `journal` | `storage_file` | `journal_entries.json` | Name of the JSON data file |
| `export` | `format` | `json` | Default format for the `export` command |

<br/>

---

## 🧪 Testing

Run the test suite to verify everything works:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test modules
pytest tests/test_core.py
pytest tests/test_utils.py
pytest tests/test_cli.py

# Run with coverage report
pytest --cov=mood_journal_bot --cov-report=term-missing
```

### Test Structure

| File | Coverage |
|------|----------|
| `tests/test_core.py` | Core functions: `add_entry`, `load_entries`, `analyze_entries`, reports, stats |
| `tests/test_utils.py` | Utility functions: `load_json_file`, `save_json_file`, `export_to_csv`, `get_data_path` |
| `tests/test_cli.py` | CLI commands: all 8 commands with argument parsing and output validation |

<br/>

---

## 🤖 Local LLM vs Cloud AI

Mood Journal Bot is designed for **local LLMs first**, but here's how the two approaches compare:

| Aspect | Local LLM (Default) | Cloud AI |
|--------|---------------------|----------|
| **Privacy** | ✅ 100% local — data never leaves your machine | ⚠️ Data sent to external servers |
| **Cost** | ✅ Free after initial setup | 💰 Per-token API charges |
| **Speed** | ⚡ Depends on your hardware (GPU recommended) | ⚡ Generally fast, network-dependent |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Model Quality** | 🟡 Good (Gemma 4 is highly capable) | 🟢 State-of-the-art (GPT-4, Claude, etc.) |
| **Setup** | 🔧 Requires Ollama + model download | 🔑 Requires API key |

### Why We Chose Local

For a **mental health journaling** application, privacy isn't optional — it's essential. Your deepest thoughts and feelings should never be processed by third-party servers. Local LLMs like Gemma 4 provide strong analytical capabilities while keeping everything on your machine.

<br/>

---

## ❓ FAQ

<details>
<summary><strong>1. Where is my journal data stored, and who can access it?</strong></summary>

<br/>

Your data is stored locally in `data/journal_entries.json` within the project directory. No one else can access it unless they have access to your filesystem. The application makes **zero network requests** — your entries are never uploaded, synced, or transmitted anywhere. The LLM (Gemma 4) also runs locally via Ollama, so even your AI analysis prompts stay on your machine.

To add extra protection, use full-disk encryption and keep the `data/` directory out of any cloud sync folders (Dropbox, OneDrive, etc.).

</details>

<details>
<summary><strong>2. How should I interpret the mood scores in charts?</strong></summary>

<br/>

Mood scores are numerical representations assigned to each mood type for visualization purposes:

- **8–10 (Positive):** Happy (9), Grateful (8), Excited (10) — these indicate emotionally positive states
- **5–7 (Neutral/Mild):** Neutral (5), Calm (7) — balanced or mildly positive emotional states
- **1–4 (Challenging):** Sad (2), Angry (2), Anxious (3), Stressed (3), Tired (4) — states that may benefit from attention

The line chart shows these scores over time, helping you spot patterns. A downward trend might suggest increasing stress, while an upward trend reflects improving wellbeing. The scores are **not** clinical assessments — they are self-report indicators designed to help you notice patterns in your emotional life.

</details>

<details>
<summary><strong>3. What can I do with exported data?</strong></summary>

<br/>

Exported data (CSV or JSON) can be used for:

- **Spreadsheet analysis** — Open CSV in Excel, Google Sheets, or LibreOffice Calc for custom charts and pivot tables
- **Data science** — Load JSON into Python (pandas) or R for statistical analysis
- **Backup** — Keep periodic exports as backups in case of data loss
- **Sharing with a therapist** — Provide a structured mood history to a mental health professional
- **Migration** — Move your data to another journaling tool that supports CSV/JSON import

The export preserves all fields: `id`, `timestamp`, `date`, `time`, `mood`, `mood_emoji`, `mood_score`, `energy_level`, `text`, and `gratitude`.

</details>

<details>
<summary><strong>4. Can I edit or delete a journal entry after creating it?</strong></summary>

<br/>

Currently, the CLI and Web UI do not provide a built-in edit or delete command. However, since all data is stored in a plain JSON file (`data/journal_entries.json`), you can:

1. Open `journal_entries.json` in any text editor
2. Find the entry by its `id`, `date`, or `text` content
3. Modify or remove the entry
4. Save the file

The application will pick up the changes on the next `load_entries()` call. A future release may add `edit` and `delete` CLI commands for convenience.

</details>

<details>
<summary><strong>5. How accurate is the AI analysis?</strong></summary>

<br/>

The AI analysis uses **Gemma 4**, a capable local language model, to identify patterns and generate insights. While it provides valuable observations about mood trends, energy correlations, and behavioral patterns, it has limitations:

- It is **not a substitute for professional mental health advice**
- Analysis quality improves with more entries (7+ days recommended)
- The model may occasionally miss nuance in complex emotional states
- Results depend on the detail and honesty of your journal entries

Think of it as a **smart journaling assistant** — it surfaces patterns you might not notice on your own, but significant mental health concerns should always be discussed with a qualified professional.

</details>

<br/>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/your-feature`)
3. **Commit** your changes (`git commit -m "Add your feature"`)
4. **Push** to the branch (`git push origin feature/your-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mood-journal-bot.git
cd mood-journal-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dev dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests to verify setup
pytest -v
```

### Guidelines

- Follow existing code style and patterns
- Add tests for new features
- Update documentation for any API changes
- Keep commits focused and descriptive

<br/>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">

<br/>

**Built with 💗 for mental health awareness**

<sub>Mood Journal Bot — Because your feelings deserve to be understood.</sub>

<br/>

<img src="https://img.shields.io/badge/Made_with-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Made with Python" />
<img src="https://img.shields.io/badge/Powered_by-Gemma_4-f72585?style=flat-square&logo=google&logoColor=white" alt="Powered by Gemma 4" />
<img src="https://img.shields.io/badge/Privacy-100%25_Local-00b894?style=flat-square&logo=shield&logoColor=white" alt="100% Local" />

<br/><br/>

[⬆ Back to Top](#-mood-journal-bot)

</div>
