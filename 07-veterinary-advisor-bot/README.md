<div align="center">

<!-- Hero Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:fb8500,100:ffb703&height=220&section=header&text=🐾%20Veterinary%20Advisor%20Bot&fontSize=42&fontColor=ffffff&fontAlignY=35&desc=AI-Powered%20Pet%20Health%20Consultation%20·%20Local%20LLM&descSize=18&descAlignY=55&animation=fadeIn" width="100%" alt="Veterinary Advisor Bot Banner"/>

<br/>

<!-- Badges -->
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Gemma_4-fb8500?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com)
[![Gradio](https://img.shields.io/badge/Gradio-Web_UI-F97316?style=for-the-badge&logo=gradio&logoColor=white)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Pet Types](https://img.shields.io/badge/Pet_Types-8-fb8500?style=for-the-badge)](#supported-pet-types)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)](#)

<br/>

<strong>An AI-powered veterinary advisor that provides pet health consultations, symptom analysis, breed-specific guidance, and nutrition advice — all running locally with Gemma 4 via Ollama. Built with medical safety guardrails: emergency detection, mandatory disclaimers, and zero medication prescriptions.</strong>

<br/><br/>

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Reference](#-api-reference) · [FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Pet owners face real challenges when it comes to their companions' health. This project exists to bridge the gap between "something seems wrong" and a proper veterinary visit.

<div align="center">

| | Challenge | How This Bot Helps |
|---|---|---|
| 🕐 | **After-hours worry** — Symptoms appear at 2 AM when no vet clinic is open | Provides immediate triage-level guidance and flags true emergencies that need an ER visit |
| 🐕 | **Breed-specific blind spots** — Owners unaware of breed-prone conditions | Delivers breed-specific health advice covering common conditions, exercise needs, and dietary considerations |
| 📋 | **Symptom tracking gaps** — No easy way to log and review symptom history | Records symptoms with severity levels and timestamps for sharing with your veterinarian |
| 💊 | **Dangerous self-medication** — Pet owners guessing dosages from the internet | Refuses to prescribe medications and always directs to a licensed veterinarian for treatment |
| 🌐 | **Privacy concerns** — Hesitation to share pet health data with cloud services | Runs 100% locally using Ollama — your pet's health data never leaves your machine |

</div>

<br/>

> [!IMPORTANT]
> This bot is **not** a replacement for professional veterinary care. It provides general health information and triage-level guidance only. Always consult a licensed veterinarian for diagnosis and treatment.

<br/>

---

<br/>

## ✨ Features

<div align="center">

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200">
  <defs>
    <linearGradient id="featureGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#fb8500;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ffb703;stop-opacity:1" />
    </linearGradient>
  </defs>
  <!-- Health Consultation -->
  <rect x="10" y="20" width="180" height="160" rx="16" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="100" y="70" text-anchor="middle" fill="#fb8500" font-size="32">💬</text>
  <text x="100" y="100" text-anchor="middle" fill="white" font-size="13" font-weight="bold">Health Chat</text>
  <text x="100" y="120" text-anchor="middle" fill="#aaa" font-size="10">Multi-turn AI</text>
  <text x="100" y="135" text-anchor="middle" fill="#aaa" font-size="10">consultation</text>
  <!-- Symptom Analysis -->
  <rect x="210" y="20" width="180" height="160" rx="16" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="300" y="70" text-anchor="middle" fill="#fb8500" font-size="32">🔍</text>
  <text x="300" y="100" text-anchor="middle" fill="white" font-size="13" font-weight="bold">Symptom Check</text>
  <text x="300" y="120" text-anchor="middle" fill="#aaa" font-size="10">Severity-aware</text>
  <text x="300" y="135" text-anchor="middle" fill="#aaa" font-size="10">analysis engine</text>
  <!-- Pet Profiles -->
  <rect x="410" y="20" width="180" height="160" rx="16" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="500" y="70" text-anchor="middle" fill="#fb8500" font-size="32">🐾</text>
  <text x="500" y="100" text-anchor="middle" fill="white" font-size="13" font-weight="bold">Pet Profiles</text>
  <text x="500" y="120" text-anchor="middle" fill="#aaa" font-size="10">Persistent storage</text>
  <text x="500" y="135" text-anchor="middle" fill="#aaa" font-size="10">with JSON backing</text>
  <!-- Emergency Detection -->
  <rect x="610" y="20" width="180" height="160" rx="16" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="700" y="70" text-anchor="middle" fill="#fb8500" font-size="32">🚨</text>
  <text x="700" y="100" text-anchor="middle" fill="white" font-size="13" font-weight="bold">Emergency Flags</text>
  <text x="700" y="120" text-anchor="middle" fill="#aaa" font-size="10">Breathing, seizures</text>
  <text x="700" y="135" text-anchor="middle" fill="#aaa" font-size="10">& poisoning alerts</text>
</svg>
```

</div>

<br/>

<div align="center">

| Feature | Description | Key Details | Access |
|---------|-------------|-------------|--------|
| 💬 **Health Consultation** | Multi-turn AI chat with veterinary knowledge | Context-aware responses using `get_response()` with pet profile enrichment | CLI `chat-cmd` / Web Chat tab |
| 🔍 **Symptom Analysis** | Structured symptom checking with severity levels | Supports `mild`, `moderate`, `severe`, `unknown` via `check_symptoms()` | CLI `/symptoms` / Web Symptom tab |
| 🐾 **Pet Profiles** | Persistent pet records with breed, age, and weight | JSON-backed storage with `add_pet_profile()` and `get_pet_profile()` | CLI flags / Web UI forms |
| 🚨 **Emergency Detection** | Automatic flagging of critical symptoms | Detects breathing difficulties, seizures, and poisoning indicators | Always active in all interfaces |

</div>

<br/>

**Additional capabilities:**

- 🦴 **Breed-Specific Advice** — Tailored health guidance via `get_breed_advice(pet_type, breed)` covering breed-prone conditions
- 🥗 **Nutrition Guidance** — Diet and feeding recommendations via `get_nutrition_advice(pet_profile)` based on pet type, age, and weight
- 📊 **Symptom History** — Track and review symptoms over time with `record_symptom()` and `get_symptom_history_for_pet()`
- 🔒 **Medical Safety** — `MEDICAL_DISCLAIMER` appended to every response; zero medication prescriptions
- 🏠 **Fully Local** — Runs on Ollama with Gemma 4; no data leaves your machine

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.10+ | Runtime |
| Ollama | Latest | Local LLM inference |
| Gemma 4 | Via Ollama | Language model |

### 1. Clone & Install

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/veterinary-advisor-bot.git
cd veterinary-advisor-bot

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Pull the Model

```bash
# Download Gemma 4 via Ollama
ollama pull gemma4
```

### 3. First Run — CLI

```bash
# Start an interactive chat session with a pet profile
python -m veterinary_advisor_bot chat-cmd --pet-type dog --name Buddy --breed "Golden Retriever"
```

You'll see:

```
🐾 Veterinary Advisor Bot — Chat Mode
Pet: Buddy (dog, Golden Retriever)
Type your question or use a sub-command. Type 'quit' to exit.

You > My dog has been scratching his ears a lot lately
🤖 Assistant > Excessive ear scratching in Golden Retrievers can indicate...

⚕️ Disclaimer: This information is for educational purposes only...
```

### 4. First Run — Web UI

```bash
# Launch the Gradio web interface
python -m veterinary_advisor_bot web
```

Open `http://localhost:7860` in your browser to access the three-tab interface.

<br/>

---

<br/>

## 📟 CLI Reference

The `veterinary_advisor_bot` module provides a multi-command CLI interface.

### Commands

#### `chat-cmd` — Interactive Health Chat

```bash
python -m veterinary_advisor_bot chat-cmd [OPTIONS]
```

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `--pet-type` | string | `dog` | Pet type: dog, cat, bird, fish, rabbit, hamster, reptile, other |
| `--name` | string | — | Pet's name for profile lookup/creation |
| `--breed` | string | — | Pet's breed for breed-specific advice |

**Sub-commands** (available within the chat session):

| Sub-command | Syntax | Description |
|-------------|--------|-------------|
| `/symptoms` | `/symptoms <description>` | Run a symptom analysis on the provided description |
| `/breed` | `/breed` | Get breed-specific health advice for the current pet |
| `/nutrition` | `/nutrition` | Get nutrition and diet recommendations for the current pet |
| `/history` | `/history` | Display symptom history for the current pet |
| `quit` | `quit` | Exit the chat session |

**Examples:**

```bash
# Basic chat session
python -m veterinary_advisor_bot chat-cmd

# Chat with full pet profile
python -m veterinary_advisor_bot chat-cmd --pet-type cat --name Luna --breed "Maine Coon"

# Inside the chat session:
You > /symptoms vomiting and lethargy for 2 days
You > /breed
You > /nutrition
You > /history
You > quit
```

#### `list-pets` — View Saved Pet Profiles

```bash
python -m veterinary_advisor_bot list-pets
```

Displays all saved pet profiles from `pet_profiles.json`:

```
📋 Saved Pet Profiles:
──────────────────────
  🐕 Buddy — dog, Golden Retriever, 3 years, 30 kg
  🐱 Luna — cat, Maine Coon, 5 years, 6 kg
  🐦 Kiwi — bird, Cockatiel, 2 years, 0.1 kg
```

<br/>

---

<br/>

## 🌐 Web UI

The Gradio-powered web interface organizes functionality into **three tabs**:

### Tab 1: 💬 Chat — Health Consultation

Interactive multi-turn conversation with the veterinary advisor AI.

- **Input:** Free-text health questions
- **Context:** Optionally select a pet profile to enrich responses with breed/age/weight context
- **Output:** AI-generated health guidance with `MEDICAL_DISCLAIMER` appended
- **Powered by:** `get_response(user_message, history, pet_profile)`

### Tab 2: 🔍 Symptom Check — Symptom Analysis

Structured symptom analysis with additional breed and nutrition advice.

- **Input:** Symptom description text field + pet profile selector
- **Analysis:** Runs `check_symptoms(symptoms, pet_profile)` with severity assessment
- **Breed Advice:** Calls `get_breed_advice(pet_type, breed)` for breed-specific considerations
- **Nutrition Advice:** Calls `get_nutrition_advice(pet_profile)` for dietary recommendations
- **Output:** Combined analysis panel with severity level and actionable guidance

### Tab 3: 📊 History — Symptom History Table

View and review past symptom records for any pet.

- **Input:** Pet name selector
- **Data:** Fetched via `get_symptom_history_for_pet(pet_name)`
- **Display:** Table with columns: Date, Symptoms, Severity, Notes
- **Storage:** Backed by `symptom_history.json` with a maximum of 500 entries

<br/>

---

<br/>

## 🏗️ Architecture

### System Flow

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 360">
  <defs>
    <linearGradient id="archGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#fb8500;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#ffb703;stop-opacity:1" />
    </linearGradient>
  </defs>
  <!-- User Layer -->
  <rect x="20" y="20" width="780" height="60" rx="12" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="410" y="40" text-anchor="middle" fill="#fb8500" font-size="11" font-weight="bold">USER LAYER</text>
  <text x="200" y="60" text-anchor="middle" fill="white" font-size="12">CLI (chat-cmd / list-pets)</text>
  <text x="620" y="60" text-anchor="middle" fill="white" font-size="12">Web UI (Gradio — 3 Tabs)</text>
  <!-- Arrow -->
  <line x1="410" y1="80" x2="410" y2="110" stroke="#fb8500" stroke-width="2" marker-end="url(#arrowhead)"/>
  <!-- Core Layer -->
  <rect x="20" y="110" width="780" height="100" rx="12" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="410" y="130" text-anchor="middle" fill="#fb8500" font-size="11" font-weight="bold">CORE ENGINE</text>
  <text x="140" y="160" text-anchor="middle" fill="white" font-size="11">get_response()</text>
  <text x="300" y="160" text-anchor="middle" fill="white" font-size="11">check_symptoms()</text>
  <text x="460" y="160" text-anchor="middle" fill="white" font-size="11">get_breed_advice()</text>
  <text x="640" y="160" text-anchor="middle" fill="white" font-size="11">get_nutrition_advice()</text>
  <text x="220" y="190" text-anchor="middle" fill="white" font-size="11">add_pet_profile()</text>
  <text x="410" y="190" text-anchor="middle" fill="white" font-size="11">get_pet_profile()</text>
  <text x="600" y="190" text-anchor="middle" fill="white" font-size="11">record_symptom()</text>
  <!-- Arrow -->
  <line x1="410" y1="210" x2="410" y2="240" stroke="#fb8500" stroke-width="2"/>
  <!-- Data Layer -->
  <rect x="20" y="240" width="380" height="60" rx="12" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="210" y="260" text-anchor="middle" fill="#fb8500" font-size="11" font-weight="bold">DATA LAYER</text>
  <text x="130" y="285" text-anchor="middle" fill="white" font-size="11">pet_profiles.json</text>
  <text x="300" y="285" text-anchor="middle" fill="white" font-size="11">symptom_history.json</text>
  <!-- LLM Layer -->
  <rect x="420" y="240" width="380" height="60" rx="12" fill="#1a1a2e" stroke="#fb8500" stroke-width="2"/>
  <text x="610" y="260" text-anchor="middle" fill="#fb8500" font-size="11" font-weight="bold">LLM LAYER</text>
  <text x="610" y="285" text-anchor="middle" fill="white" font-size="12">Ollama → Gemma 4 (local)</text>
  <!-- Safety Badge -->
  <rect x="280" y="320" width="260" height="30" rx="8" fill="#fb8500"/>
  <text x="410" y="340" text-anchor="middle" fill="white" font-size="12" font-weight="bold">🛡️ MEDICAL_DISCLAIMER on every response</text>
</svg>
```

### Data Flow

```
User Input
  │
  ├── CLI (chat-cmd)  ──────────────────┐
  │     └── Sub-commands (/symptoms,    │
  │         /breed, /nutrition, /history)│
  │                                     ▼
  ├── Web UI (Gradio) ──────────► Core Engine
  │     ├── Chat Tab                    │
  │     ├── Symptom Check Tab           ├── format_pet_context()
  │     └── History Tab                 ├── load_pet_profiles() / save_pet_profiles()
  │                                     ├── load_symptom_history() / save_symptom_history()
  │                                     │
  │                                     ▼
  │                              Ollama (Gemma 4)
  │                                     │
  │                                     ▼
  └─────────────────────────── Response + MEDICAL_DISCLAIMER
                                        │
                                        ├── Emergency flags checked
                                        │   (breathing, seizures, poisoning)
                                        │
                                        └── Rendered to user
```

### Project Structure

```
07-veterinary-advisor-bot/
├── veterinary_advisor_bot/
│   ├── __init__.py              # Package init
│   ├── __main__.py              # CLI entry point (chat-cmd, list-pets)
│   ├── core.py                  # Core functions: get_response, check_symptoms,
│   │                            #   get_breed_advice, get_nutrition_advice
│   ├── profiles.py              # Pet profiles: add_pet_profile, get_pet_profile
│   ├── symptoms.py              # Symptom tracking: record_symptom,
│   │                            #   get_symptom_history_for_pet
│   ├── utils.py                 # Helpers: format_pet_context, load/save functions
│   ├── web.py                   # Gradio web UI (3 tabs)
│   └── config.py                # Configuration loader
├── config.yaml                  # LLM & application configuration
├── pet_profiles.json            # Persistent pet profile storage
├── symptom_history.json         # Persistent symptom history storage
├── requirements.txt             # Python dependencies
├── tests/                       # Test suite
│   ├── test_core.py
│   ├── test_profiles.py
│   ├── test_symptoms.py
│   └── test_utils.py
└── README.md                    # This file
```

<br/>

---

<br/>

## 📖 API Reference

All core functions are available in the `veterinary_advisor_bot` package.

### `get_response(user_message, history, pet_profile)`

Main conversational endpoint. Sends the user's message along with conversation history and an optional pet profile to the LLM for a context-aware veterinary response.

```python
from veterinary_advisor_bot.core import get_response

response = get_response(
    user_message="My dog has been limping on his front left leg",
    history=[
        {"role": "user", "content": "Hi, I need help with my dog"},
        {"role": "assistant", "content": "Of course! What seems to be the issue?"}
    ],
    pet_profile={
        "name": "Buddy",
        "pet_type": "dog",
        "breed": "Golden Retriever",
        "age": 3,
        "weight": 30
    }
)
print(response)
# Includes veterinary guidance + MEDICAL_DISCLAIMER
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_message` | `str` | Yes | The user's health question or concern |
| `history` | `list[dict]` | Yes | Conversation history as role/content dicts |
| `pet_profile` | `dict \| None` | No | Pet profile dict for context enrichment |

**Returns:** `str` — AI-generated response with `MEDICAL_DISCLAIMER` appended.

---

### `check_symptoms(symptoms, pet_profile)`

Analyzes a symptom description against the pet's profile to provide severity assessment and guidance.

```python
from veterinary_advisor_bot.core import check_symptoms

result = check_symptoms(
    symptoms="vomiting, lethargy, loss of appetite for 2 days",
    pet_profile={
        "name": "Luna",
        "pet_type": "cat",
        "breed": "Maine Coon",
        "age": 5,
        "weight": 6
    }
)
print(result)
# Structured symptom analysis with severity assessment
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symptoms` | `str` | Yes | Description of observed symptoms |
| `pet_profile` | `dict \| None` | No | Pet profile for context-aware analysis |

**Returns:** `str` — Symptom analysis with severity level and recommendations.

---

### `get_breed_advice(pet_type, breed)`

Retrieves breed-specific health guidance including common conditions, exercise needs, and care recommendations.

```python
from veterinary_advisor_bot.core import get_breed_advice

advice = get_breed_advice(
    pet_type="dog",
    breed="Golden Retriever"
)
print(advice)
# Breed-specific health information and common conditions
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pet_type` | `str` | Yes | One of the 8 supported pet types |
| `breed` | `str` | Yes | Breed name within the pet type |

**Returns:** `str` — Breed-specific health advice.

---

### `get_nutrition_advice(pet_profile)`

Generates diet and nutrition recommendations tailored to the pet's type, breed, age, and weight.

```python
from veterinary_advisor_bot.core import get_nutrition_advice

nutrition = get_nutrition_advice(
    pet_profile={
        "name": "Buddy",
        "pet_type": "dog",
        "breed": "Golden Retriever",
        "age": 3,
        "weight": 30
    }
)
print(nutrition)
# Tailored nutrition and feeding guidelines
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pet_profile` | `dict` | Yes | Pet profile with name, pet_type, breed, age, weight |

**Returns:** `str` — Nutrition advice and feeding recommendations.

---

### `add_pet_profile(name, pet_type, breed, age, weight)`

Creates and persists a new pet profile to `pet_profiles.json`.

```python
from veterinary_advisor_bot.profiles import add_pet_profile

profile = add_pet_profile(
    name="Buddy",
    pet_type="dog",
    breed="Golden Retriever",
    age=3,
    weight=30
)
print(profile)
# {'name': 'Buddy', 'pet_type': 'dog', 'breed': 'Golden Retriever', 'age': 3, 'weight': 30}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `str` | Yes | Pet's name (used as identifier) |
| `pet_type` | `str` | Yes | One of: dog, cat, bird, fish, rabbit, hamster, reptile, other |
| `breed` | `str` | Yes | Breed name |
| `age` | `int \| float` | Yes | Age in years |
| `weight` | `int \| float` | Yes | Weight in kilograms |

**Returns:** `dict` — The created pet profile.

---

### `get_pet_profile(name)`

Retrieves a saved pet profile by name from `pet_profiles.json`.

```python
from veterinary_advisor_bot.profiles import get_pet_profile

profile = get_pet_profile("Buddy")
if profile:
    print(f"{profile['name']} is a {profile['age']}-year-old {profile['breed']}")
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | `str` | Yes | Pet's name to look up |

**Returns:** `dict | None` — Pet profile dict if found, `None` otherwise.

---

### `record_symptom(pet_name, symptoms, severity, notes)`

Records a symptom entry for a pet in `symptom_history.json` with a timestamp.

```python
from veterinary_advisor_bot.symptoms import record_symptom

record_symptom(
    pet_name="Luna",
    symptoms="sneezing, watery eyes",
    severity="mild",
    notes="Started after visiting the park"
)
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pet_name` | `str` | Yes | Name of the pet |
| `symptoms` | `str` | Yes | Description of observed symptoms |
| `severity` | `str` | Yes | One of: `mild`, `moderate`, `severe`, `unknown` |
| `notes` | `str` | No | Additional context or observations |

**Returns:** `None` — Entry is persisted to `symptom_history.json`.

---

### `get_symptom_history_for_pet(pet_name)`

Retrieves the full symptom history for a specific pet.

```python
from veterinary_advisor_bot.symptoms import get_symptom_history_for_pet

history = get_symptom_history_for_pet("Luna")
for entry in history:
    print(f"{entry['date']} — {entry['symptoms']} ({entry['severity']})")
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `pet_name` | `str` | Yes | Name of the pet to look up |

**Returns:** `list[dict]` — List of symptom history entries with date, symptoms, severity, and notes.

<br/>

---

<br/>

## 🐾 Supported Pet Types

The bot supports **8 pet types**, each with tailored health knowledge and breed databases:

<div align="center">

| Pet Type | Identifier | Example Breeds | Common Health Topics |
|----------|------------|----------------|----------------------|
| 🐕 Dog | `dog` | Golden Retriever, Labrador, German Shepherd, Bulldog | Hip dysplasia, allergies, dental disease, obesity |
| 🐱 Cat | `cat` | Maine Coon, Siamese, Persian, British Shorthair | Kidney disease, hyperthyroidism, dental issues, hairballs |
| 🐦 Bird | `bird` | Cockatiel, Budgerigar, Parrot, Canary | Respiratory infections, feather plucking, nutritional deficiency |
| 🐠 Fish | `fish` | Betta, Goldfish, Guppy, Angelfish | Ich, fin rot, swim bladder disorder, water quality issues |
| 🐇 Rabbit | `rabbit` | Holland Lop, Mini Rex, Netherland Dwarf, Lionhead | GI stasis, dental malocclusion, respiratory infections |
| 🐹 Hamster | `hamster` | Syrian, Dwarf Campbell, Roborovski, Chinese | Wet tail, respiratory infections, dental overgrowth |
| 🦎 Reptile | `reptile` | Leopard Gecko, Bearded Dragon, Ball Python, Chameleon | Metabolic bone disease, respiratory infections, parasites |
| 🐾 Other | `other` | Guinea Pig, Ferret, Hedgehog, Chinchilla | General small animal health, diet, and husbandry |

</div>

<br/>

---

<br/>

## 🛡️ Medical Safety

Medical safety is a core design principle of this project. The bot implements multiple layers of protection.

### MEDICAL_DISCLAIMER

Every response generated by the bot includes the `MEDICAL_DISCLAIMER` constant. This disclaimer is **always appended** — it cannot be disabled or bypassed.

```
⚕️ Disclaimer: This information is for educational purposes only and does not
constitute veterinary medical advice. Always consult a licensed veterinarian
for diagnosis, treatment, and medication decisions for your pet.
```

### Emergency Detection Flags

The bot actively monitors for **emergency keywords** in symptom descriptions and user messages. When detected, the response is prefixed with an urgent warning:

| Emergency Flag | Trigger Keywords | Response Action |
|----------------|-----------------|-----------------|
| 🚨 **Breathing** | Difficulty breathing, gasping, choking, labored breathing | Immediate ER warning — "Seek emergency veterinary care NOW" |
| 🚨 **Seizures** | Seizure, convulsions, fitting, tremors, shaking uncontrollably | Immediate ER warning — "Do not restrain; seek emergency care" |
| 🚨 **Poisoning** | Poisoned, ate poison, toxic ingestion, ate chocolate, antifreeze | Immediate ER warning — "Contact poison control or emergency vet" |

### What the Bot Will NOT Do

| ❌ Limitation | Reason |
|--------------|--------|
| Prescribe medications | Medication dosing requires a physical examination and licensed veterinarian |
| Provide specific dosages | Dosages vary by weight, condition, and drug interactions |
| Diagnose conditions definitively | Diagnosis requires lab work, imaging, and physical examination |
| Replace veterinary visits | The bot is a triage tool, not a substitute for professional care |
| Store sensitive medical records | The bot stores basic symptom logs only, not protected health information |

<br/>

---

<br/>

## ⚙️ Configuration

The bot is configured via `config.yaml` at the project root:

```yaml
# LLM Configuration
llm:
  model: gemma4                # Ollama model name
  temperature: 0.7             # Response creativity (0.0 - 1.0)
  max_tokens: 2048             # Maximum response length

# Supported pet types
pet_types:
  - dog
  - cat
  - bird
  - fish
  - rabbit
  - hamster
  - reptile
  - other

# Pet profile storage
profiles:
  storage_file: pet_profiles.json

# Symptom history storage
symptom_history:
  storage_file: symptom_history.json
  max_entries: 500             # Maximum symptom history entries
```

### Configuration Options

| Key | Default | Description |
|-----|---------|-------------|
| `llm.model` | `gemma4` | Ollama model to use for inference |
| `llm.temperature` | `0.7` | Controls response randomness (lower = more deterministic) |
| `llm.max_tokens` | `2048` | Maximum tokens in generated responses |
| `pet_types` | 8 types | List of supported pet type identifiers |
| `profiles.storage_file` | `pet_profiles.json` | File path for pet profile persistence |
| `symptom_history.storage_file` | `symptom_history.json` | File path for symptom history persistence |
| `symptom_history.max_entries` | `500` | Maximum number of symptom history entries before rotation |

<br/>

---

<br/>

## 🧪 Testing

Run the test suite to verify all components:

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test modules
python -m pytest tests/test_core.py -v          # Core functions
python -m pytest tests/test_profiles.py -v       # Pet profile management
python -m pytest tests/test_symptoms.py -v       # Symptom tracking
python -m pytest tests/test_utils.py -v          # Utility functions

# Run with coverage
python -m pytest tests/ --cov=veterinary_advisor_bot --cov-report=term-missing
```

### Test Categories

| Test Module | Tests | What It Covers |
|-------------|-------|----------------|
| `test_core.py` | Core engine | `get_response`, `check_symptoms`, `get_breed_advice`, `get_nutrition_advice` |
| `test_profiles.py` | Profile CRUD | `add_pet_profile`, `get_pet_profile`, profile persistence |
| `test_symptoms.py` | Symptom tracking | `record_symptom`, `get_symptom_history_for_pet`, severity validation |
| `test_utils.py` | Utilities | `format_pet_context`, load/save helpers, edge cases |

<br/>

---

<br/>

## 🏠 Local LLM vs Cloud AI

This project is designed to run **entirely locally** using Ollama. Here's why, and how it compares:

| Aspect | Local LLM (This Project) | Cloud AI (GPT-4, Claude, etc.) |
|--------|--------------------------|-------------------------------|
| **Privacy** | ✅ Data never leaves your machine | ❌ Data sent to third-party servers |
| **Cost** | ✅ Free after hardware investment | ❌ Per-token API costs |
| **Latency** | ⚡ No network round-trip | 🌐 Depends on internet connection |
| **Offline** | ✅ Works without internet | ❌ Requires internet connection |
| **Quality** | 🟡 Good with Gemma 4 | ✅ State-of-the-art accuracy |
| **Hardware** | ⚠️ Requires capable GPU/CPU | ✅ Runs on any device with internet |
| **Customization** | ✅ Full control over model and prompts | 🟡 Limited to API parameters |

### Switching Models

To use a different Ollama model, update `config.yaml`:

```yaml
llm:
  model: llama3      # or mistral, phi3, etc.
  temperature: 0.7
  max_tokens: 2048
```

Then pull the model:

```bash
ollama pull llama3
```

<br/>

---

<br/>

## 🧰 Utility Functions

The `utils.py` module provides helper functions used across the application:

### `format_pet_context(pet_profile)`

Formats a pet profile dict into a human-readable context string for LLM prompts.

```python
from veterinary_advisor_bot.utils import format_pet_context

context = format_pet_context({
    "name": "Buddy",
    "pet_type": "dog",
    "breed": "Golden Retriever",
    "age": 3,
    "weight": 30
})
# Returns: "Pet: Buddy, a 3-year-old Golden Retriever (dog), weighing 30 kg"
```

### `load_pet_profiles()` / `save_pet_profiles(profiles)`

Load and save pet profiles from/to the configured JSON storage file.

```python
from veterinary_advisor_bot.utils import load_pet_profiles, save_pet_profiles

profiles = load_pet_profiles()          # Returns dict of all profiles
save_pet_profiles(profiles)             # Persists profiles to JSON file
```

### `load_symptom_history()` / `save_symptom_history(history)`

Load and save symptom history from/to the configured JSON storage file.

```python
from veterinary_advisor_bot.utils import load_symptom_history, save_symptom_history

history = load_symptom_history()        # Returns list of symptom entries
save_symptom_history(history)           # Persists history to JSON file
```

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>1. How accurate is the medical advice?</strong></summary>

<br/>

The bot provides **general health information**, not medical diagnoses. It uses Gemma 4's training data to offer guidance similar to what you might find in reputable pet health resources. However, AI-generated advice has inherent limitations:

- It cannot perform physical examinations
- It cannot interpret lab results or imaging
- It may not be aware of the latest veterinary research
- It cannot account for your pet's complete medical history

**Always verify the bot's suggestions with your veterinarian**, especially for serious or persistent symptoms. The `MEDICAL_DISCLAIMER` is included on every response as a reminder.

</details>

<details>
<summary><strong>2. How does emergency detection work?</strong></summary>

<br/>

The bot scans user messages and symptom descriptions for **predefined emergency keywords**:

- **Breathing emergencies:** "difficulty breathing", "gasping", "choking", "labored breathing"
- **Seizure emergencies:** "seizure", "convulsions", "fitting", "tremors"
- **Poisoning emergencies:** "poisoned", "ate poison", "toxic ingestion", "ate chocolate", "antifreeze"

When any of these keywords are detected, the bot immediately prepends a **🚨 EMERGENCY** warning banner to the response, directing the user to seek immediate veterinary care. This detection runs on every message in both CLI and Web UI — it cannot be disabled.

</details>

<details>
<summary><strong>3. How extensive is the breed database?</strong></summary>

<br/>

The bot does not use a static breed database. Instead, it leverages the LLM's (Gemma 4) training knowledge to provide breed-specific advice via `get_breed_advice(pet_type, breed)`. This means:

- It can handle virtually any breed that appeared in the model's training data
- Common breeds (Golden Retriever, Siamese, etc.) will have more detailed and accurate advice
- Rare or newly recognized breeds may receive more generic guidance
- Cross-breeds and mixed breeds are supported — describe them as you would to a vet

</details>

<details>
<summary><strong>4. What are the symptom history limits?</strong></summary>

<br/>

The symptom history system is configured with a maximum of **500 entries** per installation (configurable via `symptom_history.max_entries` in `config.yaml`). When the limit is reached, the oldest entries are rotated out.

- Each entry stores: date (timestamp), pet name, symptoms, severity, and notes
- History is stored in `symptom_history.json` — a plain JSON file you can back up or share with your vet
- There is no per-pet limit; the 500 limit applies across all pets combined
- To increase the limit, modify `max_entries` in `config.yaml`

</details>

<details>
<summary><strong>5. Why doesn't the bot prescribe medications?</strong></summary>

<br/>

**This is a deliberate safety design decision.** Medication prescriptions are excluded because:

- **Dosage risks:** Incorrect dosages can be fatal, especially for small animals. A 5 kg cat requires vastly different dosing than a 40 kg dog.
- **Drug interactions:** The bot has no way to know what other medications your pet is taking.
- **Species sensitivity:** Some medications safe for dogs are lethal to cats (e.g., certain NSAIDs). The bot cannot verify species-specific safety.
- **Legal requirements:** In most jurisdictions, prescribing veterinary medications requires a licensed veterinarian with an established veterinary-client-patient relationship (VCPR).

The bot will describe general treatment approaches (e.g., "your vet may recommend anti-nausea medication") but will **never** name specific drugs or dosages.

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add your feature description"`
4. **Push** to your branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

### Guidelines

- Follow existing code patterns and naming conventions
- Add tests for new functions in the appropriate `tests/` module
- Ensure the `MEDICAL_DISCLAIMER` is never bypassed in new response paths
- Do not add medication prescription functionality
- Test with at least 2 different pet types before submitting

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/veterinary-advisor-bot.git
cd veterinary-advisor-bot

# Install in development mode
pip install -e ".[dev]"

# Run tests before submitting
python -m pytest tests/ -v
```

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

<br/>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:fb8500,100:ffb703&height=120&section=footer" width="100%" alt="Footer"/>

<br/>

**Built with ❤️ for pets everywhere**

<sub>Powered by Ollama · Gemma 4 · Gradio · Python</sub>

<br/><br/>

<a href="#"><img src="https://img.shields.io/badge/⬆_Back_to_Top-fb8500?style=for-the-badge" alt="Back to Top"/></a>

</div>
