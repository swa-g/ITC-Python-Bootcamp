def calculate_profit_loss(transactions):
    """ Calculate total profit or loss """
    total_income = sum(int(t[1]) for t in transactions if t[0] == "Income")
    total_expense = sum(int(t[1]) for t in transactions if t[0] == "Expense")
    return total_income - total_expense

def prepare_report_data(transactions):
    """ Prepare data for bar chart """
    categories = []
    income_values = []
    expense_values = []

    category_totals = {}

    for t in transactions:
        category = t[2]
        amount = int(t[1])

        if category not in category_totals:
            category_totals[category] = {"Income": 0, "Expense": 0}

        category_totals[category][t[0]] += amount

    for cat, values in category_totals.items():
        categories.append(cat)
        income_values.append(values["Income"])
        expense_values.append(-values["Expense"])  # Negative for display

    return categories, income_values, expense_values