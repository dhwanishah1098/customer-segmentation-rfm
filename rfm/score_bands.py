def assign_score_band(score, bands=5):
    thresholds = [i * (100 // bands) for i in range(1, bands)]
    for i, t in enumerate(thresholds, 1):
        if score <= t: return i
    return bands
