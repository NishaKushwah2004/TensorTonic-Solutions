import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    fpr = np.asarray(fpr)
    tpr = np.asarray(tpr)
    
   
    if fpr.shape != tpr.shape:
        raise ValueError("fpr and tpr must have the same shape")
    if len(fpr) < 2:
        raise ValueError("At least 2 points required")
    
    
    area = 0.0
    for i in range(len(fpr) - 1):
        width = fpr[i + 1] - fpr[i]
        height = (tpr[i] + tpr[i + 1]) / 2.0
        area += width * height
    
    return float(area)