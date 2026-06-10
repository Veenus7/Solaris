def calculate_health_score(income, expenses):

    total_expense = expenses["amount"].sum()

    savings = income - total_expense

    if income <= 0:
        return 0

    savings_ratio = savings / income

    score = 0

    if savings_ratio >= 0.30:
        score += 40
    elif savings_ratio >= 0.20:
        score += 30
    elif savings_ratio >= 0.10:
        score += 20

    categories = expenses["category"].nunique()

    score += min(categories * 5, 30)

    if total_expense <= income:
        score += 30

    return min(score, 100)