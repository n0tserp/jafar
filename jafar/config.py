import os
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

class Config:
    NEWSAPI_KEY: Optional[str] = os.getenv("NEWSAPI_KEY")
    REDDIT_CLIENT_ID: Optional[str] = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET: Optional[str] = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT: str = os.getenv("REDDIT_USER_AGENT", "jafar/0.1")
    X_BEARER_TOKEN: Optional[str] = os.getenv("X_BEARER_TOKEN")
    SEC_API_KEY: Optional[str] = os.getenv("SEC_API_KEY")
    FRED_API_KEY: Optional[str] = os.getenv("FRED_API_KEY")
    BLS_API_KEY: Optional[str] = os.getenv("BLS_API_KEY")
    GROK_API_KEY: Optional[str] = os.getenv("GROK_API_KEY")
    TRUFLATION_API_KEY: Optional[str] = os.getenv("TRUFLATION_API_KEY")
    ENABLE_TRUFLATION: bool = os.getenv("ENABLE_TRUFLATION", "False").lower() == "true"
    
    NEO4J_URI: str = os.getenv("NEO4J_URI", "neo4j://localhost:7687")
    NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "neo4j_pass")
    
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Feature flags, etc.

config = Config()