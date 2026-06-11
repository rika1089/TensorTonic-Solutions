import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    auc = 0
    n = len(fpr)
    for i in range(n-1) :
        auc += ( tpr[i] + tpr[i+1] ) * (fpr[i+1] - fpr[i])
    return float(auc/2)
    pass