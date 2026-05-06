def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here
    unrated = [(scores[i], i) for i in range(len(scores))
               if i not in rated_indices]
    
    # Sort by score in descending order
    unrated.sort(key=lambda x: -x[0])
    
    # Return indices of top-k items
    return [index for score, index in unrated[:k]]