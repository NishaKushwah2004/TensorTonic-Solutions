import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    
    N = len(X)
    
    # Create indices
    indices = np.arange(N)
    
    # Shuffle indices
    if rng is not None:
        rng.shuffle(indices)
    else:
        np.random.shuffle(indices)
    
    # Generate batches
    for start in range(0, N, batch_size):
        end = start + batch_size
        
        # Handle drop_last
        if drop_last and end > N:
            break
        
        batch_idx = indices[start:end]
        
        yield X[batch_idx], y[batch_idx]