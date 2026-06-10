import streamlit as st
from database.db import get_connection

st.set_page_config(
    page_title="Profile")
st.title("Financial Profile")

conn = get_connection()

existing = conn.execute(
    "SELECT * FROM user_profile LIMIT 1"
).fetchone()

conn.close()

with st.form("profile_form"):

    full_name = st.text_input(
        "Full Name",
        value=existing[1] if existing else ""
    )

    email = st.text_input(
        "Email",
        value=existing[2] if existing else ""
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=existing[3] if existing else 18
    )

    occupation = st.text_input(
        "Occupation",
        value=existing[4] if existing else ""
    )

    income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=float(existing[5]) if existing else 0.0
    )

    risk = st.selectbox(
        "Risk Appetite",
        ["Low", "Medium", "High"],
        index=(
            ["Low","Medium","High"].index(existing[6])
            if existing and existing[6] in ["Low","Medium","High"]
            else 1
        )
    )

    primary_goal = st.text_input(
        "Primary Financial Goal",
        value=existing[7] if existing else ""
    )

    submit = st.form_submit_button(
        "Save Profile"
    )

    if submit:

        conn = get_connection()

        conn.execute(
            "DELETE FROM user_profile"
        )

        conn.execute(
            """
            INSERT INTO user_profile
            (
                full_name,
                email,
                age,
                occupation,
                monthly_income,
                risk_level,
                primary_goal
            )
            VALUES (?,?,?,?,?,?,?)
            """,
            (
                full_name,
                email,
                age,
                occupation,
                income,
                risk,
                primary_goal
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Profile Saved Successfully"
        )