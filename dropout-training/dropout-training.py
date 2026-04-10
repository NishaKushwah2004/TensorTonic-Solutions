import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x, dtype=float)

    if p == 0.0:
        return x.copy(), np.ones_like(x)

    keep_prob = 1 - p

    # Random generator
    rand = rng.random(x.shape) if rng else np.random.random(x.shape)
    
    # Mask
    mask = (rand < keep_prob).astype(float) / keep_prob
    
    output = x * mask
    
    return output, mask