def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    n = len(series)
    
    # Step 1: Compute mean
    mean = sum(series) / n
    
    # Step 2: Compute total variance (gamma_0)
    gamma0 = sum((x - mean) ** 2 for x in series)
    
    # Edge case: constant series
    if gamma0 == 0:
        return [1.0] + [0.0] * max_lag
    
    # Step 3: Compute autocorrelation for each lag
    result = []
    
    for k in range(max_lag + 1):
        numerator = 0.0
        for t in range(n - k):
            numerator += (series[t] - mean) * (series[t + k] - mean)
        
        result.append(numerator / gamma0)
    
    return result