# Project Recall

> **An AI-powered research workspace that helps students and researchers instantly regain project context after returning to an ongoing project.**

🚀 **Project Recall** is being built as part of the **ML Empowerment Build Challenge 2.0**, with the vision of growing beyond a hackathon MVP into a production-ready AI research assistant.

Instead of spending hours trying to remember previous progress, Project Recall reconstructs project context from research papers, notes, and supporting documents—allowing users to continue their work exactly where they left off.

---

# 📖 Table of Contents

* [Problem Statement](#-problem-statement)
* [Our Solution](#-our-solution)
* [Hackathon MVP](#-hackathon-mvp)
* [Technology Stack](#-technology-stack)
* [Current Project Status](#-current-project-status)
* [Repository Structure](#-repository-structure)
* [Getting Started](#-getting-started)
* [Roadmap](#-roadmap)
* [Vision Beyond the Hackathon](#-vision-beyond-the-hackathon)
* [Author](#-author)

---

# 🎯 Problem Statement

Research projects often span weeks or even months. After returning to a project following a break, researchers and students frequently spend valuable time trying to answer questions such as:

* What was I working on?
* Which papers have I already reviewed?
* What conclusions have I already reached?
* What remains unfinished?
* What should I do next?

Although existing AI tools can answer questions about individual documents, they generally lack an understanding of the overall progress and context of an entire research project.

This repeated process of reconstructing context interrupts productivity and slows research.

---

# 💡 Our Solution

Project Recall aims to function as an intelligent **project memory**.

Instead of simply answering questions from uploaded files, it analyzes research documents to understand the overall state of a project and helps users quickly resume meaningful work.

The long-term vision includes:

* 📄 Intelligent document ingestion
* 🧠 AI-powered context reconstruction
* 🔍 Semantic document search
* 📚 Research memory across multiple documents
* ✨ Automatic project summaries
* ✅ Context-aware next-step recommendations

---

# 🏆 Hackathon MVP

The initial MVP focuses on validating the core concept through the following workflow:

* Upload research PDFs
* Extract document text
* Process uploaded content
* Search documents semantically
* Generate an AI-powered project summary
* Recommend the next logical action

---

# 🛠️ Technology Stack

## Backend

* Python 3.11
* FastAPI
* Uvicorn

## Development

* Git
* GitHub
* Python Virtual Environment (`venv`)

## AI (Planned)

* Google Gemma 3n
* Vector Embeddings
* Semantic Search

---

# 📈 Current Project Status

## Current Development Phase

**Phase:** Backend Foundation

### ✅ Completed

#### Project Foundation

* Hackathon registration completed *(ML Empowerment Build Challenge 2.0)*
* GitHub repository initialized and configured
* Professional project documentation established
* Development log introduced for progress tracking

#### Development Environment

* Python virtual environment configured
* Dependency management using `requirements.txt`
* Git version control workflow established
* Project structure organized for scalable development

#### Backend Development

* FastAPI backend initialized
* Automatic interactive API documentation enabled via Swagger UI (`/docs`)
* Core API routing implemented
* Static API endpoints created
* Dynamic path parameter handling implemented
* Query parameter handling implemented
* First POST endpoint developed
* Request validation implemented using Pydantic models

### 🎯 Current Focus

Building the document ingestion pipeline for research papers and project documents.

### 🚀 Next Milestone

Implement PDF upload functionality and establish the document processing workflow.
---

# 📂 Repository Structure

```text
project-recall/
│
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── requirements.txt        # Project dependencies
│   └── venv/                   # Local virtual environment (Git ignored)
│
├── docs/
│   └── development-log.md      # Development journal
│
├── .gitignore                  # Git ignore rules
│
└── README.md                   # Project documentation
```

> **Note:** This structure represents the current backend foundation. As Project Recall evolves, additional modules for document processing, AI services, vector databases, configuration management, and the frontend will be introduced while maintaining a scalable project architecture.


```

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Tanu-shree-Tandon/project-recall.git
```

Move into the backend directory:

```bash
cd project-recall/backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the development server:

```bash
uvicorn main:app --reload
```

Visit:

Backend API

```text
http://127.0.0.1:8000
```

Interactive API Documentation

```text
http://127.0.0.1:8000/docs
```

---

# 🗺️ Roadmap

## Phase 1 — Backend Foundation ✅

* Repository setup
* FastAPI configuration
* Initial API

## Phase 2 — Document Processing

* PDF upload
* PDF storage
* Text extraction

## Phase 3 — AI Integration

* Document embeddings
* Semantic search
* Context retrieval

## Phase 4 — Context Reconstruction

* AI-generated project summaries
* Research timeline reconstruction
* Next-step recommendations

## Phase 5 — User Experience

* Dashboard
* Upload interface
* Search interface
* Project workspace

---

# 🌟 Vision Beyond the Hackathon

The **ML Empowerment Build Challenge** serves as the starting point for Project Recall.

The long-term goal is to build a scalable AI research workspace that enables students, researchers, and professionals to resume complex projects without manually reconstructing previous work from scattered notes and documents.

Rather than being a one-time hackathon submission, Project Recall is intended to evolve into a long-term portfolio project and a production-ready AI application.

---

# 👩‍💻 Author

**Tanu Shree Tandon**

Second-Year BCA (Data Science) Student

Building Project Recall as a flagship AI/ML portfolio project while participating in the **ML Empowerment Build Challenge**.
