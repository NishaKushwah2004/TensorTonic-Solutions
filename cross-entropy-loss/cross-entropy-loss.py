import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    if y_pred.shape[0] != y_true.shape[0]:
        return None
    
    N = y_true.shape[0]
    
    correct_probs = y_pred[np.arange(N), y_true]
    
    loss = -np.mean(np.log(correct_probs))
    
    return float(loss)
