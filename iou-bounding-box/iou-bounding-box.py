def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    # Write code here
    x1_a, y1_a, x2_a, y2_a = box_a
    x1_b, y1_b, x2_b, y2_b = box_b

    # Step 1: Intersection coordinates
    x_left = max(x1_a, x1_b)
    y_top = max(y1_a, y1_b)
    x_right = min(x2_a, x2_b)
    y_bottom = min(y2_a, y2_b)

    # Step 2: Compute intersection area
    inter_width = max(0, x_right - x_left)
    inter_height = max(0, y_bottom - y_top)
    intersection = inter_width * inter_height

    # Step 3: Compute areas
    area_a = (x2_a - x1_a) * (y2_a - y1_a)
    area_b = (x2_b - x1_b) * (y2_b - y1_b)

    # Step 4: Compute union
    union = area_a + area_b - intersection

    # Step 5: Handle edge case
    if union == 0:
        return 0.0

    return intersection / union