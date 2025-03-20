import pandas as pd
from datetime import datetime


def calculate_rfm(df: pd.DataFrame, snapshot_date: datetime = None) -> pd.DataFrame:
    if snapshot_date is None:
        snapshot_date = df["order_date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("customer_id").agg(
        recency=("order_date", lambda x: (snapshot_date - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("revenue", "sum"),
    ).reset_index()
    return rfm


def score_rfm(rfm: pd.DataFrame, quantiles: int = 5) -> pd.DataFrame:
    rfm = rfm.copy()
    rfm["R_score"] = pd.qcut(rfm["recency"], quantiles, labels=range(quantiles, 0, -1))
    rfm["F_score"] = pd.qcut(rfm["frequency"].rank(method="first"), quantiles, labels=range(1, quantiles + 1))
    rfm["M_score"] = pd.qcut(rfm["monetary"].rank(method="first"), quantiles, labels=range(1, quantiles + 1))
    rfm["RFM_score"] = rfm["R_score"].astype(str) + rfm["F_score"].astype(str) + rfm["M_score"].astype(str)
    rfm["RFM_total"] = rfm[["R_score", "F_score", "M_score"]].astype(int).sum(axis=1)
    return rfm
