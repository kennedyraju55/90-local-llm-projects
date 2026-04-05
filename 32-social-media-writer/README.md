<div align="center">
<img src="https://img.shields.io/badge/✍️_📱_Social_Media_Writer-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
<br/>
<img src="https://img.shields.io/badge/Gemma_4-Ollama-orange?style=flat-square&logo=google&logoColor=white" alt="Gemma 4"/>
<img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/Streamlit-Web_UI-red?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit"/>
<img src="https://img.shields.io/badge/Click-CLI-green?style=flat-square&logo=gnu-bash&logoColor=white" alt="Click CLI"/>
<img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License"/>
<br/><br/>
<strong>Part of <a href="https://github.com/kennedyraju55/90-local-llm-projects">90 Local LLM Projects</a> collection</strong>
</div>
<br/>

> 🚀 Create platform-specific, engagement-optimized social media posts using a local LLM via Ollama.

---

## 📋 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [CLI Usage](#-cli-usage)
- [Web UI](#-web-ui)
- [Configuration](#-configuration)
- [Platform Previews](#-platform-previews)
- [Testing](#-testing)
- [Project Structure](#-project-structure)

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 🐦 **Multi-Platform** | Twitter/X, LinkedIn, and Instagram with platform-specific formatting |
| 🎨 **Tone Control** | Professional, casual, excited, informative, or humorous |
| 📊 **A/B Testing** | Generate distinct variants with different messaging strategies |
| #️⃣ **Smart Hashtags** | AI-generated, platform-optimized hashtag suggestions |
| 📅 **Scheduling** | Best posting times for each platform |
| ✅ **Validation** | Character count validation with reach score estimation |
| 🌐 **Web UI** | Beautiful Streamlit interface with platform-mimicking previews |
| 📋 **Copy-Ready** | One-click copy for all generated content |
| 📝 **Configurable** | YAML-based configuration for all settings |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Social Media Writer                    │
├──────────────┬──────────────┬───────────────────────────┤
│   CLI (click)│  Web (Streamlit)                         │
│   cli.py     │  web_ui.py   │                           │
├──────────────┴──────────────┤                           │
│         Core Engine         │      config.yaml          │
│         core.py             │      (settings)           │
├─────────────────────────────┤                           │
│    common.llm_client        │                           │
│    (Ollama API)             │                           │
├─────────────────────────────┤                           │
│    Ollama + LLM Model       │                           │
└─────────────────────────────┴───────────────────────────┘
```

---

## 📦 Prerequisites

- **Python 3.10+**
- **[Ollama](https://ollama.ai/)** running locally with a model (e.g., `llama3`, `gemma4`)
- The `common/` shared module from the parent project

---

## 🔧 Installation

```bash
# Clone and navigate to project
cd 32-social-media-writer

# Install dependencies
pip install -r requirements.txt

# Install as editable package
pip install -e .

# Or use Make
make install
```

### Environment Setup

```bash
# Copy and edit environment config
cp .env.example .env
```

---

## 💻 CLI Usage

### Basic Commands

```bash
# Generate Twitter posts
social-writer --platform twitter --topic "AI revolution" --tone excited

# LinkedIn post with 3 variants
social-writer --platform linkedin --topic "hiring update" --tone professional --variants 3

# Instagram post saved to file
social-writer --platform instagram --topic "behind the scenes" --tone humorous -o post.txt

# Or run directly
python src/social_writer/cli.py --platform twitter --topic "product launch"
```

### Advanced Flags

```bash
# 🔬 A/B test variants with different approaches
social-writer --platform twitter --topic "new feature" --ab-test

# #️⃣ Generate standalone hashtag suggestions
social-writer --platform instagram --topic "travel photography" --hashtags

# 📅 Show best posting times
social-writer --platform linkedin --topic "career tips" --schedule

# 🌐 Generate for ALL platforms at once
social-writer --all-platforms --topic "product launch" --tone excited
```

### CLI Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--platform` | Target platform: `twitter` / `linkedin` / `instagram` | — |
| `--topic` | Post topic (required) | — |
| `--tone` | Writing tone | `professional` |
| `--variants` | Number of post variants | `2` |
| `-o, --output` | Save output to file | `None` |
| `--hashtags` | Generate standalone hashtag suggestions | `False` |
| `--schedule` | Show best posting times for platform | `False` |
| `--ab-test` | Generate A/B test variants | `False` |
| `--all-platforms` | Generate for all platforms at once | `False` |

---

## 🌐 Web UI

Launch the Streamlit-based web interface:

```bash
streamlit run src/social_writer/web_ui.py

# Or use Make
make web
```

### Web UI Features

- **📑 Platform Tabs** — Dedicated tabs for Twitter/X, LinkedIn, and Instagram
- **🎛️ Sidebar Controls** — Topic input, tone selector, variant slider
- **📱 Platform Preview Cards:**
  - 🐦 **Twitter**: Dark theme card with character count bar (green/yellow/red)
  - 💼 **LinkedIn**: Professional white card with company-style formatting
  - 📸 **Instagram**: Gradient-styled card with image placeholder and hashtag cloud
- **📊 Metrics Dashboard** — Character count, validity, hashtags, reach score
- **📋 Copy-to-Clipboard** — `st.code` blocks for easy copying
- **🔬 A/B Comparison** — Side-by-side variant display
- **#️⃣ Hashtag Generator** — Dedicated hashtag suggestion mode
- **📅 Posting Schedule** — Best times displayed per platform

---

## ⚙️ Configuration

All settings are managed via `config.yaml`:

```yaml
app:
  name: "Social Media Writer"
  version: "2.0.0"

llm:
  model: "llama3"        # Ollama model to use
  temperature: 0.8       # Creativity level (0.0-1.0)
  max_tokens: 2048       # Max response length

platforms:
  twitter:
    max_chars: 280
    name: "Twitter/X"
    hashtag_count: 3
    best_times: ["9:00 AM", "12:00 PM", "5:00 PM"]
  linkedin:
    max_chars: 3000
    name: "LinkedIn"
    hashtag_count: 5
    best_times: ["7:30 AM", "12:00 PM", "5:30 PM"]
  instagram:
    max_chars: 2200
    name: "Instagram"
    hashtag_count: 15
    best_times: ["11:00 AM", "2:00 PM", "7:00 PM"]

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OLLAMA_HOST` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_MODEL` | LLM model name | `llama3` |
| `LOG_LEVEL` | Logging verbosity | `INFO` |

---

## 📱 Platform Previews

### 🐦 Twitter/X Preview
- Compact, dark-themed card matching Twitter's UI
- Real-time character counter with color-coded bar:
  - 🟢 Green: Under 80% of limit
  - 🟡 Yellow: 80-100% of limit
  - 🔴 Red: Over limit
- Punchy, concise formatting with inline hashtags

### 💼 LinkedIn Preview
- Professional white card with avatar and title
- Content formatted with paragraphs and line breaks
- Call-to-action optimized structure
- Business-appropriate hashtag placement

### 📸 Instagram Preview
- Gradient-styled card with image placeholder
- Emoji-enriched content formatting
- Hashtag cloud visualization
- Separated hashtag block (content → dots → hashtags)

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --tb=short --cov=social_writer

# Run specific test file
pytest tests/test_core.py -v
pytest tests/test_cli.py -v

# Or use Make
make test
```

---

## 📁 Project Structure

```
32-social-media-writer/
├── src/
│   └── social_writer/
│       ├── __init__.py        # Package init with version
│       ├── core.py            # Core logic: generation, validation, formatting
│       ├── cli.py             # Click-based CLI interface
│       └── web_ui.py          # Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Pytest config (path setup)
│   ├── test_core.py           # Core module tests
│   └── test_cli.py            # CLI tests
├── config.yaml                # Application configuration
├── setup.py                   # Package setup with entry points
├── requirements.txt           # Python dependencies
├── Makefile                   # Common dev commands
├── .env.example               # Environment variable template
└── README.md                  # This file
```

## 📸 Screenshots
<div align="center">
<table>
<tr>
<td><img src="https://via.placeholder.com/400x250/1a1a2e/e94560?text=CLI+Interface" alt="CLI"/></td>
<td><img src="https://via.placeholder.com/400x250/16213e/e94560?text=Web+UI" alt="Web UI"/></td>
</tr>
<tr><td align="center"><em>CLI Interface</em></td><td align="center"><em>Streamlit Web UI</em></td></tr>
</table>
</div>

## 📄 License

Part of the [90 Local LLM Projects](../) collection.
