# Testing & Verification Guidelines

## Test Framework
We use `pytest` and `httpx` (for FastAPI test clients) to verify all behavior.

## Core Test Scenarios
1. **API Authentication**:
   * Request with valid `X-API-Key` returns 200.
   * Request with missing/invalid key returns 401.
2. **Domain/Lexical Heuristics**:
   * Root domains in spam blacklist must be rejected.
   * Clean Substack subdomains (e.g., verified lists) allowed; spam/programmatic Substack creator subdomains blocked.
   * Legitimate news slugs (e.g., `/news/AAPL-earnings-report`) allowed.
   * Extreme keyword-stuffed slugs (e.g., `/news/AAPL-MSFT-NVDA-TSLA-COIN-AMD-intel-trends`) blocked.
3. **Performance Benchmarks**:
   * Simulating a load of 5,000 URLs to verify response time target (<15ms per URL).
