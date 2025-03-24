import pandas as pd

def clean_transactions(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df[df["revenue"] > 0].dropna(subset=["customer_id","order_date"])
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["revenue"] = df["revenue"].astype(float)
    return df.drop_duplicates(subset=["order_id"])

def aggregate_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("customer_id").agg(
        total_revenue=("revenue","sum"),
        order_count=("order_id","nunique"),
        first_order=("order_date","min"),
        last_order=("order_date","max"),
    ).reset_index()
