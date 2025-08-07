import pandas as pd
from rfm.calculator import calculate_rfm, score_rfm
from rfm.segmentation import assign_segments, segment_summary
from datetime import datetime

def make_rfm():
    txns = pd.DataFrame({
        "customer_id": list(range(50)),
        "order_id":    [f"O{i}" for i in range(50)],
        "order_date":  pd.date_range("2024-01-01", periods=50, freq="3D"),
        "revenue":     [float(i * 100 + 50) for i in range(50)],
    })
    rfm = calculate_rfm(txns, datetime(2024,12,31))
    return score_rfm(rfm)

def test_all_customers_segmented():
    rfm = assign_segments(make_rfm())
    assert rfm["segment"].notna().all()

def test_summary_columns():
    rfm = assign_segments(make_rfm())
    summary = segment_summary(rfm)
    assert "customers" in summary.columns
    assert "total_revenue" in summary.columns
