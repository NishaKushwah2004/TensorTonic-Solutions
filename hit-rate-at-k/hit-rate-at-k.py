def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    # Write code here
    n = len(recommendations)
    
    if n == 0:
        return 0.0
    
    hits = 0
    
    for recs, truth in zip(recommendations, ground_truth):
        
        # Take only top-K recommendations
        top_k = set(recs[:k])
        
        # Relevant items
        relevant = set(truth)
        
        # Check if intersection is non-empty
        if top_k & relevant:
            hits += 1
    
    return hits / n