# 🧠 AI Study Buddy

A modular **Retrieval-Augmented Generation (RAG) Framework** built completely from scratch in Python to understand the internal architecture of modern Generative AI systems.

Instead of relying on frameworks like LangChain, this project implements every major RAG component independently, making it easy to understand, customize, and extend.

---

## ✨ Features

- 📄 PDF Document Processing
- 🧹 Text Cleaning Pipeline
- ✂️ Intelligent Text Chunking
- 🔢 SentenceTransformer Embeddings
- 📚 In-Memory Document Store
- 🔍 Semantic Search
- 🎯 Maximum Marginal Relevance (MMR) Retrieval
- 🚀 CrossEncoder Re-ranking
- 💬 Conversation Memory
- 🧠 Memory Manager Abstraction
- 📑 Multi-Document Retrieval
- 🤖 Ollama LLM Integration
- 🏗️ Modular & Extensible Architecture
- 🔌 Dependency Injection
- 🧩 Plug-and-Play Components

---

# System Architecture

```
                   PDF Documents
                         │
                         ▼
                 ┌──────────────┐
                 │    Reader    │
                 └──────────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │   Analyzer   │
                 └──────────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │   Cleaner    │
                 └──────────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │   Chunker    │
                 └──────────────┘
                         │
                         ▼
             ┌─────────────────────┐
             │ Embedding Generator │
             └─────────────────────┘
                         │
                         ▼
               ┌────────────────┐
               │ Document Store │
               └────────────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
      Semantic Retriever      MMR Retriever
             │                       │
             └───────────┬───────────┘
                         ▼
               ┌────────────────┐
               │ CrossEncoder   │
               │   Reranker     │
               └────────────────┘
                         │
                         ▼
               ┌────────────────┐
               │ Memory Manager │
               └────────────────┘
                         │
                         ▼
               ┌────────────────┐
               │ Prompt Builder │
               └────────────────┘
                         │
                         ▼
                 ┌──────────────┐
                 │  Ollama LLM  │
                 └──────────────┘
                         │
                         ▼
                    Final Answer
```

---

# Project Structure

```
AI-Study-Buddy/
│
├── documents/
│
├── src/
│   │
│   ├── analyzers/
│   ├── chunkers/
│   ├── cleaners/
│   ├── config/
│   ├── document/
│   ├── embeddings/
│   ├── indexing/
│   ├── llm/
│   ├── memory/
│   ├── memory_managers/
│   ├── prompt/
│   ├── readers/
│   ├── rerankers/
│   ├── retrievers/
│   ├── store/
│   └── pipeline/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Current Components

| Component | Status |
|-----------|--------|
| PDF Reader | ✅ |
| Document Analyzer | ✅ |
| Text Cleaner | ✅ |
| Text Chunker | ✅ |
| Embedding Generator | ✅ |
| In-Memory Store | ✅ |
| Semantic Retriever | ✅ |
| MMR Retriever | ✅ |
| CrossEncoder Reranker | ✅ |
| Conversation Memory | ✅ |
| Memory Manager | ✅ |
| Prompt Builder | ✅ |
| Ollama LLM | ✅ |

---

# Retrieval Pipeline

```
Question
    │
    ▼
Conversation Memory
    │
    ▼
Retriever
    │
    ▼
Top 20 Chunks
    │
    ▼
CrossEncoder Reranker
    │
    ▼
Top 3 Chunks
    │
    ▼
Prompt Builder
    │
    ▼
LLM
    │
    ▼
Answer
```

---

# Technologies Used

- Python
- Ollama
- Gemma 3
- Sentence Transformers
- HuggingFace
- CrossEncoder
- NumPy
- PyPDF
- Scikit-Learn

---

# Design Principles

This project follows modern software engineering principles:

- SOLID Principles
- Object-Oriented Programming
- Dependency Injection
- Abstraction
- Modular Design
- Separation of Concerns
- Interface-Based Architecture

---

# Why Build Everything From Scratch?

The goal of this project is not only to build a chatbot but to understand how modern RAG systems work internally.

Instead of depending on high-level frameworks, every major component is implemented independently to gain a deeper understanding of:

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Maximum Marginal Relevance (MMR)
- CrossEncoder Re-ranking
- Conversation Memory
- Prompt Engineering
- LLM Integration
- Clean Software Architecture

This makes the framework highly extensible and suitable for experimentation with different retrieval algorithms, memory strategies, rerankers, and language models.

---

# Current Retrieval Strategies

### Semantic Retrieval

Ranks document chunks using cosine similarity between query embeddings and document embeddings.

---

### Maximum Marginal Relevance (MMR)

Balances:

- Relevance
- Diversity

to reduce redundant retrieval results.

---

### CrossEncoder Re-ranking

After retrieval, a CrossEncoder model scores the retrieved chunks together with the query to improve ranking accuracy before sending the final context to the LLM.

---

# Memory

The framework currently supports:

### Conversation Memory

Stores user and assistant messages.

### Recent Memory Manager

Retrieves the latest conversation history and injects it into the prompt.

Future memory implementations can be added without modifying the pipeline.

Examples:

- Summary Memory
- Semantic Memory
- Long-Term Memory

---

# Multi-Document Support

The document store supports multiple indexed documents.

Each chunk maintains metadata including:

- Document Name
- Page Number
- Chunk ID

allowing retrieval across multiple PDFs while preserving source information.

---

# Extensibility

Adding a new retriever only requires implementing:

```python
class BaseRetriever:
    retrieve(...)
```

Adding a new LLM only requires implementing:

```python
class BaseLLM:
    generate(...)
```

Adding a new memory strategy only requires implementing:

```python
class BaseMemoryManager:
    get_context(...)
```

The pipeline remains unchanged.

---

# Roadmap

## ✅ Completed

- PDF Processing
- Chunking
- Embeddings
- Semantic Retrieval
- MMR Retrieval
- CrossEncoder Re-ranking
- Conversation Memory
- Memory Manager
- Multi-Document Support

---

## 🚧 Coming Soon

- Function Calling
- Tool Registry
- Structured Output
- AI Agents
- Reflection
- ReAct
- MCP (Model Context Protocol)
- LangGraph-style Workflows
- FastAPI API
- Docker Support
- Evaluation Framework
- FAISS Vector Store
- Hybrid Search

---

# Installation

```bash
git clone https://github.com/<your-username>/AI-Study-Buddy.git

cd AI-Study-Buddy

pip install -r requirements.txt
```

---

# Run

Start Ollama:

```bash
ollama serve
```

Download the model:

```bash
ollama pull gemma3:1b
```

Run the application:

```bash
python main.py
```

---

# Future Vision

The long-term goal is to evolve this project into a complete **Generative AI Framework** supporting:

- RAG
- Agents
- Tool Calling
- MCP
- Multi-Agent Systems
- Production Deployment

while keeping every component modular and easy to understand.

---

# Author

**VRAJ SHAH**

Computer Science Student | Generative AI Enthusiast

Building modern AI systems from first principles.

---

⭐ If you found this project useful, consider giving it a star!