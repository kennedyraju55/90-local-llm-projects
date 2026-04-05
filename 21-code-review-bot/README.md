<div align="center">

<!-- Banner -->
<img src="docs/images/banner.svg" alt="Code Review Bot — AI-Powered Automated Code Review with Local LLMs" width="800"/>

<br/>
<br/>

<!-- Badges -->
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-e94560?style=for-the-badge&logo=llama&logoColor=white)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=for-the-badge)](https://github.com/kennedyraju55/code-review-bot/pulls)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web_UI-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

<br/>

**AI-powered code review that runs entirely on your machine.**
No API keys. No cloud uploads. No data leaks. Just fast, private, intelligent code analysis.

<br/>

[Quick Start](#-quick-start) •
[CLI Reference](#-cli-reference) •
[Web UI](#-web-ui) •
[API Reference](#-api-reference) •
[Architecture](#%EF%B8%8F-architecture) •
[FAQ](#-faq)

</div>

<br/>

---

<br/>

## 🤔 Why This Project?

Most code review tools either require cloud API keys, send your proprietary code to third-party servers, or cost a monthly subscription. **Code Review Bot** is different — it uses [Ollama](https://ollama.com/) to run large language models **locally on your hardware**, giving you enterprise-grade code analysis with zero privacy concerns.

<br/>

| Feature | 🤖 Code Review Bot | 👀 Manual Review | ☁️ Cloud AI Tools |
|---|:---:|:---:|:---:|
| **Privacy** | ✅ 100% local | ✅ Local | ❌ Code sent to cloud |
| **Cost** | ✅ Free forever | ✅ Free | ❌ $10-50/month |
| **Speed** | ✅ Seconds | ❌ Hours/days | ✅ Seconds |
| **Consistency** | ✅ Always consistent | ❌ Varies by reviewer | ✅ Consistent |
| **24/7 Availability** | ✅ Always available | ❌ Human schedules | ✅ Always available |
| **Custom Focus Areas** | ✅ Configurable | ⚠️ Depends on reviewer | ⚠️ Limited |
| **Auto-Fix Generation** | ✅ Built-in | ❌ Manual | ⚠️ Some tools |
| **Offline Support** | ✅ Fully offline | ✅ Offline | ❌ Requires internet |
| **CI/CD Integration** | ✅ JSON/MD export | ⚠️ Manual notes | ✅ Native |

<br/>

---

<br/>

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Key Features" width="800"/>
</div>

<br/>

| Feature | Description |
|:---|:---|
| 🌐 **Multi-Language Support** | Review Python, JavaScript, TypeScript, Java, Go, Rust, C/C++, Ruby, PHP, and more. Language is auto-detected from the file extension. |
| 🔧 **Auto-Fix Generation** | Generate corrected code based on review findings. The LLM produces a fixed version of your code with all issues resolved. |
| ⚠️ **Severity Scoring** | Every issue is categorized as **Critical**, **Warning**, or **Info** so you can prioritize what to fix first. |
| 🎯 **Focus Areas** | Target specific review aspects — `security`, `performance`, `readability`, `best_practices`, `error_handling` — or review everything at once. |
| 📋 **Export Reports** | Export reviews as **Markdown** (`.md`) or **JSON** (`.json`) for CI/CD pipelines, team sharing, or archival. |
| 📁 **Directory Scanning** | Batch-review entire directories with glob pattern filtering (e.g., `*.py`, `**/*.ts`). |
| 🖥️ **Rich CLI Output** | Colored, structured terminal output with syntax highlighting and severity indicators. |
| 🌐 **Streamlit Web UI** | Beautiful web interface with code editor, file upload, live review results, and report downloads. |
| ⚙️ **YAML Configuration** | Flexible config via `config.yaml` with environment variable overrides. |
| 📝 **Line References** | Every finding includes exact line numbers for fast navigation to the problem. |

<br/>

---

<br/>

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+** installed
- **Ollama** installed and running ([install guide](https://ollama.com/download))
- A pulled model (e.g., `gemma3` or `codellama`)

### 1. Install the package

```bash
# Clone the repository
git clone https://github.com/kennedyraju55/code-review-bot.git
cd code-review-bot

# Install dependencies
pip install -r requirements.txt

# Or install as an editable package
pip install -e .
```

### 2. Set up Ollama

```bash
# Start the Ollama server (if not already running)
ollama serve

# Pull a model (choose one)
ollama pull gemma3          # Recommended — good balance of speed & quality
ollama pull codellama       # Alternative — optimized for code tasks
ollama pull llama3.1        # Alternative — general purpose
```

### 3. Review your first file

```bash
# Basic review
python -m code_reviewer.cli review --file my_script.py
```

**Example output:**

```
╭──────────────────────────────────────────────────────╮
│  🔍 Code Review Bot                                  │
│  AI-powered code review with severity scoring         │
╰──────────────────────────────────────────────────────╯

📄 Reviewing: my_script.py (Python, 87 lines)

╭── 📋 Code Review Results ────────────────────────────╮
│                                                       │
│  🔴 CRITICAL (1)                                      │
│  ──────────────                                       │
│  Line 23: SQL query built with string concatenation   │
│  → Use parameterized queries to prevent SQL injection │
│                                                       │
│  🟡 WARNING (2)                                       │
│  ──────────────                                       │
│  Line 15: Bare `except:` clause catches all errors    │
│  → Catch specific exception types instead             │
│                                                       │
│  Line 42: Nested loop creates O(n²) complexity        │
│  → Consider using a dictionary for O(n) lookup        │
│                                                       │
│  🔵 INFO (1)                                          │
│  ──────────────                                       │
│  Line 8: Missing type hints on function parameters    │
│  → Add type annotations for better documentation      │
│                                                       │
╰──────────────────────────────────────────────────────╯

┌─────────────────── Summary ──────────────────────────┐
│ File        │ Language │ Lines │ Issues │ Status      │
├─────────────┼──────────┼───────┼────────┼─────────────┤
│ my_script   │ Python   │ 87    │ 4      │ ✅ Complete │
└─────────────┴──────────┴───────┴────────┴─────────────┘
```

<br/>

---

<br/>

## 📖 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and provides two main commands: `review` and `review-dir`.

### `review` — Single File Review

```bash
python -m code_reviewer.cli review [OPTIONS]
```

| Option | Type | Default | Description |
|:---|:---|:---|:---|
| `--file` | `PATH` | *(required)* | Path to the source code file to review |
| `--focus` | `TEXT` | `"all"` | Comma-separated focus areas: `security`, `performance`, `readability`, `best_practices`, `error_handling`, or `all` |
| `--show-code` | `FLAG` | `False` | Display the source code with line numbers alongside the review |
| `--autofix` | `FLAG` | `False` | Generate auto-fix suggestions with corrected code |
| `--output` | `PATH` | `None` | Export review to a file. Format is inferred from extension (`.md` or `.json`) |

**Examples:**

```bash
# Review with security focus and auto-fix
python -m code_reviewer.cli review --file api.py --focus security --autofix

# Review and export as JSON for CI/CD
python -m code_reviewer.cli review --file handler.py --output report.json

# Review with source code display
python -m code_reviewer.cli review --file utils.py --show-code

# Multiple focus areas
python -m code_reviewer.cli review --file app.py --focus "security,performance,error_handling"
```

### `review-dir` — Directory Review

```bash
python -m code_reviewer.cli review-dir [OPTIONS]
```

| Option | Type | Default | Description |
|:---|:---|:---|:---|
| `--dir` | `PATH` | *(required)* | Path to the directory to scan |
| `--pattern` | `TEXT` | `"*.py"` | Glob pattern to filter files |
| `--focus` | `TEXT` | `"all"` | Comma-separated focus areas |
| `--output` | `PATH` | `None` | Export combined review to a file (`.md` or `.json`) |

**Examples:**

```bash
# Review all Python files in src/
python -m code_reviewer.cli review-dir --dir ./src --pattern "*.py"

# Review all TypeScript files with performance focus
python -m code_reviewer.cli review-dir --dir ./frontend --pattern "*.ts" --focus performance

# Review and export combined report
python -m code_reviewer.cli review-dir --dir ./backend --pattern "*.py" --output full_report.md
```

### Global Options

```bash
python -m code_reviewer.cli [GLOBAL OPTIONS] <command>
```

| Option | Description |
|:---|:---|
| `--config PATH` | Path to a custom YAML configuration file |
| `-v`, `--verbose` | Enable verbose logging output |
| `--help` | Show help message and exit |

<br/>

---

<br/>

## 🌐 Web UI

The project includes a **Streamlit-powered web interface** for interactive code reviews.

### Launch

```bash
streamlit run src/code_reviewer/web_ui.py
# Opens at http://localhost:8501
```

### Web UI Features

| Feature | Description |
|:---|:---|
| 📝 **Code Editor** | Paste code directly into the built-in editor with syntax highlighting |
| 📁 **File Upload** | Drag-and-drop or browse to upload source code files |
| ⚙️ **Sidebar Config** | Configure model, temperature, max tokens, and focus areas interactively |
| 🔧 **Auto-Fix Toggle** | Enable/disable auto-fix generation with a single checkbox |
| 📊 **Live Results** | Review results render in real-time as the LLM streams its response |
| 📥 **Report Download** | Download the complete review as a Markdown file |

<br/>

---

<br/>

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="Architecture Overview" width="800"/>
</div>

<br/>

### Data Flow

```
Code Files → File Reader → Language Detector → Code Numbering
    → LLM Prompt Builder → Ollama API → Review Parser
    → Severity Scoring → Report Export (MD / JSON)
```

1. **File Reader** — Reads source code files with size validation (`max_file_size_kb`)
2. **Language Detector** — Maps file extensions to programming languages (`.py` → Python, `.ts` → TypeScript, etc.)
3. **Code Numbering** — Annotates each line with line numbers for precise review references
4. **LLM Prompt Builder** — Constructs a structured prompt with the code, language context, and focus areas
5. **Ollama API** — Sends the prompt to the local LLM via Ollama's REST API
6. **Review Parser** — Extracts structured review findings from the LLM response
7. **Severity Scoring** — Categorizes each issue as Critical, Warning, or Info
8. **Report Export** — Formats the review as Markdown or JSON for output

### Project Structure

```
21-code-review-bot/
├── src/
│   └── code_reviewer/
│       ├── __init__.py          # Package metadata & version
│       ├── core.py              # Core review engine (review_single_file, review_multiple_files,
│       │                        #   generate_autofix, export_report)
│       ├── cli.py               # Click CLI (review, review-dir commands)
│       ├── web_ui.py            # Streamlit web interface
│       ├── config.py            # YAML/env configuration management
│       └── utils.py             # Language detection, severity scoring, formatting
├── tests/
│   ├── __init__.py
│   ├── test_core.py             # Core logic unit tests
│   └── test_cli.py              # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner graphic
│       ├── architecture.svg     # Architecture diagram
│       └── features.svg         # Features overview graphic
├── config.yaml                  # Default configuration
├── setup.py                     # Package setup (pip install -e .)
├── requirements.txt             # Python dependencies
├── Makefile                     # Dev commands (test, lint, run)
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

<br/>

---

<br/>

## 🔌 API Reference

You can use the `code_reviewer` module directly in your Python code for programmatic reviews.

### `review_single_file`

Review a single source code file and return structured results.

```python
from code_reviewer.core import review_single_file

result = review_single_file(
    file_path="src/api/handler.py",
    focus="security,performance",
    show_code=True
)

# result is a dict with review findings
print(result["file"])         # "src/api/handler.py"
print(result["language"])     # "python"
print(result["issues"])       # List of issue dicts
print(result["summary"])      # Summary string

for issue in result["issues"]:
    print(f"[{issue['severity']}] Line {issue['line']}: {issue['message']}")
```

### `review_multiple_files`

Batch-review multiple files and return a combined report.

```python
from code_reviewer.core import review_multiple_files

results = review_multiple_files(
    directory="./src",
    pattern="*.py",
    focus="all"
)

for file_result in results:
    print(f"\n📄 {file_result['file']} — {len(file_result['issues'])} issues")
    for issue in file_result["issues"]:
        print(f"  [{issue['severity']}] Line {issue['line']}: {issue['message']}")
```

### `generate_autofix`

Generate a corrected version of the code based on review findings.

```python
from code_reviewer.core import review_single_file, generate_autofix

# First, review the file
result = review_single_file(file_path="buggy_script.py")

# Then generate the fixed version
fixed_code = generate_autofix(
    file_path="buggy_script.py",
    review_result=result
)

print(fixed_code)  # Corrected source code as a string
```

### `export_report`

Export review results to Markdown or JSON format.

```python
from code_reviewer.core import review_single_file, export_report

result = review_single_file(file_path="app.py", focus="all")

# Export as Markdown
export_report(result, output_path="review.md")

# Export as JSON
export_report(result, output_path="review.json")

# Get formatted string without writing to file
md_string = export_report(result, format="markdown")
json_string = export_report(result, format="json")
```

### Utility Functions

```python
from code_reviewer.utils import detect_language, score_severity

# Detect programming language from file extension
lang = detect_language("app.tsx")   # Returns "typescript"
lang = detect_language("main.go")   # Returns "go"
lang = detect_language("server.rs") # Returns "rust"

# Score severity from issue text
severity = score_severity("SQL injection vulnerability")  # Returns "critical"
severity = score_severity("Missing type hints")           # Returns "info"
```

<br/>

---

<br/>

## ⚙️ Configuration

### config.yaml

Create or edit `config.yaml` in the project root:

```yaml
# Ollama connection
ollama_base_url: "http://localhost:11434"

# Model settings
model: "gemma3"
temperature: 0.3
max_tokens: 4096

# File handling
max_file_size_kb: 500

# Output
output_format: "markdown"    # "markdown" or "json"

# Logging
log_level: "INFO"            # DEBUG, INFO, WARNING, ERROR
```

### Configuration Reference

| Key | Type | Default | Description |
|:---|:---|:---|:---|
| `ollama_base_url` | `string` | `http://localhost:11434` | URL of the Ollama server |
| `model` | `string` | `gemma3` | Name of the Ollama model to use |
| `temperature` | `float` | `0.3` | LLM temperature (0.0 = deterministic, 1.0 = creative) |
| `max_tokens` | `int` | `4096` | Maximum tokens in the LLM response |
| `max_file_size_kb` | `int` | `500` | Maximum file size to review (in KB). Files larger than this are skipped. |
| `output_format` | `string` | `markdown` | Default export format (`markdown` or `json`) |
| `log_level` | `string` | `INFO` | Logging verbosity level |

### Environment Variable Overrides

Environment variables take precedence over `config.yaml` values:

| Variable | Overrides | Example |
|:---|:---|:---|
| `OLLAMA_BASE_URL` | `ollama_base_url` | `http://192.168.1.100:11434` |
| `OLLAMA_MODEL` | `model` | `codellama` |
| `REVIEW_TEMPERATURE` | `temperature` | `0.5` |
| `REVIEW_MAX_TOKENS` | `max_tokens` | `8192` |
| `MAX_FILE_SIZE_KB` | `max_file_size_kb` | `1000` |
| `LOG_LEVEL` | `log_level` | `DEBUG` |

<br/>

---

<br/>

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ -v --cov=src/code_reviewer --cov-report=term-missing

# Run only core logic tests
python -m pytest tests/test_core.py -v

# Run only CLI tests
python -m pytest tests/test_cli.py -v

# Run tests matching a keyword
python -m pytest tests/ -v -k "test_review"
```

### Expected Output

```
tests/test_core.py::test_review_single_file_python PASSED
tests/test_core.py::test_review_single_file_javascript PASSED
tests/test_core.py::test_language_detection PASSED
tests/test_core.py::test_severity_scoring PASSED
tests/test_core.py::test_export_markdown PASSED
tests/test_core.py::test_export_json PASSED
tests/test_core.py::test_autofix_generation PASSED
tests/test_core.py::test_max_file_size_check PASSED
tests/test_cli.py::test_review_command PASSED
tests/test_cli.py::test_review_dir_command PASSED
tests/test_cli.py::test_output_flag PASSED
tests/test_cli.py::test_focus_flag PASSED

---------- coverage: ----------
Name                              Stmts   Miss  Cover   Missing
---------------------------------------------------------------
src/code_reviewer/__init__.py         5      0   100%
src/code_reviewer/cli.py             62      4    94%   88-91
src/code_reviewer/config.py          28      2    93%   41-42
src/code_reviewer/core.py            95      8    92%   112-119
src/code_reviewer/utils.py           34      1    97%   48
---------------------------------------------------------------
TOTAL                               224     15    93%

12 passed in 4.82s
```

<br/>

---

<br/>

## 🔒 Local vs Cloud Comparison

One of the core motivations for this project is **privacy**. Here's how local LLM processing compares to cloud-based alternatives:

| Aspect | 🏠 Local (This Tool) | ☁️ Cloud-Based |
|:---|:---|:---|
| **Data Privacy** | Code never leaves your machine | Code uploaded to third-party servers |
| **Internet Required** | ❌ No — fully offline capable | ✅ Yes — requires active connection |
| **Cost** | Free (open-source + local compute) | $10–50+/month subscription fees |
| **Latency** | Low — no network round-trips | Variable — depends on API latency |
| **Rate Limits** | None — limited only by your hardware | Often throttled or tiered |
| **Compliance** | Easy — data stays in your infra | Requires DPA, vendor review |
| **Model Control** | Full — swap models anytime | Limited to provider's offerings |
| **Customization** | Fine-tune prompts, models, config | Limited configuration options |
| **Hardware Needs** | GPU recommended for speed (CPU works) | None — runs on provider's infra |
| **Setup Effort** | ~5 minutes (Ollama + pip install) | ~2 minutes (API key signup) |

<br/>

---

<br/>

## ❓ FAQ

<details>
<summary><strong>What models work best with Code Review Bot?</strong></summary>

<br/>

The tool works with any Ollama-compatible model. Recommended options:

| Model | Size | Best For |
|:---|:---|:---|
| `gemma3` | 4.9 GB | General code review — best balance of speed and quality |
| `codellama` | 3.8 GB | Code-specific tasks — optimized for programming languages |
| `llama3.1` | 4.7 GB | General purpose — strong reasoning capabilities |
| `deepseek-coder` | 776 MB – 8.9 GB | Code generation and review — multiple size options |
| `mistral` | 4.1 GB | Fast inference — good for quick reviews |

Switch models anytime via `config.yaml` or the `OLLAMA_MODEL` environment variable.

</details>

<details>
<summary><strong>How much RAM/VRAM do I need?</strong></summary>

<br/>

- **Minimum:** 8 GB RAM (CPU-only mode, smaller models like `deepseek-coder:1.3b`)
- **Recommended:** 16 GB RAM + 6 GB VRAM (GPU acceleration with 7B models)
- **Optimal:** 32 GB RAM + 12 GB VRAM (for 13B+ models and faster inference)

Ollama automatically uses your GPU if CUDA or Metal is available. CPU-only mode works but is slower.

</details>

<details>
<summary><strong>Can I use this in a CI/CD pipeline?</strong></summary>

<br/>

Yes! Use the JSON export feature for machine-readable output:

```bash
# In your CI script
python -m code_reviewer.cli review --file app.py --output review.json

# Parse the JSON in your pipeline
python -c "
import json
with open('review.json') as f:
    report = json.load(f)
criticals = [i for i in report['issues'] if i['severity'] == 'critical']
if criticals:
    print(f'❌ {len(criticals)} critical issues found')
    exit(1)
print('✅ No critical issues')
"
```

For directory-wide reviews:

```bash
python -m code_reviewer.cli review-dir --dir ./src --pattern "*.py" --output ci_report.json
```

</details>

<details>
<summary><strong>What programming languages are supported?</strong></summary>

<br/>

The language detector supports the following extensions:

| Extension | Language | Extension | Language |
|:---|:---|:---|:---|
| `.py` | Python | `.go` | Go |
| `.js` | JavaScript | `.rs` | Rust |
| `.ts` | TypeScript | `.rb` | Ruby |
| `.tsx` | TypeScript (React) | `.php` | PHP |
| `.jsx` | JavaScript (React) | `.swift` | Swift |
| `.java` | Java | `.kt` | Kotlin |
| `.cpp`, `.cc` | C++ | `.cs` | C# |
| `.c`, `.h` | C | `.scala` | Scala |
| `.html` | HTML | `.sh` | Shell |
| `.css` | CSS | `.sql` | SQL |
| `.yaml`, `.yml` | YAML | `.r` | R |

If a file extension is not recognized, the tool defaults to plain text analysis.

</details>

<details>
<summary><strong>How do I customize the review prompt?</strong></summary>

<br/>

The review prompt is constructed in `src/code_reviewer/core.py`. You can modify the prompt template to add custom instructions, change the output format, or adjust the review criteria.

The focus areas (`security`, `performance`, `readability`, `best_practices`, `error_handling`) each inject specific instructions into the prompt. You can add new focus areas by extending the `FOCUS_PROMPTS` dictionary in `core.py`.

```python
# Example: Adding a custom focus area
FOCUS_PROMPTS = {
    "security": "Focus on security vulnerabilities...",
    "performance": "Focus on performance issues...",
    "my_custom_area": "Focus on my team's specific coding standards...",
}
```

</details>

<br/>

---

<br/>

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone and install in development mode
git clone https://github.com/kennedyraju55/code-review-bot.git
cd code-review-bot
pip install -e ".[dev]"

# Run tests to verify setup
python -m pytest tests/ -v
```

### Contribution Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature-name`
3. **Make** your changes with tests
4. **Run** the test suite: `python -m pytest tests/ -v`
5. **Commit** with a descriptive message: `git commit -m "feat: add your feature description"`
6. **Push** to your fork: `git push origin feature/your-feature-name`
7. **Open** a Pull Request against `master`

### Guidelines

- Follow existing code style and patterns
- Add tests for new features
- Update documentation for user-facing changes
- Keep PRs focused — one feature or fix per PR

<br/>

---

<br/>

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](../LICENSE) file for details.

You are free to use, modify, and distribute this software for personal and commercial purposes.

<br/>

---

<br/>

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

<br/>

Built with ❤️ using [Python](https://www.python.org/) • [Ollama](https://ollama.com/) • [Click](https://click.palletsprojects.com/) • [Streamlit](https://streamlit.io/)

<br/>

[⬆ Back to Top](#)

</div>
