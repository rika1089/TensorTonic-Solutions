def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    Includes a short final chunk only if it is the first (only) chunk.
    """
    chunks = []
    n = len(tokens)
    if chunk_size <= 0:
        return chunks

    i = 0
    step = chunk_size - overlap
    if step <= 0:
        raise ValueError("chunk_size must be greater than overlap")

    while i < n:
        chunk = tokens[i:i + chunk_size]
        # If chunk is shorter than requested and it's not the first chunk, stop
        if len(chunk) < chunk_size and i != 0:
            break
        chunks.append(chunk)
        i += step

    return chunks
