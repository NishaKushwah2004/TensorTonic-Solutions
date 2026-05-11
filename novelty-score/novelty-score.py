def novelty_score(recommendations, item_counts, n_users):
    """
    Compute the average novelty of a recommendation list.
    """
    # Write code here
    if not recommendations:
        return 0.0

    total = 0.0

    for item in recommendations:
        popularity = item_counts[item] / n_users
        total += -math.log2(popularity)

    return total / len(recommendations)