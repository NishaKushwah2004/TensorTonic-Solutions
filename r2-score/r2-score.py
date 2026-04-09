import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    # Handle constant case
    if np.all(y_true == y_true[0]):
        return 1.0 if np.all(y_true == y_pred) else 0.0

    # Compute mean
    y_mean = np.mean(y_true)

    # SSE and SST
    sse = np.sum((y_true - y_pred) ** 2)
    sst = np.sum((y_true - y_mean) ** 2)

    return float(1 - (sse / sst))