<div align="center">

<!-- Hero Banner -->
<img src="assets/banner.png" alt="Language Learning Bot Banner" width="100%" />

# 🌍 Language Learning Bot

**Your AI-powered polyglot companion — master 15 languages through conversation, vocabulary drills, and structured lessons, all powered by a local LLM.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-gemma4-06d6a0?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Gradio](https://img.shields.io/badge/Gradio-Web_UI-F97316?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-06d6a0?style=for-the-badge)](LICENSE)
[![Languages](https://img.shields.io/badge/Languages-15-06d6a0?style=for-the-badge)](#supported-languages)
[![CLI](https://img.shields.io/badge/CLI-Click-06d6a0?style=for-the-badge)](https://click.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br />

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[Contributing](#-contributing)

<br />

---

</div>

## 💡 Why This Project?

Learning a new language is one of the most rewarding—and most frustrating—endeavors you can undertake. Traditional apps are rigid, expensive, and rarely adapt to *you*. This project exists to change that.

| # | Challenge | How Language Learning Bot Solves It |
|:-:|-----------|-------------------------------------|
| 1 | **Conversation practice requires a partner** | Chat with an AI tutor that adapts to your proficiency level, corrects mistakes inline, and never judges you for stumbling over conjugations at 2 AM. |
| 2 | **Vocabulary retention drops without spaced repetition** | Build personal vocabulary lists per language, quiz yourself on demand, and track which words you've mastered versus which need more practice. |
| 3 | **Structured lesson plans are locked behind paywalls** | Generate multi-week lesson plans for any of 15 supported languages, covering grammar, vocabulary, reading, and cultural context—completely free and offline. |
| 4 | **Pronunciation guidance is hard to find outside a classroom** | Get detailed pronunciation tips for any word, including IPA transcription, syllable breakdowns, and common mistakes made by English speakers. |
| 5 | **Progress tracking is scattered across apps and notebooks** | Every session is recorded automatically. View summaries of total study time, vocabulary count, and sessions per language in one dashboard. |

> **Privacy first.** Everything runs locally via Ollama. Your conversations, vocabulary, and progress data never leave your machine.

---

## ✨ Features

<div align="center">

```svg
<svg width="720" height="100" viewBox="0 0 720 100" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="100" rx="16" fill="#0d1117"/>
  <rect x="16" y="16" width="160" height="68" rx="12" fill="#06d6a0" opacity="0.15" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="96" y="42" text-anchor="middle" fill="#06d6a0" font-size="13" font-weight="bold">💬 Conversation</text>
  <text x="96" y="62" text-anchor="middle" fill="#8b949e" font-size="11">15 Languages</text>
  <rect x="192" y="16" width="160" height="68" rx="12" fill="#06d6a0" opacity="0.15" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="272" y="42" text-anchor="middle" fill="#06d6a0" font-size="13" font-weight="bold">📚 Vocabulary</text>
  <text x="272" y="62" text-anchor="middle" fill="#8b949e" font-size="11">Build &amp; Quiz</text>
  <rect x="368" y="16" width="160" height="68" rx="12" fill="#06d6a0" opacity="0.15" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="448" y="42" text-anchor="middle" fill="#06d6a0" font-size="13" font-weight="bold">📖 Lessons</text>
  <text x="448" y="62" text-anchor="middle" fill="#8b949e" font-size="11">Plans &amp; Topics</text>
  <rect x="544" y="16" width="160" height="68" rx="12" fill="#06d6a0" opacity="0.15" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="624" y="42" text-anchor="middle" fill="#06d6a0" font-size="13" font-weight="bold">📊 Progress</text>
  <text x="624" y="62" text-anchor="middle" fill="#8b949e" font-size="11">Track Everything</text>
</svg>
```

</div>

| Feature | Description | CLI Command | Web UI Tab |
|---------|-------------|-------------|------------|
| **Conversation Practice** | Chat naturally with an AI tutor that adapts to beginner, intermediate, or advanced levels. Get real-time corrections, grammar explanations, and cultural context woven into every response. | `chat-cmd --language spanish --level beginner` | Chat |
| **Vocabulary Building** | Add words with translations, example sentences, and personal notes. Quiz yourself on demand with configurable question counts. All vocabulary is persisted in `vocabulary.json`. | `quiz --language french --count 10` | Vocabulary |
| **Structured Learning** | Request mini-lessons on any topic (e.g., greetings, past tense, food vocabulary) or generate multi-week lesson plans tailored to your level and available time. | `lesson-plan --language japanese --level intermediate --weeks 4` | Lessons |
| **Progress Tracking** | Every chat session, lesson, and quiz is automatically recorded. View summaries showing total study time, session count, and vocabulary size per language. | `progress-cmd --language german` | Progress |

---

## 🚀 Quick Start

### Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM server |
| gemma4 | — | Default language model |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/language-learning-bot.git
cd language-learning-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -e .
```

### 2. Pull the Model

```bash
ollama pull gemma4
```

### 3. Start Ollama

```bash
ollama serve
```

### 4. Start Chatting

```bash
# Launch an interactive Spanish conversation at beginner level
language-learning-bot chat-cmd --language spanish --level beginner
```

You'll see a prompt like:

```
🇪🇸 Spanish (beginner) — Type your message, or use a /command. Type 'quit' to exit.
> Hola, ¿cómo estás?
```

### 5. Launch the Web UI

```bash
language-learning-bot web
```

Open [http://localhost:7860](http://localhost:7860) in your browser to access all four tabs.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/language-learning-bot.git
cd language-learning-bot
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
uvicorn src.language_learner.api:app --reload --port 8000

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

The CLI is built as a **Click multi-command group** with four top-level commands.

### `chat-cmd` — Interactive Conversation

Start an interactive chat session with the AI language tutor.

```bash
language-learning-bot chat-cmd --language <LANGUAGE> --level <LEVEL>
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--language` | string | `spanish` | Target language (see [Supported Languages](#-supported-languages)) |
| `--level` | string | `beginner` | Proficiency level: `beginner`, `intermediate`, `advanced` |

#### Sub-Commands (In-Chat)

Once inside a `chat-cmd` session, you can use these slash commands:

| Sub-Command | Usage | Description |
|-------------|-------|-------------|
| `/lesson` | `/lesson greetings` | Get a mini-lesson on a specific topic |
| `/translate` | `/translate hello` | Translate a word or phrase into the target language |
| `/vocab` | `/vocab` | Display your saved vocabulary for the current language |
| `/pronounce` | `/pronounce gracias` | Get pronunciation tips for a specific word |
| `/add` | `/add hola hello "Hola, ¿qué tal?" casual greeting` | Add a word to your vocabulary list |
| `/my-vocab` | `/my-vocab` | Show all saved vocabulary words for the current language |
| `/progress` | `/progress` | Show your progress summary for the current language |
| `quit` | `quit` | End the chat session |

#### Examples

```bash
# Beginner Spanish conversation
language-learning-bot chat-cmd --language spanish --level beginner

# Advanced French conversation
language-learning-bot chat-cmd --language french --level advanced

# Intermediate Japanese conversation
language-learning-bot chat-cmd --language japanese --level intermediate
```

**In-session example:**

```
🇪🇸 Spanish (beginner) — Type your message, or use a /command. Type 'quit' to exit.
> /lesson greetings
📖 Here's a mini-lesson on "greetings" in Spanish (beginner level)...

> /pronounce gracias
🗣️ Pronunciation tips for "gracias":
   IPA: /ˈɡɾa.θjas/ (Spain) or /ˈɡɾa.sjas/ (Latin America)
   Syllables: gra-cias
   Common mistake: Pronouncing the 'c' as /k/ instead of /θ/ or /s/

> /add gracias "thank you" "Muchas gracias por tu ayuda" essential phrase
✅ Added "gracias" to your Spanish vocabulary.

> quit
👋 Session ended. ¡Hasta luego!
```

---

### `lesson-plan` — Generate a Structured Lesson Plan

Generate a multi-week lesson plan tailored to your level.

```bash
language-learning-bot lesson-plan --language <LANGUAGE> --level <LEVEL> --weeks <WEEKS>
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--language` | string | `spanish` | Target language |
| `--level` | string | `beginner` | Proficiency level |
| `--weeks` | int | `4` | Duration of the lesson plan in weeks |

#### Examples

```bash
# 4-week beginner German plan
language-learning-bot lesson-plan --language german --level beginner --weeks 4

# 8-week intermediate Korean plan
language-learning-bot lesson-plan --language korean --level intermediate --weeks 8

# 12-week advanced Arabic plan
language-learning-bot lesson-plan --language arabic --level advanced --weeks 12
```

**Sample output:**

```
📋 Lesson Plan: German (Beginner) — 4 Weeks

Week 1: Foundations
  - Day 1-2: Alphabet & pronunciation
  - Day 3-4: Basic greetings (Hallo, Guten Morgen, Tschüss)
  - Day 5-6: Numbers 1-20
  - Day 7: Review & practice

Week 2: Essential Grammar
  - Day 1-2: Subject pronouns (ich, du, er, sie, es)
  - Day 3-4: Present tense of "sein" (to be) and "haben" (to have)
  ...
```

---

### `quiz` — Vocabulary Quiz

Test your vocabulary knowledge with a configurable quiz.

```bash
language-learning-bot quiz --language <LANGUAGE> --count <COUNT>
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--language` | string | `spanish` | Language to quiz on |
| `--count` | int | `5` | Number of quiz questions |

#### Examples

```bash
# 5-question Spanish quiz
language-learning-bot quiz --language spanish --count 5

# 10-question French quiz
language-learning-bot quiz --language french --count 10

# 20-question Japanese quiz (max per session)
language-learning-bot quiz --language japanese --count 20
```

**Sample output:**

```
📝 Vocabulary Quiz: Spanish (5 questions)

1. What does "hola" mean?
   Your answer: hello
   ✅ Correct!

2. What does "gracias" mean?
   Your answer: thanks
   ✅ Correct! (Also accepted: "thank you")

3. What does "perro" mean?
   Your answer: cat
   ❌ Incorrect. The correct answer is "dog".

Score: 4/5 (80%) — Great job! 🎉
```

---

### `progress-cmd` — View Progress Summary

Display your learning progress for a specific language.

```bash
language-learning-bot progress-cmd --language <LANGUAGE>
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--language` | string | `spanish` | Language to view progress for |

#### Examples

```bash
# View Spanish progress
language-learning-bot progress-cmd --language spanish

# View Japanese progress
language-learning-bot progress-cmd --language japanese
```

**Sample output:**

```
📊 Progress Summary: Spanish

  Sessions:       23
  Total Time:     8h 45m
  Vocabulary:     142 words
  Last Session:   2024-12-15 (beginner, 25 min, topic: food)

  Level Breakdown:
    Beginner:     15 sessions
    Intermediate: 7 sessions
    Advanced:     1 session
```

---

## 🖥️ Web UI

The Gradio-based web interface provides four tabs, each mapping to a core feature area.

### Tab 1: 💬 Chat

Interactive conversation with the AI language tutor.

| Element | Description |
|---------|-------------|
| Language Dropdown | Select from 15 supported languages |
| Level Dropdown | Choose beginner, intermediate, or advanced |
| Chat Window | Scrollable conversation with message history |
| Message Input | Type your message or question |
| Send Button | Submit your message to the tutor |

The chat tab calls `get_response(user_message, history, language, level)` on each message, maintaining full conversation context.

### Tab 2: 📚 Vocabulary

Manage your personal vocabulary lists and take quizzes.

| Element | Description |
|---------|-------------|
| Language Selector | Choose which language's vocabulary to view |
| Word Input | Enter a new word in the target language |
| Translation Input | Provide the English translation |
| Example Input | Add an example sentence using the word |
| Notes Input | Optional personal notes (e.g., "informal", "used in Spain") |
| Add Word Button | Saves the word via `add_vocabulary_word()` |
| Vocabulary Table | Displays all saved words from `load_vocabulary()` |
| Quiz Count Slider | Set the number of quiz questions (1–20) |
| Start Quiz Button | Launches quiz via `get_vocabulary_quiz()` |

### Tab 3: 📖 Lessons

Request mini-lessons on specific topics or generate multi-week lesson plans.

| Element | Description |
|---------|-------------|
| Language Dropdown | Target language for the lesson |
| Level Dropdown | Proficiency level |
| Topic Input | Enter a topic (e.g., "past tense", "food vocabulary") |
| Get Lesson Button | Fetches a mini-lesson via `get_lesson()` |
| Weeks Slider | Duration for a lesson plan (1–12 weeks) |
| Generate Plan Button | Creates a plan via `generate_lesson_plan()` |
| Pronunciation Input | Enter a word for pronunciation tips |
| Get Tips Button | Fetches tips via `get_pronunciation_tips()` |

### Tab 4: 📊 Progress

View your learning statistics and session history.

| Element | Description |
|---------|-------------|
| Language Selector | Choose which language's progress to view |
| Refresh Button | Reload progress data |
| Summary Display | Shows output from `get_progress_summary()` |
| Session History | List of recorded sessions with date, level, duration, and topic |

---

## 🏗️ Architecture

### System Flow

```svg
<svg width="720" height="320" viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg">
  <rect width="720" height="320" rx="16" fill="#0d1117"/>

  <!-- User Layer -->
  <rect x="260" y="16" width="200" height="44" rx="10" fill="#06d6a0" opacity="0.2" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="360" y="44" text-anchor="middle" fill="#06d6a0" font-size="14" font-weight="bold">👤 User</text>

  <!-- Interface Layer -->
  <rect x="100" y="88" width="140" height="44" rx="10" fill="#1f6feb" opacity="0.2" stroke="#1f6feb" stroke-width="1.5"/>
  <text x="170" y="116" text-anchor="middle" fill="#1f6feb" font-size="13" font-weight="bold">CLI (Click)</text>
  <rect x="480" y="88" width="140" height="44" rx="10" fill="#1f6feb" opacity="0.2" stroke="#1f6feb" stroke-width="1.5"/>
  <text x="550" y="116" text-anchor="middle" fill="#1f6feb" font-size="13" font-weight="bold">Web UI (Gradio)</text>

  <!-- Core Layer -->
  <rect x="180" y="168" width="360" height="44" rx="10" fill="#06d6a0" opacity="0.2" stroke="#06d6a0" stroke-width="1.5"/>
  <text x="360" y="196" text-anchor="middle" fill="#06d6a0" font-size="14" font-weight="bold">language_learning_bot (Core)</text>

  <!-- Backend Layer -->
  <rect x="60" y="248" width="160" height="44" rx="10" fill="#8b949e" opacity="0.2" stroke="#8b949e" stroke-width="1.5"/>
  <text x="140" y="276" text-anchor="middle" fill="#8b949e" font-size="13">Ollama (gemma4)</text>
  <rect x="280" y="248" width="160" height="44" rx="10" fill="#8b949e" opacity="0.2" stroke="#8b949e" stroke-width="1.5"/>
  <text x="360" y="276" text-anchor="middle" fill="#8b949e" font-size="13">vocabulary.json</text>
  <rect x="500" y="248" width="160" height="44" rx="10" fill="#8b949e" opacity="0.2" stroke="#8b949e" stroke-width="1.5"/>
  <text x="580" y="276" text-anchor="middle" fill="#8b949e" font-size="13">progress.json</text>

  <!-- Arrows -->
  <line x1="300" y1="60" x2="210" y2="88" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="420" y1="60" x2="510" y2="88" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="170" y1="132" x2="300" y2="168" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="550" y1="132" x2="420" y2="168" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="280" y1="212" x2="180" y2="248" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="360" y1="212" x2="360" y2="248" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>
  <line x1="440" y1="212" x2="540" y2="248" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow)"/>

  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#8b949e"/>
    </marker>
  </defs>
</svg>
```

### Data Flow

```
User Input
  │
  ├─── CLI (chat-cmd / lesson-plan / quiz / progress-cmd)
  │       │
  │       └──▶ Core Functions
  │               │
  │               ├──▶ get_system_prompt(language, level)
  │               │       └──▶ Builds context-aware system prompt
  │               │
  │               ├──▶ Ollama API (gemma4)
  │               │       └──▶ LLM generates response
  │               │
  │               ├──▶ load_json_file() / save_json_file()
  │               │       └──▶ vocabulary.json / progress.json
  │               │
  │               └──▶ record_session()
  │                       └──▶ Logs session to progress.json
  │
  └─── Web UI (Gradio)
          │
          └──▶ Same Core Functions (shared module)
```

### Project Structure

```
06-language-learning-bot/
├── language_learning_bot/
│   ├── __init__.py              # Package initialization
│   ├── bot.py                   # Core bot functions
│   │   ├── get_response()       # Conversational AI responses
│   │   ├── get_lesson()         # Mini-lessons on topics
│   │   ├── get_pronunciation_tips()  # Word pronunciation guidance
│   │   ├── generate_lesson_plan()    # Multi-week plans
│   │   ├── get_vocabulary_quiz()     # Vocabulary quizzes
│   │   ├── add_vocabulary_word()     # Add to vocab list
│   │   ├── load_vocabulary()         # Load saved vocab
│   │   ├── record_session()          # Log study sessions
│   │   └── get_progress_summary()    # Progress statistics
│   ├── utils.py                 # Utility functions
│   │   ├── get_system_prompt()  # Build system prompts
│   │   ├── load_json_file()     # Read JSON data
│   │   ├── save_json_file()     # Write JSON data
│   │   └── get_data_path()      # Resolve data file paths
│   ├── cli.py                   # Click CLI commands
│   │   ├── chat-cmd             # Interactive chat
│   │   ├── lesson-plan          # Lesson plan generator
│   │   ├── quiz                 # Vocabulary quiz
│   │   └── progress-cmd         # Progress viewer
│   └── web.py                   # Gradio web interface
│       ├── Chat tab             # Conversation UI
│       ├── Vocabulary tab       # Vocab management
│       ├── Lessons tab          # Lesson & plan UI
│       └── Progress tab         # Progress dashboard
├── data/
│   ├── vocabulary.json          # Per-language vocabulary storage
│   └── progress.json            # Session history & statistics
├── config.yaml                  # Application configuration
├── tests/
│   ├── test_bot.py              # Core function tests
│   ├── test_utils.py            # Utility function tests
│   └── test_cli.py              # CLI command tests
├── pyproject.toml               # Project metadata & dependencies
├── requirements.txt             # Pinned dependencies
└── README.md                    # This file
```

---

## 📖 API Reference

All core functions live in the `language_learning_bot.bot` module.

### `get_response(user_message, history, language, level)`

Generate a conversational response from the AI language tutor.

```python
from language_learning_bot.bot import get_response

response = get_response(
    user_message="¿Cómo se dice 'thank you' en español?",
    history=[
        {"role": "user", "content": "Hola"},
        {"role": "assistant", "content": "¡Hola! ¿Cómo estás?"}
    ],
    language="spanish",
    level="beginner"
)
print(response)
# "En español, 'thank you' se dice 'gracias'. ¡Muy bien por preguntar! 🎉"
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `user_message` | `str` | The user's message in any language |
| `history` | `list[dict]` | Conversation history (role/content pairs) |
| `language` | `str` | Target language (e.g., `"spanish"`) |
| `level` | `str` | Proficiency level: `"beginner"`, `"intermediate"`, `"advanced"` |
| **Returns** | `str` | The AI tutor's response |

---

### `get_lesson(topic, language, level)`

Generate a mini-lesson on a specific topic.

```python
from language_learning_bot.bot import get_lesson

lesson = get_lesson(
    topic="greetings",
    language="french",
    level="beginner"
)
print(lesson)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `topic` | `str` | Lesson topic (e.g., `"greetings"`, `"past tense"`) |
| `language` | `str` | Target language |
| `level` | `str` | Proficiency level |
| **Returns** | `str` | Formatted lesson content |

---

### `get_pronunciation_tips(word, language)`

Get detailed pronunciation guidance for a word.

```python
from language_learning_bot.bot import get_pronunciation_tips

tips = get_pronunciation_tips(
    word="danke",
    language="german"
)
print(tips)
# IPA: /ˈdaŋ.kə/
# Syllables: dan-ke
# Tips: The 'a' is short, like in "fun". The final 'e' is a schwa sound.
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `word` | `str` | The word to get pronunciation tips for |
| `language` | `str` | The language the word belongs to |
| **Returns** | `str` | Pronunciation tips including IPA, syllable breakdown, and common mistakes |

---

### `generate_lesson_plan(language, level, duration_weeks)`

Create a structured multi-week lesson plan.

```python
from language_learning_bot.bot import generate_lesson_plan

plan = generate_lesson_plan(
    language="japanese",
    level="intermediate",
    duration_weeks=6
)
print(plan)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Target language |
| `level` | `str` | Proficiency level |
| `duration_weeks` | `int` | Number of weeks for the plan |
| **Returns** | `str` | Formatted multi-week lesson plan |

---

### `get_vocabulary_quiz(language, count)`

Generate a vocabulary quiz from saved words.

```python
from language_learning_bot.bot import get_vocabulary_quiz

quiz = get_vocabulary_quiz(
    language="spanish",
    count=5
)
print(quiz)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Language to quiz on |
| `count` | `int` | Number of questions (max: `max_words_per_session` from config) |
| **Returns** | `str` | Formatted quiz questions with answer checking |

---

### `add_vocabulary_word(language, word, translation, example, notes)`

Add a new word to your vocabulary list.

```python
from language_learning_bot.bot import add_vocabulary_word

add_vocabulary_word(
    language="italian",
    word="ciao",
    translation="hello / goodbye",
    example="Ciao, come stai?",
    notes="informal, used with friends and family"
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Language the word belongs to |
| `word` | `str` | The word in the target language |
| `translation` | `str` | English translation |
| `example` | `str` | Example sentence using the word |
| `notes` | `str` | Optional personal notes |
| **Returns** | `None` | Saves to `vocabulary.json` |

---

### `load_vocabulary(language)`

Load all saved vocabulary words for a language.

```python
from language_learning_bot.bot import load_vocabulary

vocab = load_vocabulary(language="spanish")
for entry in vocab:
    print(f"{entry['word']} — {entry['translation']}")
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Language to load vocabulary for |
| **Returns** | `list[dict]` | List of vocabulary entries with `word`, `translation`, `example`, `notes` |

---

### `record_session(language, level, duration_minutes, topic)`

Record a study session for progress tracking.

```python
from language_learning_bot.bot import record_session

record_session(
    language="korean",
    level="beginner",
    duration_minutes=30,
    topic="basic greetings"
)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Language studied |
| `level` | `str` | Proficiency level during session |
| `duration_minutes` | `int` | Duration of the session in minutes |
| `topic` | `str` | Topic covered during the session |
| **Returns** | `None` | Saves to `progress.json` |

---

### `get_progress_summary(language)`

Get a summary of your learning progress.

```python
from language_learning_bot.bot import get_progress_summary

summary = get_progress_summary(language="spanish")
print(summary)
# Sessions: 23 | Total Time: 8h 45m | Vocabulary: 142 words
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `language` | `str` | Language to get progress for |
| **Returns** | `str` | Formatted progress summary |

---

### Utility Functions

Utility functions live in `language_learning_bot.utils`.

```python
from language_learning_bot.utils import (
    get_system_prompt,
    load_json_file,
    save_json_file,
    get_data_path
)

# Build a system prompt for the AI tutor
prompt = get_system_prompt(language="spanish", level="beginner")

# Load/save JSON data files
data = load_json_file("vocabulary.json")
save_json_file("vocabulary.json", data)

# Get the full path to a data file
path = get_data_path("vocabulary.json")
# → /path/to/project/data/vocabulary.json
```

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `get_system_prompt` | `language: str, level: str` | `str` | Build a context-aware system prompt for the LLM |
| `load_json_file` | `filename: str` | `dict \| list` | Load and parse a JSON file from the data directory |
| `save_json_file` | `filename: str, data: dict \| list` | `None` | Save data to a JSON file in the data directory |
| `get_data_path` | `filename: str` | `str` | Resolve the full path to a file in the data directory |

---

## 🌐 Supported Languages

Language Learning Bot supports **15 languages** across multiple language families.

| # | Language | Family | Script | Example Greeting |
|:-:|----------|--------|--------|-----------------|
| 1 | 🇪🇸 Spanish | Romance | Latin | ¡Hola! |
| 2 | 🇫🇷 French | Romance | Latin | Bonjour ! |
| 3 | 🇩🇪 German | Germanic | Latin | Hallo! |
| 4 | 🇮🇹 Italian | Romance | Latin | Ciao! |
| 5 | 🇵🇹 Portuguese | Romance | Latin | Olá! |
| 6 | 🇯🇵 Japanese | Japonic | Kanji/Kana | こんにちは！ |
| 7 | 🇰🇷 Korean | Koreanic | Hangul | 안녕하세요! |
| 8 | 🇨🇳 Chinese | Sino-Tibetan | Hanzi | 你好！ |
| 9 | 🇸🇦 Arabic | Semitic | Arabic | !مرحبا |
| 10 | 🇮🇳 Hindi | Indo-Aryan | Devanagari | नमस्ते! |
| 11 | 🇷🇺 Russian | Slavic | Cyrillic | Привет! |
| 12 | 🇳🇱 Dutch | Germanic | Latin | Hallo! |
| 13 | 🇸🇪 Swedish | Germanic | Latin | Hej! |
| 14 | 🇹🇷 Turkish | Turkic | Latin | Merhaba! |
| 15 | 🇬🇷 Greek | Hellenic | Greek | Γεια σου! |

### Proficiency Levels

| Level | Description | Tutor Behavior |
|-------|-------------|----------------|
| **beginner** | No prior knowledge assumed | Uses simple vocabulary, provides translations, explains grammar basics |
| **intermediate** | Basic grammar and vocabulary known | Introduces complex structures, uses more target language, corrects nuanced errors |
| **advanced** | Strong command of the language | Discusses idioms, cultural context, and literature; minimal English usage |

---

## ⚙️ Configuration

### `config.yaml`

```yaml
# Language Learning Bot Configuration

llm:
  model: gemma4                    # Ollama model name
  temperature: 0.7                 # Response creativity (0.0 = deterministic, 1.0 = creative)
  max_tokens: 2048                 # Maximum response length

languages:
  - spanish
  - french
  - german
  - italian
  - portuguese
  - japanese
  - korean
  - chinese
  - arabic
  - hindi
  - russian
  - dutch
  - swedish
  - turkish
  - greek

levels:
  - beginner
  - intermediate
  - advanced

vocabulary:
  storage_file: vocabulary.json    # File for vocabulary data
  max_words_per_session: 20        # Max words per quiz session

progress:
  storage_file: progress.json     # File for progress data
  track_sessions: true            # Enable automatic session tracking
```

### Environment Variables

Override any config value with environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_MODEL` | `gemma4` | Ollama model to use |
| `LLM_TEMPERATURE` | `0.7` | Model temperature |
| `LLM_MAX_TOKENS` | `2048` | Max response tokens |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `VOCAB_FILE` | `vocabulary.json` | Vocabulary storage file |
| `PROGRESS_FILE` | `progress.json` | Progress storage file |
| `WEB_PORT` | `7860` | Web UI port |

```bash
# Example: Use a different model with higher creativity
LLM_MODEL=llama3 LLM_TEMPERATURE=0.9 language-learning-bot chat-cmd --language spanish --level advanced
```

---

## 🧪 Testing

### Run the Test Suite

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_bot.py

# Run with coverage
pytest --cov=language_learning_bot --cov-report=term-missing
```

### Test Structure

| File | Tests |
|------|-------|
| `tests/test_bot.py` | Core functions: `get_response`, `get_lesson`, `get_pronunciation_tips`, `generate_lesson_plan`, `get_vocabulary_quiz`, `add_vocabulary_word`, `load_vocabulary`, `record_session`, `get_progress_summary` |
| `tests/test_utils.py` | Utility functions: `get_system_prompt`, `load_json_file`, `save_json_file`, `get_data_path` |
| `tests/test_cli.py` | CLI commands: `chat-cmd`, `lesson-plan`, `quiz`, `progress-cmd` |

### Local LLM vs Cloud AI

This project is designed for **local LLMs via Ollama**, but the architecture supports cloud providers too.

| Aspect | Local LLM (Ollama) | Cloud AI (OpenAI, etc.) |
|--------|-------------------|------------------------|
| **Privacy** | ✅ All data stays on your machine | ⚠️ Data sent to external servers |
| **Cost** | ✅ Free after hardware investment | 💰 Per-token pricing |
| **Speed** | ⚡ Depends on your GPU/CPU | ⚡ Generally fast, network-dependent |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Model Quality** | 🔄 Improving rapidly (gemma4, llama3) | ✅ State-of-the-art (GPT-4, Claude) |
| **Setup** | 🔧 Install Ollama + pull model | 🔑 Get API key + set env var |
| **Customization** | ✅ Fine-tune your own models | ⚠️ Limited to provider options |

To switch to a cloud provider, update the LLM configuration in `config.yaml` or set the appropriate environment variables. The core functions remain the same — only the backend connection changes.

---

## ❓ FAQ

<details>
<summary><strong>How accurate are the pronunciation tips?</strong></summary>

Pronunciation tips are generated by the LLM (gemma4) based on its training data, which includes IPA transcriptions, phonetic descriptions, and common learner mistakes. For widely studied languages like Spanish, French, and German, accuracy is very high. For less common languages, tips may be less precise. The tips include IPA notation, syllable breakdowns, and specific guidance for English speakers. For production-level pronunciation training, consider pairing this tool with a dedicated speech recognition system.

</details>

<details>
<summary><strong>Can I use vocabulary features offline (without Ollama running)?</strong></summary>

Yes! Vocabulary management functions — `add_vocabulary_word()`, `load_vocabulary()`, and viewing your vocabulary list — work entirely offline since they only read and write to `vocabulary.json`. However, `get_vocabulary_quiz()` requires Ollama to be running because the quiz questions and feedback are generated by the LLM. Similarly, progress tracking via `record_session()` and `get_progress_summary()` work offline since they only interact with `progress.json`.

</details>

<details>
<summary><strong>Can I learn multiple languages at the same time?</strong></summary>

Absolutely. Vocabulary and progress data are stored per-language in `vocabulary.json` and `progress.json`. You can switch between languages freely — each language maintains its own independent word list and session history. For example, you might do a Spanish session in the morning and a Japanese session in the evening. Use `progress-cmd` with different `--language` flags to see your progress for each language independently.

</details>

<details>
<summary><strong>How long should I set my lesson plan duration?</strong></summary>

The `--weeks` parameter for `generate_lesson_plan()` depends on your goals and available study time:

- **1–2 weeks:** Quick crash course for travel or a specific event
- **4 weeks:** Solid foundation for beginners (recommended starting point)
- **8 weeks:** Comprehensive intermediate coverage
- **12 weeks:** Deep dive into advanced topics

The LLM generates daily activities for each week, so longer plans provide more detailed and gradual progression. You can always regenerate a plan if your pace changes.

</details>

<details>
<summary><strong>How does quiz difficulty scale?</strong></summary>

Quiz difficulty is determined by two factors: the words in your vocabulary list and the number of questions (`--count`). The `get_vocabulary_quiz()` function selects words from your saved vocabulary for the specified language. If you have fewer saved words than the requested count, the quiz uses all available words. To increase difficulty, add more complex words to your vocabulary. The quiz format includes translation matching, and the LLM provides contextual feedback on incorrect answers to reinforce learning.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/language-learning-bot.git
cd language-learning-bot

# Create a virtual environment
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify setup
pytest -v
```

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/add-swahili-support`)
3. **Make** your changes with tests
4. **Run** the test suite (`pytest`)
5. **Commit** with a descriptive message (`git commit -m "Add Swahili language support"`)
6. **Push** to your branch (`git push origin feature/add-swahili-support`)
7. **Open** a Pull Request

### Areas for Contribution

| Area | Examples |
|------|----------|
| **New Languages** | Add support for Swahili, Vietnamese, Thai, Polish, etc. |
| **Quiz Types** | Fill-in-the-blank, sentence construction, listening exercises |
| **Spaced Repetition** | Implement SM-2 or similar algorithm for vocabulary review |
| **Audio Integration** | Text-to-speech for pronunciation practice |
| **Import/Export** | CSV/Anki deck import for vocabulary lists |
| **UI Improvements** | Dark mode, mobile-responsive layout, keyboard shortcuts |

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ for language learners everywhere**

<sub>Part of the <a href="../">90 Local LLM Projects</a> collection</sub>

<br />

<img src="https://img.shields.io/badge/Made_with-Python-06d6a0?style=flat-square&logo=python&logoColor=white" alt="Made with Python" />
<img src="https://img.shields.io/badge/Powered_by-Ollama-06d6a0?style=flat-square&logo=ollama&logoColor=white" alt="Powered by Ollama" />
<img src="https://img.shields.io/badge/UI_by-Gradio-06d6a0?style=flat-square&logo=gradio&logoColor=white" alt="UI by Gradio" />

</div>
