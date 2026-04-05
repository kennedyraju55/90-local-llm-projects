"""Setup script for Deposition Summarizer."""

from setuptools import setup, find_packages

setup(
    name="deposition-summarizer",
    version="1.0.0",
    description="AI-powered deposition transcript analysis with complete privacy using local LLM",
    author="Deposition Summarizer Team",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        "rich",
        "click",
        "pyyaml",
        "streamlit",
        "python-dotenv",
    ],
    extras_require={
        "dev": ["pytest", "pytest-cov"],
        "api": ["fastapi", "uvicorn", "pydantic"],
    },
    entry_points={
        "console_scripts": [
            "depo-summarizer=deposition_summarizer.cli:main",
        ],
    },
)
