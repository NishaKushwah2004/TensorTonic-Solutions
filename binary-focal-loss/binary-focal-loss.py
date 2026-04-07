def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    """
    # Write code here
    n = len(predictions)
    total_loss = 0.0
    
    for p, y in zip(predictions, targets):
        if y == 1:
            pt = p
        else:
            pt = 1 - p
        
        loss = -alpha * ((1 - pt) ** gamma) * math.log(pt)
        
        total_loss += loss
    
    return total_loss / n