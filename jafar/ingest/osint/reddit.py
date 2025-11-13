import praw
from typing import List, Dict
import structlog
from jafar.config import config

logger = structlog.get_logger()

def fetch_reddit_posts(subreddit: str, limit: int = 10) -> List[Dict]:
    if not config.REDDIT_CLIENT_ID or not config.REDDIT_CLIENT_SECRET:
        logger.error("Reddit credentials not set")
        return []
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent=config.REDDIT_USER_AGENT
    )
    try:
        posts = []
        for submission in reddit.subreddit(subreddit).hot(limit=limit):
            posts.append({"title": submission.title, "selftext": submission.selftext})
        logger.info(f"Fetched {len(posts)} Reddit posts from r/{subreddit}")
        return posts
    except Exception as e:
        logger.error(f"Error fetching Reddit: {e}")
        return []