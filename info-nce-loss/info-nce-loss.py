import numpy as np

def info_nce_loss(Z1, Z2, temperature=0.1):
    """
    Compute InfoNCE Loss for contrastive learning.
    """
    # Write code here
    Z1 = np.array(Z1)
    Z2 = np.array(Z2)
    
    # Step 1: similarity matrix
    S = np.dot(Z1, Z2.T) / temperature
    
    # Step 2: numerical stability
    S_max = np.max(S, axis=1, keepdims=True)
    S_stable = S - S_max
    
    # Step 3: exponentiate
    exp_S = np.exp(S_stable)
    
    # Step 4: denominator
    denom = np.sum(exp_S, axis=1)
    
    # Step 5: numerator (diagonal)
    numerator = np.diag(exp_S)
    
    # Step 6: loss
    loss = -np.log(numerator / denom)
    
    return np.mean(loss)