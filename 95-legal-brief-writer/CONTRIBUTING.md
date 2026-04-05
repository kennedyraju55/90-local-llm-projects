# Contributing to Legal Brief Writer

Thank you for your interest in contributing! This project is part of the
[90 Local LLM Projects](https://github.com/kennedyraju55/90-local-llm-projects) monorepo.

## Getting Started

1. **Fork & clone** the repository
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run tests**: `python -m pytest tests/ -v`

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install in development mode
pip install -r requirements.txt
pip install -e .

# Ensure Ollama is running for integration tests
ollama serve &
ollama pull gemma4:latest
```

## Making Changes

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make your changes with clear commit messages
3. Add or update tests as appropriate
4. Ensure all tests pass: `python -m pytest tests/ -v`
5. Submit a pull request

## Code Style

- Follow PEP 8 conventions
- Use type hints for function signatures
- Add docstrings for public functions and classes
- Keep functions focused and under 50 lines when possible

## Testing

- Write unit tests for all new functions
- Mock LLM calls in tests (never require a running Ollama instance for unit tests)
- Aim for 80%+ code coverage

## Project Structure

```
src/brief_writer/     # Main package
├── core.py           # Core logic and LLM interaction
├── cli.py            # Click CLI interface
├── web_ui.py         # Streamlit web interface
├── api.py            # FastAPI REST API
└── config.py         # Configuration management
tests/                # Test files
examples/             # Usage examples
```

## Privacy Commitment

This project processes all data locally. When contributing:
- **Never** add external API calls or telemetry
- **Never** log or transmit user content
- Ensure all LLM calls go through the local Ollama instance only

## Reporting Issues

- Use GitHub Issues with clear descriptions
- Include steps to reproduce bugs
- Mention your Python version and OS

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
