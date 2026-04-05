<div align="center">
<img src="https://img.shields.io/badge/✍️_📰_Newsletter_Editor-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
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

## 🌟 Features

| Feature | Description |
|---------|-------------|
| 📝 **Smart Content Curation** | AI transforms raw notes into polished newsletter sections |
| 📋 **Section Templates** | 6 built-in templates: News Roundup, Deep Dive, Tips & Tricks, Spotlight, Events, Q&A |
| 👥 **Subscriber Segmentation** | Target content for All, New, Premium, or Inactive subscribers |
| 🗄️ **Archive Management** | Automatic archiving with browsable history |
| 🌐 **HTML Export** | Professional styled HTML output for email delivery |
| 🎨 **Multiple Tones** | Informative, casual, witty, formal, or friendly writing styles |
| 💻 **Dual Interface** | Full CLI + Streamlit Web UI |
| ⚙️ **YAML Configuration** | Flexible config management |
| 📊 **Rich Terminal UI** | Beautiful CLI output with Rich library |

## 🏗️ Architecture

```
36-newsletter-editor/
├── src/
│   └── newsletter_editor/
│       ├── __init__.py          # Package metadata
│       ├── core.py              # Business logic, templates, segmentation
│       ├── cli.py               # Click CLI with subcommands
│       └── web_ui.py            # Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core logic tests
│   └── test_cli.py              # CLI integration tests
├── config.yaml                  # Configuration file
├── setup.py                     # Package setup
├── Makefile                     # Build & run commands
├── .env.example                 # Environment template
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

## 📦 Installation

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai/) running locally with a model pulled

### Quick Start

```bash
# Install the package
make install

# Or install with dev dependencies
make dev

# Or manual install
pip install -e .
```

## 🖥️ CLI Usage

The CLI provides subcommands for all functionality:

### Generate a Newsletter

```bash
# Basic generation
newsletter-editor generate --input notes.txt --name "Tech Weekly"

# With template and segment
newsletter-editor generate \
  --input notes.txt \
  --name "Tech Weekly" \
  --sections 6 \
  --tone witty \
  --template deep_dive \
  --segment premium \
  --html \
  -o output.md

# Without archiving
newsletter-editor generate --input notes.txt --name "Quick Update" --no-archive
```

### List Templates

```bash
newsletter-editor templates
```

### List Subscriber Segments

```bash
newsletter-editor segments
```

### Browse Archive

```bash
newsletter-editor archive
```

### Global Options

```bash
newsletter-editor --config custom-config.yaml --verbose generate ...
```

### Input File Format

Create a text file with your raw notes:
```
AI news: GPT-5 released with major improvements
New NVIDIA chip boosts training 2x
Python 3.13 out with performance gains
React 19 now stable - new hooks API
https://example.com/ai-news
```

## 🌐 Web UI

Launch the interactive Streamlit interface:

```bash
make run-web
# or
streamlit run src/newsletter_editor/web_ui.py
```

### Web UI Features

| Tab | Description |
|-----|-------------|
| ✍️ **Section Builder** | Input content, configure settings, generate newsletter |
| 👁️ **Preview** | Live rendered preview of your newsletter |
| 📋 **Template Selector** | Browse and learn about section templates |
| 📤 **Export** | Download as Markdown/HTML, manage archive |

## ⚙️ Configuration

Edit `config.yaml` to customize behavior:

```yaml
llm:
  temperature: 0.7        # Creativity level (0.0-1.0)
  max_tokens: 4096         # Max output length

newsletter:
  default_sections: 4
  default_tone: "informative"
  supported_tones:
    - informative
    - casual
    - witty
    - formal
    - friendly

export:
  output_dir: "output"
  archive_dir: "archive"
```

## 🧪 Testing

```bash
# Run all tests
make test

# With coverage
python -m pytest tests/ -v --cov=newsletter_editor
```

## 🔧 Development

```bash
# Install dev dependencies
make dev

# Run linting
make lint

# Clean build artifacts
make clean
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

This project is part of the [90 Local LLM Projects](../../README.md) collection.
