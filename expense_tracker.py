from expense import Expense


def main():
    print("Expense Tracker 🎯")
    expense_file_path = "expense.csv"
    budget = float(input("Your Budget For This Month: "))
    expense = get_user_expense()

    save_expense_to_file(expense, expense_file_path)

    summarize_expenses(expense_file_path, budget)


def get_user_expense():
    print("Getting User Expense🎯")
    expense_name = input("Enter expense name: ").strip()
    expense_amount = float(input("Enter the amount: ").strip())

    expense_categories = ["🏠 Home", "🥬 Food", "💼 Work", "😄 Fun", "✨ Misc"]

    while True:
        for i, category in enumerate(expense_categories):
            print(f"{i + 1}. {category}")

        value_range = f"[1 - {len(expense_categories)}]"

        index = int(input(f"Enter a category number{value_range}: ")) - 1

        if index in range(len(expense_categories)):
            selected_category = expense_categories[index]
            new_expense = Expense(
                name=expense_name, amount=expense_amount, category=selected_category
            )
            return new_expense
        else:
            print("Please enter a valid number")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    expenses: list[Expense] = []
    print("Summarizing User Expense 📝")
    with open(expense_file_path, "r", encoding="utf-8") as f:
        # lines = f.readlines()
        for line in f:
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    for key, amount in amount_by_category.items():
        print(f"{key}, ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(green(f"You've spent ${total_spent:.2f} this month!"))

    remaining_budget = budget - total_spent

    print(yellow(f"Remaining Budget ${remaining_budget:.2f} for this month!!"))


def green(text):
    return f"\033[1;32m{text}\033[0m"


def red(text):
    return f"\033[1;31m{text}\033[0m"


def blue(text):
    return f"\033[1;34m{text}\033[0m"


def yellow(text):
    return f"\033[1;33m{text}\033[0m"


if __name__ == "__main__":
    main()
