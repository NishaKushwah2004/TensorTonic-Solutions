def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    result = []
    
    for i in range(1, len(series)):
        prev = series[i - 1]
        curr = series[i]
        
        if prev == 0:
            result.append(0.0)
        else:
            change = (curr - prev) / prev
            result.append(change)
    
    return result