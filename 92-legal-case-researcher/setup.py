"""Setup configuration for Legal Case Researcher."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="legal-case-researcher",
    version="1.0.0",
    author="Nrk Raju Guthikonda",
    author_email="rajug058@gmail.com",
    description="AI-powered legal case research using local LLMs with complete privacy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kennedyraju55/90-local-llm-projects",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "case-researcher=case_researcher.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Legal Industry",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
)
