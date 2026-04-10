def chunk_text(pages, chunk_size=500, overlap=100):
    chunks = []

    for page in pages:
        text = page["text"]

        if not text:
            continue

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append({
                "content": chunk,
                "page": page["page"]
            })

            start += chunk_size - overlap

    return chunks