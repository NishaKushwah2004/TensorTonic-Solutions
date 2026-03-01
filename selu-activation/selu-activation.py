import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    return [
        round(float(lam * v), 4) if v > 0 
        else round(float(lam * alpha * (math.exp(v) - 1)), 4)
        for v in x
    ]
    pass
