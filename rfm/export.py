import pandas as pd

def export_rfm_to_excel(rfm_df, path: str):
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        rfm_df.to_excel(writer, sheet_name="RFM Scores", index=False)
        rfm_df.groupby("segment")["monetary"].agg(["count", "mean", "sum"])               .to_excel(writer, sheet_name="Segment Summary")
    print(f"Exported to {path}")
