def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    max_lag = max(lags)
    result = []
    
    for t in range(max_lag, len(series)):
        row = []
        for lag in lags:
            row.append(series[t - lag])
        result.append(row)
    
    return result