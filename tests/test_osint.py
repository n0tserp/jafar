import pytest
from jafar.ingest.osint.sec import fetch_sec_filings

def test_fetch_sec_filings():
    filings = fetch_sec_filings("AAPL")
    assert isinstance(filings, list)