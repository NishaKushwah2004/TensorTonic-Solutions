def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    # Write code here
    n = len(series)
    
    # Initialize
    level = series[0]
    trend = series[1] - series[0]
    
    result = [float(level)]
    
    # Iterate over time series
    for t in range(1, n):
        prev_level = level
        
        # Update level
        level = alpha * series[t] + (1 - alpha) * (level + trend)
        
        # Update trend
        trend = beta * (level - prev_level) + (1 - beta) * trend
        
        result.append(float(level))
    
    return result