import tkinter as tk
from tkinter import messagebox, ttk

from expense import Expense
from tracker import (
    CATEGORIES,
    load_expenses,
    save_expense_to_file,
    summarize_expenses,
)


class ExpenseApp:
    def __init__(self, root):
        self.root = root
        root.title("Expense Tracker")
        root.resizable(False, False)

        self.expenses = []
        self.budget_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.amount_var = tk.StringVar()
        self.category_var = tk.StringVar(value=CATEGORIES[0])

        self.build_ui()
        self.budget_var.trace_add("write", lambda *args: self.update_summary())
        self.refresh()

    def build_ui(self):
        pad = {"padx": 10, "pady": 5}

        top = ttk.Frame(self.root)
        top.grid(row=0, column=0, sticky="ew", **pad)
        ttk.Label(top, text="Monthly budget: $").pack(side="left")
        ttk.Entry(top, textvariable=self.budget_var, width=12).pack(side="left")

        form = ttk.LabelFrame(self.root, text="Add expense")
        form.grid(row=1, column=0, sticky="ew", **pad)
        ttk.Label(form, text="Name").grid(row=0, column=0, sticky="w", padx=5, pady=3)
        name_entry = ttk.Entry(form, textvariable=self.name_var, width=24)
        name_entry.grid(row=0, column=1, padx=5, pady=3)
        ttk.Label(form, text="Amount").grid(row=1, column=0, sticky="w", padx=5, pady=3)
        amount_entry = ttk.Entry(form, textvariable=self.amount_var, width=24)
        amount_entry.grid(row=1, column=1, padx=5, pady=3)
        ttk.Label(form, text="Category").grid(
            row=2, column=0, sticky="w", padx=5, pady=3
        )
        ttk.Combobox(
            form,
            textvariable=self.category_var,
            values=CATEGORIES,
            state="readonly",
            width=21,
        ).grid(row=2, column=1, padx=5, pady=3)
        ttk.Button(form, text="Add", command=self.add_expense).grid(
            row=3, column=0, columnspan=2, pady=6
        )
        self.name_entry = name_entry
        for entry in (name_entry, amount_entry):
            entry.bind("<Return>", lambda event: self.add_expense())

        table_frame = ttk.Frame(self.root)
        table_frame.grid(row=2, column=0, sticky="ew", **pad)
        self.tree = ttk.Treeview(
            table_frame,
            columns=("name", "amount", "category"),
            show="headings",
            height=8,
        )
        for col, title, width in (
            ("name", "Name", 150),
            ("amount", "Amount", 80),
            ("category", "Category", 110),
        ):
            self.tree.heading(col, text=title)
            self.tree.column(col, width=width, anchor="w" if col != "amount" else "e")
        scroll = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left")
        scroll.pack(side="left", fill="y")

        summary = ttk.LabelFrame(self.root, text="Summary")
        summary.grid(row=3, column=0, sticky="ew", **pad)
        self.category_label = ttk.Label(summary, text="", justify="left")
        self.category_label.pack(anchor="w", padx=8, pady=(4, 0))
        self.total_label = ttk.Label(summary, text="", font=("Segoe UI", 10, "bold"))
        self.total_label.pack(anchor="w", padx=8, pady=(4, 0))
        self.remaining_label = tk.Label(summary, text="", font=("Segoe UI", 10, "bold"))
        self.remaining_label.pack(anchor="w", padx=8, pady=(0, 6))

    def refresh(self):
        self.expenses = load_expenses()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for e in self.expenses:
            self.tree.insert("", "end", values=(e.name, f"${e.amount:.2f}", e.category))
        self.update_summary()

    def update_summary(self):
        amount_by_category, total_spent = summarize_expenses(self.expenses)
        lines = [f"{cat}: ${amount:.2f}" for cat, amount in amount_by_category.items()]
        self.category_label.config(
            text="\n".join(lines) if lines else "No expenses yet"
        )
        self.total_label.config(text=f"Total spent: ${total_spent:.2f}")

        try:
            budget = float(self.budget_var.get())
        except ValueError:
            self.remaining_label.config(
                text="Enter a budget to see what's left", fg="gray"
            )
            return
        remaining_budget = budget - total_spent
        if remaining_budget < 0:
            self.remaining_label.config(
                text=f"Over budget by ${-remaining_budget:.2f}", fg="#dc2626"
            )
        else:
            self.remaining_label.config(
                text=f"Remaining: ${remaining_budget:.2f}", fg="#16a34a"
            )

    def add_expense(self):
        name = self.name_var.get().strip()
        if not name:
            messagebox.showerror("Missing name", "Enter a name for the expense.")
            return
        try:
            amount = float(self.amount_var.get().strip())
        except ValueError:
            messagebox.showerror(
                "Bad amount", "The amount must be a number, like 12.50."
            )
            return
        if amount <= 0:
            messagebox.showerror("Bad amount", "The amount must be more than 0.")
            return

        save_expense_to_file(
            Expense(name=name, amount=amount, category=self.category_var.get())
        )
        self.name_var.set("")
        self.amount_var.set("")
        self.name_entry.focus()
        self.refresh()


if __name__ == "__main__":
    root = tk.Tk()
    ExpenseApp(root)
    root.mainloop()
