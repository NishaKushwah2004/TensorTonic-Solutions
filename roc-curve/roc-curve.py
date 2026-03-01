import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)

    desc_idx = np.argsort(-y_score)
    y_score = y_score[desc_idx]
    y_true = y_true[desc_idx]

    P = np.sum(y_true == 1)
    N = np.sum(y_true == 0)

    tp_cum = np.cumsum(y_true == 1)
    fp_cum = np.cumsum(y_true == 0)

    distinct_indices = np.where(np.diff(y_score))[0]
    threshold_idxs = np.r_[distinct_indices, len(y_score) - 1]

    tpr = tp_cum[threshold_idxs] / P if P > 0 else np.zeros_like(threshold_idxs, dtype=float)
    fpr = fp_cum[threshold_idxs] / N if N > 0 else np.zeros_like(threshold_idxs, dtype=float)

    thresholds = y_score[threshold_idxs]
    
    tpr = np.r_[0.0, tpr]
    fpr = np.r_[0.0, fpr]
    thresholds = np.r_[np.inf, thresholds]

    return fpr.tolist(), tpr.tolist(), thresholds.tolist()
    pass