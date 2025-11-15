README.md 
![CI](https://github.com/n0tserp/jafar/actions/workflows/ci.yml/badge.svg)
> **NOT FINANCIAL ADVICE** — Jafar is an **educational open-source tool**. Use at your own risk. No warranties.
![Deploy](https://img.shields.io/badge/Deploy-Render.com-blue)

# Jafar — Just Analyzing Financial Asset Risk

> **An open-source alternative to BlackRock’s Aladdin**  
> Real-time OSINT + macro risk scoring for US equities

---

## Jafar is a production-grade, open-source intelligence (OSINT) and macro risk engine inspired by BlackRock's Aladdin. It ingests data from OSINT sources (SEC EDGAR, X/Twitter, NewsAPI, Reddit, **earnings call transcripts via Quartr API**) and macro indicators (FRED, BLS, VIX, etc.), builds a knowledge graph in Neo4j, and computes a **Jafar Risk Score (0–100)** for US equities.

---

## QUARTR API — EARNINGS CALL INTELLIGENCE

**New in v1.1**  
Jafar now pulls **full earnings call transcripts** from [Quartr](https://quartr.com) (optional, API key required).  
CEOs say the quiet part out loud — Jafar listens.

```env
QUARTR_API_KEY=your_key
ENABLE_QUARTR=true

## Quick Start

 ```bash
 git clone https://github.com/n0tserp/jafar.git
 cd jafar
 ./scripts/setup.sh
 docker-compose up --build
 **Dashboard**: [`http://localhost:8501`](http://localhost:8501)  
 **API**: [`http://localhost:8000/risk/AAPL`](http://localhost:8000/risk/AAPL)

## Example: AAPL Risk
{
  "symbol": "AAPL",
  "jafar_risk": 72,
  "macro_regime": "High Inflation + Tightening",
  "recession_prob": 0.68,
  "signals": [
    {"source": "Quartr", "event": "Earnings Call Q4 2025", "weight": 30},
    {"source": "X", "event": "CEO lawsuit", "weight": 25}
  ]
}

## Tech Stack

 Backend: FastAPI, Prefect 2
 NLP: spaCy + Grok 4 (free tier)
 Graph: Neo4j
 UI: Streamlit
 Data: FRED, SEC-API, NewsAPI, X API, Quartr
 Deploy: Docker + Render.com (free tier)

## Roadmap

 v1.0: Core ingestion + risk scoring
 v1.1: Quartr earnings call transcripts
 v2.0: Grok 4 agent + portfolio stress tests
 Future: Slack alerts, 500+ equities

## Contributing
 Pull requests welcome! See CONTRIBUTING.md for details.

## License
 MIT © n0tserp — see LICENSE 