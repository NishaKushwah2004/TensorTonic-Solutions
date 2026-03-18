import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    result = []
    for v in values:
        result.append(math.log(1+v))
    return result