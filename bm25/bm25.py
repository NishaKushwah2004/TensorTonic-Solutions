import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    """
    Returns numpy array of BM25 scores for each document.
    """
    # Write code here
    if not docs:
        return np.array([])
    
    N = len(docs)
    
    doc_lengths = np.array([len(doc) for doc in docs])
    avgdl = np.mean(doc_lengths) if N > 0 else 0
    
    if avgdl == 0:
        return np.zeros(N)

    df = Counter()
    for doc in docs:
        unique_terms = set(doc)
        for term in unique_terms:
            df[term] += 1
    
    idf = {}
    for term, freq in df.items():
        idf[term] = math.log((N - freq + 0.5) / (freq + 0.5) + 1)

    query_terms = list(dict.fromkeys(query_tokens))
    
    # Step 4: Compute BM25 scores
    scores = np.zeros(N)
    
    for i, doc in enumerate(docs):
        tf = Counter(doc)
        doc_len = len(doc)
        
        for term in query_terms:
            if term not in idf:
                continue  # term not in corpus → idf = 0
            
            term_freq = tf.get(term, 0)
            if term_freq == 0:
                continue
            
            numerator = term_freq * (k1 + 1)
            denominator = term_freq + k1 * (1 - b + b * (doc_len / avgdl))
            
            scores[i] += idf[term] * (numerator / denominator)
    
    return scores