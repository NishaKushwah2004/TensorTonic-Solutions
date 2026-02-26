import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len, dtype=float).reshape(-1, 1)
    
    i = np.arange(0, d_model, 2, dtype=float)
    
    div_term = np.power(base, i / d_model)
    
    angles = pos / div_term
    
    pe = np.zeros((seq_len, d_model), dtype=float)
    
    pe[:, 0::2] = np.sin(angles)
    
    if d_model > 1:
        pe[:, 1::2] = np.cos(angles[:, :pe[:, 1::2].shape[1]])
    
    return pe

    pass