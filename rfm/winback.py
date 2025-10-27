import pandas as pd

def identify_winback_candidates(rfm: pd.DataFrame, min_historical_revenue: float = 500.0,
                                 recency_min: int = 91, recency_max: int = 365) -> pd.DataFrame:
    return (rfm[
        (rfm["recency"].between(recency_min, recency_max)) &
        (rfm["monetary"] >= min_historical_revenue)
    ].sort_values("monetary", ascending=False)
     .assign(winback_priority=lambda d: (d["monetary"] / d["recency"]).round(2))
     .reset_index(drop=True))
