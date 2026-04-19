def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    # Write code here
    n = len(ratings_matrix)
    m = len(ratings_matrix[0])
  
    result = [row[:] for row in ratings_matrix]
    
    if mode == "user":
        for i in range(n):
        
            vals = [ratings_matrix[i][j] for j in range(m) if ratings_matrix[i][j] != 0]
            
            if len(vals) == 0:
                continue 
            
            mean = sum(vals) / len(vals)
            
            for j in range(m):
                if result[i][j] == 0:
                    result[i][j] = mean

    elif mode == "item":
        for j in range(m):
            vals = [ratings_matrix[i][j] for i in range(n) if ratings_matrix[i][j] != 0]
            
            if len(vals) == 0:
                continue
            
            mean = sum(vals) / len(vals)
            
            for i in range(n):
                if result[i][j] == 0:
                    result[i][j] = mean

    return result