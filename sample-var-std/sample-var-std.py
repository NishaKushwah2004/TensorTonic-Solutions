import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x, dtype=float)
    n = len(x)

    mean_x = np.mean(x)

    sample_variance = np.sum((x - mean_x) ** 2) / (n - 1)
    standard_variance = np.sqrt(sample_variance)

    return (float(sample_variance), float(standard_variance))
    