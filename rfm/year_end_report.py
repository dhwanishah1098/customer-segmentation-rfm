def year_end_rfm_report(rfm_df) -> dict:
    return {
        'total_customers': len(rfm_df),
        'segment_breakdown': rfm_df['segment'].value_counts().to_dict(),
        'avg_monetary': round(rfm_df['monetary'].mean(), 2),
        'top_segment_revenue': rfm_df.groupby('segment')['monetary'].sum().idxmax(),
        'high_risk_count': (rfm_df['segment'].isin(['at_risk','lost'])).sum(),
    }
