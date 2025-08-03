def chunk_transcript(segments, max_length=200):
    chunks = []
    current_chunk = ""
    start_time = 0

    for s in segments:
        if len(current_chunk) + len(s["text"]) > max_length:
            chunks.append({"text": current_chunk.strip(), "timestamp": start_time})
            current_chunk = s["text"] + " "
            start_time = s["start"]
        else:
            current_chunk += s["text"] + " "

    if current_chunk:
        chunks.append({"text": current_chunk.strip(), "timestamp": start_time})

    return chunks