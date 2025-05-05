def flag_churn_risk(rfm_df, recency_threshold=90, min_orders=2):
    at_risk = rfm_df[
        (rfm_df['recency'] > recency_threshold) &
        (rfm_df['frequency'] >= min_orders)
    ].copy()
    at_risk['churn_risk'] = 'high'
    return at_risk
