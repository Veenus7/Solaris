import streamlit as st

from rag.loader import load_pdf
from rag.splitter import split_docs
from rag.vectorstore import build_vectorstore

st.set_page_config(
    page_title="Financial Knowledge")
st.title("Upload Finance Books")

pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if pdf:

    path = f"uploads/{pdf.name}"

    with open(path, "wb") as f:
        f.write(pdf.getbuffer())

    docs = load_pdf(path)

    chunks = split_docs(docs)

    build_vectorstore(chunks)

    st.success("Knowledge Base Created")