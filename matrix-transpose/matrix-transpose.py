import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)

    if A.ndim != 2 :
        raise ValueError("Input must be a 2D matrix")

    N,M = A.shape

    result = np.empty((M,N), dtype = float)

    for i in range(N):
        for j in range(M):
            result[j,i] = A[i,j]

    return result
    pass
