import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    try:
        mat = np.array(matrix, dtype=float)
        
        if mat.ndim != 2:
            return None
        
        if norm_type == 'l1':
            norm = np.sum(np.abs(mat), axis=axis, keepdims=True)
        
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(mat ** 2, axis=axis, keepdims=True))
        
        elif norm_type == 'max':
            norm = np.max(np.abs(mat), axis=axis, keepdims=True)
        
        else:
            return None  
        
        norm[norm == 0] = 1
        
        normalized_matrix = mat / norm
        
        return normalized_matrix
    
    except:
        return None
