from scipy.special import expit  # Logistic
from typing import float

def compute_recession_prob(inversion: int, inflation: float, vol: float) -> float:
    # Simple logistic model
    logit = -2.0 + 1.5 * inversion + 1.0 * inflation + 0.8 * vol
    return expit(logit)