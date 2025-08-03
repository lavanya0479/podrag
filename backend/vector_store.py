import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

vector_db = []  # In-memory list to store embeddings and metadata

def add_to_vector_store(chunks):
    for c in chunks:
        vector_db.append({
            "embedding": c["embedding"],
            "text": c["text"],
            "timestamp": f"{c['timestamp']:.2f}s",
            "episode": "Uploaded Episode"
        })

def query_vector_store(query, top_k=3):
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_embedding = model.encode([query])

    sims = [
        (cosine_similarity([item["embedding"]], query_embedding)[0][0], item)
        for item in vector_db
    ]

    sims.sort(reverse=True, key=lambda x: x[0])
    return [item for _, item in sims[:top_k]]
