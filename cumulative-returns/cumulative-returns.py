def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    # Write code here
    result = []
    wealth = 1.0
    
    for r in returns:
        wealth *= (1 + r)
        result.append(wealth - 1)
    
    return result