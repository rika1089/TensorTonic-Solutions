import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    n = len(x)
    dist = 0
    for i in range(n) :
        dist += abs(x[i] - y[i])

    return float(dist)
    pass
