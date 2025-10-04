import pandas as pd
import numpy as np


def estimate_clv(rfm: pd.DataFrame, avg_lifespan_years: float = 3.0, discount_rate: float = 0.1) -> pd.DataFrame:
    rfm = rfm.copy()
    rfm["purchase_rate"] = rfm["frequency"] / (rfm["recency"] / 30 + 1)
    rfm["avg_order_value"] = rfm["monetary"] / rfm["frequency"]
    rfm["clv"] = (rfm["avg_order_value"] * rfm["purchase_rate"] * 12 * avg_lifespan_years) / (1 + discount_rate)
    return rfm[["customer_id", "segment", "monetary", "clv"]].round(2)
