import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    # Normal equation
    Xt = X.T
    w = np.linalg.inv(Xt @ X) @ Xt @ y

    return w