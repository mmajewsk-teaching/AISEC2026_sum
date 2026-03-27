
def create_fixed_size_chunks(text, chunk_size=1000, overlap=0):
    if not text:
        return []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    chunks = []
    total_len = len(text)
    num_chunks = (total_len + chunk_size - 1) // chunk_size

    for idx in range(num_chunks):
        start = idx * chunk_size
        if idx == 0 or overlap <= 0:
            chunk = text[start : start + chunk_size]
        else:
            chunk = text[start - overlap : start + chunk_size]
        chunks.append(chunk)

    return chunks
