def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    # Write code here
    # Initialize EMA with first value
    ema = [float(values[0])]
    
    # Compute EMA for remaining values
    for i in range(1, len(values)):
        new_ema = alpha * values[i] + (1 - alpha) * ema[-1]
        ema.append(float(new_ema))
    
    return ema