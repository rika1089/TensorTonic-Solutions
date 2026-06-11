import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    e_X = np.exp(-x)
    dr = 1+e_X
    sigmoid = 1 / dr

    return np.array(sigmoid)
    
    pass