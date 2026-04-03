import numpy as np

def contrastive_loss(a, b, y, margin=1.0, reduction="mean") -> float:
    """
    a, b: arrays of shape (N, D) or (D,)  (will broadcast to (N,D))
    y:    array of shape (N,) with values in {0,1}; 1=similar, 0=dissimilar
    margin: float > 0
    reduction: "mean" (default) or "sum"
    Return: float
    """
    # Write code here
    # Convert to numpy arrays
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    y = np.asarray(y, dtype=float)
    
    # Handle single vector case → reshape to (1, D)
    if a.ndim == 1:
        a = a.reshape(1, -1)
        b = b.reshape(1, -1)
    
    # Validate y
    if not np.all(np.isin(y, [0, 1])):
        raise ValueError("y must contain only 0 or 1")
    
    # Compute Euclidean distance
    d = np.linalg.norm(a - b, axis=1)
    
    # Loss computation
    loss = y * (d ** 2) + (1 - y) * (np.maximum(0, margin - d) ** 2)
    
    # Reduction
    if reduction == "mean":
        return float(np.mean(loss))
    elif reduction == "sum":
        return float(np.sum(loss))
    else:
        raise ValueError("reduction must be 'mean' or 'sum'")