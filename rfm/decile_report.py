def decile_report(rfm_df):
    rfm_df['decile'] = (rfm_df['rfm_score'] // 10).clip(1, 10)
    return rfm_df.groupby('decile')[['monetary']].agg(['mean','sum','count'])
