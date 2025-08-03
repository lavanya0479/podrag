# 🎙️ PodRAG - Audio-to-Text RAG for Podcast Topic Search

A multimodal Retrieval-Augmented Generation (RAG) system that lets users upload podcast audio (MP3/WAV), transcribe it to text, and query specific topics. The system returns timestamped answers using semantic search and contextual generation.

---

## 🚀 Features

- 🎧 Upload podcast episodes (MP3 or WAV)
- 🔤 High-accuracy transcription using OpenAI Whisper
- 🧩 Intelligent chunking with timestamp preservation
- 🔍 Semantic search over multiple episodes
- 🧠 RAG-based question answering with `google/flan-t5-small`
- ⏱️ Timestamps for relevant audio segments

---

## 🧰 Tech Stack

| Task                      | Tool / Library                |
|---------------------------|-------------------------------|
| Audio Transcription       | `openai/whisper`              |
| Embedding Model           | `sentence-transformers/all-MiniLM-L6-v2` |
| Answer Generator (RAG)    | `google/flan-t5-small`        |
| Vector Store              | In-memory (Chroma or custom) + cosine similarity |
| Interface                 | Streamlit                     |

---

## 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/podrag.git
cd podrag

# 2. (Optional) Create a virtual environment
python -m venv venv
# Activate it:
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the Streamlit app
streamlit run run_app.py
