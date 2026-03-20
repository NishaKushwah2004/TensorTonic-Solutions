def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """
    # Write code 
    if not data or not data[0]:
        return []

    n_rows = len(data)
    n_cols = len(data[0])
    
    result = [[0.0] * n_cols for _ in range(n_rows)]
    
    # Process each column independently
    for j in range(n_cols):
        # Extract column
        col = [data[i][j] for i in range(n_rows)]
        
        min_val = min(col)
        max_val = max(col)
        range_val = max_val - min_val
        
        if range_val == 0:
            continue  
        
        for i in range(n_rows):
            result[i][j] = (data[i][j] - min_val) / range_val
    
    return result