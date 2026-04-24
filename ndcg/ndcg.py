import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    n = len(relevance_scores)
    k = min(k, n)
    
    # Function to compute DCG
    def compute_dcg(scores):
        dcg = 0.0
        for i in range(len(scores)):
            rel = scores[i]
            gain = (2 ** rel) - 1
            discount = math.log2(i + 2)  # i+1 position → log2(i+2)
            dcg += gain / discount
        return dcg
    
    # DCG for given ranking
    dcg = compute_dcg(relevance_scores[:k])
    
    # Ideal DCG (sorted in descending order)
    ideal_scores = sorted(relevance_scores, reverse=True)
    idcg = compute_dcg(ideal_scores[:k])
    
    # Handle edge case
    if idcg == 0:
        return 0.0
    
    return dcg / idcg