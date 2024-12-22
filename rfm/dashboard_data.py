def build_segment_summary(rfm_df) -> list[dict]:
    """Prepare segment summary for dashboard rendering."""
    grouped = rfm_df.groupby("segment").agg(
        customer_count=("customer_id", "count"),
        avg_monetary=("monetary", "mean"),
        total_revenue=("monetary", "sum"),
        avg_recency=("recency", "mean"),
    ).reset_index()
    grouped["revenue_share_pct"] = (
        grouped["total_revenue"] / grouped["total_revenue"].sum() * 100
    ).round(1)
    return grouped.to_dict(orient="records")
