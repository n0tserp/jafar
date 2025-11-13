import pytest
from jafar.nlp.risk_scorer import compute_jafar_risk

def test_compute_jafar_risk():
    osint = [{"weight": 50}]
    macro = {"recession_prob": 0.5, "inflation_shock": 0.5, "rate_vol": 0.5}
    risk = compute_jafar_risk(osint, macro)
    assert 0 <= risk["jafar_risk"] <= 100