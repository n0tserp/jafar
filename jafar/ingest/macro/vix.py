from .fred import fetch_fred_series
import structlog

logger = structlog.get_logger()

def get_vix() -> float:
    data = fetch_fred_series("VIXCLS")
    if data and data["observations"]:
        return float(data["observations"][-1]["value"])
    return 0.0