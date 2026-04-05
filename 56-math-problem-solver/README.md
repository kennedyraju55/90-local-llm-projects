<div align="center">

<!-- Hero Banner -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/banner.svg">
  <img src="docs/images/banner.svg" alt="Math Problem Solver — AI-Powered Step-by-Step Mathematical Problem Solving" width="800"/>
</picture>

<br/>
<br/>

<!-- Badges Row 1 — Project Identity -->
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-FF6F00?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License MIT](https://img.shields.io/badge/License-MIT-06d6a0?style=for-the-badge)](LICENSE)

<!-- Badges Row 2 — Status -->
[![Tests](https://img.shields.io/badge/Tests-Passing-06d6a0?style=flat-square&logo=pytest&logoColor=white)](tests/)
[![Click CLI](https://img.shields.io/badge/CLI-Click-green?style=flat-square&logo=gnu-bash&logoColor=white)](src/math_solver/cli.py)
[![Rich Output](https://img.shields.io/badge/Output-Rich-blueviolet?style=flat-square)](https://github.com/Textualize/rich)
[![YAML Config](https://img.shields.io/badge/Config-YAML-red?style=flat-square&logo=yaml&logoColor=white)](config.yaml)
[![LaTeX](https://img.shields.io/badge/LaTeX-Output-008080?style=flat-square&logo=latex&logoColor=white)](#-latex-output)
[![Gemma 3](https://img.shields.io/badge/Model-Gemma_3-4285F4?style=flat-square&logo=google&logoColor=white)](https://ollama.com/library/gemma3)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

<br/>

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection — Project #56**

<br/>

> 🧮 **Solve any math problem with step-by-step explanations, LaTeX output, a built-in formula library, and a practice problem generator — all powered by a local LLM running on your own hardware.**

<br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Reference](#-api-reference) · [Formulas](#-built-in-formula-library) · [FAQ](#-faq)

</div>

<br/>

---

<br/>

## 💡 Why This Project?

Math problem-solving is one of the most impactful applications of local LLMs.
This project bridges the gap between **raw AI power** and **structured, educational output**.

| Challenge | How Math Problem Solver Addresses It |
|:----------|:-------------------------------------|
| 🤔 **"I got the answer but don't understand it"** | Every solution includes numbered steps with work shown and plain-English explanations |
| 📖 **"I can never remember the formula"** | 10+ built-in formulas across 4 categories — always available offline, no LLM needed |
| 🏋️ **"I need more practice"** | Generate unlimited practice problems at 3 difficulty levels with hints and answers |
| 🔒 **"I don't want my homework in the cloud"** | 100% local — runs on your machine via Ollama; no data ever leaves your computer |
| 📄 **"I need publication-quality notation"** | Every solution includes LaTeX output you can paste directly into papers or presentations |

<br/>

---

<br/>

## ✨ Features

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/features.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/features.svg">
  <img src="docs/images/features.svg" alt="Key Features Overview" width="800"/>
</picture>

</div>

<br/>

<table>
<tr>
<td width="50%">

### 🔢 Intelligent Problem Solving

- Accepts **free-form** natural language math problems
- Automatic **category detection** (algebra, calculus, geometry, statistics, arithmetic, trigonometry)
- Returns a structured `MathProblemResult` with answer, steps, concepts, tips, and related problems
- Saves solutions as **JSON** for programmatic consumption

</td>
<td width="50%">

### 📐 Built-in Formula Library

- **10+ formulas** available instantly — no LLM required
- Covers **Algebra**, **Geometry**, **Calculus**, and **Trigonometry**
- Every formula includes a **LaTeX** representation
- Optionally fetch **extended formulas** from the LLM for deeper coverage

</td>
</tr>
<tr>
<td width="50%">

### 🏋️ Practice Problem Generator

- Generate **unlimited** practice problems on demand
- Choose from **3 difficulty levels**: `basic`, `intermediate`, `advanced`
- Each problem comes with a **hint** and the **correct answer**
- Supports all **6 math categories**

</td>
<td width="50%">

### 📄 LaTeX Output & Concepts

- Every solution includes **publication-ready LaTeX** notation
- Identifies the **mathematical concepts** used in each solution
- Provides actionable **study tips** for similar problems
- Suggests **related problems** for further practice

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
| **Python** | 3.9+ | Runtime |
| **Ollama** | Latest | Local LLM backend |
| **Gemma 3** | via Ollama | Default math model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/math-problem-solver.git
cd math-problem-solver

# 2. Install the package in editable mode
pip install -e .

# 3. (Optional) Install development dependencies
pip install -e ".[dev]"

# 4. Pull the LLM model
ollama pull gemma3

# 5. Start the Ollama server (if not already running)
ollama serve
```

### Verify Installation

```bash
# Solve your first problem
math-solver solve --problem "What is 2 + 2?"

# Check formula library
math-solver formulas --category algebra

# Generate practice problems
math-solver practice --category geometry --difficulty basic --count 3
```

<br/>


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/math-problem-solver.git
cd math-problem-solver
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
uvicorn src.math_solver.api:app --reload --port 8000

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

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://github.com/Textualize/rich) for beautiful terminal output.

```
math-solver [OPTIONS] COMMAND [ARGS]...

📐 Math Problem Solver — Solve math problems with step-by-step explanations.

Options:
  -v, --verbose    Enable verbose logging
  --help           Show this message and exit

Commands:
  solve      Solve a math problem with detailed explanations
  formulas   Browse the formula reference library
  practice   Generate practice problems with hints and answers
```

<br/>

### `solve` — Solve a Math Problem

Solve any math problem with optional step-by-step breakdown, category classification, and LaTeX output.

```bash
# Basic usage
math-solver solve --problem "Solve 2x + 5 = 15"

# Specify a category for better results
math-solver solve --problem "Find the area of a circle with radius 5" --category geometry

# Disable step-by-step output (answer only)
math-solver solve --problem "What is the derivative of x³?" --no-steps

# Save the full solution to a JSON file
math-solver solve --problem "∫ x² dx" --output solution.json

# Combine options
math-solver solve -p "a² + b² = c², find c when a=3, b=4" -c geometry -o result.json
```

#### Options

| Flag | Short | Type | Default | Description |
|:-----|:------|:-----|:--------|:------------|
| `--problem` | `-p` | `TEXT` | *(required)* | The math problem to solve (natural language) |
| `--show-steps` / `--no-steps` | — | `BOOL` | `True` | Show step-by-step solution breakdown |
| `--category` | `-c` | `CHOICE` | *(auto-detect)* | Problem category: `algebra`, `calculus`, `geometry`, `statistics`, `arithmetic`, `trigonometry` |
| `--output` | `-o` | `PATH` | — | Save solution to a JSON file |

#### Example Output

```
╭──────────────── 📐 Problem ────────────────╮
│ Solve 2x + 5 = 15                          │
│ Category: algebra │ Difficulty: basic       │
╰─────────────────────────────────────────────╯

📝 Solution Steps:

Step 1: Subtract 5 from both sides
  ┌─────────────────────────────┐
  │ 2x + 5 - 5 = 15 - 5        │
  │ 2x = 10                     │
  └─────────────────────────────┘
  We isolate the variable term by removing the constant.

Step 2: Divide both sides by 2
  ┌─────────────────────────────┐
  │ 2x / 2 = 10 / 2            │
  │ x = 5                       │
  └─────────────────────────────┘
  We solve for x by dividing by the coefficient.

╭──────────── ✅ Answer ─────────────╮
│ x = 5                              │
╰────────────────────────────────────╯

📖 Concepts Used:
  • Linear equations
  • Inverse operations

💡 Tips:
  • Always perform the same operation on both sides
```

<br/>

### `formulas` — Browse Formula Library

Access the built-in formula reference or fetch extended formulas from the LLM.

```bash
# Show all built-in formulas (no LLM needed)
math-solver formulas

# Filter by category
math-solver formulas --category algebra
math-solver formulas --category geometry
math-solver formulas --category calculus
math-solver formulas --category trigonometry

# Fetch extended formulas from the LLM
math-solver formulas --category algebra --extended
```

#### Options

| Flag | Short | Type | Default | Description |
|:-----|:------|:-----|:--------|:------------|
| `--category` | `-c` | `TEXT` | *(all)* | Filter formulas by category: `algebra`, `geometry`, `calculus`, `trigonometry` |
| `--extended` | — | `FLAG` | `False` | Fetch additional formulas from the LLM (requires Ollama) |

<br/>

### `practice` — Generate Practice Problems

Generate practice problems with hints and answers at your chosen difficulty level.

```bash
# Default: 5 intermediate problems
math-solver practice --category algebra

# Customize difficulty and count
math-solver practice --category calculus --difficulty advanced --count 10

# Basic geometry practice
math-solver practice -c geometry -d basic -n 3
```

#### Options

| Flag | Short | Type | Default | Description |
|:-----|:------|:-----|:--------|:------------|
| `--category` | `-c` | `TEXT` | *(required)* | Problem category |
| `--difficulty` | `-d` | `CHOICE` | `intermediate` | Difficulty: `basic`, `intermediate`, `advanced` |
| `--count` | `-n` | `INT` | `5` | Number of problems to generate |

<br/>

---

<br/>

## 🌐 Web UI

The Streamlit-based web interface provides an interactive, browser-based experience for all features.

### Launch

```bash
# Start the web UI
streamlit run src/math_solver/web_ui.py

# Or use the Makefile
make web
```

The UI will open at **`http://localhost:8501`**.

### Web UI Features

| Feature | Description |
|:--------|:------------|
| 🔢 **Problem Input** | Enter any math problem in natural language and get instant structured solutions |
| 📝 **Step-by-Step Display** | Expandable solution steps with LaTeX rendering in the browser |
| 📖 **Formula Reference** | Browse all built-in and LLM-extended formulas by category |
| 🏋️ **Practice Quiz** | Interactive practice mode with hints, answers, and difficulty selection |
| 📊 **Category Selector** | Filter by math domain for more accurate results |
| 📄 **LaTeX Preview** | Rendered mathematical notation directly in the browser |

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/architecture.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/images/architecture.svg">
  <img src="docs/images/architecture.svg" alt="System Architecture Diagram" width="800"/>
</picture>

</div>

<br/>

### System Overview

```
User Input (natural language math problem)
    │
    ├──▶ CLI (Click + Rich)        — Terminal interface with colored output
    │       │
    └──▶ Streamlit Web UI          — Browser-based interactive interface
            │
            ▼
    ┌──────────────────────────────┐
    │     MathSolver Core          │
    │     (src/math_solver/core.py)│
    │                              │
    │  ┌─ solve_problem()          │
    │  ├─ generate_practice()      │
    │  ├─ get_formula_library()    │
    │  └─ get_formulas_from_llm()  │
    └──────────┬───────────────────┘
               │
               ▼
    ┌──────────────────────────────┐
    │   Ollama / Gemma 3           │
    │   localhost:11434            │
    │   JSON-structured responses  │
    └──────────────────────────────┘
               │
               ▼
    ┌──────────────────────────────┐
    │   Structured Output          │
    │                              │
    │  MathProblemResult           │
    │  ├── Solution                │
    │  │   └── SolutionStep[]      │
    │  ├── concepts_used[]         │
    │  ├── tips[]                  │
    │  ├── related_problems[]      │
    │  └── latex_output            │
    └──────────────────────────────┘
```

### Project Structure

```
56-math-problem-solver/
│
├── src/
│   └── math_solver/
│       ├── __init__.py            # Package metadata (__version__, __author__)
│       ├── core.py                # Business logic, data models, LLM interaction
│       ├── cli.py                 # Rich CLI with Click commands (solve, formulas, practice)
│       └── web_ui.py              # Streamlit web interface
│
├── tests/
│   ├── test_core.py               # Core logic unit tests
│   └── test_cli.py                # CLI integration tests
│
├── docs/
│   └── images/
│       ├── banner.svg             # Project banner image
│       ├── architecture.svg       # Architecture diagram
│       └── features.svg           # Features overview graphic
│
├── common/                        # Shared LLM client (from parent project)
│   └── llm_client.py              # chat(), check_ollama_running()
│
├── config.yaml                    # Application configuration (LLM, categories, UI)
├── setup.py                       # Package installation & entry points
├── requirements.txt               # Python dependencies
├── Makefile                       # Development task shortcuts
├── .env.example                   # Environment variable template
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

<br/>

---

<br/>

## 📚 API Reference

Use `math_solver` as a Python library in your own projects.

### Data Models

#### `SolutionStep`

A single step in a math solution.

```python
from dataclasses import dataclass

@dataclass
class SolutionStep:
    step_number: int       # Step index (1-based)
    description: str       # What this step does
    work: str = ""         # The mathematical work shown
    explanation: str = ""  # Why we perform this step
```

#### `Solution`

A complete solution containing an answer and ordered steps.

```python
@dataclass
class Solution:
    answer: str                           # The final answer
    steps: List[SolutionStep] = field(default_factory=list)  # Ordered solution steps
```

#### `MathProblemResult`

The top-level result object returned by `solve_problem()`.

```python
@dataclass
class MathProblemResult:
    problem: str = ""                     # Original problem text
    category: str = ""                    # Detected category (algebra, calculus, etc.)
    difficulty: str = ""                  # Detected difficulty (basic, intermediate, advanced)
    solution: Optional[Solution] = None   # The structured solution
    concepts_used: List[str] = field(default_factory=list)    # Math concepts identified
    tips: List[str] = field(default_factory=list)             # Study tips
    related_problems: List[str] = field(default_factory=list) # Suggested practice
    latex_output: str = ""                # LaTeX representation

    def to_dict(self) -> dict:
        """Convert to a plain dictionary (JSON-serializable)."""
        return asdict(self)
```

<br/>

### Core Functions

#### `solve_problem()`

Solve a math problem using the local LLM and return a structured result.

```python
from math_solver.core import solve_problem

# Basic usage
result = solve_problem("Solve 2x + 5 = 15")

# With options
result = solve_problem(
    problem="Find the derivative of x³ + 2x",
    show_steps=True,
    category="calculus"
)

# Access the result
print(result.solution.answer)          # "3x² + 2"
print(result.category)                 # "calculus"
print(result.difficulty)               # "basic"
print(result.latex_output)             # "\\frac{d}{dx}(x^3 + 2x) = 3x^2 + 2"

# Iterate over steps
for step in result.solution.steps:
    print(f"Step {step.step_number}: {step.description}")
    print(f"  Work: {step.work}")
    print(f"  Why:  {step.explanation}")

# Export to dict/JSON
import json
print(json.dumps(result.to_dict(), indent=2))
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `problem` | `str` | *(required)* | The math problem in natural language |
| `show_steps` | `bool` | `True` | Include step-by-step breakdown |
| `category` | `str` | `""` | Hint the problem category (auto-detected if empty) |

**Returns:** `MathProblemResult`

<br/>

#### `generate_practice_problems()`

Generate practice problems for a given category and difficulty.

```python
from math_solver.core import generate_practice_problems

# Generate 5 intermediate algebra problems
problems = generate_practice_problems(
    category="algebra",
    difficulty="intermediate",
    count=5
)

# Result is a dict with structure:
# {
#   "category": "algebra",
#   "difficulty": "intermediate",
#   "problems": [
#     {"number": 1, "problem": "...", "hint": "...", "answer": "..."},
#     ...
#   ]
# }

for p in problems["problems"]:
    print(f"Problem {p['number']}: {p['problem']}")
    print(f"  Hint: {p['hint']}")
    print(f"  Answer: {p['answer']}")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `category` | `str` | *(required)* | Math category |
| `difficulty` | `str` | *(required)* | `basic`, `intermediate`, or `advanced` |
| `count` | `int` | `5` | Number of problems to generate |

**Returns:** `dict`

<br/>

#### `get_formula_library()`

Access the built-in formula library. Works **offline** — no LLM required.

```python
from math_solver.core import get_formula_library

# Get all formulas
all_formulas = get_formula_library()
# Returns: {"categories": {"algebra": [...], "geometry": [...], ...}}

# Get formulas for a specific category
algebra = get_formula_library("algebra")
# Returns: {"category": "algebra", "formulas": [...]}

for f in algebra["formulas"]:
    print(f"{f['name']}: {f['formula']}")
    print(f"  LaTeX: {f['latex']}")
    print(f"  Use:   {f['description']}")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `category` | `str` | `""` | Filter by category (returns all if empty) |

**Returns:** `dict`

<br/>

#### `get_formulas_from_llm()`

Fetch an extended formula library from the LLM for deeper coverage.

```python
from math_solver.core import get_formulas_from_llm

# Fetch extended algebra formulas
extended = get_formulas_from_llm("algebra")

for f in extended.get("formulas", []):
    print(f"{f['name']}: {f['formula']}")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `category` | `str` | *(required)* | The math category to fetch formulas for |

**Returns:** `dict`

<br/>

#### Utility Functions

```python
from math_solver.core import check_service, load_config

# Check if Ollama is running
if check_service():
    print("Ollama is ready!")
else:
    print("Start Ollama with: ollama serve")

# Load configuration
config = load_config()                  # Default path: config.yaml
config = load_config("custom.yaml")     # Custom path
print(config["llm"]["temperature"])     # 0.2
```

<br/>

---

<br/>

## ⚙️ Configuration

All configuration lives in **`config.yaml`** at the project root.

```yaml
# Application metadata
app:
  name: "Math Problem Solver"
  version: "1.0.0"
  log_level: "INFO"

# LLM settings
llm:
  model: "llama3"                   # Ollama model name
  temperature: 0.2                  # Lower = more deterministic (solving)
  max_tokens: 4096                  # Max response length
  base_url: "http://localhost:11434" # Ollama API endpoint

# Supported math categories
categories:
  - algebra
  - calculus
  - geometry
  - statistics
  - arithmetic
  - trigonometry

# Difficulty levels for practice mode
difficulty_levels:
  - basic
  - intermediate
  - advanced

# Streamlit web UI settings
streamlit:
  page_title: "📐 Math Problem Solver"
  layout: "wide"
  theme: "light"
```

### Temperature Settings

The solver uses **different temperatures** for different tasks:

| Task | Temperature | Rationale |
|:-----|:------------|:----------|
| **Solving problems** | `0.2` | Low temperature for accurate, deterministic solutions |
| **Generating practice** | `0.5` | Higher temperature for creative, varied problem generation |
| **Fetching formulas** | `0.2` | Low temperature for accurate formula retrieval |

<br/>

---

<br/>

## 📐 Built-in Formula Library

The formula library is available **offline** — no LLM or network connection required.
Access it programmatically via `get_formula_library()` or through the CLI with `math-solver formulas`.

### Algebra

| Formula | Expression | LaTeX | Description |
|:--------|:-----------|:------|:------------|
| **Quadratic Formula** | `x = (-b ± √(b²-4ac)) / 2a` | `x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}` | Solve ax² + bx + c = 0 |
| **Slope-Intercept** | `y = mx + b` | `y = mx + b` | Linear equation form |
| **Point-Slope Form** | `y - y₁ = m(x - x₁)` | `y - y_1 = m(x - x_1)` | Line through a point with slope |

### Geometry

| Formula | Expression | LaTeX | Description |
|:--------|:-----------|:------|:------------|
| **Circle Area** | `A = πr²` | `A = \pi r^2` | Area of a circle |
| **Pythagorean Theorem** | `a² + b² = c²` | `a^2 + b^2 = c^2` | Right triangle sides |
| **Triangle Area** | `A = ½bh` | `A = \frac{1}{2}bh` | Area of a triangle |

### Calculus

| Formula | Expression | LaTeX | Description |
|:--------|:-----------|:------|:------------|
| **Power Rule** | `d/dx[xⁿ] = nxⁿ⁻¹` | `\frac{d}{dx}x^n = nx^{n-1}` | Derivative of power function |
| **Chain Rule** | `d/dx[f(g(x))] = f'(g(x))·g'(x)` | `\frac{d}{dx}f(g(x)) = f'(g(x)) \cdot g'(x)` | Composite function derivative |

### Trigonometry

| Formula | Expression | LaTeX | Description |
|:--------|:-----------|:------|:------------|
| **Pythagorean Identity** | `sin²θ + cos²θ = 1` | `\sin^2\theta + \cos^2\theta = 1` | Fundamental trig identity |
| **Law of Cosines** | `c² = a² + b² - 2ab·cos(C)` | `c^2 = a^2 + b^2 - 2ab\cos C` | Relate triangle sides and angles |

> 💡 **Tip:** Use `math-solver formulas --extended --category algebra` to fetch additional formulas from the LLM beyond the built-in set.

<br/>

---

<br/>

## 🧪 Testing

### Run the Test Suite

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=src/math_solver --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v
pytest tests/test_cli.py -v

# Run tests matching a pattern
pytest tests/ -v -k "test_formula"
```

### Using the Makefile

```bash
# Run tests
make test

# Run linting
make lint

# Run all checks
make check
```

### Test Structure

```
tests/
├── test_core.py      # Unit tests for core.py
│   ├── test data models (SolutionStep, Solution, MathProblemResult)
│   ├── test get_formula_library()
│   ├── test load_config()
│   └── test JSON parsing
│
└── test_cli.py        # Integration tests for cli.py
    ├── test CLI commands (solve, formulas, practice)
    ├── test option validation
    └── test output formatting
```

<br/>

---

<br/>

## 🤖 Local LLM vs Cloud AI

Why run math solving **locally** instead of using a cloud API?

| Aspect | 🏠 Local LLM (This Project) | ☁️ Cloud API (GPT, Claude, etc.) |
|:-------|:----------------------------|:---------------------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Problems sent to external servers |
| **Cost** | ✅ Free after hardware investment | ❌ Per-token pricing adds up |
| **Latency** | ✅ No network round-trip | ❌ Depends on internet speed |
| **Availability** | ✅ Works offline, no outages | ❌ Service disruptions possible |
| **Customization** | ✅ Full control over model & prompts | ⚠️ Limited by API constraints |
| **Rate Limits** | ✅ None — unlimited usage | ❌ Throttled under heavy use |
| **Model Choice** | ✅ Swap models freely (Gemma, Llama, etc.) | ❌ Locked to provider's offerings |
| **Accuracy** | ⚠️ Depends on model size | ✅ Larger models may be more accurate |
| **Setup** | ⚠️ Requires Ollama + model download | ✅ Just an API key |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What models work best for math problem solving?</strong></summary>

<br/>

The project defaults to **Gemma 3** via Ollama, which provides a good balance of accuracy and speed for mathematical reasoning. Other models that work well:

- **Llama 3** — Strong general reasoning, good at algebra and calculus
- **Mistral** — Fast inference, decent at structured math output
- **Phi-3** — Compact but surprisingly capable for basic math

To switch models, update `config.yaml`:

```yaml
llm:
  model: "gemma3"   # Change to any Ollama-supported model
```

</details>

<details>
<summary><strong>Can I use this without step-by-step explanations?</strong></summary>

<br/>

Yes! Use the `--no-steps` flag to get just the answer:

```bash
math-solver solve --problem "What is 15% of 200?" --no-steps
```

Or programmatically:

```python
result = solve_problem("What is 15% of 200?", show_steps=False)
print(result.solution.answer)  # "30"
```

</details>

<details>
<summary><strong>How do I add custom formulas to the built-in library?</strong></summary>

<br/>

Edit the `BUILTIN_FORMULAS` dictionary in `src/math_solver/core.py`:

```python
BUILTIN_FORMULAS = {
    "algebra": [
        # ... existing formulas ...
        {
            "name": "Difference of Squares",
            "formula": "a² - b² = (a+b)(a-b)",
            "latex": "a^2 - b^2 = (a+b)(a-b)",
            "description": "Factor difference of two squares"
        },
    ],
    # Add a new category
    "number_theory": [
        {
            "name": "Euler's Theorem",
            "formula": "a^φ(n) ≡ 1 (mod n)",
            "latex": "a^{\\phi(n)} \\equiv 1 \\pmod{n}",
            "description": "For coprime a and n"
        },
    ],
}
```

</details>

<details>
<summary><strong>Why does the solver sometimes give wrong answers?</strong></summary>

<br/>

Local LLMs are powerful but not infallible, especially with:

- **Complex multi-step calculus** — Integration by parts, partial fractions
- **Word problems with ambiguity** — The LLM may misinterpret the question
- **Very large numbers** — Arithmetic precision can degrade

**Tips for better accuracy:**

1. **Specify the category** with `--category` to guide the model
2. **Use the lower temperature** (`0.2`) in `config.yaml` for deterministic output
3. **Verify critical results** — treat the solver as a tutor, not an oracle
4. **Try a larger model** — swap to `llama3:70b` if accuracy matters more than speed

</details>

<details>
<summary><strong>Can I export solutions for use in LaTeX documents?</strong></summary>

<br/>

Yes! Every solution includes a `latex_output` field. Save it via the CLI:

```bash
# Save full solution as JSON
math-solver solve --problem "∫ sin(x) dx" --output solution.json
```

Then extract the LaTeX:

```python
import json

with open("solution.json") as f:
    data = json.load(f)

latex = data["latex_output"]
print(latex)
# Output: \int \sin(x) \, dx = -\cos(x) + C
```

Paste the output directly into your `.tex` file wrapped in `$...$` or `\[...\]`.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/math-problem-solver.git
cd math-problem-solver

# 2. Install in development mode
pip install -e ".[dev]"

# 3. Run the test suite
pytest tests/ -v

# 4. Make your changes and ensure tests pass
pytest tests/ -v --cov=src/math_solver
```

### Contribution Ideas

- 📐 **Add formulas** — Expand the built-in formula library with more categories
- 🧪 **Add tests** — Increase test coverage for edge cases
- 🌐 **Improve the Web UI** — Add charts, history, or export features
- 📖 **Documentation** — Improve examples, add tutorials
- 🐛 **Bug fixes** — Check the [Issues](https://github.com/kennedyraju55/math-problem-solver/issues) page

### Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

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

<img src="docs/images/banner.svg" alt="Math Problem Solver" width="600"/>

<br/>
<br/>

**Built with ❤️ as part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<br/>

[⬆ Back to Top](#)

<br/>

<sub>📐 Math Problem Solver — Project #56 — AI-powered math solving, 100% local</sub>

</div>
