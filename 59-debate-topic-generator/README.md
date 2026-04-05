<div align="center">

<!-- Hero Banner -->
<img src="docs/images/banner.svg" alt="Debate Topic Generator — AI-Powered Balanced Debate Topics" width="800"/>

<br/>
<br/>

<!-- Badges -->
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+"/></a>
<a href="https://ollama.com/"><img src="https://img.shields.io/badge/Ollama-Local_LLM-FF6F00?style=for-the-badge&logo=meta&logoColor=white" alt="Ollama"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>
<a href="https://click.palletsprojects.com/"><img src="https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Click CLI"/></a>
<a href="#-license"><img src="https://img.shields.io/badge/License-MIT-EAB308?style=for-the-badge" alt="MIT License"/></a>

<br/>

<a href="https://github.com/kennedyraju55/debate-topic-generator/actions"><img src="https://img.shields.io/badge/Tests-Passing-brightgreen?style=flat-square&logo=pytest&logoColor=white" alt="Tests"/></a>
<a href="https://github.com/kennedyraju55/debate-topic-generator"><img src="https://img.shields.io/badge/PRs-Welcome-4361ee?style=flat-square" alt="PRs Welcome"/></a>
<a href="https://github.com/kennedyraju55/90-local-llm-projects"><img src="https://img.shields.io/badge/Part_of-90_Local_LLM_Projects-blueviolet?style=flat-square" alt="90 Local LLM Projects"/></a>

<br/>
<br/>

<strong>⚔️ Generate debate topics with evidence-rated arguments, counterargument pairs,<br/>moderator guides, and weighted judging criteria — powered entirely by a local LLM.</strong>

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Architecture](#-architecture) •
[FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Preparing for a debate is hard. You need balanced arguments, anticipate counterpoints, build rebuttals, design judging rubrics, and write moderator scripts — often from scratch. This tool automates **all of it** with a single command.

| Challenge | Without This Tool | With Debate Topic Generator |
|---|---|---|
| **Finding balanced topics** | Hours of manual research across sources | One command generates structured motions with context |
| **Building arguments** | Separate pro/con lists with inconsistent depth | Matched pro/con arguments with evidence & strength ratings |
| **Anticipating rebuttals** | Guesswork and incomplete preparation | Structured argument → counterargument → rebuttal chains |
| **Creating judging rubrics** | Generic scorecards that don't fit the topic | Weighted, topic-specific criteria that sum to 100% |
| **Writing moderator guides** | Templated scripts with no topic awareness | AI-generated opening, timing, key questions & closing |

> **Built for:** Debate coaches, competitive debaters, Model UN organizers, classroom teachers, public speaking clubs, and anyone who wants structured argumentation on any subject.

<br/>

---

<br/>

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Feature Overview — 6 core capabilities" width="800"/>
</div>

<br/>

| Category | Feature | Description |
|:---:|---|---|
| **Generation** | ⚖️ Balanced Pro/Con Arguments | Every topic gets equal-weight arguments for both sides, each with a point, explanation, evidence, and strength rating |
| **Generation** | ⚔️ Counterargument & Rebuttal Pairs | Structured `argument → counterargument → rebuttal` chains that model real debate flow |
| **Evaluation** | 📊 Evidence Strength Ratings | Every argument is classified as `weak`, `moderate`, or `strong` based on evidence quality |
| **Evaluation** | 🏆 Weighted Judging Criteria | Auto-generated scoring rubrics with percentage-based weights (Argument Quality 30%, Evidence 25%, Rebuttal 25%, Presentation 20%) |
| **Moderation** | 📋 Moderator Guide Generation | Complete moderator scripts: opening statements, time allocation, key probing questions, closing instructions |
| **Moderation** | 🎯 3 Complexity Levels | `basic` for beginners, `intermediate` for clubs, `advanced` for competitive tournaments |
| **Interface** | 💻 Rich Terminal CLI | Beautiful side-by-side pro/con display with color-coded strength indicators via Rich |
| **Interface** | 🌐 Streamlit Web Dashboard | Interactive web UI for generating, browsing, and exporting debate topics |
| **Config** | ⚙️ YAML Configuration | Centralized `config.yaml` for LLM temperature, token limits, default criteria weights, and more |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| **Python** | 3.9+ | Runtime |
| **Ollama** | Latest | Local LLM inference |
| **Gemma 3** | Via Ollama | Language model |

### 1. Clone & Install

```bash
git clone https://github.com/kennedyraju55/debate-topic-generator.git
cd debate-topic-generator
pip install -e ".[dev]"
```

### 2. Start Ollama

```bash
# Start the Ollama service
ollama serve

# Pull the Gemma 3 model (first time only)
ollama pull gemma3
```

### 3. Generate Your First Debate

```bash
# Generate 3 intermediate-level debate topics about technology
debate-gen generate --subject "artificial intelligence" --complexity intermediate --topics 3
```

**Expected output:**

```
┌──────────────────────────────────────────────────┐
│ 🎙️ Debate Topics                                 │
│ artificial intelligence                          │
│ Complexity: intermediate | Topics: 3             │
└──────────────────────────────────────────────────┘

════════════════════════════════════════════════════
┌ Topic 1 ─────────────────────────────────────────┐
│ This House Believes That AI Should Be Regulated  │
│ by Governments                                   │
│                                                  │
│ Background context for the debate...             │
└──────────────────────────────────────────────────┘

┌─────── ✓ PRO Arguments ───────┐ ┌─────── ✗ CON Arguments ───────┐
│ • Public Safety       [strong] │ │ • Innovation Stifling  [strong]│
│ • Accountability      [moderate│ │ • Global Competition   [moderate│
│ • Bias Prevention     [strong] │ │ • Implementation Cost  [weak]  │
└────────────────────────────────┘ └────────────────────────────────┘
```

<br/>

---

<br/>

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and uses [Rich](https://rich.readthedocs.io/) for beautiful terminal output.

### Global Options

```bash
debate-gen [OPTIONS] COMMAND [ARGS]
```

| Option | Short | Description |
|---|---|---|
| `--verbose` | `-v` | Enable debug-level logging |
| `--help` | | Show help message and exit |

---

### `generate` — Generate Debate Topics

Generate complete debate topics with balanced arguments, counterargument pairs, judging criteria, and key questions.

```bash
debate-gen generate [OPTIONS]
```

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
| `--subject` | `-s` | `TEXT` | **Required** | Subject area for debate topics |
| `--complexity` | `-c` | `basic\|intermediate\|advanced` | `intermediate` | Complexity level |
| `--topics` | `-t` | `INT` | `3` | Number of topics to generate |
| `--output` | `-o` | `PATH` | — | Save output to JSON file |

**Examples:**

```bash
# Basic: Simple topics for beginners
debate-gen generate -s "social media" -c basic -t 2

# Intermediate: Club-level debate preparation
debate-gen generate -s "climate change" -c intermediate -t 5

# Advanced: Tournament-grade topics with full analysis
debate-gen generate -s "bioethics" -c advanced -t 3

# Save to file for later use
debate-gen generate -s "education reform" -o debate_output.json

# Verbose mode for debugging
debate-gen -v generate -s "cryptocurrency" -c advanced
```

**JSON output structure** (when using `--output`):

```json
{
  "subject": "education reform",
  "complexity": "intermediate",
  "topics": [
    {
      "number": 1,
      "motion": "This House Would Abolish Standardized Testing",
      "context": "Standardized testing has been a cornerstone...",
      "pro_arguments": [
        {
          "point": "Reduces educational inequality",
          "explanation": "Standardized tests disadvantage...",
          "evidence": "Research from the National Education Association...",
          "strength": "strong"
        }
      ],
      "con_arguments": [...],
      "counterargument_pairs": [
        {
          "argument": "Tests provide objective measurement",
          "counterargument": "Objectivity is illusory when...",
          "rebuttal": "While no measure is perfect..."
        }
      ],
      "key_questions": ["How do we measure learning without tests?"],
      "difficulty": "medium",
      "judging_criteria": [
        { "criterion": "Argument Quality", "description": "...", "weight": 30 }
      ]
    }
  ]
}
```

---

### `moderator` — Generate Moderator Guide

Generate a complete moderator guide for a specific debate motion, including opening statement, time allocation, suggested questions, and closing instructions.

```bash
debate-gen moderator [OPTIONS]
```

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
| `--motion` | `-m` | `TEXT` | **Required** | The debate motion/resolution |

**Examples:**

```bash
# Generate a moderator guide
debate-gen moderator -m "This House Believes That Social Media Does More Harm Than Good"

# For a policy debate
debate-gen moderator -m "Governments should implement universal basic income"
```

**Sample output:**

```
┌──────────────────────────────────────────────────────┐
│ 📋 Moderator Guide                                   │
│                                                      │
│ Opening:                                             │
│ Good evening, distinguished judges, debaters, and    │
│ audience. Today's motion is...                       │
│                                                      │
│ Time: 5 min opening, 3 min cross-exam, 2 min closing │
│                                                      │
│ Closing:                                             │
│ Thank both teams for their arguments...              │
└──────────────────────────────────────────────────────┘

Suggested Questions:
  • How do you define "harm" in the context of social media?
  • Can regulation solve the issues you've identified?
  • What evidence supports your claim about mental health?
```

<br/>

---

<br/>

## 🌐 Web UI

The Streamlit-based web interface provides an interactive dashboard for generating and exploring debate topics.

### Launch

```bash
streamlit run src/debate_gen/web_ui.py
```

The app opens at `http://localhost:8501` by default.

### Web UI Features

| Feature | Description |
|---|---|
| 🎯 **Subject Input** | Free-text input for any debate subject area |
| 📊 **Complexity Selector** | Dropdown for basic / intermediate / advanced |
| ✅❌ **Pro/Con Cards** | Side-by-side argument display with color-coded strength |
| ⚔️ **Counterargument Viewer** | Expandable argument → counter → rebuttal chains |
| 📋 **Moderator Panel** | One-click moderator guide generation |
| 🏆 **Judging Rubric** | Visual table of weighted evaluation criteria |
| 💾 **JSON Export** | Download generated topics as structured JSON |

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="System Architecture Diagram" width="800"/>
</div>

<br/>

### How It Works

1. **User** provides a subject, complexity level, and number of topics via CLI or Web UI
2. **Interface layer** (Click CLI or Streamlit) validates input and passes it to the core engine
3. **DebateGen Core** constructs a structured prompt with the `SYSTEM_PROMPT` template
4. **Ollama** processes the prompt through the Gemma 3 model and returns structured JSON
5. **Core Engine** parses the JSON response into typed Python dataclasses
6. **Interface layer** renders the structured data with Rich (CLI) or Streamlit (Web)

### Project Structure

```
59-debate-topic-generator/
│
├── src/
│   └── debate_gen/
│       ├── __init__.py              # Package metadata & exports
│       ├── core.py                  # Data models, LLM interaction, business logic
│       ├── cli.py                   # Click CLI with Rich terminal rendering
│       └── web_ui.py               # Streamlit web dashboard
│
├── tests/
│   ├── __init__.py                  # Test package init
│   ├── test_core.py                 # Unit tests for core logic
│   └── test_cli.py                  # CLI integration tests
│
├── common/
│   └── llm_client.py               # Shared Ollama client (cross-project)
│
├── docs/
│   └── images/
│       ├── banner.svg               # Project hero banner
│       ├── architecture.svg         # System architecture diagram
│       └── features.svg             # Feature overview graphic
│
├── config.yaml                      # YAML configuration (LLM, debate, judging)
├── setup.py                         # Package installation & entry points
├── requirements.txt                 # Python dependencies
├── Makefile                         # Development task shortcuts
├── .env.example                     # Environment variable template
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

### Data Flow

```
┌─────────────┐    ┌─────────────────┐    ┌──────────────┐    ┌───────────┐
│   User       │───▶│  CLI / Streamlit │───▶│  core.py      │───▶│  Ollama   │
│   Input      │    │  (Interface)     │    │  (Engine)      │    │  (LLM)    │
└─────────────┘    └─────────────────┘    └──────────────┘    └───────────┘
                           │                       │                  │
                           │                       ▼                  │
                           │              ┌──────────────┐            │
                           │              │  JSON Parse   │◀───────────┘
                           │              │  + Dataclass   │
                           │              └──────────────┘
                           │                       │
                           ▼                       ▼
                   ┌─────────────────┐    ┌──────────────┐
                   │  Rich / Streamlit│◀───│  DebateSet    │
                   │  Rendering       │    │  Object       │
                   └─────────────────┘    └──────────────┘
```

<br/>

---

<br/>

## 📚 API Reference

All data models are Python [dataclasses](https://docs.python.org/3/library/dataclasses.html) defined in `src/debate_gen/core.py`. They serialize cleanly to dictionaries and JSON via `dataclasses.asdict()`.

---

### `Argument`

Represents a single debate argument (pro or con) with evidence and strength rating.

```python
from debate_gen.core import Argument

arg = Argument(
    point="Universal healthcare reduces inequality",
    explanation="Countries with universal systems show lower Gini coefficients...",
    evidence="WHO 2023 report shows 23% reduction in health-related poverty",
    strength="strong"   # "weak" | "moderate" | "strong"
)

print(arg.point)       # "Universal healthcare reduces inequality"
print(arg.strength)    # "strong"
```

| Field | Type | Description |
|---|---|---|
| `point` | `str` | Summary of the argument |
| `explanation` | `str` | Detailed explanation |
| `evidence` | `str` | Supporting evidence or research citation |
| `strength` | `str` | Rating: `weak`, `moderate`, or `strong` |

---

### `CounterargumentPair`

A structured chain: original argument → counterargument → rebuttal.

```python
from debate_gen.core import CounterargumentPair

pair = CounterargumentPair(
    argument="Social media connects people globally",
    counterargument="Online connections are superficial and reduce real interaction",
    rebuttal="Studies show online communities provide vital support for isolated groups"
)

print(pair.argument)          # Original claim
print(pair.counterargument)   # The opposing response
print(pair.rebuttal)          # Defense against the counter
```

| Field | Type | Description |
|---|---|---|
| `argument` | `str` | The original argument being challenged |
| `counterargument` | `str` | The opposing counterpoint |
| `rebuttal` | `str` | Defense against the counterargument |

---

### `JudgingCriteria`

A weighted criterion for evaluating debate performance.

```python
from debate_gen.core import JudgingCriteria

criteria = JudgingCriteria(
    criterion="Argument Quality",
    description="Clarity, logic, and coherence of arguments presented",
    weight=30   # Percentage weight (all criteria should sum to 100)
)

print(f"{criteria.criterion}: {criteria.weight}%")
# "Argument Quality: 30%"
```

| Field | Type | Description |
|---|---|---|
| `criterion` | `str` | Name of the evaluation criterion |
| `description` | `str` | What judges should evaluate |
| `weight` | `int` | Percentage weight (0–100) |

**Default judging criteria** (from `config.yaml`):

| Criterion | Weight |
|---|---|
| Argument Quality | 30% |
| Evidence Strength | 25% |
| Rebuttal Effectiveness | 25% |
| Presentation | 20% |

---

### `ModeratorGuide`

Complete moderator script for running a debate session.

```python
from debate_gen.core import ModeratorGuide

guide = ModeratorGuide(
    opening_statement="Welcome to today's debate on AI regulation...",
    time_allocation="5 min opening, 3 min cross-examination, 2 min closing",
    key_questions=[
        "How do you define responsible AI development?",
        "What enforcement mechanisms do you propose?"
    ],
    closing_instructions="Thank both teams and summarize key points..."
)

for q in guide.key_questions:
    print(f"  • {q}")
```

| Field | Type | Description |
|---|---|---|
| `opening_statement` | `str` | How to open the debate |
| `time_allocation` | `str` | Time distribution for each segment |
| `key_questions` | `List[str]` | Probing questions for the moderator to ask |
| `closing_instructions` | `str` | How to wrap up the debate |

---

### `DebateTopic`

A single debate topic with all associated data: arguments, counterarguments, judging criteria, and moderator guide.

```python
from debate_gen.core import DebateTopic, Argument, CounterargumentPair, JudgingCriteria

topic = DebateTopic(
    number=1,
    motion="This House Would Ban Homework in Primary Schools",
    context="The debate over homework effectiveness has intensified...",
    pro_arguments=[
        Argument(point="Reduces stress", explanation="...", evidence="...", strength="strong")
    ],
    con_arguments=[
        Argument(point="Reinforces learning", explanation="...", evidence="...", strength="moderate")
    ],
    counterargument_pairs=[
        CounterargumentPair(
            argument="Homework builds discipline",
            counterargument="Discipline can be built through other activities",
            rebuttal="However, academic discipline specifically requires..."
        )
    ],
    key_questions=["At what age does homework become beneficial?"],
    difficulty="medium",
    judging_criteria=[
        JudgingCriteria(criterion="Evidence Quality", description="...", weight=30)
    ],
    moderator_guide=None
)

print(f"Topic {topic.number}: {topic.motion}")
print(f"Pro args: {len(topic.pro_arguments)}, Con args: {len(topic.con_arguments)}")
```

| Field | Type | Description |
|---|---|---|
| `number` | `int` | Topic sequence number |
| `motion` | `str` | The debate motion/resolution |
| `context` | `str` | Background context for the topic |
| `pro_arguments` | `List[Argument]` | Arguments in favor |
| `con_arguments` | `List[Argument]` | Arguments against |
| `counterarguments` | `List[str]` | Common counterarguments (simple list) |
| `counterargument_pairs` | `List[CounterargumentPair]` | Structured argument/counter/rebuttal chains |
| `key_questions` | `List[str]` | Discussion questions for debaters |
| `difficulty` | `str` | `easy`, `medium`, or `hard` |
| `judging_criteria` | `List[JudgingCriteria]` | Weighted evaluation criteria |
| `moderator_guide` | `Optional[ModeratorGuide]` | Moderator guide (if generated) |

---

### `DebateSet`

Container for a complete set of debate topics on a subject.

```python
from debate_gen.core import generate_debate_topics

# Generate a full debate set
debate_set = generate_debate_topics(
    subject="renewable energy",
    complexity="advanced",
    num_topics=3
)

# Access structured data
print(f"Subject: {debate_set.subject}")
print(f"Complexity: {debate_set.complexity}")
print(f"Topics generated: {len(debate_set.topics)}")

# Serialize to dictionary (for JSON export)
data = debate_set.to_dict()

# Iterate over topics
for topic in debate_set.topics:
    print(f"\n  Topic {topic.number}: {topic.motion}")
    print(f"    Pro arguments: {len(topic.pro_arguments)}")
    print(f"    Con arguments: {len(topic.con_arguments)}")
    print(f"    Counterargument pairs: {len(topic.counterargument_pairs)}")
```

| Field | Type | Description |
|---|---|---|
| `subject` | `str` | The subject area |
| `complexity` | `str` | `basic`, `intermediate`, or `advanced` |
| `topics` | `List[DebateTopic]` | List of generated debate topics |

| Method | Returns | Description |
|---|---|---|
| `to_dict()` | `dict` | Serializes the entire debate set to a dictionary via `dataclasses.asdict()` |

---

### Core Functions

#### `generate_debate_topics(subject, complexity, num_topics) → DebateSet`

Main generation function. Sends a structured prompt to the LLM and parses the response into typed dataclasses.

```python
from debate_gen.core import generate_debate_topics

result = generate_debate_topics(
    subject="artificial intelligence",
    complexity="intermediate",   # "basic" | "intermediate" | "advanced"
    num_topics=3
)
```

#### `generate_moderator_guide(motion) → ModeratorGuide`

Generates a complete moderator script for a specific motion.

```python
from debate_gen.core import generate_moderator_guide

guide = generate_moderator_guide("This House Would Ban Autonomous Weapons")
print(guide.opening_statement)
print(guide.time_allocation)
```

#### `rate_evidence_strength(evidence) → str`

Classifies evidence strength based on word count heuristics.

```python
from debate_gen.core import rate_evidence_strength

rate_evidence_strength("")                        # → "weak"
rate_evidence_strength("Some data")               # → "weak"   (< 5 words)
rate_evidence_strength("A moderate amount of evidence here")  # → "moderate" (5-14 words)
rate_evidence_strength("According to the 2023 WHO report, countries with universal healthcare systems show a 23% reduction in health-related poverty compared to those without such systems")  # → "strong" (15+ words)
```

| Word Count | Rating |
|---|---|
| 0 (empty) | `weak` |
| 1–4 | `weak` |
| 5–14 | `moderate` |
| 15+ | `strong` |

#### `check_service() → bool`

Checks whether the Ollama service is running and accessible.

```python
from debate_gen.core import check_service

if check_service():
    print("✅ Ollama is running")
else:
    print("❌ Start Ollama with: ollama serve")
```

<br/>

---

<br/>

## ⚙️ Configuration

All settings are managed via `config.yaml` in the project root:

```yaml
# Application metadata
app:
  name: "Debate Topic Generator"
  version: "1.0.0"
  log_level: "INFO"

# LLM connection settings
llm:
  model: "llama3"
  temperature: 0.8          # Higher = more creative topics (0.0–1.0)
  max_tokens: 8192          # Max response length from LLM
  base_url: "http://localhost:11434"

# Debate generation defaults
debate:
  default_topics: 3
  complexity_levels:
    - basic
    - intermediate
    - advanced
  evidence_strength_levels:
    - weak
    - moderate
    - strong

# Default judging criteria weights (must sum to 100)
judging:
  default_criteria:
    - criterion: "Argument Quality"
      weight: 30
    - criterion: "Evidence Strength"
      weight: 25
    - criterion: "Rebuttal Effectiveness"
      weight: 25
    - criterion: "Presentation"
      weight: 20

# Streamlit web UI settings
streamlit:
  page_title: "🎙️ Debate Topic Generator"
  layout: "wide"
```

### Key Configuration Options

| Setting | Default | Description |
|---|---|---|
| `llm.temperature` | `0.8` | Controls creativity vs. consistency. Lower values (0.2–0.5) produce more predictable topics; higher values (0.7–1.0) generate more diverse motions. |
| `llm.max_tokens` | `8192` | Maximum number of tokens in LLM response. Increase for more detailed arguments or more topics per request. |
| `llm.base_url` | `http://localhost:11434` | Ollama API endpoint. Change if running Ollama on a different host or port. |
| `debate.default_topics` | `3` | Default number of topics generated when `--topics` is not specified. |
| `judging.default_criteria` | 4 criteria | Default judging rubric. Weights must sum to 100. |

<br/>

---

<br/>

## 🧪 Testing

The test suite covers core logic and CLI integration.

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=src/debate_gen --cov-report=term-missing

# Run specific test file
pytest tests/test_core.py -v

# Run specific test by name
pytest tests/ -v -k "test_rate_evidence"
```

### Test Structure

| File | Covers | Description |
|---|---|---|
| `tests/test_core.py` | `core.py` | Data model construction, `rate_evidence_strength()`, JSON parsing, `to_dict()` serialization |
| `tests/test_cli.py` | `cli.py` | CLI command invocation, argument validation, output formatting, error handling |

<br/>

---

<br/>

## 🆚 Local LLM vs. Cloud AI

This project runs **100% locally** using Ollama. Here's how it compares to cloud-based alternatives:

| Aspect | 🏠 Local LLM (This Project) | ☁️ Cloud AI (GPT-4, Claude, etc.) |
|---|---|---|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after initial setup | ❌ Pay-per-token pricing |
| **Latency** | ⚡ No network round-trip | 🐌 Depends on API response time |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Quality** | 🟡 Good for structured tasks | ✅ Generally higher quality responses |
| **Speed** | 🟡 Depends on local GPU/CPU | ✅ Optimized inference infrastructure |
| **Customization** | ✅ Full control over model & prompts | 🟡 Limited to API parameters |
| **Reproducibility** | ✅ Same model version always | 🟡 Model versions may change |
| **Setup** | 🟡 Requires Ollama + model download | ✅ Just an API key |
| **Rate Limits** | ✅ No limits | ❌ API rate limits apply |

> **Bottom line:** Local LLM is ideal for privacy-sensitive debate prep (e.g., tournament strategies) and unlimited generation without cost concerns. Cloud AI is better when you need the highest possible argument quality.

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>How are pro/con arguments balanced?</strong></summary>

<br/>

The system prompt explicitly instructs the LLM to generate **equal numbers** of pro and con arguments with comparable depth and evidence quality. The prompt template in `core.py` requests "at least 3 pro arguments and 3 con arguments with evidence suggestions and strength ratings" for each topic. The LLM is guided to provide substantive evidence for both sides, preventing one-sided outputs.

The strength rating system (`weak`, `moderate`, `strong`) also helps ensure quality parity — if one side consistently gets `strong` ratings while the other gets `weak`, it signals an imbalance that the user can address.

</details>

<details>
<summary><strong>What's the difference between <code>counterarguments</code> and <code>counterargument_pairs</code>?</strong></summary>

<br/>

- **`counterarguments`** (`List[str]`): A simple list of common counterarguments as standalone strings. These are quick-reference talking points.
- **`counterargument_pairs`** (`List[CounterargumentPair]`): Structured triplets containing `argument → counterargument → rebuttal`. These model the actual flow of a debate round where one side makes a claim, the other responds, and the first side defends.

Use `counterargument_pairs` for debate practice and preparation; use `counterarguments` for quick brainstorming.

</details>

<details>
<summary><strong>Can I use a different LLM model instead of Gemma 3?</strong></summary>

<br/>

Yes! Any model available through Ollama works. Update the `llm.model` field in `config.yaml`:

```yaml
llm:
  model: "llama3"       # Meta's LLaMA 3
  # model: "mistral"    # Mistral 7B
  # model: "gemma3"     # Google's Gemma 3
  # model: "phi3"       # Microsoft's Phi-3
```

Then pull the model: `ollama pull <model-name>`. Larger models (13B+) generally produce better argument quality but require more RAM and GPU memory.

</details>

<details>
<summary><strong>How does the evidence strength rating work?</strong></summary>

<br/>

The `rate_evidence_strength()` function uses a word-count heuristic:

| Condition | Rating | Rationale |
|---|---|---|
| Empty string | `weak` | No evidence provided |
| < 5 words | `weak` | Too brief to be substantive |
| 5–14 words | `moderate` | Some supporting detail |
| 15+ words | `strong` | Detailed evidence with specifics |

This is a fast, deterministic classifier. For LLM-generated topics, the model assigns its own strength ratings based on the quality and specificity of the evidence it generates.

</details>

<details>
<summary><strong>How do judging criteria weights work?</strong></summary>

<br/>

Each `JudgingCriteria` has a `weight` field (integer, 0–100) representing the percentage importance of that criterion. All weights for a topic should sum to 100%. The default criteria from `config.yaml` are:

| Criterion | Weight | What It Measures |
|---|---|---|
| Argument Quality | 30% | Clarity, logic, and coherence of arguments |
| Evidence Strength | 25% | Quality and relevance of supporting evidence |
| Rebuttal Effectiveness | 25% | Ability to address and counter opposing arguments |
| Presentation | 20% | Delivery, structure, and persuasiveness |

Judges multiply the score for each criterion by its weight to calculate the final score. You can customize these defaults in `config.yaml` or let the LLM generate topic-specific criteria.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! This project is part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection.

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes and write tests
4. **Run** the test suite: `pytest tests/ -v`
5. **Commit** with a descriptive message: `git commit -m "feat: add topic filtering by difficulty"`
6. **Push** to your fork: `git push origin feature/your-feature-name`
7. **Open** a Pull Request

### Development Setup

```bash
# Clone and install in development mode
git clone https://github.com/kennedyraju55/debate-topic-generator.git
cd debate-topic-generator
pip install -e ".[dev]"

# Run tests
pytest tests/ -v

# Run linting (if configured)
make lint

# Start the web UI in development mode
streamlit run src/debate_gen/web_ui.py
```

### Ideas for Contributions

- 🌍 Multi-language debate topic generation
- 📊 Argument strength visualization charts
- 🔗 Integration with debate timer apps
- 📝 PDF/DOCX export for printed debate briefs
- 🎭 Role-play mode with AI debater simulation
- 📈 Historical topic tracking and comparison

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this software for any purpose, including commercial use.

<br/>

---

<br/>

<div align="center">

**⚖️ Debate Topic Generator**

Built with ❤️ as part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

<br/>

<a href="https://github.com/kennedyraju55/debate-topic-generator">⭐ Star this repo</a> •
<a href="https://github.com/kennedyraju55/debate-topic-generator/issues">🐛 Report a Bug</a> •
<a href="https://github.com/kennedyraju55/debate-topic-generator/issues">💡 Request a Feature</a>

<br/>
<br/>

<sub>Powered by Ollama • Gemma 3 • Python • Click • Rich • Streamlit</sub>

</div>
