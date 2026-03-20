import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
    X = np.asarray(X, dtype=float)

    if X.ndim != 2:
        return None
    
    N, D = X.shape
    
    if N < 2:
        return None

    mean = np.mean(X, axis=0)
    
    X_centered = X - mean
    
    cov = (X_centered.T @ X_centered) / (N - 1)
    
    return cov
