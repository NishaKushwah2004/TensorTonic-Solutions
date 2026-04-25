def simple_moving_average(values, window_size):
    """
    Compute the simple moving average of the given values.
    """
    # Write code here
    n = len(values)
    
    # Step 1: initial window sum
    window_sum = sum(values[:window_size])
    
    result = [window_sum / window_size]
    
    # Step 2: slide the window
    for i in range(window_size, n):
        window_sum += values[i]          # add new element
        window_sum -= values[i - window_size]  # remove old element
        
        result.append(window_sum / window_size)
    
    return result