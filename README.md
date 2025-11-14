README.md 
# Jafar — Just Analyzing Financial Asset Risk

> **An open-source alternative to BlackRock’s Aladdin**  
> Real-time OSINT + macro risk scoring for US equities

---

## Jafar is a production-grade, open-source intelligence (OSINT) and macro risk engine inspired by BlackRock's Aladdin. It ingests data from OSINT sources (SEC EDGAR, X/Twitter, NewsAPI, Reddit, earnings PDFs) and macro indicators (FRED, BLS, VIX, etc.), builds a knowledge graph in Neo4j, and computes a **Jafar Risk Score (0–100)** for US equities.

---

## Features

| Feature | Description |
|-------|-----------|
| **OSINT Ingestion** | SEC filings, X posts, news, Reddit, **earnings call transcripts (Quartr)** |
| **Macro Regime Detection** | FRED CPI, unemployment, VIX, yield curve |
| **Knowledge Graph** | Neo4j: `Company → Officer → Event → Risk` |
| **Jafar Risk Score** | `60% OSINT + 40% Macro` |
| **API + Dashboard** | FastAPI + Streamlit |
| **Orchestration** | Prefect 2 (15-min flows) |
| **Docker-First** | PostgreSQL, Neo4j, Redis, Prefect |

---

## Quick Start

```bash
git clone https://github.com/n0tserp/jafar.git
cd jafar
./scripts/setup.sh
docker-compose up --build

Dashboard: http://localhost:8501
API: http://localhost:8000/risk/AAPL

Example: AAPL Risk
{
  "symbol": "AAPL",
  "jafar_risk": 72,
  "macro_regime": "High Inflation + Tightening",
  "recession_prob": 0.68,
  "signals": [
    {"source": "X", "event": "CEO lawsuit", "weight": 25},
    {"source": "Macro", "event": "Yield curve inverted", "weight": 18}
  ]
}

Tech Stack

Backend: FastAPI, Prefect 2
NLP: spaCy + Grok 4 (free tier)
Graph: Neo4j
UI: Streamlit
Data: FRED, SEC-API, NewsAPI, X API
Deploy: Docker + Render.com (free tier)

Roadmap

 v1.0: Core ingestion + risk scoring
 v2.0: Grok 4 agent + portfolio stress tests
 Future: Slack alerts, 500+ equities

 Contributing
Pull requests welcome! See CONTRIBUTING.md for details.

License
MIT © n0tserp — see LICENSE
