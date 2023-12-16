import tkinter as tk
from datetime import date
from tkinter import ttk
from app.main import *


from app.main import add_expense, modify_expense, delete_expense, get_expenses

def submit_expense():
    # Get values from the input fields
    # import datetime
    import datetime as dt
    date = dt.date.today()
    amount = float(amount_entry.get())
    category = category_entry.get()
    description = description_entry.get()

    # Call the add_expense function to save the expense to the database
    add_expense(date, amount, category, description)

    # Refresh the expense list after submitting
    refresh_expense_list()

    # Clear the input fields after submitting
    clear_input_fields()

def modify_selected_expense():
    # Get the selected item from the listbox
    selected_item = expenses_listbox.curselection()

    if selected_item:
        expense_id = int(selected_item[0])
        import datetime as dt
        date = dt.date.today()
        amount = float(amount_entry.get())
        category = category_entry.get()
        description = description_entry.get()

        # Call the modify_expense function to update the selected expense in the database
        modify_expense(expense_id, date,amount, category, description)

        # Refresh the expense list after modifying
        refresh_expense_list()

        # Clear the input fields after modifying
        clear_input_fields()

def delete_selected_expense():
    # Get the selected item from the listbox
    selected_item = expenses_listbox.curselection()

    if selected_item:
        expense_id = int(selected_item[0])

        # Call the delete_expense function to remove the selected expense from the database
        delete_expense(expense_id)

        # Refresh the expense list after deleting
        refresh_expense_list()

        # Clear the input fields after deleting
        clear_input_fields()

def refresh_expense_list():
    # Clear the existing items in the listbox
    expenses_listbox.delete(0, tk.END)

    # Retrieve the updated list of expenses from the database
    expenses = get_expenses()

    # Populate the listbox with the updated expenses
    for expense in expenses:
        expenses_listbox.insert(tk.END, f"{expense[1]} - {expense[1]} - {expense[2]} - {expense[3]} - {expense[4]}")

def clear_input_fields():
    # Clear the input fields
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Expense Tracker")

# Create and configure the input form
input_form = ttk.Frame(root, padding="10")
input_form.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Labels and entry fields for the input form

ttk.Label(input_form, text="Amount:").grid(column=0, row=1, sticky=tk.W)
amount_entry = ttk.Entry(input_form, width=15)
amount_entry.grid(column=1, row=1, sticky=tk.W)

ttk.Label(input_form, text="Category:").grid(column=0, row=2, sticky=tk.W)
category_entry = ttk.Entry(input_form, width=15)
category_entry.grid(column=1, row=2, sticky=tk.W)

ttk.Label(input_form, text="Description:").grid(column=0, row=3, sticky=tk.W)
description_entry = ttk.Entry(input_form, width=15)
description_entry.grid(column=1, row=3, sticky=tk.W)

# Submit button
submit_button = ttk.Button(input_form, text="Submit Expense", command=submit_expense)
submit_button.grid(column=1, row=4, sticky=tk.W)

# Modify and Delete buttons
modify_button = ttk.Button(input_form, text="Modify Expense", command=modify_selected_expense)
modify_button.grid(column=2, row=4, sticky=tk.W)

delete_button = ttk.Button(input_form, text="Delete Expense", command=delete_selected_expense)
delete_button.grid(column=3, row=4, sticky=tk.W)

# Create a listbox to display expenses
expenses_listbox = tk.Listbox(root, width=50, height=10)
expenses_listbox.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Populate the listbox with initial data
refresh_expense_list()

# Run the Tkinter main loop
root.mainloop()