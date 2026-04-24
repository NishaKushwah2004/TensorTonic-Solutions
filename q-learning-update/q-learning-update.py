import numpy as np

def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    """
    Returns: updated Q-table Q_new
    """
    # Write code here
    Q_new = [row[:] for row in Q]
    
    # Compute target using ORIGINAL Q
    max_next = max(Q[s_next])
    td_target = r + gamma * max_next
    
    # Compute update
    Q_new[s][a] = Q[s][a] + alpha * (td_target - Q[s][a])
    
    return Q_new