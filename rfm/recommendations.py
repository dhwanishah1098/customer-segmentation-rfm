import pandas as pd


RECOMMENDATIONS = {
    "Champions": "Reward them. Ask for reviews. Upsell premium products.",
    "Loyal Customers": "Offer loyalty programs. Ask for referrals.",
    "Potential Loyalists": "Offer membership or loyalty programs.",
    "New Customers": "Provide onboarding support. Early success programs.",
    "At Risk": "Send personalised reactivation emails. Offer discounts.",
    "Cant Lose Them": "Win them back with renewal offers. Urgent outreach.",
    "Hibernating": "Offer relevant products with discounts.",
    "Lost": "Revive interest with a comeback campaign or ignore.",
}


def add_recommendations(segment_df: pd.DataFrame) -> pd.DataFrame:
    df = segment_df.copy()
    df["recommendation"] = df["segment"].map(RECOMMENDATIONS).fillna("Monitor and nurture.")
    return df
