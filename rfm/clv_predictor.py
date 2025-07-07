def predict_clv(avg_order_value, purchase_frequency, customer_lifespan_years):
    return round(avg_order_value * purchase_frequency * customer_lifespan_years, 2)

def discount_clv(clv, discount_rate=0.10, years=3):
    return round(sum(clv / (1 + discount_rate)**t for t in range(1, years+1)), 2)
