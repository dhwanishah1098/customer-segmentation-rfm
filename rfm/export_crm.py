import csv
def export_for_crm(rfm_df, output_path: str, fields=('customer_id','segment','monetary','recency')):
    with open(output_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for _, row in rfm_df[list(fields)].iterrows():
            writer.writerow(row.to_dict())
    return output_path
