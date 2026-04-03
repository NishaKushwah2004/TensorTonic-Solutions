import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    # Convert to float arrays
    p = np.asarray(p, dtype=float)
    y = np.asarray(y, dtype=float)
    
    # Flatten to handle 1D or 2D uniformly
    p = p.flatten()
    y = y.flatten()
    
    # Compute intersection
    intersection = np.sum(p * y)
    
    # Compute sums
    sum_p = np.sum(p)
    sum_y = np.sum(y)
    
    # Dice coefficient
    dice = (2 * intersection + eps) / (sum_p + sum_y + eps)
    
    # Dice loss
    return float(1 - dice)