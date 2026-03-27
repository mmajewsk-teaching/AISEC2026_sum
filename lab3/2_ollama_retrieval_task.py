import numpy as np
import ollama
import re

from utils import create_fixed_size_chunks


def get_embeddings(texts, model):
    if isinstance(texts, str):
        texts = [texts]
    embeddings = []
    for text in texts:
        response = ollama...(..., ...)
        embeddings.append(...["embedding"])
    return np.array(...)


cosine_similarity = lambda ...


def retrieve_chunks(query_embedding, chunk_embeddings, chunks, top_k=3):
    ...


if __name__ == "__main__":
    script_path = "shrek.txt"
    with open(..., "r", encoding="utf-8") as file:
        script_text = ....read()

    script_text = re.sub(" +", " ", script_text)
    chunks = ...(script_text, overlap=50)

    print("Generating embeddings for chunks...")
    embeddings_model = "nomic_local"
    chat_model = "llama_local"
    chunk_embeddings = ...(..., model=...)
    print(f"Generated {len(chunk_embeddings)} embeddings")

    while True:
        text = input(">>:")
        if text == "\\q":
            print("bye")
            break

        query_embedding = ...([text], model=...)[0]
        top_k = ...(...,...,..., top_k=3)

        context = "\n\n".join([chunk for _, _, chunk in top_k])

        prompt = "Context:\n"+..."\n\nQuestion: "+...+"\n\nAnswer based on the context:"

        response = ollama....(...=chat_model, messages=[{"role": "user", "content": ...}])
        print(f"\n{response['message']['content']}\n")
