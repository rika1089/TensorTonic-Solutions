def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    n = len(values)
    
    # create bins for the values and store -1 since no element has assigned bins
    bins = [-1]*(n)
    
    max_val = max(values)
    min_val = min(values)

    # Handling case where all the elements are same

    if max_val == min_val :
        return [0]*n # All get assigned to bin 0(same)
        
    w = (max_val - min_val) / num_bins

    for i in range(n) :
        bins[i] = min( ((values[i] - min_val) // w) , num_bins-1)

    return bins
    