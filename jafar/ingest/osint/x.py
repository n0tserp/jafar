import tweepy
from typing import List, Dict
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_x_posts(query: str, limit: int = 10) -> List[Dict]:
    if not config.X_BEARER_TOKEN:
        logger.error("X_BEARER_TOKEN not set")
        return []
    client = tweepy.Client(bearer_token=config.X_BEARER_TOKEN)
    try:
        tweets = client.search_recent_tweets(query=query, max_results=limit, tweet_fields=['text', 'created_at'])
        data = [{"text": t.text, "created_at": str(t.created_at)} for t in tweets.data or []]
        logger.info(f"Fetched {len(data)} X posts for query: {query}")
        return data
    except Exception as e:
        logger.error(f"Error fetching X posts: {e}")
        return []