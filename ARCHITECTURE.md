# Jafar Architecture

## Overview
Jafar ingests OSINT and macro data, processes via NLP, builds a knowledge graph, computes risk scores, and serves via API/Dashboard.

## Mermaid Diagram: OSINT + Macro → Graph → Risk

```mermaid
graph TD
    A[OSINT Sources: SEC, X, News, Reddit, PDFs] --> B[Ingest OSINT Flow (Prefect)]
    C[Macro Sources: FRED, BLS, VIX, 10Y, PMI, Truflation*] --> D[Ingest Macro Flow (Prefect)]
    B --> E[NLP Extractor: spaCy Entities + Grok 4 Sentiment/Events]
    D --> F[Macro Regime Model: Recession Prob, Inflation Shock]
    E --> G[Neo4j Knowledge Graph: Company ↔ Officer ↔ Event ↔ Risk]
    F --> G
    G --> H[Risk Scorer: 60% OSINT + 40% Macro → Jafar Risk (0-100)]
    H --> I[FastAPI: /risk/{symbol}, /macro/outlook]
    H --> J[Streamlit Dashboard: Heatmap + Macro Gauges]