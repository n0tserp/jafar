import requests
from typing import Dict, Optional
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_fred_series(series_id: str, observation_start: str = "2020-01-01") -> Optional[Dict]:
    if not config.FRED_API_KEY:
        logger.error("FRED_API_KEY not set")
        return None
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": config.FRED_API_KEY,
        "file_type": "json",
        "observation_start": observation_start
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Fetched FRED series {series_id}")
        return data
    except Exception as e:
        logger.error(f"Error fetching FRED {series_id}: {e}")
        return None

def get_fred_cpi() -> float:
    data = fetch_fred_series("CPIAUCSL")
    if data and data["observations"]:
        return float(data["observations"][-1]["value"])
    return 0.0