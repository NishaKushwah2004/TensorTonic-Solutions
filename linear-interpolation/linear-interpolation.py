def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    # Write code here
    result = values[:]  # copy list
    n = len(values)
    
    i = 0
    while i < n:
        if result[i] is None:
            left = i - 1
            
            # find right boundary
            right = i
            while result[right] is None:
                right += 1
            
            left_val = result[left]
            right_val = result[right]
            
            # fill values between left and right
            for j in range(left + 1, right):
                result[j] = left_val + (j - left) / (right - left) * (right_val - left_val)
            
            i = right  # skip processed block
        else:
            i += 1
    
    return result