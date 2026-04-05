def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here
    sum_map = {}
    count_map = {}
    
    # Step 1: compute sums and counts
    for cat, target in zip(categories, targets):
        sum_map[cat] = sum_map.get(cat, 0) + target
        count_map[cat] = count_map.get(cat, 0) + 1
    
    # Step 2: compute means
    mean_map = {cat: sum_map[cat] / count_map[cat] for cat in sum_map}
    
    # Step 3: replace categories with mean
    return [float(mean_map[cat]) for cat in categories]