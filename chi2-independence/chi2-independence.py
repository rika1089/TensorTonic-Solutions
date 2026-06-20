import numpy as np

def chi2_independence(C):
    """
    Compute chi-square test statistic and expected frequencies.
    C: 2D contingency table (numpy array or list of lists).
    Returns: (chi2_stat, expected)
    """
    C = np.array(C, dtype=float)
    total = np.sum(C)

    # Row and column sums
    row_sums = np.sum(C, axis=1, keepdims=True)
    col_sums = np.sum(C, axis=0, keepdims=True)

    # Expected frequencies under independence
    expected = row_sums @ col_sums / total

    # Chi-square statistic
    chi2_stat = np.sum((C - expected) ** 2 / (expected + 1e-12))

    return chi2_stat, expected
