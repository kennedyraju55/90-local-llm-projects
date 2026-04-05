<div align="center">

<!-- Hero Banner -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:003459,100:00b4d8&height=220&section=header&text=IT%20Helpdesk%20Bot&fontSize=52&fontColor=ffffff&fontAlignY=35&desc=AI-Powered%20IT%20Support%20%E2%80%A2%20Local%20LLM%20%E2%80%A2%20Zero%20Cloud%20Dependency&descSize=18&descAlignY=55&descColor=b8e0ec">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:003459,100:00b4d8&height=220&section=header&text=IT%20Helpdesk%20Bot&fontSize=52&fontColor=ffffff&fontAlignY=35&desc=AI-Powered%20IT%20Support%20%E2%80%A2%20Local%20LLM%20%E2%80%A2%20Zero%20Cloud%20Dependency&descSize=18&descAlignY=55&descColor=b8e0ec" width="100%" alt="IT Helpdesk Bot Banner">
</picture>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-00b4d8?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](CONTRIBUTING.md)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

**Resolve IT issues instantly with a locally-hosted AI helpdesk — no API keys, no cloud fees, complete data privacy.**

[Quick Start](#-quick-start) · [CLI Reference](#-cli-reference) · [Web UI](#-web-ui) · [API Docs](#-api-reference) · [FAQ](#-faq)

</div>

---

## 📋 Table of Contents

- [Why This Project?](#-why-this-project)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [CLI Reference](#-cli-reference)
- [Web UI](#-web-ui)
- [Architecture](#-architecture)
- [API Reference](#-api-reference)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Local LLM vs Cloud AI](#-local-llm-vs-cloud-ai)
- [FAQ](#-faq)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🤔 Why This Project?

IT support teams face recurring challenges that drain time, money, and morale. Most organizations rely on either overloaded human agents or expensive cloud-based AI solutions that raise data-privacy concerns. **IT Helpdesk Bot** bridges this gap by running a capable LLM entirely on your local infrastructure.

| # | Problem | Impact | Solution (IT Helpdesk Bot) | Outcome |
|---|---------|--------|----------------------------|---------|
| 1 | **Repetitive L1 tickets** consume 60 %+ of helpdesk bandwidth | Senior engineers waste hours on password resets, printer jams, and VPN issues | AI instantly triages and resolves common issues across **7 support categories** | Free up staff for complex infrastructure work |
| 2 | **Cloud AI services** expose sensitive internal data to third-party servers | Compliance violations, data-leak risk, recurring API costs | Runs **100 % locally** on Ollama — no data ever leaves your network | Full GDPR / HIPAA-friendly operation at zero marginal cost |
| 3 | **No after-hours support** — tickets pile up overnight | Employees blocked until morning; SLA breaches | Bot is available **24 / 7** with sub-second response times | Continuous coverage without shift scheduling |
| 4 | **Scattered tribal knowledge** lives in wikis, emails, and Slack threads | New hires struggle; solutions get reinvented | Built-in **searchable knowledge base** with curated solutions | Single source of truth, accessible from CLI or Web UI |
| 5 | **Ticket tracking is manual** — spreadsheets, sticky notes, or expensive ITSM tools | Lost tickets, no audit trail, poor metrics | Automatic **JSON-based ticket tracking** with history and status | Lightweight, portable, zero-config ticket management |

---

## ✨ Features

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                     IT HELPDESK BOT                             │
│                                                                 │
│   ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│   │   CLI   │  │  Web UI  │  │    KB    │  │   Tickets    │   │
│   │ Console │  │Streamlit │  │  Search  │  │   Tracker    │   │
│   └────┬────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘   │
│        │            │             │                │            │
│        └────────────┴──────┬──────┴────────────────┘            │
│                            │                                    │
│                    ┌───────┴───────┐                            │
│                    │  Core Engine  │                            │
│                    │ get_response()│                            │
│                    └───────┬───────┘                            │
│                            │                                    │
│                    ┌───────┴───────┐                            │
│                    │  Ollama LLM   │                            │
│                    │   (gemma4)    │                            │
│                    └───────────────┘                            │
└─────────────────────────────────────────────────────────────────┘
```

</div>

| Feature | Description | Highlights |
|---------|-------------|------------|
| 🏷️ **Support Categories** | Seven dedicated IT support categories covering the most common helpdesk domains | `Hardware` · `Software` · `Network` · `Security` · `Email` · `Printer` · `General` — select via CLI flag or sidebar dropdown |
| 🎫 **Ticket Management** | Automatic ticket creation, storage, and retrieval using a lightweight JSON backend | Every conversation auto-generates a ticket with timestamp, category, issue summary, and resolution status — view the last 10 from the UI |
| 📚 **Knowledge Base** | Searchable repository of curated IT solutions loaded from `knowledge_base.json` | Query from CLI (`kb <query>`) or the dedicated Web UI tab with expandable solution cards |
| 🤖 **AI Diagnostics** | Context-aware, multi-turn troubleshooting powered by a local LLM through Ollama | Maintains conversation history for follow-up questions; adjustable temperature for creative vs. deterministic responses |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.10 + | Runtime |
| **Ollama** | latest | Local LLM server |
| **gemma4** model | pulled via Ollama | Default language model |
| **pip** | latest | Package management |

### 1 — Install Ollama & Pull the Model

```bash
# Install Ollama (visit https://ollama.com for platform-specific instructions)
# Then pull the default model:
ollama pull gemma4
```

> **Tip:** Ensure Ollama is running (`ollama serve`) before launching the bot.

### 2 — Clone & Install

```bash
git clone https://github.com/kennedyraju55/it-helpdesk-bot.git
cd it-helpdesk-bot

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

### 3 — First Run (CLI)

```bash
python -m src.it_helpdesk_bot --category 2
```

This launches the interactive CLI in the **Software** support category. You will see:

```
╔══════════════════════════════════════════════════╗
║          IT Helpdesk Bot — Software Support      ║
╚══════════════════════════════════════════════════╝

Type your issue, or use a command:
  new       — start a new conversation
  ticket    — view your current ticket
  kb <q>    — search the knowledge base
  history   — show conversation history
  quit      — exit

You > My Outlook keeps freezing every time I open an attachment

Bot > I understand you're experiencing Outlook freezing when opening
      attachments. Let's troubleshoot step by step:

      1. **Check for updates** — Open Outlook → File → Office Account
         → Update Options → Update Now.
      2. **Disable hardware acceleration** — File → Options → Advanced
         → uncheck "Disable hardware graphics acceleration."
      3. **Run in Safe Mode** — Press Win+R, type `outlook /safe`,
         press Enter. If attachments open normally, a faulty add-in
         is likely the cause.
      4. **Repair Office** — Control Panel → Programs → Microsoft 365
         → Change → Online Repair.

      Would you like me to walk you through any of these steps in
      detail?

You > Yes, step 3 please
```

### 4 — First Run (Web UI)

```bash
streamlit run app.py
```

Opens `http://localhost:8501` with the full web interface. See [Web UI](#-web-ui) for details.


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/it-helpdesk-bot.git
cd it-helpdesk-bot
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
uvicorn src.helpdesk_bot.api:app --reload --port 8000

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

### Launch Command

```bash
python -m src.it_helpdesk_bot [OPTIONS]
```

### Options

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--category` | `int` (1–7) | Interactive prompt | Pre-select a support category on launch |

#### Category Codes

| Code | Category | Typical Issues |
|------|----------|----------------|
| `1` | Hardware | Laptop won't boot, external monitor not detected, keyboard unresponsive |
| `2` | Software | App crashes, installation failures, license activation |
| `3` | Network | Wi-Fi drops, VPN errors, DNS resolution failures |
| `4` | Security | Phishing emails, account lockouts, malware alerts |
| `5` | Email | Outlook sync issues, calendar not updating, mailbox full |
| `6` | Printer | Paper jams, print queue stuck, driver installation |
| `7` | General | Password resets, onboarding requests, general IT questions |

### Interactive Commands

Once inside the CLI session, the following commands are available:

| Command | Description | Example |
|---------|-------------|---------|
| `new` | Clear history and start a fresh conversation | `You > new` |
| `ticket` | Display the current ticket (ID, status, category, summary) | `You > ticket` |
| `kb <query>` | Search the knowledge base for matching solutions | `You > kb VPN connection timeout` |
| `history` | Print the full conversation history for the session | `You > history` |
| `quit` | Save the ticket and exit the CLI | `You > quit` |

### CLI Examples

**Example 1 — Hardware troubleshooting with pre-selected category:**

```bash
python -m src.it_helpdesk_bot --category 1
```

```
You > My laptop screen is flickering after the latest BIOS update

Bot > Screen flickering after a BIOS update can be caused by a
      display driver conflict. Try these steps:
      1. Roll back the BIOS update via your manufacturer's recovery tool.
      2. Update your GPU driver (Intel/NVIDIA/AMD) to the latest version.
      3. Check Display Settings → Advanced → Monitor → set the refresh
         rate to 60 Hz.
      Let me know if the issue persists after any of these steps.
```

**Example 2 — Knowledge base search:**

```bash
python -m src.it_helpdesk_bot --category 3
```

```
You > kb VPN connection timeout

╔══════════════════════════════════════════════════╗
║  Knowledge Base Results — "VPN connection timeout"║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  1. VPN Connection Timeout (Corporate)           ║
║     → Verify VPN gateway address in client config║
║     → Flush DNS: ipconfig /flushdns              ║
║     → Check firewall rules for UDP 500/4500      ║
║                                                  ║
║  2. VPN Split Tunneling Not Working              ║
║     → Enable split tunneling in VPN profile      ║
║     → Restart the VPN client service             ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

**Example 3 — View current ticket:**

```
You > ticket

┌────────────────────────────────────────────┐
│  Ticket #TKT-20250118-0042                 │
│  Category : Network                        │
│  Status   : Open                           │
│  Created  : 2025-01-18 09:14:33            │
│  Summary  : VPN connection timeout when    │
│             connecting to corporate network │
└────────────────────────────────────────────┘
```

---

## 🌐 Web UI

### Launch

```bash
streamlit run app.py
```

The Streamlit application opens at **`http://localhost:8501`** and provides two main tabs plus a configuration sidebar.

### Tab 1 — Chat

The **Chat** tab is the primary interface for multi-turn IT troubleshooting:

- **Multi-turn conversation** — maintains full conversation history so the bot can reference prior messages and provide contextual follow-ups.
- **Auto-ticket creation** — each conversation automatically generates a support ticket saved to `tickets.json`.
- **Category selection** — use the **sidebar dropdown** to pick from all 7 support categories before or during a session.
- **Streaming responses** — answers appear token-by-token for a responsive feel.

**Walkthrough:**

```
1. Select a category from the sidebar (e.g., "Security")
2. Type your issue in the chat input:
   "I received a suspicious email asking me to verify my credentials"
3. The bot responds with step-by-step guidance:
   → Do NOT click any links in the email
   → Forward it to security@company.com
   → Mark it as phishing in your email client
   → Change your password if you already clicked
4. Ask follow-up questions — the bot remembers context
5. A ticket is auto-created and visible in the sidebar
```

### Tab 2 — Knowledge Base

The **Knowledge Base** tab provides a searchable interface to the curated solution repository:

- **Search bar** — enter keywords like "printer offline" or "password policy."
- **Expandable solution cards** — results display as collapsible expanders, each showing the problem title, detailed solution steps, and related tags.
- **Category filtering** — narrow results by support category.

**Walkthrough:**

```
1. Switch to the "Knowledge Base" tab
2. Enter a search query: "email signature not showing"
3. Results appear as expandable cards:
   ▸ Email Signature Missing in Outlook
     → File → Options → Mail → Signatures
     → Ensure the correct signature is set for New Messages
     → Check if your organization enforces a signature policy via GPO
   ▸ Email Signature Formatting Lost on Mobile
     → Use plain-text signatures for mobile clients
     → Verify HTML rendering in your mobile mail app
4. Click any card to expand the full solution
```

### Sidebar

The sidebar is persistent across both tabs and contains:

| Element | Description |
|---------|-------------|
| **Category Selector** | Dropdown with all 7 categories — sets context for the AI |
| **Model Info** | Displays the active Ollama model (`gemma4`) |
| **Temperature Slider** | Adjust response creativity (0.0 = deterministic, 1.0 = creative) |
| **Ticket History** | Shows the **last 10 tickets** with ID, category, date, and status |
| **New Conversation** | Button to clear chat and start fresh |

---

## 🏗️ Architecture

### System Flow

```
┌──────────────────────────────────────────────────────────────────────┐
│                        IT HELPDESK BOT — ARCHITECTURE                │
│                                                                      │
│   ┌────────┐    ┌────────┐                                          │
│   │  User  │    │  User  │                                          │
│   │ (CLI)  │    │ (Web)  │                                          │
│   └───┬────┘    └───┬────┘                                          │
│       │             │                                                │
│       ▼             ▼                                                │
│   ┌────────────────────────┐                                        │
│   │    Interface Layer     │                                        │
│   │  CLI: __main__.py     │                                        │
│   │  Web: app.py          │                                        │
│   └──────────┬─────────────┘                                        │
│              │                                                       │
│              ▼                                                       │
│   ┌──────────────────────┐    ┌─────────────────────┐               │
│   │    Core Engine        │───▶│   Knowledge Base    │               │
│   │  get_response()       │    │ search_knowledge_   │               │
│   │  - user_message       │    │ base()              │               │
│   │  - history            │    │ get_solution_        │               │
│   │  - model              │    │ template()          │               │
│   │  - temperature        │    └─────────────────────┘               │
│   └──────────┬────────────┘                                          │
│              │                                                       │
│       ┌──────┴──────┐                                                │
│       ▼             ▼                                                │
│   ┌────────┐  ┌──────────┐                                          │
│   │ Ollama │  │ Ticket   │                                          │
│   │ Server │  │ Manager  │                                          │
│   │(gemma4)│  │save/load │                                          │
│   └────────┘  │_tickets()│                                          │
│               └──────────┘                                          │
│                    │                                                 │
│                    ▼                                                 │
│              ┌───────────┐                                          │
│              │tickets.json│                                          │
│              └───────────┘                                          │
└──────────────────────────────────────────────────────────────────────┘
```

### Step-by-Step Flow

1. **User Input** — The user describes an IT issue via the CLI or the Streamlit web interface.
2. **Category Context** — The selected support category (Hardware, Software, Network, etc.) is prepended to the system prompt to focus the AI's domain expertise.
3. **Knowledge Base Lookup** — `search_knowledge_base()` checks `knowledge_base.json` for pre-existing solutions matching the user's query keywords. Relevant hits are injected into the prompt as additional context.
4. **LLM Inference** — `get_response()` sends the enriched prompt, conversation history, model name, and temperature to the local Ollama server running `gemma4`.
5. **Response Delivery** — The AI's response is streamed back to the user interface (CLI prints line-by-line; Streamlit renders token-by-token).
6. **Ticket Persistence** — `save_ticket()` serializes the conversation, category, timestamp, and auto-generated ticket ID to `tickets.json`.
7. **History Update** — The conversation history list is appended so follow-up questions maintain full context.

### Project Structure

```
02-it-helpdesk-bot/
├── app.py                      # Streamlit web application entry point
├── config.yaml                 # Model, temperature, and storage configuration
├── knowledge_base.json         # Curated IT solutions database
├── tickets.json                # Auto-generated ticket storage (created at runtime)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── LICENSE                     # MIT License
├── tests/
│   ├── __init__.py
│   ├── test_core.py            # Tests for get_response()
│   ├── test_utils.py           # Tests for ticket and KB utilities
│   └── test_cli.py             # Tests for CLI argument parsing
└── src/
    └── it_helpdesk_bot/
        ├── __init__.py         # Package init — exports public API
        ├── __main__.py         # CLI entry point (python -m src.it_helpdesk_bot)
        ├── core.py             # get_response() — main LLM interaction
        ├── utils.py            # save_ticket(), load_tickets(),
        │                       # search_knowledge_base(), get_solution_template()
        └── config.py           # Configuration loader (reads config.yaml)
```

---

## 📖 API Reference

All public functions are importable from `src.it_helpdesk_bot`.

---

### `get_response(user_message, history, model, temperature)`

The core response generator. Sends the user's message and conversation history to the Ollama LLM and returns the AI's reply.

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `user_message` | `str` | *required* | The user's current input message |
| `history` | `list[dict]` | *required* | Conversation history — list of `{"role": "user"|"assistant", "content": "..."}` dicts |
| `model` | `str` | `"gemma4"` | Ollama model name to use for inference |
| `temperature` | `float` | `0.7` | Sampling temperature (0.0–1.0) |

**Returns:** `str` — The AI-generated response text.

**Example:**

```python
from src.it_helpdesk_bot.core import get_response

history = []
user_msg = "My laptop won't connect to the office Wi-Fi"

response = get_response(
    user_message=user_msg,
    history=history,
    model="gemma4",
    temperature=0.7
)

print(response)
# → "Let's troubleshoot your Wi-Fi connectivity issue..."

# Update history for multi-turn
history.append({"role": "user", "content": user_msg})
history.append({"role": "assistant", "content": response})

# Follow-up question
follow_up = get_response(
    user_message="I already tried forgetting the network",
    history=history,
    model="gemma4",
    temperature=0.7
)
print(follow_up)
# → "Since you've already forgotten the network, let's try..."
```

---

### `save_ticket(ticket)`

Persists a support ticket to `tickets.json`. Creates the file if it does not exist; appends to the existing array otherwise.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `ticket` | `dict` | Ticket dictionary with keys: `id`, `category`, `timestamp`, `messages`, `status` |

**Returns:** `None`

**Example:**

```python
from src.it_helpdesk_bot.utils import save_ticket
from datetime import datetime

ticket = {
    "id": "TKT-20250118-0042",
    "category": "Network",
    "timestamp": datetime.now().isoformat(),
    "messages": [
        {"role": "user", "content": "VPN keeps disconnecting"},
        {"role": "assistant", "content": "Let's check your VPN client logs..."}
    ],
    "status": "open"
}

save_ticket(ticket)
# → Ticket appended to tickets.json
```

---

### `load_tickets()`

Loads all tickets from `tickets.json` and returns them as a list.

**Parameters:** None

**Returns:** `list[dict]` — List of all stored ticket dictionaries. Returns an empty list if the file does not exist.

**Example:**

```python
from src.it_helpdesk_bot.utils import load_tickets

tickets = load_tickets()

print(f"Total tickets: {len(tickets)}")
# → Total tickets: 42

# Get the last 10 tickets (as shown in the Web UI sidebar)
recent = tickets[-10:]
for t in recent:
    print(f"{t['id']}  {t['category']:10s}  {t['status']}")
# → TKT-20250118-0033  Security    resolved
# → TKT-20250118-0034  Email       open
# → ...
```

---

### `search_knowledge_base(query)`

Searches `knowledge_base.json` for solutions matching the given query string. Uses keyword matching against solution titles, descriptions, and tags.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | `str` | Search query — keywords describing the IT issue |

**Returns:** `list[dict]` — List of matching knowledge base entries, each containing `title`, `solution`, `category`, and `tags`.

**Example:**

```python
from src.it_helpdesk_bot.utils import search_knowledge_base

results = search_knowledge_base("printer offline")

for entry in results:
    print(f"📄 {entry['title']}")
    print(f"   Category: {entry['category']}")
    print(f"   Solution: {entry['solution'][:100]}...")
    print()
# → 📄 Printer Shows Offline Status
# →    Category: Printer
# →    Solution: 1. Open Settings → Devices → Printers & Scanners.
# →              2. Select the printer → Open queue → Printer menu...
```

---

### `get_solution_template(category)`

Returns a structured solution template string for the specified support category. Used internally to format consistent responses.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `category` | `str` | One of: `Hardware`, `Software`, `Network`, `Security`, `Email`, `Printer`, `General` |

**Returns:** `str` — A formatted template string with diagnostic steps and resolution structure for the given category.

**Example:**

```python
from src.it_helpdesk_bot.utils import get_solution_template

template = get_solution_template("Security")
print(template)
# → **Security Issue — Diagnostic Template**
# →
# → 1. Identify the threat type (phishing, malware, unauthorized access)
# → 2. Isolate the affected system if compromise is suspected
# → 3. Verify with security logs and endpoint protection alerts
# → 4. Escalate to the security operations team if needed
# → 5. Document actions taken and update the ticket status
```

---

## ⚙️ Configuration

All configuration is managed through `config.yaml` in the project root.

### Full `config.yaml` Reference

```yaml
# ============================================================
# IT Helpdesk Bot — Configuration
# ============================================================

# --- LLM Model Settings ---
model: gemma4                   # Ollama model name. Alternatives: llama3, mistral, phi3
temperature: 0.7                # Response creativity: 0.0 = deterministic, 1.0 = creative
                                # Recommended: 0.3–0.5 for factual IT support,
                                #              0.7–0.9 for conversational tone

# --- Ticket Storage ---
tickets:
  storage_file: tickets.json    # Path to the ticket persistence file
                                # Created automatically on first ticket save
                                # Supports relative or absolute paths

# --- Knowledge Base ---
knowledge_base:
  file: knowledge_base.json     # Path to the curated solutions database
                                # JSON array of objects with: title, solution,
                                # category, tags

# --- Support Categories ---
# These are the 7 built-in categories (not user-configurable via YAML
# but listed here for reference):
#   1. Hardware   — Physical device issues
#   2. Software   — Application and OS issues
#   3. Network    — Connectivity and infrastructure
#   4. Security   — Threats, compliance, access control
#   5. Email      — Mail client and server issues
#   6. Printer    — Print devices and drivers
#   7. General    — Catch-all for uncategorized requests
```

### Environment Variables

You can override configuration values using environment variables:

| Variable | Overrides | Example |
|----------|-----------|---------|
| `OLLAMA_HOST` | Ollama server address | `http://192.168.1.50:11434` |
| `HELPDESK_MODEL` | `model` in config.yaml | `llama3` |
| `HELPDESK_TEMPERATURE` | `temperature` in config.yaml | `0.5` |
| `HELPDESK_TICKETS_FILE` | `tickets.storage_file` | `data/tickets.json` |
| `HELPDESK_KB_FILE` | `knowledge_base.file` | `data/kb.json` |

**Example — use a remote Ollama server with a different model:**

```bash
export OLLAMA_HOST=http://gpu-server.local:11434
export HELPDESK_MODEL=llama3
python -m src.it_helpdesk_bot --category 4
```

---

## 🧪 Testing

### Run All Tests

```bash
python -m pytest tests/ -v
```

### Run by Test Module

```bash
# Core engine tests (get_response)
python -m pytest tests/test_core.py -v

# Utility function tests (tickets, knowledge base)
python -m pytest tests/test_utils.py -v

# CLI argument parsing tests
python -m pytest tests/test_cli.py -v
```

### Test Categories

| Module | Tests | What It Covers |
|--------|-------|----------------|
| `test_core.py` | `get_response()` behavior | Verifies response generation, history handling, model parameter forwarding, and error cases when Ollama is unavailable |
| `test_utils.py` | Ticket & KB utilities | `save_ticket()` persistence, `load_tickets()` round-trip, `search_knowledge_base()` keyword matching, `get_solution_template()` output format |
| `test_cli.py` | CLI entry point | `--category` flag parsing (valid 1–7, invalid values), interactive command routing (`new`, `ticket`, `kb`, `history`, `quit`) |

### Test with Coverage

```bash
python -m pytest tests/ -v --cov=src/it_helpdesk_bot --cov-report=term-missing
```

**Expected output:**

```
Name                                Stmts   Miss  Cover   Missing
-----------------------------------------------------------------
src/it_helpdesk_bot/__init__.py         4      0   100%
src/it_helpdesk_bot/__main__.py        38      3    92%   71-73
src/it_helpdesk_bot/core.py            25      2    92%   44-45
src/it_helpdesk_bot/utils.py           52      4    92%   88-91
src/it_helpdesk_bot/config.py          18      1    94%   31
-----------------------------------------------------------------
TOTAL                                 137     10    93%
```

---

## ⚖️ Local LLM vs Cloud AI

A key design decision of this project is running the LLM **entirely locally** via Ollama. Here's how it compares to cloud-based alternatives:

| Dimension | 🏠 Local LLM (This Project) | ☁️ Cloud AI (OpenAI, Azure, etc.) |
|-----------|------------------------------|-------------------------------------|
| **Data Privacy** | ✅ All data stays on your machine — zero external transmission | ⚠️ Data sent to third-party servers; requires DPA agreements |
| **Cost** | ✅ Free after hardware investment — no per-token charges | 💰 Pay-per-use: $0.002–$0.06 per 1K tokens depending on model |
| **Latency** | ✅ Sub-second on modern GPUs; 1–3s on CPU-only | ⚠️ 0.5–5s typical; spikes during high demand |
| **Internet Required** | ✅ No — works fully offline after model download | ❌ Requires stable internet connection |
| **Model Quality** | ⚠️ Good for IT support tasks; smaller parameter count | ✅ State-of-the-art models with very large parameter counts |
| **Customization** | ✅ Full control — fine-tune, quantize, swap models freely | ⚠️ Limited to provider's model catalog and fine-tuning APIs |
| **Compliance** | ✅ Ideal for GDPR, HIPAA, SOC 2 — data never leaves premises | ⚠️ Requires vendor compliance certifications and legal review |
| **Setup Complexity** | ⚠️ Requires Ollama install + model download (~2–8 GB) | ✅ API key and a few lines of code |
| **Scalability** | ⚠️ Limited by local hardware (GPU VRAM, CPU cores) | ✅ Virtually unlimited — auto-scales with demand |
| **Maintenance** | ⚠️ Self-managed: model updates, server uptime, hardware | ✅ Fully managed by the provider |

**Bottom line:** For internal IT helpdesk scenarios handling sensitive employee data, the local LLM approach provides the best balance of privacy, cost, and capability.

---

## ❓ FAQ

<details>
<summary><strong>1. What support categories are available, and can I add my own?</strong></summary>

The bot ships with **7 built-in categories**: Hardware, Software, Network, Security, Email, Printer, and General. These cover the vast majority of L1/L2 IT support scenarios.

To add a custom category:
1. Update the category list in `src/it_helpdesk_bot/core.py`.
2. Add a corresponding solution template in `get_solution_template()` inside `src/it_helpdesk_bot/utils.py`.
3. Populate `knowledge_base.json` with entries tagged under your new category.
4. Update the `--category` flag range in `src/it_helpdesk_bot/__main__.py`.

</details>

<details>
<summary><strong>2. Where are tickets stored, and can I use a database instead of JSON?</strong></summary>

Tickets are stored in `tickets.json` (configurable via `config.yaml` → `tickets.storage_file`). The file is a JSON array where each element is a ticket object with `id`, `category`, `timestamp`, `messages`, and `status`.

To switch to a database:
- Replace the `save_ticket()` and `load_tickets()` functions in `src/it_helpdesk_bot/utils.py` with your preferred DB connector (SQLite, PostgreSQL, etc.).
- The rest of the application is storage-agnostic — it only interacts with tickets through these two functions.

</details>

<details>
<summary><strong>3. How do I customize the knowledge base?</strong></summary>

Edit `knowledge_base.json` in the project root. Each entry follows this schema:

```json
{
  "title": "Printer Shows Offline Status",
  "category": "Printer",
  "tags": ["printer", "offline", "status", "spooler"],
  "solution": "1. Open Settings → Devices → Printers & Scanners.\n2. Select the printer → Open queue.\n3. Printer menu → uncheck 'Use Printer Offline'.\n4. Restart the Print Spooler service: services.msc → Print Spooler → Restart."
}
```

Add as many entries as needed. The `search_knowledge_base()` function matches against `title`, `solution`, and `tags` fields using keyword search.

</details>

<details>
<summary><strong>4. Does the bot support multiple users simultaneously?</strong></summary>

- **CLI mode:** Each CLI session is independent. Multiple users can run separate instances of `python -m src.it_helpdesk_bot` concurrently. Ticket writes are append-only, so concurrent file access is generally safe for low-volume usage.
- **Web UI mode:** Streamlit natively supports multiple browser sessions. Each user gets an isolated session state with their own conversation history. Tickets from all users are written to the same `tickets.json` file.

For high-concurrency production deployments, consider switching the ticket backend to a database (see FAQ #2).

</details>

<details>
<summary><strong>5. How can I improve the quality of AI responses?</strong></summary>

Several strategies can improve response quality:

1. **Lower the temperature** — Set `temperature: 0.3` in `config.yaml` for more focused, deterministic answers.
2. **Enrich the knowledge base** — The more curated solutions you add to `knowledge_base.json`, the better the bot's context for answering common issues.
3. **Use a larger model** — Swap `gemma4` for a larger model like `llama3` or `mistral` if your hardware supports it. Update the `model` field in `config.yaml`.
4. **Provide detailed descriptions** — Encourage users to describe symptoms in detail. "Outlook crashes when I open PDFs in emails" is far more actionable than "Outlook broken."
5. **Use multi-turn conversations** — Follow-up questions allow the bot to narrow down the root cause with conversation context.

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository on GitHub.
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** and add tests where appropriate.
4. **Run the test suite** to verify nothing is broken:
   ```bash
   python -m pytest tests/ -v
   ```
5. **Commit** with a descriptive message:
   ```bash
   git commit -m "feat: add custom category support"
   ```
6. **Push** and open a **Pull Request** against `main`:
   ```bash
   git push origin feature/your-feature-name
   ```

### Guidelines

- Follow existing code style and patterns.
- Add tests for new functionality.
- Update this README if your changes affect usage or configuration.
- Keep PRs focused — one feature or fix per PR.

---

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

---

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:003459,100:00b4d8&height=120&section=footer">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:003459,100:00b4d8&height=120&section=footer" width="100%" alt="Footer">
</picture>

**Built with ❤️ using [Ollama](https://ollama.com/) and [Streamlit](https://streamlit.io/)**

[⬆ Back to Top](#-table-of-contents)

</div>
