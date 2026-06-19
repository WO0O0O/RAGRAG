# FinSpam Shield

An ultra-fast, pre-ingestion data-hygiene API designed to drop automated spam domains and programmatic content farms before they touch your Retrieval-Augmented Generation (RAG) vector embeddings.

* **Fast:** Response times under 15ms per URL.
* **Lightweight:** Stateless, running entirely in-memory at the metadata/lexical layer. No scraping or heavy network requests.
* **Pluggable:** Built with an extensible core to support multiple industries (starting with Finance / Ticker-Stuffing filters).

## Core API

### `POST /v1/triage`
Filters an array of URLs at the lexical and domain levels.

**Request:**
```http
POST /v1/triage
Header X-API-Key: your_api_key
Content-Type: application/json

[
  "https://nasdaq-trends-now.icu/news/AAPL-MSFT-NVDA-TSLA-analysis",
  "https://pragmaticengineer.substack.com/p/software-engineering-trends"
]
```

**Response:**
```json
[
  {
    "url": "https://nasdaq-trends-now.icu/news/AAPL-MSFT-NVDA-TSLA-analysis",
    "allow": false,
    "reason": "Programmatic financial spam detected (ticker-stuffing / domain blacklist)"
  },
  {
    "url": "https://pragmaticengineer.substack.com/p/software-engineering-trends",
    "allow": true,
    "reason": null
  }
]
```

## Running the Project

### 1. Install Dependencies
```bash
pip install -e .
# or
pip install -r requirements.txt
```

### 2. Configure Settings
Copy `.env.example` to `.env` and set your static API key:
```bash
FINSPAM_API_KEY=your_secure_api_key
```

### 3. Start the API Server
```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

## Documentation
For deeper dives, see the docs:
* Detailed specifications & heuristics: [docs/overview.md](file:///Users/danwooster/1. DEV/RAG-watcher/docs/overview.md)
* Roadmap and milestones: [docs/phases.md](file:///Users/danwooster/1. DEV/RAG-watcher/docs/phases.md)
* AI Developer guidelines: [docs/prompt.md](file:///Users/danwooster/1. DEV/RAG-watcher/docs/prompt.md)
* Testing instructions: [docs/testing.md](file:///Users/danwooster/1. DEV/RAG-watcher/docs/testing.md)
# RAGRAG
