def rating_normalization(matrix):
    """
    Mean-center each user's ratings in the user-item matrix.
    """
    # Write code here
    result = []
    
    for row in matrix:
        # Extract non-zero ratings
        rated = [x for x in row if x != 0]
        
        # If no ratings, keep row as all 0.0
        if not rated:
            result.append([0.0] * len(row))
            continue
        
        # Compute mean of non-zero ratings
        mean = sum(rated) / len(rated)
        
        # Normalize row
        normalized_row = [
            float(x - mean) if x != 0 else 0.0
            for x in row
        ]
        
        result.append(normalized_row)
    
    return result