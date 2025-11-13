from pydantic import BaseModel

class Signal(BaseModel):
    source: str
    event: str
    weight: int

class MacroOutlook(BaseModel):
    recession_prob: float
    inflation_shock: float
    rate_vol: float