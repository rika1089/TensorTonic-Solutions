import numpy as np
def xavier_initialization(W, fan_in, fan_out):
    """
    Scale raw weights to Xavier uniform initialization.
    """
    # Write code here
    L = (6 / (fan_in + fan_out))**0.5

    w = np.array(W , dtype = float)

    w = w*(2*L)
    w = w - L
    return w