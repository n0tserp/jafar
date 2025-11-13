import requests
from typing import List, Dict
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_bls_series(series_ids: List[str]) -> List[Dict]:
    if not config.BLS_API_KEY:
        logger.error("BLS_API_KEY not set")
        return []
    url = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
    payload = {
        "seriesid": series_ids,
        "startyear": "2020",
        "endyear": "2025",
        "registrationkey": config.BLS_API_KEY
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()["Results"]["series"]
        logger.info(f"Fetched BLS series: {series_ids}")
        return data
    except Exception as e:
        logger.error(f"Error fetching BLS: {e}")
        return []