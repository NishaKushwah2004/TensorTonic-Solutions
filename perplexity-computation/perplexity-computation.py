def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code 
    N = len(actual_tokens)
    
    log_sum = 0.0
    
    for i in range(N):
        p = prob_distributions[i][actual_tokens[i]]
        log_sum += math.log(p)
    
    cross_entropy = -log_sum / N
    
    return float(math.exp(cross_entropy))