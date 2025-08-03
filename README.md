# 🎙️ PodRAG - Audio-to-Text RAG for Podcast Topic Search

A multimodal Retrieval-Augmented Generation (RAG) system that lets users upload audio podcasts, transcribe them to text, and query specific topics with timestamped segments.

---

## 🚀 Features

- 🎧 Upload podcast audio (MP3/WAV)
- 🔤 Transcription using OpenAI Whisper
- 📦 Chunking & timestamping of transcript
- 🔍 Semantic search over audio content
- 🧠 Contextual question answering using `google/flan-t5-small`
- 🧭 Display relevant timestamps for found answers

---

## 🧰 Tech Stack

| Task                      | Tool / Library                |
|---------------------------|-------------------------------|
| Audio Transcription       | `openai/whisper`              |
| Embedding Model           | `all-MiniLM-L6-v2` (SBERT)    |
| Answer Generator (RAG)    | `google/flan-t5-small`        |
| Retrieval (Vector Store)  | In-memory + cosine similarity |
| Interface                 | Streamlit                     |

---

## 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/podrag.git
cd podrag

# 2. Create virtual env (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run run_app.py
