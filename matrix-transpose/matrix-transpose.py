import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    n = len(A)
    m = len(A[0])
    transpose =[]
    for j in range(m) :
        temp = []
        for i in range(n) :
            temp.append(A[i][j])
            
        transpose.append(temp)

    return np.array(transpose)
    
    pass
