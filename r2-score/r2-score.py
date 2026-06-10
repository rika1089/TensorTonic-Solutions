import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Returns a Python float.

    - y_true and y_pred must be 1D sequences of equal length.
    - Vectorized (no Python loops).
    - If all y_true are equal: return 1.0 if predictions match exactly, else 0.0.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    # Validate inputs
    if y_true.ndim != 1 or y_pred.ndim != 1 or y_true.shape[0] != y_pred.shape[0]:
        raise ValueError("y_true and y_pred must be 1D arrays of the same length")

    # Constant-target edge case
    if np.all(y_true == y_true[0]):
        return 1.0 if np.array_equal(y_pred, y_true) else 0.0

    # Sum of squares
    y_mean = np.mean(y_true)
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - y_mean) ** 2)

    # Compute R^2 and return as Python float
    r2 = 1.0 - (ss_res / ss_tot)
    return float(r2)
