# Low-Level Design (LLD) - Automated Legal Document Generation

## 1. System Architecture
The system follows a microservices architecture, integrating multiple AI pipelines.

### Components:
- **API Gateway:** Routes incoming user requests to appropriate services.
- **Document Management Service:** Handles secure storage and retrieval of legal templates and user drafts.
- **AI Orchestrator (Agentic AI):** The core decision-making module that perceives user context, plans the document structure, and triggers the specialized AI models.
- **Model Inference Services:**
  - **ML Service:** Baseline predictive tasks (e.g., approval probability).
  - **DL Service:** High-dimensional data processing.
  - **NLP/SLM Service:** Summarization, entity extraction, and legal jargon processing.
  - **GenAI Service:** Novel clause drafting and scenario simulation.

## 2. Component Interactions (Sequence)
1. **User Request:** User submits IP filing requirements via UI.
2. **Orchestrator:** The Agentic Orchestrator receives the request, parses intent using the SLM, and fetches relevant templates from the Document Service.
3. **Generation Loop:** 
   - Generative AI drafts custom clauses.
   - NLP service validates against legal precedents.
   - DL/ML service scores the draft for approval likelihood.
4. **Finalization:** The Agentic Orchestrator refines the document until the approval score crosses the safety threshold, then returns it to the user.

## 3. Data Models
**FilingRequest**
- `request_id`: UUID
- `user_id`: UUID
- `filing_type`: Enum (Patent, Trademark)
- `raw_text`: String

**GeneratedDocument**
- `document_id`: UUID
- `request_id`: UUID
- `content`: Text
- `approval_score`: Float
- `status`: Enum (Draft, Ready, Filed)

## 4. API Contracts
**POST /api/v1/generate**
- Request: `{ "filing_type": "Patent", "claims": "..." }`
- Response: `{ "document_id": "1234", "status": "processing" }`

**GET /api/v1/document/{document_id}**
- Response: `{ "content": "...", "score": 0.88 }`
