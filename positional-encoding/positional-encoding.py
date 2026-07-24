import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len)[:, np.newaxis]

    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(base) / d_model))

    angles = pos * div_term

    pe = np.zeros((seq_len, d_model), dtype = float)

    pe[:, 0::2] = np.sin(angles)

    pe[:, 1::2] = np.cos(angles[:, :d_model//2])

    return pe