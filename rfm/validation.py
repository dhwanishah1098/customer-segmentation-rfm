def validate_rfm_inputs(df, required_cols=("customer_id", "order_date", "revenue")):
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if df.empty:
        raise ValueError("Input DataFrame is empty")
    if (df["revenue"] < 0).any():
        raise ValueError("Negative revenue values detected")
    return True
