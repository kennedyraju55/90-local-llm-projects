<div align="center">

<!-- Hero Banner -->
<img src="assets/banner.png" alt="Gift Recommendation Bot Banner" width="100%" />

<br />

# 🎁 Gift Recommendation Bot

### AI-Powered Gift Ideas — Personalized, Budget-Aware, and Always Thoughtful

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Gemma 4](https://img.shields.io/badge/Gemma_4-Google-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-e63946?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

<br />

<p align="center">
  <strong>Never give a bad gift again.</strong><br />
  Gift Recommendation Bot uses a local LLM to generate personalized gift suggestions<br />
  based on occasion, relationship, budget, interests, and more — all running privately on your machine.
</p>

<br />

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Configuration](#%EF%B8%8F-configuration)

</div>

---

<br />

## 💡 Why This Project?

Gift-giving should be joyful — not stressful. Yet most of us face the same struggles every time an occasion approaches.

| # | Challenge | How Gift Recommendation Bot Solves It |
|:-:|-----------|---------------------------------------|
| 1 | **"I have no idea what to get them."** | Generates 5–7 personalized suggestions using AI, tailored to the recipient's interests, age, and your relationship. |
| 2 | **"I always forget important dates."** | Built-in occasion calendar tracks birthdays, anniversaries, and holidays with upcoming-event alerts. |
| 3 | **"I keep buying duplicate gifts."** | Per-person wishlists with purchase tracking ensure you never repeat a gift or lose a great idea. |
| 4 | **"Is this a good price?"** | Price comparison across retailers helps you find the best deal within your budget range. |
| 5 | **"I don't want my data sent to the cloud."** | Runs entirely on your local machine using Ollama + Gemma 4 — your gift data never leaves your device. |

<br />

---

<br />

## ✨ Features

<div align="center">

<!-- Features Diagram -->
```
┌─────────────────────────────────────────────────────────────────┐
│                    GIFT RECOMMENDATION BOT                      │
│                                                                 │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐  │
│   │   CLI Tool   │  │   Web UI     │  │   Python API         │  │
│   │  5 Commands  │  │  3 Tabs      │  │  8 Core Functions    │  │
│   └──────┬───────┘  └──────┬───────┘  └──────────┬───────────┘  │
│          │                 │                      │              │
│          └─────────────────┼──────────────────────┘              │
│                            │                                    │
│                    ┌───────▼───────┐                             │
│                    │  Gemma 4 LLM  │                             │
│                    │  via Ollama   │                             │
│                    └───────────────┘                             │
└─────────────────────────────────────────────────────────────────┘
```

</div>

<br />

<table>
<tr>
<td width="50%" valign="top">

### 🎯 Smart Recommendations

- Generate **5–7 curated gift ideas** per query
- Filter by **occasion**, **relationship**, **budget**, **interests**, **age**, and **gender**
- Get detailed breakdowns with descriptions, price estimates, and purchase links
- Supports **14 occasions** and **10 relationship types**

</td>
<td width="50%" valign="top">

### 📋 Wishlist Management

- Maintain **per-person wishlists** with gift name, price, occasion, and notes
- **Mark items as purchased** to track what's been bought
- Persistent JSON storage — your lists survive restarts
- Quick add from CLI or Web UI

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 📅 Occasion Calendar

- Track **upcoming occasions** for every person in your life
- Set dates for birthdays, anniversaries, holidays, and custom events
- View upcoming events within a configurable window (default: 30 days)
- Never miss an important date again

</td>
<td width="50%" valign="top">

### 💰 Price Intelligence

- **Compare prices** across multiple retailers for any gift
- See price ranges, availability, and best-deal indicators
- Budget-aware filtering ensures suggestions stay within your range
- Make informed purchasing decisions

</td>
</tr>
</table>

<br />

---

<br />

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | via Ollama | Language model |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/gift-recommendation-bot.git
cd gift-recommendation-bot

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Ensure Ollama is running with Gemma 4
ollama pull gemma4
ollama serve
```

### First Run

```bash
# Generate gift recommendations for a partner's birthday with a $100 budget
python -m gift_recommendation_bot recommend \
  --occasion birthday \
  --relationship partner \
  --budget 100 \
  --interests "cooking,reading"
```

**Expected Output:**

```
🎁 Gift Recommendations for birthday (partner) — Budget: $100

1. Artisan Cookbook Collection
   A curated set of cookbooks from renowned chefs, covering cuisines
   from Italian to Japanese.
   💰 Estimated Price: $45–$65
   🏷️ Why: Perfect for a partner who loves cooking and exploring new recipes.

2. Kindle Paperwhite
   A lightweight e-reader with adjustable warm light, perfect for
   reading anywhere.
   💰 Estimated Price: $80–$100
   🏷️ Why: Ideal for an avid reader who enjoys books across genres.

3. Personalized Recipe Journal
   A beautifully bound journal for recording favorite recipes, with
   sections for notes and photos.
   💰 Estimated Price: $25–$35
   🏷️ Why: Combines both cooking and writing interests in a thoughtful way.

... (5–7 total suggestions)
```

<br />

---

<br />

## 📟 CLI Reference

The Gift Recommendation Bot provides a multi-command CLI interface. All commands are accessible via the `gift_recommendation_bot` module.

```bash
python -m gift_recommendation_bot <command> [options]
```

<br />

### Command 1: `recommend`

Generate personalized gift recommendations using the local LLM.

```bash
python -m gift_recommendation_bot recommend \
  --occasion <OCCASION> \
  --relationship <RELATIONSHIP> \
  --budget <AMOUNT> \
  [--interests <COMMA_SEPARATED>] \
  [--age <AGE>]
```

| Flag | Required | Description |
|------|----------|-------------|
| `--occasion` | ✅ | One of the 14 supported occasions (e.g., `birthday`, `christmas`) |
| `--relationship` | ✅ | One of the 10 supported relationships (e.g., `partner`, `friend`) |
| `--budget` | ✅ | Maximum budget in dollars (numeric) |
| `--interests` | ❌ | Comma-separated list of interests (e.g., `"cooking,reading,hiking"`) |
| `--age` | ❌ | Recipient's age for more targeted suggestions |

**Examples:**

```bash
# Birthday gift for a friend, $50 budget
python -m gift_recommendation_bot recommend \
  --occasion birthday --relationship friend --budget 50

# Christmas gift for a parent who loves gardening, age 60
python -m gift_recommendation_bot recommend \
  --occasion christmas --relationship parent --budget 75 \
  --interests "gardening,tea,puzzles" --age 60

# Wedding gift for a colleague
python -m gift_recommendation_bot recommend \
  --occasion wedding --relationship colleague --budget 150
```

<br />

### Command 2: `wishlist-add`

Add a gift idea to a person's wishlist.

```bash
python -m gift_recommendation_bot wishlist-add \
  --person <NAME> \
  --gift <GIFT_NAME> \
  [--price <AMOUNT>] \
  [--occasion <OCCASION>]
```

| Flag | Required | Description |
|------|----------|-------------|
| `--person` | ✅ | Name of the person the gift is for |
| `--gift` | ✅ | Name or description of the gift |
| `--price` | ❌ | Estimated price in dollars |
| `--occasion` | ❌ | Occasion the gift is intended for |

**Examples:**

```bash
# Add a gift idea for Mom
python -m gift_recommendation_bot wishlist-add \
  --person "Mom" --gift "Silk Scarf" --price 45 --occasion mothers-day

# Quick add without price or occasion
python -m gift_recommendation_bot wishlist-add \
  --person "Alex" --gift "Board Game Collection"
```

<br />

### Command 3: `wishlist-show`

Display the wishlist for a specific person.

```bash
python -m gift_recommendation_bot wishlist-show --person <NAME>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--person` | ✅ | Name of the person whose wishlist to display |

**Example:**

```bash
python -m gift_recommendation_bot wishlist-show --person "Mom"
```

**Expected Output:**

```
📋 Wishlist for Mom

  ID  │ Gift              │ Price  │ Occasion    │ Status
 ─────┼───────────────────┼────────┼─────────────┼──────────
  1   │ Silk Scarf         │ $45    │ mothers-day │ ⬜ Pending
  2   │ Garden Tool Set    │ $35    │ birthday    │ ✅ Purchased
  3   │ Recipe Book        │ $22    │ christmas   │ ⬜ Pending

Total items: 3 | Purchased: 1 | Remaining: 2
```

<br />

### Command 4: `calendar-add`

Add an occasion to the calendar for a specific person.

```bash
python -m gift_recommendation_bot calendar-add \
  --person <NAME> \
  --occasion <OCCASION> \
  --date <YYYY-MM-DD>
```

| Flag | Required | Description |
|------|----------|-------------|
| `--person` | ✅ | Name of the person |
| `--occasion` | ✅ | Type of occasion |
| `--date` | ✅ | Date in `YYYY-MM-DD` format |

**Example:**

```bash
# Add Mom's birthday to the calendar
python -m gift_recommendation_bot calendar-add \
  --person "Mom" --occasion birthday --date 2025-03-15
```

<br />

### Command 5: `calendar-show`

Display upcoming occasions from the calendar.

```bash
python -m gift_recommendation_bot calendar-show [--days <NUMBER>]
```

| Flag | Required | Description |
|------|----------|-------------|
| `--days` | ❌ | Number of days to look ahead (default: `30`) |

**Examples:**

```bash
# Show occasions in the next 30 days (default)
python -m gift_recommendation_bot calendar-show

# Show occasions in the next 90 days
python -m gift_recommendation_bot calendar-show --days 90
```

**Expected Output:**

```
📅 Upcoming Occasions (next 30 days)

  Date        │ Person  │ Occasion     │ Days Away
 ─────────────┼─────────┼──────────────┼───────────
  2025-02-14  │ Sarah   │ valentines   │ 3
  2025-02-20  │ Mom     │ birthday     │ 9
  2025-03-01  │ Alex    │ anniversary  │ 18

3 upcoming occasions found.
```

<br />

---

<br />

## 🌐 Web UI

Launch the Streamlit-based web interface:

```bash
streamlit run gift_recommendation_bot/app.py
```

The Web UI opens at `http://localhost:8501` and provides three tabs:

<br />

### Tab 1: 🎯 Recommendations

The main recommendation engine with a form-based interface.

| Field | Input Type | Options |
|-------|-----------|---------|
| Occasion | Dropdown | All 14 supported occasions |
| Relationship | Dropdown | All 10 supported relationships |
| Budget | Slider | $10 – $1,000 |
| Interests | Text Input | Free-form comma-separated |
| Age | Number Input | Optional |
| Gender | Dropdown | Optional |

**Features:**
- Click **"Generate Recommendations"** to get 5–7 AI-powered gift ideas
- Expand any suggestion to see **detailed information** via `get_gift_details()`
- Click **"Compare Prices"** on any gift to see retailer price comparisons via `compare_prices()`
- One-click **"Add to Wishlist"** to save any recommendation directly

<br />

### Tab 2: 📋 Wishlists

Manage per-person wishlists with full CRUD operations.

| Feature | Description |
|---------|-------------|
| Person Selector | Dropdown of all people with wishlists |
| Gift Table | Sortable table with name, price, occasion, status |
| Add Gift | Form to add new items to any person's wishlist |
| Mark Purchased | Toggle button to mark items as bought |
| Status Indicators | ⬜ Pending / ✅ Purchased visual status |

<br />

### Tab 3: 📅 Calendar

Visual occasion calendar with upcoming event tracking.

| Feature | Description |
|---------|-------------|
| Upcoming Table | Shows all events within configurable day window |
| Add Occasion | Form to add new occasions with date picker |
| Days Filter | Slider to adjust the look-ahead window (1–365 days) |
| Color Coding | Occasions within 7 days highlighted in red |
| Quick Recommend | Button to jump to Recommendations tab pre-filled for an occasion |

<br />

---

<br />

## 🏗️ Architecture

### System Flow

```
┌──────────────────────────────────────────────────────────────────────┐
│                         USER INTERFACE LAYER                         │
│                                                                      │
│    ┌─────────────────┐              ┌─────────────────────────┐      │
│    │   CLI (Click)    │              │   Web UI (Streamlit)    │      │
│    │   5 commands     │              │   3 tabs                │      │
│    └────────┬─────────┘              └────────────┬────────────┘      │
│             │                                     │                  │
│             └──────────────┬──────────────────────┘                  │
└────────────────────────────┼─────────────────────────────────────────┘
                             │
┌────────────────────────────┼─────────────────────────────────────────┐
│                      CORE ENGINE LAYER                               │
│                            │                                         │
│    ┌───────────────────────▼───────────────────────────┐             │
│    │          generate_recommendations()               │             │
│    │  occasion, relationship, budget, interests,       │             │
│    │  age, gender → 5–7 gift ideas                     │             │
│    └───────────────────────┬───────────────────────────┘             │
│                            │                                         │
│    ┌───────────┬───────────┼───────────┬───────────────┐             │
│    │           │           │           │               │             │
│    ▼           ▼           ▼           ▼               ▼             │
│ get_gift    compare    add_to     get_wishlist   add_occasion        │
│ _details()  _prices()  _wishlist()     ()        ()                  │
│                        mark_purchased()  get_upcoming_occasions()    │
│                                                                      │
└────────────────────────────┬─────────────────────────────────────────┘
                             │
┌────────────────────────────┼─────────────────────────────────────────┐
│                       DATA & LLM LAYER                               │
│                            │                                         │
│    ┌───────────┐    ┌──────▼──────┐    ┌───────────────────┐         │
│    │ wishlists │    │   Ollama    │    │ occasion_calendar │         │
│    │   .json   │    │  Gemma 4    │    │      .json        │         │
│    └───────────┘    └─────────────┘    └───────────────────┘         │
│                                                                      │
│    load_wishlists()  save_wishlists()                                 │
│    load_calendar()   save_calendar()                                 │
└──────────────────────────────────────────────────────────────────────┘
```

### Project Structure

```
gift-recommendation-bot/
├── gift_recommendation_bot/
│   ├── __init__.py
│   ├── __main__.py              # CLI entry point
│   ├── core.py                  # Core recommendation engine
│   │   ├── generate_recommendations()
│   │   ├── get_gift_details()
│   │   └── compare_prices()
│   ├── wishlist.py              # Wishlist management
│   │   ├── add_to_wishlist()
│   │   ├── get_wishlist()
│   │   └── mark_purchased()
│   ├── calendar.py              # Occasion calendar
│   │   ├── add_occasion()
│   │   └── get_upcoming_occasions()
│   ├── utils.py                 # Data persistence utilities
│   │   ├── load_wishlists()
│   │   ├── save_wishlists()
│   │   ├── load_calendar()
│   │   └── save_calendar()
│   ├── config.py                # Configuration loader
│   └── app.py                   # Streamlit Web UI
├── config.yaml                  # Application configuration
├── wishlists.json               # Wishlist data (auto-generated)
├── occasion_calendar.json       # Calendar data (auto-generated)
├── requirements.txt
├── tests/
│   ├── test_core.py
│   ├── test_wishlist.py
│   ├── test_calendar.py
│   └── test_utils.py
└── README.md
```

<br />

---

<br />

## 📖 API Reference

All core functions are importable from the `gift_recommendation_bot` package.

```python
from gift_recommendation_bot.core import (
    generate_recommendations,
    get_gift_details,
    compare_prices,
)
from gift_recommendation_bot.wishlist import (
    add_to_wishlist,
    get_wishlist,
    mark_purchased,
)
from gift_recommendation_bot.calendar import (
    add_occasion,
    get_upcoming_occasions,
)
```

<br />

### `generate_recommendations(occasion, relationship, budget, interests, age, gender)`

Generate 5–7 personalized gift recommendations using the local LLM.

```python
recommendations = generate_recommendations(
    occasion="birthday",
    relationship="partner",
    budget=100,
    interests="cooking,reading",
    age=30,
    gender="female"
)

# Returns: list of dicts
# [
#     {
#         "name": "Artisan Cookbook Collection",
#         "description": "A curated set of cookbooks...",
#         "estimated_price": "$45–$65",
#         "reason": "Perfect for a partner who loves cooking..."
#     },
#     ...
# ]
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `occasion` | `str` | ✅ | One of 14 supported occasions |
| `relationship` | `str` | ✅ | One of 10 supported relationships |
| `budget` | `int` | ✅ | Maximum budget in dollars |
| `interests` | `str` | ❌ | Comma-separated interests |
| `age` | `int` | ❌ | Recipient's age |
| `gender` | `str` | ❌ | Recipient's gender |

**Returns:** `list[dict]` — 5–7 gift recommendation objects.

<br />

### `get_gift_details(gift_name, budget)`

Retrieve detailed information about a specific gift, including description, pricing tiers, where to buy, and personalization options.

```python
details = get_gift_details(
    gift_name="Kindle Paperwhite",
    budget=100
)

# Returns: dict
# {
#     "name": "Kindle Paperwhite",
#     "description": "A lightweight e-reader with adjustable warm light...",
#     "price_range": "$80–$140",
#     "where_to_buy": ["Amazon", "Best Buy", "Target"],
#     "personalization": "Add a custom case or gift card",
#     "within_budget": True
# }
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `gift_name` | `str` | ✅ | Name of the gift to look up |
| `budget` | `int` | ✅ | Budget to check against |

**Returns:** `dict` — Detailed gift information.

<br />

### `compare_prices(gift_name)`

Compare prices for a gift across multiple retailers.

```python
prices = compare_prices(gift_name="Kindle Paperwhite")

# Returns: list of dicts
# [
#     {"retailer": "Amazon", "price": 89.99, "in_stock": True, "url": "..."},
#     {"retailer": "Best Buy", "price": 94.99, "in_stock": True, "url": "..."},
#     {"retailer": "Target", "price": 99.99, "in_stock": False, "url": "..."},
# ]
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `gift_name` | `str` | ✅ | Name of the gift to compare |

**Returns:** `list[dict]` — Price comparison across retailers.

<br />

### `add_to_wishlist(person, gift, price, occasion, notes)`

Add a gift item to a specific person's wishlist.

```python
add_to_wishlist(
    person="Mom",
    gift="Silk Scarf",
    price=45.00,
    occasion="mothers-day",
    notes="She mentioned liking the blue one at Nordstrom"
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `person` | `str` | ✅ | Name of the recipient |
| `gift` | `str` | ✅ | Gift name or description |
| `price` | `float` | ❌ | Estimated price |
| `occasion` | `str` | ❌ | Associated occasion |
| `notes` | `str` | ❌ | Additional notes |

**Returns:** `dict` — The created wishlist item with generated ID.

<br />

### `get_wishlist(person)`

Retrieve all wishlist items for a specific person.

```python
wishlist = get_wishlist(person="Mom")

# Returns: list of dicts
# [
#     {
#         "id": 1,
#         "gift": "Silk Scarf",
#         "price": 45.00,
#         "occasion": "mothers-day",
#         "notes": "She mentioned liking the blue one...",
#         "purchased": False
#     },
#     ...
# ]
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `person` | `str` | ✅ | Name of the person |

**Returns:** `list[dict]` — All wishlist items for the person.

<br />

### `mark_purchased(person, item_id)`

Mark a wishlist item as purchased.

```python
mark_purchased(person="Mom", item_id=1)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `person` | `str` | ✅ | Name of the person |
| `item_id` | `int` | ✅ | ID of the wishlist item |

**Returns:** `dict` — Updated wishlist item with `purchased: True`.

<br />

### `add_occasion(person, occasion, date, notes)`

Add an occasion to the calendar for a specific person.

```python
add_occasion(
    person="Mom",
    occasion="birthday",
    date="2025-03-15",
    notes="She's turning 60 — plan something special"
)
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `person` | `str` | ✅ | Name of the person |
| `occasion` | `str` | ✅ | Type of occasion |
| `date` | `str` | ✅ | Date in `YYYY-MM-DD` format |
| `notes` | `str` | ❌ | Additional notes |

**Returns:** `dict` — The created calendar entry.

<br />

### `get_upcoming_occasions(days)`

Get all occasions occurring within the specified number of days.

```python
upcoming = get_upcoming_occasions(days=30)

# Returns: list of dicts
# [
#     {
#         "person": "Sarah",
#         "occasion": "valentines",
#         "date": "2025-02-14",
#         "notes": "",
#         "days_away": 3
#     },
#     ...
# ]
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `days` | `int` | ❌ | Look-ahead window in days (default: `30`) |

**Returns:** `list[dict]` — Upcoming occasions sorted by date.

<br />

---

<br />

## 🎉 Supported Occasions

Gift Recommendation Bot supports **14 occasion types** out of the box:

| # | Occasion | Key | Description | Typical Budget Range |
|:-:|----------|-----|-------------|---------------------|
| 1 | 🎂 Birthday | `birthday` | Annual birthday celebrations | $20 – $200 |
| 2 | 🎄 Christmas | `christmas` | Holiday season gift-giving | $25 – $300 |
| 3 | 💍 Anniversary | `anniversary` | Relationship milestones | $50 – $500 |
| 4 | 💒 Wedding | `wedding` | Marriage celebrations | $75 – $500 |
| 5 | 🎓 Graduation | `graduation` | Academic achievements | $25 – $200 |
| 6 | 🍼 Baby Shower | `baby-shower` | Welcoming a new baby | $20 – $150 |
| 7 | 🏠 Housewarming | `housewarming` | New home celebrations | $25 – $150 |
| 8 | ❤️ Valentine's Day | `valentines` | Romantic gift-giving | $20 – $300 |
| 9 | 👩 Mother's Day | `mothers-day` | Honoring mothers | $25 – $150 |
| 10 | 👨 Father's Day | `fathers-day` | Honoring fathers | $25 – $150 |
| 11 | 🏖️ Retirement | `retirement` | Career milestone celebrations | $50 – $300 |
| 12 | 🙏 Thank You | `thank-you` | Expressing gratitude | $10 – $75 |
| 13 | 🤒 Get Well | `get-well` | Wishing speedy recovery | $15 – $75 |
| 14 | 🎁 Other | `other` | Any other occasion | $10 – $500 |

<br />

---

<br />

## 👥 Supported Relationships

Gift Recommendation Bot tailors suggestions based on **10 relationship types**:

| # | Relationship | Key | Typical Gift Style | Personalization Level |
|:-:|-------------|-----|--------------------|-----------------------|
| 1 | ❤️ Partner | `partner` | Romantic, intimate, meaningful | ★★★★★ |
| 2 | 👨‍👩‍👧 Parent | `parent` | Thoughtful, practical, sentimental | ★★★★☆ |
| 3 | 👫 Sibling | `sibling` | Fun, personal, inside-joke friendly | ★★★★☆ |
| 4 | 🤝 Friend | `friend` | Casual, fun, interest-based | ★★★☆☆ |
| 5 | 💼 Colleague | `colleague` | Professional, neutral, useful | ★★☆☆☆ |
| 6 | 👶 Child | `child` | Age-appropriate, fun, educational | ★★★★☆ |
| 7 | 👴 Grandparent | `grandparent` | Comfortable, nostalgic, practical | ★★★★☆ |
| 8 | 📚 Teacher | `teacher` | Appreciative, modest, classroom-useful | ★★☆☆☆ |
| 9 | 👔 Boss | `boss` | Professional, tasteful, non-personal | ★★☆☆☆ |
| 10 | 🏘️ Neighbor | `neighbor` | Friendly, modest, community-oriented | ★☆☆☆☆ |

<br />

---

<br />

## ⚙️ Configuration

Configuration is managed via `config.yaml` in the project root.

```yaml
# config.yaml

llm:
  model: gemma4
  temperature: 0.7
  max_tokens: 3072

occasions:
  - birthday
  - christmas
  - anniversary
  - wedding
  - graduation
  - baby-shower
  - housewarming
  - valentines
  - mothers-day
  - fathers-day
  - retirement
  - thank-you
  - get-well
  - other

relationships:
  - partner
  - parent
  - sibling
  - friend
  - colleague
  - child
  - grandparent
  - teacher
  - boss
  - neighbor

wishlist:
  storage_file: wishlists.json

calendar:
  storage_file: occasion_calendar.json
```

### Configuration Options

| Section | Key | Default | Description |
|---------|-----|---------|-------------|
| `llm` | `model` | `gemma4` | Ollama model name |
| `llm` | `temperature` | `0.7` | Creativity of responses (0.0–1.0) |
| `llm` | `max_tokens` | `3072` | Maximum response length |
| `wishlist` | `storage_file` | `wishlists.json` | Path to wishlist data |
| `calendar` | `storage_file` | `occasion_calendar.json` | Path to calendar data |

<br />

---

<br />

## 🧪 Testing

Run the full test suite:

```bash
# Run all tests
pytest tests/ -v

# Run specific test modules
pytest tests/test_core.py -v          # Core recommendation engine
pytest tests/test_wishlist.py -v      # Wishlist management
pytest tests/test_calendar.py -v      # Occasion calendar
pytest tests/test_utils.py -v         # Data persistence utilities

# Run with coverage report
pytest tests/ --cov=gift_recommendation_bot --cov-report=html
```

### Test Structure

| Test File | Tests | What It Covers |
|-----------|-------|----------------|
| `test_core.py` | `generate_recommendations`, `get_gift_details`, `compare_prices` | LLM integration, output format, budget filtering |
| `test_wishlist.py` | `add_to_wishlist`, `get_wishlist`, `mark_purchased` | CRUD operations, data persistence, edge cases |
| `test_calendar.py` | `add_occasion`, `get_upcoming_occasions` | Date handling, filtering, sorting |
| `test_utils.py` | `load_wishlists`, `save_wishlists`, `load_calendar`, `save_calendar` | File I/O, JSON serialization, error handling |

<br />

---

<br />

## 🤖 Local LLM vs Cloud AI

Gift Recommendation Bot is designed to run **entirely locally** using Ollama. Here's how it compares to cloud-based alternatives:

| Aspect | Local LLM (Default) | Cloud AI (Alternative) |
|--------|---------------------|----------------------|
| **Privacy** | ✅ All data stays on your machine | ❌ Data sent to external servers |
| **Cost** | ✅ Free after initial setup | ❌ Per-request API charges |
| **Speed** | ⚡ Depends on hardware (GPU recommended) | ⚡ Generally fast, network-dependent |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Model Quality** | 🟡 Good with Gemma 4 | 🟢 State-of-the-art with GPT-4/Claude |
| **Setup** | 🟡 Requires Ollama installation | 🟢 Just an API key |
| **Customization** | ✅ Full control over model and prompts | 🟡 Limited to API parameters |

### Switching Models

To use a different Ollama model, update `config.yaml`:

```yaml
llm:
  model: llama3       # or mistral, phi3, etc.
  temperature: 0.7
  max_tokens: 3072
```

Then pull the new model:

```bash
ollama pull llama3
```

<br />

---

<br />

## ❓ FAQ

<details>
<summary><strong>1. Does the bot fetch real-time prices from actual retailers?</strong></summary>

<br />

No. The `compare_prices()` function uses the LLM to generate **estimated price ranges** based on its training data. These are approximate and should be verified before purchasing. The estimates are generally accurate for well-known products but may not reflect current sales, discounts, or regional pricing.

For the most accurate pricing, use the generated gift names to search retailers directly.

</details>

<details>
<summary><strong>2. Can I share wishlists with other people?</strong></summary>

<br />

Wishlists are stored locally in `wishlists.json`. To share them:

- **Manual sharing:** Copy the `wishlists.json` file to another machine or share it via cloud storage.
- **Export:** Use `get_wishlist(person)` programmatically and export to CSV or any format you prefer.
- **Multi-user:** For a shared household, point multiple instances to the same `wishlists.json` file via `config.yaml`.

A built-in sharing/export feature is planned for a future release.

</details>

<details>
<summary><strong>3. Does the calendar send reminders or notifications?</strong></summary>

<br />

Currently, the calendar does not send push notifications or email reminders. It provides:

- **CLI alerts:** Run `calendar-show --days 7` daily to see upcoming occasions.
- **Web UI highlights:** The Calendar tab highlights events within 7 days in red.
- **Automation tip:** Set up a cron job or scheduled task to run the `calendar-show` command and pipe the output to your notification system.

```bash
# Example cron job (Linux/macOS) — runs daily at 8 AM
0 8 * * * cd /path/to/gift-recommendation-bot && python -m gift_recommendation_bot calendar-show --days 7
```

</details>

<details>
<summary><strong>4. What happens if my budget is too low for good gift ideas?</strong></summary>

<br />

The bot will still generate recommendations within your specified budget, no matter how low. For example, a $10 budget will yield thoughtful options like:

- Handwritten letter with a small treat
- A curated playlist or photo collage (free to make)
- A single high-quality item like specialty tea or chocolate

The LLM adapts its suggestions to be creative and meaningful at any price point. You can also set `--budget 0` for free/DIY gift ideas.

</details>

<details>
<summary><strong>5. How does the bot handle gift availability?</strong></summary>

<br />

The bot generates gift **ideas** and **categories** rather than linking to specific inventory. This means:

- Suggestions are always "available" as concepts — you won't get a recommendation for an out-of-stock item.
- The `compare_prices()` function provides estimated availability, but this is based on LLM knowledge, not real-time stock checks.
- For time-sensitive purchases, generate recommendations early and verify availability at your preferred retailers.

</details>

<br />

---

<br />

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Fork and clone
git clone https://github.com/<your-username>/gift-recommendation-bot.git
cd gift-recommendation-bot

# Create development environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests to verify setup
pytest tests/ -v
```

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes with tests
4. **Run** the test suite: `pytest tests/ -v`
5. **Commit** with a descriptive message: `git commit -m "Add: your feature description"`
6. **Push** to your fork: `git push origin feature/your-feature-name`
7. **Open** a Pull Request against `main`

### Areas for Contribution

| Area | Description | Difficulty |
|------|-------------|------------|
| New occasions | Add support for cultural or regional holidays | 🟢 Easy |
| Export formats | Add CSV/PDF export for wishlists | 🟢 Easy |
| Calendar reminders | Email or desktop notification integration | 🟡 Medium |
| Real price APIs | Integrate with retailer APIs for live pricing | 🟡 Medium |
| Multi-language | Support gift recommendations in other languages | 🟡 Medium |
| Group gifting | Coordinate group gifts with budget splitting | 🔴 Hard |

<br />

---

<br />

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 kennedyraju55

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

<br />

---

<div align="center">

**Built with ❤️ using local AI — because the best gifts come from thoughtful people, not cloud servers.**

<br />

<sub>⭐ Star this repo if Gift Recommendation Bot helped you find the perfect gift!</sub>

</div>
