# Expense Tracker 🎯

A simple expense tracker written in Python, with both a command-line version
and a tkinter window. Log your expenses by category, save them to a CSV file,
and see a monthly summary of how much you've spent vs. your budget.

## Features

- Add an expense with a name, amount, and category
- Categories: 🏠 Home, 🥬 Food, 💼 Work, 😄 Fun, ✨ Misc
- Saves every expense to `expense.csv` so data persists between runs
- Shows a summary grouped by category
- Shows total spent and remaining budget, with colored output
- Command line: prompts again if you enter an invalid category
- Window (GUI): table of all expenses, live budget summary, and error pop-ups
  for a missing name or a bad amount

## Requirements

- Python 3.9 or newer
- No third-party packages — only the standard library (tkinter comes with
  Python; on some Linux systems it needs `sudo apt install python3-tk`)

## Project Structure

| File | What it does |
|------|--------------|
| `expense.py` | The `Expense` class (name, amount, category) |
| `expense_tracker.py` | The command-line version |
| `tracker_logic.py` | Logic for the GUI: loading, saving, and summarizing expenses (no tkinter) |
| `expense_gui.py` | The tkinter window; imports from `tracker_logic.py` and `expense.py` |

Both versions read and write the same `expense.csv`, so expenses added in one
show up in the other. Run either one from the project folder, since the CSV is
found relative to where you start the program.

## How to Run

Command line:

```bash
python expense_tracker.py
```

Window:

```bash
python expense_gui.py
```

## Usage

### Command line

You'll be prompted for:

1. Your budget for the month (a number)
2. The name of the expense
3. The amount
4. A category number from the menu

### Window

1. Type your monthly budget at the top (the summary updates as you type).
2. Fill in a name, an amount, and pick a category from the dropdown.
3. Press **Add** (or Enter). The expense is saved and appears in the table.
4. The summary shows spending per category, the total spent, and what's
   remaining (green) or how far over budget you are (red).

## How It Works

### Command line

- `main()` asks for your budget, then gets one expense from you.
- `get_user_expense()` collects the name, amount, and category.
- It loops until you pick a valid category number.
- `save_expense_to_file()` appends the expense to `expense.csv`.
- `summarize_expenses()` reads the whole CSV, groups amounts by
  category, and prints totals plus your remaining budget.

### Window

- The logic is kept separate from the interface, so the window only handles
  buttons and drawing.
- `load_expenses()` reads `expense.csv` and returns a list of `Expense` objects.
- `save_expense_to_file()` appends one expense using the `csv` module, so a
  comma inside a name (like "Lunch, with Sam") is saved safely.
- `summarize_expenses()` takes the list and returns the amount per category
  and the total spent.
- After every Add, the window reloads the file and redraws the table and summary.

## Notes

- The CSV stores values as plain text, so amounts are converted back
  to `float` when read.
- Colors in the command-line version use ANSI escape codes, so they work in
  most terminals.
- If the emoji in the categories show as boxes in the window, remove them
  from `CATEGORIES` in `tracker_logic.py`.

## Possible Improvements

- Command line: handle bad input (e.g. `abc` for the amount) without crashing
  (the window already does)
- Command line: use the `csv` module instead of manual `split(",")` so commas
  inside names don't break parsing (the window already does)
- Add a `__str__` method for prettier printing
- Make the budget optional in the command-line version so you can just view
  past expenses (the window already works without one)
- Window: delete or edit an existing expense