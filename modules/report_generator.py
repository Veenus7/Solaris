from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


def create_report(
    filename,
    profile_text,
    income,
    total_expense,
    savings,
    health_score,
    expense_summary,
    goals_summary,
    advice,
    knowledge
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    # Title

    elements.append(
        Paragraph(
            "Solaris Financial Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # Profile

    elements.append(
        Paragraph(
            "User Profile",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            profile_text.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # Financial Summary

    elements.append(
        Paragraph(
            "Financial Summary",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            f"Monthly Income: {income:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Total Expenses: {total_expense:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Savings: {savings:,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Financial Health Score: {health_score}/100",
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # Expenses

    elements.append(
        Paragraph(
            "Expense Breakdown",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            expense_summary.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 15)
    )

    # Goals

    elements.append(
        Paragraph(
            "Goals Progress",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            goals_summary.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    elements.append(
        PageBreak()
    )

    # Advice

    elements.append(
        Paragraph(
            "AI Financial Advice",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            advice.replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    # Knowledge Used

    elements.append(
        Paragraph(
            "Financial Knowledge Used",
            styles["Heading1"]
        )
    )

    elements.append(
        Paragraph(
            knowledge[:5000].replace(
                "\n",
                "<br/>"
            ),
            styles["BodyText"]
        )
    )

    doc.build(elements)