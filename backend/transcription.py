import whisper

def transcribe_audio(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    segments = result.get("segments", [])
    return [{"text": s["text"], "start": s["start"]} for s in segments]