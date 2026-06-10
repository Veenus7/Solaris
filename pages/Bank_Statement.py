import streamlit as st
import pandas as pd
from database.db import get_connection
from modules.categorizer import categorize_expense

st.set_page_config(
    page_title="Bank Statement")
st.title("Bank Statement Upload")

file = st.file_uploader(
    "Upload CSV Statement",
    type=["csv"]
)

if file:

    df = pd.read_csv(file)

    st.dataframe(df.head())

    conn = get_connection()

    for _, row in df.iterrows():

        merchant = str(row["Description"])

        category = categorize_expense(
            merchant
        )

        conn.execute(
            """
            INSERT INTO expenses
            (
                date,
                merchant,
                amount,
                category,
                source
            )
            VALUES(?,?,?,?,?)
            """,
            (
                str(row["Date"]),
                merchant,
                float(row["Amount"]),
                category,
                "bank_csv"
            )
        )

    conn.commit()
    conn.close()

    st.success("Statement Imported")