from jafar.config import config
from jafar.config import config
from prefect import flow, task
from prefect.tasks import task_input_hash
from prefect.deployments import Deployment
from datetime import timedelta
import structlog

from .osint import sec, x, news, reddit, pdf_earnings
from .macro import fred, bls, vix, truflation

logger = structlog.get_logger()

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=15), retries=3)
def ingest_osint_task(symbol: str):
    # Ingest from all OSINT sources
    sec_filings = sec.fetch_sec_filings(symbol)
    x_posts = x.fetch_x_posts(f"{symbol} stock")
    news_articles = news.fetch_news(symbol)
    reddit_posts = reddit.fetch_reddit_posts("wallstreetbets")  # Example subreddit
    # For PDFs, assume urls from filings
    pdf_text = pdf_earnings.extract_earnings_text("example_url.pdf") if sec_filings else ""
    return {"sec": sec_filings, "x": x_posts, "news": news_articles, "reddit": reddit_posts, "pdf": pdf_text}

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1), retries=3)
def ingest_macro_task():
    cpi = truflation.get_truflation_cpi() if config.ENABLE_TRUFLATION and config.TRUFLATION_API_KEY else fred.get_fred_cpi()
    vix_value = vix.get_vix()
    # Add more: 10Y, PMI, etc.
    ten_y = fred.fetch_fred_series("DGS10")["observations"][-1]["value"] if fred.fetch_fred_series("DGS10") else 0.0
    pmi = fred.fetch_fred_series("NAPMPMI")["observations"][-1]["value"] if fred.fetch_fred_series("NAPMPMI") else 0.0
    bls_data = bls.fetch_bls_series(["LNS14000000"])  # Unemployment
    return {"cpi": cpi, "vix": vix_value, "10y": ten_y, "pmi": pmi, "bls": bls_data}

@flow
def ingest_osint_flow(symbols: list[str]):
    for symbol in symbols:
        ingest_osint_task(symbol)

@flow
def ingest_macro_flow():
    ingest_macro_task()