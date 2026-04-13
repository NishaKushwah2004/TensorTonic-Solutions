import numpy as np
from collections import Counter
def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    # Write code here
    rater1 = np.array(rater1)
    rater2 = np.array(rater2)

    n = len(rater1)

    # Step 1: observed agreement
    p_o = np.sum(rater1 == rater2) / n

    # Step 2: label frequencies
    count1 = Counter(rater1)
    count2 = Counter(rater2)

    # Step 3: get all unique labels
    labels = set(count1.keys()).union(set(count2.keys()))

    # Step 4: expected agreement
    p_e = 0.0
    for k in labels:
        p1 = count1[k] / n
        p2 = count2[k] / n
        p_e += p1 * p2

    # Step 5: handle edge case
    if p_e == 1.0:
        return 1.0

    # Step 6: compute kappa
    kappa = (p_o - p_e) / (1 - p_e)

    return float(kappa)