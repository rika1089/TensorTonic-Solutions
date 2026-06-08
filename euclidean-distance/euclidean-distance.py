import numpy as np
import math

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    if len(x) != len(y) :
        raise ValueError('Vectors must be of samelength')
    n = len(x or y)
    euclidean_distance = 0
    for i in range(n) :
        euclidean_distance += pow((x[i]-y[i]),2)

    return math.sqrt(euclidean_distance)
    
    pass