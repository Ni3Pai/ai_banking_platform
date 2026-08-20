# 🏦 AI Banking Platform

A modular AI platform for banking and financial services.

The platform combines AI product workflows, regulatory compliance, Retrieval-Augmented Generation (RAG), agentic AI, enterprise integration patterns, and REST APIs.

Built around Dutch and European financial-services use cases, with a focus on explainability, regulatory awareness, and production-oriented AI design.

---

## 🎯 What This Project Demonstrates

- Customer risk assessment
- AI Product Owner support
- EU AI Act compliance analysis
- EU Taxonomy assessment
- Multi-document RAG
- LangChain-based RAG
- Corrective RAG
- Banking compliance agents
- LangGraph workflows
- Microsoft Graph integration patterns
- MCP + SQLite
- FastAPI
- Docker
- Railway deployment
- Production-oriented RAG API patterns

---

## 🧩 Core Banking AI Tools

### 🏦 Customer Risk Assessment

LLM-powered customer risk scoring with:

- risk score
- risk level
- reasoning
- recommended action

### 📋 AI PO User Story Generator

Generates:

- user stories
- Given / When / Then acceptance criteria
- Definition of Done
- story points
- priority

### ⚖️ EU AI Act Compliance Checker

Analyses AI use cases and returns:

- risk classification
- compliance requirements
- red flags
- recommended actions

### 🌱 EU Taxonomy Assessment

Supports the four-step assessment:

1. Taxonomy Eligibility
2. Substantial Contribution
3. Do No Significant Harm
4. Minimum Social Safeguards

---

## 🧠 RAG & Document Intelligence

Supports semantic search across banking and compliance documents.

### Capabilities

- PDF ingestion
- text extraction and chunking
- semantic embeddings
- FAISS vector search
- multi-document retrieval
- metadata-aware chunks
- source filename reporting
- grounded LLM answers

### Corrective RAG

Adds relevance grading after retrieval:

```text
Question
↓
Vector search
↓
Top candidate chunks
↓
LLM relevance grading
↓
Relevant context
↓
Grounded answer
```

Example use cases:

- Credit Risk Policy Q&A
- AML policy search
- ESG policy comparison
- regulatory document analysis

---

## 🤖 Agentic AI

### Banking Compliance Agent

AI agent that dynamically selects tools for:

- customer risk checks
- AML checks
- credit-limit checks

### LangGraph

Used to model structured and stateful AI workflows using:

- nodes
- edges
- conditional routing
- state transitions

---

## 🔌 Enterprise Integration

### Microsoft Graph

Explores enterprise AI integration patterns for:

- Teams
- Outlook
- SharePoint

### MCP + SQLite

Demonstrates how an AI application can interact with external systems:

```text
AI Application
↓
MCP Client
↓
MCP Server
↓
Database / External System
```

---

## 🚀 Production-Oriented RAG API

The FastAPI RAG module includes:

- PDF upload and validation
- text extraction
- chunking
- embeddings
- FAISS vector storage
- similarity search
- relevance grading
- grounded answer generation
- document listing
- document deletion

### API Flow

```text
POST /upload-document
        ↓
PDF validation
        ↓
Text extraction
        ↓
Chunking
        ↓
Embeddings
        ↓
FAISS

POST /ask
        ↓
Similarity search
        ↓
Relevance grading
        ↓
Relevant context
        ↓
LLM answer
```

---

## 🔌 API Endpoints

### Banking Platform

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Platform information |
| POST | `/risk-assessment` | Customer risk analysis |
| POST | `/user-stories` | Generate user stories |
| POST | `/eu-ai-act` | EU AI Act assessment |
| POST | `/eu-taxonomy` | EU Taxonomy assessment |

### Production RAG

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Service health check |
| POST | `/upload-document` | Upload and ingest a PDF |
| GET | `/documents` | List uploaded documents |
| POST | `/ask` | Ask a grounded question |
| DELETE | `/documents/{document_id}` | Delete a document |

---

## 🏗️ Tech Stack

### AI & Orchestration
- Groq API
- LangChain
- LangGraph
- Sentence Transformers
- Hugging Face embeddings

### Retrieval & Data
- FAISS
- PyPDF
- SQLite

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn

### Enterprise Integration
- Microsoft Graph patterns
- MCP

### Deployment
- Docker
- Railway

---

## 🌍 Live API

**Base URL**

`https://aibankingplatform-production.up.railway.app`

**Swagger API Docs**

`https://aibankingplatform-production.up.railway.app/docs`

---

## 🏗️ Architecture Evolution

This repository shows the progression from simple AI tools toward enterprise AI patterns:

```text
LLM API
↓
Structured AI outputs
↓
Unified banking tools
↓
FastAPI
↓
Docker
↓
Cloud deployment
↓
RAG
↓
Multi-document RAG
↓
LangChain
↓
AI Agents
↓
LangGraph
↓
Corrective RAG
↓
MCP + SQLite
↓
Production-oriented RAG API
```

---

## ☁️ Planned Production Evolution

The current implementation uses local and in-memory components for learning and prototyping.

A future Azure architecture could use:

```text
                 FastAPI
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
 Azure Blob     Azure AI     Metadata
  Storage        Search       Database
```

Potential improvements include:

- Azure Blob Storage
- Azure AI Search
- PostgreSQL or Cosmos DB
- Microsoft Entra ID / OAuth2
- Azure Key Vault
- CI/CD
- observability
- retries and rate limiting
- persistent document lifecycle management

---

## 🎯 Skills Demonstrated

### AI Product Owner / AI Product Manager
- AI workflow design
- structured output design
- human-in-the-loop thinking
- model-selection tradeoffs
- quality, latency, cost, and risk balancing

### AI Consultant
- banking AI use-case design
- EU AI Act
- EU Taxonomy
- AI governance
- enterprise integration patterns
- production architecture recommendations

### Forward Deployment Engineer
- Python
- FastAPI
- Docker
- RAG
- vector search
- agents
- LangGraph
- MCP
- enterprise integration
- deployment
- debugging

---

## ⚠️ Current Limitations

This is a portfolio and learning implementation, not a production banking system.

Current limitations include:

- in-memory FAISS
- process-local document metadata
- no persistent PDF storage
- limited authentication
- limited observability
- filename-level rather than page-level source reporting

These limitations are documented intentionally to show the next architectural steps toward production.

---

## 👤 Portfolio Context

This project sits at the intersection of:

**Financial Services + AI Product Management + AI Governance + Enterprise AI Engineering**
