import streamlit as st
import pandas as pd
from database.db import get_connection

st.set_page_config(
    page_title="Dashboard")
st.title("Dashboard")

conn = get_connection()

df = pd.read_sql_query(
    "SELECT * FROM expenses",
    conn
)

conn.close()

if len(df) == 0:
    st.info("No expenses found")
    st.stop()

st.metric(
    "Total Spending",
    f"₹{df['amount'].sum():,.2f}"
)

st.subheader("Recent Expenses")

st.dataframe(df)

category_totals = (
    df.groupby("category")["amount"]
    .sum()
    .reset_index()
)

st.subheader("Category Breakdown")

st.bar_chart(
    category_totals.set_index("category")
)