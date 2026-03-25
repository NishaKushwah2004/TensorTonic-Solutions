import numpy as np
from collections import Counter
import math

def tfidf_vectorizer(documents):
    """
    Build TF-IDF matrix from a list of text documents.
    Returns tuple of (tfidf_matrix, vocabulary).
    """
    # Write code here
    if not documents:
        return np.array([]), []

    tokenized_docs = [doc.lower().split() if doc else [] for doc in documents]
    
    vocab = sorted(set(word for doc in tokenized_docs for word in doc))
    vocab_size = len(vocab)
    n_docs = len(documents)
    
    if vocab_size == 0:
        return np.zeros((n_docs, 0)), []
    
    word_to_index = {word: idx for idx, word in enumerate(vocab)}
    
    df = Counter()
    for doc in tokenized_docs:
        unique_words = set(doc)
        for word in unique_words:
            df[word] += 1
    
    idf = {}
    for word in vocab:
        idf[word] = math.log(n_docs / df[word]) if df[word] > 0 else 0

    tfidf_matrix = np.zeros((n_docs, vocab_size))
    
    for doc_idx, doc in enumerate(tokenized_docs):
        if not doc:
            continue
        
        term_counts = Counter(doc)
        total_terms = len(doc)
        
        for word, count in term_counts.items():
            if word in word_to_index:
                tf = count / total_terms
                tfidf = tf * idf[word]
                tfidf_matrix[doc_idx][word_to_index[word]] = tfidf
    
    return tfidf_matrix, vocab