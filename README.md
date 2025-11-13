# Jafar: Open-Source OSINT + Macro Risk Engine

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![CI Status](https://github.com/yourusername/jafar/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/jafar/actions)

Just Analyzing Financial Asset Risk

Jafar is a production-grade, open-source intelligence (OSINT) and macro risk engine inspired by BlackRock's Aladdin. It ingests data from OSINT sources (SEC EDGAR, X/Twitter, NewsAPI, Reddit, earnings PDFs) and macro indicators (FRED, BLS, VIX, etc.), builds a knowledge graph in Neo4j, and computes a Jafar Risk Score for US equities.

## Why Jafar > Aladdin (Open-Source Edition)
- **Open-Source & Free**: Unlike proprietary systems, Jafar uses only open-source tools + Grok 4 API (free tier).
- **Macro-Integrated Risk**: Blends OSINT signals (60%) with macro regimes (40%) for holistic risk assessment.
- **Scalable & Deployable**: Runs on Docker + Prefect 2, deployable on Render/Fly.io/AWS Free Tier.
- **Demo-Ready**: One-click setup with sample data for AAPL + macro indices.

![Jafar Dashboard Demo](demo/demo.gif)

## Quick Start
1. Clone the repo: `git clone https://github.com/yourusername/jafar.git`
2. Set up environment: Copy `.env.example` to `.env` and fill in API keys (e.g., NEWSAPI_KEY, GROK_API_KEY).
3. Run: `docker-compose up --build`
4. Access:
   - Streamlit Dashboard: http://localhost:8501
   - FastAPI Docs: http://localhost:8000/docs
5. Demo: Run `./scripts/run_demo.sh` to populate sample data.

## Features
- **Ingestion**: OSINT (every 15 min) + Macro (daily).
- **NLP**: Entity extraction (spaCy) + Sentiment/Events (Grok 4).
- **Knowledge Graph**: Neo4j for Company ↔ Officer ↔ Macro Event ↔ Risk Signal.
- **Risk Scoring**: Jafar Risk (0-100) with macro overlays (recession prob, inflation).
- **Optional Truflation**: Toggle via `ENABLE_TRUFLATION=True` (falls back to FRED CPI).
- **Dashboard**: Risk heatmap + Macro Outlook panel (gauges for inflation, rates, VIX).
- **API**: Endpoints for risk scores and macro outlooks.

## Demo GIF Instructions
Record using tools like Peek or ScreenToGif:
1. Start docker-compose.
2. Navigate to Streamlit: Show risk heatmap for AAPL.
3. Simulate risk spike (e.g., mock high inflation).
4. Show Macro Outlook gauges updating.
5. Export as `demo/demo.gif`.

## Sample Macro Query
"What happens to tech if CPI > 4%?"  
- Jafar simulates: Higher risk scores for rate-sensitive tech stocks due to tightening regime.

For more, see [ARCHITECTURE.md](ARCHITECTURE.md) and [ROADMAP.md](ROADMAP.md).