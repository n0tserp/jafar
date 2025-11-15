![CI](https://github.com/n0tserp/jafar/actions/workflows/ci.yml/badge.svg)
![Deploy](https://img.shields.io/badge/Deploy-Render.com-blue)

> **NOT FINANCIAL ADVICE** — Educational open-source tool. Use at your own risk.

# Jafar — Just Analyzing Financial Asset Risk

> **Open-source alternative to BlackRock’s Aladdin**  
> Real-time OSINT + macro risk scoring for US equities

---

## Overview

Jafar is a production-grade risk engine that:
- Ingests **OSINT** (SEC, X, Reddit, News, **Quartr earnings calls**)
- Pulls **macro data** (FRED, VIX, CPI, yield curve)
- Builds a **Neo4j knowledge graph**
- Outputs a **Jafar Risk Score (0–100)**: `60% OSINT + 40% Macro`

---

## QUARTR API — Earnings Call Intelligence

**New in v1.1**  
- Pulls **full earnings call transcripts** from [Quartr](https://quartr.com)
- Uses **Grok 4** to detect CEO panic (zero-shot prompt)
- Optional: enable with `.env`


- QUARTR_API_KEY=your_key
- ENABLE_QUARTR=true

---

## Features

- OSINT Ingestion
  SEC filings, X posts, Reddit (r/wallstreetbets), NewsAPI, Quartr transcripts
- Macro Regime Detection
  FRED CPI, unemployment, VIX, 10Y-2Y yield curve
- Knowledge Graph
  Neo4j: Company → Officer → Event → Risk
- Jafar Risk Score60% OSINT + 40% Macro — fully auditable
- API + Dashboard
  FastAPI + Streamlit (live graph + score history)
- Orchestration
  Prefect 2 — 15-minute flows, task caching
- Docker-First
  PostgreSQL, Neo4j, Redis, Prefect, API, UI

---

## Quick Start

- git clone https://github.com/n0tserp/jafar.git
- cd jafar
- ./scripts/setup.sh
- docker-compose up --build

- Dashboard: http://localhost:8501
- API: http://localhost:8000/risk/AAPL

---

## Tech Stack

- Backend, "FastAPI, Prefect 2"
- NLP, "spaCy + Grok 4 (free tier)"
- Graph, "Neo4j"
- UI, "Streamlit"
- Data, "FRED, SEC-API, NewsAPI, X API, Quartr"
- Deploy, "Docker + Render.com (free tier)"

---

## Roadmap

- [x] v1.0: Core ingestion + risk scoring
- [x] v1.1: Quartr earnings call transcripts
- [ ] v2.0: Grok 4 agent + portfolio stress tests
- [ ] Future: Slack alerts, 500+ equities

---

## Contributing

Pull requests welcome! See CONTRIBUTING.md for setup.

---

## License

MIT © n0tserp — see LICENSE

---

## Example: AAPL Risk Score

```json
{
  "symbol": "AAPL",
  "jafar_risk": 72,
  "macro_regime": "High Inflation + Tightening",
  "recession_prob": 0.68,
  "signals": [
    {
      "source": "Quartr",
      "event": "Earnings Call Q4 2025",
      "weight": 30
    },
    {
      "source": "X",
      "event": "CEO lawsuit",
      "weight": 25
    }
  ]
}
