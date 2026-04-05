<p align="center">
  <img src="docs/images/banner.svg" alt="Commit Message Generator Banner" width="800"/>
</p>

<p align="center">
  <strong>Generate conventional commit messages from git diffs using a local LLM — no API keys, no cloud, no data leaving your machine.</strong>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"/></a>
  <a href="https://ollama.com/"><img src="https://img.shields.io/badge/Ollama-Local%20LLM-00b4d8?style=flat-square&logo=ollama&logoColor=white" alt="Ollama"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License MIT"/></a>
  <a href="https://github.com/kennedyraju55/commit-message-generator/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs Welcome"/></a>
  <img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>

<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-cli-reference">CLI Reference</a> •
  <a href="#-web-ui">Web UI</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-configuration">Configuration</a> •
  <a href="#-faq">FAQ</a>
</p>

---

## 💡 Why This Project?

Writing clear, consistent commit messages is tedious. Most developers resort to vague messages like `"fix stuff"` or `"update code"`. This tool analyzes your actual code changes and generates properly formatted **Conventional Commits** — entirely on your local machine using [Ollama](https://ollama.com/).

### Comparison: Manual vs. Cloud AI vs. Commit Gen

| Criteria | Manual Writing | Cloud AI (GPT/Claude) | **Commit Gen (Local)** |
|---|---|---|---|
| **Privacy** | ✅ No data shared | ❌ Code sent to cloud | ✅ **100% local** |
| **Cost** | ✅ Free | ❌ API costs add up | ✅ **Free forever** |
| **Consistency** | ❌ Varies by developer | ⚠️ Prompt-dependent | ✅ **Conventional Commits** |
| **Speed** | ❌ Slow, context-switching | ⚠️ Network latency | ✅ **Instant, offline** |
| **Internet Required** | ✅ No | ❌ Yes | ✅ **No** |
| **Customizable** | ❌ No | ⚠️ Limited | ✅ **Full control** |
| **Emoji Support** | ❌ Manual | ⚠️ Inconsistent | ✅ **Automatic mapping** |
| **Batch Processing** | ❌ One at a time | ⚠️ Manual batching | ✅ **Built-in** |

---

## ✨ Features

<p align="center">
  <img src="docs/images/features.svg" alt="Key Features" width="800"/>
</p>

### Feature Highlights

| Feature | Description | Flag/Option |
|---|---|---|
| 📋 **Conventional Commits** | `type(scope): description` format following the specification | Default behavior |
| 🎨 **Emoji Prefixes** | Automatic emoji mapping: ✨ feat, 🐛 fix, 📝 docs, 🎨 style, ♻️ refactor | `--no-emoji` to disable |
| 📦 **Batch Mode** | Process multiple diffs in one call via the Python API | `generate_batch_messages()` |
| 🏷️ **Type Selection** | Hint the commit type: feat, fix, docs, style, refactor, perf, test, build, ci, chore | `--type feat` |
| 📄 **Diff From File** | Read diffs from a file instead of live git state | `--diff-file changes.diff` |
| 💡 **Multiple Suggestions** | Get ranked commit message options to pick the best one | `num_suggestions` in config |
| 🌐 **Web UI** | Streamlit-based browser interface with git integration | `make web` |
| 🔌 **Stdin Piping** | Pipe any diff output directly into the CLI | `git diff \| commit-gen generate` |

### Supported Commit Types

| Type | Emoji | Description |
|---|---|---|
| `feat` | ✨ | A new feature |
| `fix` | 🐛 | A bug fix |
| `docs` | 📝 | Documentation changes |
| `style` | 🎨 | Code style/formatting (no logic change) |
| `refactor` | ♻️ | Code refactoring (no feature/fix) |
| `perf` | ⚡ | Performance improvements |
| `test` | ✅ | Adding or updating tests |
| `build` | 📦 | Build system or dependency changes |
| `ci` | 👷 | CI/CD configuration changes |
| `chore` | 🔧 | Maintenance tasks |

---

## 🚀 Quick Start

### Prerequisites

| Requirement | Version | Installation |
|---|---|---|
| Python | 3.10+ | [python.org](https://www.python.org/downloads/) |
| Ollama | Latest | [ollama.com](https://ollama.com/) |
| Git | 2.x+ | [git-scm.com](https://git-scm.com/) |

### 1. Install Ollama & Pull a Model

```bash
# Install Ollama (https://ollama.com/download)
# Then pull the default model:
ollama pull gemma4
```

### 2. Clone & Install

```bash
git clone https://github.com/kennedyraju55/commit-message-generator.git
cd commit-message-generator

# Install dependencies
make install
# Or manually:
pip install -r requirements.txt
```

### 3. Generate Your First Commit Message

```bash
# Stage some changes
git add .

# Generate commit messages from staged diff
python -m commit_gen.cli generate
```

### Example Output

```
╭──────────────────────────────────────────────────────────╮
│  🤖 Commit Message Suggestions                          │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  1. ✨ feat(auth): add JWT token refresh endpoint        │
│                                                          │
│  2. ✨ feat(auth): implement token refresh with expiry   │
│     validation and automatic renewal                     │
│                                                          │
│  3. ✨ feat(api): add authentication token refresh       │
│     mechanism for session management                     │
│                                                          │
╰──────────────────────────────────────────────────────────╯
```

### Install as CLI Tool (Optional)

```bash
pip install -e .

# Now use anywhere:
commit-gen generate --staged
commit-gen generate --type fix
commit-gen from-text "diff --git a/file.py ..."
```


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/commit-message-generator.git
cd commit-message-generator
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
uvicorn src.commit_gen.api:app --reload --port 8000

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

## 📖 CLI Reference

The CLI is built with [Click](https://click.palletsprojects.com/) and provides two main commands.

### Global Options

| Option | Short | Description |
|---|---|---|
| `--config PATH` | | Path to config YAML file (default: `config.yaml`) |
| `--verbose` | `-v` | Enable DEBUG-level logging |

### `commit-gen generate`

Generate commit messages from git diffs.

```bash
commit-gen generate [OPTIONS]
```

| Option | Type | Default | Description |
|---|---|---|---|
| `--staged` | flag | `True` | Use only staged changes (`git diff --cached`) |
| `--all` | flag | `False` | Include all unstaged changes (`git diff`) |
| `--type` | choice | auto | Commit type hint: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore` |
| `--diff-file` | path | — | Read diff from a file instead of git |
| `--no-emoji` | flag | `False` | Disable emoji prefixes in output |

**Examples:**

```bash
# Staged changes (default)
commit-gen generate

# All changes including unstaged
commit-gen generate --all

# Specify commit type
commit-gen generate --type fix

# Read diff from file
commit-gen generate --diff-file my-changes.diff

# Disable emoji
commit-gen generate --no-emoji

# Pipe from git
git diff HEAD~3 | commit-gen generate

# Combine options
commit-gen generate --all --type feat --no-emoji
```

### `commit-gen from-text`

Generate commit messages from pasted diff text.

```bash
commit-gen from-text DIFF_TEXT [OPTIONS]
```

| Argument/Option | Type | Description |
|---|---|---|
| `DIFF_TEXT` | string | The diff content as a text argument |
| `--type` | choice | Commit type hint (same choices as `generate`) |

**Examples:**

```bash
# Paste diff text directly
commit-gen from-text "diff --git a/src/auth.py b/src/auth.py
--- a/src/auth.py
+++ b/src/auth.py
@@ -10,6 +10,12 @@
+def refresh_token(token):
+    return jwt.encode(payload, SECRET)"

# With type hint
commit-gen from-text "..." --type feat
```

---

## 🌐 Web UI

Commit Gen includes a **Streamlit-based web interface** for a more visual experience.

### Launch

```bash
make web
# Or directly:
streamlit run src/commit_gen/web_ui.py
```

Then open **http://localhost:8501** in your browser.

### Web UI Features

| Feature | Description |
|---|---|
| **Paste Diff Tab** | Paste any diff content and generate messages |
| **Git Integration Tab** | Read staged or all changes directly from your repo |
| **Sidebar Settings** | Configure model, temperature, suggestion count, emoji toggle, commit type |
| **Branch Display** | Shows current git branch name |
| **Diff Stats** | Displays file change statistics |
| **Download** | Export generated messages as a `.txt` file |

### Web UI Workflow

1. **Open** the app at `http://localhost:8501`
2. **Configure** settings in the sidebar (model, temperature, etc.)
3. **Choose** the "Paste Diff" or "Git Integration" tab
4. **Click** "Generate" to get commit message suggestions
5. **Download** or copy the results

---

## 🏗️ Architecture

<p align="center">
  <img src="docs/images/architecture.svg" alt="Architecture Overview" width="800"/>
</p>

### Data Flow

```
┌─────────────────┐
│   Input Source   │
│  (staged/all/    │──► Diff Reader ──► Truncation ──► Prompt Builder
│   file/stdin)    │         │              │                │
└─────────────────┘         │              │                │
                      Parse raw diff   Limit to          Build system
                      into segments    max_diff_chars     prompt + context
                                                               │
                                                               ▼
┌─────────────────┐                                    ┌──────────────┐
│    Output        │◄── Emoji Mapper ◄── Parser ◄──── │  Ollama LLM  │
│  Suggestions     │                                   │  (Gemma 4)   │
└─────────────────┘                                    └──────────────┘
```

### Project Structure

```
22-commit-message-generator/
├── src/
│   └── commit_gen/
│       ├── __init__.py          # Package initialization
│       ├── core.py              # Core logic: generate_commit_messages, generate_batch_messages
│       ├── cli.py               # Click CLI: generate, from-text commands
│       ├── web_ui.py            # Streamlit web interface
│       ├── config.py            # CommitConfig dataclass, load_config, constants
│       └── utils.py             # Git helpers, truncation, emoji mapping
├── common/
│   └── llm_client.py           # Shared Ollama client (chat, stream, embed)
├── tests/
│   ├── __init__.py
│   ├── test_core.py            # Unit tests for core functions
│   └── test_cli.py             # CLI integration tests
├── docs/
│   └── images/
│       ├── banner.svg           # Project banner
│       ├── architecture.svg     # Architecture diagram
│       └── features.svg         # Features overview
├── config.yaml                  # Default configuration
├── .env.example                 # Environment variable template
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup (pip install -e .)
├── Makefile                     # Dev commands (install, test, lint, web)
└── README.md                   # This file
```

### Module Responsibilities

| Module | Role | Key Exports |
|---|---|---|
| `core.py` | Message generation orchestration | `generate_commit_messages()`, `generate_batch_messages()` |
| `cli.py` | Terminal interface via Click | `main()`, `generate`, `from-text` commands |
| `web_ui.py` | Browser interface via Streamlit | `run()` |
| `config.py` | Configuration management | `CommitConfig`, `load_config()`, `COMMIT_TYPES`, `COMMIT_EMOJIS` |
| `utils.py` | Git operations & text processing | `get_git_diff()`, `truncate_diff()`, `add_emoji_to_message()` |
| `llm_client.py` | Ollama API communication | `chat()`, `chat_stream()`, `check_ollama_running()` |

---

## 📚 API Reference

### `generate_commit_messages()`

The primary function for generating commit messages from a diff string.

```python
from commit_gen.core import generate_commit_messages
from commit_gen.config import load_config

config = load_config()

diff = """
diff --git a/src/auth.py b/src/auth.py
--- a/src/auth.py
+++ b/src/auth.py
@@ -10,6 +10,12 @@
+def refresh_token(token):
+    if is_expired(token):
+        return generate_new_token(token.user_id)
+    return token
"""

# Auto-detect commit type
result = generate_commit_messages(diff, config=config)
print(result)

# Specify commit type
result = generate_commit_messages(diff, msg_type="feat", config=config)
print(result)
```

**Parameters:**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `diff` | `str` | required | The git diff content to analyze |
| `msg_type` | `str` | `""` | Optional commit type hint (`feat`, `fix`, etc.) |
| `config` | `CommitConfig \| None` | `None` | Configuration object; loads defaults if `None` |

**Returns:** `str` — Formatted commit message suggestions.

---

### `generate_batch_messages()`

Process multiple diffs in a single call for batch workflows.

```python
from commit_gen.core import generate_batch_messages
from commit_gen.config import load_config

config = load_config()

diffs = [
    {
        "name": "auth-module",
        "diff": "diff --git a/src/auth.py ..."
    },
    {
        "name": "api-routes",
        "diff": "diff --git a/src/routes.py ..."
    },
    {
        "name": "test-updates",
        "diff": "diff --git a/tests/test_auth.py ..."
    },
]

results = generate_batch_messages(diffs, config=config)

for item in results:
    print(f"\n=== {item['name']} ===")
    print(item["messages"])
```

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `diffs` | `list[dict]` | List of `{"name": str, "diff": str}` objects |
| `config` | `CommitConfig \| None` | Configuration object |

**Returns:** `list[dict]` — List of `{"name": str, "messages": str}` results.

---

### Utility Functions

```python
from commit_gen.utils import (
    get_git_diff,
    get_git_stat,
    get_git_staged_files,
    get_git_branch,
    truncate_diff,
    add_emoji_to_message,
    read_diff_from_stdin,
)

# Get staged diff
staged_diff = get_git_diff(staged_only=True)

# Get all changes
all_diff = get_git_diff(staged_only=False)

# Get diff statistics
stats = get_git_stat(staged_only=True)

# Get list of staged files
files = get_git_staged_files()
# → ["src/auth.py", "tests/test_auth.py"]

# Get current branch
branch = get_git_branch()
# → "feature/token-refresh"

# Truncate long diffs
short_diff = truncate_diff(large_diff, max_chars=4000)

# Add emoji to a commit message
message = add_emoji_to_message(
    "feat(auth): add token refresh",
    {"feat": "✨", "fix": "🐛", "docs": "📝"}
)
# → "✨ feat(auth): add token refresh"
```

---

### Configuration API

```python
from commit_gen.config import (
    CommitConfig,
    load_config,
    setup_logging,
    COMMIT_TYPES,
    COMMIT_EMOJIS,
)

# Load from default config.yaml
config = load_config()

# Load from custom path
config = load_config("my-config.yaml")

# Access config values
print(config.model)            # "gemma4"
print(config.temperature)      # 0.5
print(config.num_suggestions)  # 3
print(config.use_emoji)        # True

# Available commit types
print(COMMIT_TYPES)
# ["feat", "fix", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore"]

# Emoji mapping
print(COMMIT_EMOJIS)
# {"feat": "✨", "fix": "🐛", "docs": "📝", "style": "🎨", ...}

# Setup logging from config
setup_logging(config)
```

---

### Ollama Client (Shared)

```python
from common.llm_client import (
    check_ollama_running,
    list_models,
    chat,
    chat_stream,
    generate,
    embed,
)

# Health check
if check_ollama_running():
    print("Ollama is running!")

# List available models
models = list_models()
# → [{"name": "gemma4", ...}, {"name": "llama3", ...}]

# Chat completion
response = chat(
    messages=[{"role": "user", "content": "Hello"}],
    model="gemma4",
    temperature=0.5,
)

# Streaming chat
for chunk in chat_stream(
    messages=[{"role": "user", "content": "Explain git rebase"}],
    model="gemma4",
):
    print(chunk, end="", flush=True)

# Simple text generation
text = generate(
    prompt="What is a conventional commit?",
    model="gemma4",
)

# Text embeddings
vector = embed("Some text to embed", model="gemma4")
# → [0.123, -0.456, ...]
```

---

## ⚙️ Configuration

### config.yaml

The default configuration file controls all behavior:

```yaml
# Ollama connection
ollama_base_url: "http://localhost:11434"
model: "gemma4"

# Generation parameters
temperature: 0.5          # 0.0 = deterministic, 1.0 = creative
max_tokens: 2048          # Max tokens in LLM response
num_suggestions: 3        # Number of commit messages to generate

# Feature flags
use_emoji: true           # Prepend emoji to commit type
conventional: true        # Follow Conventional Commits spec

# Diff handling
max_diff_chars: 4000      # Truncate diffs beyond this length

# Logging
log_level: "INFO"         # DEBUG, INFO, WARNING, ERROR
```

### Environment Variables

Environment variables **override** `config.yaml` values:

| Variable | Overrides | Example |
|---|---|---|
| `OLLAMA_BASE_URL` | `ollama_base_url` | `http://192.168.1.100:11434` |
| `OLLAMA_MODEL` | `model` | `llama3` |
| `LOG_LEVEL` | `log_level` | `DEBUG` |
| `COMMIT_GEN_CONFIG` | Config file path | `./my-config.yaml` |

```bash
# Use a remote Ollama instance
export OLLAMA_BASE_URL=http://192.168.1.100:11434

# Switch to a different model
export OLLAMA_MODEL=llama3

# Enable debug logging
export LOG_LEVEL=DEBUG

# Use a custom config file
export COMMIT_GEN_CONFIG=/path/to/config.yaml
```

### Configuration Priority

```
Environment Variables  →  config.yaml  →  Hardcoded Defaults
    (highest)                                  (lowest)
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
make test
# Or:
python -m pytest tests/ -v --tb=short

# Run with coverage report
make test-cov
# Or:
python -m pytest tests/ -v --cov=src/commit_gen --cov-report=term-missing
```

### Linting

```bash
make lint
# Runs py_compile on core.py, cli.py, web_ui.py
```

### Test Structure

| File | Tests | Coverage |
|---|---|---|
| `test_core.py` | `generate_commit_messages`, `generate_batch_messages`, utility functions, config loading | Core logic |
| `test_cli.py` | CLI `generate` command with various flag combinations | CLI integration |

### Example Test

```python
# tests/test_core.py
from commit_gen.core import generate_commit_messages
from commit_gen.config import CommitConfig

def test_generate_returns_string(mock_ollama):
    config = CommitConfig(model="gemma4", num_suggestions=1)
    result = generate_commit_messages("diff --git ...", config=config)
    assert isinstance(result, str)
    assert len(result) > 0
```

---

## 🔒 Local vs. Cloud — Why Local Matters

| Aspect | Local (Commit Gen) | Cloud APIs |
|---|---|---|
| **Data Privacy** | Code never leaves your machine | Code sent to third-party servers |
| **Compliance** | GDPR/HIPAA/SOC2 friendly | May violate data policies |
| **Cost** | Free (one-time model download) | Pay per token/request |
| **Latency** | ~1–3s on modern hardware | 2–10s (network + queue) |
| **Availability** | Works offline, on planes, in air-gapped envs | Requires internet |
| **Customization** | Swap models, adjust temperature, custom prompts | Limited to API parameters |
| **Rate Limits** | None | Often throttled |
| **Model Choice** | Any Ollama-compatible model | Vendor lock-in |

---

## ❓ FAQ

<details>
<summary><strong>Which Ollama models work best?</strong></summary>

The default model is **Gemma 4** (`gemma4`), which provides excellent results for code understanding and conventional commit formatting. Other recommended models:

- **`llama3`** — Strong general-purpose model, great for commit messages
- **`codellama`** — Specialized for code, good for technical diffs
- **`mistral`** — Fast and lightweight, suitable for quick suggestions

Change the model in `config.yaml` or via environment variable:
```bash
export OLLAMA_MODEL=llama3
```

</details>

<details>
<summary><strong>How do I handle large diffs?</strong></summary>

Large diffs are automatically truncated to `max_diff_chars` (default: 4000 characters) while preserving diff structure. To handle larger diffs:

```yaml
# config.yaml
max_diff_chars: 8000  # Increase the limit
```

For very large changes, consider committing in smaller, logical chunks — this also produces better commit messages since the LLM can focus on a specific change.

</details>

<details>
<summary><strong>Can I use this without a git repository?</strong></summary>

Yes! Use the `--diff-file` flag or the `from-text` command:

```bash
# From a diff file
commit-gen generate --diff-file changes.diff

# From pasted text
commit-gen from-text "diff --git a/file.py ..."
```

The Web UI also supports pasting diffs directly without git integration.

</details>

<details>
<summary><strong>How do I integrate this into my git workflow?</strong></summary>

You can create a git alias for quick access:

```bash
git config --global alias.ai-commit '!commit-gen generate --staged'
```

Then use:
```bash
git add .
git ai-commit
# Copy the suggestion and:
git commit -m "✨ feat(auth): add token refresh endpoint"
```

Or pipe the diff directly:
```bash
git diff --cached | commit-gen generate
```

</details>

<details>
<summary><strong>What if Ollama is not running?</strong></summary>

The tool checks Ollama connectivity before generating. If Ollama isn't running, you'll see a clear error message. Start Ollama with:

```bash
# Start the Ollama service
ollama serve

# Verify it's running
curl http://localhost:11434/api/tags
```

You can also point to a remote Ollama instance:
```bash
export OLLAMA_BASE_URL=http://remote-server:11434
```

</details>

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

### Development Setup

```bash
# Clone the repo
git clone https://github.com/kennedyraju55/commit-message-generator.git
cd commit-message-generator

# Install dev dependencies
make install-dev

# Run tests to verify setup
make test
```

### Contribution Workflow

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/my-feature`
3. **Make** your changes with tests
4. **Run** the test suite: `make test`
5. **Lint** your code: `make lint`
6. **Commit** with a conventional commit message (use this tool! 😄)
7. **Push** and open a Pull Request

### Makefile Commands

| Command | Description |
|---|---|
| `make install` | Install production dependencies |
| `make install-dev` | Install with dev/test dependencies |
| `make test` | Run test suite |
| `make test-cov` | Run tests with coverage report |
| `make lint` | Run linting checks |
| `make run` | Generate messages from staged changes |
| `make web` | Launch Streamlit web UI |
| `make clean` | Remove cache and temp files |
| `make help` | Show all available commands |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <sub>Built with ❤️ using <a href="https://ollama.com/">Ollama</a> and <a href="https://www.python.org/">Python</a></sub>
  <br/>
  <sub>Part of the <a href="https://github.com/kennedyraju55">Local LLM Projects</a> collection</sub>
  <br/><br/>
  <a href="#-quick-start">⬆ Back to Top</a>
</p>