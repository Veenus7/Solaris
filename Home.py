import streamlit as st
import pandas as pd
from database.db import get_connection, create_tables
from dotenv import load_dotenv

load_dotenv()
create_tables()
st.set_page_config(
    page_title="Solaris AI",
    page_icon="☀️",
    layout="wide"
)

st.title("Solaris")
st.caption("AI powered Financial Advisor,Expense tracker, Manage goals, savings and get AI-powered financial insights.")

conn = get_connection()

# LOAD DATA

try:
    expenses = pd.read_sql_query(
        "SELECT * FROM expenses",
        conn
    )
except:
    expenses = pd.DataFrame()

try:
    goals = pd.read_sql_query(
        "SELECT * FROM goals",
        conn
    )
except:
    goals = pd.DataFrame()

try:
    profile = pd.read_sql_query(
        "SELECT * FROM user_profile",
        conn
    )
except:
    profile = pd.DataFrame()

conn.close()

# PROFILE


income = 0

if not profile.empty:
    income = profile.iloc[0]["monthly_income"]


# EXPENSES


total_expenses = 0

if not expenses.empty:
    total_expenses = expenses["amount"].sum()

savings = income - total_expenses

savings_pct = 0

if income > 0:
    savings_pct = (savings / income) * 100


# TOP STATS


st.subheader("Financial Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Monthly Income",
        f"₹{income:,.0f}"
    )

with col2:
    st.metric(
        "Total Expenses",
        f"₹{total_expenses:,.0f}"
    )

with col3:
    st.metric(
        "Savings",
        f"₹{savings:,.0f}"
    )

with col4:
    st.metric(
        "Savings %",
        f"{savings_pct:.1f}%"
    )

st.divider()


# GOALS


st.subheader("Goal Progress")

if goals.empty:

    st.info("No goals added yet.")

else:

    for _, goal in goals.iterrows():

        target = goal["target_amount"]
        saved = goal["saved_amount"]

        progress = 0

        if target > 0:
            progress = saved / target

        st.markdown(
            f"### {goal['goal_name']}"
        )

        st.progress(
            min(progress, 1.0)
        )

        st.write(
            f"₹{saved:,.0f} / ₹{target:,.0f}"
        )

        remaining = target - saved

        if remaining > 0:
            st.caption(
                f"Remaining: ₹{remaining:,.0f}"
            )
        else:
            st.success(
                "Goal Achieved 🎉"
            )

st.divider()


# EXPENSE SUMMARY


st.subheader("Expense Breakdown")

if not expenses.empty:

    category_summary = (
        expenses
        .groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    st.bar_chart(
        category_summary.set_index("category")
    )

else:

    st.info(
        "No expenses available."
    )

st.divider()

# RECENT TRANSACTIONS


st.subheader("Recent Transactions")

if not expenses.empty:

    recent = (
        expenses
        .sort_values(
            "id",
            ascending=False
        )
        .head(10)
    )

    st.dataframe(
        recent[
            [
                "date",
                "merchant",
                "amount",
                "category",
                "source"
            ]
        ],
        use_container_width=True
    )

else:

    st.info(
        "No transactions found."
    )

st.divider()


# PROFILE SUMMARY


st.subheader("Profile")

if not profile.empty:

    p = profile.iloc[0]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Income",
            f"₹{p['monthly_income']:,.0f}"
        )

    with c2:
        st.metric(
            "Age",
            int(p["age"])
        )

    with c3:
        st.metric(
            "Risk Level",
            p["risk_level"]
        )

    if "name" in profile.columns:

        with c4:
            st.metric(
                "Name",
                p["name"]
            )

else:

    st.info(
        "No profile created."
    )

st.divider()

st.success(
    "Finance AI Dashboard Loaded Successfully"
)