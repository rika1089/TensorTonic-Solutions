import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Convert to numpy arrays
    y_left = np.array(y_left)
    y_right = np.array(y_right)

    N_left = len(y_left)
    N_right = len(y_right)
    N = N_left + N_right

    # Handle empty split
    if N == 0:
        return 0.0

    def gini(y):
        if len(y) == 0:
            return 0.0
        # class counts
        _, counts = np.unique(y, return_counts=True)
        probs = counts / len(y)
        return 1.0 - np.sum(probs ** 2)

    g_left = gini(y_left)
    g_right = gini(y_right)

    # Weighted average
    return (N_left / N) * g_left + (N_right / N) * g_right
