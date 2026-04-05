# Examples for Nutrition Label Analyzer

This directory contains example scripts demonstrating how to use this project.

## Quick Demo

```bash
python examples/demo.py
```

## What the Demo Shows

- **`analyze_food()`** — Analyze nutrition for a single food item.
- **`analyze_label()`** — Analyze nutrition label data from text.
- **`compare_foods()`** — Compare nutrition across multiple food items.
- **`read_file()`** — Read text content from a file.
- **`calculate_daily_values()`** — Calculate percent Daily Value for each nutrient.
- **`DietaryGoal`** — Represents a dietary macro-nutrient goal.
- **`MealTracker`** — Tracks meals and nutrient totals for a day.

## Prerequisites

- Python 3.10+
- Ollama running with Gemma 4 model
- Project dependencies installed (`pip install -e .`)

## Running

From the project root directory:

```bash
# Install the project in development mode
pip install -e .

# Run the demo
python examples/demo.py
```
