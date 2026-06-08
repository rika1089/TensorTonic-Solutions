import numpy as np

def euclidean_distance(x):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    n = len(x)
    euclidean_distance = 0
    for i in range(n) :
        euclidean_distance += (x[i]) ** 2

    return euclidean_distance ** 0.5
    
    pass

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    if euclidean_distance(a)==0 or euclidean_distance(b) == 0 :
        return 0.0 
        
    if len(a) != len(b) :
        raise ValueError("Length of two vectors must be same")
    n = len(a)
    cosine = 0
    for i in range(n) :
        cosine += a[i] * b[i]

    return cosine / (euclidean_distance(a) * euclidean_distance(b))
    
    
    pass