<div align="center">
<img src="https://img.shields.io/badge/✍️_📝_Blog_Post_Generator-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
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

> **Generate SEO-friendly blog posts** powered by a local LLM via Ollama. Features a rich CLI, Streamlit web UI, SEO scoring, tone analysis, and multi-draft generation.

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    Blog Post Generator                   │
├──────────────┬───────────────┬───────────────────────────┤
│   CLI (click)│  Web UI       │  Core Library             │
│   cli.py     │  (Streamlit)  │  core.py                  │
│              │  web_ui.py    │  ┌───────────────────────┐ │
│  --topic     │  Topic input  │  │ build_prompt()        │ │
│  --keywords  │  Keyword tags │  │ generate_blog_post()  │ │
│  --tone      │  Tone select  │  │ generate_outline()    │ │
│  --length    │  Length slider │  │ generate_multiple_    │ │
│  --drafts    │  Drafts slider│  │   drafts()            │ │
│  --outline   │  Generate btn │  │ score_seo()           │ │
│  --seo-report│  SEO gauge    │  │ analyze_tone()        │ │
│  --export-md │  Export btns  │  │ export_markdown()     │ │
│              │               │  │ BlogPost dataclass    │ │
│              │               │  └───────────────────────┘ │
├──────────────┴───────────────┴───────────────────────────┤
│              common/llm_client.py (Ollama)               │
└──────────────────────────────────────────────────────────┘
```

## ✨ Features

- 🤖 **Local LLM Powered** — Uses Ollama with any supported model (llama3, gemma4, etc.)
- 🔍 **SEO Scoring** — Automated 0-100 SEO analysis (keyword density, headings, meta, length)
- 🎨 **5 Writing Tones** — Professional, casual, technical, friendly, persuasive
- 📋 **Outline Preview** — Generate and review outlines before full posts
- 📄 **Multi-Draft** — Generate up to 5 alternative drafts with varying creativity
- 🎭 **Tone Analysis** — Heuristic analysis of generated content tone
- 📊 **Rich CLI Output** — Beautiful tables, spinners, and formatted markdown
- 🌐 **Streamlit Web UI** — Full-featured browser interface with history
- 💾 **Markdown Export** — Export with YAML frontmatter (title, date, keywords, SEO score)
- ⚙️ **Configurable** — YAML-based configuration with sensible defaults

## 📁 Project Structure

```
31-blog-post-generator/
├── src/
│   └── blog_gen/
│       ├── __init__.py        # Package init with version
│       ├── __main__.py        # python -m blog_gen.cli support
│       ├── core.py            # Core logic, data models, analysis
│       ├── cli.py             # Click CLI interface
│       └── web_ui.py          # Streamlit web interface
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Path setup for pytest
│   ├── test_core.py           # Core function tests
│   └── test_cli.py            # CLI integration tests
├── config.yaml                # Application configuration
├── setup.py                   # Package setup
├── requirements.txt           # Dependencies
├── Makefile                   # Common tasks
├── .env.example               # Environment template
└── README.md                  # This file
```

## 🚀 Installation

### Prerequisites

- **Python 3.10+**
- **[Ollama](https://ollama.ai/)** running locally
  ```bash
  ollama serve
  ollama pull llama3
  ```

### Install (User)

```bash
pip install -r requirements.txt
```

### Install (Developer)

```bash
pip install -e ".[dev]"
```

## 💻 CLI Usage

### Basic Usage

```bash
# Generate a blog post
python -m blog_gen.cli --topic "AI in Healthcare"

# With keywords and tone
python -m blog_gen.cli --topic "AI in Healthcare" \
  --keywords "ML,diagnosis,patient care" \
  --tone professional --length 800

# Save to file
python -m blog_gen.cli --topic "Cloud Computing" -o blog_post.md
```

### Advanced Options

```bash
# Preview outline first
python -m blog_gen.cli --topic "AI Trends" --outline

# Generate 3 alternative drafts
python -m blog_gen.cli --topic "AI Trends" --drafts 3

# Show SEO analysis report
python -m blog_gen.cli --topic "AI Trends" --seo-report

# Export with YAML frontmatter
python -m blog_gen.cli --topic "AI Trends" --export-md output.md

# Full pipeline
python -m blog_gen.cli --topic "AI in Healthcare" \
  --keywords "ML,diagnosis" --tone technical --length 1200 \
  --outline --seo-report --export-md article.md
```

### CLI Options Reference

| Option | Description | Default |
|--------|-------------|---------|
| `--topic` | Blog post topic (required) | — |
| `--keywords` | Comma-separated SEO keywords | None |
| `--tone` | Writing tone | `professional` |
| `--length` | Approximate word count | `800` |
| `-o, --output` | Save raw output to file | None |
| `--drafts` | Number of drafts (1-5) | `1` |
| `--outline` | Preview outline first | `False` |
| `--seo-report` | Show SEO analysis | `False` |
| `--export-md` | Export markdown with frontmatter | None |

### Example Output

```
╭─ Blog Post Generator ─╮
│ Blog Post Generator    │
╰────────────────────────╯
Topic: AI in Healthcare
Keywords: ML, diagnosis
Tone: professional
Target Length: ~800 words

╭─ Generated Blog Post ──────────────────────────────────╮
│ # AI in Healthcare: Transforming Patient Care          │
│                                                        │
│ > Discover how AI and ML are revolutionizing ...       │
│                                                        │
│ ## Introduction                                        │
│ The healthcare industry is undergoing ...              │
╰────────────────────────────────────────────────────────╯

         SEO Analysis Report
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━┳━━━━━┳━━━━━━━┓
┃ Criterion        ┃ Score ┃ Max ┃ Rating┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━╇━━━━━╇━━━━━━━┩
│ Keyword Density  │  22.5 │  30 │  ★★★  │
│ Heading Structure│  25.0 │  25 │  ★★★  │
│ Meta Description │  20.0 │  20 │  ★★★  │
│ Content Length   │  25.0 │  25 │  ★★★  │
│                  │       │     │       │
│ TOTAL            │  92.5 │ 100 │       │
└──────────────────┴───────┴─────┴───────┘
```

## 🌐 Web UI Usage

Launch the Streamlit interface:

```bash
streamlit run src/blog_gen/web_ui.py
```

The web UI provides:

- **Topic & Keywords** — Text inputs for your blog topic and SEO keywords
- **Tone & Length** — Dropdown and slider for writing parameters
- **Multi-Draft** — Slider to generate multiple draft variations
- **Outline Preview** — Button to preview structure before generating
- **SEO Dashboard** — Score gauge, keyword density, heading analysis
- **Tone Analysis** — Visual breakdown of detected writing tones
- **Export** — Download as plain markdown or with YAML frontmatter
- **History** — Sidebar showing previously generated posts in the session

## ⚙️ Configuration

Edit `config.yaml` to customise behaviour:

```yaml
app:
  name: "Blog Post Generator"
  version: "2.0.0"
llm:
  model: "llama3"           # Ollama model name
  temperature: 0.7          # Creativity (0.0-1.0)
  max_tokens: 2400          # Max response tokens
blog:
  default_tone: "professional"
  default_length: 800
  max_drafts: 5
  seo:
    min_keyword_density: 0.01
    max_keyword_density: 0.03
    min_word_count: 300
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v --tb=short

# With coverage
python -m pytest tests/ -v --cov=blog_gen --cov-report=term-missing
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Write tests for your changes
4. Ensure all tests pass (`python -m pytest tests/ -v`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

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

This project is licensed under the MIT License.
