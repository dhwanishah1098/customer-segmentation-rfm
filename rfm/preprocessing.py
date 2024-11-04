import pandas as pd
from datetime import date

def preprocess_transactions(df: pd.DataFrame, snapshot_date=None) -> pd.DataFrame:
    """Clean and prepare transaction data for RFM scoring."""
    if snapshot_date is None:
        snapshot_date = date.today()
    df = df.dropna(subset=["customer_id", "order_date", "revenue"])
    df["order_date"] = pd.to_datetime(df["order_date"])
    df = df[df["revenue"] > 0]
    df["days_since"] = (pd.Timestamp(snapshot_date) - df["order_date"]).dt.days
    return df
