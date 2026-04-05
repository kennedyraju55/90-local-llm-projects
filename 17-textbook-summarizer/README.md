<div align="center">

<img src="docs/images/banner.svg" alt="Textbook Summarizer Banner" width="800"/>

<br/><br/>

<img src="https://img.shields.io/badge/Gemma_4-Ollama-orange?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/Rich-Terminal_UI-purple?style=flat-square" alt="Rich"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<img src="https://img.shields.io/badge/Privacy-100%25_Local-brightgreen?style=flat-square&logo=lock&logoColor=white" alt="Privacy"/>

<br/><br/>

<strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

<br/>

*Turn dense textbook chapters into structured summaries, glossaries, concept maps, and quizzes — all locally with Gemma 4.*

</div>

---

## 📑 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
  - [CLI Reference](#cli-reference)
  - [Summary Styles](#summary-styles)
  - [Glossary Generation](#glossary-generation)
  - [Concept Map Generation](#concept-map-generation)
  - [Quiz Generation](#quiz-generation)
  - [Multi-Chapter Processing](#multi-chapter-processing)
- [Configuration](#%EF%B8%8F-configuration)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [How It Works](#-how-it-works)
- [FAQ](#-frequently-asked-questions)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 💡 Why This Project?

Students spend **hours** reading dense textbook chapters, often struggling to identify what matters most. Highlighting and re-reading feel productive but rarely translate into deep understanding. Meanwhile, the most effective study techniques — active recall, spaced repetition, self-quizzing — require materials that most students never create because it takes too long.

**Textbook Summarizer** bridges that gap. Paste a chapter into a text file, run a single command, and get back:

- A **structured summary** (concise bullets, detailed paragraphs, or a flashcard-style study guide)
- An **auto-generated glossary** of every key term with definitions
- A **concept map** showing how ideas relate to each other
- A **quiz** with multiple-choice, short-answer, and critical-thinking questions — with answers

Everything runs **100% locally** through Ollama and Gemma 4. No cloud APIs, no subscriptions, no student data leaving your machine. Your study materials, your privacy.

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Feature | Description | Function |
|---------|-------------|----------|
| 📝 **3 Summary Styles** | Concise bullets, detailed paragraphs, or study-guide Q&A | `summarize_chapter()` |
| 📖 **Glossary Generator** | Extracts key terms with clear, contextual definitions | `generate_glossary()` |
| 🗺️ **Concept Maps** | Visual relationship mapping between chapter concepts | `generate_concept_map()` |
| ❓ **Quiz Generator** | Multiple choice, short answer, and critical thinking questions | `generate_study_questions()` |
| 📚 **Multi-Chapter** | Batch processing of entire textbooks with automatic chapter detection | `summarize_multi_chapter()` |
| 🔒 **100% Private** | All processing runs locally — student data never leaves your machine | Ollama + Gemma 4 |
| 🔍 **Chapter Detection** | Recognizes Chapter, Ch., Unit, and Lesson heading formats | `detect_chapter_info()` |
| ⚙️ **YAML Configuration** | Customize model, temperature, token limits, and defaults | `config.yaml` |

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800"/>
</div>

<br/>

The pipeline flows through five stages:

1. **Input** — `read_chapter_file(filepath)` reads the raw `.txt` chapter file
2. **Detection** — `detect_chapter_info(text)` uses regex patterns to identify chapter numbers and titles (supports `Chapter`, `Ch.`, `Unit`, and `Lesson` formats)
3. **LLM Engine** — Gemma 4 via Ollama processes the text through style-specific prompts to generate summaries, glossaries, concept maps, and quiz questions
4. **Output** — Results are rendered in the terminal using Rich panels, markdown formatting, and color-coded sections
5. **Export** — Study materials are output as structured markdown

---

## 🚀 Quick Start

Get up and running in under two minutes:

```bash
# 1. Clone and navigate
git clone https://github.com/kennedyraju55/textbook-summarizer.git
cd textbook-summarizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start Ollama and pull the model
ollama serve
ollama pull gemma4

# 4. Summarize a chapter
python -m src.textbook_summarizer.cli --file chapter.txt

# 5. Generate everything — summary, glossary, concept map, quiz
python -m src.textbook_summarizer.cli --file chapter.txt \
    --glossary --concept-map --quiz
```

---

## 📦 Installation

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | Latest | Language model |

### Step-by-Step

**1. Clone the repository:**

```bash
git clone https://github.com/kennedyraju55/textbook-summarizer.git
cd textbook-summarizer
```

**2. Install Python dependencies:**

```bash
pip install -r requirements.txt
```

This installs:
- **Click** — CLI framework for argument parsing and command structure
- **Rich** — Terminal formatting with panels, markdown rendering, and progress spinners
- **Ollama** — Python client for the local Ollama LLM server
- **Regex** — Pattern matching for chapter detection
- **PyYAML** — Configuration file parsing

**3. Install and start Ollama:**

```bash
# Install Ollama (see https://ollama.com for platform-specific instructions)
# Then start the server and pull the model:
ollama serve
ollama pull gemma4
```

**4. Verify the installation:**

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --verbose
```

If Ollama is running and the model is pulled, you should see the summarizer process your chapter and display structured output in the terminal.

---

## 📖 Usage

### CLI Reference

The CLI uses a single command with flags to control output:

```bash
python -m src.textbook_summarizer.cli [OPTIONS]
```

| Option | Type | Required | Default | Description |
|--------|------|----------|---------|-------------|
| `--file` | `PATH` | ✅ Yes | — | Path to the textbook chapter text file |
| `--style` | `CHOICE` | No | `concise` | Summary style: `concise`, `detailed`, or `study-guide` |
| `--multi-chapter` | `FLAG` | No | — | Process file as a multi-chapter textbook |
| `--glossary` | `FLAG` | No | — | Generate a key terms glossary |
| `--concept-map` | `FLAG` | No | — | Generate a concept map |
| `--quiz` | `FLAG` | No | — | Generate study questions |
| `--num-questions` | `INT` | No | `5` | Number of quiz questions to generate |
| `--config` | `PATH` | No | — | Path to a custom `config.yaml` |
| `--verbose` | `FLAG` | No | — | Enable debug logging output |

---

### Summary Styles

Textbook Summarizer supports three distinct summary styles, each designed for a different stage of the study process.

#### Concise (`--style concise`)

Best for: **Quick review before exams**, getting the gist of a chapter.

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --style concise
```

Output structure:
- **Key Concepts** — Bullet-point list of the most important ideas
- **Definitions** — `**Term**: Brief definition` (one sentence max)
- **Formulas & Equations** — Any formulas found, or "None found."
- **Summary** — 3-5 sentence chapter overview
- **Review Questions** — 3-5 short review questions

#### Detailed (`--style detailed`)

Best for: **Deep understanding**, research papers, thorough exam prep.

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --style detailed
```

Output structure:
- **Key Concepts** — Full paragraph explanation per concept with examples
- **Definitions** — Terms with context, usage, and examples
- **Formulas & Equations** — Formulas with variable explanations and application context
- **Summary** — 8-12 sentence comprehensive overview
- **Critical Thinking Questions** — 5-8 thought-provoking questions mixing factual recall and analysis

#### Study Guide (`--style study-guide`)

Best for: **Active recall practice**, flashcard creation, self-quizzing.

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --style study-guide
```

Output structure:
- **Key Concepts (Q&A)** — Question-and-answer format for each concept
- **Definitions (Flashcards)** — `Q: What is [term]? A: Definition and explanation`
- **Formulas & Equations** — `Q: What formula is used for [purpose]? A: Formula with explanation`
- **Summary** — 4-6 sentence quick-review summary
- **Practice Questions** — 5-8 questions with answers, easy to challenging

---

### Glossary Generation

Generate a standalone key terms glossary from any chapter:

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --glossary
```

The `generate_glossary(text, config=None)` function extracts all key terms and produces output in the format:

```
- **Term**: Definition
- **Another Term**: Definition with context
```

The glossary appears in a Rich panel titled "📖 Key Terms Glossary" with a green border in the terminal.

---

### Concept Map Generation

Visualize how concepts in a chapter relate to each other:

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --concept-map
```

The `generate_concept_map(text, config=None)` function produces a text-based concept map:

```
**Main Concept** → Related Concept 1, Related Concept 2
**Related Concept 1** → Sub-concept A, Sub-concept B
```

This is rendered in a Rich panel titled "🗺️ Concept Map" with a yellow border.

---

### Quiz Generation

Generate study questions with answers from chapter content:

```bash
# Default: 5 questions
python -m src.textbook_summarizer.cli --file chapter.txt --quiz

# Custom question count
python -m src.textbook_summarizer.cli --file chapter.txt --quiz --num-questions 10
```

The `generate_study_questions(text, num_questions=5, config=None)` function generates a mix of:

- **Multiple Choice** — 4 options with the correct answer indicated
- **Short Answer** — Direct factual questions with concise answers
- **Critical Thinking** — Open-ended questions requiring analysis and synthesis

Questions appear in a Rich panel titled "❓ Study Questions" with a magenta border.

---

### Multi-Chapter Processing

Process an entire textbook file with multiple chapters in a single run:

```bash
python -m src.textbook_summarizer.cli --file textbook.txt --multi-chapter
```

The `summarize_multi_chapter(filepath, style="concise", config=None)` function:

1. Reads the entire file with `read_chapter_file(filepath)`
2. Splits it into individual chapters using `split_chapters(text)` (regex-based detection)
3. Summarizes each chapter independently with `summarize_chapter()`
4. Returns a list of dictionaries, each containing:
   - `title` — Detected chapter title
   - `summary` — Generated summary text
   - `word_count` — Word count of the original chapter text

You can combine `--multi-chapter` with any other flags:

```bash
# Multi-chapter with detailed style and all study aids
python -m src.textbook_summarizer.cli --file textbook.txt \
    --multi-chapter \
    --style detailed \
    --glossary \
    --concept-map \
    --quiz \
    --num-questions 8
```

---

## ⚙️ Configuration

Customize behavior through `config.yaml`:

```yaml
# Textbook Summarizer Configuration
llm:
  model: gemma4
  temperature: 0.4
  max_tokens: 4096

summarizer:
  styles:
    - concise
    - detailed
    - study-guide
  default_style: concise
  max_chapter_words: 50000
  generate_glossary: true
  generate_concept_map: true
  generate_study_questions: true
  num_study_questions: 5
```

### Configuration Options

| Key | Default | Description |
|-----|---------|-------------|
| `llm.model` | `gemma4` | Ollama model name |
| `llm.temperature` | `0.4` | LLM creativity (0.0 = deterministic, 1.0 = creative) |
| `llm.max_tokens` | `4096` | Maximum response length in tokens |
| `summarizer.default_style` | `concise` | Default summary style when `--style` is not specified |
| `summarizer.max_chapter_words` | `50000` | Maximum words per chapter before truncation |
| `summarizer.num_study_questions` | `5` | Default number of quiz questions |

Pass a custom config file:

```bash
python -m src.textbook_summarizer.cli --file chapter.txt --config my_config.yaml
```

---

## 📚 API Reference

### `read_chapter_file(filepath)`

Read and return the contents of a textbook chapter file.

```python
from textbook_summarizer.core import read_chapter_file

text = read_chapter_file("biology_ch3.txt")
# Returns: chapter text as a string
# Raises: FileNotFoundError if the file does not exist
```

---

### `detect_chapter_info(text)`

Detect chapter number and title from the text. Searches the first 10 lines for patterns matching:
- `Chapter 3: Cell Biology`
- `Ch. 5 — Thermodynamics`
- `Unit 2: Linear Algebra`
- `Lesson 7: The French Revolution`

```python
from textbook_summarizer.core import detect_chapter_info

info = detect_chapter_info(text)
# Returns: "Chapter 3: Cell Biology" or "Unknown Chapter"
```

---

### `summarize_chapter(text, style="concise", config=None)`

Generate a structured summary of a textbook chapter using the LLM.

```python
from textbook_summarizer.core import summarize_chapter

# Concise summary (default)
summary = summarize_chapter(text)

# Detailed summary
summary = summarize_chapter(text, style="detailed")

# Study guide with custom config
summary = summarize_chapter(text, style="study-guide", config=config)
```

**Parameters:**
- `text` (str) — Full chapter text
- `style` (str) — `"concise"`, `"detailed"`, or `"study-guide"`
- `config` (dict, optional) — Configuration dictionary

**Returns:** LLM-generated summary as a string

**Raises:** `ValueError` if style is not one of the three valid options

---

### `summarize_multi_chapter(filepath, style="concise", config=None)`

Summarize all chapters found in a multi-chapter textbook file.

```python
from textbook_summarizer.core import summarize_multi_chapter

results = summarize_multi_chapter("full_textbook.txt", style="detailed")
for chapter in results:
    print(f"{chapter['title']} ({chapter['word_count']} words)")
    print(chapter['summary'])
```

**Parameters:**
- `filepath` (str) — Path to the textbook file
- `style` (str) — Summary style
- `config` (dict, optional) — Configuration dictionary

**Returns:** List of dicts with `title`, `summary`, and `word_count` keys

---

### `generate_glossary(text, config=None)`

Generate a key terms glossary from chapter text.

```python
from textbook_summarizer.core import generate_glossary

glossary = generate_glossary(text)
# Returns markdown formatted as:
# - **Term**: Definition
# - **Another Term**: Definition
```

---

### `generate_concept_map(text, config=None)`

Generate a text-based concept map showing relationships between chapter concepts.

```python
from textbook_summarizer.core import generate_concept_map

concept_map = generate_concept_map(text)
# Returns markdown formatted as:
# **Main Concept** → Related Concept 1, Related Concept 2
# **Related Concept 1** → Sub-concept A, Sub-concept B
```

---

### `generate_study_questions(text, num_questions=5, config=None)`

Generate study/quiz questions from chapter content with a mix of question types.

```python
from textbook_summarizer.core import generate_study_questions

# Default 5 questions
questions = generate_study_questions(text)

# Custom count
questions = generate_study_questions(text, num_questions=10)
```

**Parameters:**
- `text` (str) — Chapter text content
- `num_questions` (int) — Number of questions to generate (default: 5)
- `config` (dict, optional) — Configuration dictionary

**Returns:** Mixed question set (multiple choice, short answer, critical thinking) with answers

---

## 📁 Project Structure

```
17-textbook-summarizer/
├── src/
│   └── textbook_summarizer/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Core summarization logic & LLM calls
│       ├── cli.py               # Click CLI interface with Rich output
│       ├── web_ui.py            # Streamlit web interface
│       ├── config.py            # YAML configuration loader
│       └── utils.py             # Helpers (chapter splitting, word count)
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Unit tests for core functions
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # Pipeline architecture diagram
│       └── features.svg         # Feature overview grid
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup with entry points
├── requirements.txt             # Python dependencies
├── Makefile                     # Build and test shortcuts
├── .env.example                 # Environment variable template
├── .gitignore
└── README.md                    # This file
```

### Key Files

| File | Purpose |
|------|---------|
| `core.py` | All seven core functions: `read_chapter_file`, `detect_chapter_info`, `summarize_chapter`, `summarize_multi_chapter`, `generate_glossary`, `generate_concept_map`, `generate_study_questions` |
| `cli.py` | Click command with `--file`, `--style`, `--multi-chapter`, `--glossary`, `--concept-map`, `--quiz`, `--num-questions`, `--config`, `--verbose` flags |
| `config.py` | Loads and merges YAML configuration with sensible defaults |
| `utils.py` | `split_chapters()` for multi-chapter detection, `count_words()` for word counts |

---

## 🧪 Testing

Run the test suite with pytest:

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src/textbook_summarizer

# Run specific test files
python -m pytest tests/test_core.py -v
python -m pytest tests/test_cli.py -v
```

### Using Make

```bash
make test          # Run all tests
make test-cov      # Run tests with coverage report
make lint          # Run linter
```

---

## 🔍 How It Works

### 1. Chapter Reading

`read_chapter_file(filepath)` reads the raw text file. It validates the file exists, handles UTF-8 encoding, and returns the full chapter content as a string.

### 2. Chapter Detection

`detect_chapter_info(text)` scans the first 10 lines of the text for heading patterns using regex:

```python
patterns = [
    r"(?i)^(chapter\s+\d+[\s:.\-]+.+)$",    # Chapter 3: Title
    r"(?i)^(chapter\s+\d+)$",                 # Chapter 3
    r"(?i)^(ch\.?\s*\d+[\s:.\-]+.+)$",        # Ch. 3: Title
    r"(?i)^(unit\s+\d+[\s:.\-]+.+)$",         # Unit 3: Title
    r"(?i)^(lesson\s+\d+[\s:.\-]+.+)$",       # Lesson 3: Title
]
```

If no pattern matches, it returns `"Unknown Chapter"`.

### 3. LLM Summarization

`summarize_chapter(text, style, config)` selects a style-specific prompt template from `STYLE_PROMPTS` and sends it to Gemma 4 via Ollama's `generate()` function. Each style produces a differently structured output:

- **Concise**: Bullets, short definitions, 3-5 sentence summary, 3-5 review questions
- **Detailed**: Full paragraphs, definitions with examples, 8-12 sentence summary, 5-8 critical thinking questions
- **Study Guide**: Q&A flashcard format, practice questions easy → challenging

### 4. Study Aid Generation

Each study aid function (`generate_glossary`, `generate_concept_map`, `generate_study_questions`) sends a specialized prompt to the LLM with format instructions:

- **Glossary**: `**Term**: Definition` format
- **Concept Map**: `**Main Concept** → Related Concept 1, Related Concept 2` format
- **Quiz**: Mixed question types with answers

### 5. Rich Terminal Output

The CLI uses Rich to render all output with:
- Color-coded panels for each section (blue for summaries, green for glossary, yellow for concept maps, magenta for quizzes)
- Markdown rendering inside panels
- Progress spinners during LLM processing
- Word count and chapter detection feedback

---

## ❓ Frequently Asked Questions

### What textbook formats are supported?

Textbook Summarizer works with **plain text files** (`.txt`). Copy and paste your chapter content into a text file. The tool detects chapter headings that follow standard patterns like "Chapter 3: Cell Biology", "Ch. 5 — Thermodynamics", "Unit 2: Linear Algebra", or "Lesson 7: The French Revolution".

### How effective is AI-generated study material?

Research on learning science shows that **active recall** (testing yourself) and **elaborative interrogation** (asking "why?" and "how?") are among the most effective study techniques. Textbook Summarizer generates materials specifically designed for these approaches:

- The **study-guide** style produces flashcard-style Q&A pairs ideal for self-testing
- The **quiz generator** creates questions across difficulty levels for progressive challenge
- **Concept maps** help you see relationships between ideas, improving comprehension
- **Glossaries** provide quick-reference definitions during review

The AI-generated materials serve as a **starting point** — reviewing and correcting them is itself an effective study technique.

### Can I use models other than Gemma 4?

Yes. Change the `llm.model` value in `config.yaml` to any model available in your Ollama installation:

```yaml
llm:
  model: llama3.1    # or mistral, phi3, etc.
```

### How long does summarization take?

Processing time depends on chapter length and your hardware. Typical times on a modern machine:

| Chapter Length | Approximate Time |
|---------------|-----------------|
| 1,000 words | 10-20 seconds |
| 5,000 words | 30-60 seconds |
| 10,000 words | 1-3 minutes |
| 50,000 words | 5-10 minutes |

### Is my data private?

**Yes, 100%.** All processing happens locally on your machine through Ollama. No text is sent to any cloud service, API, or third-party server. Your textbook content and generated study materials stay entirely on your computer.

### Can I process an entire textbook at once?

Yes, use the `--multi-chapter` flag. The tool will automatically detect chapter boundaries and process each chapter independently:

```bash
python -m src.textbook_summarizer.cli --file full_textbook.txt --multi-chapter --style detailed
```

### What if my chapter has no heading?

If `detect_chapter_info()` cannot find a heading pattern in the first 10 lines, it returns `"Unknown Chapter"`. The summarization still works — the heading detection is for display purposes only.

### How do I adjust the summary length?

Use `config.yaml` to control the LLM output:

- `llm.max_tokens` — Increase for longer summaries (default: 4096)
- `llm.temperature` — Lower values (0.2) produce more focused output; higher values (0.7) add more variety
- Choose the `--style detailed` flag for inherently longer output

---

## 🔧 Troubleshooting

### "Ollama is not running"

The CLI checks for a running Ollama server on startup. If you see this error:

```bash
# Start the Ollama server
ollama serve

# Verify it's running
curl http://localhost:11434/api/tags
```

### "File not found" error

Ensure the file path is correct and the file exists:

```bash
# Check the file exists
ls -la chapter.txt

# Use absolute path if needed
python -m src.textbook_summarizer.cli --file /full/path/to/chapter.txt
```

### Slow performance

- **Use a smaller model**: Try `gemma4` (smaller variant) or `phi3` for faster processing
- **Reduce `max_tokens`** in `config.yaml` for shorter output
- **Ensure GPU acceleration**: Check `ollama ps` to verify GPU is being used

### Empty or poor output

- Ensure the input file is not empty and contains readable text
- Try increasing `llm.max_tokens` in `config.yaml`
- Try a lower `llm.temperature` (e.g., `0.3`) for more focused output
- Use `--verbose` to see debug logging

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-improvement`
3. **Make** your changes and add tests
4. **Run** the test suite: `python -m pytest tests/ -v`
5. **Commit** with a descriptive message
6. **Push** and open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/textbook-summarizer.git
cd textbook-summarizer

# Install in development mode
pip install -e ".[dev]"

# Run tests
python -m pytest tests/ -v --cov=src/textbook_summarizer
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

Built with ❤️ using [Ollama](https://ollama.com) · [Gemma 4](https://ai.google.dev/gemma) · [Click](https://click.palletsprojects.com) · [Rich](https://rich.readthedocs.io)

<img src="https://img.shields.io/badge/Made_with-Ollama-fb8500?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PC9zdmc+" alt="Made with Ollama"/>

</div>
