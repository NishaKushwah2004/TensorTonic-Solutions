import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v, dtype=float)
    
    norms = np.linalg.norm(v, axis=-1, keepdims=True)
    
    safe_norms = np.where(norms > 1e-10, norms, 1.0)
    
    normalized = v / safe_norms
   
    normalized = np.where(norms > 1e-10, normalized, 0.0)
    
    return normalized