import numpy as np

def color_to_grayscale(image):
    """
    Convert an RGB image (H, W, 3) to grayscale and return a list of lists.
    """
    arr = np.array(image, dtype=float)
    if arr.ndim != 3 or arr.shape[-1] != 3:
        raise ValueError("image must have shape (H, W, 3)")
    gray = 0.299 * arr[..., 0] + 0.587 * arr[..., 1] + 0.114 * arr[..., 2]
    return gray.tolist()
