import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Step 1: Convert to NumPy array and ensure float type
    X = np.array(X, dtype=float)

    # Step 2: Handle 1D case (convert to 2D for uniform processing)
    is_1d = False
    if X.ndim == 1:
        X = X.reshape(-1, 1)
        is_1d = True

    # Step 3: Create a copy (do not modify original data)
    X_imputed = X.copy()

    # Step 4: Iterate over each column
    for col in range(X.shape[1]):
        column = X[:, col]

        # Step 5: Identify valid (non-NaN) values
        valid_mask = ~np.isnan(column)

        # Step 6: Handle all-NaN column
        if not np.any(valid_mask):
            fill_value = 0.0
        else:
            # Step 7: Compute statistic (mean or median)
            if strategy == 'mean':
                fill_value = np.mean(column[valid_mask])
            elif strategy == 'median':
                fill_value = np.median(column[valid_mask])
            else:
                raise ValueError("strategy must be 'mean' or 'median'")

        # Step 8: Replace NaNs with computed value
        nan_mask = np.isnan(column)
        X_imputed[nan_mask, col] = fill_value

    # Step 9: Convert back to 1D if needed
    if is_1d:
        return X_imputed.flatten()

    return X_imputed