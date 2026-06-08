import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    if n == 1 :
        return np.array([v])

    matrix = [[0] * n for _ in range(n)]

    for i in range(n) :
        matrix[i][i] = v[i]

    return np.array(matrix)
    pass
