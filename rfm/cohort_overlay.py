def add_acquisition_cohort(rfm_df, orders_df):
    first_order = orders_df.groupby('customer_id')['order_date'].min().rename('cohort_month')
    first_order = first_order.dt.to_period('M')
    return rfm_df.merge(first_order, on='customer_id', how='left')
