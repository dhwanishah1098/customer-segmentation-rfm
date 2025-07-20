import pandas as pd
from datetime import datetime

def flag_at_risk(rfm: pd.DataFrame, recency_threshold: int = 90, freq_min: int = 2) -> pd.DataFrame:
    df = rfm.copy()
    df["churn_risk"] = (
        (df["recency"] >= recency_threshold) &
        (df["frequency"] >= freq_min)
    )
    df["churn_risk_score"] = (df["recency"] / df["recency"].max() * 0.6 +
                               (1 - df["frequency"] / df["frequency"].max()) * 0.4).round(3)
    return df
