<div align="center">

<!-- Hero Banner -->
<img src="assets/banner.png" alt="Meal Planner Bot Banner" width="800"/>

# 🍽️ Meal Planner Bot

**AI-powered meal planning, recipe generation, and smart shopping lists — all running locally.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-2ec4b6?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-2ec4b6?style=for-the-badge)]()

<p>
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-web-ui">Web UI</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-contributing">Contributing</a>
</p>

---

*Generate personalized 7–14 day meal plans for 10 dietary preferences, get detailed recipes with full nutrition breakdowns, and create consolidated shopping lists — all powered by a local LLM running on your own hardware.*

</div>

---

## 🤔 Why This Project?

Meal planning is one of those tasks that sounds simple but quickly becomes overwhelming. This project was built to solve real, everyday friction points:

| # | Challenge | How It Feels | How Meal Planner Bot Solves It |
|---|-----------|--------------|-------------------------------|
| 1 | **Decision Fatigue** | Staring at the fridge every evening wondering "what should I cook?" | Generates a complete 7–14 day plan in seconds with a single command |
| 2 | **Dietary Restrictions** | Manually filtering recipes that match your keto / vegan / allergy needs | Supports 10 built-in diet types and comma-separated allergy exclusions |
| 3 | **Nutritional Guesswork** | No idea if you're hitting your calorie or macro targets | Every plan respects your daily calorie target; recipes include full nutrition info |
| 4 | **Grocery Store Chaos** | Buying duplicates, forgetting ingredients, multiple store trips | Auto-generates a consolidated, deduplicated shopping list from your meal plan |
| 5 | **Recipe Boredom** | Rotating the same 5 meals every week | LLM-powered creativity produces varied, interesting meals tailored to your preferences |

> **Bottom line:** You tell the bot your diet, your allergies, and your calorie goal. It gives you a full week of meals, any recipe on demand, and a shopping list you can take straight to the store.

---

## ✨ Features

<div align="center">

```svg
<svg width="720" height="100" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="160" height="80" rx="12" fill="#2ec4b6" opacity="0.15" stroke="#2ec4b6" stroke-width="2"/>
  <text x="90" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#2ec4b6">🥗</text>
  <text x="90" y="65" text-anchor="middle" font-size="11" fill="#333">Diet Flexibility</text>

  <rect x="190" y="10" width="160" height="80" rx="12" fill="#2ec4b6" opacity="0.15" stroke="#2ec4b6" stroke-width="2"/>
  <text x="270" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#2ec4b6">📅</text>
  <text x="270" y="65" text-anchor="middle" font-size="11" fill="#333">Meal Planning</text>

  <rect x="370" y="10" width="160" height="80" rx="12" fill="#2ec4b6" opacity="0.15" stroke="#2ec4b6" stroke-width="2"/>
  <text x="450" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#2ec4b6">📖</text>
  <text x="450" y="65" text-anchor="middle" font-size="11" fill="#333">Recipe Library</text>

  <rect x="550" y="10" width="160" height="80" rx="12" fill="#2ec4b6" opacity="0.15" stroke="#2ec4b6" stroke-width="2"/>
  <text x="630" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="#2ec4b6">🛒</text>
  <text x="630" y="65" text-anchor="middle" font-size="11" fill="#333">Shopping Intelligence</text>
</svg>
```

</div>

| Feature | Description | Highlights |
|---------|-------------|------------|
| **🥗 Diet Flexibility** | Supports 10 distinct dietary preferences out of the box | Omnivore, vegetarian, vegan, keto, paleo, mediterranean, gluten-free, dairy-free, pescatarian, low-carb |
| **📅 Meal Planning** | Generate complete meal plans spanning 1 to 14 days | Breakfast, lunch, dinner, and snacks with calorie-aware portioning |
| **📖 Recipe Library** | Get detailed recipes for any meal in your plan — or search by name | Full ingredients, step-by-step instructions, nutritional breakdown, and save-to-file |
| **🛒 Shopping Intelligence** | Auto-generate a consolidated shopping list from your entire meal plan | Deduplicates ingredients, groups by category, and saves to JSON for easy reference |

### Additional Capabilities

- 🔒 **100% Local & Private** — runs entirely on your machine via Ollama; no data leaves your network
- ⚡ **Dual Interface** — full-featured CLI for terminal power users, plus a Streamlit web UI for visual interaction
- 💾 **Persistent Storage** — save favorite recipes to `saved_recipes.json` and shopping lists to `shopping_list.json`
- 🎛️ **Fine-Tuned Control** — adjust LLM temperature, max tokens, calorie targets, and default preferences via `config.yaml`
- 🧪 **Testable & Modular** — clean separation of concerns makes it easy to extend, test, and contribute

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM backend |
| gemma4 model | — | Default language model |

### 1. Clone the Repository

```bash
git clone https://github.com/kennedyraju55/meal-planner-bot.git
cd meal-planner-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull the LLM Model

```bash
ollama pull gemma4
```

### 5. Run Your First Meal Plan

```bash
python main.py --diet vegan --days 7
```

You should see a complete 7-day vegan meal plan printed to your terminal, with breakfast, lunch, dinner, and snacks for each day.

### 6. (Optional) Launch the Web UI

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

---

## 💻 CLI Reference

### Usage

```
python main.py [OPTIONS]
```

### Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--diet` | `string` | `omnivore` | Dietary preference. One of: `omnivore`, `vegetarian`, `vegan`, `keto`, `paleo`, `mediterranean`, `gluten-free`, `dairy-free`, `pescatarian`, `low-carb` |
| `--days` | `integer` | `7` | Number of days to plan (1–14) |
| `--allergies` | `string` | `""` | Comma-separated list of allergens to exclude (e.g., `nuts,shellfish,soy`) |
| `--calories` | `integer` | `2000` | Daily calorie target |

### Examples

**Generate a 7-day vegan plan:**

```bash
python main.py --diet vegan --days 7
```

**Generate a 14-day keto plan with a 1800-calorie target, excluding nuts and dairy:**

```bash
python main.py --diet keto --days 14 --allergies nuts,dairy --calories 1800
```

**Generate a 3-day mediterranean plan:**

```bash
python main.py --diet mediterranean --days 3
```

**Generate a gluten-free plan with shellfish allergy:**

```bash
python main.py --diet gluten-free --days 7 --allergies shellfish
```

### Interactive Mode

After generating a meal plan, you enter an interactive prompt where you can explore recipes, generate shopping lists, and save your favorites.

| Command | Description |
|---------|-------------|
| *Type a meal name* | Get the full recipe and nutrition details for that meal (calls `get_recipe_details()`) |
| `shop` | Generate a consolidated shopping list from the current meal plan |
| `save` | Save the last retrieved recipe to `saved_recipes.json` |
| `quit` | Exit the interactive session |

**Interactive session example:**

```
🍽️  Your 7-day vegan meal plan has been generated!

Enter a meal name, 'shop', 'save', or 'quit':
> Chickpea Buddha Bowl

📖 Recipe: Chickpea Buddha Bowl
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ingredients:
  - 1 can chickpeas, drained and rinsed
  - 1 cup quinoa
  - 1 avocado, sliced
  - 1 cup roasted sweet potato cubes
  - 2 cups mixed greens
  - Tahini dressing

Instructions:
  1. Cook quinoa according to package directions
  2. Roast sweet potato at 400°F for 25 minutes
  3. Assemble bowl with greens, quinoa, chickpeas, sweet potato
  4. Top with avocado and drizzle with tahini dressing

Nutrition (per serving):
  Calories: 520 | Protein: 18g | Carbs: 62g | Fat: 22g | Fiber: 14g

> save
✅ Recipe saved to saved_recipes.json

> shop
🛒 Shopping list generated and saved to shopping_list.json

> quit
👋 Goodbye!
```

---

## 🌐 Web UI

The Meal Planner Bot includes a full-featured Streamlit web interface with three dedicated tabs.

### Launch

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` by default.

### Tab Overview

| Tab | Purpose | Controls |
|-----|---------|----------|
| **📅 Meal Plan** | Generate personalized meal plans | Diet selector dropdown, days slider (1–14), allergies text input, calories number input, "Generate" button |
| **🛒 Shopping List** | Create a shopping list from the current plan | "Generate Shopping List" button; displays grouped, deduplicated ingredients; option to download as JSON |
| **📖 Recipe Lookup** | Search for detailed recipes by meal name | Text input for meal name, diet selector for context, "Get Recipe" button; displays full recipe with nutrition |

### Tab Details

#### 📅 Meal Plan Tab

1. Select your dietary preference from the dropdown (10 options)
2. Adjust the number of days with the slider (1–14)
3. Enter any allergies as a comma-separated list
4. Set your daily calorie target
5. Click **Generate** to create your personalized meal plan
6. Results display as a structured day-by-day breakdown

#### 🛒 Shopping List Tab

1. Generate a meal plan first (or load an existing one)
2. Click **Generate Shopping List** to produce a consolidated ingredient list
3. Ingredients are deduplicated and grouped by category
4. Download the list as `shopping_list.json` for offline use

#### 📖 Recipe Lookup Tab

1. Enter any meal name (e.g., "Grilled Salmon with Asparagus")
2. Optionally select a diet type for context-appropriate suggestions
3. Click **Get Recipe** to retrieve the full recipe
4. View ingredients, step-by-step instructions, and nutritional information
5. Save recipes to your local collection

---

## 🏗️ Architecture

### System Flow

```svg
<svg width="700" height="220" xmlns="http://www.w3.org/2000/svg">
  <!-- User -->
  <rect x="10" y="80" width="100" height="50" rx="10" fill="#2ec4b6" opacity="0.2" stroke="#2ec4b6" stroke-width="2"/>
  <text x="60" y="110" text-anchor="middle" font-size="12" fill="#333">👤 User</text>

  <!-- Arrow -->
  <line x1="110" y1="105" x2="170" y2="105" stroke="#2ec4b6" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- CLI / Web UI -->
  <rect x="170" y="60" width="120" height="90" rx="10" fill="#2ec4b6" opacity="0.2" stroke="#2ec4b6" stroke-width="2"/>
  <text x="230" y="95" text-anchor="middle" font-size="11" fill="#333">CLI / Web UI</text>
  <text x="230" y="115" text-anchor="middle" font-size="10" fill="#666">main.py / app.py</text>

  <!-- Arrow -->
  <line x1="290" y1="105" x2="350" y2="105" stroke="#2ec4b6" stroke-width="2"/>

  <!-- Core Engine -->
  <rect x="350" y="50" width="140" height="110" rx="10" fill="#2ec4b6" opacity="0.3" stroke="#2ec4b6" stroke-width="2"/>
  <text x="420" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#333">Core Engine</text>
  <text x="420" y="105" text-anchor="middle" font-size="9" fill="#666">generate_meal_plan()</text>
  <text x="420" y="120" text-anchor="middle" font-size="9" fill="#666">get_recipe_details()</text>
  <text x="420" y="135" text-anchor="middle" font-size="9" fill="#666">generate_shopping_list()</text>

  <!-- Arrow -->
  <line x1="490" y1="105" x2="550" y2="105" stroke="#2ec4b6" stroke-width="2"/>

  <!-- Ollama -->
  <rect x="550" y="80" width="120" height="50" rx="10" fill="#333" opacity="0.1" stroke="#333" stroke-width="2"/>
  <text x="610" y="100" text-anchor="middle" font-size="11" fill="#333">🤖 Ollama</text>
  <text x="610" y="116" text-anchor="middle" font-size="10" fill="#666">gemma4</text>

  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#2ec4b6"/>
    </marker>
  </defs>
</svg>
```

### Data Flow

```
User Input (diet, days, allergies, calories)
        │
        ▼
┌─────────────────────────┐
│   CLI (main.py) or      │
│   Web UI (app.py)       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  meal_planner_bot/      │
│  ├─ generate_meal_plan()│──────► Ollama API (gemma4)
│  ├─ get_recipe_details()│◄────── LLM Response
│  ├─ generate_shopping_  │
│  │  list()              │
│  └─ save_recipe()       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│  Output & Storage       │
│  ├─ Terminal / Web UI   │
│  ├─ saved_recipes.json  │
│  └─ shopping_list.json  │
└─────────────────────────┘
```

### Project Structure

```
03-meal-planner-bot/
├── main.py                      # CLI entry point
├── app.py                       # Streamlit web UI
├── config.yaml                  # Application configuration
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── src/
│   └── meal_planner_bot/        # Core package
│       ├── __init__.py
│       ├── planner.py           # generate_meal_plan(), get_recipe_details()
│       ├── shopping.py          # generate_shopping_list()
│       └── utils.py             # save_recipe(), parse_calories_from_plan(),
│                                # generate_shopping_list_prompt()
│
├── tests/                       # Test suite
│   ├── test_planner.py
│   ├── test_shopping.py
│   └── test_utils.py
│
├── assets/                      # Images and static files
│   └── banner.png
│
├── saved_recipes.json           # Persisted recipes (generated at runtime)
└── shopping_list.json           # Persisted shopping lists (generated at runtime)
```

---

## 📚 API Reference

### `generate_meal_plan(diet, days, allergies, calories, model, temperature)`

Generates a structured meal plan for the specified number of days.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `diet` | `str` | `"omnivore"` | Dietary preference (one of the 10 supported diets) |
| `days` | `int` | `7` | Number of days to plan (1–14) |
| `allergies` | `str` | `""` | Comma-separated allergens to exclude |
| `calories` | `int` | `2000` | Daily calorie target |
| `model` | `str` | `"gemma4"` | Ollama model to use for generation |
| `temperature` | `float` | `0.7` | LLM temperature (0.0–1.0); higher = more creative |

**Returns:** `str` — A formatted multi-day meal plan with breakfast, lunch, dinner, and snacks.

**Example:**

```python
from src.meal_planner_bot.planner import generate_meal_plan

plan = generate_meal_plan(
    diet="vegan",
    days=7,
    allergies="nuts,soy",
    calories=1800,
    model="gemma4",
    temperature=0.7
)
print(plan)
```

---

### `get_recipe_details(meal_name, diet)`

Retrieves a detailed recipe for a specific meal, including ingredients, instructions, and nutritional information.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `meal_name` | `str` | — | Name of the meal to look up (e.g., `"Chickpea Buddha Bowl"`) |
| `diet` | `str` | `"omnivore"` | Dietary context for appropriate ingredient substitutions |

**Returns:** `str` — Full recipe with ingredients, step-by-step instructions, and nutrition facts.

**Example:**

```python
from src.meal_planner_bot.planner import get_recipe_details

recipe = get_recipe_details(
    meal_name="Mediterranean Quinoa Salad",
    diet="mediterranean"
)
print(recipe)
```

---

### `generate_shopping_list(meal_plan)`

Generates a consolidated, deduplicated shopping list from an existing meal plan.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `meal_plan` | `str` | — | The full text of a generated meal plan |

**Returns:** `str` — A categorized shopping list with quantities.

**Example:**

```python
from src.meal_planner_bot.shopping import generate_shopping_list

plan = generate_meal_plan(diet="keto", days=7, allergies="", calories=2000,
                          model="gemma4", temperature=0.7)

shopping_list = generate_shopping_list(meal_plan=plan)
print(shopping_list)
```

---

### `save_recipe(recipe, filename)`

Persists a recipe to a local JSON file for future reference.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `recipe` | `str` | — | The recipe text to save |
| `filename` | `str` | `"saved_recipes.json"` | Output file path |

**Returns:** `None` — Writes to disk and prints a confirmation message.

**Example:**

```python
from src.meal_planner_bot.utils import save_recipe

recipe = get_recipe_details("Grilled Salmon with Asparagus", diet="pescatarian")
save_recipe(recipe, filename="saved_recipes.json")
```

---

### Utility Functions

#### `parse_calories_from_plan(plan_text)`

Extracts calorie information from a generated meal plan for validation and analysis.

```python
from src.meal_planner_bot.utils import parse_calories_from_plan

calories = parse_calories_from_plan(plan_text)
print(f"Average daily calories: {calories}")
```

#### `generate_shopping_list_prompt(meal_plan)`

Constructs the LLM prompt used internally by `generate_shopping_list()`. Useful for debugging or customizing the prompt template.

```python
from src.meal_planner_bot.utils import generate_shopping_list_prompt

prompt = generate_shopping_list_prompt(meal_plan)
print(prompt)
```

---

## ⚙️ Configuration

All settings are managed via `config.yaml` in the project root.

### Full Configuration File

```yaml
# config.yaml — Meal Planner Bot Configuration

# LLM Settings
model: gemma4
temperature: 0.7
max_tokens: 4096

# Meal Plan Defaults
meal_plan:
  default_days: 7
  default_diet: omnivore

# Storage Paths
storage:
  recipes_file: saved_recipes.json
  shopping_list_file: shopping_list.json
```

### Configuration Reference

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `model` | `string` | `gemma4` | Ollama model name to use for all LLM calls |
| `temperature` | `float` | `0.7` | Controls randomness in LLM output (0.0 = deterministic, 1.0 = maximum creativity) |
| `max_tokens` | `integer` | `4096` | Maximum number of tokens the LLM can generate per response |
| `meal_plan.default_days` | `integer` | `7` | Default number of days when `--days` is not specified |
| `meal_plan.default_diet` | `string` | `omnivore` | Default diet type when `--diet` is not specified |
| `storage.recipes_file` | `string` | `saved_recipes.json` | File path for storing saved recipes |
| `storage.shopping_list_file` | `string` | `shopping_list.json` | File path for storing generated shopping lists |

### Environment Variables

You can override configuration values using environment variables:

| Environment Variable | Overrides | Example |
|---------------------|-----------|---------|
| `OLLAMA_HOST` | Ollama server address | `http://localhost:11434` |
| `MEAL_PLANNER_MODEL` | `model` | `gemma4` |
| `MEAL_PLANNER_TEMPERATURE` | `temperature` | `0.7` |
| `MEAL_PLANNER_MAX_TOKENS` | `max_tokens` | `4096` |
| `MEAL_PLANNER_DEFAULT_DAYS` | `meal_plan.default_days` | `7` |
| `MEAL_PLANNER_DEFAULT_DIET` | `meal_plan.default_diet` | `omnivore` |

**Example:**

```bash
export OLLAMA_HOST=http://192.168.1.100:11434
export MEAL_PLANNER_MODEL=gemma4
python main.py --diet keto --days 7
```

---

## 🥗 Supported Diets

Meal Planner Bot supports **10 dietary preferences** out of the box. Each diet shapes the LLM prompt to ensure all generated meals, recipes, and shopping lists align with the specified dietary guidelines.

| # | Diet | Key Principle | Typical Foods | Avoids |
|---|------|--------------|---------------|--------|
| 1 | **Omnivore** | No restrictions; balanced variety | Meat, fish, dairy, grains, vegetables, fruits | — |
| 2 | **Vegetarian** | No meat or fish | Dairy, eggs, legumes, grains, vegetables, fruits | Meat, poultry, fish, seafood |
| 3 | **Vegan** | No animal products | Legumes, tofu, tempeh, grains, nuts, vegetables, fruits | All animal products including dairy, eggs, honey |
| 4 | **Keto** | Very low carb, high fat | Meat, fish, eggs, cheese, nuts, avocado, low-carb vegetables | Grains, sugar, high-carb fruits, starchy vegetables |
| 5 | **Paleo** | Whole, unprocessed foods | Meat, fish, eggs, vegetables, fruits, nuts, seeds | Grains, legumes, dairy, processed foods, refined sugar |
| 6 | **Mediterranean** | Plant-forward, healthy fats | Olive oil, fish, whole grains, vegetables, fruits, legumes | Processed foods, red meat (limited), refined grains |
| 7 | **Gluten-Free** | No gluten-containing grains | Rice, quinoa, corn, potatoes, meat, fish, vegetables | Wheat, barley, rye, and derivatives |
| 8 | **Dairy-Free** | No dairy products | Meat, fish, plant milks, vegetables, fruits, grains | Milk, cheese, butter, yogurt, cream |
| 9 | **Pescatarian** | Fish and seafood, no other meat | Fish, seafood, dairy, eggs, grains, vegetables, fruits | Meat, poultry |
| 10 | **Low-Carb** | Reduced carbohydrate intake | Meat, fish, eggs, non-starchy vegetables, healthy fats | Bread, pasta, rice, sugar, high-carb foods |

### Using Diets via CLI

```bash
# Each diet is specified with the --diet flag
python main.py --diet vegetarian --days 7
python main.py --diet keto --days 14 --calories 1600
python main.py --diet mediterranean --days 7 --allergies shellfish
python main.py --diet paleo --days 10 --allergies eggs,nuts
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run a specific test file
pytest tests/test_planner.py
pytest tests/test_shopping.py
pytest tests/test_utils.py

# Run with coverage report
pytest --cov=src/meal_planner_bot --cov-report=term-missing
```

### Test Structure

| Test File | Covers | Key Tests |
|-----------|--------|-----------|
| `test_planner.py` | `generate_meal_plan()`, `get_recipe_details()` | Plan generation for all diets, allergy filtering, day range validation |
| `test_shopping.py` | `generate_shopping_list()` | List consolidation, deduplication, category grouping |
| `test_utils.py` | `save_recipe()`, `parse_calories_from_plan()`, `generate_shopping_list_prompt()` | File I/O, calorie parsing accuracy, prompt formatting |

---

## 🤖 Local LLM vs. Cloud AI

This project is designed for **local-first AI** using Ollama. Here's how it compares to cloud-based alternatives:

| Aspect | Local LLM (This Project) | Cloud AI (OpenAI, etc.) |
|--------|--------------------------|------------------------|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to external servers |
| **Cost** | ✅ Free after hardware investment | ❌ Pay-per-token API costs |
| **Speed** | ⚠️ Depends on local hardware (GPU recommended) | ✅ Typically fast with dedicated infrastructure |
| **Internet** | ✅ Works fully offline | ❌ Requires internet connection |
| **Model Control** | ✅ Choose and swap models freely | ⚠️ Limited to provider's available models |
| **Customization** | ✅ Fine-tune, adjust temperature, modify prompts | ⚠️ Limited to API parameters |
| **Setup** | ⚠️ Requires Ollama installation and model download | ✅ Just an API key |
| **Consistency** | ⚠️ Output varies by model and hardware | ✅ More consistent with versioned models |

### Recommended Hardware for Local LLM

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 8 GB | 16 GB+ |
| GPU VRAM | 4 GB | 8 GB+ |
| Storage | 10 GB free | 20 GB+ free |
| CPU | 4 cores | 8+ cores |

---

## ❓ FAQ

<details>
<summary><strong>How accurate are the calorie counts?</strong></summary>

Calorie counts are **LLM-estimated**, not pulled from a verified nutritional database. They provide a reasonable approximation based on typical serving sizes and ingredients. For precise dietary tracking, cross-reference the generated nutrition info with a certified database like USDA FoodData Central. The `parse_calories_from_plan()` utility can help you extract and audit calorie values from generated plans.

</details>

<details>
<summary><strong>How reliable is the allergy filtering?</strong></summary>

The `--allergies` flag injects allergen exclusions directly into the LLM prompt. The model is instructed to avoid all specified allergens in meals, recipes, and shopping lists. However, because this is LLM-generated content and **not** a medically certified system, **always review generated content before consuming if you have severe or life-threatening allergies.** This tool is meant for convenience and planning — it is not a substitute for professional medical or dietary advice.

</details>

<details>
<summary><strong>How do I save and access recipes?</strong></summary>

There are two ways to save recipes:

1. **CLI:** After retrieving a recipe in interactive mode, type `save` to persist it to `saved_recipes.json`.
2. **Programmatically:** Call `save_recipe(recipe_text, filename="saved_recipes.json")` from `src/meal_planner_bot/utils.py`.

Saved recipes are stored as a JSON array. Each entry includes the recipe name, ingredients, instructions, and nutrition info. You can open the file directly or load it in your own scripts:

```python
import json

with open("saved_recipes.json", "r") as f:
    recipes = json.load(f)

for recipe in recipes:
    print(recipe)
```

</details>

<details>
<summary><strong>What format is the shopping list in?</strong></summary>

Shopping lists are generated as human-readable text in the terminal and simultaneously saved to `shopping_list.json`. The JSON format groups ingredients by category (produce, proteins, dairy, grains, pantry staples, etc.) with quantities. You can also use the `generate_shopping_list()` function programmatically:

```python
from src.meal_planner_bot.shopping import generate_shopping_list

shopping_list = generate_shopping_list(meal_plan=plan)
# Automatically saved to shopping_list.json
```

</details>

<details>
<summary><strong>Can I mix multiple diets in a single plan?</strong></summary>

The `--diet` flag accepts a single diet type per plan. However, you can achieve a mixed-diet effect in two ways:

1. **Generate multiple shorter plans** with different diets and combine them manually (e.g., 4 days keto + 3 days mediterranean).
2. **Use the `omnivore` diet** with specific allergies to exclude certain food groups, effectively creating a custom hybrid diet.

Direct multi-diet support within a single `generate_meal_plan()` call is not currently implemented but is on the roadmap.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and set up
git clone https://github.com/kennedyraju55/meal-planner-bot.git
cd meal-planner-bot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run tests to verify setup
pytest -v
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Areas for Contribution

- 🌍 **New diet types** — Add support for additional dietary preferences
- 🧪 **Test coverage** — Expand unit and integration tests
- 🎨 **Web UI improvements** — Enhance the Streamlit interface
- 📖 **Recipe templates** — Improve prompt engineering for better recipe quality
- 🌐 **Internationalization** — Add multi-language support for meal plans
- 🔌 **Model support** — Test and document compatibility with additional Ollama models

### Code Style

- Follow [PEP 8](https://pep8.org/) for Python code
- Use type hints where practical
- Write docstrings for all public functions
- Keep functions focused and modular

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

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

**Built with ❤️ and local AI**

<sub>Powered by <a href="https://ollama.com">Ollama</a> · Interface by <a href="https://streamlit.io">Streamlit</a> · Made for the 90 Local LLM Projects series</sub>

<br/>

<img src="https://img.shields.io/badge/Made_with-Local_AI-2ec4b6?style=flat-square" alt="Made with Local AI"/>

</div>
