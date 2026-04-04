import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    # Convert to NumPy arrays
    x = np.array(x, dtype=float)
    q = np.array(q, dtype=float)
    
    # Sort data
    x = np.sort(x)
    
    # Compute percentiles
    result = np.percentile(x, q, method='linear')
    
    return result