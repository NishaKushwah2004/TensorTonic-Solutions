import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)

    mean = float(np.mean(x))
    median = float(np.median(x))

    freq = Counter(x)
    max_freq = max(freq.values())

    mode = float(min([k for k, v in freq.items() if v == max_freq]))

    return (mean, median, mode)
    