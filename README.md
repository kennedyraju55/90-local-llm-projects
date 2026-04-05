<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=280&section=header&text=90%20Local%20LLM%20Projects&fontSize=52&fontAlignY=35&desc=Production-Level%20AI%20Apps%20%E2%80%A2%20100%25%20Private%20%E2%80%A2%20Zero%20Cloud%20Costs&descSize=20&descAlignY=55&animation=fadeIn" width="100%"/>

<br/>

### 🧠 Built with Gemma 4 + Ollama · Fully Offline · Your Data Never Leaves Your Machine

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge&logo=ollama&logoColor=white)](https://ollama.ai)
[![Gemma](https://img.shields.io/badge/Gemma_4-Google_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)](LICENSE)
[![Projects](https://img.shields.io/badge/🚀_Projects-90-FF6B6B?style=for-the-badge)]()
[![Tests](https://img.shields.io/badge/✅_Tests-2400+-00C853?style=for-the-badge)]()
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)]()
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)]()

<br/>

<table>
<tr>
<td align="center"><strong>🤖<br/>90<br/>Projects</strong></td>
<td align="center"><strong>📂<br/>9<br/>Categories</strong></td>
<td align="center"><strong>✅<br/>2400+<br/>Tests</strong></td>
<td align="center"><strong>🚀<br/>500+<br/>API Endpoints</strong></td>
<td align="center"><strong>🎨<br/>270<br/>SVGs</strong></td>
<td align="center"><strong>🐳<br/>Docker<br/>Ready</strong></td>
</tr>
</table>

<br/>

> **🔒 Your data never leaves your machine.** Every single project runs entirely on your local hardware using Gemma 4 via Ollama. No API keys. No cloud costs. No data sharing. Ever.

<br/>

<a href="https://kennedyraju55.github.io/90-local-llm-projects/">
  <img src="https://img.shields.io/badge/📖_Read_the_Web_Book-View_Online-blue?style=for-the-badge&logoColor=white" alt="Web Book"/>
</a>

</div>

---

## 📋 Table of Contents

<details>
<summary>Click to expand navigation</summary>

- [🌟 Why Local LLMs?](#-why-local-llms)
- [⚡ Quick Start](#-quick-start)
- [📦 What's Inside Each Project](#-whats-inside-each-project)
- [📂 All 90 Projects](#-all-90-projects)
  - [🤖 Chatbots & Conversational AI (01–10)](#-category-1-chatbots--conversational-ai)
  - [📄 Document Processing & Analysis (11–20)](#-category-2-document-processing--analysis)
  - [💻 Code & Developer Tools (21–30)](#-category-3-code--developer-tools)
  - [✍️ Content Creation & Writing (31–40)](#️-category-4-content-creation--writing)
  - [📊 Data & Business Intelligence (41–50)](#-category-5-data--business-intelligence)
  - [🎓 Education & Learning (51–60)](#-category-6-education--learning)
  - [🏠 Personal Productivity (61–70)](#-category-7-personal-productivity)
  - [🔒 Security, Privacy & DevOps (71–80)](#-category-8-security-privacy--devops)
  - [🏥 Healthcare & Wellness (81–90)](#-category-9-healthcare--wellness)
- [🏗️ Architecture](#️-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Repository Structure](#-repository-structure)
- [🌐 Web Book](#-web-book)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

</details>

---

## 🌟 Why Local LLMs?

<div align="center">

| | Feature | ☁️ Cloud LLMs | 🏠 Local LLMs (This Repo) |
|---|---------|:---:|:---:|
| 🔒 | **Privacy** | Data sent to servers | ✅ **Data stays on YOUR machine** |
| 💰 | **Cost** | Pay per token | ✅ **Completely free forever** |
| 🌐 | **Internet** | Required always | ✅ **Works fully offline** |
| ⚡ | **Latency** | Network round-trips | ✅ **Instant local inference** |
| 🎛️ | **Control** | Limited customization | ✅ **Full model control** |
| 📊 | **Data Governance** | Subject to third-party policies | ✅ **Your data, your rules** |
| 🏢 | **Enterprise Ready** | Compliance concerns | ✅ **Air-gap compatible** |

</div>

---

## ⚡ Quick Start

### Prerequisites

```bash
# 1. Install Ollama → https://ollama.ai
# 2. Pull the Gemma 4 model
ollama pull gemma4

# 3. Clone this repo
git clone https://github.com/kennedyraju55/90-local-llm-projects.git
cd 90-local-llm-projects

# 4. Install base dependencies
pip install -r requirements-base.txt
```

### Run Any Project

```bash
# Pick any project (1-90) and run it!
cd 01-pdf-chat-assistant
pip install -r requirements.txt
python app.py --help
```

> 💡 **Each of the 90 projects also lives in its own dedicated GitHub repo** — click any project link below to explore it individually!

---

## 📦 What's Inside Each Project

Every project follows the same production-grade structure:

```
each-project/
├── src/{module}/
│   ├── core.py          # Business logic + LLM integration
│   ├── cli.py           # Click CLI interface
│   ├── web_ui.py        # Streamlit web UI (dark theme)
│   ├── api.py           # FastAPI REST API
│   └── config.py        # Configuration
├── tests/               # pytest test suite
├── examples/demo.py     # Usage examples
├── docs/images/         # SVG diagrams
├── Dockerfile            # Multi-stage Docker build
├── docker-compose.yml   # Full stack with Ollama
├── .github/workflows/   # CI/CD pipeline
├── CONTRIBUTING.md
├── CHANGELOG.md
└── README.md            # 500+ line documentation
```

---

## 📂 All 90 Projects

### 🤖 Category 1: Chatbots & Conversational AI

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 01 | [**PDF Chat Assistant**](https://github.com/kennedyraju55/pdf-chat-assistant) | Ask questions about PDFs | PDF parsing, context-aware Q&A |
| 02 | [**IT Helpdesk Bot**](https://github.com/kennedyraju55/it-helpdesk-bot) | Local IT support chatbot | Troubleshooting, knowledge base |
| 03 | [**Meal Planner Bot**](https://github.com/kennedyraju55/meal-planner-bot) | Recipe & meal suggestions | Dietary preferences, weekly plans |
| 04 | [**Fitness Coach Bot**](https://github.com/kennedyraju55/fitness-coach-bot) | Personalized workout plans | Equipment-aware, progressive |
| 05 | [**Travel Itinerary Bot**](https://github.com/kennedyraju55/travel-itinerary-bot) | Vacation planning assistant | Budget-aware, day-by-day plans |
| 06 | [**Language Learning Bot**](https://github.com/kennedyraju55/language-learning-bot) | Practice conversations | Grammar correction, levels |
| 07 | [**Veterinary Advisor Bot**](https://github.com/kennedyraju55/veterinary-advisor-bot) | Pet health chatbot | Species-specific advice |
| 08 | [**Gift Recommendation Bot**](https://github.com/kennedyraju55/gift-recommendation-bot) | Personalized gift ideas | Occasion & budget aware |
| 09 | [**Study Buddy Bot**](https://github.com/kennedyraju55/study-buddy-bot) | Exam preparation helper | Quizzing, concept explanations |
| 10 | [**Mood Journal Bot**](https://github.com/kennedyraju55/mood-journal-bot) | Private mood tracking | Sentiment analysis, patterns |

### 📄 Category 2: Document Processing & Analysis

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 11 | [**Legal Doc Summarizer**](https://github.com/kennedyraju55/legal-doc-summarizer) | Contract & legal analysis | Key clauses, obligations |
| 12 | [**Resume Analyzer**](https://github.com/kennedyraju55/resume-analyzer) | Resume optimization tool | Job matching, scoring |
| 13 | [**Meeting Summarizer**](https://github.com/kennedyraju55/meeting-summarizer) | Transcript to action items | Decisions, follow-ups |
| 14 | [**Medical Lit Summarizer**](https://github.com/kennedyraju55/medical-lit-summarizer) | Research paper summaries | Methodology, findings |
| 15 | [**Invoice Extractor**](https://github.com/kennedyraju55/invoice-extractor) | Receipt data extraction | Structured JSON output |
| 16 | [**PDF Report Generator**](https://github.com/kennedyraju55/pdf-report-generator) | Auto report generation | Data-driven narratives |
| 17 | [**Textbook Summarizer**](https://github.com/kennedyraju55/textbook-summarizer) | Chapter summaries | Key concepts, definitions |
| 18 | [**Policy Compliance Checker**](https://github.com/kennedyraju55/policy-compliance-checker) | Regulation review | Compliance scoring |
| 19 | [**News Digest Generator**](https://github.com/kennedyraju55/news-digest-generator) | RSS feed summarization | Topic grouping |
| 20 | [**Research Paper Q&A**](https://github.com/kennedyraju55/research-paper-qa) | Academic Q&A assistant | Citation-aware answers |

### 💻 Category 3: Code & Developer Tools

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 21 | [**Code Review Bot**](https://github.com/kennedyraju55/code-review-bot) | Code review & bug detection | Security, performance focus |
| 22 | [**Commit Message Generator**](https://github.com/kennedyraju55/commit-message-generator) | Smart git commits | Conventional commits |
| 23 | [**Stack Trace Explainer**](https://github.com/kennedyraju55/stack-trace-explainer) | Debug helper | Plain English errors |
| 24 | [**Regex Generator**](https://github.com/kennedyraju55/regex-generator) | Pattern builder & explainer | Generate & explain regex |
| 25 | [**API Doc Generator**](https://github.com/kennedyraju55/api-doc-generator) | Auto API documentation | Function extraction |
| 26 | [**Code Snippet Search**](https://github.com/kennedyraju55/code-snippet-search) | Local code finder | NL-powered search |
| 27 | [**SQL Query Generator**](https://github.com/kennedyraju55/sql-query-generator) | Natural language to SQL | Schema-aware |
| 28 | [**Code Translator**](https://github.com/kennedyraju55/code-translator) | Language converter | 5+ languages |
| 29 | [**Unit Test Generator**](https://github.com/kennedyraju55/unit-test-generator) | Auto test writing | pytest output |
| 30 | [**Code Complexity Analyzer**](https://github.com/kennedyraju55/code-complexity-analyzer) | Quality metrics | Readability scores |

### ✍️ Category 4: Content Creation & Writing

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 31 | [**Blog Post Generator**](https://github.com/kennedyraju55/blog-post-generator) | SEO-friendly articles | Tone control, keywords |
| 32 | [**Social Media Writer**](https://github.com/kennedyraju55/social-media-writer) | Multi-platform posts | Platform-specific |
| 33 | [**Email Campaign Writer**](https://github.com/kennedyraju55/email-campaign-writer) | Marketing copy | A/B variants |
| 34 | [**Poem & Lyrics Generator**](https://github.com/kennedyraju55/poem-lyrics-generator) | Creative writing | Multiple styles |
| 35 | [**Video Script Writer**](https://github.com/kennedyraju55/video-script-writer) | YouTube scripts | Timestamps, B-roll |
| 36 | [**Newsletter Editor**](https://github.com/kennedyraju55/newsletter-editor) | Content curation | Section formatting |
| 37 | [**Story Outline Generator**](https://github.com/kennedyraju55/story-outline-generator) | Fiction planning | Characters, plots |
| 38 | [**Product Description Writer**](https://github.com/kennedyraju55/product-description-writer) | E-commerce copy | SEO-optimized |
| 39 | [**Presentation Generator**](https://github.com/kennedyraju55/presentation-generator) | Slide scripts | Speaker notes |
| 40 | [**Cover Letter Generator**](https://github.com/kennedyraju55/cover-letter-generator) | Job applications | Resume matching |

### 📊 Category 5: Data & Business Intelligence

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 41 | [**CSV Data Analyzer**](https://github.com/kennedyraju55/csv-data-analyzer) | Upload & analyze CSVs | NL queries, pandas |
| 42 | [**Sentiment Analysis Dashboard**](https://github.com/kennedyraju55/sentiment-analysis-dashboard) | Customer feedback | Confidence scores |
| 43 | [**Survey Response Analyzer**](https://github.com/kennedyraju55/survey-response-analyzer) | Insights extraction | Theme grouping |
| 44 | [**Stock Report Generator**](https://github.com/kennedyraju55/stock-report-generator) | Financial analysis | Trend narrative |
| 45 | [**Competitor Analysis Tool**](https://github.com/kennedyraju55/competitor-analysis-tool) | Market research | SWOT analysis |
| 46 | [**Support Ticket Classifier**](https://github.com/kennedyraju55/support-ticket-classifier) | Auto routing | Priority scoring |
| 47 | [**Financial Report Generator**](https://github.com/kennedyraju55/financial-report-generator) | Accounting summaries | Period comparison |
| 48 | [**Sales Email Generator**](https://github.com/kennedyraju55/sales-email-generator) | Outreach copy | Personalization |
| 49 | [**KPI Dashboard Reporter**](https://github.com/kennedyraju55/kpi-dashboard-reporter) | Business metrics | Trend highlights |
| 50 | [**Trend Analysis Tool**](https://github.com/kennedyraju55/trend-analysis-tool) | Market trends | Topic detection |

### 🎓 Category 6: Education & Learning

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 51 | [**Quiz Generator**](https://github.com/kennedyraju55/quiz-generator) | Auto assessments | Multiple formats |
| 52 | [**Flashcard Creator**](https://github.com/kennedyraju55/flashcard-creator) | Study cards | Review mode |
| 53 | [**Essay Grader**](https://github.com/kennedyraju55/essay-grader) | Writing evaluation | Rubric scoring |
| 54 | [**Curriculum Planner**](https://github.com/kennedyraju55/curriculum-planner) | Course design | Weekly breakdown |
| 55 | [**Science Experiment Explainer**](https://github.com/kennedyraju55/science-experiment-explainer) | Lab guides | Safety, materials |
| 56 | [**Math Problem Solver**](https://github.com/kennedyraju55/math-problem-solver) | Step-by-step solutions | Multi-topic |
| 57 | [**History Timeline Generator**](https://github.com/kennedyraju55/history-timeline-generator) | Event summaries | Key dates |
| 58 | [**Vocabulary Builder**](https://github.com/kennedyraju55/vocabulary-builder) | Word learning | Quiz mode |
| 59 | [**Debate Topic Generator**](https://github.com/kennedyraju55/debate-topic-generator) | Critical thinking | Pro/con arguments |
| 60 | [**Reading Comprehension Builder**](https://github.com/kennedyraju55/reading-comprehension-builder) | Passage analysis | Q&A generation |

### 🏠 Category 7: Personal Productivity

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 61 | [**Smart Calendar Assistant**](https://github.com/kennedyraju55/smart-calendar-assistant) | Schedule optimization | Meeting suggestions |
| 62 | [**Personal Knowledge Base**](https://github.com/kennedyraju55/personal-knowledge-base) | Semantic search notes | AI-powered search |
| 63 | [**Diary Journal Organizer**](https://github.com/kennedyraju55/diary-journal-organizer) | Private notes | AI insights |
| 64 | [**Household Budget Analyzer**](https://github.com/kennedyraju55/household-budget-analyzer) | Expense tracking | Category breakdown |
| 65 | [**Reading List Manager**](https://github.com/kennedyraju55/reading-list-manager) | Book summaries | Recommendations |
| 66 | [**Home Automation Scripter**](https://github.com/kennedyraju55/home-automation-scripter) | IoT scripts | YAML configs |
| 67 | [**Family Story Creator**](https://github.com/kennedyraju55/family-story-creator) | Memory preservation | Narrative generation |
| 68 | [**Habit Tracker Analyzer**](https://github.com/kennedyraju55/habit-tracker-analyzer) | Behavior analysis | Streak tracking |
| 69 | [**Standup Generator**](https://github.com/kennedyraju55/standup-generator) | Meeting prep | Git-aware |
| 70 | [**Time Management Coach**](https://github.com/kennedyraju55/time-management-coach) | Productivity tips | Time analysis |

### 🔒 Category 8: Security, Privacy & DevOps

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 71 | [**Cybersecurity Alert Summarizer**](https://github.com/kennedyraju55/cybersecurity-alert-summarizer) | Threat reports | Priority ranking |
| 72 | [**Incident Report Generator**](https://github.com/kennedyraju55/incident-report-generator) | Security logs | Timeline, remediation |
| 73 | [**GDPR Compliance Checker**](https://github.com/kennedyraju55/gdpr-compliance-checker) | Privacy review | Data handling checks |
| 74 | [**Password Strength Advisor**](https://github.com/kennedyraju55/password-strength-advisor) | Security tips | Policy analysis |
| 75 | [**Log File Analyzer**](https://github.com/kennedyraju55/log-file-analyzer) | System diagnostics | Pattern detection |
| 76 | [**Docker Compose Generator**](https://github.com/kennedyraju55/docker-compose-generator) | Container configs | Stack templates |
| 77 | [**CI/CD Pipeline Generator**](https://github.com/kennedyraju55/cicd-pipeline-generator) | Workflow automation | Multi-platform |
| 78 | [**Infra Doc Generator**](https://github.com/kennedyraju55/infra-doc-generator) | Cloud documentation | Config to docs |
| 79 | [**Vulnerability Report Writer**](https://github.com/kennedyraju55/vulnerability-report-writer) | Security assessment | Executive summaries |
| 80 | [**Env Config Manager**](https://github.com/kennedyraju55/env-config-manager) | Settings helper | Validation, security |

### 🏥 Category 9: Healthcare & Wellness

| # | Project | Description | Key Features |
|:---:|---------|-------------|--------------|
| 81 | [**Symptom Checker Bot**](https://github.com/kennedyraju55/symptom-checker-bot) | Health triage | Medical disclaimers |
| 82 | [**Drug Interaction Checker**](https://github.com/kennedyraju55/drug-interaction-checker) | Medication safety | Education-only |
| 83 | [**Medical Terms Explainer**](https://github.com/kennedyraju55/medical-terms-explainer) | Health literacy | Etymology, usage |
| 84 | [**Health Plan Generator**](https://github.com/kennedyraju55/health-plan-generator) | Wellness advice | Holistic plans |
| 85 | [**EHR De-identifier**](https://github.com/kennedyraju55/ehr-deidentifier) | Privacy tool | PII removal |
| 86 | [**Nutrition Label Analyzer**](https://github.com/kennedyraju55/nutrition-label-analyzer) | Food analysis | Health insights |
| 87 | [**Exercise Form Guide**](https://github.com/kennedyraju55/exercise-form-guide) | Workout instructions | Safety tips |
| 88 | [**Sleep Improvement Advisor**](https://github.com/kennedyraju55/sleep-improvement-advisor) | Rest optimization | Pattern analysis |
| 89 | [**Stress Management Bot**](https://github.com/kennedyraju55/stress-management-bot) | Coping strategies | CBT techniques |
| 90 | [**First Aid Guide Bot**](https://github.com/kennedyraju55/first-aid-guide-bot) | Emergency help | Step-by-step |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                        User Interface                        │
│                  (CLI / Streamlit / Gradio)                   │
├──────────────────────────────────────────────────────────────┤
│                     Application Layer                        │
│     90 Production-Level Python Apps with Business Logic      │
│        Each with its own repo, tests, docs & assets          │
├──────────────────────────────────────────────────────────────┤
│                    Common LLM Client                         │
│              (common/llm_client.py - shared)                 │
├──────────────────────────────────────────────────────────────┤
│                      Ollama Server                           │
│                (http://localhost:11434)                       │
├──────────────────────────────────────────────────────────────┤
│                      Gemma 4 Model                           │
│                (9.6 GB - runs locally)                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

<div align="center">

| Technology | Purpose | |
|:---:|:---:|:---:|
| ![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=flat-square&logo=python&logoColor=white) | Core language | Production-ready |
| ![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white) | Local LLM server | Self-hosted |
| ![Gemma](https://img.shields.io/badge/Gemma_4-4285F4?style=flat-square&logo=google&logoColor=white) | Google's local LLM | 9.6 GB model |
| ![Rich](https://img.shields.io/badge/Rich-Terminal_UI-green?style=flat-square) | Beautiful terminal output | Formatted tables |
| ![Click](https://img.shields.io/badge/Click-CLI_Framework-yellow?style=flat-square) | CLI framework | Type-safe args |
| ![Pytest](https://img.shields.io/badge/Pytest-Testing-red?style=flat-square&logo=pytest&logoColor=white) | Testing framework | 2400+ tests |
| ![Pydantic](https://img.shields.io/badge/Pydantic-Validation-teal?style=flat-square) | Data validation | Type-safe models |

</div>

---

## 📁 Repository Structure

```
90-local-llm-projects/
├── common/                    # Shared utilities
│   ├── __init__.py
│   └── llm_client.py         # Ollama client library
├── 01-pdf-chat-assistant/     # Project 1 (also its own GitHub repo)
│   ├── app.py                 # Main application
│   ├── requirements.txt       # Dependencies
│   ├── test_app.py           # Tests
│   ├── assets/               # SVG images
│   └── README.md             # Documentation
├── 02-it-helpdesk-bot/        # Project 2
│   └── ...
├── ...                        # Projects 3-90
├── web-book/                  # 📖 Interactive Web Book
├── assets/images/             # Shared project images
├── requirements-base.txt      # Base dependencies
├── .gitignore
└── README.md                  # ← You are here
```

---

## 🌐 Web Book

<div align="center">

📖 **Explore all 90 projects in a beautifully formatted web book!**

<a href="https://kennedyraju55.github.io/90-local-llm-projects/">
  <img src="https://img.shields.io/badge/🌐_Web_Book-Browse_All_Projects-2ea44f?style=for-the-badge" alt="Web Book"/>
</a>

The web book includes detailed walkthroughs, architecture diagrams, and code examples for every project.

</div>

---

## 📊 Project Statistics

<div align="center">

| Metric | Count |
|:---:|:---:|
| 🚀 **Total Projects** | **90** |
| 📂 **Categories** | **9** |
| ✅ **Unit Tests** | **2,400+** |
| 🚀 **API Endpoints** | **500+** |
| 🎨 **SVG Assets** | **270** |
| 🐳 **Docker** | **Ready (all 90 projects)** |
| 🐍 **Language** | **Python** |
| 🤖 **LLM** | **Gemma 4 (100% local)** |
| 🔒 **Privacy** | **100% offline** |

</div>

---

## 🤝 Contributing

Contributions are welcome! Please:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-project`)
3. **Commit** your changes (`git commit -m 'Add amazing project'`)
4. **Push** to the branch (`git push origin feature/amazing-project`)
5. **Open** a Pull Request

Each of the 90 projects also has its own repo — contributions to individual projects are welcome too!

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

## ⭐ Star This Repo!

**If you find these 90 projects useful, please give this repo a ⭐!**
**It helps others discover the power of local LLMs.**

[![Star this repo](https://img.shields.io/badge/⭐_Star_This_Repo-GitHub-yellow?style=for-the-badge&logo=github)](https://github.com/kennedyraju55/90-local-llm-projects)

---

**Built with ❤️ using Local AI — No data was sent to the cloud in the making of these projects.**

[⬆ Back to Top](#-table-of-contents)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%"/>
