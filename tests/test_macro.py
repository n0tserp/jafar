import pytest
from jafar.ingest.macro.fred import get_fred_cpi

def test_get_fred_cpi():
    cpi = get_fred_cpi()
    assert cpi > 0