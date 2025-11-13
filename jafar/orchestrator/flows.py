from prefect import flow
from jafar.ingest.scheduler import ingest_osint_flow, ingest_macro_flow
from jafar.nlp.extractor import extract_entities, grok_sentiment_event
# Add more integration

@flow
def score_flow(symbols: list[str]):
    ingest_osint_flow(symbols)
    ingest_macro_flow()
    # Process with NLP, update graph, compute scores