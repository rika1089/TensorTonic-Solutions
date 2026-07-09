import numpy as np

def streaming_minmax_init(D):
    """
    Initialize state dict with min, max arrays of shape (D,).
    """
    # Write code here
    state = {
        "min" : np.full(D,np.inf,dtype=float),
        "max" : np.full(D,-np.inf,dtype=float)
    }
    return state

def streaming_minmax_update(state, X_batch, eps=1e-8):
    """
    Update state's min/max with X_batch, return normalized batch.
    """
    # Write code here
    X_batch = np.array(X_batch,dtype = float)

    batch_min = X_batch.min(axis=0)
    batch_max = X_batch.max(axis=0)

    state['min'] = np.minimum(state["min"],batch_min)
    state['max'] = np.maximum(state["max"],batch_max)

    dr = state['max'] - state['min']
    dr = np.maximum(dr,eps)
    normalised = (X_batch - state["min"]) / dr

    return normalised.tolist()
    pass