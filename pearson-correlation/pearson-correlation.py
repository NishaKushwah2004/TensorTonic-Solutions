import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    # Write code here
    try:
        X = np.array(X, dtype=float)
        
        if X.ndim != 2 or X.shape[0] < 2:
            return None
        
        N, D = X.shape
        
        mean = np.mean(X, axis=0, keepdims=True)
        X_centered = X - mean
        
        cov = (X_centered.T @ X_centered) / (N - 1)
        
        std = np.sqrt(np.diag(cov)) 
        
        std_outer = np.outer(std, std) 
        
        corr = cov / std_outer
        
        corr[std_outer == 0] = np.nan
        
        for i in range(D):
            if std[i] != 0:
                corr[i, i] = 1.0
            else:
                corr[i, i] = np.nan
        
        return corr
    
    except:
        return None
