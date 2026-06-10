def categorize_expense(merchant):

    merchant = merchant.lower()
    mapping = {
        "swiggy": "Food",
        "zomato": "Food",
        "uber": "Transport",
        "ola": "Transport",
        "amazon": "Shopping",
        "flipkart": "Shopping",
        "netflix": "Entertainment",
        "spotify": "Entertainment",
        "jio": "Bills",
        "airtel": "Bills"
    }

    for key, value in mapping.items():
        if key in merchant:
            return value

    return "Others"