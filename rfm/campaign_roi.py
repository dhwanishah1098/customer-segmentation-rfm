import pandas as pd

def calculate_campaign_roi(spend: float, incremental_revenue: float, margin: float = 0.35) -> dict:
    incremental_profit = incremental_revenue * margin
    roi = (incremental_profit - spend) / spend * 100
    return {
        "spend": round(spend, 2),
        "incremental_revenue": round(incremental_revenue, 2),
        "incremental_profit": round(incremental_profit, 2),
        "roi_pct": round(roi, 2),
        "profitable": roi > 0,
    }
