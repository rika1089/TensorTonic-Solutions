def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.array(X,dtype = float)
    y = np.array(y,dtype = float)

    n_samples,n_features = X.shape
    I = np.eye(n_features)

    A = X.T @ X + lam * I

    w = np.linalg.inv(A) @ X.T @ y

    return w.tolist()