import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        A = np.asarray(matrix, dtype=float)
        
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None
        
        if A.size == 0:
            return None
        
        eigenvalues = np.linalg.eigvals(A)
        
        idx = np.lexsort((eigenvalues.imag, eigenvalues.real))
        eigenvalues = eigenvalues[idx]
        
        return eigenvalues
    
    except:
        return None
