from expense import Expense


def main():
    print("Expense Tracker 🎯")

    expense = get_user_expense()

    save_expense_to_file()

    summarize_expenses()


def get_user_expense():
    print("Getting User Expense")
    expense_name = input("Enter expense name: ").strip()
    expense_amount = float(input("Enter the amount: ").strip())

    expense_categories = ["Home", "Food", "Work", "Fun", "Misc"]

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


def save_expense_to_file():
    pass


def summarize_expenses():
    pass


if __name__ == "__main__":
    main()
