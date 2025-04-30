
def high_value_customers(rfm, threshold=1000):
    return rfm[rfm["monetary"] >= threshold]

def low_frequency_customers(rfm, max_f=2):
    return rfm[rfm["frequency"] <= max_f]

def at_risk_count(rfm):
    return (rfm["segment"] == "At Risk").sum()

def champions_revenue(rfm):
    return rfm[rfm["segment"] == "Champions"]["monetary"].sum().round(2)

def rfm_stats(rfm):
    return rfm[["recency","frequency","monetary"]].describe().round(2)

def segment_counts(rfm):
    return rfm["segment"].value_counts().to_dict()

def high_clv_customers(rfm, n=100):
    return rfm.nlargest(n, "clv") if "clv" in rfm.columns else rfm

def lost_revenue(rfm):
    return rfm[rfm["segment"] == "Lost"]["monetary"].sum().round(2)

def avg_recency_by_segment(rfm):
    return rfm.groupby("segment")["recency"].mean().round(1)

def winback_list(rfm, min_monetary=200):
    return rfm[(rfm["recency"] > 60) & (rfm["monetary"] >= min_monetary)][["customer_id","monetary","recency"]]

def rfm_score_distribution(rfm):
    return rfm["RFM_total"].value_counts().sort_index()

def top_segments_by_revenue(rfm):
    return rfm.groupby("segment")["monetary"].sum().sort_values(ascending=False)

def customer_age_days(rfm):
    return rfm["recency"].describe().round(1)

def hibernating_customers(rfm):
    return rfm[rfm["segment"] == "Hibernating"][["customer_id","recency","monetary"]]
