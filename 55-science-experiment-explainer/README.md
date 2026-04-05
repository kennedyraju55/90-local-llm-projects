<div align="center">

  <!-- Hero Banner -->
  <img src="docs/images/banner.svg" alt="Science Experiment Explainer Banner" width="800"/>

  <br/><br/>

  <!-- Badges -->
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.10+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"/></a>
  <a href="https://ollama.ai/"><img src="https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=llama&logoColor=white" alt="Ollama"/></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/></a>
  <a href="https://click.palletsprojects.com/"><img src="https://img.shields.io/badge/Click-CLI-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white" alt="Click CLI"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-f1c40f?style=for-the-badge" alt="License: MIT"/></a>

  <br/>

  <a href="https://github.com/kennedyraju55/science-experiment-explainer"><img src="https://img.shields.io/github/stars/kennedyraju55/science-experiment-explainer?style=social" alt="GitHub Stars"/></a>
  <a href="https://github.com/kennedyraju55/science-experiment-explainer/issues"><img src="https://img.shields.io/github/issues/kennedyraju55/science-experiment-explainer?color=7209b7" alt="Open Issues"/></a>
  <a href="https://github.com/kennedyraju55/science-experiment-explainer/pulls"><img src="https://img.shields.io/github/issues-pr/kennedyraju55/science-experiment-explainer?color=3a0ca3" alt="Pull Requests"/></a>
  <img src="https://img.shields.io/badge/code%20style-ruff-000000.svg" alt="Code style: ruff"/>

  <br/><br/>

  <strong>🔬 Production-grade science experiment explainer powered by a local LLM.</strong>
  <br/>
  <em>Step-by-step guides · Safety warnings · Equipment lists · Cost estimates · Difficulty ratings</em>

  <br/><br/>

  <strong>Part of the <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>

  <br/><br/>

  <!-- Quick Links -->
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-web-ui">Web UI</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-faq">FAQ</a> •
  <a href="#-contributing">Contributing</a>

</div>

<br/>

---

<br/>

## 💡 Why This Project?

Science experiments are an incredible way to learn — but explaining them **safely** and **clearly** across
different grade levels is surprisingly hard. This project solves that with AI-powered experiment guides
that include built-in safety data, equipment management, and cost estimates.

| Challenge | Without This Tool | With Science Experiment Explainer |
|-----------|-------------------|-----------------------------------|
| **Safety Information** | Manual research across scattered MSDS sheets | Built-in database with 10+ chemicals, PPE requirements, and risk levels |
| **Grade Adaptation** | One-size-fits-all explanations | AI-adapted content from elementary to college level |
| **Equipment Planning** | Guesswork on what's needed and costs | 15+ items catalogued with household alternatives and USD estimates |
| **Experiment Variations** | Limited to what you already know | LLM-powered alternative suggestions at matching difficulty |
| **Documentation** | Handwritten notes, no consistency | Export to JSON, Markdown, or printable checklists in one click |

<br/>

---

<br/>

## ✨ Features

<div align="center">
  <img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Category | What You Get |
|----------|-------------|
| 🔬 **Experiment Guides** | Detailed step-by-step procedures with tips, timing, and safety notes for every step |
| 🛡️ **Safety First** | 10+ chemical safety profiles, automatic PPE detection, grade-level restrictions, risk assessment |
| 🔧 **Equipment & Costs** | 15+ lab equipment items with household alternatives, cost estimates in USD, substitute suggestions |
| 📤 **Flexible Export** | JSON (machine-readable), Markdown (documentation), Checklist (printable) — all from one command |

### Full Feature List

| Feature | Description |
|---------|-------------|
| 🛡️ **Safety Database** | Built-in chemical & material safety rules with severity levels (Low → Critical) |
| 🔧 **Equipment Lists** | Automatic equipment detection with household alternatives |
| 💰 **Cost Estimates** | Estimated costs for equipment and materials in USD |
| 📊 **Expected Results** | Clear descriptions of what should happen, common issues, and troubleshooting |
| ⭐ **Difficulty Ratings** | Beginner → Intermediate → Advanced → Expert rating system via `DifficultyRating` enum |
| 🔄 **Alternative Experiments** | LLM-powered suggestions for related experiments at similar difficulty |
| 📋 **Step-by-Step Guides** | Numbered `ProcedureStep` objects with tips, timing, and safety notes |
| 🧾 **Materials Checklists** | Printable shopping lists with quantities, substitutes, and cost estimates |
| 📤 **Multiple Export Formats** | JSON, Markdown, and Checklist output via `export_experiment()` |
| 🌐 **Web UI** | Interactive Streamlit dashboard with 4 tabs |
| 💻 **CLI** | Full-featured Click command-line interface with 6 commands |
| 🔍 **Experiment Search** | Search by topic, subject, or difficulty with `search_experiments()` |
| ✅ **Data Validation** | Validate experiment data with `validate_experiment_data()` |
| ⚙️ **Configurable** | YAML config + environment variables for complete customization |
| 🏠 **100% Local** | All AI processing via Ollama — your data never leaves your machine |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.10+ | Runtime |
| **Ollama** | Latest | Local LLM inference engine |
| **Gemma 3** (or any model) | — | Language model for experiment generation |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/science-experiment-explainer.git
cd science-experiment-explainer

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for CLI command
pip install -e .
```

### 2. Start Ollama

```bash
# Start the Ollama server
ollama serve

# Pull Gemma 3 (recommended) or any supported model
ollama pull gemma3
```

### 3. Run Your First Experiment

```bash
# Using the module directly
python -m src.science_explainer.cli explain -e "baking soda volcano"

# Or after editable install
science-explainer explain -e "baking soda volcano"
```

### 4. Launch the Web UI (Optional)

```bash
streamlit run src/science_explainer/web_ui.py
# Or use the Makefile shortcut
make run-web
```

### Quick Install via Makefile

```bash
make install       # Production install
make dev           # Development install (includes pytest, ruff)
make test          # Run all tests
make run-web       # Launch Streamlit dashboard
```

<br/>

---

<br/>

## 💻 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and organized as a command group
with **six sub-commands**. After `pip install -e .`, the `science-explainer` command is available globally.

### `explain` — Generate Experiment Guide

Generate a complete, AI-powered experiment explanation with safety warnings, materials,
procedure steps, expected results, and discussion questions.

```bash
# Basic usage — middle school level, medium detail
science-explainer explain -e "baking soda volcano"

# High school level with detailed output
science-explainer explain -e "electrolysis of water" -l "high school" -d detailed

# Brief overview saved to file
science-explainer explain -e "plant growth" -d brief -o experiment.json

# College-level detailed analysis
science-explainer explain -e "titration of acids and bases" -l "college" -d detailed
```

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--experiment` | `-e` | *(required)* | Name of the experiment to explain |
| `--level` | `-l` | `"middle school"` | Grade level: elementary, middle school, high school, college |
| `--detail` | `-d` | `"medium"` | Detail level: `brief`, `medium`, or `detailed` |
| `--output` | `-o` | — | Save output to a JSON file |

### `search` — Find Experiments

Search the experiment knowledge base by topic, subject area, or difficulty level.

```bash
# Search by topic
science-explainer search -t "chemical reactions"

# Search by subject
science-explainer search -s "Physics"

# Search by difficulty
science-explainer search -d "Intermediate"

# Combine filters
science-explainer search -t "electricity" -s "Physics" -d "Advanced"
```

| Option | Short | Description |
|--------|-------|-------------|
| `--topic` | `-t` | Topic keyword to search for |
| `--subject` | `-s` | Subject area (Chemistry, Physics, Biology, Earth Science, Environmental Science) |
| `--difficulty` | `-d` | Difficulty level (Beginner, Intermediate, Advanced, Expert) |

### `safety` — Safety Information

Look up safety information for materials and chemicals used in experiments.

```bash
# Check safety for common materials
science-explainer safety -e "hydrogen peroxide"
science-explainer safety -e "hydrochloric acid"
science-explainer safety -e "vinegar"

# Check restricted materials
science-explainer safety -e "sodium hydroxide"
```

| Option | Short | Description |
|--------|-------|-------------|
| `--experiment` | `-e` | *(required)* Material or experiment name to look up |

**Output includes:** risk level (🟢🟡🟠🔴), required PPE, safety precautions, and grade restrictions.

### `equipment` — Equipment Details

Get equipment information, household alternatives, and cost estimates.

```bash
# Look up specific equipment
science-explainer equipment -e "beaker"
science-explainer equipment -e "microscope"
science-explainer equipment -e "bunsen burner"
```

| Option | Short | Description |
|--------|-------|-------------|
| `--experiment` | `-e` | *(required)* Equipment item name |

**Output includes:** description, required/optional status, household alternatives, and cost estimate.

### `alternatives` — Suggest Alternatives

Get AI-powered alternative experiment suggestions at a matching difficulty level.

```bash
# Get alternatives for an experiment
science-explainer alternatives -e "baking soda volcano"

# Specify grade level for better suggestions
science-explainer alternatives -e "baking soda volcano" -l "middle school"

# Advanced alternatives
science-explainer alternatives -e "electroplating" -l "high school"
```

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--experiment` | `-e` | *(required)* | Experiment name to find alternatives for |
| `--level` | `-l` | — | Grade level for targeted suggestions |

### `export` — Export Experiment Data

Export previously saved experiment data to different formats.

```bash
# Export to Markdown documentation
science-explainer export -i experiment.json -f markdown -o experiment.md

# Export to printable checklist
science-explainer export -i experiment.json -f checklist -o checklist.txt

# Export to formatted JSON
science-explainer export -i experiment.json -f json -o formatted.json
```

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--input` | `-i` | *(required)* | Input JSON file containing experiment data |
| `--format` | `-f` | `"json"` | Output format: `json`, `markdown`, or `checklist` |
| `--output` | `-o` | — | Output file path |

### Complete CLI Options Reference

| Command | Option | Short | Default | Description |
|---------|--------|-------|---------|-------------|
| `explain` | `--experiment` | `-e` | *(required)* | Experiment name |
| | `--level` | `-l` | `"middle school"` | Grade level |
| | `--detail` | `-d` | `"medium"` | `brief` / `medium` / `detailed` |
| | `--output` | `-o` | — | Save to JSON file |
| `search` | `--topic` | `-t` | — | Topic keyword |
| | `--subject` | `-s` | — | Subject area |
| | `--difficulty` | `-d` | — | Difficulty level |
| `safety` | `--experiment` | `-e` | *(required)* | Material or experiment name |
| `equipment` | `--experiment` | `-e` | *(required)* | Equipment item name |
| `alternatives` | `--experiment` | `-e` | *(required)* | Experiment name |
| | `--level` | `-l` | — | Grade level |
| `export` | `--input` | `-i` | *(required)* | Input JSON file |
| | `--format` | `-f` | `"json"` | `json` / `markdown` / `checklist` |
| | `--output` | `-o` | — | Output file path |

<br/>

---

<br/>

## 🌐 Web UI

The interactive Streamlit dashboard provides a visual interface for all features.

### Launch

```bash
# Direct launch
streamlit run src/science_explainer/web_ui.py

# Via Makefile
make run-web
```

### Dashboard Tabs

| Tab | Features |
|-----|----------|
| 🔬 **Explore Experiment** | Enter experiment name, generate full AI explanation, search experiments by topic |
| 📋 **Step-by-Step Guide** | Interactive checklist with progress tracking, tips per step, duration estimates |
| 🛡️ **Safety Center** | Risk levels with color coding (🟢🟡🟠🔴), PPE checklist, age-appropriateness check |
| 📦 **Materials & Equipment** | Materials checklist, equipment alternatives, cost estimates, printable shopping list |

### Sidebar Controls

| Control | Options | Purpose |
|---------|---------|---------|
| **Subject** | Chemistry, Physics, Biology, Earth Science, Environmental Science | Filter experiments by subject area |
| **Grade Level** | Elementary, Middle School, High School, College | Set appropriate complexity level |
| **Difficulty** | Beginner → Expert (slider) | Fine-tune difficulty rating |

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
  <img src="docs/images/architecture.svg" alt="System Architecture" width="800"/>
</div>

<br/>

The system follows a **layered architecture** with clear separation of concerns:

| Layer | Component | Responsibility |
|-------|-----------|----------------|
| **Interface** | CLI (Click) / Streamlit Web | User interaction, input parsing, output formatting |
| **Core Engine** | `ScienceExplainer` | Orchestrates LLM calls, experiment generation, search, validation |
| **Safety** | `SafetyDatabase` | Chemical safety profiles, PPE requirements, grade restrictions |
| **Equipment** | `EquipmentManager` | Equipment catalog, alternatives, cost estimation |
| **LLM** | Ollama / Gemma 3 | Natural language generation for experiment explanations |
| **Export** | `export_experiment()` | Format conversion (JSON, Markdown, Checklist) |

### Project Structure

```
55-science-experiment-explainer/
├── docs/
│   └── images/
│       ├── banner.svg              # Project banner image
│       ├── architecture.svg        # System architecture diagram
│       └── features.svg            # Feature overview graphic
├── src/
│   └── science_explainer/
│       ├── __init__.py             # Package metadata, version, exports
│       ├── core.py                 # Core engine: dataclasses, SafetyDatabase,
│       │                           #   EquipmentManager, explain/search/export
│       ├── cli.py                  # Click CLI: explain, search, safety,
│       │                           #   equipment, alternatives, export commands
│       └── web_ui.py               # Streamlit web dashboard (4 tabs)
├── tests/
│   ├── __init__.py
│   ├── test_core.py                # Core logic unit tests
│   └── test_cli.py                 # CLI integration tests
├── common/                         # Shared utilities
├── config.yaml                     # Application configuration (YAML)
├── setup.py                        # Package setup & entry points
├── requirements.txt                # Python dependencies
├── Makefile                        # Build, test, run targets
├── .env.example                    # Environment variable template
└── README.md                       # This file
```

<br/>

---

<br/>

## 📚 API Reference

### Core Data Classes

The `science_explainer.core` module defines a rich set of dataclasses for structured experiment data.

#### `Experiment` — Top-Level Container

The primary dataclass representing a complete experiment with all metadata.

```python
from science_explainer.core import Experiment, DifficultyRating

experiment = Experiment(
    name="Baking Soda Volcano",
    subject="Chemistry",
    grade_level="middle school",
    duration="30 minutes",
    objective="Demonstrate an acid-base reaction producing CO₂ gas",
    concepts=["acid-base reactions", "chemical reactions", "gas production"],
    materials=[...],          # list[Material]
    safety=[...],             # list[SafetyWarning]
    procedure=[...],          # list[ProcedureStep]
    results=[...],            # list[ExperimentResult]
    explanation="When baking soda (NaHCO₃) reacts with vinegar (CH₃COOH)...",
    variations=["Try different amounts of baking soda", "Add food coloring"],
    discussion_questions=["What gas is produced?", "Is this reaction endothermic?"],
    difficulty_rating=DifficultyRating.BEGINNER,
    alternatives=[...],       # list[AlternativeExperiment]
    equipment=[...]           # list[Equipment]
)
```

#### `DifficultyRating` — IntEnum

```python
from science_explainer.core import DifficultyRating

class DifficultyRating(IntEnum):
    BEGINNER = 1        # Elementary level, minimal supervision
    INTERMEDIATE = 2    # Middle school, some supervision
    ADVANCED = 3        # High school, trained supervision
    EXPERT = 4          # College level, lab experience required
```

#### `Material` — Experiment Materials

```python
from science_explainer.core import Material

baking_soda = Material(
    item="Baking Soda (Sodium Bicarbonate)",
    quantity="2 tablespoons",
    notes="Common household item",
    substitute="Washing soda (less vigorous reaction)",
    cost_estimate=1.50
)
```

| Field | Type | Description |
|-------|------|-------------|
| `item` | `str` | Name of the material |
| `quantity` | `str` | Amount needed |
| `notes` | `str` | Additional notes |
| `substitute` | `str` | Alternative material |
| `cost_estimate` | `float` | Estimated cost in USD |

#### `SafetyWarning` — Safety Information

```python
from science_explainer.core import SafetyWarning

warning = SafetyWarning(
    level="medium",
    description="Hydrogen peroxide can cause skin irritation",
    precaution="Wear gloves when handling concentrated solutions",
    equipment_needed="Safety goggles, nitrile gloves"
)
```

| Field | Type | Description |
|-------|------|-------------|
| `level` | `str` | Risk level: low, medium, high, critical |
| `description` | `str` | Description of the hazard |
| `precaution` | `str` | Safety precaution to take |
| `equipment_needed` | `str` | Required protective equipment |

#### `ProcedureStep` — Step-by-Step Instructions

```python
from science_explainer.core import ProcedureStep

step = ProcedureStep(
    step_num=1,
    instruction="Put on safety goggles and lay down newspaper to protect the surface",
    tip="Work in a well-ventilated area near a sink for easy cleanup",
    duration_minutes=2,
    safety_notes="Always wear eye protection when working with chemicals"
)
```

| Field | Type | Description |
|-------|------|-------------|
| `step_num` | `int` | Step number in sequence |
| `instruction` | `str` | What to do |
| `tip` | `str` | Helpful tip for this step |
| `duration_minutes` | `int` | Estimated time in minutes |
| `safety_notes` | `str` | Safety considerations for this step |

#### `Equipment` — Lab Equipment

```python
from science_explainer.core import Equipment

beaker = Equipment(
    name="Beaker",
    description="Glass container for mixing liquids",
    required=True,
    alternatives=["Mason jar", "Pyrex measuring cup"]
)
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Equipment name |
| `description` | `str` | What it's used for |
| `required` | `bool` | Whether it's essential |
| `alternatives` | `list[str]` | Household alternatives |

### `SafetyDatabase` — Chemical Safety Profiles

The `SafetyDatabase` class provides built-in safety information for 10+ common lab chemicals
and materials, including grade-level restrictions.

```python
from science_explainer.core import SafetyDatabase

safety_db = SafetyDatabase()

# Look up safety info for a material
warning = safety_db.get_safety_info("hydrogen peroxide")
# Returns: SafetyWarning(level="medium", ...)

# Get required PPE for an experiment
ppe_list = safety_db.get_required_ppe(experiment)
# Returns: ["safety goggles", "nitrile gloves"]

# Check overall risk level
risk = safety_db.get_risk_level(experiment)
# Returns: "medium"

# Verify age appropriateness
is_safe = safety_db.check_age_appropriate(experiment, "middle school")
# Returns: True/False
```

#### Built-in Chemical Database

| Material | Risk Level | PPE Required | Grade Restriction |
|----------|-----------|--------------|-------------------|
| Vinegar | 🟢 Low | Safety goggles | None |
| Baking Soda | 🟢 Low | Safety goggles | None |
| Food Coloring | 🟢 Low | None | None |
| Hydrogen Peroxide | 🟡 Medium | Goggles, gloves | None |
| Dry Ice | 🟡 Medium | Insulated gloves, goggles | None |
| Ethanol | 🟡 Medium | Goggles, fire extinguisher | Middle School+ |
| Hydrochloric Acid | 🟠 High | Full PPE, fume hood | High School+ |
| Sodium Hydroxide | 🟠 High | Full PPE | High School+ |
| Magnesium Ribbon | 🟠 High | Goggles, tongs | High School+ |
| Potassium Permanganate | 🟠 High | Goggles, gloves, lab coat | High School+ |

#### Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `get_safety_info()` | `material: str` | `SafetyWarning` | Look up safety data for a material |
| `get_required_ppe()` | `experiment: Experiment` | `list[str]` | Compile PPE list for all materials |
| `get_risk_level()` | `experiment: Experiment` | `str` | Overall risk assessment |
| `check_age_appropriate()` | `experiment, grade_level` | `bool` | Grade-level safety check |

### `EquipmentManager` — Equipment Catalog

The `EquipmentManager` class manages a catalog of 15+ lab equipment items with
descriptions, household alternatives, and cost estimates.

```python
from science_explainer.core import EquipmentManager

equip_mgr = EquipmentManager()

# Get equipment needed for an experiment
equipment_list = equip_mgr.get_equipment_list(experiment)
# Returns: [Equipment(name="Beaker", ...), ...]

# Find alternatives for specific equipment
alts = equip_mgr.suggest_alternatives("beaker")
# Returns: ["Mason jar", "Pyrex measuring cup"]

# Estimate total cost
total = equip_mgr.estimate_cost(equipment_list)
# Returns: 25.50  (USD)
```

#### Equipment Database (Sample)

| Equipment | Description | Alternatives | Est. Cost |
|-----------|-------------|-------------|-----------|
| Beaker | Glass container for mixing | Mason jar, measuring cup | $5.00 |
| Test Tube | Small glass tube for reactions | Shot glass, small vial | $2.00 |
| Bunsen Burner | Gas burner for heating | Candle, alcohol lamp | $25.00 |
| Microscope | Magnification device | Magnifying glass, phone macro lens | $50.00 |
| Graduated Cylinder | Precise liquid measurement | Measuring cup with ml markings | $8.00 |
| Petri Dish | Shallow culture dish | Small plate, jar lid | $3.00 |
| Thermometer | Temperature measurement | Digital kitchen thermometer | $5.00 |
| Safety Goggles | Eye protection | Swimming goggles | $8.00 |
| Funnel | Pour liquids into containers | Cut plastic bottle top | $2.00 |
| Pipette | Precise liquid transfer | Eye dropper, straw | $1.00 |

#### Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `get_equipment_list()` | `experiment: Experiment` | `list[Equipment]` | Equipment needed for experiment |
| `suggest_alternatives()` | `equipment_name: str` | `list[str]` | Household alternatives |
| `estimate_cost()` | `equipment_list: list` | `float` | Total cost estimate (USD) |

### Core Functions

#### `explain_experiment()`

Generate a comprehensive experiment explanation using the local LLM.

```python
from science_explainer.core import explain_experiment

result = explain_experiment(
    experiment="baking soda volcano",
    level="middle school",
    detail="detailed"
)
# Returns: dict with all experiment data
```

#### `suggest_alternatives()`

Get AI-powered alternative experiment suggestions.

```python
from science_explainer.core import suggest_alternatives

alts = suggest_alternatives(
    experiment="baking soda volcano",
    level="middle school"
)
# Returns: list[dict] — alternative experiments
```

#### `search_experiments()`

Search for experiments by topic, subject, or difficulty.

```python
from science_explainer.core import search_experiments

results = search_experiments(
    topic="chemical reactions",
    subject="Chemistry",
    difficulty="Intermediate"
)
# Returns: list[dict] — matching experiments
```

#### `validate_experiment_data()`

Validate experiment data structure for completeness and correctness.

```python
from science_explainer.core import validate_experiment_data

errors = validate_experiment_data(data)
# Returns: list[str] — validation errors (empty if valid)
```

#### `export_experiment()`

Export experiment data to different formats.

```python
from science_explainer.core import export_experiment

# Export to Markdown
md_output = export_experiment(data, fmt="markdown")

# Export to printable checklist
checklist = export_experiment(data, fmt="checklist")

# Export to formatted JSON
json_output = export_experiment(data, fmt="json")
```

| Format | Description | Use Case |
|--------|-------------|----------|
| `json` | Machine-readable JSON | Re-importing, API integration |
| `markdown` | Formatted Markdown document | Documentation, sharing |
| `checklist` | Printable checklist with `[ ]` checkboxes | Lab prep, student handouts |

### `ConfigManager` — Configuration

```python
from science_explainer.core import ConfigManager

config = ConfigManager(config_path="config.yaml")

# Get a specific setting
model = config.get("llm", "model", default="gemma3")

# Access raw config dict
raw = config.raw
```

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | `config_path: str` | — | Load config from YAML file |
| `get()` | `section, key, default` | `Any` | Get a config value with fallback |
| `raw` | — | `dict` | Raw configuration dictionary |

<br/>

---

<br/>

## ⚙️ Configuration

### `config.yaml`

```yaml
llm:
  temperature: 0.5
  max_tokens: 4096

experiment:
  default_level: "middle school"
  default_detail: "medium"
  subjects:
    - Chemistry
    - Physics
    - Biology
    - Earth Science
    - Environmental Science
  grade_levels:
    - elementary
    - middle school
    - high school
    - college

safety:
  require_adult_supervision_below: "high school"
  risk_levels:
    low: "green"
    medium: "yellow"
    high: "orange"
    critical: "red"
  mandatory_ppe:
    - safety goggles
    - lab coat

equipment:
  show_cost_estimates: true
  currency: "USD"
  suggest_alternatives: true

storage:
  experiments_dir: "./experiments"
  favorites_file: "favorites.json"

logging:
  level: "INFO"
  file: "science_explainer.log"
```

### Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `gemma3` | Model to use for inference |
| `LOG_LEVEL` | `INFO` | Logging verbosity (DEBUG, INFO, WARNING, ERROR) |
| `EXPERIMENTS_DIR` | `./experiments` | Directory for saved experiments |

<br/>

---

<br/>

## 🧪 Testing

### Run Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ -v --cov=src/science_explainer --cov-report=term-missing

# Run specific test files
pytest tests/test_core.py -v      # Core logic tests
pytest tests/test_cli.py -v       # CLI integration tests

# Using Makefile
make test
```

### Test Coverage

| Module | Test File | What's Tested |
|--------|-----------|---------------|
| `core.py` | `test_core.py` | Experiment parsing, SafetyDatabase lookups, EquipmentManager, data validation, export formats |
| `cli.py` | `test_cli.py` | All 6 CLI commands, option handling, file output, error cases |

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements.txt
pip install pytest pytest-cov ruff

# Or via Makefile
make dev

# Lint code
ruff check src/ tests/

# Format code
ruff format src/ tests/
```

<br/>

---

<br/>

## 🏠 Local LLM vs Cloud AI

This project is designed to run **100% locally** using Ollama. Here's why that matters:

| Aspect | Local LLM (This Project) | Cloud AI (GPT-4, Claude, etc.) |
|--------|--------------------------|-------------------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after setup | ❌ Pay-per-token pricing |
| **Speed** | ⚡ No network latency | 🌐 Depends on internet speed |
| **Availability** | ✅ Works offline | ❌ Requires internet connection |
| **Customization** | ✅ Choose any Ollama model | ⚠️ Limited to provider's models |
| **Safety Data** | ✅ Built-in database, no hallucination | ⚠️ LLM may hallucinate safety info |
| **Rate Limits** | ✅ None | ❌ API rate limits apply |
| **Data Retention** | ✅ You control storage | ⚠️ Provider may retain data |
| **Setup** | ⚠️ Requires Ollama installation | ✅ Just an API key |
| **Hardware** | ⚠️ Needs decent GPU/CPU | ✅ Runs on provider's infrastructure |

> **Recommended models:** Gemma 3 (default), Llama 3, Mistral, or any Ollama-compatible model.

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What models work with this project?</strong></summary>

<br/>

Any model supported by [Ollama](https://ollama.ai/) works with Science Experiment Explainer.
The default and recommended model is **Gemma 3**, but you can use any model:

```bash
# Pull a model
ollama pull gemma3    # Recommended
ollama pull llama3    # Alternative
ollama pull mistral   # Alternative

# Set via environment variable
export OLLAMA_MODEL=gemma3
```

Configure the model in `.env` or set the `OLLAMA_MODEL` environment variable.

</details>

<details>
<summary><strong>Is the safety database reliable for actual lab work?</strong></summary>

<br/>

The built-in `SafetyDatabase` contains **curated, human-reviewed** safety profiles for 10+
common lab chemicals. It includes:
- Risk levels (Low → Critical)
- Required PPE for each material
- Grade-level restrictions
- Precautions and handling notes

**However**, this database is designed as an **educational aid**, not a replacement for
official Material Safety Data Sheets (MSDS). Always consult MSDS for professional lab work
and follow your institution's safety protocols.

</details>

<details>
<summary><strong>Can I add custom experiments to the database?</strong></summary>

<br/>

Yes! You can:
1. **Generate** an experiment with the `explain` command and save it with `-o experiment.json`
2. **Edit** the JSON file to customize any field
3. **Export** to Markdown or checklist format with the `export` command
4. **Validate** your custom data with `validate_experiment_data()`

```bash
# Generate and save
science-explainer explain -e "my custom experiment" -o custom.json

# Export to readable format
science-explainer export -i custom.json -f markdown -o custom.md
```

</details>

<details>
<summary><strong>How do I use this in a classroom setting?</strong></summary>

<br/>

Science Experiment Explainer is ideal for classroom use:

1. **Set grade level** to match your students: `-l "middle school"`
2. **Check safety** before any experiment: `science-explainer safety -e "material"`
3. **Generate checklists** for students: `science-explainer export -f checklist -o handout.txt`
4. **Use the Web UI** for interactive exploration: `make run-web`

The system automatically:
- Restricts dangerous materials for younger grade levels
- Adds adult supervision warnings where needed
- Provides household alternatives for budget-constrained schools
- Generates printable checklists for lab prep

</details>

<details>
<summary><strong>What if Ollama is not running or the model isn't available?</strong></summary>

<br/>

If Ollama is not running or the specified model isn't pulled, you'll see a clear error message.
The safety database and equipment manager work **independently of the LLM**, so you can still:

```bash
# These work without Ollama
science-explainer safety -e "hydrogen peroxide"
science-explainer equipment -e "beaker"
```

To fix LLM-dependent features:
```bash
# Start Ollama
ollama serve

# Pull the model
ollama pull gemma3

# Verify it's running
curl http://localhost:11434/api/tags
```

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/science-experiment-explainer.git
cd science-experiment-explainer

# 2. Install dev dependencies
make dev

# 3. Run tests to verify setup
make test

# 4. Make your changes and run tests again
pytest tests/ -v --cov=src/science_explainer
```

### Contribution Ideas

| Area | Ideas |
|------|-------|
| 🧪 **Safety Data** | Add more chemicals to `SafetyDatabase.BUILT_IN` |
| 🔧 **Equipment** | Expand `EquipmentManager.EQUIPMENT_DB` with more items |
| 🌐 **Web UI** | Add new Streamlit tabs, improve visualizations |
| 📝 **Tests** | Increase test coverage, add edge case tests |
| 📖 **Documentation** | Improve API docs, add tutorials |
| 🌍 **i18n** | Add multi-language support for experiment explanations |

### Guidelines

1. Follow existing code style (enforced by `ruff`)
2. Add tests for new features
3. Update documentation for API changes
4. Keep safety data accurate and well-sourced

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">

  <br/>

  **🔬 Science Experiment Explainer**

  <em>Making science experiments safe, accessible, and fun — powered by local AI.</em>

  <br/>

  Built with ❤️ as part of [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects)

  <br/>

  <a href="https://github.com/kennedyraju55/science-experiment-explainer">⭐ Star this repo</a> •
  <a href="https://github.com/kennedyraju55/science-experiment-explainer/issues">🐛 Report Bug</a> •
  <a href="https://github.com/kennedyraju55/science-experiment-explainer/issues">💡 Request Feature</a>

  <br/><br/>

  <sub>Made with Python, Ollama, and a passion for science education</sub>

</div>
