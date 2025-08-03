import torch
from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="google/flan-t5-small", device=0 if torch.cuda.is_available() else -1)

qa_pipeline = load_model()

def generate_answer(query, docs):
    context = "\n\n".join([d["text"] for d in docs])
    prompt = f"Answer the question based on the context.\n\nContext:\n{context}\n\nQuestion: {query}"

    result = qa_pipeline(prompt, max_new_tokens=256, do_sample=False)
    return result[0]["generated_text"].strip()
