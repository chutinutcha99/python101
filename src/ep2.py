import tkinter as tk

def add_income():
    income = int(income_entry.get())
    current_income = int(income_label['text'])
    current_income += income
    income_label.config(text=str(current_income))

def add_expense():
    expense = int(expense_entry.get())
    current_expense = int(expense_label['text'])
    current_expense += expense
    expense_label.config(text=str(current_expense))

root = tk.Tk()
root.geometry("300x200")

income_label = tk.Label(root, text="0")
income_label.pack()

expense_label = tk.Label(root, text="0")
expense_label.pack()

income_entry = tk.Entry(root)
income_entry.pack()

expense_entry = tk.Entry(root)
expense_entry.pack()

add_income_button = tk.Button(root, text="Add Income", command=add_income)
add_income_button.pack()

add_expense_button = tk.Button(root, text="Add Expense", command=add_expense)
add_expense_button.pack()

root.mainloop()
