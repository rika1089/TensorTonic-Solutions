import math

def perplexity(prob_distributions, actual_tokens):
    """
    Compute perplexity given probability distributions and actual tokens.
    
    Args:
        prob_distributions: list of lists, each a probability distribution over vocab
        actual_tokens: list of ints, indices of the actual tokens
    Returns:
        float, perplexity
    """
    N = len(actual_tokens)
    log_probs = []
    for dist, token in zip(prob_distributions, actual_tokens):
        p = dist[token]
        log_probs.append(math.log(p))
    
    cross_entropy = -sum(log_probs) / N
    return math.exp(cross_entropy)
