import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.array(A,dtype = float)
    if abs(np.linalg.det(A)) < 1e-10 :
        return None
    Ainv = np.linalg.inv(A)
    return (Ainv)
    pass
