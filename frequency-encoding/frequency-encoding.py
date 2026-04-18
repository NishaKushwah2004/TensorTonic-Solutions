def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    # Write code here
    n = len(values)
    
    # Step 1: Count frequencies
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    
    # Step 2: Convert to proportions
    for key in freq:
        freq[key] = freq[key] / n
    
    # Step 3: Build result
    return [freq[v] for v in values]