def rolling_std(values, window_size):
    """
    Compute the rolling population standard deviation.
    """
    # Write code here
    n = len(values)
    result = []

    window_sum = 0
    window_sq_sum = 0

    # Step 1: initialize first window
    for i in range(window_size):
        window_sum += values[i]
        window_sq_sum += values[i] * values[i]

    # Step 2: process windows
    for i in range(n - window_size + 1):
        mean = window_sum / window_size
        variance = (window_sq_sum / window_size) - (mean * mean)
        std_dev = math.sqrt(variance)

        result.append(std_dev)

        # Slide window
        if i + window_size < n:
            outgoing = values[i]
            incoming = values[i + window_size]

            window_sum += incoming - outgoing
            window_sq_sum += incoming * incoming - outgoing * outgoing

    return result