def bigram_probabilities(tokens):
    """
    Returns: (counts, probs)
      counts: dict mapping (w1, w2) -> integer count
      probs: dict mapping (w1, w2) -> float P(w2 | w1) with add-1 smoothing
    """
    # Your code here
    from collections import defaultdict

    # Step 1: Vocabulary
    V = set(tokens)
    V_size = len(V)

    # Step 2: Bigram counts
    counts = defaultdict(int)
    for i in range(len(tokens) - 1):
        counts[(tokens[i], tokens[i + 1])] += 1

    # Step 3: Count total outgoing for each w1
    total_out = defaultdict(int)
    for (w1, w2), c in counts.items():
        total_out[w1] += c

    # Step 4: Compute probabilities with add-1 smoothing
    probs = {}
    for w1 in V:
        denom = total_out[w1] + V_size
        for w2 in V:
            c = counts[(w1, w2)]  # 0 if not present
            probs[(w1, w2)] = (c + 1) / denom

    return dict(counts), probs