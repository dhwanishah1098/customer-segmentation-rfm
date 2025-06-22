# Configurable RFM scoring thresholds
RFM_CONFIG = {
    "quantiles": 5,
    "weights": {"R": 0.3, "F": 0.3, "M": 0.4},
    "min_orders_for_loyal": 3,
    "at_risk_recency_days": 90,
    "lost_recency_days": 180,
}

def weighted_rfm_score(rfm_row, config=RFM_CONFIG) -> float:
    return (float(rfm_row["R_score"]) * config["weights"]["R"] +
            float(rfm_row["F_score"]) * config["weights"]["F"] +
            float(rfm_row["M_score"]) * config["weights"]["M"])
