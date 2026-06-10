from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os


def get_retriever():

    if not os.path.exists(
        "rag/faiss_db/index.faiss"
    ):
        raise Exception(
            "No knowledge base found. Upload a finance PDF first."
        )

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "rag/faiss_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever()