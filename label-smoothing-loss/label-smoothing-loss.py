def label_smoothing_loss(predictions, target, epsilon):
    """
    Compute cross-entropy loss with label smoothing.
    """
    # Write code here
    K = len(predictions)
    loss = 0.0
    
    for i in range(K):
        if i == target:
            q_i = (1 - epsilon) + (epsilon / K)
        else:
            q_i = epsilon / K
        
        p_i = max(min(predictions[i], 1 - 1e-15), 1e-15)
        
        loss += q_i * math.log(p_i)
    
    return -loss