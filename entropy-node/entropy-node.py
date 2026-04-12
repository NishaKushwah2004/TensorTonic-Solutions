import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0
    
    # Get counts of each class
    _, counts = np.unique(y, return_counts=True)
    
    # Convert to probabilities
    probs = counts / counts.sum()
    
    # Remove zero probabilities (safe guard)
    probs = probs[probs > 0]
    
    # Compute entropy
    entropy = -np.sum(probs * np.log2(probs))
    
    return float(entropy)