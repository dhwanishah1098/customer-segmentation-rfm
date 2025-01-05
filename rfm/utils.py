
def high_value_customers(rfm, threshold=1000):
    return rfm[rfm["monetary"] >= threshold]
