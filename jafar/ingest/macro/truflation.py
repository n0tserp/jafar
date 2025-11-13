import requests
from typing import float
import structlog
from jafar.config import config

logger = structlog.get_logger()

def get_truflation_cpi() -> float:
    if not config.TRUFLATION_API_KEY:
        logger.error("TRUFLATION_API_KEY not set")
        return 0.0
    url = "https://api.truflation.com/cpi"  # Hypothetical endpoint
    headers = {"Authorization": f"Bearer {config.TRUFLATION_API_KEY}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return float(response.json()["cpi"])
    except Exception as e:
        logger.error(f"Error fetching Truflation: {e}")
        return 0.0