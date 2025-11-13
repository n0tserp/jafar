from newsapi import NewsApiClient
from typing import List, Dict
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_news(query: str, limit: int = 10) -> List[Dict]:
    if not config.NEWSAPI_KEY:
        logger.error("NEWSAPI_KEY not set")
        return []
    newsapi = NewsApiClient(api_key=config.NEWSAPI_KEY)
    try:
        articles = newsapi.get_everything(q=query, page_size=limit)
        data = articles['articles']
        logger.info(f"Fetched {len(data)} news articles for {query}")
        return data
    except Exception as e:
        logger.error(f"Error fetching news: {e}")
        return []