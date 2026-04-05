<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- 📖 VOCABULARY BUILDER — Portfolio-Grade README                        -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

<!-- Hero Banner -->
<img src="docs/images/banner.svg" alt="Vocabulary Builder Banner" width="800"/>

<br/>
<br/>

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma_3-f4a261?style=for-the-badge&logo=meta&logoColor=white)](https://ollama.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Click](https://img.shields.io/badge/Click-CLI-2a9d8f?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-e9c46a?style=for-the-badge)](LICENSE)
[![Tests](https://img.shields.io/badge/Tests-Passing-2a9d8f?style=for-the-badge&logo=pytest&logoColor=white)](tests/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br/>

**Build your vocabulary with AI-powered etymology, mnemonics, spaced repetition, and interactive quizzes — all running locally on your machine.**

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Architecture](#-architecture) •
[Configuration](#%EF%B8%8F-configuration)

<br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Vocabulary learning is one of the most effective use cases for AI. Traditional tools give you a word and a definition — **Vocabulary Builder** gives you the full picture:

| Challenge | Traditional Tools | Vocabulary Builder |
|:----------|:-----------------|:-------------------|
| **Shallow definitions** | Single-line dictionary lookups | Rich metadata: etymology, mnemonics, word families, multiple context sentences |
| **No retention strategy** | Random flashcard order | SM-2 spaced repetition algorithm with adaptive intervals |
| **Cloud dependency** | Requires internet & subscription | 100% local with Ollama — your data never leaves your machine |
| **No topic control** | Pre-built word lists only | Generate vocabulary for any topic: SAT, GRE, medical, legal, tech, literature |
| **Passive learning** | Read-only experience | Interactive quizzes with instant scoring, progress tracking, and streak monitoring |

> 💡 **The science:** Spaced repetition has been shown to improve long-term retention by up to **200%** compared to massed practice ([Cepeda et al., 2006](https://doi.org/10.1111/j.1467-9280.2006.01693.x)). This project implements the proven **SM-2 algorithm** — the same algorithm used by Anki.

<br/>

---

<br/>

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Category | Features | Details |
|:---------|:---------|:--------|
| 🏛️ **Rich Word Data** | Etymology, mnemonics, word families, difficulty levels | Every word comes with its history, a memory trick, related words, and a difficulty rating |
| 🧠 **Spaced Repetition** | SM-2 algorithm, adaptive intervals, ease factor tuning | Cards are reviewed at scientifically optimal intervals that adapt to your performance |
| 🎯 **Quiz Engine** | Definition matching, instant feedback, score tracking | Test your knowledge with interactive quizzes that show mnemonics when you get one wrong |
| 📊 **Progress Stats** | Mastery percentage, average scores, learning streaks | Track how many words you've learned, your quiz performance over time, and daily streaks |

### Additional Highlights

- **💻 Dual Interface** — Rich terminal CLI with colors and formatting **+** full Streamlit web dashboard
- **🃏 Flashcard Mode** — Web UI card-based learning with reveal animations
- **📝 Context Sentences** — Multiple real-world usage examples generated for every word
- **🔄 Synonyms & Antonyms** — Discover related words and build semantic networks
- **⚙️ YAML Configuration** — Centralized config for LLM parameters, spaced repetition tuning, and quiz settings
- **🧪 Fully Tested** — Comprehensive pytest suite covering core logic, spaced repetition, and CLI integration
- **📦 Installable Package** — `pip install -e .` with console script entry point

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://www.python.org/) | ≥ 3.9 | Runtime |
| [Ollama](https://ollama.com/) | Latest | Local LLM inference |
| [Gemma 3](https://ollama.com/library/gemma3) | Any size | Language model |

### Step 1 — Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/vocabulary-builder.git
cd vocabulary-builder

# Install the package with dev dependencies
pip install -e ".[dev]"
```

### Step 2 — Start Ollama

```bash
# Start the Ollama service
ollama serve

# Pull the Gemma 3 model (if not already downloaded)
ollama pull gemma3
```

### Step 3 — Verify Installation

```bash
# Check that the CLI is installed
vocab-builder --help

# Generate your first vocabulary set
vocab-builder learn --topic "SAT words" --count 5
```

### Step 4 — Launch the Web UI (Optional)

```bash
streamlit run src/vocab_builder/web_ui.py
```

> 📌 **Tip:** The CLI and Web UI share the same core engine. Vocabulary files saved from the CLI (`.json`) can be loaded in the Web UI and vice versa.

<br/>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/vocabulary-builder.git
cd vocabulary-builder
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

<br/>


---

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.vocab_builder.api:app --reload --port 8000

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

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and [Rich](https://rich.readthedocs.io/) for a beautiful terminal experience.

### Global Options

```bash
vocab-builder [OPTIONS] COMMAND [ARGS]...
```

| Option | Short | Description |
|:-------|:------|:------------|
| `--verbose` | `-v` | Enable verbose/debug logging |
| `--help` | | Show help message and exit |

---

### `learn` — Generate Vocabulary

Generate a vocabulary set from any topic using the local LLM.

```bash
vocab-builder learn --topic "SAT words" --count 15
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--topic` | `-t` | *(required)* | The vocabulary topic to generate words for |
| `--count` | `-c` | `10` | Number of words to generate |
| `--level` | `-l` | `""` | Target difficulty level (e.g., `beginner`, `advanced`, `GRE`) |
| `--output` | `-o` | `vocab_{topic}.json` | Output file path for the generated vocabulary |

#### Examples

```bash
# Generate 15 SAT words
vocab-builder learn --topic "SAT words" --count 15

# Advanced medical terminology
vocab-builder learn --topic "Medical terminology" --level advanced

# Save to a custom file
vocab-builder learn --topic "GRE words" --output gre_vocab.json

# Beginner-friendly tech vocabulary
vocab-builder learn --topic "Programming concepts" --level beginner --count 20
```

#### Sample Output

```
╭──────────── 📖 Vocabulary Builder ────────────╮
│ SAT words                                      │
│ Level: intermediate | Words: 5                  │
╰────────────────────────────────────────────────╯

ephemeral (adjective)
  Lasting for a very short time; transient.
  Example: "The ephemeral beauty of cherry blossoms draws millions of visitors each spring."
  Etymology: From Greek 'ephemeros' — lasting only a day (epi- 'on' + hemera 'day')
  Synonyms: transient, fleeting, momentary
  Antonyms: permanent, enduring, eternal
  Word Family: ephemerality, ephemerally
  💡 Mnemonic: Think "e-FEM-eral" — like a femme fatale who appears briefly and vanishes

✓ Vocabulary saved to vocab_sat_words.json
```

---

### `quiz` — Test Your Knowledge

Run an interactive vocabulary quiz from a saved vocabulary file.

```bash
vocab-builder quiz --file vocab_sat_words.json
```

| Option | Short | Default | Description |
|:-------|:------|:--------|:------------|
| `--file` | `-f` | *(required)* | Path to a vocabulary JSON file |

#### Examples

```bash
# Quiz from a previously generated file
vocab-builder quiz --file vocab_sat_words.json

# Quiz from GRE vocabulary
vocab-builder quiz --file gre_vocab.json
```

#### Sample Quiz Session

```
╭────── Vocabulary Quiz ──────╮
│ 5 words                      │
│ Type the word that matches   │
│ the definition.              │
╰──────────────────────────────╯

Question 1/5
  Definition: Lasting for a very short time; transient.
  Part of speech: adjective
  Your answer: ephemeral
✓ Correct!

Question 2/5
  Definition: A feeling of listlessness and dissatisfaction.
  Part of speech: noun
  Your answer: ennui
✗ The word is: malaise
  Mnemonic: Think "MAL-aise" — MAL means bad, so it's a bad feeling of unease

╭──── Quiz Results ────╮
│ Score: 4/5 (80%)      │
╰──────────────────────╯
```

<br/>

---

<br/>

## 🌐 Web UI

The Streamlit-based web interface provides a full-featured learning dashboard.

### Launch

```bash
streamlit run src/vocab_builder/web_ui.py
```

The app opens at `http://localhost:8501` with a wide layout and the following modes:

### Modes

| Mode | Description |
|:-----|:------------|
| 📚 **Learn Mode** | Enter a topic and generate vocabulary with definitions, etymology, mnemonics, and context sentences |
| 🎯 **Quiz Mode** | Load a vocabulary file and test your knowledge with instant scoring and feedback |
| 🃏 **Word Cards** | Flashcard-style view with reveal animations — tap to flip and see the definition |
| 📊 **Progress Dashboard** | Track your quiz scores, mastery percentage, and learning streaks over time |

### Web UI Configuration

The Streamlit interface is configured via `config.yaml`:

```yaml
streamlit:
  page_title: "📖 Vocabulary Builder"
  layout: "wide"
```

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="System Architecture" width="800"/>
</div>

<br/>

### How It Works

1. **User** interacts via the **CLI** (terminal) or **Streamlit** (browser)
2. Both interfaces call the **Core Engine** (`core.py`) — the single source of truth for all business logic
3. The Core Engine communicates with **Ollama** running **Gemma 3** locally for vocabulary generation
4. Generated words flow through specialized modules:
   - **Word Generator** — Creates rich word entries with etymology, mnemonics, and word families
   - **Spaced Repetition** — SM-2 algorithm manages review intervals and ease factors
   - **Quiz Engine** — Builds quizzes, scores answers, and provides feedback
   - **Progress Tracker** — Aggregates stats: mastery percentage, average scores, streaks

### Project Structure

```
58-vocabulary-builder/
│
├── src/
│   └── vocab_builder/
│       ├── __init__.py              # Package metadata & exports
│       ├── core.py                  # Business logic, data models, LLM integration
│       │                            #   → WordEntry, VocabularySet, SpacedRepetitionCard
│       │                            #   → generate_vocabulary(), run_quiz(), score_quiz()
│       │                            #   → create_spaced_repetition_deck(), get_due_cards()
│       ├── cli.py                   # Click CLI with Rich formatting
│       │                            #   → learn command, quiz command
│       │                            #   → display_vocabulary(), run_interactive_quiz()
│       └── web_ui.py                # Streamlit web interface
│                                    #   → Learn, Quiz, Flashcards, Progress Dashboard
│
├── tests/
│   ├── test_core.py                 # Unit tests for core logic & spaced repetition
│   └── test_cli.py                  # CLI integration tests
│
├── docs/
│   └── images/
│       ├── banner.svg               # Project hero banner
│       ├── architecture.svg         # System architecture diagram
│       └── features.svg             # Features overview graphic
│
├── common/                          # Shared LLM client (from parent project)
│   └── llm_client.py                # Ollama chat interface
│
├── config.yaml                      # Application configuration
├── setup.py                         # Package installation & entry points
├── requirements.txt                 # Python dependencies
├── Makefile                         # Development task runner
├── .env.example                     # Environment variable template
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

<br/>

---

<br/>

## 📚 API Reference

All public classes and functions are in `vocab_builder.core`.

### Data Models

#### `WordEntry`

A single vocabulary word with all its metadata.

```python
from vocab_builder.core import WordEntry

word = WordEntry(
    word="ephemeral",
    part_of_speech="adjective",
    definition="Lasting for a very short time; transient.",
    example_sentence="The ephemeral beauty of cherry blossoms draws millions.",
    etymology="From Greek 'ephemeros' — lasting only a day",
    synonyms=["transient", "fleeting", "momentary"],
    antonyms=["permanent", "enduring"],
    difficulty="medium",
    mnemonic="e-FEM-eral — like a femme fatale who vanishes quickly",
    word_family=["ephemerality", "ephemerally"],
    context_sentences=[
        "Social media fame is often ephemeral.",
        "The ephemeral nature of trends makes forecasting difficult.",
    ],
)
```

| Field | Type | Default | Description |
|:------|:-----|:--------|:------------|
| `word` | `str` | `""` | The vocabulary word |
| `part_of_speech` | `str` | `""` | Noun, verb, adjective, etc. |
| `definition` | `str` | `""` | Clear definition of the word |
| `example_sentence` | `str` | `""` | A sentence demonstrating usage |
| `etymology` | `str` | `""` | Word origin and historical development |
| `synonyms` | `List[str]` | `[]` | Words with similar meaning |
| `antonyms` | `List[str]` | `[]` | Words with opposite meaning |
| `difficulty` | `str` | `"medium"` | `easy`, `medium`, or `hard` |
| `mnemonic` | `str` | `""` | Memory aid or trick |
| `word_family` | `List[str]` | `[]` | Related words and derivations |
| `context_sentences` | `List[str]` | `[]` | Additional usage examples |

---

#### `VocabularySet`

A collection of words grouped by topic and level.

```python
from vocab_builder.core import VocabularySet

vocab_set = VocabularySet(
    topic="SAT words",
    level="intermediate",
    words=[word],  # list of WordEntry objects
)

# Serialize to dictionary (for JSON export)
data = vocab_set.to_dict()
```

| Field | Type | Default | Description |
|:------|:-----|:--------|:------------|
| `topic` | `str` | `""` | The topic of the vocabulary set |
| `level` | `str` | `""` | Target difficulty level |
| `words` | `List[WordEntry]` | `[]` | The vocabulary words |

| Method | Returns | Description |
|:-------|:--------|:------------|
| `to_dict()` | `dict` | Serializes the entire set (including all words) to a dictionary |

---

#### `SpacedRepetitionCard`

A flashcard that tracks review state using the SM-2 algorithm.

```python
from vocab_builder.core import SpacedRepetitionCard

card = SpacedRepetitionCard(word="ephemeral")

# Simulate a review — quality 0-5 (0=forgot, 5=perfect)
card.update(quality=4)

print(card.interval)      # Days until next review
print(card.ease_factor)   # Current ease factor (starts at 2.5)
print(card.repetitions)   # Number of successful reviews
print(card.next_review)   # Unix timestamp of next review
```

| Field | Type | Default | Description |
|:------|:-----|:--------|:------------|
| `word` | `str` | *(required)* | The word this card represents |
| `interval` | `int` | `1` | Days until next review |
| `ease_factor` | `float` | `2.5` | SM-2 ease factor (minimum 1.3) |
| `repetitions` | `int` | `0` | Count of successful reviews |
| `next_review` | `float` | `0.0` | Unix timestamp for next review |

| Method | Parameters | Description |
|:-------|:-----------|:------------|
| `update(quality)` | `quality: int` (0–5) | Updates interval, ease factor, and next review using SM-2. Quality < 3 resets the card. |

**SM-2 Algorithm Details:**

```
if quality < 3:
    reset repetitions to 0, interval to 1 day
else:
    rep 0 → interval = 1 day
    rep 1 → interval = 6 days
    rep 2+ → interval = interval × ease_factor

ease_factor = max(1.3, EF + 0.1 - (5 - q) × (0.08 + (5 - q) × 0.02))
next_review = now + interval × 86400
```

---

#### `ProgressStats`

Aggregate learning statistics.

```python
from vocab_builder.core import ProgressStats

stats = ProgressStats(
    total_words=50,
    words_learned=35,
    words_reviewing=15,
    quiz_scores=[85.0, 90.0, 75.0, 95.0],
    streak=7,
)

print(f"Mastery: {stats.mastery_pct:.1f}%")   # 70.0%
print(f"Average: {stats.avg_score:.1f}%")      # 86.2%
```

| Field | Type | Default | Description |
|:------|:-----|:--------|:------------|
| `total_words` | `int` | `0` | Total words in the learning set |
| `words_learned` | `int` | `0` | Words fully mastered |
| `words_reviewing` | `int` | `0` | Words still in review |
| `quiz_scores` | `List[float]` | `[]` | History of quiz scores |
| `streak` | `int` | `0` | Current daily learning streak |

| Property | Returns | Description |
|:---------|:--------|:------------|
| `mastery_pct` | `float` | Percentage of words learned (0–100) |
| `avg_score` | `float` | Average of all quiz scores |

---

### Core Functions

#### `generate_vocabulary(topic, count, level) → VocabularySet`

Generate a vocabulary set using the local LLM.

```python
from vocab_builder.core import generate_vocabulary

vocab = generate_vocabulary(
    topic="SAT words",
    count=10,
    level="advanced",
)

for word in vocab.words:
    print(f"{word.word}: {word.definition}")
```

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `topic` | `str` | *(required)* | The topic to generate vocabulary for |
| `count` | `int` | `10` | Number of words to generate |
| `level` | `str` | `""` | Target difficulty level |

---

#### `load_vocab_file(filepath) → VocabularySet`

Load a previously saved vocabulary set from a JSON file.

```python
from vocab_builder.core import load_vocab_file

vocab = load_vocab_file("vocab_sat_words.json")
print(f"Loaded {len(vocab.words)} words about '{vocab.topic}'")
```

---

#### `run_quiz(words) → Dict`

Prepare a quiz from a list of words (non-interactive, returns structure for UI).

```python
from vocab_builder.core import run_quiz

quiz_data = run_quiz(vocab.words)
# {"total": 10, "questions": [{"word": ..., "definition": ..., ...}]}
```

---

#### `score_quiz(answers) → Dict`

Score quiz answers. Each answer is a dict with `word` and `user_answer`.

```python
from vocab_builder.core import score_quiz

results = score_quiz([
    {"word": "ephemeral", "user_answer": "ephemeral"},
    {"word": "ubiquitous", "user_answer": "ubiqitous"},
])
# {"score": 1, "total": 2, "percentage": 50.0}
```

---

#### `create_spaced_repetition_deck(words) → List[SpacedRepetitionCard]`

Create a spaced repetition deck from a list of `WordEntry` objects.

```python
from vocab_builder.core import create_spaced_repetition_deck

deck = create_spaced_repetition_deck(vocab.words)
print(f"Created deck with {len(deck)} cards")
```

---

#### `get_due_cards(deck) → List[SpacedRepetitionCard]`

Get all cards that are due for review (next_review ≤ current time).

```python
from vocab_builder.core import get_due_cards

due = get_due_cards(deck)
print(f"{len(due)} cards due for review")
```

---

#### `check_service() → bool`

Check if the Ollama service is running and accessible.

```python
from vocab_builder.core import check_service

if check_service():
    print("Ollama is running!")
else:
    print("Start Ollama with: ollama serve")
```

<br/>

---

<br/>

## ⚙️ Configuration

All settings are managed in `config.yaml`:

```yaml
# Application Settings
app:
  name: "Vocabulary Builder"
  version: "1.0.0"
  log_level: "INFO"

# LLM Configuration
llm:
  model: "llama3"
  temperature: 0.7          # Higher = more creative word examples
  max_tokens: 8192          # Max response length from the LLM
  base_url: "http://localhost:11434"

# Spaced Repetition Tuning
spaced_repetition:
  initial_interval: 1       # Days before first review
  easy_bonus: 1.3           # Multiplier for easy cards
  graduating_interval: 6    # Days after graduation

# Quiz Settings
quiz:
  default_count: 10         # Default number of quiz questions
  pass_threshold: 80        # Minimum % to pass a quiz

# Streamlit Web UI
streamlit:
  page_title: "📖 Vocabulary Builder"
  layout: "wide"
```

### Key Parameters Explained

| Parameter | Default | Range | Description |
|:----------|:--------|:------|:------------|
| `llm.temperature` | `0.7` | `0.0–1.0` | Controls creativity. Lower = more factual definitions, higher = more varied examples |
| `llm.max_tokens` | `8192` | `1024–32768` | Maximum tokens per LLM response. Increase for larger word sets |
| `spaced_repetition.initial_interval` | `1` | `1–7` | Days before the first review of a new card |
| `spaced_repetition.easy_bonus` | `1.3` | `1.0–2.0` | Extra interval multiplier for cards rated as easy |
| `quiz.pass_threshold` | `80` | `0–100` | Minimum percentage to be considered passing |

<br/>

---

<br/>

## 🧪 Testing

The project includes comprehensive tests using pytest.

### Run All Tests

```bash
# Basic test run
pytest tests/ -v

# With coverage report
pytest tests/ -v --cov=src/vocab_builder --cov-report=term-missing

# Run only core tests
pytest tests/test_core.py -v

# Run only CLI tests
pytest tests/test_cli.py -v
```

### Test Structure

| File | Covers | Description |
|:-----|:-------|:------------|
| `test_core.py` | `core.py` | WordEntry creation, VocabularySet serialization, SM-2 algorithm, quiz scoring, deck creation |
| `test_cli.py` | `cli.py` | CLI command invocation, output formatting, error handling |

### Development Commands (Makefile)

```bash
make test        # Run tests
make lint        # Run linters
make install     # Install package
make clean       # Clean build artifacts
```

<br/>

---

<br/>

## 🏠 Local LLM vs Cloud AI

| Aspect | Vocabulary Builder (Local) | Cloud-Based Tools |
|:-------|:--------------------------|:------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Words & learning data sent to remote servers |
| **Cost** | ✅ Free after setup | ❌ Monthly subscription or per-API-call pricing |
| **Speed** | ✅ No network latency | ❌ Depends on internet speed and server load |
| **Offline** | ✅ Works without internet | ❌ Requires constant connection |
| **Customization** | ✅ Full control over model, prompts, and config | ❌ Limited to provider's interface |
| **Model Choice** | ✅ Swap models anytime (Gemma, Llama, Mistral) | ❌ Locked to provider's model |
| **Data Retention** | ✅ You own all generated vocabulary files | ❌ Data may be used for training |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What models can I use besides Gemma 3?</strong></summary>

<br/>

Any model supported by Ollama works. Update `config.yaml`:

```yaml
llm:
  model: "llama3"      # or "mistral", "phi3", "gemma3", etc.
```

Then pull the model: `ollama pull llama3`

The prompts are model-agnostic — they ask for JSON output, which most instruction-tuned models handle well. Larger models (7B+) tend to produce richer etymology and more creative mnemonics.

</details>

<details>
<summary><strong>How does the SM-2 spaced repetition algorithm work?</strong></summary>

<br/>

SM-2 (SuperMemo 2) is a proven algorithm for optimizing long-term memory:

1. **New cards** start with a 1-day interval
2. **After first successful review** → 6-day interval
3. **Subsequent reviews** → `interval × ease_factor`
4. **Failed reviews** (quality < 3) → reset to 1 day
5. **Ease factor** adjusts based on performance (minimum 1.3)

Rate your recall from 0 (forgot) to 5 (perfect). The algorithm adapts the review schedule to your performance — harder words are shown more frequently, easier words less often.

</details>

<details>
<summary><strong>Can I import my own word lists?</strong></summary>

<br/>

Yes! Create a JSON file matching the vocabulary format:

```json
{
  "topic": "My Custom Words",
  "level": "mixed",
  "words": [
    {
      "word": "serendipity",
      "part_of_speech": "noun",
      "definition": "The occurrence of finding pleasant things by chance.",
      "example_sentence": "It was pure serendipity that they met at the cafe.",
      "etymology": "Coined by Horace Walpole in 1754",
      "synonyms": ["luck", "fortune", "chance"],
      "antonyms": ["misfortune"],
      "difficulty": "medium",
      "mnemonic": "SERENE + DIPITY — a serene dip into good fortune",
      "word_family": ["serendipitous", "serendipitously"],
      "context_sentences": ["The discovery was a moment of serendipity."]
    }
  ]
}
```

Then quiz yourself: `vocab-builder quiz --file my_words.json`

</details>

<details>
<summary><strong>How much disk space does Ollama + Gemma 3 need?</strong></summary>

<br/>

| Component | Size |
|:----------|:-----|
| Ollama | ~200 MB |
| Gemma 3 (2B) | ~1.5 GB |
| Gemma 3 (7B) | ~5 GB |
| Gemma 3 (27B) | ~16 GB |

The 2B model is sufficient for vocabulary generation. Larger models produce more detailed etymologies and creative mnemonics but require more VRAM. For best results on consumer hardware, the 7B model offers the best quality-to-resource ratio.

</details>

<details>
<summary><strong>Can I use this for standardized test prep (SAT, GRE, TOEFL)?</strong></summary>

<br/>

Absolutely! The topic parameter is flexible:

```bash
# SAT preparation
vocab-builder learn --topic "SAT critical reading vocabulary" --count 20 --level advanced

# GRE verbal reasoning
vocab-builder learn --topic "GRE high-frequency words" --count 30 --level advanced

# TOEFL academic vocabulary
vocab-builder learn --topic "TOEFL academic word list" --count 25 --level intermediate

# IELTS band 7+ vocabulary
vocab-builder learn --topic "IELTS advanced academic vocabulary" --count 20
```

The LLM generates words appropriate for each test. Combine with spaced repetition for maximum retention before your exam.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/vocabulary-builder.git
cd vocabulary-builder

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests to verify setup
pytest tests/ -v
```

### Guidelines

1. **Fork** the repository and create a feature branch
2. **Write tests** for new functionality
3. **Run the test suite** before submitting: `pytest tests/ -v`
4. **Follow the existing code style** — the project uses standard Python conventions
5. **Update documentation** if you add new features or change behavior
6. **Submit a pull request** with a clear description of your changes

### Areas for Contribution

- 🌍 **Multi-language support** — vocabulary generation in other languages
- 📈 **Enhanced analytics** — learning curve visualizations, word difficulty analysis
- 🔊 **Audio pronunciation** — text-to-speech integration for word pronunciation
- 📱 **Mobile-friendly UI** — responsive Streamlit layout improvements
- 🧩 **Additional quiz types** — fill-in-the-blank, multiple choice, matching exercises
- 📚 **Pre-built word lists** — curated vocabulary sets for common topics

<br/>

---

<br/>

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose.

<br/>

---

<br/>

<div align="center">

**📖 Vocabulary Builder** — Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection

Built with ❤️ using Python, Ollama, and Gemma 3

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-kennedyraju55-181717?style=flat-square&logo=github)](https://github.com/kennedyraju55)
[![Project](https://img.shields.io/badge/Project-58_of_90-e63946?style=flat-square)](https://github.com/kennedyraju55/90-local-llm-projects)

<br/>

*"A word is dead when it is said, some say. I say it just begins to live that day." — Emily Dickinson*

</div>
