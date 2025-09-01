import pandas as pd

def channel_preference(df: pd.DataFrame) -> pd.DataFrame:
    return (df.groupby(["customer_id","channel"])["order_id"].count()
            .reset_index(name="orders")
            .sort_values(["customer_id","orders"], ascending=[True,False])
            .drop_duplicates("customer_id", keep="first")
            .rename(columns={"channel":"preferred_channel"}))
