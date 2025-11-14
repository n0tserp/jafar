from typing import List, Dict
from typing import Dict, float
import numpy as np
import structlog

logger = structlog.get_logger()


def compute_jafar_risk(osint_signals: List[Dict], macro_signals: Dict) -> Dict:
    # OSINT 60%
    osint_score = np.mean([s["weight"] for s in osint_signals]) * 0.6 if osint_signals else 0.0
    
    # Macro 40%
    recession_prob = macro_signals.get("recession_prob", 0.0)
    inflation_shock = macro_signals.get("inflation_shock", 0.0)
    rate_vol = macro_signals.get("rate_vol", 0.0)
    macro_score = (recession_prob + inflation_shock + rate_vol) / 3 * 40
    
    total_risk = int(osint_score + macro_score)
    regime = "High Inflation + Tightening" if inflation_shock > 0.5 else "Stable"
    
    return {
        "jafar_risk": total_risk,
        "macro_regime": regime,
        "recession_prob": recession_prob,
        "signals": osint_signals + macro_signals.get("signals", [])
    }