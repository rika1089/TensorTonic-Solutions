import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    # Count frequencies
    counts = Counter(x)

    # Get the most common element
    mode_value, mode_freq = counts.most_common(1)[0]
    x = np.array(x)
    mean = np.mean(x)
    median = np.median(x)
    return tuple([float(mean),float(median),float(mode_value)])
    
    pass