<div align="center">

  <!-- Hero Banner -->
  <img src="docs/images/banner.svg" alt="Reading Comprehension Builder — AI-Powered Reading Exercises" width="800"/>

  <br/><br/>

  <!-- Badges -->
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+"/></a>
  <a href="https://ollama.com/"><img src="https://img.shields.io/badge/Ollama-Local_LLM-FF6F00?style=for-the-badge&logo=meta&logoColor=white" alt="Ollama"/></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>
  <a href="https://click.palletsprojects.com/"><img src="https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Click CLI"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT License"/></a>
  <a href="https://github.com/kennedyraju55/reading-comprehension-builder/actions"><img src="https://img.shields.io/badge/Tests-Passing-brightgreen?style=for-the-badge&logo=pytest&logoColor=white" alt="Tests Passing"/></a>

  <br/><br/>

  <strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection (#60)</strong>

  <br/><br/>

  <!-- Quick Links -->
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-web-ui">Web UI</a> •
  <a href="#%EF%B8%8F-architecture">Architecture</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-faq">FAQ</a> •
  <a href="#-contributing">Contributing</a>

</div>

<br/>

---

## 🤔 Why This Project?

Reading comprehension is a foundational skill across every level of education, yet creating
high-quality exercises at the right difficulty level is time-consuming and often inconsistent.
This project solves that problem by leveraging a **local LLM** to generate calibrated,
multi-level reading exercises — instantly and privately.

| Challenge | Traditional Approach | This Project |
|-----------|---------------------|--------------|
| **Creating passages at the right level** | Manual writing by educators; hours per passage | AI generates level-calibrated passages (200–700 words) in seconds |
| **Diverse question types** | Limited to what the author remembers to include | Automatically produces 5 question types: factual, inferential, analytical, vocabulary, main-idea |
| **Consistent scoring** | Subjective grading varies by teacher | Standardized 4-level rubric with percentage-based scoring |
| **Vocabulary support** | Separate vocabulary lists maintained manually | Key terms auto-extracted with definitions alongside every passage |
| **Privacy & cost** | Cloud APIs charge per token and send student data externally | 100% local inference with Ollama — zero cost, full privacy |

> 💡 **Built for educators, tutors, homeschool parents, and self-learners** who need
> on-demand reading exercises without the overhead of manual content creation.

---

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Key Features Overview" width="800"/>
</div>

<br/>

<table>
  <tr>
    <td width="50%">

### 📖 Smart Passage Generation
Generate reading passages on **any topic** — from ancient history to quantum
physics. The AI calibrates vocabulary complexity, sentence structure, and
passage length to match the selected reading level (elementary through college).

</td>
    <td width="50%">

### ❓ Multi-Type Question Engine
Each exercise includes a configurable number of questions spanning **five cognitive
levels**: factual recall, inferential reasoning, analytical thinking, vocabulary
in context, and main-idea identification — ensuring comprehensive comprehension
assessment.

</td>
  </tr>
  <tr>
    <td width="50%">

### 🏆 Structured Scoring Rubric
Every exercise ships with a **four-level scoring rubric** (Excellent, Good, Fair,
Needs Improvement) that maps percentage scores to qualitative feedback, making
it easy for students to understand exactly where they stand.

</td>
    <td width="50%">

### 🔑 Detailed Answer Explanations
The answer key doesn't just list correct answers — it provides **explanations**
for why each answer is correct and includes **passage annotations** pointing to
the relevant text, turning every exercise into a learning opportunity.

</td>
  </tr>
</table>

### Additional Capabilities

| Feature | Description |
|---------|-------------|
| 🎮 **Interactive Quiz Mode** | Answer questions directly in the CLI with `--interactive` and get instant scoring |
| 🌐 **Streamlit Web UI** | Full-featured web dashboard for generating, answering, and scoring exercises |
| 📝 **Vocabulary Extraction** | Key terms automatically extracted with definitions for each passage |
| 💾 **JSON Export** | Save exercises to JSON for sharing, archiving, or integration with other tools |
| ⚙️ **YAML Configuration** | Centralized `config.yaml` for LLM settings, temperature, and token limits |
| 🔒 **100% Local** | All inference runs on your machine via Ollama — no cloud APIs, no data leaving your network |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.9+ | Runtime |
| **Ollama** | Latest | Local LLM server |
| **Gemma 3** | 4B+ recommended | Language model |

### 1. Clone & Install

```bash
git clone https://github.com/kennedyraju55/reading-comprehension-builder.git
cd reading-comprehension-builder
pip install -e ".[dev]"
```

### 2. Start Ollama

```bash
# Install Ollama from https://ollama.com
ollama serve

# Pull the Gemma 3 model (in a separate terminal)
ollama pull gemma3
```

### 3. Verify Setup

```bash
# Check that the LLM service is reachable
python -c "from reading_comp.core import check_service; print('✅ Ready!' if check_service() else '❌ Ollama not running')"
```

### 4. Generate Your First Exercise

```bash
reading-comp generate --topic "The Solar System" --level "middle school" --questions 5
```

---

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and exposes two main commands.

### `reading-comp generate`

Generate a reading comprehension exercise on any topic.

```
Usage: reading-comp generate [OPTIONS]

Options:
  -t, --topic TEXT        Topic for the reading passage (required)
  -l, --level TEXT        Reading level [elementary|middle school|high school|college]
                          (default: middle school)
  -q, --questions INT     Number of questions to generate (default: 5)
  --length TEXT           Passage length [short|medium|long] (default: medium)
  -i, --interactive       Enter interactive quiz mode after generation
  -a, --show-answers      Display the answer key immediately
  -o, --output FILE       Save exercise to a JSON file
  --help                  Show this message and exit
```

#### Examples

```bash
# Basic generation
reading-comp generate --topic "Climate Change" --level "high school"

# Interactive quiz mode — answer questions and get scored
reading-comp generate --topic "Space Exploration" --level college --interactive

# Generate and immediately show the answer key
reading-comp generate --topic "Ancient Egypt" --level "middle school" --show-answers

# Generate a short elementary passage with 3 questions
reading-comp generate -t "Farm Animals" -l elementary -q 3 --length short

# Save exercise to file for later use
reading-comp generate --topic "Marine Biology" --output exercise.json
```

### `reading-comp answer-key`

Display the answer key for a previously saved exercise.

```
Usage: reading-comp answer-key [OPTIONS]

Options:
  -f, --file FILE    Path to a saved exercise JSON file (required)
  --help             Show this message and exit
```

#### Example

```bash
# View answers and explanations for a saved exercise
reading-comp answer-key --file exercise.json
```

**Sample Output:**

```
┌─────────────────────────────────────────────────┐
│              📋 Answer Key                      │
├────┬──────────────┬────────┬────────────────────┤
│  # │ Type         │ Answer │ Explanation        │
├────┼──────────────┼────────┼────────────────────┤
│  1 │ factual      │ B      │ The passage states │
│    │              │        │ that Mars has two   │
│    │              │        │ moons…             │
│  2 │ inferential  │ C      │ Based on the       │
│    │              │        │ description of…    │
│  3 │ vocabulary   │ A      │ In this context,   │
│    │              │        │ "terrestrial"…     │
│  4 │ analytical   │ D      │ The author's use   │
│    │              │        │ of contrast…       │
│  5 │ main-idea    │ B      │ The central theme  │
│    │              │        │ revolves around…   │
└────┴──────────────┴────────┴────────────────────┘
```

---

## 🌐 Web UI

Launch the Streamlit web interface for a graphical experience:

```bash
streamlit run src/reading_comp/web_ui.py
```

### Web UI Capabilities

| Feature | Description |
|---------|-------------|
| 📝 **Topic Input** | Enter any topic or paste custom text |
| 🎚️ **Level Selector** | Choose from 4 reading levels via dropdown |
| 📖 **Passage Display** | Clean reading view with highlighted vocabulary |
| ❓ **Interactive Questions** | Answer via radio buttons / dropdowns |
| 📊 **Score Dashboard** | Instant scoring with rubric feedback |
| 🔑 **Answer Reveal** | Show/hide explanations per question |
| 💾 **Export** | Download exercise as JSON |

---

## 🏗️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="System Architecture Diagram" width="800"/>
</div>

<br/>

### How It Works

1. **User** selects a topic, reading level, and number of questions via CLI or Web UI
2. **Core Engine** (`core.py`) constructs a calibrated prompt based on the difficulty level
3. **Ollama/Gemma** generates the passage, questions, vocabulary, and annotations
4. **Core Engine** parses the LLM response into structured `ReadingExercise` dataclass
5. **User** answers questions interactively (CLI `--interactive` or Web UI)
6. **Scoring Engine** evaluates answers against the answer key and applies the rubric

### Project Structure

```
60-reading-comprehension-builder/
├── src/
│   └── reading_comp/             # Main package
│       ├── __init__.py           # Package metadata & exports
│       ├── core.py               # Business logic: generate, score, answer key
│       ├── cli.py                # Click-based CLI (generate, answer-key)
│       └── web_ui.py             # Streamlit web interface
├── common/
│   └── llm_client.py            # Shared Ollama HTTP client
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core logic & scoring
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/                  # SVG diagrams & assets
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml                  # LLM & application configuration
├── setup.py                     # Package installation & entry points
├── Makefile                     # Development task shortcuts
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
├── .gitignore
└── README.md                    # This file
```

---

## 📚 API Reference

The core module (`reading_comp.core`) exposes dataclasses and functions that can be
used programmatically in your own Python scripts or applications.

### Dataclasses

#### `VocabularyWord`

A single vocabulary term extracted from the passage.

```python
from dataclasses import dataclass

@dataclass
class VocabularyWord:
    word: str          # The vocabulary term
    definition: str    # Context-appropriate definition
```

**Example:**

```python
vocab = VocabularyWord(
    word="photosynthesis",
    definition="The process by which green plants convert sunlight into energy"
)
print(f"{vocab.word}: {vocab.definition}")
# photosynthesis: The process by which green plants convert sunlight into energy
```

---

#### `Question`

A single comprehension question with multiple-choice options.

```python
@dataclass
class Question:
    number: int           # Question number (1-based)
    type: str             # "factual" | "inferential" | "analytical" | "vocabulary" | "main-idea"
    question: str         # The question text
    options: list         # Multiple-choice options (A, B, C, D)
    answer: str           # Correct answer letter
    explanation: str      # Why this answer is correct
    difficulty: str       # Difficulty label
    annotation: str       # Relevant passage excerpt
```

**Example:**

```python
q = Question(
    number=1,
    type="factual",
    question="What is the primary function of mitochondria?",
    options=["A) Protein synthesis", "B) Energy production", "C) Cell division", "D) Waste removal"],
    answer="B",
    explanation="The passage states that mitochondria are the 'powerhouses of the cell'.",
    difficulty="middle school",
    annotation="Mitochondria generate most of the cell's supply of ATP..."
)
```

---

#### `ScoringRubric`

A single level in the scoring rubric.

```python
@dataclass
class ScoringRubric:
    level: str            # "Excellent" | "Good" | "Fair" | "Needs Improvement"
    min_score: int        # Minimum percentage (inclusive)
    max_score: int        # Maximum percentage (inclusive)
    description: str      # What this level means
    feedback: str         # Feedback message for the student
```

**Default Rubric Levels:**

| Level | Range | Description | Feedback |
|-------|-------|-------------|----------|
| 🌟 Excellent | 90–100% | Outstanding comprehension | Demonstrates thorough understanding of the passage |
| ✅ Good | 70–89% | Strong comprehension with minor gaps | Shows solid grasp with some areas for review |
| ⚠️ Fair | 50–69% | Basic understanding, missing key details | Understands main ideas but misses important details |
| ❌ Needs Improvement | 0–49% | Below expectations | Significant gaps in comprehension; re-read recommended |

---

#### `ReadingExercise`

The complete exercise returned by `generate_comprehension()`.

```python
@dataclass
class ReadingExercise:
    title: str                              # Exercise title
    topic: str                              # User-specified topic
    reading_level: str                      # Calibrated reading level
    passage: str                            # The generated reading passage
    word_count: int                         # Passage word count
    vocabulary_words: list[VocabularyWord]   # Extracted vocabulary
    questions: list[Question]               # Comprehension questions
    summary: str                            # Brief passage summary
    annotations: list                       # Passage annotations
    scoring_rubric: list[ScoringRubric]     # 4-level rubric

    def to_dict(self) -> dict:
        """Serialize the exercise to a dictionary (JSON-compatible)."""
        ...
```

---

### Core Functions

#### `generate_comprehension(topic, level, num_questions, passage_length) → ReadingExercise`

Generate a complete reading comprehension exercise.

```python
from reading_comp.core import generate_comprehension

exercise = generate_comprehension(
    topic="The Renaissance",
    level="high school",
    num_questions=5,
    passage_length="medium"
)

print(exercise.title)
print(f"Passage: {exercise.word_count} words")
print(f"Questions: {len(exercise.questions)}")
print(f"Vocabulary: {len(exercise.vocabulary_words)} words")
```

---

#### `score_exercise(exercise, user_answers) → Dict`

Score a user's answers against the exercise answer key.

```python
from reading_comp.core import score_exercise

results = score_exercise(exercise, user_answers=["B", "C", "A", "D", "B"])

print(f"Score: {results['score']}/{results['total']}")
print(f"Percentage: {results['percentage']}%")
print(f"Level: {results['rubric_level']}")
print(f"Feedback: {results['feedback']}")
```

**Return Value:**

```python
{
    "score": 4,                  # Number correct
    "total": 5,                  # Total questions
    "percentage": 80.0,          # Percentage score
    "rubric_level": "Good",      # Rubric classification
    "feedback": "Strong comprehension with minor gaps",
    "details": [                 # Per-question breakdown
        {"question": 1, "correct": True,  "user_answer": "B", "correct_answer": "B"},
        {"question": 2, "correct": True,  "user_answer": "C", "correct_answer": "C"},
        {"question": 3, "correct": True,  "user_answer": "A", "correct_answer": "A"},
        {"question": 4, "correct": False, "user_answer": "D", "correct_answer": "B"},
        {"question": 5, "correct": True,  "user_answer": "B", "correct_answer": "B"},
    ]
}
```

---

#### `get_answer_key(exercise) → list[Dict]`

Extract the answer key from an exercise.

```python
from reading_comp.core import get_answer_key

key = get_answer_key(exercise)
for item in key:
    print(f"Q{item['number']} ({item['type']}): {item['answer']} — {item['explanation']}")
```

---

#### `check_service() → bool`

Verify that the Ollama LLM service is running and reachable.

```python
from reading_comp.core import check_service

if check_service():
    print("✅ Ollama is running")
else:
    print("❌ Start Ollama with: ollama serve")
```

---

#### `load_config(path) → dict`

Load application configuration from a YAML file.

```python
from reading_comp.core import load_config

config = load_config("config.yaml")
print(f"Temperature: {config['llm']['temperature']}")
print(f"Max tokens: {config['llm']['max_tokens']}")
```

---

## ⚙️ Configuration

### Difficulty Calibration

The system automatically calibrates passage complexity based on the selected reading level:

| Level | Target Words | Question Types | Vocabulary Complexity | Sentence Structure |
|-------|-------------|----------------|----------------------|-------------------|
| **Elementary** | ~200 words | Factual, Vocabulary, Main-Idea | Simple, everyday words | Short, declarative sentences |
| **Middle School** | ~350 words | + Inferential | Grade-appropriate terms | Compound sentences introduced |
| **High School** | ~500 words | + Analytical | Academic vocabulary | Complex & compound-complex |
| **College** | ~700 words | Emphasizes Inferential & Analytical | Domain-specific terminology | Sophisticated, multi-clause |

### LLM Settings (`config.yaml`)

```yaml
llm:
  temperature: 0.7      # Controls creativity/randomness (0.0–1.0)
  max_tokens: 8192       # Maximum response length from the model
```

| Parameter | Default | Description |
|-----------|---------|-------------|
| `temperature` | `0.7` | Higher values = more creative passages; lower = more focused |
| `max_tokens` | `8192` | Increase for longer passages or more questions |

---

## 🧪 Testing

Run the test suite with pytest:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=src/reading_comp --cov-report=term-missing

# Run only core logic tests
pytest tests/test_core.py -v

# Run only CLI tests
pytest tests/test_cli.py -v
```

### Test Structure

| File | Covers |
|------|--------|
| `tests/test_core.py` | `generate_comprehension()`, `score_exercise()`, `get_answer_key()`, dataclass validation, rubric scoring edge cases |
| `tests/test_cli.py` | CLI argument parsing, `generate` command, `answer-key` command, error handling |

---

## 🏠 Local LLM vs. Cloud AI

| Aspect | Local LLM (This Project) | Cloud AI (GPT-4, Claude, etc.) |
|--------|--------------------------|-------------------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Sent to third-party servers |
| **Cost** | ✅ Free after hardware investment | ❌ Pay-per-token pricing |
| **Speed** | ⚡ Low latency on modern GPUs | 🌐 Network-dependent latency |
| **Internet** | ✅ Works fully offline | ❌ Requires internet connection |
| **Customization** | ✅ Fine-tune models locally | ⚠️ Limited to API parameters |
| **Student Data** | ✅ FERPA/COPPA friendly by design | ⚠️ Requires compliance review |
| **Quality** | ⚠️ Depends on model size | ✅ State-of-the-art accuracy |
| **Setup** | ⚠️ Requires Ollama + model download | ✅ API key and go |

> 🔒 **For educational environments**, local LLMs offer an unmatched combination of
> **privacy**, **cost savings**, and **compliance** with student data regulations.

---

## ❓ FAQ

<details>
<summary><strong>What models are supported?</strong></summary>

<br/>

This project is designed for **Gemma 3** running via **Ollama**, but it works with any
Ollama-compatible model. To use a different model, update the model name in `config.yaml`
or the `common/llm_client.py` configuration.

Popular alternatives:
- `gemma3` (recommended, 4B+ parameters)
- `llama3.1` (Meta's Llama)
- `mistral` (Mistral AI)
- `phi3` (Microsoft)

</details>

<details>
<summary><strong>How do I adjust the difficulty of generated passages?</strong></summary>

<br/>

Use the `--level` flag with one of four options:

```bash
reading-comp generate --topic "Volcanoes" --level elementary    # ~200 words, simple
reading-comp generate --topic "Volcanoes" --level "middle school" # ~350 words
reading-comp generate --topic "Volcanoes" --level "high school"   # ~500 words
reading-comp generate --topic "Volcanoes" --level college        # ~700 words, complex
```

The system automatically calibrates vocabulary complexity, sentence structure,
passage length, and question types for each level.

</details>

<details>
<summary><strong>Can I use my own passage instead of generating one?</strong></summary>

<br/>

Yes! The **Streamlit Web UI** supports pasting your own custom text as the reading
passage. The system will then generate questions, vocabulary, and scoring rubrics
based on your provided text. In the CLI, you can save exercises as JSON and modify
the passage field before loading it back with `answer-key`.

</details>

<details>
<summary><strong>How does the scoring rubric work?</strong></summary>

<br/>

The scoring engine uses a **four-level rubric** based on percentage scores:

| Level | Score Range | What It Means |
|-------|------------|---------------|
| 🌟 Excellent | 90–100% | Outstanding comprehension of all aspects |
| ✅ Good | 70–89% | Strong understanding with minor gaps |
| ⚠️ Fair | 50–69% | Basic grasp but missing key details |
| ❌ Needs Improvement | 0–49% | Significant gaps; re-reading recommended |

Call `score_exercise(exercise, user_answers)` to get a full breakdown including
per-question results and the applicable rubric level.

</details>

<details>
<summary><strong>What are the hardware requirements?</strong></summary>

<br/>

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 8 GB | 16 GB+ |
| **Storage** | 5 GB (for model) | 10 GB+ |
| **GPU** | Not required (CPU works) | NVIDIA GPU with 6GB+ VRAM |
| **CPU** | Any modern x86/ARM | Apple Silicon M1+ or modern Intel/AMD |

Ollama handles all model management. Larger models (12B+) provide better quality
but require more RAM/VRAM. The 4B Gemma 3 model works well on most machines.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/reading-comprehension-builder.git
cd reading-comprehension-builder

# Install in development mode
pip install -e ".[dev]"

# Run tests to verify everything works
pytest tests/ -v
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes with tests
4. **Run** the test suite: `pytest tests/ -v`
5. **Commit** with a descriptive message
6. **Push** and open a **Pull Request**

### Areas for Contribution

| Area | Ideas |
|------|-------|
| 🧪 **Testing** | Increase coverage, add edge case tests |
| 📖 **Reading Levels** | Add ESL / advanced-academic levels |
| 🌐 **Web UI** | Enhanced Streamlit components, charts, progress tracking |
| 🔧 **Models** | Support for additional LLM providers |
| 📊 **Analytics** | Track student progress over multiple exercises |
| 🌍 **i18n** | Multi-language passage generation |

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

  <strong>📚 Reading Comprehension Builder</strong>
  <br/>
  <sub>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</sub>
  <br/><br/>
  <sub>Built with ❤️ using Python, Ollama, and Gemma 3</sub>
  <br/>
  <sub>
    <a href="https://github.com/kennedyraju55/reading-comprehension-builder/issues">Report Bug</a> •
    <a href="https://github.com/kennedyraju55/reading-comprehension-builder/issues">Request Feature</a> •
    <a href="https://github.com/kennedyraju55/reading-comprehension-builder">⭐ Star This Repo</a>
  </sub>

</div>
