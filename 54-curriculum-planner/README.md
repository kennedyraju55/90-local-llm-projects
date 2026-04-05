<!-- ═══════════════════════════════════════════════════════════════════════════
     📋 CURRICULUM PLANNER — AI-Powered Course Design & Learning Outcome Mapping
     Part of the 90 Local LLM Projects collection
     ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

  <!-- Hero Banner -->
  <img src="docs/images/banner.svg" alt="Curriculum Planner Banner" width="800"/>

  <br/><br/>

  <!-- Badges -->
  [![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
  [![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
  [![Gemma 3](https://img.shields.io/badge/Gemma_3-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
  [![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
  [![Click CLI](https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)](LICENSE)
  [![Tests](https://img.shields.io/badge/Tests-Passing-22C55E?style=for-the-badge&logo=pytest&logoColor=white)](#-testing)

  <br/>

  **Production-grade AI-powered curriculum design** with learning outcome mapping,<br/>
  assessment planning, prerequisite tracking, and Bloom's taxonomy integration.

  <br/>

  [Quick Start](#-quick-start) •
  [CLI Reference](#-cli-reference) •
  [Web UI](#-web-ui) •
  [Architecture](#-architecture) •
  [API Reference](#-api-reference) •
  [Configuration](#%EF%B8%8F-configuration) •
  [FAQ](#-faq)

  <br/>

  <strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Designing a well-structured curriculum is **hard**. Educators, instructional designers, and training teams
face recurring challenges that this tool directly addresses:

| Challenge | Traditional Approach | Curriculum Planner Solution |
|:---|:---|:---|
| **Blank-page paralysis** | Manually brainstorming week-by-week topics from scratch | AI generates a complete weekly plan in seconds from just a course name |
| **Outcome alignment** | Tracking Bloom's taxonomy levels in spreadsheets | Automated outcome mapping with coverage gap detection |
| **Assessment balance** | Guessing at weights; assessments clustered at semester end | Weighted assessment calendar distributed across all weeks |
| **Resource discovery** | Hours of Googling for textbooks, videos, and articles | AI-curated resource suggestions categorized by type |
| **Prerequisite clarity** | Informal lists that miss dependencies and alternatives | Dependency trees with alternative path suggestions |

> **Bottom line:** This tool turns a course title and duration into a complete, standards-aligned
> curriculum — including weekly plans, learning outcomes, assessments, resources, and prerequisites —
> entirely offline using a local LLM.

<br/>

---

<br/>

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Category | Capabilities |
|:---|:---|
| **🧠 AI Course Generation** | Generate complete curricula from a topic, week count, and difficulty level. Supports beginner, intermediate, and advanced tiers with customizable focus areas. Up to 52 weeks of content. |
| **🎯 Learning Outcome Mapping** | Map outcomes to Bloom's taxonomy levels (Remember → Create). Generate outcome-to-week matrices. Detect coverage gaps automatically. |
| **📊 Assessment Planning** | Create balanced assessment schedules with weighted scoring. Supports quizzes, assignments, projects, exams, presentations, and discussions. Calendar view for due dates. |
| **📚 Resource & Prerequisite Management** | AI-curated resource suggestions categorized by type (books, videos, articles, labs). Prerequisite dependency trees with alternative learning paths. |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|:---|:---|:---|
| [Python](https://www.python.org/) | 3.10+ | Runtime |
| [Ollama](https://ollama.com/) | Latest | Local LLM inference |
| [Gemma 3](https://ollama.com/library/gemma3) | Any | Language model |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/curriculum-planner.git
cd curriculum-planner

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### 2. Start Ollama

```bash
# Pull the Gemma 3 model (first time only)
ollama pull gemma3

# Start Ollama server (if not already running)
ollama serve
```

### 3. Generate Your First Curriculum

```bash
# CLI — generate a 12-week beginner Python course
curriculum-planner design --course "Introduction to Python" --weeks 12 --level beginner

# Or launch the Streamlit web interface
streamlit run src/curriculum_planner/app.py
```

<br/>

---

<br/>

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and exposes five commands.
Run `curriculum-planner --help` for a full list.

<br/>

### `design` — Generate a Curriculum

Create a complete course curriculum from a topic, week count, and difficulty level.

```bash
curriculum-planner design \
  --course "Machine Learning Fundamentals" \
  --weeks 16 \
  --level intermediate \
  --focus "supervised learning, neural networks" \
  --output ml_curriculum.json
```

| Flag | Short | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `--course` | `-c` | ✅ | — | Course title or topic |
| `--weeks` | `-w` | — | `12` | Number of weeks (1–52) |
| `--level` | `-l` | — | `beginner` | Difficulty: `beginner`, `intermediate`, `advanced` |
| `--focus` | `-f` | — | — | Comma-separated focus areas |
| `--output` | `-o` | — | `stdout` | Output file path |

**Example output** (abbreviated):

```json
{
  "title": "Machine Learning Fundamentals",
  "level": "intermediate",
  "weeks": 16,
  "weekly_plan": [
    {
      "week": 1,
      "title": "Introduction to Machine Learning",
      "topics": ["What is ML?", "Types of learning", "Python ML stack"],
      "goals": ["Understand ML taxonomy", "Set up development environment"],
      "activities": ["Install scikit-learn", "Run first classifier"],
      "assessment": "Environment setup quiz",
      "outcomes": ["LO-1", "LO-2"]
    }
  ]
}
```

<br/>

### `outcomes` — Learning Outcome Management

List, map, or check coverage of learning outcomes in an existing curriculum file.

```bash
# List all learning outcomes
curriculum-planner outcomes --curriculum-file ml_curriculum.json --action list

# Map outcomes to weeks (generates matrix)
curriculum-planner outcomes --curriculum-file ml_curriculum.json --action map

# Check for coverage gaps
curriculum-planner outcomes --curriculum-file ml_curriculum.json --action check
```

| Flag | Short | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `--curriculum-file` | `-f` | ✅ | — | Path to curriculum JSON file |
| `--action` | — | — | `list` | Action: `list`, `map`, `check` |

**Outcome matrix example** (`--action map`):

```
Outcome        | Wk1 | Wk2 | Wk3 | Wk4 | ... | Wk16
───────────────┼─────┼─────┼─────┼─────┼─────┼──────
LO-1 Remember  |  ✓  |     |     |     |     |
LO-2 Understand|  ✓  |  ✓  |     |     |     |
LO-3 Apply     |     |  ✓  |  ✓  |  ✓  |     |
LO-4 Analyze   |     |     |     |  ✓  |  ✓  |  ✓
```

<br/>

### `resources` — Resource Suggestions

Get AI-curated learning resources for a course topic.

```bash
curriculum-planner resources --course "Data Structures and Algorithms"
```

| Flag | Short | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `--course` | `-c` | ✅ | — | Course title or topic |

**Example output:**

```
📚 Resources for "Data Structures and Algorithms"

 Required:
  📖 "Introduction to Algorithms" (Cormen et al.) — Textbook
  🎥 MIT OpenCourseWare 6.006 — Video Lectures

 Recommended:
  📰 GeeksforGeeks DSA Series — Articles
  🧪 LeetCode Problem Sets — Practice Labs
```

<br/>

### `export` — Export Curriculum

Export a curriculum JSON file to different formats.

```bash
# Export to Markdown
curriculum-planner export \
  --input ml_curriculum.json \
  --format markdown \
  --output ml_curriculum.md

# Export to JSON (reformatted)
curriculum-planner export \
  --input ml_curriculum.json \
  --format json \
  --output ml_curriculum_formatted.json
```

| Flag | Short | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `--input` | `-i` | ✅ | — | Input curriculum JSON file |
| `--format` | `-f` | — | `json` | Output format: `json`, `markdown` |
| `--output` | `-o` | — | `stdout` | Output file path |

<br/>

### `prerequisites` — Prerequisite Analysis

Analyze and display prerequisite dependencies for a curriculum.

```bash
curriculum-planner prerequisites --curriculum-file ml_curriculum.json
```

| Flag | Short | Required | Default | Description |
|:---|:---|:---|:---|:---|
| `--curriculum-file` | `-f` | ✅ | — | Path to curriculum JSON file |

**Example output:**

```
🔗 Prerequisite Tree for "Machine Learning Fundamentals"

 ✅ Python Programming (Required)
    └─ Alternatives: JavaScript, R
 ✅ Linear Algebra (Required)
    └─ Alternatives: Khan Academy Linear Algebra course
 ⚠️  Statistics & Probability (Required)
    └─ Alternatives: "Statistics for Data Science" MOOC
 ○  Calculus (Optional)
    └─ Helpful for understanding gradient descent
```

<br/>

---

<br/>

## 🌐 Web UI

The Streamlit web interface provides an interactive experience for designing curricula
without touching the command line.

```bash
# Launch the web UI
streamlit run src/curriculum_planner/app.py
```

**Web UI capabilities:**

- 🎨 **Interactive form** — Fill in course details, select difficulty, set focus areas
- 📅 **Visual weekly plan** — Browse the generated curriculum week by week
- 📊 **Outcome matrix** — See Bloom's taxonomy alignment at a glance
- 📥 **One-click export** — Download as JSON or Markdown
- 🔗 **Prerequisite visualization** — Interactive dependency tree

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="Architecture Diagram" width="800"/>
</div>

<br/>

The system follows a **layered architecture** with clear separation of concerns:

| Layer | Components | Responsibility |
|:---|:---|:---|
| **Interface** | CLI (Click), Streamlit Web UI | User interaction and I/O |
| **Core Engine** | `generate_curriculum()`, `build_course_design()` | Orchestration and LLM communication |
| **Modules** | OutcomeMapper, AssessmentPlanner, ResourceSuggester, PrerequisiteTracker | Domain-specific logic |
| **Export** | `export_curriculum()` | JSON and Markdown serialization |
| **Infrastructure** | ConfigManager, Ollama client | Configuration and LLM inference |

### Project Structure

```
54-curriculum-planner/
├── src/
│   └── curriculum_planner/
│       ├── __init__.py          # Package metadata and version
│       ├── core.py              # Business logic, dataclasses, LLM integration
│       ├── cli.py               # Click CLI with 5 command groups
│       └── web_ui.py            # Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core logic tests (30+ tests)
│   └── test_cli.py              # CLI integration tests
├── common/                      # Shared utilities
├── docs/
│   └── images/                  # SVG diagrams and assets
│       ├── banner.svg
│       ├── architecture.svg
│       └── features.svg
├── config.yaml                  # Application configuration (YAML)
├── setup.py                     # Package setup with entry points
├── requirements.txt             # Python dependencies
├── Makefile                     # Development workflow targets
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

<br/>

---

<br/>

## 📖 API Reference

All public classes and functions are importable from `curriculum_planner.core`.

<br/>

### `CourseDesign` — Top-Level Data Model

The primary dataclass representing a complete curriculum.

```python
from curriculum_planner.core import CourseDesign, build_course_design

# Build from raw LLM output (dict)
course = build_course_design(data)

print(course.title)          # "Machine Learning Fundamentals"
print(course.level)          # "intermediate"
print(course.weeks)          # 16
print(len(course.weekly_plan))  # 16 WeekPlan objects
print(len(course.outcomes))     # LearningOutcome objects
print(len(course.assessments))  # Assessment objects
```

**Fields:**

| Field | Type | Description |
|:---|:---|:---|
| `title` | `str` | Course title |
| `level` | `str` | Difficulty level (beginner/intermediate/advanced) |
| `weeks` | `int` | Number of weeks |
| `description` | `str` | Course description |
| `objectives` | `list[str]` | Learning objectives |
| `prerequisites` | `list[Prerequisite]` | Course prerequisites |
| `weekly_plan` | `list[WeekPlan]` | Week-by-week breakdown |
| `resources` | `list[Resource]` | Recommended resources |
| `assessments` | `list[Assessment]` | Assessment schedule |
| `outcomes` | `list[LearningOutcome]` | Learning outcomes with Bloom's levels |

<br/>

### `OutcomeMapper` — Bloom's Taxonomy Alignment

Maps learning outcomes to weeks and generates coverage matrices.

```python
from curriculum_planner.core import OutcomeMapper

mapper = OutcomeMapper(outcomes=course.outcomes, weekly_plan=course.weekly_plan)

# Map outcomes to the weeks where they are addressed
mapping = mapper.map_outcomes_to_weeks()
# → {"LO-1": [1, 2], "LO-2": [2, 3, 4], ...}

# Generate a 2D coverage matrix
matrix = mapper.generate_outcome_matrix()
# → [["LO-1", "✓", "", "✓", ...], ["LO-2", "", "✓", ...]]

# Find outcomes not covered by any week
gaps = mapper.check_coverage()
# → [LearningOutcome(id="LO-7", description="...", bloom_level="Create")]
```

**Methods:**

| Method | Returns | Description |
|:---|:---|:---|
| `map_outcomes_to_weeks()` | `dict` | Outcome ID → list of week numbers |
| `generate_outcome_matrix()` | `list[list]` | 2D matrix (outcomes × weeks) |
| `check_coverage()` | `list[LearningOutcome]` | Uncovered outcomes |

<br/>

### `AssessmentPlanner` — Weighted Assessment Scheduling

Creates balanced assessment schedules with automatic weight normalization.

```python
from curriculum_planner.core import AssessmentPlanner

planner = AssessmentPlanner(assessments=course.assessments)

# Plan assessments against outcomes and weeks
planned = planner.plan_assessments(outcomes=course.outcomes, weeks=16)
# → [Assessment(name="Quiz 1", type="quiz", week=2, weight=5.0, ...)]

# Calculate normalized weights (sum to 100%)
weights = planner.calculate_weights()
# → [{"name": "Quiz 1", "weight": 5.0}, {"name": "Midterm Project", "weight": 25.0}]

# Get chronological assessment calendar
calendar = planner.get_assessment_calendar()
# → [{"week": 2, "assessments": ["Quiz 1"]}, {"week": 8, "assessments": ["Midterm"]}]
```

**Methods:**

| Method | Returns | Description |
|:---|:---|:---|
| `plan_assessments(outcomes, weeks)` | `list` | Planned assessments with scheduling |
| `calculate_weights()` | `list` | Normalized weight distribution |
| `get_assessment_calendar()` | `list[dict]` | Week-by-week assessment schedule |

<br/>

### `ResourceSuggester` — AI-Curated Resources

Suggests and categorizes learning resources for course topics.

```python
from curriculum_planner.core import ResourceSuggester

suggester = ResourceSuggester()

# Get AI-suggested resources for topics
resources = suggester.suggest_resources(topics=["neural networks", "backpropagation"])
# → [Resource(type="book", title="Deep Learning", ...), ...]

# Categorize existing resources by type (static method)
categorized = ResourceSuggester.categorize_resources(resources)
# → {"book": [...], "video": [...], "article": [...], "lab": [...]}
```

**Methods:**

| Method | Returns | Description |
|:---|:---|:---|
| `suggest_resources(topics)` | `list` | AI-generated resource suggestions |
| `categorize_resources(resources)` | `dict` | Resources grouped by type (static) |

<br/>

### `PrerequisiteTracker` — Dependency Management

Tracks course prerequisites with dependency trees and alternative paths.

```python
from curriculum_planner.core import PrerequisiteTracker, Prerequisite

tracker = PrerequisiteTracker()

# Add prerequisites
tracker.add_prerequisite(Prerequisite(
    name="Linear Algebra",
    description="Matrix operations and vector spaces",
    required=True,
    alternatives=["Khan Academy Linear Algebra"]
))

# Check which prerequisites are required
required = tracker.check_prerequisites()
# → [Prerequisite(name="Linear Algebra", required=True, ...)]

# Generate dependency tree
tree = tracker.generate_prerequisite_tree()
# → {"Linear Algebra": {"required": True, "alternatives": [...]}}
```

**Methods:**

| Method | Returns | Description |
|:---|:---|:---|
| `add_prerequisite(prereq)` | — | Add a prerequisite to the tracker |
| `check_prerequisites()` | `list` | List of required prerequisites |
| `generate_prerequisite_tree()` | `dict` | Full dependency tree with alternatives |

<br/>

### Core Functions

```python
from curriculum_planner.core import (
    generate_curriculum,
    validate_curriculum_data,
    build_course_design,
    export_curriculum,
    ConfigManager,
)

# Generate a curriculum using the LLM
data = generate_curriculum(
    course="Data Engineering",
    weeks=10,
    level="advanced",
    focus="Apache Spark, Airflow",
    cfg=ConfigManager("config.yaml"),
)

# Validate raw curriculum data
errors = validate_curriculum_data(data)
if errors:
    print("Validation errors:", errors)

# Build a CourseDesign object from raw data
course = build_course_design(data)

# Export to file
output_path = export_curriculum(data, output_path="output.md", fmt="markdown")
```

<br/>

---

<br/>

## ⚙️ Configuration

All settings are managed via `config.yaml` in the project root.

### Full Configuration Reference

```yaml
# ─── LLM Settings ────────────────────────────────────────
llm:
  temperature: 0.7           # Creativity level (0.0 = deterministic, 1.0 = creative)
  max_tokens: 8192           # Maximum response length from the model

# ─── Curriculum Defaults ─────────────────────────────────
curriculum:
  default_weeks: 12          # Default course duration
  default_level: beginner    # Default difficulty level
  max_weeks: 52              # Maximum allowed weeks

# ─── Bloom's Taxonomy Levels ─────────────────────────────
bloom_levels:
  - Remember                 # Recall facts and basic concepts
  - Understand               # Explain ideas or concepts
  - Apply                    # Use information in new situations
  - Analyze                  # Draw connections among ideas
  - Evaluate                 # Justify a decision or course of action
  - Create                   # Produce new or original work

# ─── Assessment Configuration ────────────────────────────
assessment:
  types:
    - quiz                   # Short knowledge checks
    - assignment             # Take-home exercises
    - project                # Extended practical work
    - exam                   # Formal examinations
    - presentation           # Oral presentations
    - discussion             # Participation-based assessment

# ─── Storage & Logging ───────────────────────────────────
storage:
  output_dir: "./curricula"

logging:
  level: INFO
  file: curriculum_planner.log
```

### Bloom's Taxonomy Levels

| Level | Cognitive Process | Example Verbs | Typical Assessment |
|:---|:---|:---|:---|
| **Remember** | Recall | define, list, identify, name | Quiz, flashcards |
| **Understand** | Comprehension | describe, explain, summarize, paraphrase | Short answer, discussion |
| **Apply** | Application | implement, solve, demonstrate, use | Assignment, lab |
| **Analyze** | Analysis | compare, contrast, examine, differentiate | Case study, essay |
| **Evaluate** | Judgment | critique, assess, judge, justify | Peer review, presentation |
| **Create** | Synthesis | design, develop, construct, produce | Project, portfolio |

### Assessment Types

| Type | Use Case | Typical Weight |
|:---|:---|:---|
| `quiz` | Quick knowledge checks after a topic | 5–10% |
| `assignment` | Take-home exercises reinforcing weekly topics | 10–15% |
| `project` | Extended practical work spanning multiple weeks | 20–30% |
| `exam` | Comprehensive assessment (midterm / final) | 15–25% |
| `presentation` | Oral defense of projects or research | 5–15% |
| `discussion` | Participation in class or forum discussions | 5–10% |

### Using `ConfigManager`

```python
from curriculum_planner.core import ConfigManager

cfg = ConfigManager("config.yaml")
cfg.load()

# Access configuration values
temp = cfg.get("llm", "temperature", default=0.7)
max_weeks = cfg.get("curriculum", "max_weeks", default=52)

# Access the raw data dict
print(cfg.data)
```

<br/>

---

<br/>

## 🧪 Testing

The test suite uses **pytest** with mocked LLM calls — no running Ollama instance required.

### Running Tests

```bash
# Run the full test suite
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/curriculum_planner --cov-report=term-missing

# Run only core logic tests
python -m pytest tests/test_core.py -v

# Run only CLI integration tests
python -m pytest tests/test_cli.py -v

# Run a single test by name
python -m pytest tests/test_core.py::test_generate_curriculum_parses_json -v
```

### Test Coverage

| Module | Tests | Coverage Areas |
|:---|:---|:---|
| `test_core.py` | 25+ | Dataclasses, OutcomeMapper, AssessmentPlanner, ResourceSuggester, PrerequisiteTracker, validation, export |
| `test_cli.py` | 5+ | CLI commands, flag parsing, output formatting, error handling |

### What's Tested

- ✅ All dataclass instantiation and defaults (`WeekPlan`, `LearningOutcome`, `Assessment`, etc.)
- ✅ `OutcomeMapper` — mapping, matrix generation, coverage gap detection
- ✅ `AssessmentPlanner` — scheduling, weight normalization, calendar generation
- ✅ `ResourceSuggester` — resource suggestion and categorization
- ✅ `PrerequisiteTracker` — adding, checking, tree generation
- ✅ `generate_curriculum()` — JSON parsing from LLM output (mocked)
- ✅ `validate_curriculum_data()` — required field validation
- ✅ `export_curriculum()` — JSON and Markdown export
- ✅ `ConfigManager` — loading, getting values, defaults
- ✅ All CLI commands — `design`, `outcomes`, `resources`, `export`, `prerequisites`

### Using Make

```bash
make test          # Run all tests
make test-cov      # Run tests with coverage
make lint          # Run linters
make format        # Format code
```

<br/>

---

<br/>

## 🔒 Local LLM vs Cloud AI

| Feature | Curriculum Planner (Local) | Cloud AI APIs |
|:---|:---|:---|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after hardware investment | ❌ Per-token pricing adds up |
| **Latency** | ✅ No network round-trips | ❌ Dependent on internet speed |
| **Availability** | ✅ Works offline, no API keys | ❌ Requires internet and valid API key |
| **Customization** | ✅ Full control over model and prompts | ⚠️ Limited to provider's offerings |
| **Rate Limits** | ✅ None — run as many queries as you want | ❌ Throttled by provider |
| **Model Choice** | ✅ Swap models freely (Gemma, Llama, etc.) | ⚠️ Locked to provider's models |
| **Reproducibility** | ✅ Same model + seed = same output | ❌ Model versions change without notice |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>How long does it take to generate a curriculum?</strong></summary>

<br/>

Generation time depends on your hardware and the number of weeks requested:

| Weeks | Approximate Time (RTX 3060) | Approximate Time (CPU-only) |
|:---|:---|:---|
| 4 weeks | ~15 seconds | ~45 seconds |
| 12 weeks | ~30 seconds | ~2 minutes |
| 52 weeks | ~2 minutes | ~8 minutes |

The LLM generates the entire curriculum in a single call, so longer courses take
proportionally more time. GPU acceleration via Ollama is strongly recommended.

</details>

<details>
<summary><strong>Can I use a different model instead of Gemma 3?</strong></summary>

<br/>

Yes! Any model available through Ollama works. Popular alternatives:

```bash
# Use Llama 3
ollama pull llama3
# Then set the model in your environment or config

# Use Mistral
ollama pull mistral

# Use Phi-3
ollama pull phi3
```

Larger models (13B+ parameters) generally produce higher quality curricula with better
structure and more detailed weekly plans.

</details>

<details>
<summary><strong>How does Bloom's Taxonomy mapping work?</strong></summary>

<br/>

The system maps each learning outcome to one of six cognitive levels from Bloom's
revised taxonomy:

1. **Remember** → Recall facts (e.g., "List the Python data types")
2. **Understand** → Explain concepts (e.g., "Describe how recursion works")
3. **Apply** → Use knowledge (e.g., "Implement a binary search algorithm")
4. **Analyze** → Break down (e.g., "Compare sorting algorithm complexities")
5. **Evaluate** → Judge (e.g., "Assess the trade-offs of SQL vs NoSQL")
6. **Create** → Produce (e.g., "Design a REST API for an e-commerce platform")

The `OutcomeMapper` then tracks which weeks address each outcome and generates
a coverage matrix to ensure all levels are represented across the course.

</details>

<details>
<summary><strong>Can I edit a generated curriculum after creation?</strong></summary>

<br/>

Absolutely. The exported JSON is fully editable:

```bash
# Generate the curriculum
curriculum-planner design --course "Web Dev" --weeks 8 --output curriculum.json

# Edit the JSON file with your favorite editor
code curriculum.json

# Re-run analysis on the edited file
curriculum-planner outcomes --curriculum-file curriculum.json --action check
curriculum-planner prerequisites --curriculum-file curriculum.json

# Re-export to Markdown
curriculum-planner export --input curriculum.json --format markdown --output syllabus.md
```

The tool is designed for a **generate → review → refine** workflow.

</details>

<details>
<summary><strong>What happens if the LLM produces invalid output?</strong></summary>

<br/>

The `validate_curriculum_data()` function checks for required fields and structural
integrity. If the LLM output doesn't parse correctly:

1. **JSON parsing errors** — The system retries with a more constrained prompt
2. **Missing fields** — `validate_curriculum_data()` returns a list of specific errors
3. **Invalid values** — Type checking in dataclasses catches malformed data

You can also validate manually:

```python
from curriculum_planner.core import validate_curriculum_data

errors = validate_curriculum_data(data)
if errors:
    for error in errors:
        print(f"⚠️  {error}")
```

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/<your-username>/curriculum-planner.git
cd curriculum-planner

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Install development dependencies
pip install -e ".[dev]"

# 5. Make your changes and add tests

# 6. Run the test suite
python -m pytest tests/ -v

# 7. Commit and push
git add .
git commit -m "feat: your feature description"
git push origin feature/your-feature-name

# 8. Open a Pull Request on GitHub
```

### Contribution Ideas

- 🌍 **Internationalization** — Multi-language curriculum generation
- 📊 **Visualization** — Charts and graphs for outcome coverage
- 🔌 **Additional LLM backends** — OpenAI, Anthropic, Hugging Face
- 📄 **More export formats** — PDF, DOCX, HTML
- 🧪 **Additional tests** — Edge cases, integration tests

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

<br/>

---

<br/>

<div align="center">

  **📋 Curriculum Planner** — Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection

  <br/>

  Built with ❤️ using Python, Ollama, and Gemma 3

  <br/>

  [![GitHub](https://img.shields.io/badge/GitHub-kennedyraju55-181717?style=flat-square&logo=github)](https://github.com/kennedyraju55/curriculum-planner)
  [![Stars](https://img.shields.io/github/stars/kennedyraju55/curriculum-planner?style=flat-square&color=ff6b35)](https://github.com/kennedyraju55/curriculum-planner/stargazers)

  <br/>

  <sub>If this project helped you, consider giving it a ⭐</sub>

</div>
