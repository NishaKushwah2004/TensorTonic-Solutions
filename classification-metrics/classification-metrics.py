import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have same length")
    
    n = len(y_true)
    
    # Accuracy
    accuracy = np.sum(y_true == y_pred) / n
    
    # Unique classes
    classes = np.unique(np.concatenate([y_true, y_pred]))
    k = len(classes)
    
    # Map labels → index
    class_to_idx = {c: i for i, c in enumerate(classes)}
    
    # Confusion matrix
    cm = np.zeros((k, k), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[class_to_idx[t], class_to_idx[p]] += 1
    
    # Per-class TP, FP, FN
    TP = np.diag(cm)
    FP = np.sum(cm, axis=0) - TP
    FN = np.sum(cm, axis=1) - TP
    support = np.sum(cm, axis=1)
    
    # Safe division
    def safe_div(a, b):
        return np.divide(a, b, out=np.zeros_like(a, dtype=float), where=b!=0)
    
    precision_c = safe_div(TP, TP + FP)
    recall_c    = safe_div(TP, TP + FN)
    f1_c        = safe_div(2 * precision_c * recall_c, precision_c + recall_c)
    
    # Averaging
    if average == "micro":
        TP_sum = np.sum(TP)
        FP_sum = np.sum(FP)
        FN_sum = np.sum(FN)
        
        precision = TP_sum / (TP_sum + FP_sum) if (TP_sum + FP_sum) else 0.0
        recall    = TP_sum / (TP_sum + FN_sum) if (TP_sum + FN_sum) else 0.0
        f1        = (2 * precision * recall / (precision + recall)
                     if (precision + recall) else 0.0)
    
    elif average == "macro":
        precision = np.mean(precision_c)
        recall    = np.mean(recall_c)
        f1        = np.mean(f1_c)
    
    elif average == "weighted":
        weights = support / np.sum(support)
        precision = np.sum(precision_c * weights)
        recall    = np.sum(recall_c * weights)
        f1        = np.sum(f1_c * weights)
    
    elif average == "binary":
        if pos_label not in class_to_idx:
            return {"accuracy": accuracy, "precision": 0.0, "recall": 0.0, "f1": 0.0}
        
        i = class_to_idx[pos_label]
        tp, fp, fn = TP[i], FP[i], FN[i]
        
        precision = tp / (tp + fp) if (tp + fp) else 0.0
        recall    = tp / (tp + fn) if (tp + fn) else 0.0
        f1        = (2 * precision * recall / (precision + recall)
                     if (precision + recall) else 0.0)
    
    else:
        raise ValueError("Invalid average type")
    
    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1": float(f1)
    }