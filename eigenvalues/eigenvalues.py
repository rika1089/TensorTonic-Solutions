import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    try:
        A = np.array(matrix)

        # Check if matrix is square
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None   # gracefully return None

        return np.linalg.eigvals(A)

    except Exception as e:
        return None 
    
    pass