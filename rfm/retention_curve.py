def retention_by_cohort(orders_df):
    orders_df['cohort'] = orders_df.groupby('customer_id')['order_date'].transform('min').dt.to_period('M')
    orders_df['period'] = orders_df['order_date'].dt.to_period('M')
    orders_df['months_since'] = (orders_df['period'] - orders_df['cohort']).apply(lambda x: x.n)
    return orders_df.groupby(['cohort','months_since'])['customer_id'].nunique().reset_index(name='customers')
