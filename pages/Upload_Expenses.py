import streamlit as st
import pandas as pd
from modules.ocr import extract_text
from modules.extractor import extract_expense_details
from modules.categorizer import categorize_expense
from database.db import get_connection

st.set_page_config(
    page_title="Upload Expense")
st.title("Upload Expense")

uploaded_file = st.file_uploader(
    "Upload Payment Screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    file_path = f"uploads/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = extract_text(file_path)

    expense = extract_expense_details(text)

    category = categorize_expense(
        expense["merchant"]
    )

    conn = get_connection()

    conn.execute(
     """
     INSERT INTO expenses
     (date, merchant, amount, category, source)
     VALUES (?, ?, ?, ?, ?)
     """,
     (
        str(pd.Timestamp.now().date()),
        expense["merchant"],
        expense["amount"],
        category,
        "screenshot"
     )
)


    conn.commit()
    conn.close()

    st.success("Expense Added")

    st.json(
        {
            "merchant": expense["merchant"],
            "amount": expense["amount"],
            "category": category
        }
    )