import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    # Compute pre-activation
    pre_act = x_t @ Wx + h_prev @ Wh + b
    
    # Apply tanh activation
    h_t = np.tanh(pre_act)
    
    return h_t
