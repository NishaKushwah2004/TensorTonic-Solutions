import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    n = len(y_true)
    ece = 0.0

    # Step 1: assign bins
    bin_indices = np.floor(y_pred * n_bins).astype(int)
    
    # Handle edge case: p = 1.0 → last bin
    bin_indices = np.minimum(bin_indices, n_bins - 1)

    # Step 2: process each bin
    for b in range(n_bins):
        mask = (bin_indices == b)
        count = np.sum(mask)

        if count == 0:
            continue  # skip empty bins

        # accuracy = mean of true labels
        acc = np.mean(y_true[mask])

        # confidence = mean predicted prob
        conf = np.mean(y_pred[mask])

        # weighted contribution
        ece += (count / n) * abs(acc - conf)

    return float(ece)