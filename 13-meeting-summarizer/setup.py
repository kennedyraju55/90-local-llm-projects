"""Setup script for Meeting Summarizer."""

from setuptools import setup, find_packages

setup(
    name="meeting-summarizer",
    version="1.0.0",
    description="Production-grade meeting transcript summarizer using local LLM",
    python_requires=">=3.11",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests", "rich", "click", "pyyaml", "streamlit", "python-dotenv",
    ],
    extras_require={"dev": ["pytest", "pytest-cov"]},
    entry_points={"console_scripts": ["meeting-summarizer=meeting_summarizer.cli:main"]},
)
