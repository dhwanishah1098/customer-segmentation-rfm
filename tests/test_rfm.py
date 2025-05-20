import pandas as pd
import pytest
from rfm.calculator import calculate_rfm, score_rfm
from datetime import datetime

@pytest.fixture
def txns():
    return pd.DataFrame({
        "customer_id": ["A","A","B","C","C","C"],
        "order_id": ["O1","O2","O3","O4","O5","O6"],
        "order_date": pd.to_datetime(["2024-01-01","2024-03-01","2024-06-01",
                                      "2024-01-15","2024-02-15","2024-03-15"]),
        "revenue": [100,200,50,80,90,110],
    })

def test_rfm_shape(txns):
    snapshot = datetime(2024, 7, 1)
    rfm = calculate_rfm(txns, snapshot)
    assert len(rfm) == 3
    assert "recency" in rfm.columns

def test_rfm_scores(txns):
    rfm = score_rfm(calculate_rfm(txns, datetime(2024,7,1)), quantiles=3)
    assert "R_score" in rfm.columns
    assert "RFM_score" in rfm.columns
