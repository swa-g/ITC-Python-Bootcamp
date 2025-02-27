import tkinter as tk
from tkinter import ttk, messagebox
import tracker_db

class IncomeExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expense Tracker")
        self.root.geometry("600x500")

        # Variables
        self.transaction_type = tk.StringVar(value="Income")
        self.entry_amount = tk.StringVar()
        self.category = tk.StringVar()

        # Title
        tk.Label(root, text="Income & Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Radio Buttons: Income or Expense
        frame_radio = tk.Frame(root)
        tk.Radiobutton(frame_radio, text="Income", variable=self.transaction_type, value="Income", command=self.update_dropdown).pack(side=tk.LEFT, padx=10)          
        tk.Radiobutton(frame_radio, text="Expense", variable=self.transaction_type, value="Expense", command=self.update_dropdown).pack(side=tk.LEFT, padx=10)        
        frame_radio.pack()
        
        # Amount Entry
        tk.Label(root, text="Amount:").pack()
        tk.Entry(root, textvariable=self.entry_amount).pack()

        # Category Dropdown
        tk.Label(root, text="Category:").pack()
        self.dropdown = ttk.Combobox(root, textvariable=self.category, state="readonly")
        self.dropdown.pack()
        self.update_dropdown()

        # Add Button
        tk.Button(root, text="Add", command=self.add_transaction).pack(pady=10)

    def update_dropdown(self):
        """ Update dropdown options based on selection """
        categories = {
            "Income": ["Book Sales", "Salary"],
            "Expense": ["Food", "Rent"]
        }
        self.dropdown["values"] = categories[self.transaction_type.get()]
        self.category.set(categories[self.transaction_type.get()][0])

    def add_transaction(self):
        """ Adds a transaction """
        amount = self.entry_amount.get()
        category = self.category.get()
        transaction_type = self.transaction_type.get()

        if not amount.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")
            return

        tracker_db.save_transaction(transaction_type, amount, category)



# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()