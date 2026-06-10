import streamlit as st
import pandas as pd

from database.db import get_connection
from modules.advisor import rag_financial_advice

st.set_page_config(
    page_title="Financial Advisor")
st.title("AI Financial Advisor")

# Load Data

conn = get_connection()

try:

    profile = pd.read_sql_query(
        "SELECT * FROM user_profile",
        conn
    )

    expenses = pd.read_sql_query(
        "SELECT * FROM expenses",
        conn
    )

    goals = pd.read_sql_query(
        "SELECT * FROM goals",
        conn
    )

except Exception as e:

    st.error(f"Database Error: {e}")
    conn.close()
    st.stop()

conn.close()


# Validate Profile


if profile.empty:

    st.warning(
        "Please create your profile first."
    )

    st.stop()

# Profile Summary


user = profile.iloc[0]

profile_text = f"""
Name: {user['full_name']}
Age: {user['age']}
Occupation: {user['occupation']}
Monthly Income: ₹{user['monthly_income']}
Risk Level: {user['risk_level']}
Primary Goal: {user['primary_goal']}
"""

st.subheader("User Profile")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Income",
        f"₹{user['monthly_income']:,.0f}"
    )

with col2:
    st.metric(
        "Age",
        user["age"]
    )

with col3:
    st.metric(
        "Risk",
        user["risk_level"]
    )

# Expense Analysis


st.subheader("Expense Summary")

if expenses.empty:

    st.info(
        "No expenses found."
    )

    expense_summary = "No expenses available."

else:

    category_expenses = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    st.dataframe(
        category_expenses.reset_index()
    )

    expense_summary = (
        category_expenses.to_string()
    )


# Goal Summary


st.subheader("Goals")

goals_summary = ""

if goals.empty:

    st.info(
        "No goals added."
    )

    goals_summary = "No goals available."

else:

    for _, row in goals.iterrows():

        target = float(
            row["target_amount"]
        )

        saved = float(
            row["saved_amount"]
        )

        progress = (
            saved / target
            if target > 0
            else 0
        )

        st.write(
            f"**{row['goal_name']}**"
        )

        st.progress(
            min(progress, 1.0)
        )

        st.write(
            f"₹{saved:,.0f} / ₹{target:,.0f}"
        )

        goals_summary += f"""
        Goal: {row['goal_name']}
        Target Amount: ₹{target}
        Saved Amount: ₹{saved}
        Deadline: {row['deadline']}
        Progress: {progress*100:.1f}%
        """


# Generate Advice


st.divider()

if st.button(
    "Generate AI Advice"
):

    with st.spinner(
        "Analyzing finances..."
    ):

        try:

            advice, context = (
                rag_financial_advice(
                    profile_text,
                    expense_summary,
                    goals_summary
                )
            )

            st.subheader(
                "Personalized Advice"
            )

            st.write(
                advice
            )

            with st.expander(
                "Financial Knowledge Used"
            ):

                st.write(
                    context
                )

        except Exception as e:

            st.error(
                f"Error generating advice: {e}"
            )