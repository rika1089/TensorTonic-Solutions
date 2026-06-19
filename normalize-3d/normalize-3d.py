import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.array(v, dtype=float)
    if v.ndim == 1 :
        norms = np.linalg.norm(v)
        return v / (norms+1e-12)
    
    else :
        norms = np.linalg.norm(v,axis = 1,keepdims = True)
        return v / (norms + 1e-12)
    pass