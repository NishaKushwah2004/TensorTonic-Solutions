import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    """
    Returns: (boot_means, lower, upper)
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    
    # Choose RNG
    if rng is None:
        rng = np.random.default_rng()
    
    # Generate bootstrap indices (vectorized)
    indices = rng.integers(0, n, size=(n_bootstrap, n))
    
    # Create bootstrap samples
    samples = x[indices]
    
    # Compute means for each bootstrap sample
    boot_means = np.mean(samples, axis=1)
    
    # Compute confidence interval
    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1 - alpha)
    
    return boot_means, float(lower), float(upper)
