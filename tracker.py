import csv

from expense import Expense

EXPENSE_FILE = "expense.csv"
CATEGORIES = ["🏠 Home", "🥬 Food", "💼 Work", "😄 Fun", "✨ Misc"]


def load_expenses(expense_file_path=EXPENSE_FILE):
    """Read every expense from the CSV. Missing file means no expenses yet."""
    expenses = []
    try:
        with open(expense_file_path, "r", encoding="utf-8", newline="") as f:
            # skipinitialspace handles the old "name, amount, category" format
            for row in csv.reader(f, skipinitialspace=True):
                if len(row) != 3:
                    continue
                name, amount, category = (x.strip() for x in row)
                try:
                    amount = float(amount)
                except ValueError:
                    continue
                expenses.append(Expense(name=name, amount=amount, category=category))
    except FileNotFoundError:
        pass
    return expenses


def save_expense_to_file(expense, expense_file_path=EXPENSE_FILE):
    """Append one expense. The csv module quotes names that contain commas."""
    with open(expense_file_path, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([expense.name, expense.amount, expense.category])


def summarize_expenses(expenses):
    """Return (amount_by_category, total_spent)."""
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    total_spent = sum([x.amount for x in expenses])
    return amount_by_category, total_spent
