<div align="center">

  <!-- Hero Banner -->
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg"/>
    <img src="docs/images/banner.svg" alt="Flashcard Creator — AI-Powered Spaced Repetition Flashcard System" width="800"/>
  </picture>

  <br/><br/>

  <!-- Badges -->
  <a href="https://ai.google.dev/gemma"><img src="https://img.shields.io/badge/Gemma_3-Local_LLM-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemma 3"/></a>
  <a href="https://ollama.com"><img src="https://img.shields.io/badge/Ollama-Runtime-000000?style=for-the-badge&logo=ollama&logoColor=white" alt="Ollama"/></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/></a>
  <a href="https://streamlit.io"><img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>

  <br/>

  <a href="https://click.palletsprojects.com"><img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/></a>
  <a href="https://docs.pytest.org"><img src="https://img.shields.io/badge/pytest-Tested-009688?style=flat-square&logo=pytest&logoColor=white" alt="pytest"/></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT License"/>
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square" alt="PRs Welcome"/>
  <img src="https://img.shields.io/badge/Version-1.0.0-00b4d8?style=flat-square" alt="Version 1.0.0"/>
  <img src="https://img.shields.io/badge/Algorithm-SM--2-purple?style=flat-square" alt="SM-2"/>

  <br/><br/>

  <strong>
    Production-grade flashcard creation &amp; review system powered by a local LLM<br/>
    with spaced repetition (SM-2), deck management, import/export, CLI &amp; web UI.
  </strong>

  <br/><br/>

  <strong>Project #52 of <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a></strong>

  <br/><br/>

  <!-- Quick Links -->
  <a href="#-why-this-project">Why This Project?</a> •
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-web-ui">Web UI</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-testing">Testing</a> •
  <a href="#-faq">FAQ</a> •
  <a href="#-contributing">Contributing</a>

</div>

<br/>

---

<br/>

## 💡 Why This Project?

Most flashcard tools are cloud-dependent, subscription-locked, or lack real
spaced-repetition scheduling.  **Flashcard Creator** solves all of that by
running entirely on your machine with a local LLM.

| # | Problem | Solution |
|---|---------|----------|
| 1 | **Manual card creation is tedious** — writing hundreds of cards by hand burns study time. | AI-powered generation via Gemma 3 — give it a topic, get structured cards in seconds. |
| 2 | **Cloud flashcard apps harvest your data** — study content is personal and sensitive. | 100 % local — Ollama runs on your machine, decks are stored as plain JSON files. |
| 3 | **Random review order wastes time** — you re-study easy cards while hard ones slip away. | SM-2 spaced-repetition algorithm schedules each card at the scientifically optimal interval. |
| 4 | **Vendor lock-in traps your content** — exporting from Anki / Quizlet is painful. | First-class JSON and CSV import/export — your data is always portable and yours. |
| 5 | **No offline access** — cloud tools are useless without internet. | Everything runs offline — Ollama, the CLI, and the Streamlit UI need zero internet. |

<br/>

---

<br/>

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Key Features — SM-2, Deck Management, Interactive Review, Import/Export, Rich Metadata, Statistics" width="800"/>
</div>

<br/>

| | AI Generation | Study & Review |
|---|---|---|
| **Core** | 🤖 Generate flashcards on any topic with Gemma 3 via Ollama | 🧠 SM-2 spaced-repetition algorithm with adaptive ease factors |
| **Metadata** | 🏷️ Automatic difficulty tagging (easy / medium / hard), hints, and topic tags | 🎯 Quality-based recall ratings (0–5) with session score tracking |
| **Management** | 📚 Full deck CRUD — create, delete, list, merge, and browse decks | 📊 Per-deck statistics — cards reviewed, score %, difficulty breakdown |
| **Portability** | 📤 Import and export decks as JSON or CSV files | 💻 CLI (Click + Rich) **and** 🌐 Streamlit web UI — pick your interface |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Install |
|---|---|---|
| **Python** | 3.10 + | [python.org](https://python.org) |
| **Ollama** | latest | [ollama.com](https://ollama.com) |
| **Gemma 3** | any | `ollama pull gemma3` |

### 1 — Clone &amp; install

```bash
git clone https://github.com/kennedyraju55/flashcard-creator.git
cd flashcard-creator

# Install in editable / development mode
pip install -e ".[dev]"

# Or install dependencies directly
pip install -r requirements.txt
```

### 2 — Start Ollama

```bash
ollama serve          # start the runtime (leave running)
ollama pull gemma3    # download the model (once)
```

### 3 — Generate your first deck

```bash
flashcard-creator create --topic "Python Decorators" --count 5 --deck-name "Python"
```

<details>
<summary><strong>📋 Example output</strong></summary>

```
┌──────────────────────────────────────────────────────┐
│              🗂️ Flashcard Creator                     │
│              Powered by Local LLM                     │
└──────────────────────────────────────────────────────┘

Creating 5 flashcards about 'Python Decorators'...

┌────────────────────────────────────────────────────────────────────┐
│                  Flashcards: Python Decorators                     │
├────┬──────────────────────────┬───────────────────────┬────────────┤
│  # │ Front                    │ Back                  │ Difficulty │
├────┼──────────────────────────┼───────────────────────┼────────────┤
│  1 │ What is a decorator in   │ A decorator is a      │ easy       │
│    │ Python?                  │ function that takes    │            │
│    │                          │ another function and   │            │
│    │                          │ extends its behavior   │            │
│    │                          │ without modifying it.  │            │
├────┼──────────────────────────┼───────────────────────┼────────────┤
│  2 │ What does the @          │ The @ symbol is        │ easy       │
│    │ symbol mean before a     │ syntactic sugar for    │            │
│    │ function definition?     │ applying a decorator.  │            │
├────┼──────────────────────────┼───────────────────────┼────────────┤
│  3 │ What is functools.wraps  │ It preserves the      │ medium     │
│    │ used for?                │ original function's    │            │
│    │                          │ metadata (__name__,    │            │
│    │                          │ __doc__, etc.) when    │            │
│    │                          │ wrapping it.           │            │
├────┼──────────────────────────┼───────────────────────┼────────────┤
│  4 │ Can decorators accept    │ Yes — you create a     │ hard       │
│    │ arguments?               │ decorator factory:     │            │
│    │                          │ a function that        │            │
│    │                          │ returns a decorator.   │            │
├────┼──────────────────────────┼───────────────────────┼────────────┤
│  5 │ Name two common use      │ Logging and access     │ medium     │
│    │ cases for decorators.    │ control / authenti-    │            │
│    │                          │ cation.                │            │
└────┴──────────────────────────┴───────────────────────┴────────────┘

✓ Added 5 cards to deck 'Python'
✓ Flashcards saved to flashcards_python_decorators.json
```

</details>

### 4 — Review your deck

```bash
flashcard-creator review --deck "Python" --shuffle
```

### 5 — Launch the web UI (optional)

```bash
streamlit run src/flashcard_creator/web_ui.py
```

<br/>

---

<br/>

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses
[Rich](https://rich.readthedocs.io/) for beautiful terminal output. Six
commands cover the full workflow.

```text
Usage: flashcard-creator [OPTIONS] COMMAND [ARGS]...

  🗂️ Flashcard Creator — Generate and review study flashcards.

Commands:
  create       Create flashcards from a topic using the LLM.
  review       Interactive flashcard review session.
  decks        List all saved decks.
  import-deck  Import a deck from a file.
  export-deck  Export a deck to a file.
  stats        Show review statistics for a deck.
```

<br/>

### `create` — Generate flashcards

Create flashcards on any topic using the local LLM. Cards are displayed in a
Rich table and optionally saved to a named deck.

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--topic` | `-t` | `TEXT` | *(required)* | Topic for flashcard generation |
| `--count` | `-c` | `INT` | `10` (from config) | Number of flashcards to generate |
| `--difficulty` | `-d` | `easy\|medium\|hard` | `medium` (from config) | Difficulty level |
| `--deck-name` | `-n` | `TEXT` | — | Save generated cards to this deck |
| `--output` | `-o` | `PATH` | auto-generated | Output JSON file path |

```bash
# Generate 15 hard flashcards about Docker and save to a deck
flashcard-creator create \
  --topic "Docker Compose" \
  --count 15 \
  --difficulty hard \
  --deck-name "DevOps"
```

<br/>

### `review` — Interactive review session

Review a deck interactively. Each card is shown front-first; press Enter to
reveal the back, then rate your recall on a 0–5 scale. Scores are fed into the
SM-2 algorithm to schedule future reviews.

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--deck` | `-d` | `TEXT` | *(required)* | Name of the deck to review |
| `--due-only` | — | `FLAG` | `False` | Only review cards that are due (per SM-2) |
| `--shuffle / --no-shuffle` | — | `FLAG` | `True` | Shuffle card order |

```bash
# Review only due cards without shuffling
flashcard-creator review --deck "DevOps" --due-only --no-shuffle
```

<br/>

### `decks` — List all saved decks

Display every saved deck with card counts, tags, and creation dates.

```bash
flashcard-creator decks
```

```
┌──────────────────────────────────────────────────────────────┐
│                        Saved Decks                            │
├──────────────┬───────┬────────────────────────┬───────────────┤
│ Name         │ Cards │ Tags                   │ Created       │
├──────────────┼───────┼────────────────────────┼───────────────┤
│ Python       │    25 │ python, decorators     │ 2025-01-15    │
│ DevOps       │    15 │ docker, compose        │ 2025-01-16    │
│ SQL Mastery  │    30 │ sql, joins, database   │ 2025-01-17    │
└──────────────┴───────┴────────────────────────┴───────────────┘
```

<br/>

### `import-deck` — Import a deck from file

Import flashcards from an external JSON or CSV file. The imported deck is
saved to the configured `decks_dir`.

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--file` | `-f` | `PATH` | *(required)* | File to import (must exist) |
| `--format` | `-F` | `json\|csv` | `json` | File format |

```bash
flashcard-creator import-deck --file shared_deck.csv --format csv
```

<br/>

### `export-deck` — Export a deck to file

Export a deck to JSON or CSV for sharing, backup, or migration.

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--deck` | `-d` | `TEXT` | *(required)* | Deck name to export |
| `--format` | `-F` | `json\|csv` | `json` | Output format |
| `--output` | `-o` | `PATH` | auto-generated | Output file path |

```bash
flashcard-creator export-deck --deck "Python" --format csv --output python_cards.csv
```

<br/>

### `stats` — View deck statistics

Show aggregated review statistics for a deck, including card counts by
difficulty, number of reviewed cards, and cards currently due.

| Option | Short | Type | Default | Description |
|--------|-------|------|---------|-------------|
| `--deck` | `-d` | `TEXT` | *(required)* | Deck name |

```bash
flashcard-creator stats --deck "Python"
```

```
┌─────────────────────────────────────────┐
│            Stats: Python                 │
├─────────────────────┬───────────────────┤
│ Metric              │             Value │
├─────────────────────┼───────────────────┤
│ Total cards         │                25 │
│ Cards reviewed      │                18 │
│ Due for review      │                 7 │
│   easy              │                 8 │
│   medium            │                12 │
│   hard              │                 5 │
└─────────────────────┴───────────────────┘
```

<br/>

---

<br/>

## 🌐 Web UI

Launch the Streamlit-based web interface for a visual, browser-based experience:

```bash
streamlit run src/flashcard_creator/web_ui.py
```

The web UI provides four modes accessible from the sidebar:

| Mode | What You Can Do |
|------|-----------------|
| **🤖 Create Cards** | Enter a topic, choose count and difficulty, generate cards with the LLM, edit inline, and save to a deck. |
| **🧠 Review Mode** | Select a deck, flip through cards one-by-one, optionally reveal hints, rate your recall (0–5), and see a session summary with score percentage. |
| **📚 Deck Browser** | Browse all decks, search cards by keyword, filter by tag, view card details including hints and difficulty levels. |
| **📊 Statistics** | Cards-per-deck chart, difficulty breakdown, mastery progress over time, SM-2 ease factor and interval distributions. |

> **Tip:** The web UI uses the same `core.py` engine as the CLI — decks
> created via one interface are immediately visible in the other.

<br/>

---

<br/>

## 🏛️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="System Architecture — User → CLI/Streamlit → Core → Ollama, SM-2, DeckManager, ReviewSession, Import/Export" width="800"/>
</div>

<br/>

The system follows a clean layered architecture:

| Layer | Components | Responsibility |
|-------|------------|----------------|
| **Interface** | `cli.py` (Click + Rich), `web_ui.py` (Streamlit) | User interaction, input validation, display |
| **Core** | `core.py` — `SpacedRepetition`, `DeckManager`, `ReviewSession` | Business logic, SM-2 scheduling, deck CRUD |
| **Generation** | `create_flashcards()` → `common/llm_client.py` → Ollama | LLM prompting, JSON parsing, card creation |
| **Storage** | `./decks/*.json`, `config.yaml`, CSV export files | Persistent deck storage, configuration |

<br/>

### Project Tree

```
52-flashcard-creator/
├── docs/
│   └── images/
│       ├── banner.svg             # Hero banner image
│       ├── architecture.svg       # System architecture diagram
│       └── features.svg           # Feature highlights grid
├── src/
│   └── flashcard_creator/
│       ├── __init__.py            # Package metadata & version
│       ├── core.py                # Business logic, SM-2, deck management
│       ├── cli.py                 # Click CLI commands (6 commands)
│       └── web_ui.py              # Streamlit web interface (4 modes)
├── tests/
│   ├── __init__.py
│   ├── test_core.py               # Core logic, SM-2, import/export tests
│   └── test_cli.py                # CLI command integration tests
├── common/
│   └── llm_client.py              # Shared Ollama / LLM client
├── decks/                         # Saved decks (JSON files)
├── config.yaml                    # Application configuration
├── setup.py                       # Package setup (pip installable)
├── requirements.txt               # Python dependencies
├── Makefile                       # Common dev tasks
├── .env.example                   # Environment variable template
├── .gitignore
└── README.md                      # This file
```

<br/>

---

<br/>

## 📖 API Reference

All public classes and functions live in `flashcard_creator.core`. Import them
directly for programmatic use.

```python
from flashcard_creator.core import (
    ConfigManager,
    Flashcard,
    Deck,
    ReviewStats,
    SpacedRepetition,
    ReviewSession,
    DeckManager,
    create_flashcards,
    dict_to_flashcards,
    export_deck_json,
    export_deck_csv,
    import_deck_json,
    import_deck_csv,
)
```

<br/>

### `Flashcard` (dataclass)

A single flashcard with spaced-repetition metadata.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `id` | `str` | UUID (8 chars) | Unique identifier |
| `front` | `str` | `""` | Question or term (front of card) |
| `back` | `str` | `""` | Answer or definition (back of card) |
| `hint` | `str` | `""` | Optional hint shown before the answer |
| `difficulty` | `str` | `"medium"` | `easy`, `medium`, or `hard` |
| `tags` | `list[str]` | `[]` | Categorisation tags |
| `created_at` | `str` | ISO timestamp | When the card was created |
| `last_reviewed` | `str \| None` | `None` | Last review timestamp |
| `ease_factor` | `float` | `2.5` | SM-2 ease factor (≥ 1.3) |
| `interval` | `int` | `1` | Days until next review |
| `repetitions` | `int` | `0` | Consecutive successful reviews |

```python
from flashcard_creator.core import Flashcard

card = Flashcard(
    front="What is a closure?",
    back="A function that captures variables from its enclosing scope.",
    hint="Think about variable scope",
    difficulty="medium",
    tags=["python", "functions"],
)
print(card.id)           # e.g. "a3f1b2c4"
print(card.ease_factor)  # 2.5
```

<br/>

### `Deck` (dataclass)

A named collection of flashcards.

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `name` | `str` | `"Untitled"` | Deck name |
| `description` | `str` | `""` | Deck description |
| `cards` | `list[Flashcard]` | `[]` | Cards in the deck |
| `created_at` | `str` | ISO timestamp | When the deck was created |
| `tags` | `list[str]` | `[]` | Deck-level tags |

```python
from flashcard_creator.core import Deck, Flashcard

deck = Deck(
    name="Python Basics",
    description="Fundamental Python concepts",
    tags=["python", "beginner"],
)
deck.cards.append(Flashcard(front="What is PEP 8?", back="Python's style guide."))
print(f"{deck.name}: {len(deck.cards)} cards")
```

<br/>

### `SpacedRepetition`

Implements the SM-2 spaced-repetition algorithm.

| Method | Signature | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__` | `(config: ConfigManager \| None)` | — | Load SM-2 parameters from config |
| `calculate_next_review` | `(card: Flashcard, quality: int)` | `Flashcard` | Update card intervals and ease factor in-place |
| `get_due_cards` | `(deck: Deck)` | `list[Flashcard]` | Return cards that are due for review now |

```python
from flashcard_creator.core import SpacedRepetition, Flashcard

sr = SpacedRepetition()
card = Flashcard(front="Q", back="A")

# Perfect recall — interval grows
card = sr.calculate_next_review(card, quality=5)
print(card.interval)      # 1 (first review)
print(card.ease_factor)   # 2.6

# Second perfect recall
card = sr.calculate_next_review(card, quality=5)
print(card.interval)      # 6 (graduating interval)
```

<br/>

### `DeckManager`

Persist and manage multiple decks on disk.

| Method | Signature | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__` | `(decks_dir: str = "./decks")` | — | Create manager with storage directory |
| `create_deck` | `(name, description, tags)` | `Deck` | Create and save a new deck |
| `delete_deck` | `(name)` | `bool` | Delete a deck from disk |
| `list_decks` | `()` | `list[Deck]` | List all saved decks |
| `get_deck` | `(name)` | `Deck \| None` | Load a deck by name |
| `add_card` | `(deck_name, card)` | `Deck` | Add a card to a deck (creates deck if needed) |
| `remove_card` | `(deck_name, card_id)` | `Deck` | Remove a card by its ID |
| `import_deck` | `(filepath, fmt)` | `Deck` | Import a deck from JSON or CSV |
| `export_deck` | `(deck, filepath, fmt)` | `str` | Export a deck to JSON or CSV |
| `merge_decks` | `(deck_a, deck_b, new_name)` | `Deck` | Merge two decks into one |
| `get_stats` | `(deck)` | `ReviewStats` | Get aggregated statistics for a deck |

```python
from flashcard_creator.core import DeckManager, Flashcard

dm = DeckManager("./decks")

# Create a deck and add a card
deck = dm.create_deck("Algorithms", description="CS fundamentals")
dm.add_card("Algorithms", Flashcard(
    front="What is Big-O notation?",
    back="A mathematical notation describing the upper bound of an algorithm's time complexity.",
    difficulty="medium",
))

# List all decks
for d in dm.list_decks():
    print(f"  {d.name}: {len(d.cards)} cards")

# Export and re-import
dm.export_deck(deck, "algorithms.csv", fmt="csv")
imported = dm.import_deck("algorithms.csv", fmt="csv")

# Merge two decks
merged = dm.merge_decks(deck, imported, new_name="Combined CS")
```

<br/>

### `ReviewSession`

Tracks state for a single review session.

| Method | Signature | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__` | `(deck, shuffle=True, due_only=False)` | — | Set up review queue |
| `record` | `(quality: int)` | `None` | Record a 0–5 quality rating |
| `finish` | `()` | `ReviewStats` | End session, return aggregated stats |

```python
from flashcard_creator.core import ReviewSession, DeckManager

dm = DeckManager("./decks")
deck = dm.get_deck("Algorithms")

session = ReviewSession(deck, shuffle=True, due_only=False)
for card in session.cards:
    print(f"Q: {card.front}")
    # ... user answers ...
    session.record(quality=4)

stats = session.finish()
print(f"Score: {stats.correct}/{stats.cards_reviewed} ({stats.score_pct:.0f}%)")
print(f"Average quality: {stats.avg_quality:.1f}")
print(f"Time elapsed: {stats.time_elapsed_s:.0f}s")
```

<br/>

### `ReviewStats` (dataclass)

Aggregated statistics returned by `ReviewSession.finish()` and
`DeckManager.get_stats()`.

| Field | Type | Description |
|-------|------|-------------|
| `total_cards` | `int` | Total cards in the deck / session |
| `cards_reviewed` | `int` | Number of cards actually reviewed |
| `correct` | `int` | Cards with quality ≥ 3 |
| `incorrect` | `int` | Cards with quality < 3 |
| `score_pct` | `float` | Percentage score (correct / reviewed × 100) |
| `avg_quality` | `float` | Mean quality rating across all reviews |
| `time_elapsed_s` | `float` | Total session time in seconds |
| `cards_by_difficulty` | `dict` | Count of cards per difficulty level |
| `due_cards` | `int` | Number of cards currently due for review |

<br/>

### Core Functions

| Function | Signature | Returns | Description |
|----------|-----------|---------|-------------|
| `create_flashcards` | `(topic, count, difficulty, config)` | `dict` | Generate flashcards via LLM |
| `dict_to_flashcards` | `(data: dict)` | `list[Flashcard]` | Convert raw LLM JSON to Flashcard instances |
| `export_deck_json` | `(deck, filepath)` | `str` | Export a deck to a JSON file |
| `export_deck_csv` | `(deck, filepath)` | `str` | Export a deck to a CSV file |
| `import_deck_json` | `(filepath)` | `Deck` | Import a deck from a JSON file |
| `import_deck_csv` | `(filepath)` | `Deck` | Import a deck from a CSV file |

<br/>

---

<br/>

## ⚙️ Configuration

All settings live in `config.yaml` at the project root:

```yaml
# ──────────────────────────────────────────────────
# Flashcard Creator Configuration
# ──────────────────────────────────────────────────

llm:
  temperature: 0.7             # LLM creativity (0.0 = deterministic, 1.0 = creative)
  max_tokens: 4096             # Maximum response length from the model

flashcards:
  default_count: 10            # Cards generated per request (if not specified)
  default_difficulty: "medium" # Default difficulty level (easy | medium | hard)
  max_cards_per_deck: 500      # Safety limit to prevent oversized decks

spaced_repetition:
  algorithm: "sm2"             # Spaced repetition algorithm (only sm2 supported)
  initial_ease_factor: 2.5     # Starting ease factor for new cards
  minimum_ease_factor: 1.3     # Floor — ease factor never drops below this
  initial_interval: 1          # Days before first review
  graduating_interval: 6       # Days after second consecutive correct answer

storage:
  decks_dir: "./decks"         # Directory where deck JSON files are saved
  stats_file: "review_stats.json"

logging:
  level: "INFO"                # Logging level: DEBUG, INFO, WARNING, ERROR
  file: "flashcard_creator.log"
```

<br/>

### Environment Variables

Override defaults with environment variables (see `.env.example`):

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `gemma3` | Model to use for generation |
| `LOG_LEVEL` | `INFO` | Logging verbosity |
| `DECKS_DIR` | `./decks` | Deck storage directory |

<br/>

### `ConfigManager` API

```python
from flashcard_creator.core import ConfigManager

cfg = ConfigManager()                       # auto-discovers config.yaml
cfg = ConfigManager("path/to/config.yaml")  # explicit path

# Access any setting with section.key and a fallback
temperature = cfg.get("llm", "temperature", 0.7)
max_cards   = cfg.get("flashcards", "max_cards_per_deck", 500)
ease_floor  = cfg.get("spaced_repetition", "minimum_ease_factor", 1.3)
```

<br/>

---

<br/>

## 🧪 Testing

Tests are written with **pytest** and mock the LLM client, so they run
**without Ollama**.

```bash
# Run all tests with verbose output
python -m pytest tests/ -v --tb=short

# Run with coverage report
python -m pytest tests/ --cov=src/flashcard_creator --cov-report=term-missing

# Run only core logic tests (SM-2, deck management, import/export)
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v
```

### What's tested

| Module | Test file | Coverage |
|--------|-----------|----------|
| SM-2 algorithm (`SpacedRepetition`) | `test_core.py` | Quality grades 0–5, ease factor bounds, interval progression |
| Deck CRUD (`DeckManager`) | `test_core.py` | Create, delete, list, get, add/remove cards, merge |
| Import / Export | `test_core.py` | JSON round-trip, CSV round-trip, edge cases |
| Review sessions (`ReviewSession`) | `test_core.py` | Score calculation, shuffle, due-only filtering |
| CLI commands | `test_cli.py` | All 6 commands via Click's `CliRunner` |

<br/>

---

<br/>

## 🤖 Local LLM vs Cloud AI

| | **Flashcard Creator (Local)** | **Cloud-Based Tools** |
|---|---|---|
| **Privacy** | ✅ All data stays on your machine | ❌ Study data sent to third-party servers |
| **Cost** | ✅ Free forever — no subscription | ❌ Monthly fees ($5–$20/month) |
| **Offline** | ✅ Works without internet | ❌ Requires constant connectivity |
| **Speed** | ✅ Local inference — no network latency | ⚠️ Depends on API response time |
| **Customisation** | ✅ Swap models, tune temperature, fork the code | ❌ Limited to vendor's feature set |
| **Data Format** | ✅ Plain JSON / CSV — fully portable | ⚠️ Proprietary formats, difficult export |
| **Model Choice** | ✅ Gemma 3, Llama 3, Mistral, or any Ollama model | ❌ Locked to provider's model |

<br/>

---

<br/>

## 🧠 Spaced Repetition — SM-2 Deep Dive

The SM-2 algorithm was developed by Piotr Wozniak and is the foundation of
tools like Anki.  Flashcard Creator implements it in `SpacedRepetition`.

### Quality Grades

After each card review, you rate your recall:

| Grade | Meaning | Effect |
|-------|---------|--------|
| **0** | Complete blackout | Reset repetitions, interval → 1 day |
| **1** | Incorrect — remembered after seeing answer | Reset repetitions, interval → 1 day |
| **2** | Incorrect — answer seemed easy to recall | Reset repetitions, interval → 1 day |
| **3** | Correct with serious difficulty | Increment repetitions, adjust interval |
| **4** | Correct with some hesitation | Increment repetitions, adjust interval |
| **5** | Perfect recall | Increment repetitions, adjust interval |

### Ease Factor Formula

```
EF' = EF + (0.1 − (5 − q) × (0.08 + (5 − q) × 0.02))
```

Where `EF` is the current ease factor and `q` is the quality grade (0–5).
The ease factor is clamped to a minimum of **1.3** (configurable via
`spaced_repetition.minimum_ease_factor`).

### Interval Progression

| Repetition | Interval | Notes |
|------------|----------|-------|
| 0 (first review) | 1 day | `initial_interval` from config |
| 1 (second review) | 6 days | `graduating_interval` from config |
| n ≥ 2 | `previous_interval × EF` | Exponential growth based on ease |
| Failed (quality < 3) | 1 day | Repetitions reset to 0 |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>How many flashcards can I generate at once?</strong></summary>

By default, the LLM generates up to the `default_count` in your config (10).
You can override this with `--count`. The `max_cards_per_deck` setting (500)
is a safety limit for deck size, not a per-generation cap.
</details>

<details>
<summary><strong>Can I use a different model instead of Gemma 3?</strong></summary>

Yes! Any model available via Ollama works. Set `OLLAMA_MODEL` in your
`.env` file or pass it through the `common/llm_client.py` configuration.
Popular choices include `llama3`, `mistral`, `phi3`, and `codellama`.
</details>

<details>
<summary><strong>What happens if I rate a card incorrectly (quality 0–2)?</strong></summary>

The SM-2 algorithm resets the card's repetition count to 0 and sets its
interval back to 1 day. The ease factor is also reduced, making the card
appear more frequently in future reviews until you consistently recall it.
</details>

<details>
<summary><strong>Can I share decks with friends or import from Anki?</strong></summary>

You can export any deck as JSON or CSV (`flashcard-creator export-deck`),
share the file, and have others import it (`flashcard-creator import-deck`).
For Anki imports, export your Anki deck as CSV first, then import it here.
</details>

<details>
<summary><strong>Does the web UI support all CLI features?</strong></summary>

Yes. The web UI (Streamlit) uses the same `core.py` engine as the CLI.
Decks created in the CLI appear in the web UI and vice versa. Both interfaces
support card creation, review with SM-2, deck management, and statistics.
</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/flashcard-creator.git
cd flashcard-creator

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install in development mode with test dependencies
pip install -e ".[dev]"

# Run the test suite
python -m pytest tests/ -v
```

### Guidelines

1. **Fork** the repository and create a feature branch.
2. **Write tests** for any new functionality.
3. **Run the full test suite** before submitting a PR.
4. **Follow the existing code style** — the project uses standard Python conventions.
5. **Update documentation** if you add new commands or configuration options.

### Areas for Contribution

- 🎨 **Web UI enhancements** — dark mode toggle, card editor improvements
- 📊 **Statistics visualisations** — charts, heatmaps, progress graphs
- 🧠 **Additional algorithms** — Leitner system, FSRS
- 🌍 **Internationalisation** — multi-language support
- 📱 **Mobile-friendly UI** — responsive Streamlit layout
- 🔌 **Integrations** — Anki import, Quizlet import, Notion export

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE)
file for details.

You are free to use, modify, and distribute this software for any purpose.

<br/>

---

<br/>

<div align="center">

  **Project #52** of the
  <a href="https://github.com/kennedyraju55/90-local-llm-projects"><strong>90 Local LLM Projects</strong></a>
  collection.

  <br/><br/>

  Built with ❤️ using **Gemma 3**, **Ollama**, **Python**, and **Streamlit**.

  <br/>

  <sub>If you found this useful, consider giving the repo a ⭐</sub>

</div>
