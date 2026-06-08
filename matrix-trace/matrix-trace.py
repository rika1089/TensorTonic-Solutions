import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    n = len(A)
    trace = 0
    for i in range (n) :
        trace += A[i][i]

    return trace
    
    pass
