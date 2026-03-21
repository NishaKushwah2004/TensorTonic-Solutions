import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    try:
        A = np.array(A, dtype=float)
        
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None
        
        n = A.shape[0]
  
        det = np.linalg.det(A)
        
        if abs(det) < 1e-10:
            return None
        
        A_inv = np.linalg.inv(A)
        
        I = np.eye(n)
        if np.linalg.norm(A @ A_inv - I) >= 1e-7:
            return None
        
        return A_inv
    
    except:
        return None

