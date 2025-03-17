FREQUENCY_BANDS = [
    (1, 1, 'one_time'),
    (2, 3, 'occasional'),
    (4, 9, 'regular'),
    (10, None, 'frequent'),
]
def classify_frequency(n):
    for lo, hi, label in FREQUENCY_BANDS:
        if hi is None or lo <= n <= hi:
            return label
    return 'unknown'
