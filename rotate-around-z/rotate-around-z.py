import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    # Your code here
    pts = np.asarray(points, dtype=float)
    
    is_single = (pts.ndim == 1)
    if is_single:
        pts = pts.reshape(1, 3)
   
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    
    x = pts[:, 0]
    y = pts[:, 1]
    z = pts[:, 2]
    
    x_new = x * cos_t - y * sin_t
    y_new = x * sin_t + y * cos_t
    z_new = z  # unchanged
    
    rotated = np.stack([x_new, y_new, z_new], axis=1)
    
    if is_single:
        return rotated[0]
    return rotated