import pandas as pd

def segment_migration(rfm_t1: pd.DataFrame, rfm_t2: pd.DataFrame) -> pd.DataFrame:
    merged = rfm_t1[["customer_id","segment"]].merge(
        rfm_t2[["customer_id","segment"]], on="customer_id", suffixes=("_prev","_curr")
    )
    return (merged.groupby(["segment_prev","segment_curr"])
            .size().reset_index(name="customers")
            .sort_values("customers", ascending=False))
