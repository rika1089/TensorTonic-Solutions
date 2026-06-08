# import numpy as np

# def euclidean_distance(x):
#     """
#     Compute the Euclidean (L2) distance between vectors x and y.
#     Must return a float.
#     """
#     # Write code here
#     n = len(x)
#     euclidean_distance = 0
#     for i in range(n) :
#         euclidean_distance += (x[i]) ** 2

#     return euclidean_distance ** 0.5
    
#     pass

# def cosine_similarity(a, b):
#     """
#     Compute cosine similarity between two 1D NumPy arrays.
#     Returns: float in [-1, 1]
#     """
#     # Write code here
#     if euclidean_distance(a)==0 or euclidean_distance(b) == 0 :
#         return 0.0 
        
#     if len(a) != len(b) :
#         raise ValueError("Length of two vectors must be same")
#     n = len(a)
#     cosine = 0
#     for i in range(n) :
#         cosine += a[i] * b[i]

#     return cosine / (euclidean_distance(a) * euclidean_distance(b))
    
    
#     pass

import numpy as np

def euclidean(x,y) :
    x = np.array(x)
    y = np.array(y)

    if x.shape != y.shape :
        raise ValueError

    return float(np.linalg.norm(x-y))

def cosine_similarity(a,b) :
    a = np.array(a)
    b = np.array(b)

    if a.shape != b.shape :
        raise ValueError

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0 :
        return 0.0

    return float(np.dot(a,b) / (norm_a * norm_b))