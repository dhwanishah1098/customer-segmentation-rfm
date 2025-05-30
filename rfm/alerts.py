def generate_segment_alerts(current, previous):
    alerts = []
    for seg, curr_count in current.items():
        prev_count = previous.get(seg, 0)
        if prev_count and (curr_count - prev_count) / prev_count < -0.10:
            alerts.append({'segment': seg, 'change_pct': round((curr_count-prev_count)/prev_count*100,1)})
    return alerts
