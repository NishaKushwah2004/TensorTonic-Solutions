def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    freq = {}
    
    for sentence in sentences:
        for word in sentence:
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
                
    return freq