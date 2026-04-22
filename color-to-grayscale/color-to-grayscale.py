def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    H = len(image)
    W = len(image[0])
    
    grayscale = []
    
    for i in range(H):
        row = []
        for j in range(W):
            R, G, B = image[i][j]
            Y = 0.299 * R + 0.587 * G + 0.114 * B
            row.append(Y)
        grayscale.append(row)
    
    return grayscale