<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://img.shields.io/badge/%F0%9F%94%A4_REGEX_GENERATOR-AI--Powered_Patterns-10b981?style=for-the-badge&labelColor=0d1117">
  <img alt="Regex Generator" src="https://img.shields.io/badge/%F0%9F%94%A4_REGEX_GENERATOR-AI--Powered_Patterns-059669?style=for-the-badge">
</picture>

<br/>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 120" width="600" height="120">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#059669;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="600" height="120" rx="16" fill="#0d1117"/>
  <text x="300" y="55" text-anchor="middle" font-family="Segoe UI,Arial" font-size="36" font-weight="bold" fill="url(#grad1)">🔤 Regex Generator</text>
  <text x="300" y="90" text-anchor="middle" font-family="Segoe UI,Arial" font-size="16" fill="#8b949e">Pattern Library • Live Tester • Multi-Flavor</text>
</svg>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat-square)](https://ollama.ai)
[![Gemma](https://img.shields.io/badge/Gemma_4-Google_AI-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)

*Generate regex from natural language, explain patterns, test live, browse a pattern library — all with multi-flavor support. Powered by local Gemma 4 LLM via Ollama.*

</div>

---

## 🏗️ Architecture

```mermaid
graph LR
    A[Natural Language] -->|generate| B[Regex Engine]
    C[Regex Pattern] -->|explain| B
    D[Pattern + Strings] -->|test| B
    B --> E[Ollama / Gemma 4]
    B --> F[Pattern Library]
    B --> G[Regex Validator]
    E --> H[Rich Output / Streamlit]
    F --> H
    G --> H
```

```
┌──────────────┐     ┌───────────────┐     ┌─────────────┐
│  CLI / Web   │────▶│  Core Engine   │────▶│  Ollama API │
│  • generate  │     │  • generate    │     │  (Gemma 4)  │
│  • explain   │     │  • explain     │     └─────────────┘
│  • test      │     │  • validate    │
│  • library   │     │  • library     │
└──────────────┘     └───────────────┘
                            │
                     ┌──────▼──────┐
                     │  Utilities  │
                     │  • test     │
                     │  • validate │
                     │  • extract  │
                     │  • highlight│
                     └─────────────┘
```

## ✨ Features

| Feature | Description |
|---------|-------------|
| ✨ **Natural Language → Regex** | Describe what you want to match, get a working pattern |
| 📖 **Pattern Explanation** | Component-by-component breakdown of any regex |
| 🧪 **Live Regex Tester** | Test patterns against strings with match highlighting |
| 📚 **Pattern Library** | 12+ pre-built patterns (email, URL, IP, phone, UUID, etc.) |
| 🌐 **Multi-Flavor Support** | Python, JavaScript, PCRE, POSIX, Java, .NET, Go, Rust |
| ✅ **Pattern Validation** | Instant validation with group count and error details |
| 🔍 **Match Extraction** | See all matches, groups, and positions |
| 🌐 **Streamlit Web UI** | Interactive web interface with generate, explain, and test tabs |
| ⚙️ **YAML Configuration** | Flexible config with environment variable overrides |
| 🎨 **Rich Terminal** | Beautiful colored CLI output with tables |

## 📸 Screenshots

<div align="center">

| Generate | Explain |
|:---:|:---:|
| ![Generate](https://placehold.co/400x300/0d1117/10b981?text=Regex+Generate) | ![Explain](https://placehold.co/400x300/0d1117/4488ff?text=Regex+Explain) |

| Test | Web UI |
|:---:|:---:|
| ![Test](https://placehold.co/400x300/0d1117/ffcc00?text=Live+Tester) | ![Web](https://placehold.co/400x300/0d1117/FF4B4B?text=Streamlit+UI) |

</div>

## 📦 Installation

```bash
cd 24-regex-generator
pip install -r requirements.txt
pip install -e .

ollama serve && ollama pull gemma4
```

## 🚀 CLI Usage

```bash
# Generate from natural language
python -m regex_gen.cli generate "email addresses"
python -m regex_gen.cli generate "US phone numbers" --flavor javascript

# Generate and test
python -m regex_gen.cli generate "IPv4 addresses" -t "192.168.1.1" -t "invalid"

# Explain a pattern
python -m regex_gen.cli explain "[a-z]+@[a-z]+\.[a-z]{2,}"

# Test a pattern
python -m regex_gen.cli test "\d{3}-\d{4}" "555-1234" "hello" "123-4567"

# Browse pattern library
python -m regex_gen.cli library
python -m regex_gen.cli library email
```

## 🌐 Web UI Usage

```bash
streamlit run src/regex_gen/web_ui.py
# Open http://localhost:8501
```

## 📋 Example Output

```
╭──────────────────────────────────────────────╮
│  🔤 Regex Generator                          │
│  Generate regex from natural language         │
╰──────────────────────────────────────────────╯

Description: "email addresses"
Flavor: python

╭── 🎯 Generated Regex ───────────────────────╮
│ Pattern: [a-zA-Z0-9._%+-]+@[a-z.-]+\.[a-z]+ │
│                                              │
│ Components:                                  │
│ • [a-zA-Z0-9._%+-]+ - Username part         │
│ • @                  - Literal at symbol     │
│ • [a-z.-]+           - Domain name           │
│ • \.[a-z]+           - TLD extension         │
╰──────────────────────────────────────────────╯

┌──────── Pattern: \S+@\S+\.\S+ ──────────────┐
│ String          │ Matches │ Match Text       │
│ user@example.co │ ✅      │ user@example.co  │
│ invalid         │ ❌      │ -                │
└──────────────────────────────────────────────┘
```

## 🧪 Testing

```bash
python -m pytest tests/ -v
python -m pytest tests/ -v --cov=src/regex_gen --cov-report=term-missing
```

## 📁 Project Structure

```
24-regex-generator/
├── src/regex_gen/
│   ├── __init__.py          # Package metadata
│   ├── core.py              # Generation, explanation, library
│   ├── cli.py               # Click CLI interface
│   ├── web_ui.py            # Streamlit web interface
│   ├── config.py            # Configuration & pattern library
│   └── utils.py             # Testing, validation, extraction
├── tests/
│   ├── __init__.py
│   ├── test_core.py         # Core logic tests
│   └── test_cli.py          # CLI tests
├── config.yaml              # Default configuration
├── setup.py                 # Package setup
├── requirements.txt         # Dependencies
├── Makefile                 # Dev commands
├── .env.example             # Environment template
└── README.md                # This file
```

## ⚙️ Configuration

```yaml
model: "gemma4"
temperature: 0.3
max_tokens: 2048
default_flavor: "python"
```

## 🤝 Contributing

1. Fork → Branch → Commit → Push → PR

## 📄 License

Part of [90 Local LLM Projects](../README.md). See root [LICENSE](../LICENSE).

## ⚙️ Requirements

- Python 3.10+
- Ollama running locally with Gemma 4 model
