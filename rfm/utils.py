
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
