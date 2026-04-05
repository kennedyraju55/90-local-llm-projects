"""Setup configuration for Court Filing Generator."""

from setuptools import setup, find_packages

setup(
    name="court-filing-generator",
    version="1.0.0",
    description="AI-powered court filing and legal document generator using local LLM",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Court Filing Generator Contributors",
    license="MIT",
    python_requires=">=3.10",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests>=2.31.0",
        "pyyaml>=6.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "streamlit>=1.30.0",
        "fastapi>=0.109.0",
        "uvicorn>=0.27.0",
        "pydantic>=2.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "ruff>=0.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "filing-generator=filing_generator.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Text Processing :: General",
    ],
)
