import streamlit as st
from backend.transcription import transcribe_audio
from backend.chunking import chunk_transcript
from backend.embedding import embed_chunks
from backend.vector_store import query_vector_store, add_to_vector_store
from backend.rag_pipeline import generate_answer
import tempfile

def main_ui():
    try:
        st.title("🎙️ PodRAG: Podcast Topic Search")

        uploaded_file = st.file_uploader("Upload a podcast episode (mp3/wav)", type=["mp3", "wav"])
        query = st.text_input("Enter your topic/question")

        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp:
                tmp.write(uploaded_file.read())
                audio_path = tmp.name

            st.info("Transcribing audio...")
            transcript = transcribe_audio(audio_path)
            chunks = chunk_transcript(transcript)
            embed_chunks(chunks)
            add_to_vector_store(chunks)
            st.success("Transcript added to vector store!")

        if query:
            st.info("Searching...")
            results = query_vector_store(query)
            answer = generate_answer(query, results)

            st.subheader("Answer:")
            st.write(answer)

            st.subheader("Relevant Segments:")
            for r in results:
                st.markdown(f"**{r['episode']}** — `{r['timestamp']}`")
                st.markdown(f"> {r['text']}")

    except Exception as e:
        st.error(f"💥 An error occurred:\n\n```\n{e}\n```")
