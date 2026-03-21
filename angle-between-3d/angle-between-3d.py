import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    try:
        v = np.asarray(v, dtype=float)
        w = np.asarray(w, dtype=float)
        
        if v.shape != (3,) or w.shape != (3,):
            return np.nan
     
        norm_v = np.linalg.norm(v)
        norm_w = np.linalg.norm(w)
     
        if norm_v < 1e-10 or norm_w < 1e-10:
            return np.nan
        
        dot = np.dot(v, w)
        
        cos_theta = dot / (norm_v * norm_w)
        
        cos_theta = np.clip(cos_theta, -1.0, 1.0)
        
        theta = np.arccos(cos_theta)
        
        return float(theta)
    
    except:
        return np.nan
