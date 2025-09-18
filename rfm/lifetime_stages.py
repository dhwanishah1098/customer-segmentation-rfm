import pandas as pd

def assign_lifecycle_stage(rfm: pd.DataFrame) -> pd.DataFrame:
    df = rfm.copy()
    def stage(row):
        if row["frequency"] == 1 and row["recency"] <= 30: return "New"
        if row["frequency"] >= 5 and row["recency"] <= 60: return "Established"
        if row["frequency"] >= 10: return "Veteran"
        if row["recency"] > 180: return "Lapsed"
        return "Developing"
    df["lifecycle_stage"] = df.apply(stage, axis=1)
    return df
