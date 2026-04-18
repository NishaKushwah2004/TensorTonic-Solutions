def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    # Step 1: Store sum and count
    sums = {}
    counts = {}
    
    for cat, target in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + target
        counts[cat] = counts.get(cat, 0) + 1
    
    # Step 2: Compute means
    means = {}
    for cat in sums:
        means[cat] = sums[cat] / counts[cat]
    
    # Step 3: Build result
    return [means[cat] for cat in categories]