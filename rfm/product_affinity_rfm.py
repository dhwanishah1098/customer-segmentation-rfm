def affinity_by_segment(orders_df, rfm_df):
    merged = orders_df.merge(rfm_df[['customer_id','segment']], on='customer_id')
    return merged.groupby(['segment','product_id'])['order_id'].count().reset_index(name='purchase_count')
