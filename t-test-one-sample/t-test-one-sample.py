import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    x = np.array(x, dtype=float)
    n = len(x)
    mean_x = np.mean(x)
    s = np.std(x, ddof=1)  # sample standard deviation

    t_stat = (mean_x - mu0) / (s / np.sqrt(n))
    return float(t_stat)
