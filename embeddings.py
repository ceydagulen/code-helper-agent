from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def build_vector_store(chunks: list):
    documents = []

    for chunk in chunks:
        documents.append(
            Document(
                page_content=chunk["content"],
                metadata={"path": chunk["path"]}
            )
        )

    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
