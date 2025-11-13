import requests
from typing import List, Dict
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_sec_filings(symbol: str) -> List[Dict]:
    if not config.SEC_API_KEY:
        logger.error("SEC_API_KEY not set")
        return []
    url = f"https://api.sec-api.io?token={config.SEC_API_KEY}"
    payload = {
        "query": {"query_string": {"query": f"ticker:{symbol}"}},
        "from": "0",
        "size": "10",
        "sort": [{"filedAt": {"order": "desc"}}]
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        filings = response.json()["filings"]
        logger.info(f"Fetched {len(filings)} SEC filings for {symbol}")
        return filings
    except Exception as e:
        logger.error(f"Error fetching SEC for {symbol}: {e}")
        return []