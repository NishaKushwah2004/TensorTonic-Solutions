import math
from collections import Counter

def get_ngrams(tokens, n):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def bleu_score(candidate, reference, max_n):
    """
    Compute the BLEU score for a candidate translation.
    """
    
    c_len = len(candidate)
    r_len = len(reference)
    
    # Edge case
    if c_len == 0:
        return 0.0
    
    precisions = []
    
    for n in range(1, max_n + 1):
        cand_ngrams = Counter(get_ngrams(candidate, n))
        ref_ngrams = Counter(get_ngrams(reference, n))
        
        if len(cand_ngrams) == 0:
            return 0.0
        
        clipped_count = 0
        total_count = sum(cand_ngrams.values())
        
        for ng in cand_ngrams:
            clipped_count += min(cand_ngrams[ng], ref_ngrams.get(ng, 0))
        
        p_n = clipped_count / total_count
        
        if p_n == 0:
            return 0.0
        
        precisions.append(p_n)
    
    # Brevity Penalty
    if c_len >= r_len:
        BP = 1.0
    else:
        BP = math.exp(1 - r_len / c_len)
    
    # Geometric mean
    log_sum = sum(math.log(p) for p in precisions)
    geo_mean = math.exp(log_sum / max_n)
    
    return float(BP * geo_mean)