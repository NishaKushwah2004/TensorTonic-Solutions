import numpy as np

def poisson_pmf_cdf(lam, k):
    """
    Compute Poisson PMF and CDF.
    """
    # Write code here
    # Function to compute log factorial
    def log_factorial(n):
        if n == 0 or n == 1:
            return 0.0
        return np.sum(np.log(np.arange(1, n + 1)))
    
    # ---- PMF ----
    log_pmf = -lam + k * np.log(lam) - log_factorial(k)
    pmf = np.exp(log_pmf)
    
    # ---- CDF ----
    cdf = 0.0
    for i in range(k + 1):
        log_p = -lam + i * np.log(lam) - log_factorial(i)
        cdf += np.exp(log_p)
    
    return float(pmf), float(cdf)