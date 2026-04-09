import math

def log_loss(y_true, y_pred, eps=1e-15):
    """
    Compute per-sample log loss.
    """
    # Write code here
    losses = []

    for y, p in zip(y_true, y_pred):
        # Clip probability
        p = min(max(p, eps), 1 - eps)

        # Compute log loss
        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        losses.append(loss)

    return losses