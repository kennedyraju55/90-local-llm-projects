<div align="center">

<!-- Hero Banner -->
<img src="docs/banner.png" alt="Study Buddy Bot Banner" width="800"/>

<br/>

# 📚 Study Buddy Bot

### Your AI-Powered Personal Tutor — Powered by Local LLMs

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Model](https://img.shields.io/badge/Model-Gemma_4-4361ee?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

*Generate quizzes, flashcards, study plans, and concept explanations — all running locally on your machine with zero cloud dependency.*

[Quick Start](#-quick-start) •
[Features](#-features) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[FAQ](#-faq)

</div>

---

## 💡 Why This Project?

Traditional study methods often fall short. **Study Buddy Bot** tackles the most common challenges students face — powered by a local LLM that understands your subject matter deeply.

| Challenge | How Study Buddy Bot Solves It |
|---|---|
| 📖 **Passive reading doesn't stick** | Active recall through generated quizzes and flashcards forces retrieval practice |
| 🤯 **Complex topics feel overwhelming** | The Feynman Technique breaks concepts into simple, digestible explanations |
| 📅 **No structure to study sessions** | Auto-generated multi-day study plans with topic scheduling and milestones |
| ⏱️ **Losing track of time** | Built-in Pomodoro timer keeps sessions focused with enforced breaks |
| 📊 **No visibility into progress** | Statistics dashboard tracks sessions, time spent, and mastery by subject |

> **Privacy first** — your study data never leaves your machine. Everything runs locally via Ollama + Gemma 4.

---

## ✨ Features

<div align="center">

```svg
<svg width="720" height="120" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="feat" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4361ee;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#7209b7;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="720" height="120" rx="16" fill="url(#feat)"/>
  <text x="360" y="45" text-anchor="middle" fill="white" font-size="22" font-weight="bold" font-family="Segoe UI, sans-serif">
    Study Buddy Bot — Feature Overview
  </text>
  <text x="360" y="80" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="15" font-family="Segoe UI, sans-serif">
    5 Study Modes • Flashcard System • Pomodoro Timer • Progress Analytics
  </text>
</svg>
```

</div>

| 🎯 Study Modes | 🃏 Flashcard System |
|---|---|
| 5 modes: **Quiz**, **Explain**, **Plan**, **Summarize**, **Flashcards** — each tailored to a different learning style. Generate mixed-type questions, multi-day plans, or detailed concept breakdowns on any subject. | Generate 5–20 Q&A flashcard pairs per topic. Save sets locally to `flashcards.json`, reload them anytime, and practice with spaced repetition principles baked in. |

| ⏱️ Pomodoro Timer | 📊 Progress Analytics |
|---|---|
| Customizable focus sessions (5–60 min) with automatic break scheduling. Default: 25 min focus / 5 min break. Tracks elapsed time and keeps you in flow state. | Dashboard view of total study time, sessions completed, and per-subject breakdowns. All progress persisted to `study_progress.json` for long-term tracking. |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM serving |
| Gemma 4 | Via Ollama | Language model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/study-buddy-bot.git
cd study-buddy-bot

# 2. Create and activate a virtual environment
python -m venv .venv

# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure Ollama is running with Gemma 4
ollama pull gemma4
ollama serve
```

### First Run

```bash
# Generate a detailed explanation of Quantum Mechanics
study --subject "Physics" --topic "Quantum Mechanics" --mode explain
```

**Expected output:**

```
📚 Study Buddy Bot — Explain Mode
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Subject: Physics
Topic:   Quantum Mechanics

🔬 Concept Explanation
──────────────────────
Quantum Mechanics is the branch of physics that describes the behavior
of matter and energy at the atomic and subatomic scale...

💡 Key Takeaways
  • Wave-particle duality: particles exhibit both wave and particle properties
  • Heisenberg Uncertainty Principle: position and momentum cannot both be known precisely
  • Quantum superposition: particles exist in multiple states until observed
  ...

🌍 Real-World Analogy
  Think of a coin spinning in the air — it's neither heads nor tails
  until it lands. That's superposition in everyday terms.
```

### Launch the Web UI

```bash
streamlit run src/study_buddy_bot/app.py
```

Opens at `http://localhost:8501` with all 5 tabs ready.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/study-buddy-bot.git
cd study-buddy-bot
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
uvicorn src.study_buddy.api:app --reload --port 8000

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

Study Buddy Bot provides a multi-command CLI for terminal-based studying.

### `study` — Generate Study Content

```bash
study --subject <SUBJECT> --topic <TOPIC> [--mode <MODE>]
```

| Flag | Required | Default | Description |
|---|---|---|---|
| `--subject` | ✅ | — | Subject area (e.g., "Physics", "History") |
| `--topic` | ✅ | — | Specific topic within the subject |
| `--mode` | ❌ | `explain` | Study mode: `quiz`, `explain`, `plan`, `summarize`, `flashcards` |

**Examples:**

```bash
# Generate a quiz on organic chemistry
study --subject "Chemistry" --topic "Organic Chemistry" --mode quiz

# Create a 7-day study plan for calculus
study --subject "Mathematics" --topic "Calculus" --mode plan

# Get a concise summary of the French Revolution
study --subject "History" --topic "French Revolution" --mode summarize

# Generate flashcards for biology
study --subject "Biology" --topic "Cell Division" --mode flashcards
```

### `timer` — Pomodoro Focus Timer

```bash
timer [--minutes <MINUTES>]
```

| Flag | Required | Default | Description |
|---|---|---|---|
| `--minutes` | ❌ | `25` | Duration of the focus session in minutes (5–60) |

**Examples:**

```bash
# Default 25-minute Pomodoro session
timer

# Short 15-minute review session
timer --minutes 15

# Extended 45-minute deep study session
timer --minutes 45
```

### `stats` — View Study Statistics

```bash
stats
```

Displays an overview of your study activity:

```
📊 Study Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Total Sessions: 42
Total Time:     18h 30m

By Subject:
  Physics        ██████████████░░░░░░  12 sessions (5h 15m)
  Mathematics    ████████████░░░░░░░░  10 sessions (4h 30m)
  Chemistry      ████████░░░░░░░░░░░░   8 sessions (3h 45m)
  History        ██████░░░░░░░░░░░░░░   7 sessions (3h 00m)
  Biology        ████░░░░░░░░░░░░░░░░   5 sessions (2h 00m)
```

### `flashcard-list` — List Saved Flashcard Sets

```bash
flashcard-list
```

Shows all flashcard sets stored in `flashcards.json`:

```
🃏 Saved Flashcard Sets
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Physics / Quantum Mechanics     — 10 cards
2. Chemistry / Organic Chemistry   — 15 cards
3. Biology / Cell Division         — 8 cards
4. Mathematics / Linear Algebra    — 12 cards
```

---

## 🌐 Web UI

The Streamlit-based web interface provides **5 tabs** for a complete study experience.

### Tab Overview

| Tab | Icon | Description |
|---|---|---|
| **Study** | 📖 | Generate study content with any mode + interactive follow-up Q&A |
| **Quiz** | 🧠 | Generate quizzes with 3–15 mixed-type questions and instant grading |
| **Flashcards** | 🃏 | Generate 5–20 flashcards, save sets, and review saved collections |
| **Timer** | ⏱️ | Pomodoro timer with 5–60 minute sessions and break scheduling |
| **Progress** | 📊 | Statistics dashboard with per-subject breakdowns and session history |

### 📖 Study Tab

- Select a **subject** and **topic**
- Choose a **study mode** (quiz, explain, plan, summarize, flashcards)
- View generated content in a formatted display
- Ask **follow-up questions** in the interactive Q&A section
- Conversation history is maintained within the session

### 🧠 Quiz Tab

- Configure **3–15 questions** per quiz
- Mixed question types: multiple choice, true/false, short answer
- Submit answers and receive **instant feedback** with explanations
- Questions are generated fresh each time from the LLM

### 🃏 Flashcards Tab

- Generate **5–20 flashcards** per topic
- Each card has a **question** (front) and **answer** (back)
- **Save** generated sets to `flashcards.json` for later review
- **Browse** and review previously saved flashcard collections
- Flip-card interface for self-testing

### ⏱️ Timer Tab

- Set focus duration: **5–60 minutes** (default: 25)
- Visual countdown with progress indicator
- Automatic **break reminders** (default: 5 min break)
- Session time is recorded to your study progress

### 📊 Progress Tab

- **Total sessions** and **total study time** at a glance
- Per-subject breakdown with session counts and time spent
- Visual bar charts for study distribution
- Data loaded from `study_progress.json`

---

## 🏗️ Architecture

### System Flow

```svg
<svg width="720" height="280" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="arch" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#4361ee;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#3a0ca3;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="720" height="280" rx="16" fill="#0d1117"/>
  <!-- Boxes -->
  <rect x="20" y="30" width="140" height="60" rx="10" fill="url(#arch)" opacity="0.9"/>
  <text x="90" y="65" text-anchor="middle" fill="white" font-size="14" font-weight="bold" font-family="monospace">CLI / Web UI</text>

  <rect x="200" y="30" width="140" height="60" rx="10" fill="url(#arch)" opacity="0.9"/>
  <text x="270" y="58" text-anchor="middle" fill="white" font-size="13" font-weight="bold" font-family="monospace">study_buddy_bot</text>
  <text x="270" y="75" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="monospace">core module</text>

  <rect x="380" y="30" width="140" height="60" rx="10" fill="url(#arch)" opacity="0.9"/>
  <text x="450" y="65" text-anchor="middle" fill="white" font-size="14" font-weight="bold" font-family="monospace">Ollama API</text>

  <rect x="560" y="30" width="140" height="60" rx="10" fill="url(#arch)" opacity="0.9"/>
  <text x="630" y="58" text-anchor="middle" fill="white" font-size="14" font-weight="bold" font-family="monospace">Gemma 4</text>
  <text x="630" y="75" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="11" font-family="monospace">Local LLM</text>

  <!-- Arrows -->
  <line x1="160" y1="60" x2="200" y2="60" stroke="#4361ee" stroke-width="2" marker-end="url(#arrow)"/>
  <line x1="340" y1="60" x2="380" y2="60" stroke="#4361ee" stroke-width="2"/>
  <line x1="520" y1="60" x2="560" y2="60" stroke="#4361ee" stroke-width="2"/>

  <!-- Storage -->
  <rect x="200" y="140" width="140" height="50" rx="10" fill="#1a1a2e" stroke="#4361ee" stroke-width="1.5"/>
  <text x="270" y="170" text-anchor="middle" fill="#4361ee" font-size="12" font-family="monospace">flashcards.json</text>

  <rect x="380" y="140" width="160" height="50" rx="10" fill="#1a1a2e" stroke="#4361ee" stroke-width="1.5"/>
  <text x="460" y="170" text-anchor="middle" fill="#4361ee" font-size="12" font-family="monospace">study_progress.json</text>

  <rect x="200" y="220" width="140" height="40" rx="10" fill="#1a1a2e" stroke="#4361ee" stroke-width="1.5"/>
  <text x="270" y="245" text-anchor="middle" fill="#4361ee" font-size="12" font-family="monospace">config.yaml</text>

  <line x1="270" y1="90" x2="270" y2="140" stroke="#4361ee" stroke-width="1.5" stroke-dasharray="5,5"/>
  <line x1="270" y1="190" x2="270" y2="220" stroke="#4361ee" stroke-width="1.5" stroke-dasharray="5,5"/>
  <line x1="340" y1="90" x2="460" y2="140" stroke="#4361ee" stroke-width="1.5" stroke-dasharray="5,5"/>
</svg>
```

### Request Flow

```
User Input ──▶ CLI / Web UI ──▶ study_buddy_bot (core) ──▶ Ollama API ──▶ Gemma 4
                                      │                                      │
                                      │◀─────── Generated Content ◀──────────│
                                      │
                                      ├──▶ flashcards.json   (save/load flashcard sets)
                                      ├──▶ study_progress.json (record sessions & stats)
                                      └──▶ config.yaml        (model & app settings)
```

### Project Structure

```
09-study-buddy-bot/
├── src/
│   └── study_buddy_bot/
│       ├── __init__.py          # Package initialization
│       ├── app.py               # Streamlit web UI (5 tabs)
│       ├── core.py              # Core functions (quiz, explain, plan, etc.)
│       ├── cli.py               # CLI entry points (study, timer, stats, flashcard-list)
│       └── utils.py             # File I/O helpers (load/save flashcards & progress)
├── tests/
│   ├── test_core.py             # Unit tests for core functions
│   ├── test_cli.py              # CLI integration tests
│   └── test_utils.py            # Utility function tests
├── common/                      # Shared utilities across projects
├── docs/                        # Documentation assets
├── config.yaml                  # Application configuration
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
├── Makefile                     # Build & run shortcuts
├── .env.example                 # Environment variable template
└── .gitignore                   # Git ignore rules
```

---

## 📘 API Reference

All core functions live in `src/study_buddy_bot/core.py`.

### `generate_quiz(subject, topic, num_questions)`

Generate a quiz with mixed question types for any subject and topic.

```python
from study_buddy_bot.core import generate_quiz

# Generate a 10-question quiz on thermodynamics
quiz = generate_quiz(
    subject="Physics",
    topic="Thermodynamics",
    num_questions=10
)

# quiz contains a list of question objects with:
# - question text
# - question type (multiple_choice, true_false, short_answer)
# - answer options (for multiple choice)
# - correct answer
# - explanation
for q in quiz["questions"]:
    print(f"Q: {q['question']}")
    print(f"A: {q['correct_answer']}\n")
```

### `explain_concept(subject, topic, depth)`

Get a detailed or summary explanation of any concept.

```python
from study_buddy_bot.core import explain_concept

# Detailed explanation
explanation = explain_concept(
    subject="Biology",
    topic="Photosynthesis",
    depth="detailed"
)
print(explanation["content"])
print(explanation["key_takeaways"])
print(explanation["analogy"])

# Summary explanation
summary = explain_concept(
    subject="Biology",
    topic="Photosynthesis",
    depth="summary"
)
print(summary["content"])
```

### `create_study_plan(subject, topic, days)`

Generate a structured multi-day study plan with daily objectives.

```python
from study_buddy_bot.core import create_study_plan

# Create a 7-day study plan for calculus
plan = create_study_plan(
    subject="Mathematics",
    topic="Calculus",
    days=7
)

for day in plan["schedule"]:
    print(f"Day {day['day']}: {day['title']}")
    print(f"  Objectives: {', '.join(day['objectives'])}")
    print(f"  Duration: {day['estimated_time']}\n")
```

### `generate_flashcards(subject, topic, count)`

Create Q&A flashcard pairs for study and review.

```python
from study_buddy_bot.core import generate_flashcards

# Generate 15 flashcards on organic chemistry
cards = generate_flashcards(
    subject="Chemistry",
    topic="Organic Chemistry",
    count=15
)

for card in cards["flashcards"]:
    print(f"Q: {card['question']}")
    print(f"A: {card['answer']}\n")
```

### `ask_question(subject, topic, question, history)`

Ask follow-up questions with conversation history for context-aware responses.

```python
from study_buddy_bot.core import ask_question

# Initial question
history = []
response = ask_question(
    subject="Physics",
    topic="Quantum Mechanics",
    question="What is wave-particle duality?",
    history=history
)
print(response["answer"])

# Follow-up question with history
history.append({"role": "user", "content": "What is wave-particle duality?"})
history.append({"role": "assistant", "content": response["answer"]})

follow_up = ask_question(
    subject="Physics",
    topic="Quantum Mechanics",
    question="Can you give me a real-world example?",
    history=history
)
print(follow_up["answer"])
```

### `save_flashcard_set(subject, topic, cards)`

Persist a generated flashcard set to local storage.

```python
from study_buddy_bot.core import save_flashcard_set

# Save flashcards for later review
save_flashcard_set(
    subject="History",
    topic="World War II",
    cards=[
        {"question": "When did WWII begin?", "answer": "September 1, 1939"},
        {"question": "When did WWII end?", "answer": "September 2, 1945"},
    ]
)
```

### `get_flashcard_set(subject, topic)`

Retrieve a previously saved flashcard set.

```python
from study_buddy_bot.core import get_flashcard_set

# Load saved flashcards
cards = get_flashcard_set(
    subject="History",
    topic="World War II"
)

if cards:
    for card in cards:
        print(f"Q: {card['question']}")
        print(f"A: {card['answer']}\n")
```

### `record_study_session(subject, topic, mode, duration_minutes)`

Record a completed study session for progress tracking.

```python
from study_buddy_bot.core import record_study_session

# Record a 25-minute quiz session
record_study_session(
    subject="Physics",
    topic="Thermodynamics",
    mode="quiz",
    duration_minutes=25
)
```

### `get_study_stats()`

Retrieve aggregated study statistics across all subjects.

```python
from study_buddy_bot.core import get_study_stats

stats = get_study_stats()

print(f"Total Sessions: {stats['total_sessions']}")
print(f"Total Time: {stats['total_minutes']} minutes")

for subject, data in stats["by_subject"].items():
    print(f"  {subject}: {data['sessions']} sessions, {data['minutes']} min")
```

---

## 📚 Study Modes

Study Buddy Bot supports **5 distinct study modes**, each designed for a specific learning strategy.

| Mode | Command Flag | Description | Best For |
|---|---|---|---|
| 🧠 **Quiz** | `--mode quiz` | Generates mixed-type questions (multiple choice, true/false, short answer) with answers and explanations | Testing knowledge retention and identifying gaps |
| 📖 **Explain** | `--mode explain` | Produces detailed concept explanations with key takeaways, analogies, and real-world examples | Understanding new or complex topics deeply |
| 📅 **Plan** | `--mode plan` | Creates a multi-day study schedule with daily objectives, time estimates, and milestones | Structuring long-term study for exams or courses |
| 📝 **Summarize** | `--mode summarize` | Delivers concise topic summaries highlighting the most important points | Quick review before exams or refreshing memory |
| 🃏 **Flashcards** | `--mode flashcards` | Generates Q&A pairs optimized for spaced repetition and active recall | Memorizing facts, definitions, and key concepts |

### Mode Selection Guide

```
Need to test yourself?        → quiz
Need to understand something? → explain
Need a study schedule?        → plan
Need a quick refresher?       → summarize
Need to memorize facts?       → flashcards
```

---

## 🧑‍🏫 Teaching Methodology

Study Buddy Bot incorporates four evidence-based learning techniques into its content generation.

### 🔬 Feynman Technique

The Feynman Technique is at the heart of every explanation. Concepts are broken down as if teaching them to someone with no background knowledge:

1. **Identify** the concept
2. **Explain** it in simple, plain language
3. **Identify gaps** where the explanation breaks down
4. **Simplify** further using analogies and everyday examples

> *"If you can't explain it simply, you don't understand it well enough."* — Richard Feynman

### 🧠 Active Recall

Instead of passively reading, Study Buddy Bot forces you to **retrieve information from memory**:

- **Quizzes** require you to answer from memory before seeing the correct answer
- **Flashcards** present questions first, hiding answers until you've attempted a response
- **Follow-up Q&A** challenges you to articulate your understanding

Research shows that active recall improves long-term retention by up to **150%** compared to passive review.

### 🔄 Spaced Repetition

The flashcard system is designed to support spaced repetition workflows:

- **Save** flashcard sets and revisit them across multiple study sessions
- **Track** which subjects you've studied and when via the progress system
- **Plan** mode generates multi-day schedules that naturally space out topic reviews

### 🧩 Mnemonics & Memory Aids

Generated content includes memory aids where appropriate:

- **Acronyms** for lists and sequences
- **Visual analogies** connecting abstract concepts to concrete images
- **Story-based mnemonics** that make facts memorable
- **Real-world examples** that anchor learning to familiar experiences

---

## ⚙️ Configuration

All settings are managed in `config.yaml`:

```yaml
# Language Model Configuration
llm:
  model: gemma4                # Ollama model name
  temperature: 0.7             # Creativity level (0.0 = deterministic, 1.0 = creative)
  max_tokens: 3072             # Maximum response length

# Available Study Modes
modes:
  - quiz
  - explain
  - plan
  - summarize
  - flashcards

# Pomodoro Timer Settings
timer:
  default_minutes: 25          # Default focus session length
  break_minutes: 5             # Break duration between sessions

# Progress Tracking
progress:
  storage_file: study_progress.json

# Flashcard Storage
flashcards_storage:
  storage_file: flashcards.json
```

### Configuration Options

| Key | Type | Default | Description |
|---|---|---|---|
| `llm.model` | string | `gemma4` | Ollama model to use for generation |
| `llm.temperature` | float | `0.7` | Controls randomness (lower = more focused) |
| `llm.max_tokens` | int | `3072` | Max tokens per LLM response |
| `timer.default_minutes` | int | `25` | Default Pomodoro session length |
| `timer.break_minutes` | int | `5` | Break duration between focus sessions |
| `progress.storage_file` | string | `study_progress.json` | File path for progress data |
| `flashcards_storage.storage_file` | string | `flashcards.json` | File path for flashcard data |

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test modules
pytest tests/test_core.py -v
pytest tests/test_cli.py -v
pytest tests/test_utils.py -v

# Run with coverage
pytest tests/ --cov=study_buddy_bot --cov-report=term-missing

# Run using Makefile
make test
```

### Test Structure

| File | Covers |
|---|---|
| `tests/test_core.py` | `generate_quiz`, `explain_concept`, `create_study_plan`, `generate_flashcards`, `ask_question`, `save_flashcard_set`, `get_flashcard_set`, `record_study_session`, `get_study_stats` |
| `tests/test_cli.py` | CLI commands: `study`, `timer`, `stats`, `flashcard-list` |
| `tests/test_utils.py` | `load_saved_flashcards`, `save_flashcards_data`, `load_study_progress`, `save_study_progress` |

---

## 🤖 Local LLM vs Cloud AI

| Aspect | Local LLM (This Project) | Cloud AI |
|---|---|---|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to external servers |
| **Cost** | ✅ Free after hardware setup | ❌ Pay per API call |
| **Latency** | ⚡ No network round-trip | 🌐 Depends on connection |
| **Availability** | ✅ Works offline | ❌ Requires internet |
| **Model Quality** | 🟡 Good (Gemma 4) | 🟢 Excellent (GPT-4, Claude) |
| **Customization** | ✅ Full control over model & prompts | 🟡 Limited to API parameters |
| **Hardware** | ❌ Requires capable GPU/CPU | ✅ Runs on any device |

### Why Gemma 4?

- **Open-weight** model from Google — free to use locally
- **Strong reasoning** capabilities for educational content
- **Efficient** — runs well on consumer hardware via Ollama
- **Multilingual** support for studying in multiple languages

---

## ❓ FAQ

<details>
<summary><strong>Are there any subject limits? Can I study anything?</strong></summary>

Study Buddy Bot works with **any subject** you provide. The `--subject` and `--topic` parameters accept free-form text, so you can study physics, history, programming, music theory, cooking, or any other topic. The quality of generated content depends on the underlying LLM's knowledge of the subject. Gemma 4 performs well across a broad range of academic and general-knowledge topics.

</details>

<details>
<summary><strong>Can I import flashcards from other apps (Anki, Quizlet)?</strong></summary>

Not directly. Study Buddy Bot stores flashcards in a simple JSON format in `flashcards.json`. However, you can manually convert exported flashcard files to the expected format:

```json
{
  "Physics_Quantum Mechanics": [
    {"question": "What is superposition?", "answer": "A quantum state where..."},
    {"question": "What is entanglement?", "answer": "A phenomenon where..."}
  ]
}
```

Each set is keyed by `{subject}_{topic}` and contains an array of `{"question": ..., "answer": ...}` objects. You can write a small script to convert Anki `.apkg` or Quizlet CSV exports into this format.

</details>

<details>
<summary><strong>Can I customize the Pomodoro timer beyond the defaults?</strong></summary>

Yes. You can customize the timer in two ways:

1. **CLI**: Pass `--minutes` to set any duration from 5 to 60 minutes:
   ```bash
   timer --minutes 45
   ```

2. **Config**: Edit `config.yaml` to change the defaults:
   ```yaml
   timer:
     default_minutes: 30    # Change default from 25 to 30
     break_minutes: 10      # Change break from 5 to 10
   ```

3. **Web UI**: Use the slider in the Timer tab to set any value between 5 and 60 minutes.

</details>

<details>
<summary><strong>How do I control quiz difficulty?</strong></summary>

Quiz difficulty is influenced by two factors:

1. **Topic specificity**: More specific topics yield harder questions. Compare:
   - Easy: `--topic "Basic Algebra"`
   - Hard: `--topic "Abstract Algebra — Group Theory"`

2. **LLM temperature**: Lower temperature produces more focused, fact-based questions. Higher temperature introduces more creative, challenging scenarios. Adjust in `config.yaml`:
   ```yaml
   llm:
     temperature: 0.3   # More factual, straightforward questions
     temperature: 0.9   # More creative, challenging questions
   ```

The `num_questions` parameter (3–15 in the Web UI) controls quantity, not difficulty.

</details>

<details>
<summary><strong>How do I reset my study progress?</strong></summary>

To reset all progress, simply delete the storage files:

```bash
# Reset study progress
rm study_progress.json

# Reset saved flashcards
rm flashcards.json
```

Both files will be automatically recreated (empty) on the next run. To reset only a specific subject, edit the JSON files directly and remove the relevant entries.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make** your changes and add tests
4. **Run** the test suite:
   ```bash
   pytest tests/ -v
   ```
5. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add spaced repetition scheduling"
   ```
6. **Push** and open a Pull Request:
   ```bash
   git push origin feature/your-feature-name
   ```

### Development Setup

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Run linting
make lint

# Run tests with coverage
make test-cov
```

### Areas for Contribution

- 🌍 **Internationalization** — Multi-language UI support
- 📱 **Mobile-friendly UI** — Responsive Streamlit layout improvements
- 🔌 **Export formats** — Anki `.apkg`, CSV, PDF export for flashcards and study plans
- 📈 **Advanced analytics** — Spaced repetition scheduling, mastery scores, streaks
- 🧪 **Test coverage** — Additional edge case and integration tests

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ for learners everywhere**

<sub>Part of the [Local LLM Projects](https://github.com/kennedyraju55) collection — Project 09</sub>

<br/>

<a href="#-study-buddy-bot">⬆ Back to Top</a>

</div>
