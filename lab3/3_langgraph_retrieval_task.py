import ollama
import re
import os
import sqlite3
import sqlite_vec
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_community.vectorstores import SQLiteVec
from langchain_ollama import OllamaEmbeddings
from utils import create_fixed_size_chunks



def setup_db(text_path, db_path, embeddings_model):
    with open(...) as f:
        text = re.sub(" +", " ", f.read())

    if os.path.exists(...):
        os....(db_path)
        print(f"Removed existing database")

    chunks = ...(text, chunk_size=1000, overlap=50)

    print("Generating embeddings...")

    # this is hard, so let it be
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)

    # use ollama here
    embeddings = ...(model=...)
    # and langchain magix here
    store = SQLiteVec....(texts=..., embedding=..., table="documents", connection=conn)
    print(f"Stored {len(chunks)} chunks")
    return store


def create_graph():
    chat_model = "llama_local"
    db_path = "retrieval.db"
    embeddings_model = "nomic_local"
    store= setup_db("shrek.txt", db_path, embeddings_model)

    class State(TypedDict):
        query: str
        context: str
        response: str

    def embed_query(state: State):
        return state


    def retrieve(state: State):
        results = store....(state[...], k=3)
        print(results)
        return {...: "\n\n".join([doc.page_content for doc in results])}


    def generate(state: State):
        prompt = f"""Context:
        {state[...]}

        Question: {state[...]}

        Answer:"""
        stream = ollama.chat(model=chat_model, messages=[{"role": "user", "content": prompt}], stream=True)
        return {"response": stream}


    workflow = StateGraph(State)
    workflow.add_node("embed", embed_query)
    # missing arguments
    workflow.add_node("retrieve", ...)
    workflow.add_node("generate", ...)

    workflow.set_entry_point("embed")
    workflow.add_edge("embed", "retrieve")
    # misssing full line
    ...
    workflow.add_edge("generate", END)
    graph = workflow.compile()
    return graph



if __name__ == "__main__":
    app = create_graph()
    while True:
        q = input(">>:")
        if q == "\\q":
            print("bye")
            break
        result = app.invoke({'query': q})
        stream = result['response']
        print()
        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)
        print("\n")
