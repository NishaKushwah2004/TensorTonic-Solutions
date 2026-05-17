def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    
    result = []
    
    for req in requests:
        user_id = req["user_id"]
        online_features = req["online_features"]
        
        # Get offline features or defaults
        offline_features = feature_store.get(user_id, defaults)
        
        # Merge offline + online features
        combined = {**offline_features, **online_features}
        
        result.append(combined)
    
    return result