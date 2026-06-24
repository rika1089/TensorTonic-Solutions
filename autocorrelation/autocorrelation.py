import numpy as np

def autocorrelation(series, max_lag):
    """
    Compute autocorrelation for lags 0..max_lag using population normalization (divide by n).
    Returns a Python list of floats.
    """
    series = np.array(series, dtype=float)
    n = len(series)
    mean = series.mean()
    var = series.var()  # population variance (divide by n)

    if var == 0:
        # constant series: autocorrelation is 1 at lag 0, 0 elsewhere
        return [1.0] + [0.0] * max_lag

    acf = []
    for lag in range(max_lag + 1):
        if lag == 0:
            acf.append(1.0)
        else:
            cov = np.sum((series[:-lag] - mean) * (series[lag:] - mean)) / n
            acf.append(float(cov / var))
    return acf
    
    # Write code here