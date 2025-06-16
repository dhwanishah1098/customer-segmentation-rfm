def rfm_by_region(rfm_df):
    return rfm_df.groupby(['region','segment']).agg(
        customers=('customer_id','count'),
        avg_monetary=('monetary','mean'),
        total_revenue=('monetary','sum')
    ).reset_index()
