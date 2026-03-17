import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    state = {
        'min': np.full(D, np.inf),     # +infinity
        'max': np.full(D, -np.inf)     # -infinity
    }
    return state


def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    X_batch = np.array(X_batch)

    # Step 1: Compute batch min and max (per feature)
    batch_min = np.min(X_batch, axis=0)
    batch_max = np.max(X_batch, axis=0)

    # Step 2: Update global running min and max
    state['min'] = np.minimum(state['min'], batch_min)
    state['max'] = np.maximum(state['max'], batch_max)

    # Step 3: Compute denominator safely (avoid division by zero)
    denom = state['max'] - state['min']
    denom = np.maximum(denom, eps)

    # Step 4: Normalize batch using updated global min/max
    X_norm = (X_batch - state['min']) / denom

    return X_norm