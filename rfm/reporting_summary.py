import pandas as pd

def executive_summary(rfm: pd.DataFrame, period: str = "Q4 2025") -> dict:
    total_customers = len(rfm)
    segments = rfm["segment"].value_counts()
    return {
        "period": period,
        "total_customers": total_customers,
        "champions_pct": round(segments.get("Champions", 0) / total_customers * 100, 1),
        "at_risk_count": int(segments.get("At Risk", 0)),
        "lost_count": int(segments.get("Lost", 0)),
        "avg_ltv": round(rfm["clv"].mean(), 2) if "clv" in rfm.columns else None,
        "total_revenue": round(rfm["monetary"].sum(), 2),
    }
