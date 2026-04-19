def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    n = len(values)
  
    arr = [(val, idx) for idx, val in enumerate(values)]
    
  
    arr.sort()
    
    ranks = [0.0] * n
    i = 0
    
   
    while i < n:
        j = i
        
  
        while j < n and arr[j][0] == arr[i][0]:
            j += 1
        
        avg_rank = (i + 1 + j) / 2.0
        

        for k in range(i, j):
            ranks[arr[k][1]] = avg_rank
        
        i = j
    
    return ranks