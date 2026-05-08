def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    # Convert lists to sets to remove duplicates
    a = set(set_a)
    b = set(set_b)
    
    # Compute union
    union = a | b
    
    # If both sets are empty
    if len(union) == 0:
        return 0.0
    
    # Compute intersection
    intersection = a & b
    
    # Jaccard similarity
    return len(intersection) / len(union)