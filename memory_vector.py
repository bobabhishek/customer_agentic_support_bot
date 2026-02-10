#(LOCAL VECTOR STORE)
import json
import numpy as np
from azure_openai_client import get_embedding

MEMORY_FILE = "vector_memory.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def store_memory(customer_id, text, status="unresolved"):
    memory = load_memory()
    embedding = get_embedding(text)

    memory.append({
        "customer_id": customer_id,
        "text": text,
        "embedding": embedding,
        "status": status
    })

    save_memory(memory)


def retrieve_relevant_memory(customer_id, query, top_k=2):
    memory = load_memory()
    query_embedding = get_embedding(query)

    scored = []
    for item in memory:
        if item["customer_id"] == customer_id and item["status"] == "unresolved":
            score = cosine_similarity(query_embedding, item["embedding"])
            scored.append((score, item["text"]))

    scored.sort(reverse=True)
    return [text for _, text in scored[:top_k]]


def mark_resolved(customer_id):
    memory = load_memory()

    for item in memory:
        if item["customer_id"] == customer_id:
            item["status"] = "resolved"

    save_memory(memory)
