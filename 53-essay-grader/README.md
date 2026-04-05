<div align="center">

<!-- Hero Banner -->
<img src="docs/images/banner.svg" alt="Essay Grader — AI-Powered Essay Assessment & Feedback Platform" width="800"/>

<br/>
<br/>

<!-- Badges -->
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/></a>
<a href="https://ollama.ai/"><img src="https://img.shields.io/badge/Ollama-Local_LLM-1a1a2e?style=for-the-badge&logo=llama&logoColor=white" alt="Ollama"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ec4b6?style=for-the-badge" alt="MIT License"/></a>

<br/>

<a href="https://github.com/kennedyraju55/essay-grader/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square" alt="Tests"/></a>
<a href="https://github.com/kennedyraju55/essay-grader"><img src="https://img.shields.io/badge/PRs-welcome-2ec4b6?style=flat-square" alt="PRs Welcome"/></a>
<a href="https://github.com/kennedyraju55/90-local-llm-projects"><img src="https://img.shields.io/badge/collection-90_Local_LLM_Projects-16213e?style=flat-square" alt="Collection"/></a>
<img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>


<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/><br/>
<br/>

**Production-grade essay grading with multi-rubric support, inline annotations, plagiarism detection, and analytics — powered entirely by a local LLM. No data ever leaves your machine.**

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[Architecture](#-architecture) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration) •
[FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Essay grading is one of the most time-consuming tasks in education. Existing solutions either require sending student work to cloud APIs (raising **privacy concerns**) or provide shallow, rubric-agnostic feedback. This project solves both problems.

| Challenge | Traditional Approach | Essay Grader Solution |
|:----------|:---------------------|:----------------------|
| **Privacy** | Student essays sent to cloud APIs | 🔒 100% local — Ollama + Gemma 3 on your hardware |
| **Consistency** | Rubric drift between graders | 📋 5 structured rubric presets with weighted criteria |
| **Feedback depth** | Generic comments like "needs improvement" | ✏️ Inline annotations pinned to specific passages |
| **Scalability** | One essay at a time, manual copy-paste | ⚡ Batch processing — grade an entire directory in one command |
| **Analytics** | No aggregate view across students | 📊 Grade distribution stats with mean, median, std deviation |

<br/>

---

<br/>

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Feature Overview" width="800"/>
</div>

<br/>

<table>
<tr>
<td width="50%" valign="top">

### 📋 Multi-Rubric Grading

Grade essays against **5 built-in rubric presets** — or define your own. Each rubric contains weighted criteria with max scores and descriptions, ensuring consistent and transparent assessment.

**Presets:** `academic` · `creative_writing` · `argumentative` · `narrative` · `research_paper`

</td>
<td width="50%" valign="top">

### ✏️ Inline Annotations

Get **contextual, passage-level feedback** powered by the LLM. Each annotation is pinned to a specific text segment with a severity level (`info` / `warning` / `error`) and an actionable comment.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔍 Plagiarism Detection

AI-powered originality analysis that identifies **suspicious passages**, detects writing-style shifts, and returns a plagiarism score with a detailed explanation — all without any external API.

</td>
<td width="50%" valign="top">

### 📊 Grade Distribution & Analytics

Track scores across multiple essays with the `GradeDistribution` class. Compute **mean**, **median**, **standard deviation**, and generate summary reports — perfect for classroom-wide analysis.

</td>
</tr>
</table>

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:------------|:--------|:--------|
| [Python](https://www.python.org/) | 3.10+ | Runtime |
| [Ollama](https://ollama.ai/) | Latest | Local LLM server |
| Gemma 3 model | — | Default grading model |

### Installation

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/essay-grader.git
cd essay-grader

# Install dependencies
pip install -r requirements.txt

# (Optional) Install as editable package
pip install -e .
```

### Start Grading

```bash
# 1. Make sure Ollama is running with Gemma 3
ollama serve
ollama pull gemma3

# 2. Grade your first essay
python -m src.essay_grader.cli grade --essay my_essay.txt

# 3. Or launch the web UI
streamlit run src/essay_grader/web_ui.py
```

### Verify Installation

```bash
# Run the test suite
python -m pytest tests/ -v

# List available rubric presets
python -m src.essay_grader.cli rubrics
```

<br/>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/essay-grader.git
cd essay-grader
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
uvicorn src.essay_grader.api:app --reload --port 8000

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

The CLI is built with [Click](https://click.palletsprojects.com/) and provides four commands: **`grade`**, **`rubrics`**, **`report`**, and **`batch`**.

### `grade` — Grade a Single Essay

The primary command. Reads an essay file, evaluates it against a rubric, and outputs a detailed grade report.

```bash
# Basic usage with the default rubric (academic)
python -m src.essay_grader.cli grade --essay essay.txt

# Choose a specific rubric preset
python -m src.essay_grader.cli grade --essay essay.txt --rubric argumentative

# Provide assignment context for more relevant feedback
python -m src.essay_grader.cli grade --essay essay.txt \
    --rubric research_paper \
    --context "Analyze the socioeconomic impacts of climate change"

# Enable inline annotations for passage-level feedback
python -m src.essay_grader.cli grade --essay essay.txt --annotate

# Save results to a JSON file
python -m src.essay_grader.cli grade --essay essay.txt --output grade_result.json

# Save results as a Markdown report
python -m src.essay_grader.cli grade --essay essay.txt --output report.md
```

**Options:**

| Flag | Short | Required | Description |
|:-----|:------|:---------|:------------|
| `--essay` | `-e` | ✅ | Path to the essay text file (`.txt` or `.md`) |
| `--rubric` | `-r` | — | Rubric preset name or comma-separated custom criteria |
| `--context` | `-c` | — | Assignment prompt or context for grading |
| `--output` | `-o` | — | Output file path (`.json` or `.md`) |
| `--annotate` | — | — | Include inline annotations in the output |

### `rubrics` — List Available Presets

```bash
python -m src.essay_grader.cli rubrics
```

Displays all built-in rubric presets with their criteria, weights, and descriptions:

| Preset | Criteria |
|:-------|:---------|
| `academic` | Thesis · Evidence · Analysis · Organization · Grammar |
| `creative_writing` | Voice · Imagery · Plot Structure · Character Development · Originality |
| `argumentative` | Claim · Reasoning · Counter Arguments · Evidence · Persuasion |
| `narrative` | Storytelling · Reflection · Descriptive Language · Structure · Mechanics |
| `research_paper` | Research Question · Literature Review · Methodology · Analysis · Citations · Writing Quality |

### `report` — Generate Reports from Grade Data

Convert existing grade JSON files into formatted reports.

```bash
# Generate a Markdown report
python -m src.essay_grader.cli report --input grade.json --format markdown

# Specify a custom output path
python -m src.essay_grader.cli report --input grade.json --format markdown --output my_report.md

# Output as JSON (reformatted)
python -m src.essay_grader.cli report --input grade.json --format json
```

**Options:**

| Flag | Short | Required | Description |
|:-----|:------|:---------|:------------|
| `--input` | `-i` | ✅ | Path to grade JSON file |
| `--format` | `-f` | — | Output format: `markdown` or `json` (default: `markdown`) |
| `--output` | `-o` | — | Output file path |

### `batch` — Grade Multiple Essays

Process an entire directory of essay files in a single command.

```bash
# Grade all .txt and .md files in a directory
python -m src.essay_grader.cli batch --directory ./essays/

# With a specific rubric and custom output directory
python -m src.essay_grader.cli batch \
    --directory ./essays/ \
    --rubric research_paper \
    --output-dir ./results/
```

**Options:**

| Flag | Short | Required | Default | Description |
|:-----|:------|:---------|:--------|:------------|
| `--directory` | `-d` | ✅ | — | Directory containing essay files |
| `--rubric` | `-r` | — | `academic` | Rubric preset or custom criteria |
| `--output-dir` | `-o` | — | `./reports` | Directory for generated reports |

<br/>

---

<br/>

## 🌐 Web UI

Launch the interactive Streamlit dashboard for a visual grading experience:

```bash
streamlit run src/essay_grader/web_ui.py
```

### Web UI Features

| Feature | Description |
|:--------|:------------|
| **Grade Essay** | Paste text or upload a file, select a rubric, and view detailed results with score breakdowns and annotated feedback |
| **Rubric Builder** | Create custom rubrics with named criteria, weights, and descriptions |
| **Grade History** | Browse past grading sessions and compare scores across essays |
| **Analytics Dashboard** | Visualize grade distributions, criterion averages, and improvement trends |
| **Download Reports** | Export results as JSON or Markdown directly from the UI |

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="System Architecture" width="800"/>
</div>

<br/>

### How It Works

1. **Essay Input** — The user provides an essay via CLI (`--essay file.txt`), the Streamlit web UI, or the Python API.
2. **Interface Layer** — The Click CLI or Streamlit UI parses arguments, loads configuration, and delegates to the core engine.
3. **Core Engine** — `core.py` orchestrates grading by constructing prompts from the selected rubric and sending them to the LLM.
4. **LLM Backend** — Ollama runs Gemma 3 locally, processing the essay and returning structured JSON with scores, feedback, and annotations.
5. **Processing Modules** — Specialized functions handle rubric evaluation, inline annotations, plagiarism detection, and grade distribution analytics.
6. **Export** — Results are packaged into `GradeResult` dataclass instances and exported as JSON, Markdown, or console output.

### Project Structure

```
53-essay-grader/
├── docs/
│   └── images/
│       ├── banner.svg               # Project banner image
│       ├── architecture.svg         # System architecture diagram
│       └── features.svg             # Feature overview graphic
├── src/
│   └── essay_grader/
│       ├── __init__.py              # Package metadata & version
│       ├── core.py                  # Business logic, rubrics, grading engine
│       ├── cli.py                   # Click CLI (grade, rubrics, report, batch)
│       └── web_ui.py                # Streamlit web interface
├── common/
│   └── llm_client.py               # Shared Ollama LLM client
├── tests/
│   ├── __init__.py
│   ├── test_core.py                 # Core logic unit tests
│   └── test_cli.py                  # CLI integration tests
├── config.yaml                      # Application configuration
├── requirements.txt                 # Python dependencies
├── setup.py                         # Package setup
├── Makefile                         # Development shortcuts
├── .env.example                     # Environment variable template
└── README.md                        # This file
```

<br/>

---

<br/>

## 📖 API Reference

Use Essay Grader as a Python library in your own applications.

### Core Functions

#### `grade_essay()`

Grade an essay against a rubric using the local LLM.

```python
from src.essay_grader.core import grade_essay, read_essay

essay_text = read_essay("my_essay.txt")
result = grade_essay(
    essay_text=essay_text,
    rubric="academic",             # Preset name or Rubric instance
    context="Compare and contrast the causes of WWI and WWII",
    temperature=0.3,
    max_tokens=4096,
)

print(f"Score: {result['overall_score']}")
print(f"Grade: {result['grade_letter']}")
for criterion, score in result["criteria_scores"].items():
    print(f"  {criterion}: {score}")
```

#### `generate_annotations()`

Generate inline, passage-level annotations for an essay.

```python
from src.essay_grader.core import generate_annotations

annotations = generate_annotations(
    essay_text="The industrial revolution changed everything...",
    temperature=0.3,
)

for ann in annotations:
    print(f"[{ann.severity}] {ann.text_segment!r}")
    print(f"  → {ann.comment}")
```

#### `check_plagiarism_indicators()`

Run AI-powered plagiarism analysis on an essay.

```python
from src.essay_grader.core import check_plagiarism_indicators

result = check_plagiarism_indicators(
    essay_text="Lorem ipsum dolor sit amet...",
    temperature=0.3,
)

print(f"Plagiarism Score: {result.score}")
print(f"Explanation: {result.explanation}")
for passage in result.suspicious_passages:
    print(f"  ⚠ {passage}")
```

#### `export_grade_report()`

Export grade data to JSON or Markdown.

```python
from src.essay_grader.core import export_grade_report

# Export as Markdown
output_path = export_grade_report(
    grade_data=result,
    output_path="report.md",
    fmt="markdown",
    essay_text=essay_text,
)
print(f"Report saved to: {output_path}")

# Export as JSON
export_grade_report(grade_data=result, output_path="report.json", fmt="json")
```

#### Utility Functions

```python
from src.essay_grader.core import (
    read_essay,
    validate_grade_data,
    calculate_grade_letter,
)

# Read an essay from a file
text = read_essay("essay.txt")

# Validate grade data structure
errors = validate_grade_data(grade_dict)
if errors:
    print("Validation errors:", errors)

# Convert numeric score to letter grade
letter = calculate_grade_letter(score=87.5, scale="default")
print(letter)  # "B+"
```

### Data Classes

#### `RubricCriterion`

Represents a single grading criterion within a rubric.

```python
from src.essay_grader.core import RubricCriterion

criterion = RubricCriterion(
    name="Thesis",
    weight=0.25,
    max_score=10,
    description="Clarity and strength of the central argument",
)
```

| Field | Type | Description |
|:------|:-----|:------------|
| `name` | `str` | Name of the criterion |
| `weight` | `float` | Weight in overall score calculation (0.0–1.0) |
| `max_score` | `int` | Maximum possible score |
| `description` | `str` | What this criterion evaluates |

#### `Rubric`

A collection of criteria that defines how an essay is evaluated.

```python
from src.essay_grader.core import Rubric, RubricCriterion

rubric = Rubric(
    name="custom_rubric",
    criteria=[
        RubricCriterion("Thesis", 0.3, 10, "Central argument"),
        RubricCriterion("Evidence", 0.3, 10, "Supporting evidence"),
        RubricCriterion("Style", 0.2, 10, "Writing style"),
        RubricCriterion("Grammar", 0.2, 10, "Mechanics"),
    ],
    description="A custom rubric for persuasive essays",
)
```

| Field | Type | Description |
|:------|:-----|:------------|
| `name` | `str` | Rubric identifier |
| `criteria` | `list[RubricCriterion]` | List of grading criteria |
| `description` | `str` | Human-readable description |

#### `GradeResult`

The complete result of grading an essay.

```python
# Returned by grade_essay() as a dict — fields map to GradeResult
result = {
    "overall_score": 8.2,
    "grade_letter": "B+",
    "criteria_scores": {"Thesis": 9, "Evidence": 7, ...},
    "strengths": ["Clear thesis", "Good transitions"],
    "weaknesses": ["Needs more evidence in paragraph 3"],
    "suggestions": ["Add primary sources", "Strengthen conclusion"],
    "summary": "A well-structured essay with room for improvement...",
    "annotations": [...],
    "timestamp": "2025-01-15T10:30:00Z",
}
```

| Field | Type | Description |
|:------|:-----|:------------|
| `overall_score` | `float` | Weighted overall score |
| `grade_letter` | `str` | Letter grade (A+ through F) |
| `criteria_scores` | `dict` | Per-criterion scores |
| `strengths` | `list[str]` | Identified strengths |
| `weaknesses` | `list[str]` | Identified weaknesses |
| `suggestions` | `list[str]` | Actionable improvement suggestions |
| `summary` | `str` | Overall assessment summary |
| `annotations` | `list` | Inline annotations (if enabled) |
| `timestamp` | `str` | ISO 8601 timestamp |

#### `InlineAnnotation`

A feedback annotation pinned to a specific text segment.

```python
from src.essay_grader.core import InlineAnnotation

annotation = InlineAnnotation(
    start_pos=42,
    end_pos=78,
    text_segment="The data clearly shows that...",
    annotation_type="evidence",
    comment="Consider citing the specific dataset or study",
    severity="warning",  # "info" | "warning" | "error"
)
```

| Field | Type | Description |
|:------|:-----|:------------|
| `start_pos` | `int` | Start character position in the essay |
| `end_pos` | `int` | End character position in the essay |
| `text_segment` | `str` | The annotated text passage |
| `annotation_type` | `str` | Category of the annotation |
| `comment` | `str` | Feedback comment |
| `severity` | `str` | Severity level: `info`, `warning`, or `error` |

#### `PlagiarismIndicator`

Results of plagiarism analysis.

```python
from src.essay_grader.core import PlagiarismIndicator

indicator = PlagiarismIndicator(
    score=0.15,
    suspicious_passages=["The quick brown fox..."],
    explanation="Low plagiarism risk. One passage resembles common phrasing.",
)
```

| Field | Type | Description |
|:------|:-----|:------------|
| `score` | `float` | Plagiarism likelihood score (0.0–1.0) |
| `suspicious_passages` | `list[str]` | Flagged text passages |
| `explanation` | `str` | Detailed explanation of findings |

#### `GradeDistribution`

Statistical tracking across multiple graded essays.

```python
from src.essay_grader.core import GradeDistribution

dist = GradeDistribution()
dist.add_score(85.0)
dist.add_score(92.5)
dist.add_score(78.0)
dist.add_score(88.0)

print(f"Count:  {dist.count}")    # 4
print(f"Mean:   {dist.mean}")     # 85.875
print(f"Median: {dist.median}")   # 86.5
print(f"Std:    {dist.std}")      # 5.27...
print(f"Scores: {dist.scores}")   # [85.0, 92.5, 78.0, 88.0]

# Human-readable summary
print(dist.summary())
```

| Property / Method | Type | Description |
|:------------------|:-----|:------------|
| `add_score(score)` | method | Add a score to the distribution |
| `scores` | `list[float]` | All recorded scores |
| `count` | `int` | Number of scores |
| `mean` | `float` | Arithmetic mean |
| `median` | `float` | Median value |
| `std` | `float` | Standard deviation |
| `summary()` | `str` | Formatted summary string |

### `ConfigManager`

Singleton configuration manager backed by `config.yaml`.

```python
from src.essay_grader.core import ConfigManager

# Get the singleton instance
config = ConfigManager.get_instance("config.yaml")

# Access nested config values with dot-path keys
temperature = config.get("llm", "temperature", default=0.3)
default_rubric = config.get("grading", "default_rubric", default="academic")

# Access the raw config dictionary
raw = config.raw

# Reset the singleton (useful in tests)
ConfigManager.reset()
```

<br/>

---

<br/>

## ⚙️ Configuration

All settings are managed through `config.yaml` at the project root:

```yaml
# LLM settings
llm:
  temperature: 0.3          # Sampling temperature (lower = more deterministic)
  max_tokens: 4096           # Maximum response tokens

# Grading defaults
grading:
  default_rubric: "academic" # Default rubric preset
  max_essay_length: 50000    # Max input character count
  annotation_enabled: true   # Enable inline annotations by default

# Grade scale mapping (score thresholds)
grade_scale:
  "A+": 97
  "A":  93
  "A-": 90
  "B+": 87
  "B":  83
  "B-": 80
  "C+": 77
  "C":  73
  "C-": 70
  "D+": 67
  "D":  63
  "D-": 60
  "F":  0

# Plagiarism detection
plagiarism:
  enabled: true
  threshold: 0.7             # Score above this triggers a warning

# Storage
storage:
  history_file: "grade_history.json"
  reports_dir: "./reports"

# Logging
logging:
  level: "INFO"
  file: "essay_grader.log"
```

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
cp .env.example .env
```

Environment variables override `config.yaml` values where applicable.

<br/>

---

<br/>

## 🧪 Testing

```bash
# Run the full test suite
python -m pytest tests/ -v

# Run with coverage reporting
python -m pytest tests/ -v --cov=src/essay_grader --cov-report=term-missing

# Run a specific test file
python -m pytest tests/test_core.py -v

# Using Make shortcuts
make test
```

### Test Modules

| Module | Coverage |
|:-------|:---------|
| `test_core.py` | Unit tests for grading logic, rubrics, `GradeDistribution`, validation, grade letter calculation, and export |
| `test_cli.py` | Integration tests for all CLI commands (`grade`, `rubrics`, `report`, `batch`) including error handling |

### Example Output

```
╭──────────── Essay Grade ────────────╮
│  Overall Score: 7.5/10  (B+)       │
╰─────────────────────────────────────╯

┌──────────────┬───────┬──────────────────────────┐
│ Criterion    │ Score │ Feedback                 │
├──────────────┼───────┼──────────────────────────┤
│ Thesis       │ 8/10  │ Clear and well-defined   │
│ Evidence     │ 7/10  │ Good use of sources      │
│ Analysis     │ 7/10  │ Adequate depth           │
│ Organization │ 8/10  │ Logical flow             │
│ Grammar      │ 8/10  │ Minor errors only        │
└──────────────┴───────┴──────────────────────────┘

✓ Strengths:
  • Clear thesis statement
  • Good use of transitions

✗ Weaknesses:
  • Needs more evidence in paragraph 3

💡 Suggestions:
  • Add more primary sources
  • Strengthen conclusion
```

<br/>

---

<br/>

## 🔒 Local LLM vs Cloud AI

A key design decision of this project is running **entirely locally**. Here's how it compares:

| Dimension | ☁️ Cloud AI (GPT-4, Claude) | 🏠 Essay Grader (Local) |
|:----------|:---------------------------|:------------------------|
| **Privacy** | Essays sent to third-party servers | ✅ All data stays on your machine |
| **Cost** | Pay per token / API call | ✅ Free after initial hardware |
| **Latency** | Network round-trip required | ✅ Local inference, no network |
| **Internet** | Required | ✅ Works fully offline |
| **Model quality** | State-of-the-art (GPT-4, Claude) | Good (Gemma 3 via Ollama) |
| **Customization** | Limited to prompt engineering | ✅ Full control over model & config |
| **FERPA / GDPR** | Requires compliance review | ✅ No data leaves your infrastructure |
| **Scalability** | Unlimited (with budget) | Limited by local hardware |

> **Bottom line:** If student privacy matters (and it always does), local LLM grading is the responsible choice.

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What models does Essay Grader support?</strong></summary>

<br/>

Essay Grader uses **Ollama** as its LLM backend, so it supports any model Ollama can run. The default and recommended model is **Gemma 3**, which provides a good balance of quality and speed for grading tasks. You can switch models by updating the Ollama configuration — no code changes required.

</details>

<details>
<summary><strong>How accurate is the grading compared to human graders?</strong></summary>

<br/>

Local LLMs like Gemma 3 produce grading that is **directionally accurate** — they reliably identify strong and weak essays. However, they may not match the nuance of an experienced human grader on edge cases. Essay Grader is best used as a **first-pass tool** that handles the bulk of assessment, freeing educators to focus on essays that need deeper attention. The structured rubric system helps constrain the LLM's output to meaningful, consistent evaluations.

</details>

<details>
<summary><strong>Can I create custom rubrics beyond the 5 presets?</strong></summary>

<br/>

Yes. You can pass comma-separated criteria via the CLI (`--rubric "thesis,evidence,style"`) or build custom `Rubric` and `RubricCriterion` objects in the Python API. The Streamlit web UI also includes a **Rubric Builder** for interactive rubric creation with weights and descriptions.

</details>

<details>
<summary><strong>How does plagiarism detection work without internet?</strong></summary>

<br/>

The plagiarism detection uses the local LLM to analyze **writing-style consistency** within the essay. It looks for abrupt shifts in vocabulary, tone, or complexity that may indicate copied passages. It does **not** compare against an external database of documents — it's a stylometric analysis tool. For web-based plagiarism checking, use a dedicated service like Turnitin alongside this tool.

</details>

<details>
<summary><strong>What hardware do I need to run this locally?</strong></summary>

<br/>

The hardware requirements depend on the Ollama model you choose:

- **Gemma 3 (4B):** 8 GB RAM, any modern CPU — runs on most laptops
- **Gemma 3 (12B):** 16 GB RAM, GPU recommended for faster inference
- **Gemma 3 (27B):** 32 GB RAM + dedicated GPU (NVIDIA with 12+ GB VRAM)

For classroom use with batch grading, a machine with a dedicated GPU is recommended for reasonable throughput.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork & clone the repository
git clone https://github.com/<your-username>/essay-grader.git
cd essay-grader

# 2. Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-cov ruff

# 3. Create a feature branch
git checkout -b feature/my-improvement

# 4. Make your changes, then run tests
python -m pytest tests/ -v

# 5. Lint your code
ruff check src/ tests/

# 6. Commit and push
git add .
git commit -m "feat: describe your change"
git push origin feature/my-improvement

# 7. Open a Pull Request on GitHub
```

### Areas for Contribution

- 🧪 Additional test coverage
- 📋 New rubric presets for specialized domains
- 🌍 Internationalization / multi-language support
- 📊 Enhanced analytics and visualization
- 📝 Documentation improvements

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">
<br/>

**📝 Essay Grader** — Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection

<br/>

Built with ❤️ using Python · Ollama · Gemma 3 · Streamlit

<br/>

<sub>Made by <a href="https://github.com/kennedyraju55">kennedyraju55</a></sub>

<br/>
</div>
