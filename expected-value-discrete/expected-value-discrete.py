import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.array(x, dtype=float)
    p = np.array(p, dtype=float)

    if x.shape != p.shape:
        raise ValueError("x and p must have same shape")

    if not np.allclose(np.sum(p), 1.0, atol=1e-6):
        raise ValueError("Probabilities must sum to 1")

    expected = np.sum(x*p)

    return float(expected)
