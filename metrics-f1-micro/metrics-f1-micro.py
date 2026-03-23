def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    n = len(y_true)
    
    tp = 0
    for i in range(n):
        if y_true[i] == y_pred[i]:
            tp += 1
    
    return tp / n