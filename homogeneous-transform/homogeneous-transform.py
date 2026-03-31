import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points = np.asarray(points)

    # Handle single point
    single = False
    if points.ndim == 1:
        points = points.reshape(1, 3)
        single = True

    # Step 1: Convert to homogeneous (append 1)
    ones = np.ones((points.shape[0], 1))
    points_h = np.hstack((points, ones))   # shape (N, 4)

    # Step 2: Apply transformation
    transformed = (T @ points_h.T).T       # shape (N, 4)

    # Step 3: Extract (x', y', z')
    result = transformed[:, :3]

    # Return correct shape
    return result[0] if single else result