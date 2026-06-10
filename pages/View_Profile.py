import streamlit as st
import pandas as pd

from database.db import get_connection

st.set_page_config(
    page_title="View Profile")
st.title("Profile Dashboard")

conn = get_connection()

profile = pd.read_sql_query(
    "SELECT * FROM user_profile",
    conn
)

conn.close()

if profile.empty:

    st.warning(
        "Create your profile first"
    )

else:

    user = profile.iloc[0]

    st.subheader(
        f"Welcome, {user['full_name']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Monthly Income",
            f"₹{user['monthly_income']:,.0f}"
        )

    with col2:

        st.metric(
            "Age",
            str(user["age"])
        )

    with col3:

        st.metric(
            "Risk Level",
            user["risk_level"]
        )

    st.divider()

    st.write(
        f"**Occupation:** {user['occupation']}"
    )

    st.write(
        f"**Email:** {user['email']}"
    )

    st.write(
        f"**Primary Goal:** {user['primary_goal']}"
    )

    st.divider()

    if user["risk_level"] == "Low":

        st.success(
            "Conservative investment profile"
        )

    elif user["risk_level"] == "Medium":

        st.info(
            "Balanced investment profile"
        )

    else:

        st.warning(
            "Aggressive investment profile"
        )   