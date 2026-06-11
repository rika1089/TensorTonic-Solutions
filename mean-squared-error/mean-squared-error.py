import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    n = len(y_pred)
    y_pred = np.array(y_pred)
    y_true = np.array(y_true)

    mse_sum  = np.sum((y_pred - y_true) ** 2)
    mse = mse_sum / n
    return float(mse)
    pass
