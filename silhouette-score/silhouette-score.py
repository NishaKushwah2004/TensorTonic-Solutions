import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    n = X.shape[0]
    
    # Step 1: Pairwise Euclidean distance matrix
    diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    D = np.sqrt(np.sum(diff**2, axis=2))  # shape (n, n)
    
    unique_labels = np.unique(labels)
    
    a = np.zeros(n)
    b = np.full(n, np.inf)
    
    for label in unique_labels:
        mask = (labels == label)
        not_mask = ~mask
        
        # Intra-cluster distance a(i)
        if np.sum(mask) > 1:
            a[mask] = np.sum(D[mask][:, mask], axis=1) / (np.sum(mask) - 1)
        else:
            a[mask] = 0
        
        # Inter-cluster distance b(i)
        for other_label in unique_labels:
            if other_label == label:
                continue
            other_mask = (labels == other_label)
            
            dist = np.mean(D[mask][:, other_mask], axis=1)
            b[mask] = np.minimum(b[mask], dist)
    
    # Step 3: Silhouette score
    s = (b - a) / np.maximum(a, b)
    
    return np.mean(s)