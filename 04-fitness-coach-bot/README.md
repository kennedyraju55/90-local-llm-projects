<div align="center">

<!-- Hero Banner -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/banner-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/banner-light.png">
  <img alt="Fitness Coach Bot — AI-Powered Personal Training with Local LLMs" src="docs/assets/banner-light.png" width="800">
</picture>

# 🏋️ Fitness Coach Bot

### AI-Powered Personal Fitness Coach — Running Entirely on Your Machine

**Generate personalized workout plans, track your progress, and explore a comprehensive exercise library — all powered by a local LLM with zero cloud dependency.**

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](#quick-start)
[![Ollama](https://img.shields.io/badge/ollama-gemma4-ff6b35?style=for-the-badge&logo=ollama&logoColor=white)](#configuration)
[![License: MIT](https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge)](#license)
[![Tests](https://img.shields.io/badge/tests-passing-22c55e?style=for-the-badge&logo=pytest&logoColor=white)](#testing)
[![Local LLM](https://img.shields.io/badge/local_LLM-100%25_private-8b5cf6?style=for-the-badge&logo=lock&logoColor=white)](#local-llm-vs-cloud-ai)

<br>

[Quick Start](#quick-start) •
[CLI Reference](#cli-reference) •
[Web UI](#web-ui) •
[API Reference](#api-reference) •
[Configuration](#configuration) •
[Contributing](#contributing)

<br>

</div>

---

## 📋 Table of Contents

- [Why This Project?](#why-this-project)
- [Features](#features)
- [Quick Start](#quick-start)
- [CLI Reference](#cli-reference)
- [Web UI](#web-ui)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Fitness Goals](#fitness-goals)
- [Testing](#testing)
- [Local LLM vs Cloud AI](#local-llm-vs-cloud-ai)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## 🤔 Why This Project?

Most people who want to get fit run into the same frustrating roadblocks. Fitness Coach Bot was built to solve every single one of them — locally, privately, and for free.

| # | Challenge | The Problem | How Fitness Coach Bot Solves It |
|---|-----------|-------------|--------------------------------|
| 1 | **💸 Expensive Personal Trainers** | Personal training sessions cost $50–$150/hour. Most people can't sustain that investment long-term, and quit within weeks. | Generates unlimited personalized workout plans using a local LLM. Zero cost after setup — train as often as you want without spending a dime. |
| 2 | **🤸 Bad Exercise Form** | Without guidance, beginners perform exercises incorrectly, risking injury and reducing effectiveness. Generic YouTube tutorials don't adapt to your level. | Provides detailed exercise breakdowns via `get_exercise_details()` with difficulty-appropriate cues, target muscles, and form guidance tailored to your fitness level. |
| 3 | **📊 No Workout Tracking** | Scribbling sets and reps on paper (or forgetting entirely) makes it impossible to measure progress. Without data, motivation fades and plateaus go unnoticed. | Built-in workout logging with `log_workout()` and progress tracking with `record_progress()`. Persistent JSON storage lets you visualize trends over time. |
| 4 | **📋 Generic Cookie-Cutter Plans** | Free workout plans online ignore your equipment, schedule, fitness level, and goals. A "one-size-fits-all" plan fits almost nobody. | Every plan is generated based on your exact parameters: level, goal, available equipment, days per week, and session duration. No two plans are the same. |
| 5 | **🔒 Privacy Concerns** | Cloud-based fitness apps harvest your health data, body measurements, workout habits, and sell it to advertisers. Your body metrics shouldn't be someone else's product. | Runs 100% locally on your machine via Ollama. Your fitness data never leaves your computer. No accounts, no telemetry, no data harvesting — ever. |

---

## ✨ Features

<div align="center">

```svg
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ╔═══════════════╗    ╔═══════════════╗    ╔═══════════════╗       │
│   ║   🏋️ PLAN     ║───▶║   📚 LIBRARY  ║───▶║   📝 LOG      ║       │
│   ║  Generation   ║    ║   Explorer    ║    ║  Workouts     ║       │
│   ╚═══════════════╝    ╚═══════════════╝    ╚═══════════════╝       │
│          │                                          │               │
│          │              ╔═══════════════╗            │               │
│          └─────────────▶║   📈 TRACK    ║◀───────────┘               │
│                         ║  Progress     ║                           │
│                         ╚═══════════════╝                           │
│                                                                     │
│             Fitness Coach Bot — Complete Training Loop               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

</div>

| Feature | Description | CLI Command | Key Function |
|---------|-------------|-------------|--------------|
| **🏋️ Workout Generation** | AI-generated plans tailored to your fitness level, goals, available equipment, weekly schedule, and session duration. Supports 3 difficulty levels and 6 distinct fitness goals. | `--level beginner --goal weight-loss` | `generate_workout_plan()` |
| **📚 Exercise Library** | Built-in `EXERCISE_LIBRARY` with searchable exercises, complete with target muscles, exercise type, and difficulty rating. Filter and explore without needing an internet connection. | Interactive: `library` | `search_exercises()` |
| **📝 Workout Logging** | Track every set, rep, and weight for each exercise. Data persists to `workout_log.json` so you can review your training history anytime and identify trends. | Interactive: `log` | `log_workout()` |
| **📈 Progress Analytics** | Record body weight (kg) and body fat percentage over time with optional notes. The web UI renders trend charts so you can visualize your transformation. | Interactive: `progress` | `record_progress()` |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM inference |
| gemma4 model | — | Language model for plan generation |

### 1. Clone the Repository

```bash
git clone https://github.com/kennedyraju55/fitness-coach-bot.git
cd fitness-coach-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the LLM Model

```bash
ollama pull gemma4
```

### 5. Generate Your First Workout Plan

```bash
python -m fitness_coach_bot --level beginner --goal weight-loss --equipment "dumbbells,mat"
```

**Expected output:**

```
🏋️ Fitness Coach Bot — Generating your personalized workout plan...

Level:      beginner
Goal:       weight-loss
Equipment:  dumbbells, mat
Days/Week:  4
Duration:   45 min/session

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 Your 4-Day Weight Loss Plan
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Day 1 — Full Body Circuit
  1. Goblet Squats (dumbbells) — 3×12
  2. Push-Ups (mat) — 3×10
  3. Dumbbell Rows — 3×12 each side
  4. Plank Hold (mat) — 3×30s
  ...
```

---

## 💻 CLI Reference

### Command Syntax

```bash
python -m fitness_coach_bot [OPTIONS]
```

### Options

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `--level` | `string` | ✅ Yes | — | Fitness level: `beginner`, `intermediate`, or `advanced` |
| `--goal` | `string` | No | `general-fitness` | Training goal (see [Fitness Goals](#fitness-goals)) |
| `--equipment` | `string` | No | `bodyweight` | Comma-separated list of available equipment |
| `--days` | `int` | No | `4` | Training days per week (1–7) |
| `--duration` | `int` | No | `45` | Session duration in minutes (15–120) |

### Examples

```bash
# Beginner weight-loss plan with minimal equipment
python -m fitness_coach_bot --level beginner --goal weight-loss --equipment "dumbbells,mat"

# Intermediate muscle-gain plan, 5 days a week, 60-minute sessions
python -m fitness_coach_bot --level intermediate --goal muscle-gain \
  --equipment "barbell,dumbbells,bench,pull-up-bar" --days 5 --duration 60

# Advanced endurance training, bodyweight only
python -m fitness_coach_bot --level advanced --goal endurance --days 6 --duration 90

# Flexibility-focused plan for beginners
python -m fitness_coach_bot --level beginner --goal flexibility --equipment "mat,resistance-bands"

# Strength training with full gym access
python -m fitness_coach_bot --level advanced --goal strength \
  --equipment "barbell,dumbbells,bench,squat-rack,cable-machine,pull-up-bar" \
  --days 4 --duration 75
```

### Interactive Mode

Once a workout plan is generated, Fitness Coach Bot enters interactive mode:

```
🏋️ Fitness Coach Bot Interactive Mode
Type a command or exercise name. Type 'quit' to exit.

> push-ups
📖 Detailed breakdown for "Push-Ups" at beginner level...

> log
📝 Log a workout entry:
   Exercise: push-ups
   Sets: 3
   Reps: 10
   Weight (kg, 0 for bodyweight): 0
   ✅ Logged successfully to workout_log.json

> progress
📈 Record progress:
   Weight (kg): 78.5
   Body fat (%): 22.3
   Notes: Feeling stronger this week
   ✅ Progress recorded to progress.json

> library
📚 Exercise Library — 50+ exercises
   Filter by difficulty (beginner/intermediate/advanced): beginner
   ...

> quit
👋 Great workout! See you next time.
```

| Command | Action |
|---------|--------|
| `<exercise name>` | Show detailed info for the named exercise via `get_exercise_details()` |
| `log` | Log a workout entry (exercise, sets, reps, weight) via `log_workout()` |
| `progress` | Record body metrics (weight, body fat, notes) via `record_progress()` |
| `library` | Browse and search the full exercise library via `search_exercises()` |
| `quit` | Exit interactive mode |

---

## 🌐 Web UI

Fitness Coach Bot includes a web interface with four tabs for a complete training experience.

### Starting the Web UI

```bash
python -m fitness_coach_bot --web
```

The web UI launches at `http://localhost:7860` by default.

### Tab Overview

<div align="center">

```
┌──────────────────────────────────────────────────────────────────┐
│  🏋️ Fitness Coach Bot                                            │
├──────────────┬──────────────┬──────────────┬─────────────────────┤
│ Workout Plan │ Log Workout  │  Progress    │ Exercise Library    │
├──────────────┴──────────────┴──────────────┴─────────────────────┤
│                                                                  │
│                     [ Active Tab Content ]                        │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

</div>

#### Tab 1 — Workout Plan

Generate personalized workout plans through the UI.

| Field | Input Type | Options |
|-------|-----------|---------|
| Level | Dropdown | `beginner`, `intermediate`, `advanced` |
| Goal | Dropdown | `weight-loss`, `muscle-gain`, `endurance`, `flexibility`, `general-fitness`, `strength` |
| Equipment | Text input | Comma-separated (e.g., `dumbbells, mat, bench`) |
| Days per Week | Slider | 1–7 |
| Session Duration | Slider | 15–120 minutes |

Click **Generate Plan** to call `generate_workout_plan()`. The plan renders in a formatted panel with exercise details expandable inline via `get_exercise_details()`.

#### Tab 2 — Log Workout

Track your training sessions with structured data entry.

| Field | Input Type | Validation |
|-------|-----------|------------|
| Exercise Name | Text / Autocomplete | Matches `EXERCISE_LIBRARY` entries |
| Sets | Number input | 1–20 |
| Reps | Number input | 1–100 |
| Weight (kg) | Number input | 0+ (0 = bodyweight) |

Submissions call `log_workout()` and persist to `workout_log.json`. A history table displays recent logged entries below the form.

#### Tab 3 — Progress

Visualize your fitness journey over time.

- **Body Weight Chart** — Line graph of weight (kg) over time
- **Body Fat Chart** — Line graph of body fat percentage over time
- **Notes Timeline** — Chronological list of your recorded notes
- **Record New Entry** — Input fields for weight, body fat %, and notes calling `record_progress()`

All data is stored in `progress.json`.

#### Tab 4 — Exercise Library

Browse and search the built-in `EXERCISE_LIBRARY`.

| Feature | Description |
|---------|-------------|
| **Search** | Real-time search across exercise names via `search_exercises()` |
| **Difficulty Filter** | Filter by `beginner`, `intermediate`, or `advanced` |
| **Exercise Cards** | Each card shows: name, target muscles, exercise type, difficulty |
| **Detail View** | Click any exercise to see full details from `get_exercise_details()` |

---

## 🏗️ Architecture

### System Flow

<div align="center">

```svg
┌─────────────┐     ┌─────────────────┐     ┌──────────────┐
│   CLI / Web  │────▶│  fitness_coach   │────▶│    Ollama    │
│   Interface  │     │     _bot core    │     │  (gemma4)    │
│              │◀────│                  │◀────│              │
└─────────────┘     └────────┬────────┘     └──────────────┘
                             │
                    ┌────────┼────────┐
                    ▼        ▼        ▼
              ┌──────┐ ┌──────┐ ┌──────────┐
              │ Log  │ │Prog. │ │ Exercise │
              │ JSON │ │ JSON │ │ Library  │
              └──────┘ └──────┘ └──────────┘
```

</div>

### Request Flow

```
User Input (CLI flags or Web UI form)
  │
  ├─▶ Parse arguments (level, goal, equipment, days, duration)
  │
  ├─▶ generate_workout_plan(level, goal, equipment, days_per_week, session_minutes)
  │     │
  │     ├─▶ Build prompt with user parameters
  │     ├─▶ Send to Ollama (gemma4, temperature=0.7, max_tokens=4096)
  │     └─▶ Parse and format LLM response
  │
  ├─▶ Interactive loop (CLI) or event handlers (Web UI)
  │     │
  │     ├─▶ get_exercise_details(exercise_name, level)
  │     ├─▶ log_workout(exercise, sets, reps, weight, filepath)
  │     ├─▶ record_progress(weight_kg, body_fat_pct, notes)
  │     └─▶ search_exercises()
  │
  └─▶ Data persistence (workout_log.json, progress.json)
```

### Project Structure

```
04-fitness-coach-bot/
├── README.md                  # This file
├── config.yaml                # Model and app configuration
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup
├── Makefile                   # Build and dev commands
├── .env.example               # Environment variable template
├── .gitignore                 # Git ignore rules
│
├── src/
│   └── fitness_coach_bot/
│       ├── __init__.py        # Package init
│       ├── __main__.py        # CLI entry point
│       ├── core.py            # generate_workout_plan(), get_exercise_details()
│       ├── utils.py           # log_workout(), record_progress(), search_exercises()
│       ├── exercises.py       # EXERCISE_LIBRARY data
│       ├── config.py          # Configuration loader
│       └── web.py             # Gradio / Streamlit web interface
│
├── tests/
│   ├── test_core.py           # Tests for core functions
│   ├── test_utils.py          # Tests for utility functions
│   └── test_exercises.py      # Tests for exercise library
│
├── common/                    # Shared utilities
│
└── docs/
    └── assets/                # Banner images and screenshots
```

---

## 📖 API Reference

### `generate_workout_plan(level, goal, equipment, days_per_week, session_minutes)`

Generates a personalized workout plan by sending a structured prompt to the local LLM.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `level` | `str` | ✅ | — | Fitness level: `"beginner"`, `"intermediate"`, or `"advanced"` |
| `goal` | `str` | No | `"general-fitness"` | Training goal (see [Fitness Goals](#fitness-goals)) |
| `equipment` | `list[str]` | No | `["bodyweight"]` | Available equipment |
| `days_per_week` | `int` | No | `4` | Training frequency (1–7) |
| `session_minutes` | `int` | No | `45` | Session length in minutes (15–120) |

**Returns:** `dict` — Structured workout plan with daily exercises, sets, reps, and rest periods.

**Example:**

```python
from fitness_coach_bot.core import generate_workout_plan

plan = generate_workout_plan(
    level="beginner",
    goal="weight-loss",
    equipment=["dumbbells", "mat"],
    days_per_week=4,
    session_minutes=45
)

for day in plan["days"]:
    print(f"\n{day['name']}:")
    for exercise in day["exercises"]:
        print(f"  - {exercise['name']} — {exercise['sets']}×{exercise['reps']}")
```

---

### `get_exercise_details(exercise_name, level)`

Retrieves detailed information about a specific exercise, with form cues and modifications tailored to the specified fitness level.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `exercise_name` | `str` | ✅ | — | Name of the exercise to look up |
| `level` | `str` | No | `"beginner"` | Fitness level for tailored guidance |

**Returns:** `dict` — Exercise details including muscles targeted, type, difficulty, form cues, and level-appropriate modifications.

**Example:**

```python
from fitness_coach_bot.core import get_exercise_details

details = get_exercise_details("push-ups", level="beginner")

print(f"Exercise:  {details['name']}")
print(f"Muscles:   {', '.join(details['muscles'])}")
print(f"Type:      {details['type']}")
print(f"Difficulty: {details['difficulty']}")
print(f"Form Tips:")
for tip in details["form_tips"]:
    print(f"  • {tip}")
```

---

### `log_workout(exercise, sets, reps, weight, filepath)`

Logs a single workout entry to persistent JSON storage.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `exercise` | `str` | ✅ | — | Exercise name |
| `sets` | `int` | ✅ | — | Number of sets completed |
| `reps` | `int` | ✅ | — | Number of reps per set |
| `weight` | `float` | No | `0.0` | Weight used in kg (0 for bodyweight) |
| `filepath` | `str` | No | `"workout_log.json"` | Path to the log file |

**Returns:** `dict` — The logged entry with a timestamp.

**Example:**

```python
from fitness_coach_bot.utils import log_workout

entry = log_workout(
    exercise="goblet-squats",
    sets=3,
    reps=12,
    weight=10.0,
    filepath="workout_log.json"
)

print(f"Logged: {entry['exercise']} — {entry['sets']}×{entry['reps']} @ {entry['weight']}kg")
print(f"Timestamp: {entry['timestamp']}")
```

---

### `record_progress(weight_kg, body_fat_pct, notes)`

Records a progress snapshot with body metrics and optional notes.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `weight_kg` | `float` | ✅ | — | Current body weight in kilograms |
| `body_fat_pct` | `float` | No | `None` | Body fat percentage |
| `notes` | `str` | No | `""` | Free-text notes about how you feel, milestones, etc. |

**Returns:** `dict` — The recorded progress entry with a timestamp.

**Example:**

```python
from fitness_coach_bot.utils import record_progress

entry = record_progress(
    weight_kg=78.5,
    body_fat_pct=22.3,
    notes="Week 3 — noticeably more energy in the mornings"
)

print(f"Weight:   {entry['weight_kg']} kg")
print(f"Body Fat: {entry['body_fat_pct']}%")
print(f"Date:     {entry['timestamp']}")
```

---

### `search_exercises(query, difficulty, muscle_group)`

Searches the built-in `EXERCISE_LIBRARY` with optional filters.

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | `str` | No | `""` | Search term to match against exercise names |
| `difficulty` | `str` | No | `None` | Filter by difficulty: `"beginner"`, `"intermediate"`, `"advanced"` |
| `muscle_group` | `str` | No | `None` | Filter by target muscle group |

**Returns:** `list[dict]` — Matching exercises from the library.

**Example:**

```python
from fitness_coach_bot.utils import search_exercises

# Search for chest exercises suitable for beginners
results = search_exercises(query="chest", difficulty="beginner")

for ex in results:
    print(f"  {ex['name']} — {ex['difficulty']} — {', '.join(ex['muscles'])}")
```

---

### `EXERCISE_LIBRARY`

The built-in exercise database, available as a module-level constant.

```python
from fitness_coach_bot.utils import EXERCISE_LIBRARY

print(f"Total exercises: {len(EXERCISE_LIBRARY)}")

# Each exercise entry contains:
# {
#     "name": "push-ups",
#     "muscles": ["chest", "triceps", "shoulders"],
#     "type": "compound",
#     "difficulty": "beginner"
# }
```

---

## ⚙️ Configuration

### config.yaml

The default configuration file at the project root:

```yaml
# ─── LLM Model Settings ───────────────────────────────────────────
model: gemma4
temperature: 0.7
max_tokens: 4096

# ─── Workout Defaults ─────────────────────────────────────────────
workout:
  default_days_per_week: 4
  default_session_minutes: 45

# ─── Storage Paths ─────────────────────────────────────────────────
storage:
  workout_log_file: workout_log.json
  progress_file: progress.json
```

### Configuration Options

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `model` | `string` | `gemma4` | Ollama model name for LLM inference |
| `temperature` | `float` | `0.7` | LLM sampling temperature (0.0–1.0). Lower = more focused, higher = more creative |
| `max_tokens` | `int` | `4096` | Maximum tokens in LLM response |
| `workout.default_days_per_week` | `int` | `4` | Default training days when `--days` is not specified |
| `workout.default_session_minutes` | `int` | `45` | Default session duration when `--duration` is not specified |
| `storage.workout_log_file` | `string` | `workout_log.json` | File path for workout log persistence |
| `storage.progress_file` | `string` | `progress.json` | File path for progress data persistence |

### Environment Variables

You can override configuration values with environment variables. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

| Variable | Overrides | Example |
|----------|-----------|---------|
| `OLLAMA_MODEL` | `model` | `OLLAMA_MODEL=gemma4` |
| `OLLAMA_HOST` | Ollama server URL | `OLLAMA_HOST=http://localhost:11434` |
| `OLLAMA_TEMPERATURE` | `temperature` | `OLLAMA_TEMPERATURE=0.7` |
| `OLLAMA_MAX_TOKENS` | `max_tokens` | `OLLAMA_MAX_TOKENS=4096` |
| `FCB_DAYS_PER_WEEK` | `workout.default_days_per_week` | `FCB_DAYS_PER_WEEK=5` |
| `FCB_SESSION_MINUTES` | `workout.default_session_minutes` | `FCB_SESSION_MINUTES=60` |
| `FCB_LOG_FILE` | `storage.workout_log_file` | `FCB_LOG_FILE=my_log.json` |
| `FCB_PROGRESS_FILE` | `storage.progress_file` | `FCB_PROGRESS_FILE=my_progress.json` |

---

## 🎯 Fitness Goals

Fitness Coach Bot supports six distinct training goals. Each goal shapes the exercise selection, rep ranges, rest periods, and overall plan structure.

| Goal | CLI Value | Focus | Rep Range | Rest Between Sets | Session Structure |
|------|-----------|-------|-----------|-------------------|-------------------|
| **Weight Loss** | `weight-loss` | High calorie burn through circuits and compound movements | 12–20 | 30–45 seconds | Circuit-based supersets with minimal rest |
| **Muscle Gain** | `muscle-gain` | Hypertrophy via progressive overload and volume | 8–12 | 60–90 seconds | Body-part splits with compound + isolation work |
| **Endurance** | `endurance` | Cardiovascular and muscular endurance | 15–25+ | 15–30 seconds | High-rep circuits, timed intervals, and cardio blocks |
| **Flexibility** | `flexibility` | Mobility, stretching, and range of motion | Hold-based | 30–60 seconds | Yoga-inspired flows, dynamic and static stretching |
| **General Fitness** | `general-fitness` | Balanced all-around fitness and health | 10–15 | 45–60 seconds | Mixed modality — strength, cardio, and mobility |
| **Strength** | `strength` | Maximal force production and neural adaptation | 3–6 | 2–5 minutes | Heavy compound lifts with low volume, high intensity |

### Goal Selection Examples

```bash
# Fat loss with home equipment
python -m fitness_coach_bot --level beginner --goal weight-loss --equipment "dumbbells,mat,jump-rope"

# Bodybuilding-style muscle gain
python -m fitness_coach_bot --level intermediate --goal muscle-gain \
  --equipment "barbell,dumbbells,bench,cable-machine" --days 5 --duration 60

# Marathon preparation
python -m fitness_coach_bot --level advanced --goal endurance --days 6 --duration 90

# Morning flexibility routine
python -m fitness_coach_bot --level beginner --goal flexibility \
  --equipment "mat,foam-roller" --days 7 --duration 20

# Powerlifting-style strength
python -m fitness_coach_bot --level advanced --goal strength \
  --equipment "barbell,squat-rack,bench,deadlift-platform" --days 4 --duration 75
```

---

## 🧪 Testing

### Running the Test Suite

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test modules
pytest tests/test_core.py
pytest tests/test_utils.py
pytest tests/test_exercises.py

# Run with coverage
pytest --cov=fitness_coach_bot --cov-report=term-missing
```

### Test Categories

| Module | Tests | Description |
|--------|-------|-------------|
| `test_core.py` | `generate_workout_plan`, `get_exercise_details` | Validates plan generation parameters, LLM prompt construction, and exercise detail retrieval |
| `test_utils.py` | `log_workout`, `record_progress`, `search_exercises` | Tests data persistence, input validation, and search/filter logic |
| `test_exercises.py` | `EXERCISE_LIBRARY` integrity | Ensures all exercises have required fields (name, muscles, type, difficulty) |

### Using Make

```bash
# Run all tests
make test

# Run tests with coverage
make coverage

# Run linting
make lint

# Format code
make format
```

---

## 🔒 Local LLM vs Cloud AI

Fitness Coach Bot is designed as a **local-first** application. Here's how it compares to cloud-based alternatives:

| Aspect | Fitness Coach Bot (Local) | Cloud AI Services |
|--------|---------------------------|-------------------|
| **Privacy** | ✅ All data stays on your machine | ❌ Health data sent to third-party servers |
| **Cost** | ✅ Free after Ollama setup | ❌ API costs per request ($0.01–$0.10+) |
| **Internet Required** | ✅ Works fully offline | ❌ Requires constant internet connection |
| **Latency** | ✅ Low (local inference) | ⚠️ Variable (network + API queue) |
| **Data Ownership** | ✅ You own everything | ❌ Provider may retain/use your data |
| **Customization** | ✅ Swap models freely via Ollama | ⚠️ Limited to provider's model offerings |
| **Rate Limits** | ✅ None — run as much as you want | ❌ Throttled at free/low tiers |
| **Hardware Required** | ⚠️ 8GB+ RAM recommended | ✅ Runs on any device with internet |
| **Model Quality** | ⚠️ Depends on local hardware | ✅ Large frontier models available |

### Switching Models

You can use any Ollama-compatible model by changing the `model` field in `config.yaml`:

```yaml
# Use a different model
model: llama3.1

# Or set via environment variable
# OLLAMA_MODEL=mistral
```

Popular alternatives:

| Model | Size | Best For |
|-------|------|----------|
| `gemma4` | ~5GB | Default — good balance of quality and speed |
| `llama3.1` | ~4.7GB | Strong general-purpose reasoning |
| `mistral` | ~4.1GB | Fast inference, good for lower-end hardware |
| `phi3` | ~2.3GB | Lightweight, runs on 8GB RAM systems |

---

## ❓ FAQ

### 1. How accurate is the exercise form guidance?

The form guidance in `get_exercise_details()` is generated by the local LLM based on widely accepted exercise science principles. It provides solid foundational cues (e.g., "keep your core engaged," "don't let knees cave inward") appropriate to your selected fitness level. However, it is **not a substitute for a certified personal trainer** — especially for complex movements like barbell squats or Olympic lifts. If you're new to exercise, consider having a professional review your form for compound lifts before training independently.

### 2. How does progress tracking work?

Progress tracking uses two persistent JSON files:

- **`workout_log.json`** — Every call to `log_workout()` appends a timestamped entry with exercise name, sets, reps, and weight. This lets you track volume and progressive overload across sessions.
- **`progress.json`** — Every call to `record_progress()` stores a timestamped snapshot of your body weight (kg), body fat percentage, and any notes you add.

The web UI reads these files and renders trend charts. You can also process them with any JSON-compatible tool (Python, jq, Excel) for custom analysis.

### 3. What equipment do I need to get started?

**None!** By default, Fitness Coach Bot generates bodyweight-only plans. You can specify any equipment you have via the `--equipment` flag:

```bash
# Bodyweight only (no flag needed)
python -m fitness_coach_bot --level beginner --goal general-fitness

# Home gym basics
python -m fitness_coach_bot --level beginner --goal weight-loss --equipment "dumbbells,mat,resistance-bands"

# Full gym
python -m fitness_coach_bot --level advanced --goal strength \
  --equipment "barbell,dumbbells,bench,squat-rack,cable-machine,pull-up-bar,kettlebell"
```

The LLM adapts exercise selection based on what you have available.

### 4. Can I adjust workout difficulty after generating a plan?

Yes! Workout difficulty is controlled by the `--level` flag:

- **`beginner`** — Simpler movements, lower volume, longer rest periods, more detailed form cues
- **`intermediate`** — Progressive overload, moderate volume, varied exercises
- **`advanced`** — Complex movements, high volume/intensity, periodization concepts

You can regenerate a plan at any time with a different level. Your workout logs and progress data persist independently of plan generation, so switching levels doesn't lose your history.

### 5. How many exercises are in the built-in library?

The `EXERCISE_LIBRARY` contains **50+ exercises** spanning all major muscle groups and difficulty levels. Each entry includes:

- **Name** — The exercise identifier
- **Muscles** — Target and synergist muscle groups
- **Type** — Compound or isolation
- **Difficulty** — beginner, intermediate, or advanced

You can browse the full library in the web UI's Exercise Library tab or through the interactive CLI `library` command. Use `search_exercises()` programmatically to filter by name, difficulty, or muscle group.

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and set up development environment
git clone https://github.com/kennedyraju55/fitness-coach-bot.git
cd fitness-coach-bot
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e ".[dev]"
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes with tests
4. **Run** the test suite: `pytest -v`
5. **Lint** your code: `make lint`
6. **Commit** with a descriptive message: `git commit -m "feat: add new exercise category"`
7. **Push** to your fork: `git push origin feature/your-feature-name`
8. **Open** a Pull Request against `main`

### Areas for Contribution

| Area | Description |
|------|-------------|
| 🏋️ Exercises | Add new exercises to `EXERCISE_LIBRARY` |
| 🧪 Tests | Improve test coverage for edge cases |
| 🌐 Web UI | Enhance charts, add new visualizations |
| 📖 Documentation | Improve guides, add tutorials |
| 🐛 Bug Fixes | Fix issues from the issue tracker |
| ✨ Features | Implement requested features |

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 kennedyraju55

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**Built with 🧡 using [Ollama](https://ollama.ai) and local AI**

<sub>Part of the <a href="../">90 Local LLM Projects</a> series — Project #04</sub>

</div>
