def item_cf_predict(user_ratings, item_similarities, target):
    """
    Predict the rating using item-based collaborative filtering.
    """

    weighted_sum = 0.0
    similarity_sum = 0.0

    for i in range(len(user_ratings)):

        # Skip target item
        if i == target:
            continue

        # Use only rated items with positive similarity
        if user_ratings[i] != 0 and item_similarities[i] > 0:
            weighted_sum += item_similarities[i] * user_ratings[i]
            similarity_sum += item_similarities[i]

    # No valid contributing items
    if similarity_sum == 0:
        return 0.0

    return weighted_sum / similarity_sum