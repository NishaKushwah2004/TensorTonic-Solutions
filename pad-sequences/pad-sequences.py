import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if not seqs:
        return np.empty((0, 0), dtype=int)

    # ✅ Determine max length
    if max_len is None:
        max_len = max(len(seq) for seq in seqs) if seqs else 0

    N = len(seqs)
    L = max_len

    # ✅ Initialize with pad_value
    result = np.full((N, L), pad_value, dtype=int)

    # ✅ Fill sequences
    for i, seq in enumerate(seqs):
        trunc = seq[:L]  # truncate if needed
        result[i, :len(trunc)] = trunc

    return result