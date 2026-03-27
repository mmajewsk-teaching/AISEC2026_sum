import torch
import numpy as np
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModel


import nltk
from nltk.tokenize import sent_tokenize
import re
from utils import create_fixed_size_chunks


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
cosine_similarity = lambda ...


def get_embeddings(texts, tokenizer, model):
    encoded_inputs = ...(
        ..., padding=True, truncation=True, return_tensors="pt"
    ).to(device)
    with torch.no_grad():
        outputs = ...(**encoded_inputs)
    token_embeddings = ....last_hidden_state
    embeddings = torch.mean(..., dim=1)
    return embeddings.cpu().numpy()


def retrieve_chunks(
    query_embedding, chunk_embeddings, chunks, top_k=3, similarity_fn=cosine_similarity
):
    similarities = []
    for i, chunk_embedding in enumerate(chunk_embeddings):
        similarity = ...(..., ...)
        similarities.append((i, similarity, chunks[i]))
    similarities.sort(key=..., reverse=...)
    return similarities[:top_k]

if __name__=="__main__":
    nltk.download("punkt_tab")

    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name).to(device)

    script_path = "shrek.txt"

    with open(script_path, "r", encoding="utf-8") as file:
        script_text = file.read()


    script_text = re.sub(" +", " ", script_text)
    chunks_fixed_size_overlapping = ...(..., overlap=50)
    embeddings_fixed_size_overlapping = ....(
        ...., ..., ...
    )

    while True:
        text = input(">>:")
        if text == "\\q":
            print("bye")
            break

        query_embedding = ...([text], ..., ...)[0]
        top_k = retrieve_chunks(..., ..., ..., top_k=3, similarity_fn=cosine_similarity)
        print(top_k)
