def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    hist = [0] * 256
    
    # Traverse image
    for row in image:
        for pixel in row:
            hist[pixel] += 1
    
    return hist