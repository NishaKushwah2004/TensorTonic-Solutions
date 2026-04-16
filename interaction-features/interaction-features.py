def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    result = []
    
    for row in X:
        new_row = list(row)  # copy original features
        d = len(row)
        
        for i in range(d):
            for j in range(i + 1, d):
                new_row.append(row[i] * row[j])
        
        result.append(new_row)
    
    return result