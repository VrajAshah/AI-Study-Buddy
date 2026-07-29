# AI Agent Framework

> A modular, extensible AI Agent Framework built from scratch using Python, designed with clean architecture principles. The framework supports conversational AI, Retrieval-Augmented Generation (RAG), tool execution, document processing, and provider-independent LLM integration.

> **Current Version:** v0.1.0-alpha

---

# Overview

This project is an attempt to build an AI Agent Framework instead of a single AI application.

The goal is to separate responsibilities into independent modules so that new workflows, tools, memory systems, retrievers, and LLM providers can be added without modifying the core framework.

Current capabilities include:

- Multi-workflow agent orchestration
- Conversation workflow
- Retrieval-Augmented Generation (RAG)
- Tool execution
- Document indexing
- Semantic retrieval using MMR
- Conversation memory
- Gemini LLM integration
- Provider-independent LLM abstraction

---

# Architecture

```text
                                IntelligentAgent
                                       │
                        ┌──────────────┴──────────────┐
                        │                             │
                process_document()                 run()
                        │                             │
                        ▼                             ▼
        DocumentProcessingPipeline            ContextBuilder
                        │                             │
                        ▼                             ▼
                  Document Store               Decision Engine
                                                      │
                                                      ▼
                                              Workflow Registry
                                                      │
                 ┌────────────────────────────────────┼────────────────────────────────────┐
                 ▼                                    ▼                                    ▼
           Chat Workflow                        RAG Workflow                         Tool Workflow
                 │                                    │                                    │
                 ▼                                    ▼                                    ▼
          Chat Pipeline                       RAG Pipeline                        Tool Pipeline
                 │                                    │                                    │
                 ▼                                    ▼                                    ▼
             Gemini LLM                 Retriever → Prompt Builder                Tool Executor
                 │                                    │                                    │
                 ▼                                    ▼                                    ▼
          LLM Response                         Gemini LLM                         Calculator Tool
```

---

# Project Structure

```text
src/

├── agent/
│   ├── intelligent_agent.py
│   ├── context.py
│   ├── context_builder.py
│   └── state.py
│
├── decision/
│   ├── decision.py
│   ├── workflow.py
│   └── rule_based_decision_engine.py
│
├── workflows/
│   ├── chat_workflow.py
│   ├── rag_workflow.py
│   ├── tool_workflow.py
│   └── workflow_registry.py
│
├── pipelines/
│   ├── chat_pipeline.py
│   ├── rag_pipeline.py
│   ├── tool_pipeline.py
│   └── document_processing_pipeline.py
│
├── prompts/
│
├── retrievers/
│   └── mmr_retriever.py
│
├── store/
│   └── in_memory_store.py
│
├── memory/
│
├── tools/
│   ├── calculator_tool.py
│   ├── tool_executor.py
│   └── tool_registry.py
│
├── llm/
│   ├── gemini_client.py
│   ├── llm_response.py
│   └── token_usage.py
│
├── embeddings/
│
├── models/
│
└── factory/
    └── agent_factory.py
```

---

# Core Components

## Intelligent Agent

The `IntelligentAgent` is the entry point of the framework.

Responsibilities:

- Accept user queries
- Process uploaded documents
- Build execution context
- Invoke the Decision Engine
- Execute the appropriate workflow
- Return the final response

---

## Agent State

The framework maintains a shared state object across all components.

Current state contains:

- Active uploaded documents
- Conversation history
- Available tools
- Metadata

This shared state allows different workflows to collaborate without tight coupling.

---

## Context Builder

The Context Builder converts the current Agent State into a lightweight execution context.

Example:

```text
Context

├── has_active_document
├── has_history
├── available_tools
└── current_question
```

This context is used by the Decision Engine to determine which workflow should execute.

---

## Decision Engine

The Decision Engine is responsible for routing user requests.

Current supported workflows:

- Chat
- Retrieval-Augmented Generation (RAG)
- Tool Execution

Example:

```text
User:
2 * 3 / 4

↓

Decision

workflow = TOOL
tool = calculator
```

---

## Workflow Registry

The Workflow Registry maps workflow types to workflow implementations.

```text
CHAT  → ChatWorkflow
RAG   → RAGWorkflow
TOOL  → ToolWorkflow
```

This design allows adding new workflows without modifying the agent.

---

# Document Processing

Uploaded documents pass through the following pipeline:

```text
Document
    ↓
Reader
    ↓
Analyzer
    ↓
Chunker
    ↓
Embedding Generator
    ↓
Indexer
    ↓
Document Store
    ↓
Agent State
```

Indexed documents become immediately available for semantic search.

---

# Retrieval-Augmented Generation (RAG)

Current retrieval flow:

```text
User Question
      ↓
Embedding Generation
      ↓
MMR Retriever
      ↓
Top Relevant Chunks
      ↓
Prompt Builder
      ↓
Gemini
      ↓
Answer
```

The framework uses **Maximum Marginal Relevance (MMR)** to retrieve relevant and diverse document chunks.

---

# Conversation Memory

Conversation history is maintained independently from document retrieval.

The current implementation supports:

- Multi-turn conversations
- Previous question context
- Previous assistant responses

Memory is automatically included in prompts.

---

# Tool Execution

Unlike many agent implementations, tool routing is handled by the framework instead of the LLM.

Current flow:

```text
User
 ↓
Decision Engine
 ↓
Tool Workflow
 ↓
Tool Pipeline
 ↓
Tool Executor
 ↓
Calculator Tool
```

This avoids unnecessary LLM calls for deterministic tool execution.

Current tool:

- Calculator

The architecture supports adding additional tools such as:

- Weather
- SQL
- Search
- File Operations
- Web APIs

without changing the orchestration layer.

---

# LLM Abstraction

The framework is provider-independent.

Current implementation uses **Google Gemini**, but all providers return a common response object.

```text
LLMResponse

├── content
├── tool_call
├── model_name
├── usage
├── response_time
├── finish_reason
└── created_at
```

This allows future integration with:

- OpenAI
- Anthropic
- Ollama
- Hugging Face
- Groq
- Local models

without affecting workflows.

---

# Current Features

- Modular agent architecture
- Shared agent state
- Context-based workflow routing
- Multi-workflow execution
- Retrieval-Augmented Generation
- Maximum Marginal Relevance (MMR) retrieval
- Conversation memory
- Document indexing
- In-memory vector store
- Tool execution framework
- Calculator tool
- Gemini integration
- Generic LLM abstraction
- Clean separation of responsibilities

---

# Current Workflow Routing

```text
                    User Query
                         │
                         ▼
                 Context Builder
                         │
                         ▼
                 Decision Engine
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
      CHAT             RAG             TOOL
        │                │                │
        ▼                ▼                ▼
 Chat Pipeline     RAG Pipeline     Tool Pipeline
```

---

# Technologies

- Python
- Google Gemini API
- NumPy
- Object-Oriented Programming (OOP)
- Clean Architecture
- Retrieval-Augmented Generation (RAG)
- Maximum Marginal Relevance (MMR)

---

# Current Status

## ✅ Completed

- Modular agent architecture
- Shared Agent State
- Workflow Registry
- Rule-Based Decision Engine
- Chat Workflow
- RAG Workflow
- Tool Workflow
- Document Processing Pipeline
- MMR Retriever
- In-Memory Vector Store
- Conversation Memory
- Gemini Integration
- Generic LLM Response Abstraction

---

## 🚧 In Progress

- Prompt Builder module
- Memory optimization
- Metadata-aware retrieval
- Duplicate chunk filtering

---

## 📌 Planned

- Streaming responses
- Multiple document support
- Hybrid Retrieval (Vector + BM25)
- Native Gemini Function Calling
- MCP (Model Context Protocol)
- Multi-Agent Collaboration
- Planner / Executor Architecture
- Web Search Tool
- SQL Tool
- File System Tool
- Local LLM Support (Ollama, GGUF)
- Observability & Tracing
- REST API
- Docker Deployment

---

# Design Principles

This framework is designed around the following principles:

- **Modularity** – Components can be replaced independently.
- **Extensibility** – New workflows, tools, retrievers, and LLM providers can be added easily.
- **Separation of Concerns** – Each module has a single responsibility.
- **Provider Independence** – The framework is not tied to any specific LLM.
- **Deterministic Orchestration** – Workflow and tool routing are controlled by the framework rather than delegated to the LLM.

---

# Future Vision

The long-term goal is to evolve this project into a production-ready AI Agent Framework supporting:

- Autonomous Agents
- Multi-Agent Collaboration
- Model Context Protocol (MCP)
- Pluggable Memory Systems
- Enterprise-Grade Retrieval
- Local and Cloud LLMs
- Advanced Tool Orchestration
- Agent Observability
- Scalable Deployment

---

# License

This project is being developed for educational, research, and learning purposes. Contributions, ideas, and feedback are welcome.
