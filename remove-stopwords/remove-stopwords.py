def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    ans = []
    for t in tokens :
        if t not in stopwords :
            ans.append(t)

    return ans
    pass