import spacy
import httpx
from typing import Dict, List
import structlog
from jafar.config import config

logger = structlog.get_logger()

nlp = spacy.load("en_core_web_sm")

async def extract_entities(text: str) -> List[Dict]:
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities

async def grok_sentiment_event(text: str) -> Dict:
    if not config.GROK_API_KEY:
        logger.error("GROK_API_KEY not set")
        return {"sentiment": 0.0, "events": []}
    url = "https://api.x.ai/grok"  # Hypothetical Grok API endpoint
    payload = {
        "prompt": f"Analyze sentiment and extract events: {text}",
        "model": "grok-4"
    }
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            return {"sentiment": data.get("sentiment", 0.0), "events": data.get("events", [])}
    except Exception as e:
        logger.error(f"Error calling Grok API: {e}")
        return {"sentiment": 0.0, "events": []}