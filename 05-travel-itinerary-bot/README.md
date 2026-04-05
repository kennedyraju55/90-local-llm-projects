<div align="center">

<!-- Hero Banner -->
<img src="assets/banner.png" alt="Travel Itinerary Bot Banner" width="100%" />

# ✈️ Travel Itinerary Bot

### AI-Powered Travel Planning with Local LLMs

<p>
  <strong>Generate personalized itineraries, budget breakdowns, and packing lists — all powered by a local Gemma 4 model. No API keys. No cloud fees. Complete privacy.</strong>
</p>

<!-- Badges -->
<p>
  <a href="#quick-start"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+" /></a>
  <a href="#configuration"><img src="https://img.shields.io/badge/LLM-Gemma_4-7209b7?style=for-the-badge&logo=google&logoColor=white" alt="Gemma 4" /></a>
  <a href="#web-ui"><img src="https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" /></a>
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT-green?style=for-the-badge" alt="MIT License" /></a>
  <a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge" alt="PRs Welcome" /></a>
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

<p>
  <a href="#quick-start">Quick Start</a> •
  <a href="#features">Features</a> •
  <a href="#cli-reference">CLI</a> •
  <a href="#web-ui">Web UI</a> •
  <a href="#api-reference">API</a> •
  <a href="#faq">FAQ</a>
</p>

<br />

</div>

---

## 📋 Table of Contents

- [Why This Project?](#why-this-project)
- [Features](#features)
- [Quick Start](#quick-start)
- [CLI Reference](#cli-reference)
- [Web UI](#web-ui)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Budget Tiers](#budget-tiers)
- [Testing](#testing)
- [Local LLM vs Cloud AI](#local-llm-vs-cloud-ai)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## 🤔 Why This Project?

Planning a trip should be exciting, not exhausting. Traditional travel planning is fragmented, time-consuming, and often expensive. This project solves real pain points that every traveler faces.

| # | Challenge | Pain Point | How We Solve It | Result |
|---|-----------|-----------|-----------------|--------|
| 1 | **Itinerary Overload** | Spending hours on blogs, forums, and review sites to piece together a day-by-day plan | `generate_itinerary()` creates complete, structured plans with a single command | Full itinerary in seconds |
| 2 | **Budget Guesswork** | No clear picture of daily costs until you're already overspending on the trip | `generate_budget_breakdown()` produces itemized cost estimates across accommodation, food, transport, and activities | Spend with confidence |
| 3 | **Packing Anxiety** | Forgetting essentials or overpacking because you had no destination-aware checklist | `generate_packing_list()` tailors recommendations to your destination, duration, and planned activities | Pack smart, travel light |
| 4 | **Multi-City Complexity** | Juggling logistics across multiple destinations with different cultures, currencies, and climates | `generate_multi_destination_itinerary()` handles seamless multi-stop trip planning | One command, many cities |
| 5 | **Privacy & Cost** | Cloud AI services charge per query and send your personal travel data to third-party servers | Runs 100% locally on Gemma 4 — no API keys, no subscriptions, no data leaves your machine | Free and private forever |

> **Bottom line:** One tool replaces a dozen tabs. Your travel data stays on your machine. Your wallet stays intact.

---

## ✨ Features

<div align="center">

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 120">
  <defs>
    <linearGradient id="featureGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7209b7;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#b5179e;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="120" rx="16" fill="url(#featureGrad)" />
  <text x="400" y="45" text-anchor="middle" fill="white" font-size="28" font-weight="bold"
        font-family="Segoe UI, sans-serif">✨ Feature Highlights</text>
  <text x="400" y="85" text-anchor="middle" fill="rgba(255,255,255,0.85)" font-size="16"
        font-family="Segoe UI, sans-serif">Four powerful modules working together for the perfect trip</text>
</svg>
```

</div>

<table>
<tr>
<td width="50%" valign="top">

### 🗺️ Itinerary Planning

- **Single & multi-destination** trip generation
- Day-by-day schedules with morning, afternoon, and evening activities
- Interest-based personalization (food, temples, hiking, nightlife, etc.)
- Support for **1–30 day** trips with **1–20 travelers**
- Automatic travel day allocation for multi-city routes
- Local restaurant, attraction, and experience recommendations

</td>
<td width="50%" valign="top">

### 💰 Budget Management

- **Three budget tiers:** budget, moderate, luxury
- Itemized cost breakdowns per category (accommodation, food, transport, activities)
- Per-person and total group cost calculations
- Daily and trip-total spending estimates
- Category-wise percentage allocation with visual charts
- Currency-aware recommendations based on destination

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎒 Packing Intelligence

- Destination-aware packing suggestions
- Activity-specific gear recommendations
- Duration-based quantity calculations
- Climate and season considerations
- Categorized lists: clothing, toiletries, electronics, documents, miscellaneous
- Carry-on vs checked luggage guidance

</td>
<td width="50%" valign="top">

### 📍 Place Discovery

- Detailed information on specific places and attractions
- Historical and cultural context for landmarks
- Practical visitor tips: hours, fees, best times to visit
- Nearby dining and accommodation suggestions
- Transportation options to and from each location
- Insider tips and hidden gems from AI knowledge

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | Latest | Language model |
| Git | Any | Clone repository |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/travel-itinerary-bot.git
cd travel-itinerary-bot

# 2. Create and activate a virtual environment
python -m venv venv

# On macOS/Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure Ollama is running with Gemma 4
ollama pull gemma4
ollama serve
```

### First Run

Generate a multi-destination itinerary with a single command:

```bash
python -m travel_itinerary_bot \
  --destination "Tokyo,Kyoto" \
  --days 5 \
  --budget moderate \
  --interests "food,temples" \
  --travelers 2
```

**Expected output:**

```
╔══════════════════════════════════════════════════╗
║        🌏 Travel Itinerary: Tokyo → Kyoto       ║
║        📅 5 Days | 💰 Moderate | 👥 2 Travelers  ║
╚══════════════════════════════════════════════════╝

📍 Tokyo (Days 1-3)
─────────────────────
Day 1: Arrival & Shibuya
  🌅 Morning   — Arrive at Narita/Haneda, check into hotel
  🌞 Afternoon — Shibuya Crossing, Hachiko Statue, Meiji Shrine
  🌙 Evening   — Ramen dinner in Shinjuku, Golden Gai exploration

Day 2: Temples & Street Food
  🌅 Morning   — Senso-ji Temple, Nakamise Shopping Street
  🌞 Afternoon — Tsukiji Outer Market food tour
  🌙 Evening   — Akihabara electronics district, izakaya dinner

Day 3: Cultural Immersion
  🌅 Morning   — Imperial Palace East Gardens
  🌞 Afternoon — Harajuku & Takeshita Street
  🌙 Evening   — Shinkansen to Kyoto

📍 Kyoto (Days 4-5)
─────────────────────
Day 4: Ancient Kyoto
  ...

✅ Itinerary saved to saved_itineraries.json
```

### Launch the Web UI

```bash
streamlit run app.py
```

The web interface opens at `http://localhost:8501` with four interactive tabs.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/travel-itinerary-bot.git
cd travel-itinerary-bot
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


---

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.travel_planner.api:app --reload --port 8000

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

### Command-Line Options

```
usage: python -m travel_itinerary_bot [OPTIONS]

Options:
  --destination TEXT    Destination city or comma-separated cities for multi-dest
                        Examples: "Paris", "Tokyo,Kyoto,Osaka"
  --days INTEGER       Trip duration in days (1-30, default: 5)
  --budget TEXT         Budget level: budget | moderate | luxury (default: moderate)
  --interests TEXT      Comma-separated interests
                        Examples: "food,temples", "hiking,photography,nightlife"
  --travelers INTEGER  Number of travelers (1-20, default: 1)
  --interactive        Launch interactive mode
  --save               Save itinerary to saved_itineraries.json
  --help               Show this help message and exit
```

### Usage Examples

```bash
# Single destination, solo budget traveler
python -m travel_itinerary_bot --destination "Bangkok" --days 7 --budget budget

# Multi-destination luxury trip for a group
python -m travel_itinerary_bot \
  --destination "Rome,Florence,Venice" \
  --days 10 \
  --budget luxury \
  --interests "art,wine,history" \
  --travelers 4

# Weekend getaway
python -m travel_itinerary_bot --destination "Lisbon" --days 3 --budget moderate \
  --interests "food,architecture"

# Save the generated itinerary
python -m travel_itinerary_bot --destination "Seoul" --days 5 --save
```

### Interactive Mode

Launch interactive mode for an ongoing session:

```bash
python -m travel_itinerary_bot --interactive
```

**Available interactive commands:**

| Command | Description | Example |
|---------|-------------|---------|
| `<place name>` | Get detailed information about a specific place | `Fushimi Inari Shrine` |
| `budget` | Generate a budget breakdown for the current itinerary | `budget` |
| `pack` | Generate a packing list for the current trip | `pack` |
| `quit` | Exit interactive mode | `quit` |

**Interactive session example:**

```
🌍 Travel Itinerary Bot — Interactive Mode
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Enter destination(s): Tokyo,Kyoto
Number of days (1-30): 5
Budget level (budget/moderate/luxury): moderate
Interests (comma-separated): food,temples
Number of travelers: 2

⏳ Generating itinerary...
✅ Itinerary generated!

─────────────────────────────────────────
What would you like to do?
  • Type a place name for details
  • Type 'budget' for cost breakdown
  • Type 'pack' for packing list
  • Type 'quit' to exit
─────────────────────────────────────────

> Senso-ji Temple

📍 Senso-ji Temple — Tokyo's Oldest Temple
  📜 Built in 645 AD, dedicated to Kannon (Goddess of Mercy)
  🕐 Open: 6:00 AM – 5:00 PM (grounds open 24/7)
  💴 Admission: Free
  🚇 Access: Asakusa Station (Ginza Line, Exit 1)
  💡 Tips: Visit early morning to avoid crowds...

> budget

💰 Budget Breakdown (Moderate — 2 Travelers)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🏨 Accommodation:  $750  (30%)
  🍜 Food & Dining:  $500  (20%)
  🚆 Transport:      $400  (16%)
  🎯 Activities:     $350  (14%)
  🛍️ Shopping:       $300  (12%)
  📦 Miscellaneous:  $200  (8%)
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━
  💵 Total:         $2,500
  👤 Per Person:    $1,250

> quit

👋 Safe travels!
```

---

## 🌐 Web UI

The Streamlit-based web interface provides four tabs for a complete travel planning experience.

### Launching the Web UI

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

### Tab 1: 🗺️ Itinerary

The primary tab for generating travel itineraries.

**Controls:**
- **Destination(s):** Text input field — enter a single city or comma-separated cities for multi-destination trips
- **Number of Days:** Slider (1–30)
- **Budget Level:** Dropdown — budget, moderate, luxury
- **Interests:** Multi-select — food, temples, hiking, nightlife, art, shopping, photography, history, nature, adventure
- **Number of Travelers:** Number input (1–20)
- **Generate button:** Triggers `generate_itinerary()` or `generate_multi_destination_itinerary()` based on input

**Output:** A structured, day-by-day itinerary rendered in an expandable card layout with morning, afternoon, and evening sections.

### Tab 2: 💰 Budget

Detailed cost breakdown for any generated itinerary.

**Controls:**
- Inherits trip parameters from the Itinerary tab
- **Generate Budget Breakdown** button triggers `generate_budget_breakdown()`

**Output:**
- Itemized cost table with categories: accommodation, food, transport, activities, shopping, miscellaneous
- Interactive pie chart showing percentage allocation per category
- Per-person and total cost summary
- Daily average spending estimate

### Tab 3: 🎒 Packing List

Smart, destination-aware packing recommendations.

**Controls:**
- Destination and duration fields
- Interest/activity selection
- **Generate Packing List** button triggers `generate_packing_list()`

**Output:**
- Categorized checklist: clothing, toiletries, electronics, documents, miscellaneous
- Activity-specific items highlighted
- Quantity suggestions based on trip duration

### Tab 4: 📍 Place Details

Deep-dive information on specific places and attractions.

**Controls:**
- **Place Name:** Text input
- **Destination:** Text input (for context)
- **Get Details** button triggers `get_place_details()`

**Output:**
- Historical and cultural background
- Visitor information (hours, fees, best times)
- Transportation options
- Nearby recommendations
- Insider tips

---

## 🏗️ Architecture

### System Overview

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400">
  <defs>
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#7209b7" />
      <stop offset="100%" style="stop-color:#b5179e" />
    </linearGradient>
  </defs>

  <!-- Title -->
  <rect x="250" y="10" width="300" height="40" rx="8" fill="url(#headerGrad)" />
  <text x="400" y="36" text-anchor="middle" fill="white" font-size="16" font-weight="bold"
        font-family="Segoe UI, sans-serif">System Architecture</text>

  <!-- User Layer -->
  <rect x="50" y="70" width="150" height="50" rx="8" fill="#f8f9fa" stroke="#7209b7" stroke-width="2" />
  <text x="125" y="100" text-anchor="middle" font-size="13" font-family="Segoe UI, sans-serif">💻 CLI Interface</text>

  <rect x="250" y="70" width="150" height="50" rx="8" fill="#f8f9fa" stroke="#7209b7" stroke-width="2" />
  <text x="325" y="100" text-anchor="middle" font-size="13" font-family="Segoe UI, sans-serif">🌐 Web UI (Streamlit)</text>

  <!-- Core Layer -->
  <rect x="100" y="160" width="350" height="50" rx="8" fill="#7209b7" />
  <text x="275" y="190" text-anchor="middle" fill="white" font-size="14" font-weight="bold"
        font-family="Segoe UI, sans-serif">travel_itinerary_bot (Core Module)</text>

  <!-- Function boxes -->
  <rect x="50" y="240" width="130" height="40" rx="6" fill="#e9d5ff" stroke="#7209b7" />
  <text x="115" y="264" text-anchor="middle" font-size="10" font-family="monospace">generate_itinerary</text>

  <rect x="200" y="240" width="130" height="40" rx="6" fill="#e9d5ff" stroke="#7209b7" />
  <text x="265" y="264" text-anchor="middle" font-size="10" font-family="monospace">budget_breakdown</text>

  <rect x="350" y="240" width="130" height="40" rx="6" fill="#e9d5ff" stroke="#7209b7" />
  <text x="415" y="264" text-anchor="middle" font-size="10" font-family="monospace">packing_list</text>

  <rect x="500" y="240" width="130" height="40" rx="6" fill="#e9d5ff" stroke="#7209b7" />
  <text x="565" y="264" text-anchor="middle" font-size="10" font-family="monospace">place_details</text>

  <!-- LLM Layer -->
  <rect x="200" y="320" width="250" height="50" rx="8" fill="#f8f9fa" stroke="#7209b7" stroke-width="2" />
  <text x="325" y="350" text-anchor="middle" font-size="13" font-family="Segoe UI, sans-serif">🤖 Ollama + Gemma 4</text>
</svg>
```

### Data Flow

```
User Input (CLI / Web UI)
    │
    ▼
┌─────────────────────────────────┐
│   Input Parsing & Validation    │
│   parse_destinations()          │
│   Validate days (1-30)          │
│   Validate travelers (1-20)    │
│   Validate budget tier          │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│   Prompt Engineering            │
│   generate_budget_prompt()      │
│   generate_packing_list_prompt()│
│   Context-aware templating      │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│   LLM Inference (Gemma 4)       │
│   temperature: 0.7              │
│   max_tokens: 4096              │
│   Local inference via Ollama    │
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│   Response Processing           │
│   parse_budget_items()          │
│   Structure & format output     │
│   save_itinerary() → JSON      │
└──────────────┬──────────────────┘
               │
               ▼
    Rendered Output (CLI / Web UI)
```

### Project Structure

```
travel-itinerary-bot/
├── travel_itinerary_bot/
│   ├── __init__.py              # Package initialization
│   ├── __main__.py              # CLI entry point
│   ├── core.py                  # Core generation functions
│   │   ├── generate_itinerary()
│   │   ├── generate_multi_destination_itinerary()
│   │   ├── get_place_details()
│   │   ├── generate_budget_breakdown()
│   │   └── generate_packing_list()
│   ├── utils.py                 # Utility functions
│   │   ├── parse_destinations()
│   │   ├── save_itinerary()
│   │   ├── parse_budget_items()
│   │   ├── generate_budget_prompt()
│   │   └── generate_packing_list_prompt()
│   └── config.py                # Configuration loader
├── app.py                       # Streamlit web UI
├── config.yaml                  # Application configuration
├── saved_itineraries.json       # Persisted itineraries
├── requirements.txt             # Python dependencies
├── tests/
│   ├── test_core.py             # Core function tests
│   ├── test_utils.py            # Utility function tests
│   └── test_config.py           # Configuration tests
├── assets/
│   └── banner.png               # README banner image
├── .env.example                 # Environment variable template
├── .gitignore
├── LICENSE
└── README.md                    # This file
```

---

## 📚 API Reference

### Core Functions

All core functions are located in `travel_itinerary_bot/core.py`.

#### `generate_itinerary()`

Generates a complete day-by-day travel itinerary for a single destination.

```python
from travel_itinerary_bot.core import generate_itinerary

itinerary = generate_itinerary(
    destination="Tokyo",
    days=5,
    budget="moderate",
    interests=["food", "temples", "photography"],
    travelers=2
)

print(itinerary)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `destination` | `str` | Yes | — | Target city or region |
| `days` | `int` | Yes | — | Trip duration (1–30) |
| `budget` | `str` | Yes | — | Budget tier: `"budget"`, `"moderate"`, or `"luxury"` |
| `interests` | `list[str]` | Yes | — | List of traveler interests |
| `travelers` | `int` | Yes | — | Number of travelers (1–20) |

**Returns:** `str` — Formatted itinerary text with day-by-day activities.

---

#### `generate_multi_destination_itinerary()`

Generates a combined itinerary spanning multiple destinations with automatic day allocation.

```python
from travel_itinerary_bot.core import generate_multi_destination_itinerary

itinerary = generate_multi_destination_itinerary(
    destinations=["Tokyo", "Kyoto", "Osaka"],
    days_per_dest=[3, 2, 2],
    budget="moderate",
    interests=["food", "temples"],
    travelers=2
)

print(itinerary)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `destinations` | `list[str]` | Yes | — | List of destination cities |
| `days_per_dest` | `list[int]` | Yes | — | Days to spend at each destination |
| `budget` | `str` | Yes | — | Budget tier: `"budget"`, `"moderate"`, or `"luxury"` |
| `interests` | `list[str]` | Yes | — | List of traveler interests |
| `travelers` | `int` | Yes | — | Number of travelers (1–20) |

**Returns:** `str` — Combined multi-destination itinerary with travel transitions.

---

#### `get_place_details()`

Retrieves detailed information about a specific place or attraction.

```python
from travel_itinerary_bot.core import get_place_details

details = get_place_details(
    place="Fushimi Inari Shrine",
    destination="Kyoto"
)

print(details)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `place` | `str` | Yes | — | Name of the place or attraction |
| `destination` | `str` | Yes | — | City where the place is located (provides context) |

**Returns:** `str` — Detailed place information including history, hours, fees, tips.

---

#### `generate_budget_breakdown()`

Produces an itemized budget breakdown for a trip with category-wise allocation.

```python
from travel_itinerary_bot.core import generate_budget_breakdown

breakdown = generate_budget_breakdown(
    itinerary=itinerary,
    budget="moderate",
    travelers=2
)

print(breakdown)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `itinerary` | `str` | Yes | — | Previously generated itinerary text |
| `budget` | `str` | Yes | — | Budget tier: `"budget"`, `"moderate"`, or `"luxury"` |
| `travelers` | `int` | Yes | — | Number of travelers (1–20) |

**Returns:** `str` — Itemized budget breakdown with per-person and total costs.

---

#### `generate_packing_list()`

Creates a destination-aware packing list tailored to the trip parameters.

```python
from travel_itinerary_bot.core import generate_packing_list

packing = generate_packing_list(
    destination="Tokyo",
    days=5,
    interests=["food", "temples", "hiking"]
)

print(packing)
```

**Parameters:**

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `destination` | `str` | Yes | — | Target destination |
| `days` | `int` | Yes | — | Trip duration (1–30) |
| `interests` | `list[str]` | Yes | — | Planned activities and interests |

**Returns:** `str` — Categorized packing checklist.

---

### Utility Functions

All utility functions are located in `travel_itinerary_bot/utils.py`.

#### `parse_destinations()`

Parses a comma-separated destination string into a clean list.

```python
from travel_itinerary_bot.utils import parse_destinations

destinations = parse_destinations("Tokyo, Kyoto, Osaka")
# Returns: ["Tokyo", "Kyoto", "Osaka"]
```

#### `save_itinerary()`

Persists a generated itinerary to the configured JSON storage file.

```python
from travel_itinerary_bot.utils import save_itinerary

save_itinerary(itinerary_data, filename="saved_itineraries.json")
```

#### `parse_budget_items()`

Extracts structured budget line items from LLM-generated text.

```python
from travel_itinerary_bot.utils import parse_budget_items

items = parse_budget_items(raw_budget_text)
# Returns: [{"category": "Accommodation", "amount": 750, "percentage": 30}, ...]
```

#### `generate_budget_prompt()`

Constructs the LLM prompt for budget breakdown generation.

```python
from travel_itinerary_bot.utils import generate_budget_prompt

prompt = generate_budget_prompt(itinerary, budget="moderate", travelers=2)
```

#### `generate_packing_list_prompt()`

Constructs the LLM prompt for packing list generation.

```python
from travel_itinerary_bot.utils import generate_packing_list_prompt

prompt = generate_packing_list_prompt(destination="Tokyo", days=5, interests=["food", "temples"])
```

---

## ⚙️ Configuration

### config.yaml

The application is configured via `config.yaml` at the project root:

```yaml
# config.yaml — Travel Itinerary Bot Configuration

# LLM Settings
model: gemma4
temperature: 0.7
max_tokens: 4096

# Travel Defaults
travel:
  default_days: 5
  default_budget: moderate

# Storage
storage:
  itineraries_file: saved_itineraries.json
```

### Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | `str` | `gemma4` | Ollama model name to use for inference |
| `temperature` | `float` | `0.7` | LLM creativity level (0.0 = deterministic, 1.0 = creative) |
| `max_tokens` | `int` | `4096` | Maximum tokens in LLM response |
| `travel.default_days` | `int` | `5` | Default trip duration when not specified |
| `travel.default_budget` | `str` | `moderate` | Default budget tier when not specified |
| `storage.itineraries_file` | `str` | `saved_itineraries.json` | File path for saved itineraries |

### Environment Variables

Override configuration values using environment variables:

```bash
# .env or export directly
OLLAMA_HOST=http://localhost:11434     # Ollama server URL
OLLAMA_MODEL=gemma4                    # Override model name
TRAVEL_DEFAULT_DAYS=7                  # Override default days
TRAVEL_DEFAULT_BUDGET=luxury           # Override default budget
ITINERARIES_FILE=my_trips.json         # Override storage file
```

**Precedence order:** Environment variables > config.yaml > built-in defaults

---

## 💵 Budget Tiers

The bot supports three distinct budget tiers, each producing fundamentally different recommendations:

| Aspect | 🎒 Budget | ⚖️ Moderate | 👑 Luxury |
|--------|-----------|-------------|-----------|
| **Accommodation** | Hostels, guesthouses, capsule hotels | 3-star hotels, boutique stays, Airbnb | 5-star hotels, resorts, ryokans |
| **Dining** | Street food, convenience stores, local markets | Mix of casual and mid-range restaurants | Fine dining, omakase, Michelin-starred |
| **Transport** | Public transit, walking, budget buses | Rail passes, occasional taxis, domestic flights | Private transfers, first-class rail, car hire |
| **Activities** | Free attractions, self-guided tours, parks | Guided tours, museum passes, cooking classes | VIP experiences, private guides, exclusive access |
| **Daily Estimate (Solo)** | $50–80/day | $150–250/day | $400–800+/day |
| **Best For** | Backpackers, students, long-term travelers | Couples, families, balanced travelers | Honeymooners, celebrations, business travelers |

### Budget Allocation Formula

The budget breakdown distributes costs across categories with the following approximate ratios:

```
Budget Tier:
  🏨 Accommodation:  25%
  🍜 Food:           30%
  🚆 Transport:      20%
  🎯 Activities:     10%
  📦 Miscellaneous:  15%

Moderate Tier:
  🏨 Accommodation:  30%
  🍜 Food:           25%
  🚆 Transport:      15%
  🎯 Activities:     15%
  📦 Miscellaneous:  15%

Luxury Tier:
  🏨 Accommodation:  35%
  🍜 Food:           20%
  🚆 Transport:      15%
  🎯 Activities:     20%
  📦 Miscellaneous:  10%
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test modules
python -m pytest tests/test_core.py -v
python -m pytest tests/test_utils.py -v
python -m pytest tests/test_config.py -v

# Run with coverage
python -m pytest tests/ --cov=travel_itinerary_bot --cov-report=term-missing
```

### Test Structure

```
tests/
├── test_core.py      # Tests for generate_itinerary, generate_multi_destination_itinerary,
│                      # get_place_details, generate_budget_breakdown, generate_packing_list
├── test_utils.py     # Tests for parse_destinations, save_itinerary, parse_budget_items,
│                      # generate_budget_prompt, generate_packing_list_prompt
└── test_config.py    # Tests for configuration loading, defaults, and overrides
```

### Example Test Cases

```python
# test_utils.py
def test_parse_destinations_single():
    result = parse_destinations("Tokyo")
    assert result == ["Tokyo"]

def test_parse_destinations_multiple():
    result = parse_destinations("Tokyo, Kyoto, Osaka")
    assert result == ["Tokyo", "Kyoto", "Osaka"]

def test_parse_destinations_whitespace():
    result = parse_destinations("  Paris ,  London  ,  Rome  ")
    assert result == ["Paris", "London", "Rome"]
```

---

## 🤖 Local LLM vs Cloud AI

This project is built around **local LLM inference**. Here's why and how it compares:

| Dimension | 🏠 Local LLM (This Project) | ☁️ Cloud AI (GPT-4, Claude, etc.) |
|-----------|------------------------------|-----------------------------------|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after hardware investment | ❌ Pay-per-token, costs accumulate |
| **Speed** | ⚡ Depends on local GPU/CPU | ⚡ Generally fast, but network-dependent |
| **Quality** | 🟡 Good for structured tasks | ✅ Superior for nuanced, creative output |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Setup** | 🟡 Requires Ollama + model download | ✅ Just an API key |
| **Customization** | ✅ Full control over model, prompts, temperature | 🟡 Limited to API parameters |
| **Rate Limits** | ✅ None — run as many queries as you want | ❌ Subject to API rate limits |

### Switching Models

To use a different Ollama model, update `config.yaml`:

```yaml
# Try different models
model: gemma4          # Default — good balance of speed and quality
# model: llama3.1      # Alternative — strong general performance
# model: mistral       # Alternative — fast and efficient
# model: codellama     # Not recommended — optimized for code, not travel
```

Then pull the model:

```bash
ollama pull <model-name>
```

---

## ❓ FAQ

<details>
<summary><strong>1. Does the bot provide real-time prices for flights, hotels, and activities?</strong></summary>

No. The Travel Itinerary Bot generates **estimated costs** based on the LLM's training data, not real-time pricing feeds. The budget breakdowns reflect typical price ranges for each destination and budget tier, but actual costs may vary based on season, availability, and current exchange rates. For booking and real-time pricing, use the itinerary as a planning guide and cross-reference with booking platforms like Google Flights, Booking.com, or Agoda.

</details>

<details>
<summary><strong>2. Is there a limit on the number of destinations in a multi-destination trip?</strong></summary>

There is no hard-coded limit on the number of destinations, but practical constraints apply. The `max_tokens: 4096` setting means very long itineraries may be truncated. For best results:
- **2–4 destinations** works great with detailed day-by-day plans.
- **5–7 destinations** is feasible but produces less detail per city.
- **8+ destinations** may hit token limits — consider splitting into separate itinerary runs or increasing `max_tokens` in `config.yaml`.

Each destination in the comma-separated `--destination` flag is parsed by `parse_destinations()` and passed to `generate_multi_destination_itinerary()`.

</details>

<details>
<summary><strong>3. What types of interests can I specify?</strong></summary>

Interests are free-text and not limited to a predefined list. The LLM interprets them contextually. Common examples include:

- **Culture:** `temples`, `museums`, `history`, `architecture`, `art`
- **Food:** `food`, `street food`, `fine dining`, `cooking classes`, `wine`
- **Nature:** `hiking`, `beaches`, `parks`, `wildlife`, `mountains`
- **Adventure:** `scuba diving`, `rock climbing`, `skiing`, `surfing`
- **Lifestyle:** `shopping`, `nightlife`, `photography`, `wellness`, `yoga`
- **Family:** `kid-friendly`, `theme parks`, `family activities`

You can combine any interests: `--interests "food,temples,photography,nightlife"`. The more specific your interests, the more tailored the itinerary.

</details>

<details>
<summary><strong>4. How does group travel (multiple travelers) affect the output?</strong></summary>

The `--travelers` parameter (1–20) influences the itinerary and budget in several ways:

- **Budget calculations:** `generate_budget_breakdown()` computes both per-person and total group costs. Shared costs (like accommodation) are split, while individual costs (like meals) are multiplied.
- **Activity recommendations:** The LLM adjusts suggestions — a solo traveler might get hostel recommendations, while a group of 6 gets Airbnb or villa suggestions.
- **Restaurant recommendations:** Group-friendly dining options are prioritized for larger parties.
- **Transport suggestions:** Groups may get private transfer recommendations instead of individual transit passes.

</details>

<details>
<summary><strong>5. Can I use the bot completely offline?</strong></summary>

**Yes!** Once you have Ollama installed and the Gemma 4 model downloaded, the entire application runs offline:

```bash
# One-time setup (requires internet)
ollama pull gemma4

# Everything below works offline
python -m travel_itinerary_bot --destination "Paris" --days 5 --budget moderate
streamlit run app.py
```

No API keys, no cloud services, no internet required for generation. The only exception is the initial model download. Saved itineraries are stored locally in `saved_itineraries.json`.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/<your-username>/travel-itinerary-bot.git
cd travel-itinerary-bot

# Create a feature branch
git checkout -b feature/your-feature-name

# Install dev dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available

# Make your changes
# ...

# Run tests
python -m pytest tests/ -v

# Commit and push
git add .
git commit -m "feat: description of your changes"
git push origin feature/your-feature-name
```

### Contribution Guidelines

1. **Fork** the repository and create a feature branch from `main`.
2. **Write tests** for any new functionality.
3. **Follow existing code style** — consistent naming, docstrings, type hints.
4. **Update documentation** if your changes affect the API, CLI, or configuration.
5. **One feature per PR** — keep pull requests focused and reviewable.

### Areas for Contribution

| Area | Description | Difficulty |
|------|-------------|-----------|
| 🌍 New destinations | Improve prompts for underrepresented regions | Easy |
| 🧪 Test coverage | Add unit tests for edge cases | Easy |
| 🌐 i18n | Add multi-language itinerary generation | Medium |
| 📊 Visualizations | Enhance budget charts and trip timelines in the Web UI | Medium |
| 🗄️ Database storage | Replace JSON storage with SQLite for better querying | Medium |
| 🔌 API endpoints | Add a REST API layer for programmatic access | Hard |
| 🗺️ Map integration | Embed interactive maps in the Web UI | Hard |

---

## 📄 License

This project is licensed under the **MIT License**.

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

**Built with 💜 using local AI — no cloud, no cost, no compromises.**

<sub>Part of the <a href="#">90 Local LLM Projects</a> series — Project #05</sub>

<br />

<a href="#-travel-itinerary-bot">⬆ Back to Top</a>

</div>
