<div align="center">
<img src="https://img.shields.io/badge/✍️_🏷️_Product_Description_Writer-Local_LLM_Powered-blue?style=for-the-badge&labelColor=1a1a2e&color=16213e" alt="Project Banner" width="600"/>
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
| 🏪 **Multi-Platform Support** | Amazon, Shopify, Etsy, eBay with platform-specific optimization |
| 🔗 **Feature-Benefit Mapping** | Automatically maps product features to customer benefits |
| 🔍 **SEO Keywords** | Keyword integration with density analysis and scoring |
| 🔀 **A/B Variants** | Generate multiple description variants for testing |
| 📏 **Length Control** | Short (50-100), Medium (150-250), Long (300-500) word options |
| 📊 **SEO Score** | Real-time SEO score with keyword coverage metrics |
| 💻 **Dual Interface** | Full CLI + Streamlit Web UI |
| ⚙️ **YAML Configuration** | Flexible config management |

## 🏗️ Architecture

```
38-product-description-writer/
├── src/
│   └── product_writer/
│       ├── __init__.py          # Package metadata
│       ├── core.py              # Business logic, SEO, platform configs
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
make install    # or: pip install -e .
make dev        # with dev dependencies
```

## 🖥️ CLI Usage

### Generate Descriptions

```bash
# Basic
product-writer generate --product "Wireless Headphones"

# Full options
product-writer generate \
  --product "Wireless Headphones" \
  --features "noise-cancel,bluetooth,40h battery" \
  --platform amazon \
  --length long \
  --variants 3 \
  --keywords "wireless,headphones,noise canceling" \
  -o output.md
```

### List Platforms

```bash
product-writer platforms
```

### Map Features to Benefits

```bash
product-writer benefits --features "waterproof,bluetooth,portable"
```

## 🌐 Web UI

```bash
make run-web
```

| Tab | Description |
|-----|-------------|
| 📝 **Product Form** | Enter product details, features, keywords |
| 🏪 **Platform Tabs** | Browse platform-specific guidelines |
| 📄 **Generated** | View and download generated descriptions |
| 📊 **SEO Score** | Keyword coverage, density analysis, overall score |

## ⚙️ Configuration

```yaml
llm:
  temperature: 0.7
  max_tokens: 4096
product:
  platforms: [amazon, shopify, etsy, ebay, generic]
  default_variants: 2
seo:
  keyword_count: 10
```

## 🧪 Testing

```bash
make test
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
