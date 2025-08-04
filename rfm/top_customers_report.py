def top_customers(rfm_df, n=20):
    return (rfm_df.sort_values('monetary', ascending=False)
            .head(n)[['customer_id','segment','monetary','frequency','recency']]
            .reset_index(drop=True))
