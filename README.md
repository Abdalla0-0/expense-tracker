# Expense Tracker 🎯

A simple command-line expense tracker written in Python. Log your daily
expenses by category, save them to a CSV file, and see a monthly summary
of how much you've spent vs. your budget.

## Features

- Add an expense with a name, amount, and category
- Categories: 🏠 Home, 🥬 Food, 💼 Work, 😄 Fun, ✨ Misc
- Saves every expense to `expense.csv` so data persists between runs
- Shows a summary grouped by category
- Shows total spent and remaining budget, with colored output
- Prompts again if you enter an invalid category

## Requirements

- Python 3.9 or newer
- No third-party packages — only the standard library

## How to Run

```bash
python expense_tracker.py  
```


## Usage

You'll be prompted for:

1. Your budget for the month (a number)
2. The name of the expense
3. The amount
4. A category number from the menu

## How It Works

- `main()` asks for your budget, then gets one expense from you.
- `get_user_expense()` collects the name, amount, and category.
- It loops until you pick a valid category number.
- `save_expense_to_file()` appends the expense to `expense.csv`.
- `summarize_expenses()` reads the whole CSV, groups amounts by
  category, and prints totals plus your remaining budget.

## Notes

- The CSV stores values as plain text, so amounts are converted back
  to `float` when read.
- Colors use ANSI escape codes, so they work in most terminals.

## Possible Improvements

- Handle bad input (e.g. `abc` for the amount) without crashing
- Use the `csv` module instead of manual `split(",")` so commas inside
  names don't break parsing
- Add a `__str__` method for prettier printing
- Make the budget optional so you can just view past expenses