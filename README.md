# AI Agent Framework

> A modular, extensible, provider-independent AI Agent Framework built from scratch in Python using Clean Architecture principles.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Architecture](https://img.shields.io/badge/Architecture-Clean-green)
![LLM](https://img.shields.io/badge/LLM-Gemini%20%7C%20Ollama-orange)
![Status](https://img.shields.io/badge/Version-v0.1.0-success)

---

# Overview

This project is **not an AI application**.

It is an attempt to build a reusable **AI Agent Framework** capable of supporting multiple workflows, multiple LLM providers, document processing, Retrieval-Augmented Generation (RAG), deterministic tool execution, and future Agentic AI capabilities.

The framework has been designed from the ground up using **Object-Oriented Design**, **Factory Pattern**, **Strategy Pattern**, and **Separation of Concerns**, making every major component replaceable without affecting the rest of the system.

Unlike many AI projects that tightly couple business logic with LLM calls, this framework delegates orchestration to the framework itself while keeping LLMs as interchangeable reasoning engines.

---

# Current Features

## Agent Framework

- Modular Intelligent Agent
- Shared Agent State
- Context Builder
- Rule-Based Decision Engine
- Workflow Registry
- Chat Workflow
- RAG Workflow
- Tool Workflow

---

## Document Intelligence

- PDF Reader
- Document Analyzer
- Document Processing Pipeline
- Document Manager
- Sentence Chunking
- Document Indexing
- Embedding Generation
- In-Memory Document Store

---

## Retrieval

- Semantic Retrieval
- Maximum Marginal Relevance (MMR)
- Configurable Retriever Factory
- Re-ranking Pipeline

---

## Prompt System

- Prompt Context
- Prompt Factory
- Chat Prompt Builder
- RAG Prompt Builder
- Tool Prompt Builder
- Workflow-specific Prompt Templates

---

## LLM Layer

- Generic LLM Interface
- Gemini Integration
- Ollama Integration
- Common LLM Response Model
- Token Usage Tracking

---

## Tool Framework

- Tool Registry
- Tool Executor
- Calculator Tool
- Deterministic Tool Routing

---

## Memory

- Conversation Memory
- Memory Manager
- Recent Conversation Context

---

## Infrastructure

- Centralized Configuration
- Factory-Based Dependency Injection
- Logging
- Exception Handling
- Provider Independence

---

# High Level Architecture

```text
                               User
                                │
                                ▼
                       IntelligentAgent
                                │
      ┌─────────────────────────┼──────────────────────────┐
      │                         │                          │
      ▼                         ▼                          ▼
Document Manager         Context Builder             Agent State
      │                         │                          │
      ▼                         ▼                          │
Document Pipeline       Decision Engine                   │
      │                         │                          │
      ▼                         ▼                          │
Document Store         Workflow Registry ◄─────────────────┘
                                │
         ┌──────────────────────┼────────────────────────┐
         ▼                      ▼                        ▼
    Chat Workflow          RAG Workflow            Tool Workflow
         │                      │                        │
         ▼                      ▼                        ▼
   Chat Pipeline          RAG Pipeline           Tool Pipeline
         │                      │                        │
         ▼                      ▼                        ▼
      Prompt              Prompt Builder          Tool Executor
         │                      │                        │
         ▼                      ▼                        ▼
                    Gemini / Ollama / Future Providers
```

---

# Design Philosophy

The framework follows a few fundamental principles.

## 1. Separation of Concerns

Every component has exactly one responsibility.

Examples:

- Retriever retrieves.
- Prompt Builder builds prompts.
- LLM generates responses.
- Decision Engine selects workflows.
- IntelligentAgent orchestrates everything.

---

## 2. Replaceability

Every major component can be replaced independently.

Examples:

- Gemini → OpenAI
- MMR Retriever → Hybrid Retriever
- InMemory Store → ChromaDB
- Rule-Based Decision Engine → LLM Decision Engine

No other component should require modification.

---

## 3. Extensibility

The framework is designed to support future additions such as:

- New workflows
- New retrievers
- New rerankers
- New memory systems
- New tools
- New document stores
- New LLM providers

without modifying existing implementations.

---

## 4. Provider Independence

The framework never directly depends on Gemini or Ollama.

Instead it communicates through abstract interfaces.

This allows future integration with:

- OpenAI
- Anthropic
- Groq
- HuggingFace
- Local GGUF models
- Any OpenAI-compatible API

with minimal changes.

---

# Project Structure

```text
AI-Agent-Framework/

├── src/
│
├── agent/
│   ├── intelligent_agent.py
│   ├── base_agent.py
│   └── state.py
│
├── analyzers/
│
├── chunkers/
│
├── classifiers/
│
├── cleaners/
│
├── config/
│
├── context/
│   ├── context.py
│   └── context_builder.py
│
├── document/
│   └── document_manager.py
│
├── embeddings/
│
├── factories/
│   ├── agent_factory.py
│   ├── llm_factory.py
│   ├── memory_factory.py
│   ├── processing_factory.py
│   ├── retriever_factory.py
│   ├── store_factory.py
│   ├── tool_factory.py
│   └── workflow_factory.py
│
├── indexing/
│
├── llm/
│
├── logging/
│
├── memory/
│
├── memory_managers/
│
├── models/
│
├── orchestration/
│
├── pipeline/
│
├── prompt/
│
├── prompts/
│
├── readers/
│
├── rerankers/
│
├── retrievers/
│
├── store/
│
├── tools/
│
├── workflows/
│
└── main.py
```

---

# Intelligent Agent

The **IntelligentAgent** is the entry point of the framework.

It acts as the orchestrator responsible for coordinating every component while avoiding business logic itself.

Its responsibilities include:

- Accept user queries
- Manage uploaded documents
- Build execution context
- Invoke the Decision Engine
- Select the correct workflow
- Execute the workflow
- Return the final response

The agent itself never knows how retrieval, prompting, or LLM inference works.

---

# Agent Lifecycle

Every request follows the same execution pipeline.

```text
User Question
      │
      ▼
Context Builder
      │
      ▼
Decision Engine
      │
      ▼
Workflow Registry
      │
      ▼
Selected Workflow
      │
      ▼
Pipeline
      │
      ▼
LLM / Tool
      │
      ▼
Response
```

Because every request passes through this pipeline, adding new workflows requires no changes inside the agent.

---

# Agent State

The framework maintains a shared **AgentState** object that is accessible throughout the application.

Current state stores:

- Active uploaded documents
- Conversation history
- Available tools
- Runtime metadata

The AgentState enables components to communicate without being tightly coupled.

For example:

- Context Builder reads the current state.
- Document Manager updates active documents.
- Decision Engine checks whether documents are available.
- Future planners and agents will share the same state.

---

# Context Builder

The Context Builder transforms the AgentState into a lightweight execution context.

Example:

```text
Context

├── has_active_document
├── has_history
├── tools_available
└── question
```

The Context object intentionally contains only the information required by the Decision Engine.

This avoids exposing the complete AgentState to every component.

---

# Decision Engine

The Decision Engine determines which workflow should execute.

Current supported workflows:

- Chat
- Retrieval-Augmented Generation
- Tool Execution

Example:

```
User:
2 * 3 / 4

↓

Workflow = TOOL
Tool = Calculator
```

If a document is available and the question is document-related, the RAG workflow is selected.

Otherwise:

- Mathematical expressions → Tool Workflow
- General conversation → Chat Workflow

The routing logic is deterministic and controlled entirely by the framework.

---

# Workflow Registry

The Workflow Registry maps workflow identifiers to their implementations.

```text
CHAT
    │
    ▼
ChatWorkflow

RAG
    │
    ▼
RAGWorkflow

TOOL
    │
    ▼
ToolWorkflow
```

Adding a new workflow only requires:

- Creating the workflow
- Registering it

The IntelligentAgent never changes.

---

# Factory Architecture

The framework makes heavy use of the Factory Pattern to isolate object creation.

Current factories include:

## AgentFactory

Responsible for assembling the complete framework.

It creates:

- LLM
- Retriever
- Memory
- Pipelines
- Workflows
- State
- IntelligentAgent

---

## LLMFactory

Creates the configured LLM provider.

Current providers:

- Gemini
- Ollama

Future providers:

- OpenAI
- Anthropic
- Groq
- HuggingFace

---

## ProcessingFactory

Responsible for document processing components.

Creates:

- Cleaner
- Chunker
- Embedding Generator
- Document Indexer
- Reranker

---

## RetrieverFactory

Creates the configured retriever.

Current implementations:

- Semantic Retriever
- Maximum Marginal Relevance Retriever

Future implementations:

- Hybrid Retriever
- Metadata Retriever
- Parent-Child Retriever

---

## StoreFactory

Creates the configured document store.

Current:

- InMemoryDocumentStore

Future:

- ChromaDB
- Pinecone
- Weaviate
- Qdrant

---

## MemoryFactory

Creates:

- Conversation Memory
- Memory Manager

Future memory systems can be introduced without modifying pipelines.

---

## ToolFactory

Creates:

- Tool Registry
- Tool Executor

Current Tool:

- Calculator

Future tools:

- Weather
- Search
- SQL
- File System
- Web APIs

---

## WorkflowFactory

Registers every workflow inside the Workflow Registry.

Current workflows:

- Chat
- RAG
- Tool

Future workflows may include:

- Planner Workflow
- Reflection Workflow
- Multi-Agent Workflow
- MCP Workflow

The IntelligentAgent never needs to know how workflows are created.

# Document Processing

The framework separates document lifecycle management from document processing.

The **DocumentManager** is responsible for managing uploaded documents, while the **DocumentProcessingPipeline** is responsible for transforming raw documents into searchable knowledge.

## Document Lifecycle

```
Upload PDF
      │
      ▼
Document Manager
      │
      ▼
Document Processing Pipeline
      │
      ▼
Indexed Document
      │
      ▼
Document Store
      │
      ▼
Agent State Updated
```

Current responsibilities of the Document Manager:

- Upload documents
- Process documents
- Remove documents
- List active documents
- Clear uploaded documents
- Maintain active document state

This separation ensures that document management logic remains independent of document indexing.

---

# Document Processing Pipeline

Every uploaded document passes through the following stages.

```
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
Document Indexer
      │
      ▼
Document Store
```

Each stage has a single responsibility.

### Reader

Reads the uploaded document.

Current implementation:

- PDF Reader

Future:

- DOCX Reader
- TXT Reader
- HTML Reader
- Markdown Reader

---

### Analyzer

Extracts useful information from raw pages.

Examples:

- Page text
- Metadata
- Language
- Summary

---

### Cleaner

Normalizes document text before chunking.

Examples:

- Remove unnecessary whitespace
- Normalize line breaks
- Remove invalid characters

---

### Chunker

Splits large documents into semantically meaningful chunks.

Current implementation:

- Sentence Chunking

Future implementations:

- Recursive Chunking
- Semantic Chunking
- Token Chunking
- Sliding Window Chunking

---

### Embedding Generator

Converts every chunk into vector embeddings.

The framework treats embedding generation as an independent component, allowing future replacement without affecting retrieval.

---

### Document Indexer

Coordinates the complete indexing process.

Responsibilities:

- Clean document
- Chunk document
- Generate embeddings
- Produce indexed document

---

# Document Store

The framework stores indexed documents inside a document store.

Current implementation:

```
InMemoryDocumentStore
```

Responsibilities:

- Store indexed documents
- Provide searchable document collection
- Support retrieval

Future implementations:

- ChromaDB
- Pinecone
- Weaviate
- Qdrant

---

# Retrieval Pipeline

Current retrieval flow:

```
User Question
       │
       ▼
Embedding Generation
       │
       ▼
Retriever
       │
       ▼
Relevant Chunks
       │
       ▼
Reranker
       │
       ▼
Top Chunks
```

The retriever is completely independent from the document store implementation.

Current retrievers:

- Semantic Retriever
- Maximum Marginal Relevance (MMR)

Future retrievers:

- Hybrid Retrieval
- Metadata Retrieval
- Parent-Child Retrieval

---

# Prompt System

The prompt system is fully modular.

Instead of a single PromptBuilder, every workflow owns its own prompt builder.

```
PromptFactory
        │
        ├──────────────┐
        │              │
        ▼              ▼
ChatPrompt      RAGPrompt
        │              │
        ▼              ▼
Prompt Builder  Prompt Builder
```

This allows every workflow to construct prompts independently.

Current prompt builders:

- Chat Prompt Builder
- RAG Prompt Builder
- Tool Prompt Builder

---

# Prompt Context

Every prompt builder receives a common PromptContext object.

Example:

```
PromptContext

├── question
├── history
├── retrieval_results
├── metadata
└── extras
```

This avoids long method signatures and provides a common interface for all prompt builders.

---

# LLM Layer

The framework is provider-independent.

Every provider returns the same LLMResponse object.

Current providers:

- Google Gemini
- Ollama

Future providers:

- OpenAI
- Anthropic
- Groq
- Hugging Face
- Local GGUF Models

---

# LLM Response

Every provider maps its native response into a common model.

```
LLMResponse

├── content
├── tool_call
├── model_name
├── usage
├── response_time
├── finish_reason
└── created_at
```

Because workflows depend only on LLMResponse, switching providers requires no workflow changes.

---

# Memory

Conversation memory is maintained independently from retrieval.

Current implementation:

- Conversation Memory
- Recent Memory Manager

Responsibilities:

- Store user messages
- Store assistant responses
- Build conversational context

Future memory systems:

- Summary Memory
- Long-Term Memory
- Vector Memory
- Episodic Memory

---

# Tool Framework

Unlike many LLM-based agents, tools are selected by the framework rather than by the language model.

Current flow:

```
User Question
      │
      ▼
Decision Engine
      │
      ▼
Tool Workflow
      │
      ▼
Tool Pipeline
      │
      ▼
Tool Executor
      │
      ▼
Calculator Tool
```

This avoids unnecessary LLM calls for deterministic operations.

Current tools:

- Calculator

Planned tools:

- Weather
- SQL
- Search
- File System
- REST APIs

---

# Logging

The framework includes centralized logging.

Logging levels include:

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

Logs are used throughout the framework instead of print statements.

This simplifies debugging while making the framework suitable for production environments.

---

# Exception Handling

Errors are handled gracefully without terminating the application.

Responsibilities:

- Capture exceptions
- Log failures
- Return user-friendly responses
- Continue execution whenever possible

This allows long-running interactive sessions without crashing due to unexpected failures.

---

# Configuration

The framework uses centralized configuration to avoid hard-coded values.

Current configurable components include:

- LLM Provider
- Retriever
- Chunker
- Cleaner
- Document Processing
- Embedding Generation

Future configuration will include:

- Vector Database
- Memory System
- Reranker
- Prompt Templates
- Logging
- Observability

# Current Features

## Core Framework

- Modular Intelligent Agent
- Shared Agent State
- Context-Based Decision Making
- Workflow Registry
- Rule-Based Decision Engine
- Factory-Based Dependency Injection
- Configuration System
- Centralized Logging
- Exception Handling

---

## Document Intelligence

- PDF Reading
- Document Analysis
- Document Processing Pipeline
- Document Manager
- Sentence Chunking
- Embedding Generation
- Document Indexing
- In-Memory Document Store

---

## Retrieval

- Semantic Retrieval
- Maximum Marginal Relevance (MMR)
- Re-ranking
- Retrieval-Augmented Generation (RAG)

---

## Prompt Framework

- Prompt Factory
- Prompt Context
- Chat Prompt Builder
- RAG Prompt Builder
- Tool Prompt Builder
- Workflow-specific Prompt Templates

---

## LLM Layer

- Generic LLM Interface
- Gemini Integration
- Ollama Integration
- Common Response Model

---

## Memory

- Conversation Memory
- Recent Memory Manager

---

## Tools

- Calculator Tool
- Tool Registry
- Tool Executor

---

# Example Usage

## Create Agent

```python
from src.factories.agent_factory import AgentFactory

agent = AgentFactory.create()
```

---

## Upload Document

```python
agent.process_document("artificial_intelligence.pdf")
```

---

## Ask Questions

```python
response = agent.run(
    "What is Artificial Intelligence?"
)

print(response.content)
```

---

## Tool Execution

```python
response = agent.run("25 * 15 + 8")
```

The Decision Engine automatically routes the request to the Tool Workflow.

---

## Chat

```python
response = agent.run(
    "Explain reinforcement learning."
)
```

The framework automatically selects the Chat Workflow.

---

# Extending the Framework

One of the primary goals of this project is extensibility.

Adding new capabilities should require minimal changes to existing code.

---

## Add a New LLM

Create a new implementation of the BaseLLM interface.

```text
llm/

openai_llm.py
```

Register it inside:

```
LLMFactory
```

No other component requires modification.

---

## Add a New Retriever

Implement a new retriever.

Example:

```
HybridRetriever
```

Register it inside:

```
RetrieverFactory
```

---

## Add a New Tool

Create a new Tool.

Example:

```
WeatherTool
```

Register it inside:

```
ToolFactory
```

The Decision Engine can then route requests automatically.

---

## Add a New Workflow

Implement:

```
PlannerWorkflow
```

Register it inside:

```
WorkflowFactory
```

The IntelligentAgent remains unchanged.

---

# Roadmap

## Version 0.2

### Persistent Retrieval

- ChromaDB Integration
- Metadata-aware Retrieval
- Hybrid Retrieval
- Multi-document Retrieval
- Persistent Embeddings

---

## Version 0.3

### Agentic AI

- Planner Workflow
- Reflection Workflow
- Multi-step Reasoning
- Task Decomposition
- Native Gemini Function Calling

---

## Version 0.4

### Advanced Memory

- Summary Memory
- Long-Term Memory
- Episodic Memory
- Vector Memory

---

## Version 0.5

### Enterprise Features

- Observability
- Tracing
- Metrics
- Streaming Responses
- Authentication

---

## Version 1.0

### AI Agent Platform

- Multi-Agent Collaboration
- Model Context Protocol (MCP)
- Plugin System
- REST API
- Docker Deployment
- Kubernetes Deployment
- Cloud Vector Databases
- Production Monitoring

---

# Technologies

- Python 3.12
- Google Gemini API
- Ollama
- NumPy
- Object-Oriented Programming
- Clean Architecture
- Retrieval-Augmented Generation (RAG)
- Maximum Marginal Relevance (MMR)

Future:

- ChromaDB
- FastAPI
- BM25
- Docker
- Redis
- PostgreSQL

---

# Design Principles

The framework is built around the following principles.

### Modularity

Every component should have a single responsibility.

---

### Extensibility

Adding new functionality should not require modifying existing modules.

---

### Replaceability

Components such as LLMs, Retrievers, Memory Systems, Stores, and Workflows should be interchangeable.

---

### Provider Independence

The framework should not depend on any specific AI provider.

---

### Clean Architecture

Business logic remains independent of frameworks and third-party libraries.

---

### Deterministic Orchestration

Workflow selection and tool routing are handled by the framework rather than delegated to the language model.

---

# Future Vision

The long-term goal of this project is to evolve from a modular RAG framework into a production-ready AI Agent Platform.

Future capabilities include:

- Autonomous Agents
- Multi-Agent Collaboration
- Model Context Protocol (MCP)
- Enterprise Retrieval
- Local & Cloud LLM Support
- Persistent Memory
- Hybrid Search
- Plugin Ecosystem
- Observability & Tracing
- Cloud Deployment
- API Gateway
- Production Monitoring

The architecture has been intentionally designed so these capabilities can be introduced incrementally without requiring large-scale refactoring.

---

# Contributing

Contributions, suggestions, and discussions are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a feature branch
3. Implement your changes
4. Add tests where applicable
5. Submit a Pull Request

Constructive feedback and architectural discussions are encouraged.

---

# License

This project is currently developed for educational, research, and learning purposes.

Feel free to explore the code, learn from it, and build upon the ideas presented here.

---

# Author

**VJ S**

Building an AI Agent Framework from scratch to understand the internals of modern AI systems instead of relying solely on existing frameworks.

⭐ If you find this project interesting, consider giving it a star and following its progress as new capabilities are added.