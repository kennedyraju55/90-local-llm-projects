"""Setup configuration for Legal Brief Writer."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="legal-brief-writer",
    version="1.0.0",
    description="AI-powered legal brief and memoranda generation with complete privacy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="NRK Raju Guthikonda",
    author_email="rajug058@gmail.com",
    url="https://github.com/kennedyraju55/90-local-llm-projects",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "brief-writer=brief_writer.cli:main",
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
        "Topic :: Text Processing :: General",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
