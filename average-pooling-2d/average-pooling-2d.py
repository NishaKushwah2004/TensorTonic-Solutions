def average_pooling_2d(X, pool_size):
    """
    Apply 2D average pooling with non-overlapping windows.
    """
    # Write code here
    H = len(X)
    W = len(X[0])
    
    out_h = H // pool_size
    out_w = W // pool_size
    
    result = []
    
    for i in range(out_h):
        row = []
        for j in range(out_w):
            total = 0
            
            # Traverse pooling window
            for a in range(pool_size):
                for b in range(pool_size):
                    total += X[i * pool_size + a][j * pool_size + b]
            
            avg = total / (pool_size * pool_size)
            row.append(avg)
        
        result.append(row)
    
    return result