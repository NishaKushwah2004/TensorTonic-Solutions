import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Write code here
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    
    # Add epsilon to avoid log(0)
    q_stable = q + eps
    
    # Mask where p > 0 (to avoid log(0) issues)
    mask = p > 0
    
    # Compute KL divergence
    kl = np.sum(p[mask] * np.log(p[mask] / q_stable[mask]))
    
    return kl