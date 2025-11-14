import os
import requests
import structlog
from typing import List, Dict

logger = structlog.get_logger()

QUARTR_API_KEY = os.getenv("QUARTR_API_KEY")

def get_quartr_transcripts(symbol: str, limit: int = 4) -> List[Dict]:
    if not QUARTR_API_KEY:
        logger.info("QUARTR_API_KEY not set — skipping Quartr")
        return []

    url = "https://api.quartr.com/v1/transcripts"
    headers = {"Authorization": f"Bearer {QUARTR_API_KEY}"}
    params = {"ticker": symbol, "limit": limit}

    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        transcripts = []
        for item in data.get("transcripts", []):
            transcripts.append({
                "source": "Quartr",
                "event": f"Earnings Call Q{item['quarter']} {item['year']}",
                "text": item["transcript"],
                "weight": 30,
                "date": item["date"]
            })
        logger.info(f"Quartr: {len(transcripts)} transcripts for {symbol}")
        return transcripts
    except Exception as e:
        logger.error(f"Quartr API error: {e}")
        return []