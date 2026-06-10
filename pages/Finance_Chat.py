import streamlit as st

from rag.vectorstore import get_retriever
from modules.advisor import model

st.set_page_config(
    page_title="Finance Chat")
st.title(
    "Finance Knowledge Chat"
)

question = st.text_input(
    "Ask a question"
)

if st.button(
    "Ask"
):

    retriever = get_retriever()

    docs = retriever.invoke(
        question
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Context:

    {context}

    Question:

    {question}
    """

    response = model.generate_content(
        prompt
    )

    st.write(
        response.text
    )

    with st.expander(
        "Sources"
    ):

        st.write(context)

try:

    retriever = get_retriever()

except Exception as e:

    st.error(str(e))

    st.stop()