import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    
    # If 1D → treat as single feature
    if X.ndim == 1:
        min_val = np.min(X)
        max_val = np.max(X)
        denom = max(max_val - min_val, eps)
        return (X - min_val) / denom
    
    # 2D case
    min_vals = np.min(X, axis=axis, keepdims=True)
    max_vals = np.max(X, axis=axis, keepdims=True)
    
    # Avoid division by zero
    denom = np.maximum(max_vals - min_vals, eps)
    
    scaled = (X - min_vals) / denom
    
    return scaled