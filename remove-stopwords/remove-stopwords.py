def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    tks = []
    for token in tokens :
        if token not in stopwords :
            tks.append(token)

    return tks
    pass