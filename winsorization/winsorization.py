def winsorize(values, lower_pct, upper_pct):
    """
    Clip values at the given percentile bounds.
    """
    # Write code here
    n = len(values)
    arr = sorted(values)
    
    # Helper to compute percentile with interpolation
    def percentile(p):
        k = (n - 1) * p / 100
        f = int(k)
        c = min(f + 1, n - 1)
        return arr[f] + (k - f) * (arr[c] - arr[f])
    
    lower = percentile(lower_pct)
    upper = percentile(upper_pct)
    
    # Clip values while preserving original order
    result = []
    for x in values:
        result.append(max(lower, min(upper, x)))
    
    return result