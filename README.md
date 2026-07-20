# AI Study Buddy

An educational project built from scratch to understand how Retrieval-Augmented Generation (RAG) systems work internally.

Unlike frameworks that hide the implementation details, this project builds every major component manually to understand the complete document retrieval pipeline.

---

# Project Goal

The goal of this project is to learn AI Engineering by implementing each stage of a RAG system from scratch instead of relying on frameworks like LangChain.

Current pipeline:

```
PDF
 │
 ▼
PDF Reader
 │
 ▼
Document Analyzer
 │
 ▼
Text Cleaner
 │
 ▼
Sentence Chunker
 │
 ▼
Embedding Generator
 │
 ▼
Semantic Retriever
 │
 ▼
Prompt Builder
```

The next milestone is integrating an LLM to generate natural language answers from the retrieved context.

---

# Features Implemented

## PDF Reader

- Reads PDF documents
- Extracts pages
- Supports multi-page documents

---

## Document Analyzer

Classifies each page as:

- Text Page
- Image Page
- Mixed Page
- Blank Page

Stores page metadata for later processing.

---

## Text Cleaner

Preprocesses extracted text by:

- Removing unnecessary whitespace
- Normalizing text
- Preparing clean text for chunking

---

## Sentence Chunker

Splits document text into semantic chunks.

Each chunk stores:

- Chunk text
- Page number
- Embedding vector (generated later)

---

## Rule-Based Document Classifier

Automatically identifies document types using feature extraction and weighted keyword scoring.

Current supported document types:

- Invoice
- Resume
- Research Paper
- Bank Statement
- Unknown

---

## Feature Extraction

Extracts document-level features such as:

- Word count
- Page count
- Keyword frequencies
- Structural indicators

These features are used by the classifier.

---

## Embedding Generator

Uses Sentence Transformers to generate semantic embeddings.

Current embedding model:

```
all-MiniLM-L6-v2
```

Embeddings are generated for:

- Document chunks
- User questions

---

## Semantic Retriever

Implements semantic search manually without external vector databases.

Includes:

- Custom cosine similarity
- Dot product implementation
- Vector length calculation
- Top-K retrieval

Returns the most relevant chunks based on semantic similarity.

---

## Retrieval Result Model

Each retrieval result stores:

- Retrieved chunk
- Similarity score

This abstraction keeps the retrieval layer extensible for future metadata.

---

## Prompt Builder

Creates structured prompts for LLMs.

The prompt includes:

- System instructions
- Retrieved context
- User question

This separates prompt generation from retrieval logic.

---

# Project Structure

```
src/
│
├── analyzers/
├── chunkers/
├── classifiers/
├── cleaners/
├── config/
├── embeddings/
├── models/
├── prompt/
├── prompts/
├── readers/
├── retrievers/
```

---

# Technologies Used

- Python
- PyMuPDF (fitz)
- Sentence Transformers
- NumPy

---

# Current Workflow

```
PDF
 │
 ▼
Read Pages
 │
 ▼
Analyze Pages
 │
 ▼
Clean Text
 │
 ▼
Chunk Document
 │
 ▼
Generate Embeddings
 │
 ▼
Semantic Retrieval
 │
 ▼
Prompt Generation
```

---

# Future Roadmap

## Phase 1 (Completed)

- [x] PDF Reader
- [x] Document Analyzer
- [x] Text Cleaner
- [x] Sentence Chunker
- [x] Feature Extraction
- [x] Rule-Based Document Classification
- [x] Embedding Generator
- [x] Semantic Retrieval
- [x] Prompt Builder

---

## Phase 2

- [ ] LLM Integration
- [ ] Response Generation
- [ ] Prompt Templates
- [ ] Source Attribution

---

## Phase 3

- [ ] FAISS Integration
- [ ] ChromaDB Support
- [ ] Hybrid Search
- [ ] Metadata Filtering
- [ ] Multi-document Retrieval

---

## Phase 4

- [ ] Chat Memory
- [ ] Multiple PDF Knowledge Base
- [ ] Web Interface
- [ ] Streaming Responses

---

# Learning Objectives

This project focuses on understanding:

- Document Processing
- Feature Engineering
- Text Preprocessing
- Semantic Embeddings
- Vector Similarity Search
- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- AI System Design
- Software Architecture for AI Applications

---

# Why Build This Instead of Using LangChain?

The purpose of this project is educational.

Rather than treating RAG as a black box, every component is implemented manually to understand:

- How PDFs are processed
- How embeddings work
- How cosine similarity retrieves relevant information
- How prompts are constructed
- How each component interacts within a RAG pipeline

Once these fundamentals are understood, frameworks such as LangChain or LlamaIndex become tools for productivity rather than dependencies.

---

# Author

Built as a learning project to understand AI Engineering from first principles.