def chunk_text(text: str, chunk_size: int = 3) -> list[str]:
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    chunks = []

    for i in range(0, len(lines), chunk_size):
        chunk = "\n".join(lines[i:i + chunk_size])
        chunks.append(chunk)

    return chunks