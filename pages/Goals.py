import streamlit as st
import pandas as pd

from database.db import get_connection

st.set_page_config(
    page_title="Goals")
st.title("Financial Goals")


# Add New Goal


st.header("Add New Goal")

with st.form("goal_form"):

    goal_name = st.text_input("Goal Name")

    target_amount = st.number_input(
        "Target Amount",
        min_value=0.0
    )

    saved_amount = st.number_input(
        "Current Savings",
        min_value=0.0
    )

    deadline = st.date_input(
        "Deadline"
    )

    submitted = st.form_submit_button(
        "Add Goal"
    )

    if submitted:

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO goals
            (
                goal_name,
                target_amount,
                saved_amount,
                deadline
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                goal_name,
                target_amount,
                saved_amount,
                str(deadline)
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Goal Added Successfully"
        )


# View Goals


st.header("My Goals")

conn = get_connection()

goals = pd.read_sql_query(
    "SELECT * FROM goals",
    conn
)

conn.close()

if goals.empty:

    st.info(
        "No goals found"
    )

else:

    for _, row in goals.iterrows():

        goal_id = int(row["id"])

        target = float(
            row["target_amount"]
        )

        saved = float(
            row["saved_amount"]
        )

        progress = 0

        if target > 0:

            progress = saved / target

        st.subheader(
            row["goal_name"]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.write(
                f"Target: ₹{target:,.2f}"
            )

            st.write(
                f"Saved: ₹{saved:,.2f}"
            )

            st.write(
                f"Deadline: {row['deadline']}"
            )

        with col2:

            st.progress(
                min(progress, 1.0)
            )

            st.write(
                f"{progress*100:.1f}% Complete"
            )

            if saved >= target:

                st.success(
                    "Goal Achieved!"
                )

            else:

                remaining = target - saved

                st.info(
                    f"₹{remaining:,.2f} Remaining"
                )

        st.markdown("### Update Progress")

        new_saved = st.number_input(
            f"Update Savings ({row['goal_name']})",
            min_value=0.0,
            value=saved,
            key=f"update_{goal_id}"
        )

        col_update, col_delete = st.columns(2)

        with col_update:

            if st.button(
                "Save",
                key=f"save_{goal_id}"
            ):

                conn = get_connection()

                conn.execute(
                    """
                    UPDATE goals
                    SET saved_amount=?
                    WHERE id=?
                    """,
                    (
                        new_saved,
                        goal_id
                    )
                )

                conn.commit()
                conn.close()

                st.success(
                    "Goal Updated"
                )

                st.rerun()

        with col_delete:

            if st.button(
                "Delete",
                key=f"delete_{goal_id}"
            ):

                conn = get_connection()

                conn.execute(
                    """
                    DELETE FROM goals
                    WHERE id=?
                    """,
                    (
                        goal_id,
                    )
                )

                conn.commit()
                conn.close()

                st.success(
                    "Goal Deleted"
                )

                st.rerun()

        st.divider()