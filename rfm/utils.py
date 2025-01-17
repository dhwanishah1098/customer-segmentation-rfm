
def high_value_customers(rfm, threshold=1000):
    return rfm[rfm["monetary"] >= threshold]

def low_frequency_customers(rfm, max_f=2):
    return rfm[rfm["frequency"] <= max_f]

def at_risk_count(rfm):
    return (rfm["segment"] == "At Risk").sum()
