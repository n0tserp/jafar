![CI](https://github.com/n0tserp/jafar/actions/workflows/ci.yml/badge.svg)
![Deploy](https://img.shields.io/badge/Deploy-Render.com-blue)

> **NOT FINANCIAL ADVICE** — Educational tool only. Use at your own risk.

# Jafar — Just Analyzing Financial Asset Risk

> **Open-source alternative to BlackRock’s Aladdin**  
> Real-time OSINT + macro risk scoring for US equities

---

## What It Does
- Ingests **SEC filings**, **X posts**, **Reddit**, **NewsAPI**, **Quartr earnings calls**
- Pulls **FRED**, **VIX**, **CPI**, **unemployment**
- Builds **Neo4j knowledge graph**
- Computes **Jafar Risk Score (0–100)**: `60% OSINT + 40% Macro`

---

## QUARTR API — Earnings Call Intelligence

**New in v1.1**  
- Pulls full earnings call transcripts from [Quartr](https://quartr.com)
- Detects CEO panic with **Grok 4**

```env
QUARTR_API_KEY=your_key
ENABLE_QUARTR=true

Features

- OSINT Ingestion: SEC, X, Reddit, Quartr
- Macro Detection: FRED, VIX, yield curve
- Knowledge Graph: Neo4j (Company → Event → Risk)
- Risk Score: 60% OSINT + 40% Macro
- API + Dashboard: FastAPI + Streamlit
- Orchestration: Prefect 2 (15-min flows)
- Docker-First: PostgreSQL, Neo4j, Redis

Quick Start
git clone https://github.com/n0tserp/jafar.git
cd jafar
./scripts/setup.sh
docker-compose up --build
- Dashboard: http://localhost:8501
- API: http://localhost:8000/risk/AAPL

EXAMPLE: AAPL Risk
{
  "symbol": "AAPL",
  "jafar_risk": 72,
  "macro_regime": "High Inflation + Tightening",
  "signals": [
    {"source": "Quartr", "event": "Earnings Call Q4 2025", "weight": 30},
    {"source": "X", "event": "CEO lawsuit", "weight": 25}
  ]
}

Tech Stack

- Backend: FastAPI, Prefect 2
- NLP: spaCy + Grok 4 (free tier)
- Graph: Neo4j
- UI: Streamlit
- Data: FRED, SEC-API, NewsAPI, X API, Quartr
- Deploy: Docker + Render.com

Roadmap

 [x] v1.0: Core ingestion + scoring
 [x] v1.1: Quartr earnings transcripts
 [ ] v2.0: Grok 4 agent + stress tests
 [ ] Future: Slack alerts, 500+ equities

 Contributing
Pull requests welcome! See CONTRIBUTING.md

License
MIT © n0tserp — see LICENSE