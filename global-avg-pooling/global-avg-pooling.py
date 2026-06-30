import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    arr = np.asarray(x, dtype=float)  # do not modify input, ensure float dtype

    if arr.ndim == 3:
        # (C, H, W) -> mean over H and W -> (C,)
        C, H, W = arr.shape
        if H < 1 or W < 1:
            raise ValueError("H and W must be >= 1")
        return arr.mean(axis=(1, 2))
    elif arr.ndim == 4:
        # (N, C, H, W) -> mean over H and W -> (N, C)
        N, C, H, W = arr.shape
        if H < 1 or W < 1:
            raise ValueError("H and W must be >= 1")
        return arr.mean(axis=(2, 3))
    else:
        raise ValueError("Input must have shape (C,H,W) or (N,C,H,W)")
