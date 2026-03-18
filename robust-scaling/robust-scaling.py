def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code 
    n = len(values)

    if n==1:
        return [0.0]

    values_sorted = sorted(values)

    def get_median(arr):
        m = len(arr)
        if m%2==1:
            return arr[m//2]
        else:
            return (arr[m // 2 - 1] + arr[m//2]) / 2.0

    median = get_median(values_sorted)

    if n%2 == 1:
        lower_half = values_sorted[:n//2]
        upper_half = values_sorted[n//2+1:]
    else:
        lower_half = values_sorted[:n//2]
        upper_half = values_sorted[n//2:]

    Q1 = get_median(lower_half)
    Q3 = get_median(upper_half)

    IQR = Q3 - Q1

    scaled = []
    for x in values:
        if IQR == 0:
            scaled.append(float(x - median))
        else:
            scaled.append((x-median) / IQR)

    return scaled
    
        