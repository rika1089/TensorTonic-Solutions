import numpy as np

def robust_scaling(values):
    """
    Scale values using median and interquartile range computed
    by taking medians of the lower/upper halves (exclusive median).
    Returns a list of floats.
    """
    arr = np.array(values, dtype=float)
    if arr.size == 0:
        return []

    median = np.median(arr)

    # split into lower and upper halves excluding the median
    sorted_arr = np.sort(arr)
    n = len(sorted_arr)
    if n % 2 == 0:
        lower = sorted_arr[:n//2]
        upper = sorted_arr[n//2:]
    else:
        lower = sorted_arr[:n//2]      # excludes median
        upper = sorted_arr[n//2 + 1:]  # excludes median

    q1 = np.median(lower) if lower.size > 0 else median
    q3 = np.median(upper) if upper.size > 0 else median
    iqr = q3 - q1

    if iqr == 0:
        return [0.0] * n

    scaled = (arr - median) / iqr
    return scaled.tolist()
