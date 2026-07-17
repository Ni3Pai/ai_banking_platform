# 🏦 AI Banking Platform

A unified AI-powered platform combining 4 enterprise 
tools for banking and financial services.

Built for Dutch corporate banking context with EU 
regulatory compliance built in.

## 🛠️ Tools Included

### 1. 🏦 Customer Risk Assessment
AI-powered customer risk scoring using LLM reasoning.
Goes beyond simple rules — provides nuanced analysis
with recommendations.

### 2. 📋 AI PO User Story Generator
Generates production-ready user stories from plain 
English business requirements. Outputs:
- User story in standard format
- Given/When/Then acceptance criteria
- Definition of Done
- Story points and priority

### 3. ⚖️ EU AI Act Compliance Checker
Analyses AI use cases against EU AI Act framework.
Classifies risk tier and generates compliance requirements,
red flags and recommended actions.

### 4. 🌱 EU Taxonomy Assessment
Enterprise-grade EU Taxonomy Compass assessment for
corporate banking clients. Follows official 4-step framework:
- Taxonomy Eligibility
- Substantial Contribution
- DNSH across 6 objectives
- Minimum Social Safeguards

## 🚀 How To Run

1. Open in Google Colab
2. Add GROQ_API_KEY to Colab secrets
3. Run all cells
4. Choose a tool from the menu

## 💡 Features
- Interactive menu driven interface
- Input validation and error handling
- Returns to menu after each tool
- Handles missing or incomplete data gracefully

## 🏗️ Tech Stack
- Python
- Groq API (LLaMA 3.3)
- Google Colab

## 📁 Related Repositories
- [AI Banking Risk Assessor](link)
- [AI PO Assistant](link)
- [EU AI Act Checker](link)
- [EU Taxonomy Assessment Tool](link)

## 🔌 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Platform info |
| POST | `/risk-assessment` | Analyse customer risk |
| POST | `/user-stories` | Generate user stories |
| POST | `/eu-ai-act` | Check EU AI Act compliance |
| POST | `/eu-taxonomy` | EU Taxonomy assessment |

## Example Request
```json
POST /risk-assessment
{
    "name": "Jan de Vries",
    "balance": 750,
    "transactions": 142,
    "is_active": true
}
```

## Example Response
```json
{
    "customer_name": "Jan de Vries",
    "risk_score": 4,
    "risk_level": "Low",
    "reason": "Moderate balance with stable activity",
    "recommendation": "Continue monitoring"
}
```

## 🌍 Live API
**Base URL:** https://aibankingplatform-production.up.railway.app

**API Docs:** https://aibankingplatform-production.up.railway.app/docs

## Quick Test
```bash
curl -X POST https://aibankingplatform-production.up.railway.app/risk-assessment \
  -H "Content-Type: application/json" \

## 🧠 RAG Pipeline (Document Intelligence)

AI-powered document question answering using 
Retrieval Augmented Generation (RAG).

### How It Works
1. Upload any PDF  document
2. Document is split into chunks
3. Semantic search finds relevant sections
4. AI answers from your specific document

### Tech
- pypdf — PDF text extraction
- sentence-transformers — semantic embeddings  
- Groq API — answer generation
- Semantic search — meaning based retrieval

### Example
Question: "Which sectors require DNSH assessment?"
Answer: "Energy, Manufacturing and Transport"
← Answered from your actual document, not general knowledge


## 📚 Multi-Document RAG
AI-powered policy Q&A across multiple documents simultaneously.
Searches ESG, Credit Risk and AML policies with citations.
- LangChain + FAISS
- Cross-document semantic search
- Source citations in answers

## 🤖 Banking Compliance Agent
AI agent that reasons and uses tools to check compliance.
Automatically decides which checks to run.
- 3 compliance tools (risk, AML, credit limits)
- Multi-tool reasoning
- Complete client onboarding checks
  -d '{"name": "Jan de Vries", "balance": 750, "transactions": 142, "is_active": true}'
```
