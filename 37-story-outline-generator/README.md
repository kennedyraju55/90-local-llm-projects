<div align="center">
<img src="https://img.shields.io/badge/✍️_📖_Story_Outline_Generator-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
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
| 📖 **Full Story Outlines** | Generate complete outlines with chapters, characters, and plot arcs |
| 🧑 **Character Profiles** | Deep character development with 6 archetypes (Hero, Mentor, Shadow, etc.) |
| 📈 **Plot Arc Visualization** | Visual tension curves for 4 structures (Three-Act, Hero's Journey, Five-Act, Save the Cat) |
| 📚 **Chapter-by-Chapter Breakdown** | Detailed chapter plans with POV, events, emotional beats, cliffhangers |
| 🌍 **Worldbuilding** | Geography, politics, culture, technology, history, economy |
| 🎭 **8 Genre Support** | Sci-fi, fantasy, mystery, thriller, romance, horror, literary, historical |
| 💻 **Dual Interface** | Full CLI + Streamlit Web UI |
| ⚙️ **YAML Configuration** | Flexible config management |

## 🏗️ Architecture

```
37-story-outline-generator/
├── src/
│   └── story_gen/
│       ├── __init__.py          # Package metadata
│       ├── core.py              # Business logic, archetypes, structures
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
```

## 📦 Installation

```bash
# Install the package
make install

# Or with dev dependencies
make dev
```

## 🖥️ CLI Usage

### Generate an Outline

```bash
# Basic
story-gen generate --genre sci-fi --premise "AI awakens on a space station"

# Advanced
story-gen generate --genre fantasy --premise "dragons return" \
  --chapters 15 --characters 6 \
  --structure heros_journey --worldbuilding \
  -o outline.md
```

### Character Profiles

```bash
story-gen character --name "Ada Chen" --role protagonist --genre sci-fi --archetype hero
```

### List Archetypes & Structures

```bash
story-gen archetypes
story-gen structures
```

## 🌐 Web UI

```bash
make run-web
# or
streamlit run src/story_gen/web_ui.py
```

### Web UI Tabs

| Tab | Description |
|-----|-------------|
| 🎬 **Genre & Premise** | Input story concept, configure settings, generate outline |
| 🧑 **Character Cards** | Generate character profiles with archetype selection |
| 📈 **Plot Arc** | Visualize tension curves for different structures |
| 📚 **Chapters** | View chapter breakdown, download outline |

## ⚙️ Configuration

```yaml
llm:
  temperature: 0.8
  max_tokens: 4096

story:
  default_chapters: 10
  default_characters: 4
  genres: [sci-fi, fantasy, mystery, thriller, romance, horror, literary, historical]
```

## 🧪 Testing

```bash
make test
python -m pytest tests/ -v --cov=story_gen
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

Part of the [90 Local LLM Projects](../../README.md) collection.
