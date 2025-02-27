import tkinter as tk
from tkinter import ttk, messagebox
import tracker_db
import tracker_logic

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

        # Table
        self.tree = ttk.Treeview(root, columns=("Type", "Amount", "Category"), show="headings", height=5)
        self.tree.heading("Type", text="Type")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")
        self.tree.pack()

        # Profit/Loss Label
        self.label_profit_loss = tk.Label(root, text="Profit/Loss: 0", font=("Arial", 12, "bold"))
        self.label_profit_loss.pack(pady=10)

        # Load existing data
        self.load_transactions()

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
        self.load_transactions()

    def load_transactions(self):
        """ Load transactions from CSV """
        self.tree.delete(*self.tree.get_children())
        transactions = tracker_db.load_transactions()
        total = tracker_logic.calculate_profit_loss(transactions)

        for t in transactions:
            self.tree.insert("", "end", values=t)

        self.label_profit_loss.config(text=f"Profit/Loss: {total}")    


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()