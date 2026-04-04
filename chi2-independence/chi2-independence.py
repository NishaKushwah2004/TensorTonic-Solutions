import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    """
    # Write code here
    # Convert to NumPy array
    C = np.array(C, dtype=float)
    
    # Row sums, column sums, total
    row_sum = np.sum(C, axis=1)
    col_sum = np.sum(C, axis=0)
    total = np.sum(C)
    
    # Expected frequencies using outer product
    expected = np.outer(row_sum, col_sum) / total
    
    # Chi-square statistic
    chi2 = np.sum((C - expected) ** 2 / expected)
    
    return chi2, expected