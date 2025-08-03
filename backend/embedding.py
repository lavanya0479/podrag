from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks):
    for chunk in chunks:
        chunk["embedding"] = model.encode(chunk["text"])