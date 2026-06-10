import google.generativeai as genai

from rag.retrieval import get_retriever

import os


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def get_financial_advice(
    income,
    expenses_summary
):

    prompt = f"""
     User Profile:

     Name: {profile['name']}
     Occupation: {profile['occupation']}
     Income: ₹{profile['income']}
     Risk Appetite: {profile['risk']}
     Goal: {profile['goal']}

     Expenses:
     {expenses_summary}

     Provide personalized financial advice.
    """

    response = model.generate_content(
        prompt
    )

    return response.text



def rag_financial_advice(question):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {question}

    Answer using the context.
    """

    response = model.generate_content(
        prompt
    )

    return response.text



def rag_financial_advice(
    profile,
    expense_summary,
    goals_summary
):

    retriever = get_retriever()

    docs = retriever.invoke(
        "personal finance budgeting investing saving money"
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    USER PROFILE

    {profile}

    EXPENSES

    {expense_summary}

    GOALS

    {goals_summary}

    FINANCIAL KNOWLEDGE

    {context}

    Analyze the user's finances.

    Give:
    1. Spending analysis
    2. Saving recommendations
    3. Goal recommendations
    4. Investment suggestions based on risk level
    """

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        prompt
    )

    return response.text, context