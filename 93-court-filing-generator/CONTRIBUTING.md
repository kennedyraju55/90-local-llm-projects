# Contributing to Court Filing Generator

Thank you for your interest in contributing! This project generates court filings and legal documents using local AI.

## Getting Started

1. **Fork and clone** the repository
2. **Install dependencies:**
   ```bash
   cd 93-court-filing-generator
   pip install -r requirements.txt
   ```
3. **Install Ollama** and pull the model:
   ```bash
   ollama serve &
   ollama pull gemma4
   ```

## Development Workflow

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Run tests: `python -m pytest tests/ -v`
4. Commit with descriptive messages
5. Push and create a Pull Request

## Code Standards

- **Python 3.10+** required
- **Type hints** on all functions
- **Docstrings** on all public functions and classes
- Follow existing code patterns and style
- Keep all processing local — no external API calls

## Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ -v --cov=src/filing_generator
```

## Adding New Filing Types

1. Add the type to `FilingType` enum in `core.py`
2. Add a template entry to `FILING_TEMPLATES`
3. Update tests in `test_core.py`
4. Update the README filing types table

## Privacy Policy

This project is designed for 100% local processing. **Never** add code that:
- Sends data to external servers
- Logs sensitive case information to remote services
- Requires internet connectivity for core functionality

## Legal Note

⚠️ All generated documents are drafts requiring attorney review. Contributors should not present AI output as legal advice.

## Questions?

Open an issue for bugs, feature requests, or questions.
