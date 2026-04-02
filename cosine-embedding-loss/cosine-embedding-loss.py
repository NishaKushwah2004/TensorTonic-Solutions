def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    # Write code here
    # Dot product
    dot = sum(a * b for a, b in zip(x1, x2))
    
    # Norms
    norm1 = math.sqrt(sum(a * a for a in x1))
    norm2 = math.sqrt(sum(b * b for b in x2))
    
    # Cosine similarity
    cos_sim = dot / (norm1 * norm2)
    
    # Loss computation
    if label == 1:
        return float(1 - cos_sim)
    elif label == -1:
        return float(max(0, cos_sim - margin))
    else:
        raise ValueError("label must be +1 or -1")