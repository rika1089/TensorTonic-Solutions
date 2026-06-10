import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix for X and return a numpy.ndarray.
    Return None for invalid input.
    """
    # Basic type and rectangular check
    if not isinstance(X, (list, tuple, np.ndarray)):
        return None

    try:
        A = np.array(X, dtype=float)   # will raise for ragged rows
    except Exception:
        return None

    # Must be 2D and have at least 2 observations (rows)
    if A.ndim != 2 or A.shape[0] < 2:
        return None

    cov = np.cov(A, rowvar=False)

    # If np.cov returns a 0-D ndarray (shape ()), wrap into 1x1 ndarray
    if np.ndim(cov) == 0:
        return np.array([[float(cov)]])

    # Ensure result is a numpy ndarray of floats
    return np.asarray(cov, dtype=float)
