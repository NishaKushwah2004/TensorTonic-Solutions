def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    # Write code here
    result = []
    
    for p in range(period):
        total = 0
        count = 0
        
        for i in range(p, len(series), period):
            total += series[i]
            count += 1
        
        result.append(total / count)
    
    return result