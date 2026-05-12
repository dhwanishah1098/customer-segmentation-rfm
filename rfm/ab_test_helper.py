import pandas as pd
import numpy as np
from scipy import stats


def split_segment_for_ab_test(rfm: pd.DataFrame, segment: str, test_ratio: float = 0.5, seed: int = 42) -> tuple:
    seg_df = rfm[rfm["segment"] == segment].sample(frac=1, random_state=seed).reset_index(drop=True)
    split = int(len(seg_df) * test_ratio)
    return seg_df.iloc[:split], seg_df.iloc[split:]


def compare_ab_results(control: pd.Series, test: pd.Series) -> dict:
    t_stat, p_value = stats.ttest_ind(control, test)
    return {
        "control_mean": control.mean().round(2),
        "test_mean": test.mean().round(2),
        "lift_pct": round((test.mean() - control.mean()) / control.mean() * 100, 2),
        "p_value": round(p_value, 4),
        "significant": p_value < 0.05,
    }
