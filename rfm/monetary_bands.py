MONETARY_BANDS = [(0,100,'low'),(100,500,'medium'),(500,2000,'high'),(2000,None,'vip')]
def classify_monetary(val):
    for lo,hi,label in MONETARY_BANDS:
        if hi is None or lo <= val < hi: return label
    return 'unknown'
