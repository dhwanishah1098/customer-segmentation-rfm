def compare_segments(df_prev, df_curr, id_col='customer_id', seg_col='segment'):
    merged = df_prev[[id_col, seg_col]].merge(df_curr[[id_col, seg_col]], on=id_col, suffixes=('_prev','_curr'))
    return merged[merged['segment_prev'] != merged['segment_curr']]
