<div align="center">

<img src="docs/images/banner.svg" alt="Research Paper Q&A Banner" width="800"/>

<br/><br/>

[![Python](https://img.shields.io/badge/Python-3.9+-3776ab?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-f72585?style=flat-square&logo=ollama&logoColor=white)](https://ollama.com)
[![Gemma 4](https://img.shields.io/badge/Gemma_4-Google-b5179e?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Click](https://img.shields.io/badge/Click-CLI-7209b7?style=flat-square&logo=gnu-bash&logoColor=white)](https://click.palletsprojects.com)
[![Rich](https://img.shields.io/badge/Rich-Terminal_UI-f72585?style=flat-square)](https://rich.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

[Getting Started](#-getting-started) •
[Features](#-features) •
[Architecture](#-architecture) •
[Usage](#-usage) •
[API Reference](#-api-reference) •
[FAQ](#-faq)

</div>

---


## 🐳 Docker Deployment

Run this project instantly with Docker — no local Python setup needed!

### Quick Start with Docker

```bash
# Clone and start
git clone https://github.com/kennedyraju55/research-paper-qa.git
cd research-paper-qa
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

## ⚡ REST API

Every project includes a FastAPI REST API with auto-generated docs.

### Start the API Server

```bash
# Run directly
uvicorn src.research_qa.api:app --reload --port 8000

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

## 🧐 Why This Project?

Researchers are **drowning in papers**. The average scientist reads 250+ papers per year, and that
number keeps climbing. Every literature review means hours of re-reading, flipping between PDFs, and
trying to remember which paper said what about a specific methodology.

**Research Paper Q&A** changes that workflow entirely:

- 📄 **Load a paper** (or several) and start asking questions in plain English.
- 📎 **Every answer comes with citations** — `[Paper: filename, Section: X]` — so you can verify
  claims instantly instead of hunting through pages.
- 💡 **AI-generated follow-up questions** guide you deeper into the material, surfacing angles you
  might have missed.
- 🔒 **Everything runs locally** on your machine via Ollama. No cloud APIs, no subscriptions, no
  research data leaving your laptop.

Whether you're doing a literature review, preparing for a journal club, or just trying to understand
a dense methods section, this tool turns a 30-minute reading session into a 5-minute Q&A
conversation.

---

## ✨ Features

<div align="center">
<img src="docs/images/features.svg" alt="Features Overview" width="800"/>
</div>

<br/>

| Feature | Description |
|---------|-------------|
| **Interactive Q&A** | Ask natural-language questions about your papers and receive cited answers with full conversation context |
| **Multi-Paper Support** | Load multiple papers simultaneously and cross-reference findings across them |
| **Citation Tracking** | Automatic extraction in structured `[Paper: filename, Section: X]` format for easy verification |
| **Follow-up Suggestions** | AI-generated next questions to guide deeper exploration of the research material |
| **Conversation Memory** | Full context maintained across your entire session for coherent multi-turn dialogue |
| **100% Private** | All processing happens locally via Ollama — your research data never leaves your machine |
| **Notes Export** | Export your Q&A session to Markdown for later reference |
| **YAML Configuration** | Customize model parameters, follow-up count, and more via `config.yaml` |
| **Rich Terminal UI** | Beautiful terminal interface powered by Rich with syntax highlighting and formatted output |

---

## 🏗️ Architecture

<div align="center">
<img src="docs/images/architecture.svg" alt="System Architecture" width="800"/>
</div>

<br/>

The system follows a clean five-stage pipeline:

1. **Research Papers** — Plain-text `.txt` or `.md` files containing your paper content.
2. **Paper Loader** — `load_paper()` reads a single file; `load_multiple_papers()` reads several
   and returns a `dict` mapping each filename to its content.
3. **System Prompt Builder** — `build_system_prompt()` embeds the paper text into a carefully
   crafted system prompt. For multi-paper sessions, `build_multi_paper_content()` combines papers
   with `=== Paper: filename ===` separators.
4. **Gemma 4 via Ollama** — The LLM engine handles three responsibilities:
   - **Q&A Engine** (`ask_question()`) — Answers questions with citations, maintaining conversation
     history.
   - **Citation Extractor** (`extract_citations()`) — Parses `[Paper: filename, Section: X]`
     references from answers using regex.
   - **Follow-up Suggester** (`suggest_followup_questions()`) — Generates numbered follow-up
     questions based on conversation context.
5. **Interactive Session** — The Click-powered CLI presents results with Rich formatting, tracks
   history, and supports export.

---

## 🚀 Getting Started

### Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.9+ | Runtime |
| Ollama | Latest | Local LLM server |
| Gemma 4 | Latest | Language model |
| ~16 GB RAM | — | Recommended for Gemma 4 |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/kennedyraju55/research-paper-qa.git
cd research-paper-qa

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Start Ollama and pull the model
ollama serve
ollama pull gemma4
```

### Verify Installation

```bash
# Check that Ollama is running and the model is available
ollama list | grep gemma4

# Run the test suite
python -m pytest tests/ -v
```

---

## 📖 Usage

### Quick Start — Single Paper

```bash
python -m src.research_qa.cli --paper papers/attention_is_all_you_need.txt
```

### Multi-Paper Session

```bash
python -m src.research_qa.cli \
    --paper papers/attention_is_all_you_need.txt \
    --paper papers/bert_pre_training.txt \
    --paper papers/gpt2_language_models.txt
```

### With Custom Config and Verbose Logging

```bash
python -m src.research_qa.cli \
    --paper papers/my_paper.txt \
    --config config.yaml \
    --verbose
```

### CLI Options

| Option | Required | Default | Description |
|--------|----------|---------|-------------|
| `--paper` | Yes | — | Path to a paper file. Repeat for multiple papers. |
| `--config` | No | `config.yaml` | Path to YAML configuration file. |
| `--verbose` | No | Off | Enable debug-level logging output. |

---

## 💬 Interactive Commands

Once the session starts, you interact through a Rich-powered prompt:

| Command | Description |
|---------|-------------|
| `<question>` | Ask any question about the loaded paper(s) |
| `suggest` | Get AI-generated follow-up question suggestions |
| `history` | View the full conversation history |
| `export [file]` | Export notes to a file (default: `qa_notes.md`) |
| `clear` | Reset conversation history and start fresh |
| `quit` / `exit` | End the session |

### Example Interactive Session

```
$ python -m src.research_qa.cli --paper papers/attention_is_all_you_need.txt

╭──────────────────────────────────────────────────────────────────╮
│  🔬 Research Paper Q&A                                          │
│  Loaded: attention_is_all_you_need.txt                          │
│  Model: gemma4 via Ollama                                       │
╰──────────────────────────────────────────────────────────────────╯

📄 Paper loaded successfully (47,832 characters)
Type your questions below. Type 'quit' to exit.

────────────────────────────────────────────────────────────────────

❓ You: What is the main contribution of this paper?

🤖 Assistant:
The main contribution of this paper is the Transformer architecture, a novel
sequence transduction model based entirely on attention mechanisms, dispensing
with recurrence and convolutions entirely.

The authors demonstrate that the Transformer achieves superior performance on
machine translation tasks while being significantly more parallelizable and
requiring less time to train than architectures based on recurrent or
convolutional layers.

Key innovations include:
• Multi-Head Attention — allows the model to jointly attend to information
  from different representation subspaces at different positions
• Scaled Dot-Product Attention — a specific attention function used within
  each head
• Positional Encoding — since the model contains no recurrence, positional
  encodings are added to give the model information about token order

[Paper: attention_is_all_you_need.txt, Section: Abstract]
[Paper: attention_is_all_you_need.txt, Section: Introduction]

────────────────────────────────────────────────────────────────────

❓ You: How does multi-head attention differ from single-head attention?

🤖 Assistant:
Multi-head attention extends single-head attention by running multiple attention
functions in parallel, each with different learned linear projections.

In single-head attention, you compute one set of attention weights over the full
d_model-dimensional keys, queries, and values. The limitation is that the single
attention head averages across all positions, which can inhibit the model from
focusing on multiple relevant aspects simultaneously.

Multi-head attention addresses this by:
1. Projecting queries, keys, and values h times with different learned linear
   projections to d_k, d_k, and d_v dimensions respectively
2. Running the attention function in parallel on each of these projected
   versions, yielding d_v-dimensional output values
3. Concatenating the outputs and projecting once more to get the final result

The paper uses h=8 parallel attention heads, with d_k = d_v = d_model/h = 64.
This allows each head to specialize — some heads learn to attend to syntactic
relationships, while others capture semantic or positional patterns.

[Paper: attention_is_all_you_need.txt, Section: 3.2.2 Multi-Head Attention]

────────────────────────────────────────────────────────────────────

❓ You: suggest

💡 Follow-up Suggestions:
  1. What are the computational advantages of the Transformer over RNNs and
     CNNs as discussed in the paper?
  2. How do positional encodings work, and why are they necessary in the
     Transformer architecture?
  3. What were the specific BLEU score results on WMT 2014, and how did they
     compare to previous state-of-the-art?

────────────────────────────────────────────────────────────────────

❓ You: history

📝 Conversation History (2 exchanges):

  [1] You: What is the main contribution of this paper?
      AI:  The main contribution of this paper is the Transformer
           architecture, a novel sequence transduction model based
           entirely on attention mechanisms...

  [2] You: How does multi-head attention differ from single-head attention?
      AI:  Multi-head attention extends single-head attention by running
           multiple attention functions in parallel...

────────────────────────────────────────────────────────────────────

❓ You: export session_notes.md

📤 Notes exported to session_notes.md

────────────────────────────────────────────────────────────────────

❓ You: quit

👋 Goodbye! Session ended.
```

### Multi-Paper Session Example

```
$ python -m src.research_qa.cli \
    --paper papers/attention.txt \
    --paper papers/bert.txt

╭──────────────────────────────────────────────────────────────────╮
│  🔬 Research Paper Q&A                                          │
│  Loaded: attention.txt, bert.txt                                │
│  Model: gemma4 via Ollama                                       │
╰──────────────────────────────────────────────────────────────────╯

📄 2 papers loaded successfully
Type your questions below. Type 'quit' to exit.

────────────────────────────────────────────────────────────────────

❓ You: How does BERT build upon the Transformer architecture?

🤖 Assistant:
BERT builds directly upon the Transformer architecture by using the encoder
portion of the original Transformer model. While the original Transformer uses
both an encoder and a decoder stack for sequence-to-sequence tasks, BERT uses
only the encoder for bidirectional pre-training.

Key differences and extensions:
• Bidirectional context — Unlike the original Transformer which processes
  left-to-right in the decoder, BERT trains bidirectionally using Masked
  Language Modeling (MLM)
• Pre-training + Fine-tuning — BERT introduces a two-stage approach where
  the Transformer encoder is first pre-trained on unlabeled text, then
  fine-tuned on downstream tasks
• [CLS] token — BERT adds a special classification token whose final
  hidden state serves as the aggregate sequence representation

Both papers share the core multi-head attention mechanism and the same scaled
dot-product attention formulation.

[Paper: bert.txt, Section: 3 BERT]
[Paper: attention.txt, Section: 3.2.2 Multi-Head Attention]
[Paper: bert.txt, Section: 3.1 Pre-training BERT]
```

---

## 📚 API Reference

### `load_paper(paper_path)`

Reads a single paper file and returns its content as a string.

```python
from research_qa.core import load_paper

content = load_paper("papers/my_paper.txt")
print(f"Loaded {len(content)} characters")
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `paper_path` | `str` | Path to the paper file (`.txt` or `.md`) |

**Returns:** `str` — The full text content of the paper.

**Raises:** `FileNotFoundError` — If the specified file does not exist.

---

### `load_multiple_papers(paper_paths)`

Reads multiple paper files and returns a dictionary mapping each filename to its content.

```python
from research_qa.core import load_multiple_papers

papers = load_multiple_papers([
    "papers/attention.txt",
    "papers/bert.txt",
])
for name, content in papers.items():
    print(f"{name}: {len(content)} chars")
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `paper_paths` | `list[str]` | List of file paths to paper files |

**Returns:** `dict[str, str]` — Mapping of `filename → content`.

---

### `build_system_prompt(paper_content)`

Constructs a formatted system prompt with the paper content embedded for the LLM.

```python
from research_qa.core import build_system_prompt

prompt = build_system_prompt(content)
# Returns a system prompt string with instructions and the full paper text
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `paper_content` | `str` | The text content of the paper |

**Returns:** `str` — A formatted system prompt ready for the LLM.

---

### `build_multi_paper_content(papers)`

Combines multiple papers into a single string with clear separators.

```python
from research_qa.core import build_multi_paper_content

combined = build_multi_paper_content(papers)
# Output format:
# === Paper: attention.txt ===
# <content>
# === Paper: bert.txt ===
# <content>
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `papers` | `dict[str, str]` | Dictionary mapping filename to paper content |

**Returns:** `str` — Combined paper content with `=== Paper: filename ===` separators.

---

### `ask_question(question, conversation_history, system_prompt, config=None)`

Sends a question to the LLM with conversation context and returns the answer.

```python
from research_qa.core import ask_question

history = []
answer = ask_question(
    question="What is the main finding?",
    conversation_history=history,
    system_prompt=prompt,
)
# `history` is mutated — the Q&A pair is appended automatically
print(answer)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `question` | `str` | — | The user's question |
| `conversation_history` | `list` | — | Mutable list of conversation turns; appended to automatically |
| `system_prompt` | `str` | — | The system prompt with embedded paper content |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** `str` — The LLM's answer, potentially containing citation references.

---

### `suggest_followup_questions(conversation_history, system_prompt, num_suggestions=3, config=None)`

Generates follow-up question suggestions based on the conversation so far.

```python
from research_qa.core import suggest_followup_questions

suggestions = suggest_followup_questions(
    conversation_history=history,
    system_prompt=prompt,
    num_suggestions=3,
)
for s in suggestions:
    print(s)
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `conversation_history` | `list` | — | The current conversation history |
| `system_prompt` | `str` | — | The system prompt with embedded paper content |
| `num_suggestions` | `int` | `3` | Number of follow-up questions to generate |
| `config` | `dict \| None` | `None` | Optional configuration overrides |

**Returns:** `list[str]` — A numbered list of suggested follow-up questions.

---

### `extract_citations(answer)`

Extracts citation references from an LLM answer using regex pattern matching.

```python
from research_qa.core import extract_citations

citations = extract_citations(answer)
# Returns: ["[Paper: attention.txt, Section: 3.2.2]", ...]
```

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `answer` | `str` | The LLM's answer text |

**Returns:** `list[str]` — List of citation strings in `[Paper: filename, Section: X]` format.

---

## ⚙️ Configuration

Configuration is managed through `config.yaml`:

```yaml
# config.yaml
qa:
  num_followup_suggestions: 3
```

### Configuration Options

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `qa.num_followup_suggestions` | `int` | `3` | Number of follow-up suggestions generated by `suggest_followup_questions()` |

You can pass a custom config file via the CLI:

```bash
python -m src.research_qa.cli --paper paper.txt --config my_config.yaml
```

---

## 🧪 Testing

```bash
# Run the full test suite
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src.research_qa

# Run a specific test file
python -m pytest tests/test_core.py -v
```

---

## 📂 Project Structure

```
20-research-paper-qa/
├── docs/
│   └── images/
│       ├── banner.svg              # Project banner
│       ├── architecture.svg        # System architecture diagram
│       └── features.svg            # Feature highlights
├── src/
│   └── research_qa/
│       ├── __init__.py             # Package init
│       ├── core.py                 # Core Q&A, citation, and suggestion logic
│       ├── cli.py                  # Click CLI with interactive session
│       └── config.py              # YAML configuration loader
├── tests/
│   ├── test_core.py               # Core function tests
│   └── test_cli.py                # CLI integration tests
├── common/
│   └── llm_client.py             # Shared Ollama client wrapper
├── config.yaml                    # Default configuration
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── Makefile                       # Build and dev commands
├── .env.example                   # Environment variable template
├── .gitignore
└── README.md                      # This file
```

---

## 🔧 Dependencies

| Package | Purpose |
|---------|---------|
| [Click](https://click.palletsprojects.com) | CLI framework with option parsing and help generation |
| [Rich](https://rich.readthedocs.io) | Terminal formatting, prompts, and styled output |
| [Ollama](https://github.com/ollama/ollama-python) | Python client for the local Ollama LLM server |
| [Regex](https://pypi.org/project/regex/) | Advanced regex for citation extraction patterns |

---

## ❓ FAQ

### What paper formats are supported?

Currently, the tool accepts **plain-text** (`.txt`) and **Markdown** (`.md`) files. PDF support is
not built in — you'll need to convert PDFs to text first using a tool like `pdftotext`, `pymupdf`,
or copy-paste from your PDF reader.

```bash
# Example: convert PDF to text with pdftotext
pdftotext paper.pdf paper.txt

# Then load it
python -m src.research_qa.cli --paper paper.txt
```

### How accurate are the citations?

Citations are extracted using regex pattern matching on the LLM's output. The model is instructed
(via the system prompt) to cite its sources in `[Paper: filename, Section: X]` format. Accuracy
depends on:

- **Paper structure** — Well-structured papers with clear section headings produce better citations.
- **Question specificity** — Specific questions yield more precise citations than broad ones.
- **Model capability** — Gemma 4 generally produces reliable citations, but always verify critical
  claims against the original paper.

The `extract_citations()` function uses regex to parse references, so it will capture any text
matching the `[Paper: ..., Section: ...]` pattern.

### Is there a limit on how many papers I can load?

There is no hard-coded limit, but practical constraints apply:

- **Context window** — Gemma 4's context window determines how much text the model can process at
  once. Very long papers or many papers may exceed this limit.
- **RAM** — Each paper's content is held in memory. Loading dozens of large papers will increase
  memory usage.
- **Quality** — With more papers loaded, the model has more context to search through, which can
  sometimes reduce answer precision.

**Recommended:** 1–5 papers per session for optimal quality. For large literature reviews, consider
batching papers into thematic groups.

### Can I use a different model instead of Gemma 4?

Yes. You can configure a different Ollama-compatible model by updating the model setting in your
`config.yaml` or environment variables. Any model available through `ollama list` can be used. Keep
in mind that citation quality varies by model.

### Does my data leave my machine?

**No.** The entire pipeline runs locally:

- Ollama runs the LLM on your hardware.
- Paper files are read from your local filesystem.
- No API calls are made to external services.
- No telemetry or usage data is collected.

Your research data stays on your machine at all times.

### How do I reset the conversation without restarting?

Use the `clear` command in the interactive session:

```
❓ You: clear
🔄 Conversation cleared. Starting fresh.
```

This resets the conversation history while keeping the paper(s) loaded.

### Can I export my Q&A session?

Yes! Use the `export` command:

```
❓ You: export                    # Exports to qa_notes.md (default)
❓ You: export my_notes.md        # Exports to a custom filename
```

The exported file contains the full conversation history in Markdown format, including questions,
answers, and citations.

### Why am I getting slow responses?

Response speed depends on:

- **Hardware** — GPU acceleration significantly improves inference speed. CPU-only mode works but is
  slower.
- **Paper length** — Longer papers mean more context for the model to process.
- **Number of papers** — Multi-paper sessions require more processing per query.
- **Model size** — Gemma 4 is a capable model; ensure your system meets the RAM requirements
  (~16 GB recommended).

### How does conversation memory work?

The `ask_question()` function maintains a `conversation_history` list that is passed to every LLM
call. Each Q&A exchange is appended to this list, giving the model full context of prior questions
and answers. This enables:

- **Follow-up questions** — "Can you elaborate on that?" works because the model sees the prior
  answer.
- **Pronoun resolution** — "What does it mean?" correctly resolves "it" based on conversation
  context.
- **Progressive exploration** — Each question builds on the previous answers.

The `clear` command resets this history list.

---

## 🗺️ Roadmap

- [ ] PDF parsing support (direct `.pdf` file loading)
- [ ] Streaming responses for real-time output
- [ ] Semantic search across paper sections
- [ ] BibTeX citation export format
- [ ] Batch question mode for automated analysis
- [ ] Configurable citation format styles

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

<div align="center">

**Part of the [90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) collection**

Built with ❤️ using [Ollama](https://ollama.com) • [Gemma 4](https://ai.google.dev/gemma) • [Click](https://click.palletsprojects.com) • [Rich](https://rich.readthedocs.io)

</div>
