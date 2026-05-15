def baseline_predict(ratings_matrix, target_pairs):
    """
    Compute baseline predictions using global mean and user/item biases.
    """

    rows = len(ratings_matrix)
    cols = len(ratings_matrix[0])

    # Global mean
    total = 0
    count = 0

    for row in ratings_matrix:
        for val in row:
            if val != 0:
                total += val
                count += 1

    mu = total / count

    # User biases
    user_bias = [0.0] * rows

    for i in range(rows):
        s = 0
        c = 0

        for j in range(cols):
            if ratings_matrix[i][j] != 0:
                s += ratings_matrix[i][j]
                c += 1

        if c > 0:
            user_bias[i] = (s / c) - mu

    # Item biases
    item_bias = [0.0] * cols

    for j in range(cols):
        s = 0
        c = 0

        for i in range(rows):
            if ratings_matrix[i][j] != 0:
                s += ratings_matrix[i][j]
                c += 1

        if c > 0:
            item_bias[j] = (s / c) - mu

    # Predictions
    result = []

    for u, i in target_pairs:
        pred = mu + user_bias[u] + item_bias[i]
        result.append(pred)

    return result