import pandas as pd

def rfm_by_region(df: pd.DataFrame, rfm: pd.DataFrame) -> pd.DataFrame:
    customer_region = df.groupby("customer_id")["region"].agg(lambda x: x.mode()[0]).reset_index()
    return rfm.merge(customer_region, on="customer_id", how="left")

def top_segments_by_region(rfm: pd.DataFrame) -> pd.DataFrame:
    return (rfm.groupby(["region","segment"])["customer_id"].count()
            .reset_index(name="customers")
            .sort_values(["region","customers"], ascending=[True, False]))
