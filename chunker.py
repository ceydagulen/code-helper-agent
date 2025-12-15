from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_code(files: list):
    """
    files: [
        {"path": "...", "content": "..."},
        ...
    ]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    all_chunks = []

    for file in files:
        chunks = splitter.split_text(file["content"])

        for chunk in chunks:
            all_chunks.append({
                "path": file["path"],
                "content": chunk
            })

    return all_chunks
