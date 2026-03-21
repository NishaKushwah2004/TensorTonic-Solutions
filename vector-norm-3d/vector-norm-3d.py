import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    # Your code here
    try:
        v = np.asarray(v, dtype=float)
        
        if v.ndim == 1:
            if v.shape[0] != 3:
                return None
            return float(np.sqrt(np.sum(v ** 2)))
        
        elif v.ndim == 2:
            if v.shape[1] != 3:
                return None
            return np.sqrt(np.sum(v ** 2, axis=1))
        
        else:
            return None
    
    except:
        return None