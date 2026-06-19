# FinSpam Shield - Overview & Requirements

## Core Value Proposition
FinSpam Shield is a stateless, high-performance inline firewall for quantitative hedge funds, private equity firms, and market intelligence startups running Retrieval-Augmented Generation (RAG) pipelines. It drops programmatic SEO content farms and keyword-stuffed news URLs before they touch vector embeddings, preventing sentiment skew and compliance issues.

## MVP Specifications (1-Week Scope)
* **API Endpoint**: `POST /v1/triage`
  * Accepts: JSON array of URLs (e.g., `["https://nasdaq-trends-now.icu/news/AAPL-MSFT", "https://pragmaticengineer.substack.com/p/issue"]`).
  * Returns: List of objects containing URL and binary verdict (`allow: true` or `allow: false`).
* **SLA**: Under 15ms response time per URL.
* **Authentication**: Strict validation via a static `X-API-Key` passed in the request header.

## Out of Scope
* **NO HTTP Request Execution**: Do not crawl, scrape, or fetch the HTML content of the target sites.
* **NO Multi-Tenant Dashboard**: No user registration, settings, usage charts, or UI.

## Core Gotchas & Heuristics
1. **Subdomain Neutrality (The Substack/Medium Dilemma)**: Root blogging platforms (e.g., `substack.com`, `medium.com`) are neutral. Spam occurs on individual creator subdomains. Your parsing engine must verify creator subdomains independently of the root domain.
2. **Ticker Collision**: Content farms aggressively keyword-stuff URLs (e.g., `/news/AAPL-MSFT-NVDA-TSLA-AMZN`). A legitimate news URL might contain a few tickers (e.g., `/news/AAPL-earnings-2026`). The engine must differentiate between normal ticker mention and high-density keyword stuffing.

## Compliance Leverage
* **SEC Rule 204-2 (Books and Records)**: Regulated entities must verify the integrity of inputs used to formulate investment advice.
* **FINRA Rule 2020**: Prevention of acting on automated market rumors.

---

## Architectural Scaling & Extensibility Design
To support scaling to other industries (e.g. Legal, Medical, Tech) in the future, the triage codebase must follow these structural guidelines:
1. **Core Triage Coordinator**: Decoupled from industry-specific business rules. It handles URL parsing, subdomain extraction, and routing requests to active validators.
2. **Pluggable Industry Evaluators (SOLID - Open/Closed Principle)**: Industry-specific logic must reside in self-contained evaluator classes implementing a common `TriageEvaluator` interface.
3. **Seed lists and Datasets isolation**: Blacklist/whitelist files and seed domain datasets must be loaded dynamically based on active industry categories.

