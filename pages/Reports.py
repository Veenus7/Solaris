import os

import streamlit as st
import pandas as pd

from database.db import get_connection

from modules.advisor import (
    rag_financial_advice
)

from modules.report_generator import (
    create_report
)

st.set_page_config(
    page_title="Report")
st.title("Generate Financial Report")

if st.button(
    "Generate Report"
):

    conn = get_connection()

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

    conn.close()

    if profile.empty:

        st.error(
            "Create profile first"
        )

        st.stop()

    user = profile.iloc[0]

    income = float(
        user["monthly_income"]
    )

    total_expense = (
        expenses["amount"].sum()
        if not expenses.empty
        else 0
    )

    savings = (
        income - total_expense
    )

    # Simple Health Score

    if income == 0:

        health_score = 0

    else:

        ratio = (
            total_expense / income
        )

        health_score = max(
            0,
            int(
                100 - ratio * 100
            )
        )

    # Profile Summary

    profile_text = f"""
Name: {user['full_name']}
Age: {user['age']}
Occupation: {user['occupation']}
Income: {user['monthly_income']}
Risk Level: {user['risk_level']}
Primary Goal: {user['primary_goal']}
"""

    # Expense Summary

    if expenses.empty:

        expense_summary = (
            "No expenses found"
        )

    else:

        expense_summary = (
            expenses
            .groupby("category")
            ["amount"]
            .sum()
            .to_string()
        )

    # Goal Summary

    goals_summary = ""

    if goals.empty:

        goals_summary = (
            "No goals added"
        )

    else:

        for _, row in goals.iterrows():

            progress = 0

            if row["target_amount"] > 0:

                progress = (
                    row["saved_amount"]
                    /
                    row["target_amount"]
                ) * 100

            goals_summary += f"""
Goal: {row['goal_name']}
Target: {row['target_amount']}
Saved: {row['saved_amount']}
Progress: {progress:.1f}%

"""

    # RAG Advice

    try:

        advice, knowledge = (
            rag_financial_advice(
                profile_text,
                expense_summary,
                goals_summary
            )
        )

    except Exception as e:

        advice = (
            f"Unable to generate advice: {e}"
        )

        knowledge = ""

    os.makedirs(
        "reports",
        exist_ok=True
    )

    path = (
        "reports/financial_report.pdf"
    )

    create_report(
        path,
        profile_text,
        income,
        total_expense,
        savings,
        health_score,
        expense_summary,
        goals_summary,
        advice,
        knowledge
    )

    st.success(
        "Report Generated Successfully"
    )

    with open(
        path,
        "rb"
    ) as file:

        st.download_button(
            "Download Report",
            file,
            file_name="financial_report.pdf",
            mime="application/pdf"
        )