from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def build_vectorstore(chunks):

    embeddings = get_embeddings()

    db = FAISS.from_documents(
        chunks,
        embeddings
    )

    os.makedirs(
        "rag/faiss_db",
        exist_ok=True
    )

    db.save_local(
        "rag/faiss_db"
    )

    return db


def get_retriever():

    if not os.path.exists(
        "rag/faiss_db/index.faiss"
    ):
        raise Exception(
            "Upload a finance PDF first."
        )

    embeddings = get_embeddings()

    db = FAISS.load_local(
        "rag/faiss_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever()