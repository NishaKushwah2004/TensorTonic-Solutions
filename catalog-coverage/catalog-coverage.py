def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    # Write code here
    # Return 0 if catalog is empty
    if n_items == 0:
        return 0.0

    unique_items = set()

    # Collect all unique recommended items
    for rec_list in recommendations:
        unique_items.update(rec_list)

    # Coverage formula
    return len(unique_items) / n_items