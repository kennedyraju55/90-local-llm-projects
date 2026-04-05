<div align="center">
<img src="https://img.shields.io/badge/✍️_📊_Presentation_Generator-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
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

## Features

| Feature | Description |
|---------|-------------|
| 4 Presentation Formats | Standard, Pecha Kucha (20x20), Lightning Talk, Keynote |
| 9 Slide Templates | Title, Agenda, Content, Data, Quote, Comparison, Timeline, Q&A, Closing |
| Speaker Notes | Conversational speaker notes for each slide |
| Visual Suggestions | AI-recommended charts, diagrams, and images per slide |
| Timing Estimates | Per-slide and total presentation timing with visual bar |
| Markdown Export | Clean markdown export for easy conversion |
| Dual Interface | Full CLI + Streamlit Web UI |
| YAML Configuration | Flexible config management |

## Architecture

`
39-presentation-generator/
├── src/
│   └── presentation_gen/
│       ├── __init__.py          # Package metadata
│       ├── core.py              # Business logic, formats, templates, timing
│       ├── cli.py               # Click CLI with subcommands
│       └── web_ui.py            # Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core logic tests
│   └── test_cli.py              # CLI tests
├── config.yaml                  # Configuration
├── setup.py                     # Package setup
├── Makefile                     # Build commands
├── .env.example                 # Environment template
├── requirements.txt             # Dependencies
└── README.md                    # Documentation
`

## Installation

`bash
make install    # or: pip install -e .
make dev        # with dev dependencies
`

## CLI Usage

### Generate a Presentation

`bash
# Basic
presentation-gen generate --topic "Machine Learning 101"

# Full options
presentation-gen generate \
  --topic "Machine Learning 101" \
  --slides 15 \
  --audience "beginners" \
  --format keynote \
  --notes-only \
  -o slides.md
`

### List Formats and Templates

`bash
presentation-gen formats
presentation-gen slide-types
`

### Estimate Timing

`bash
presentation-gen timing --slides 20 --format pecha-kucha
`

## Web UI

`bash
make run-web
`

| Tab | Description |
|-----|-------------|
| Topic Input | Enter topic, audience, format, slide count |
| Slide Cards | Expandable slide cards with notes |
| Timing | Visual timing bar with per-slide estimates |
| Download | Download full presentation or notes only |

## Configuration

`yaml
llm:
  temperature: 0.7
  max_tokens: 4096
presentation:
  default_slides: 12
  words_per_minute: 130
`

## Testing

`bash
make test
`

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

## License

Part of the [90 Local LLM Projects](../../README.md) collection.
