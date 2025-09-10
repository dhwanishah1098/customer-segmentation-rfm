def generate_winback_list(rfm_df, min_ltv=500, max_recency=365):
    candidates = rfm_df[
        (rfm_df['monetary'] >= min_ltv) &
        (rfm_df['recency'] <= max_recency) &
        (rfm_df['segment'].isin(['at_risk','hibernating','lost']))
    ].copy()
    candidates['priority'] = candidates['monetary'].rank(ascending=False)
    return candidates.sort_values('priority')
