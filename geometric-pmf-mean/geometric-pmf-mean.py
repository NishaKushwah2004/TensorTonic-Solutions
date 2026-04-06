import numpy as np

def geometric_pmf_mean(k, p):
    """
    Compute Geometric PMF and Mean.
    """
    # Write code here
    # Convert k to numpy array
    k = np.array(k)
    
    # Compute PMF using vectorized operation
    pmf = (1 - p) ** (k - 1) * p
    
    # Compute mean
    mean = 1 / p
    
    return pmf, float(mean)