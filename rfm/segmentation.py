import pandas as pd


SEGMENT_MAP = {
    "Champions": lambda r: (r["R_score"] >= 4) & (r["F_score"] >= 4) & (r["M_score"] >= 4),
    "Loyal Customers": lambda r: (r["F_score"] >= 3) & (r["RFM_total"] >= 10),
    "Potential Loyalists": lambda r: (r["R_score"] >= 3) & (r["F_score"] <= 3) & (r["RFM_total"] >= 8),
    "New Customers": lambda r: (r["R_score"] >= 4) & (r["F_score"] == 1),
    "At Risk": lambda r: (r["R_score"] <= 2) & (r["F_score"] >= 3),
    "Cant Lose Them": lambda r: (r["R_score"] == 1) & (r["F_score"] >= 4),
    "Hibernating": lambda r: (r["R_score"] <= 2) & (r["F_score"] <= 2),
    "Lost": lambda r: (r["R_score"] == 1) & (r["F_score"] == 1),
}


def assign_segments(rfm: pd.DataFrame) -> pd.DataFrame:
    rfm = rfm.copy()
    rfm["segment"] = "Others"
    for segment, condition in SEGMENT_MAP.items():
        mask = condition(rfm) & (rfm["segment"] == "Others")
        rfm.loc[mask, "segment"] = segment
    return rfm


def segment_summary(rfm: pd.DataFrame) -> pd.DataFrame:
    return (
        rfm.groupby("segment")
        .agg(
            customers=("customer_id", "count"),
            avg_recency=("recency", "mean"),
            avg_frequency=("frequency", "mean"),
            avg_monetary=("monetary", "mean"),
            total_revenue=("monetary", "sum"),
        )
        .round(2)
        .sort_values("total_revenue", ascending=False)
        .reset_index()
    )
