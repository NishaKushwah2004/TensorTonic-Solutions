import numpy as np

def td_value_update(V, s, r, s_next, alpha, gamma):
    """
    Returns: updated value function V_new
    """
    # Write code here
    V_new = V.copy()   # avoid modifying input
    
    # Compute TD error
    delta = r + gamma * V[s_next] - V[s]
    
    # Update value of current state
    V_new[s] = V[s] + alpha * delta
    
    return V_new