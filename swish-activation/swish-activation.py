import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    x_cliped = np.clip(x, -500, 500)
    sigmoid = 1/(1+ np.exp(-x_cliped))

    return x*sigmoid
    pass