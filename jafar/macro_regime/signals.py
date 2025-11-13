from typing import Dict, float
from .model import compute_recession_prob

def get_macro_signals(macro_data: Dict) -> Dict:
    cpi = macro_data["cpi"]
    vix = macro_data["vix"]
    ten_y = macro_data["10y"]
    # Assume 2Y yield for inversion
    two_y = 4.0  # Mock, fetch from FRED DGS2
    inversion = 1 if ten_y - two_y < 0 else 0
    inflation_shock = 1 if cpi > 4 else 0
    rate_vol = vix / 20  # Normalized
    
    recession_prob = compute_recession_prob(inversion, inflation_shock, rate_vol)
    
    return {
        "recession_prob": recession_prob,
        "inflation_shock": inflation_shock,
        "rate_vol": rate_vol,
        "signals": [{"source": "Macro", "event": "Yield curve inverted" if inversion else "Stable", "weight": 18}]
    }