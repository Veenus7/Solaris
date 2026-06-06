import re


def extract_expense_details(text):

    amount_pattern = r"\d+\.\d+|\d+"

    amounts = re.findall(amount_pattern, text)

    amount = float(amounts[0]) if amounts else 0

    merchant = "Unknown"

    lines = text.split("\n")

    for line in lines:
        if len(line.strip()) > 3:
            merchant = line.strip()
            break

    return {
        "amount": amount,
        "merchant": merchant
    }