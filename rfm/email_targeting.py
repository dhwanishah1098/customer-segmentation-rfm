import pandas as pd

TEMPLATES = {
    "Champions":          "Thanks for being amazing! Here's an exclusive early access offer.",
    "Loyal Customers":    "You're one of our best — enjoy this members-only discount.",
    "Potential Loyalists":"We think you'll love what's new — check out our latest collection.",
    "New Customers":      "Welcome! Here's everything you need to get started.",
    "At Risk":            "We miss you — here's 15% off to come back.",
    "Cant Lose Them":     "Urgent: your exclusive renewal offer expires in 48 hours.",
    "Hibernating":        "It's been a while — here's what you've been missing.",
    "Lost":               "We'd love to have you back — one last offer, just for you.",
}

def assign_email_template(rfm: pd.DataFrame) -> pd.DataFrame:
    df = rfm.copy()
    df["email_subject"] = df["segment"].map(TEMPLATES).fillna("Here's something we think you'll love.")
    return df[["customer_id","segment","email_subject"]]
