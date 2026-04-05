<div align="center">

  ![Quiz Generator Banner](docs/images/banner.svg)

  <br/>

  ![Gemma 3](https://img.shields.io/badge/Gemma_3-Local_LLM-E94560?style=for-the-badge&logo=google&logoColor=white)
  ![Ollama](https://img.shields.io/badge/Ollama-Inference-0f3460?style=for-the-badge&logo=llama&logoColor=white)
  ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
  ![Click](https://img.shields.io/badge/Click-CLI-00C853?style=for-the-badge&logo=gnu-bash&logoColor=white)
  ![pytest](https://img.shields.io/badge/pytest-Tested-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
  ![License](https://img.shields.io/badge/License-MIT-FFC107?style=for-the-badge)
  ![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)

  <br/>

  **AI-Powered Quiz Generation & Assessment Platform — 100% Local, 100% Private**

  Generate, take, score, and manage quizzes on *any* topic using a locally-hosted LLM.<br/>
  No API keys. No cloud. No data leaves your machine.

  <br/>

  [**Quick Start**](#-quick-start) · [**CLI Reference**](#-cli-reference) · [**Web UI**](#-web-ui) · [**Architecture**](#-architecture) · [**API Reference**](#-api-reference) · [**Configuration**](#%EF%B8%8F-configuration) · [**Contributing**](#-contributing)

  <br/>

  <strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

<br/>

---

## 🤔 Why This Project?

Creating quizzes manually is tedious, slow, and hard to scale. Cloud-based AI tools raise privacy concerns and cost money. **Quiz Generator** solves both problems by combining local LLM inference with a production-grade assessment pipeline.

| Problem | Traditional Approach | Quiz Generator Solution |
|---------|---------------------|------------------------|
| ⏳ **Time-consuming quiz creation** | Manually write each question, option, and answer | AI generates complete quizzes in seconds |
| 🔒 **Data privacy concerns** | Send educational content to cloud APIs | 100% local — nothing leaves your machine |
| 💸 **Recurring API costs** | Pay per token for OpenAI / Anthropic | Free forever with local Ollama inference |
| 📊 **No performance tracking** | Spreadsheets and manual record-keeping | Built-in score history, averages, and analytics |
| 🔄 **Inflexible formats** | Locked into one quiz platform's format | Export to JSON, Markdown, or PDF-ready format |

---

## ✨ Features

<div align="center">

  ![Features Overview](docs/images/features.svg)

</div>

<br/>

<table>
<tr>
<td width="50%">

### 📝 Multi-Format Quiz Generation
- **Multiple Choice** — 4 options with one correct answer
- **True / False** — Binary assessment questions
- **Short Answer** — Open-ended response questions
- **Mixed Mode** — Combine all formats in one quiz
- AI-generated explanations for every answer
- Smart JSON parsing with code-fence handling

</td>
<td width="50%">

### ⏱️ Timed Assessments
- Per-question countdown timer
- Configurable seconds per question (default: 30s)
- Automatic expiration detection
- Elapsed time tracking per quiz attempt
- Timer toggle via CLI flag or config
- Real-time countdown in Web UI

</td>
</tr>
<tr>
<td width="50%">

### 📦 Question Bank
- Persistent local storage (JSON-backed)
- Add questions from any generated quiz
- Filter by **topic**, **difficulty**, or **question type**
- Browse, remove, and clear operations
- Reuse questions across multiple quiz sessions
- CLI and Web UI management interfaces

</td>
<td width="50%">

### 📊 Score Tracking & Analytics
- Automatic recording of every quiz result
- Full history with timestamps and topics
- Average score calculation across all attempts
- Best score retrieval with metadata
- Trend analysis in the Streamlit dashboard
- Persistent storage across sessions

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Minimum Version | Purpose |
|-------------|----------------|---------|
| **Python** | 3.11+ | Runtime environment |
| **Ollama** | Latest | Local LLM inference server |
| **Gemma 3** | Via Ollama | Default language model |
| **Git** | Any | Clone the repository |

### Step 1 — Install Ollama & Pull the Model

```bash
# Install Ollama (visit https://ollama.com for your platform)
# Then pull the Gemma 3 model:
ollama pull gemma3

# Verify Ollama is running:
ollama list
```

### Step 2 — Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/quiz-generator.git
cd quiz-generator

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# (Optional) Install in development mode
pip install -e ".[dev]"
```

### Step 3 — Generate Your First Quiz

```bash
python -m quiz_gen.cli generate --topic "Python Programming" --questions 5
```

<details>
<summary>📋 <strong>Example Output</strong> (click to expand)</summary>

```
🧠 Quiz Generator
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Topic:      Python Programming
Type:       multiple-choice
Difficulty: medium
Questions:  5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Q1. What is the output of `print(type([]))` in Python?

    A) <class 'tuple'>
    B) <class 'list'>
    C) <class 'dict'>
    D) <class 'set'>

Q2. Which keyword is used to define a function in Python?

    A) function
    B) func
    C) def
    D) define

Q3. What does the `len()` function return when called on a dictionary?

    A) Number of values
    B) Number of key-value pairs
    C) Total memory size
    D) Number of unique values

Q4. Which of the following is an immutable data type in Python?

    A) list
    B) dict
    C) set
    D) tuple

Q5. What is the correct way to handle exceptions in Python?

    A) try/catch
    B) try/except
    C) catch/throw
    D) begin/rescue

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Quiz generated successfully!
```

</details>

### Step 4 — Launch the Web UI

```bash
streamlit run src/quiz_gen/web_ui.py
```

The web interface opens at `http://localhost:8501` with interactive quiz generation, scoring, and analytics.

---

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and organized as a command group with four sub-commands.

```bash
python -m quiz_gen.cli [COMMAND] [OPTIONS]
```

### `generate` — Create a New Quiz

Generate an AI-powered quiz on any topic.

```bash
# Basic generation
python -m quiz_gen.cli generate --topic "World War II" --questions 10

# With answers shown inline
python -m quiz_gen.cli generate -t "Biology" -q 5 --show-answers

# True/False quiz, hard difficulty
python -m quiz_gen.cli generate -t "Data Structures" --type true-false -d hard

# Short answer quiz saved to file
python -m quiz_gen.cli generate -t "Chemistry" -q 15 --type short-answer --output quiz.json

# Mixed format with all question types
python -m quiz_gen.cli generate -t "Machine Learning" --type mixed -q 10 -d easy
```

| Option | Short | Default | Choices | Description |
|--------|-------|---------|---------|-------------|
| `--topic` | `-t` | *required* | — | Quiz topic (any subject) |
| `--questions` | `-q` | `5` | 1–50 | Number of questions to generate |
| `--type` | — | `multiple-choice` | `multiple-choice`, `true-false`, `short-answer`, `mixed` | Question format |
| `--difficulty` | `-d` | `medium` | `easy`, `medium`, `hard` | Difficulty level |
| `--output` | `-o` | — | — | Save quiz to a JSON file |
| `--show-answers` | `-a` | `false` | — | Display answers inline |

### `take` — Take a Quiz Interactively

Start an interactive quiz session with instant scoring and feedback.

```bash
# Take a quiz from a saved file
python -m quiz_gen.cli take --file quiz.json

# Generate and take in one step
python -m quiz_gen.cli take --topic "Geography" --questions 10

# Enable per-question timer
python -m quiz_gen.cli take --file quiz.json --timer

# Generate a hard quiz and take it immediately
python -m quiz_gen.cli take -t "Organic Chemistry" -q 8 --timer
```

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--file` | `-f` | — | Path to a saved quiz JSON file |
| `--topic` | `-t` | — | Generate a new quiz on this topic |
| `--questions` | `-q` | `5` | Number of questions (when generating) |
| `--timer` | — | `false` | Enable per-question countdown timer |

### `export` — Export Quiz to Other Formats

Convert saved quizzes to different output formats.

```bash
# Export to Markdown (great for printing / PDF conversion)
python -m quiz_gen.cli export --input quiz.json --format markdown --output quiz.md

# Export to clean, formatted JSON
python -m quiz_gen.cli export --input quiz.json --format json --output clean.json

# Export to PDF-ready format
python -m quiz_gen.cli export --input quiz.json --format pdf-ready --output quiz_print.md
```

| Option | Short | Default | Choices | Description |
|--------|-------|---------|---------|-------------|
| `--input` | `-i` | *required* | — | Path to input quiz JSON file |
| `--format` | `-f` | `json` | `json`, `markdown`, `pdf-ready` | Output format |
| `--output` | `-o` | — | — | Output file path |

### `bank` — Manage the Question Bank

Store, browse, and manage a persistent collection of quiz questions.

```bash
# Add questions from a quiz file to the bank
python -m quiz_gen.cli bank add --file quiz.json

# List all questions in the bank
python -m quiz_gen.cli bank list

# Filter by topic
python -m quiz_gen.cli bank list --topic "Math"

# Clear the entire question bank
python -m quiz_gen.cli bank clear
```

#### `bank add`

| Option | Short | Description |
|--------|-------|-------------|
| `--file` | `-f` | Path to quiz JSON file to import |

#### `bank list`

| Option | Short | Description |
|--------|-------|-------------|
| `--topic` | `-t` | Filter questions by topic |

#### `bank clear`

No options — clears all questions from the bank.

---

## 🌐 Web UI

The Streamlit-based web interface provides a rich, interactive experience with real-time quiz generation, scoring, and analytics.

```bash
streamlit run src/quiz_gen/web_ui.py
```

Opens at `http://localhost:8501` in your default browser.

### Tabs Overview

| Tab | Icon | Description |
|-----|------|-------------|
| **Generate Quiz** | 📝 | Set topic, type, difficulty — generate and preview with expandable answers |
| **Take Quiz** | 🎯 | Interactive quiz with radio buttons / text input, optional timer, instant scoring |
| **Question Bank** | 🗂️ | Browse, filter, and manage saved questions with search and delete |
| **Score History** | 📊 | View past scores, averages, best scores, trend charts, and performance stats |

### Sidebar Controls

| Control | Type | Description |
|---------|------|-------------|
| **Topic** | Text input | Subject for quiz generation |
| **Number of Questions** | Slider (1–50) | How many questions to generate |
| **Question Type** | Selectbox | Multiple Choice, True/False, Short Answer, Mixed |
| **Difficulty** | Selectbox | Easy, Medium, Hard |
| **Timer** | Toggle | Enable/disable per-question timer |
| **Ollama Status** | Indicator | Shows whether Ollama is running and reachable |

---

## 🏗️ Architecture

<div align="center">

  ![Architecture Diagram](docs/images/architecture.svg)

</div>

<br/>

The application follows a **layered architecture** with clean separation of concerns:

| Layer | Component | Responsibility |
|-------|-----------|---------------|
| **Presentation** | `cli.py` (Click) | Terminal interface, argument parsing, formatted output |
| **Presentation** | `web_ui.py` (Streamlit) | Browser-based interactive interface |
| **Business Logic** | `core.py` | Quiz generation, scoring, validation, data models |
| **Data Access** | `QuestionBank`, `ScoreTracker` | JSON-based persistent storage |
| **Configuration** | `ConfigManager` | YAML config loading with dot-path access |
| **External** | Ollama / Gemma 3 | Local LLM inference via REST API (port 11434) |

### Project Structure

```
51-quiz-generator/
├── docs/
│   └── images/
│       ├── banner.svg              # Project banner image
│       ├── architecture.svg        # System architecture diagram
│       └── features.svg            # Feature highlights diagram
├── src/
│   └── quiz_gen/
│       ├── __init__.py             # Package init & version
│       ├── core.py                 # Business logic, models, LLM integration
│       │   ├── ConfigManager       #   YAML config loader
│       │   ├── DifficultyLevel     #   Enum: EASY, MEDIUM, HARD
│       │   ├── QuizQuestion        #   Dataclass for questions
│       │   ├── QuizResult          #   Dataclass for results
│       │   ├── QuestionBank        #   Persistent question storage
│       │   ├── TimedQuiz           #   Timer management
│       │   ├── ScoreTracker        #   Score history & analytics
│       │   ├── generate_quiz()     #   LLM-powered generation
│       │   ├── score_quiz()        #   Answer evaluation
│       │   ├── export_quiz_json()  #   JSON export
│       │   ├── export_quiz_pdf_ready()  # Markdown export
│       │   └── validate_quiz_data()     # Schema validation
│       ├── cli.py                  # Click CLI commands
│       │   ├── generate            #   Create a new quiz
│       │   ├── take                #   Interactive quiz session
│       │   ├── export              #   Format conversion
│       │   └── bank                #   Question bank management
│       └── web_ui.py               # Streamlit web interface
├── common/
│   └── llm_client.py              # Shared Ollama HTTP client
├── tests/
│   ├── __init__.py
│   ├── test_core.py               # Core module unit tests
│   └── test_cli.py                # CLI integration tests
├── config.yaml                    # Application configuration
├── setup.py                       # Package setup & metadata
├── Makefile                       # Development shortcuts
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment variable template
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## 📚 API Reference

### `QuizQuestion` — Question Data Model

A dataclass representing a single quiz question with all metadata.

```python
from quiz_gen.core import QuizQuestion, DifficultyLevel

question = QuizQuestion(
    number=1,
    question="What is the capital of France?",
    answer="Paris",
    q_type="multiple-choice",
    options=["London", "Paris", "Berlin", "Madrid"],
    explanation="Paris has been the capital of France since the 10th century.",
    topic="Geography",
    difficulty=DifficultyLevel.EASY,
)

# Serialize to dictionary
data = question.to_dict()

# Deserialize from dictionary
restored = QuizQuestion.from_dict(data)
```

### `QuestionBank` — Persistent Question Storage

Store, filter, and manage a collection of quiz questions.

```python
from quiz_gen.core import QuestionBank

bank = QuestionBank(storage_file="question_bank.json")

# Add a single question
bank.add(question)

# Add all questions from generated quiz data
count = bank.add_from_quiz(quiz_data)
print(f"Added {count} questions")

# Filter questions
easy_geo = bank.filter(topic="Geography", difficulty=DifficultyLevel.EASY)
mcq_only = bank.filter(q_type="multiple-choice")

# Browse all questions
all_questions = bank.all()
print(f"Bank contains {len(bank)} questions")

# Remove by index
bank.remove(0)

# Clear everything
bank.clear()
```

### `TimedQuiz` — Timer Management

Add per-question countdown timers to any quiz session.

```python
from quiz_gen.core import TimedQuiz

timed = TimedQuiz(quiz_data=quiz_data, seconds_per_question=30)

# Start the timer
timed.start()

# Check elapsed time
print(f"Elapsed: {timed.elapsed:.1f}s")

# Check total time limit
print(f"Time limit: {timed.time_limit}s")

# Check if timer has expired
if timed.is_expired:
    print("Time's up!")

# Stop the timer
timed.stop()
```

### `ScoreTracker` — Performance Analytics

Track quiz results and compute performance statistics.

```python
from quiz_gen.core import ScoreTracker, QuizResult

tracker = ScoreTracker(history_file="quiz_scores.json")

# Record a result
result = QuizResult(
    score=8,
    total=10,
    percentage=80.0,
    time_taken=245.5,
    topic="Python",
    timestamp="2025-01-15T10:30:00",
)
tracker.record(result)

# View history
for entry in tracker.history():
    print(f"{entry['topic']}: {entry['percentage']}%")

# Get statistics
avg = tracker.average_score()
best = tracker.best_score()
print(f"Average: {avg:.1f}%  |  Best: {best['percentage']}%")
print(f"Total quizzes taken: {len(tracker)}")

# Clear history
tracker.clear()
```

### `ConfigManager` — Configuration Access

Load and access YAML configuration with dot-path notation.

```python
from quiz_gen.core import ConfigManager

config = ConfigManager(config_path="config.yaml")

# Access nested values with dot-path keys
temperature = config.get("llm", "temperature", default=0.7)
max_questions = config.get("quiz", "max_questions", default=50)
timer_enabled = config.get("timer", "enabled", default=False)

# Access the raw config dictionary
raw = config.raw
print(raw)
```

### Core Functions

```python
from quiz_gen.core import (
    generate_quiz,
    score_quiz,
    export_quiz_json,
    export_quiz_pdf_ready,
    validate_quiz_data,
)

# Generate a quiz using the local LLM
quiz_data = generate_quiz(
    topic="Machine Learning",
    num_questions=10,
    quiz_type="multiple-choice",
    difficulty="hard",
    config=config,
)

# Score user answers against the quiz
result = score_quiz(questions=quiz_data["questions"], user_answers=user_answers)
print(f"Score: {result.score}/{result.total} ({result.percentage}%)")

# Export to JSON file
path = export_quiz_json(quiz_data, path="ml_quiz.json")

# Export to Markdown (PDF-ready)
markdown_str = export_quiz_pdf_ready(quiz_data)

# Validate quiz data structure
errors = validate_quiz_data(quiz_data)
if errors:
    for err in errors:
        print(f"Validation error: {err}")
```

---

## ⚙️ Configuration

All settings live in `config.yaml` at the project root. Every value has a sensible default.

```yaml
# ─── LLM Settings ────────────────────────────────────────
llm:
  temperature: 0.7              # Creativity (0.0 = deterministic, 1.0 = creative)
  max_tokens: 4096              # Maximum response length from the LLM

# ─── Quiz Defaults ───────────────────────────────────────
quiz:
  default_num_questions: 5      # Default number of questions
  default_type: "multiple-choice"
  default_difficulty: "medium"  # easy | medium | hard
  max_questions: 50             # Upper limit for generation

# ─── Timer ────────────────────────────────────────────────
timer:
  enabled: false                # Enable timer by default
  default_seconds_per_question: 30

# ─── Data Persistence ────────────────────────────────────
scoring:
  history_file: "quiz_scores.json"

question_bank:
  storage_file: "question_bank.json"

# ─── Logging ──────────────────────────────────────────────
logging:
  level: "INFO"                 # DEBUG | INFO | WARNING | ERROR
  file: "quiz_gen.log"
```

### Environment Variables

You can override settings with environment variables. See `.env.example` for the full list.

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `gemma3` | Model name for inference |
| `QUIZ_CONFIG_PATH` | `config.yaml` | Path to configuration file |
| `QUIZ_LOG_LEVEL` | `INFO` | Logging verbosity |
| `QUIZ_HISTORY_FILE` | `quiz_scores.json` | Score history file path |
| `QUIZ_BANK_FILE` | `question_bank.json` | Question bank file path |

---

## 🧪 Testing

Tests use **pytest** and mock all LLM calls, so they run instantly without Ollama.

```bash
# Run all tests with verbose output
python -m pytest tests/ -v --tb=short

# Run with coverage report
python -m pytest tests/ -v --cov=quiz_gen --cov-report=term-missing

# Run only core logic tests
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v
```

### Test Coverage

| Module | File | Covers |
|--------|------|--------|
| **Core Logic** | `tests/test_core.py` | `generate_quiz`, `score_quiz`, `QuizQuestion`, `QuizResult`, `QuestionBank`, `TimedQuiz`, `ScoreTracker`, `ConfigManager`, validation, export |
| **CLI** | `tests/test_cli.py` | `generate`, `take`, `export`, `bank add`, `bank list`, `bank clear` commands via Click test runner |

---

## 🏠 Local LLM vs. Cloud AI

Why run a local LLM instead of calling OpenAI or Anthropic?

| Criteria | ☁️ Cloud AI (GPT-4, Claude) | 🏠 Local LLM (Gemma 3 + Ollama) |
|----------|---------------------------|----------------------------------|
| **Privacy** | ❌ Data sent to third-party servers | ✅ 100% local — nothing leaves your machine |
| **Cost** | 💸 Pay per token ($0.01–0.06/1K tokens) | 🆓 Free forever after one-time model download |
| **Speed** | ⚡ Fast (but network-dependent) | ⚡ Fast on modern hardware (GPU recommended) |
| **Customization** | 🔒 Limited to API parameters | 🔧 Full control over model, prompts, temperature |
| **Offline** | ❌ Requires internet connection | ✅ Works completely offline |
| **Rate Limits** | ⚠️ Throttled under heavy use | ♾️ No limits — run as many quizzes as you want |
| **Data Retention** | ⚠️ Provider may retain prompts | ✅ Zero data retention by third parties |
| **Setup** | ✅ Just an API key | 🔧 Install Ollama + pull model (~2–5 GB) |

> **Bottom line:** If you care about privacy, cost, or offline access, local LLM is the clear winner for educational content generation.

---

## ❓ FAQ

<details>
<summary><strong>Which LLM models are supported?</strong></summary>

<br/>

Quiz Generator works with **any model available through Ollama**. The default is **Gemma 3**, but you can use Llama 3, Mistral, Phi-3, or any other model. Change the model in your `.env` file:

```bash
OLLAMA_MODEL=llama3
```

The quality of generated quizzes depends on the model's capabilities. Larger models generally produce better questions and more accurate answers.

</details>

<details>
<summary><strong>How much disk space and RAM do I need?</strong></summary>

<br/>

- **Gemma 3 (4B):** ~2.5 GB disk, ~4 GB RAM
- **Gemma 3 (12B):** ~7 GB disk, ~8 GB RAM
- **Llama 3 (8B):** ~4.7 GB disk, ~6 GB RAM

A GPU with 6+ GB VRAM is recommended for faster inference, but CPU-only mode works too (just slower).

</details>

<details>
<summary><strong>Can I generate quizzes in languages other than English?</strong></summary>

<br/>

Yes! Simply specify the topic in your target language, and the LLM will generate questions in that language. For example:

```bash
python -m quiz_gen.cli generate -t "Geschichte Deutschlands" -q 5
```

Results depend on the model's multilingual capabilities. Gemma 3 supports many languages out of the box.

</details>

<details>
<summary><strong>Why are some generated answers incorrect?</strong></summary>

<br/>

Local LLMs can occasionally produce inaccurate answers, especially on niche or highly specialized topics. To improve accuracy:

1. Use a **larger model** (e.g., Gemma 3 12B instead of 4B)
2. Lower the **temperature** in `config.yaml` (e.g., `0.3` instead of `0.7`)
3. Use the `validate_quiz_data()` function to check for structural issues
4. Review generated quizzes before using them in assessments

</details>

<details>
<summary><strong>Can I use this for classroom assessments?</strong></summary>

<br/>

Absolutely! Quiz Generator is designed for educational use. You can:

1. **Generate** quizzes on your lecture topics
2. **Export** to Markdown or PDF-ready format for printing
3. **Customize** difficulty levels for different student groups
4. **Build a question bank** over time for reuse across semesters

Always review AI-generated questions for accuracy before using them in graded assessments.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/quiz-generator.git
cd quiz-generator

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.venv\Scripts\activate       # Windows

# Install in development mode
pip install -e ".[dev]"

# Run the test suite
python -m pytest tests/ -v
```

### Guidelines

1. **Fork** the repository and create a feature branch
2. **Write tests** for new functionality
3. **Follow** the existing code style and patterns
4. **Update** documentation for any user-facing changes
5. **Run** the full test suite before submitting
6. **Open a PR** with a clear description of your changes

### Areas for Contribution

| Area | Description |
|------|-------------|
| 🧠 **New quiz types** | Add fill-in-the-blank, matching, ordering questions |
| 🌍 **Internationalization** | Improve multilingual prompt templates |
| 📊 **Analytics** | Advanced score visualizations and statistics |
| 🧪 **Test coverage** | Increase coverage for edge cases |
| 📖 **Documentation** | Tutorials, guides, and examples |
| 🐛 **Bug fixes** | Fix issues from the issue tracker |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, including commercial use.

---

<div align="center">

  <br/>

  **Built with ❤️ as part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

  <br/>

  ![Gemma 3](https://img.shields.io/badge/Gemma_3-E94560?style=flat-square&logo=google&logoColor=white)
  ![Ollama](https://img.shields.io/badge/Ollama-0f3460?style=flat-square)
  ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

  <br/>

  [⬆ Back to Top](#)

</div>
