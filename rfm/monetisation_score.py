import pandas as pd

def monetisation_potential(rfm: pd.DataFrame) -> pd.DataFrame:
    df = rfm.copy()
    df["spend_velocity"] = (df["monetary"] / df["frequency"]).round(2)
    df["engagement_score"] = (
        (df["frequency"] / df["frequency"].max()) * 0.5 +
        (1 - df["recency"] / df["recency"].max()) * 0.5
    ).round(3)
    df["upsell_potential"] = (df["engagement_score"] * df["spend_velocity"]).round(2)
    return df
