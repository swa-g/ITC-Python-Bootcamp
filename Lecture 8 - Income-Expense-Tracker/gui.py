import tkinter as tk
from tkinter import ttk
from db import add_transaction, get_transactions, delete_transaction, get_balance

class ExpenseTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Income & Expense Tracker")
        self.root.geometry("500x400")

        # Balance Display
        self.balance_label = tk.Label(self.root, text=f"Balance: ${get_balance():.2f}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Amount Entry
        tk.Label(self.root, text="Amount:").pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        # Description Entry
        tk.Label(self.root, text="Description:").pack()
        self.desc_entry = tk.Entry(self.root)
        self.desc_entry.pack()

        # Type Selection
        self.type_var = tk.StringVar(value="Expense")
        tk.Radiobutton(self.root, text="Income", variable=self.type_var, value="Income").pack()
        tk.Radiobutton(self.root, text="Expense", variable=self.type_var, value="Expense").pack()

        # Add Transaction Button
        self.add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack(pady=5)

        # Transactions Listbox
        self.transaction_list = tk.Listbox(self.root, width=50, height=10)
        self.transaction_list.pack(pady=5)

        # Delete Transaction Button
        self.delete_button = tk.Button(self.root, text="Delete Selected", command=self.delete_transaction)
        self.delete_button.pack()

        self.load_transactions()

    def add_transaction(self):
        amount = self.amount_entry.get()
        desc = self.desc_entry.get()
        type = self.type_var.get()

        if amount and desc:
            add_transaction(type, float(amount), desc)
            self.transaction_list.insert(tk.END, f"{type}: ${amount} - {desc}")
            self.amount_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
            self.update_balance()

    def delete_transaction(self):
        try:
            selected_index = self.transaction_list.curselection()[0]
            transaction_id = get_transactions()[selected_index][0]
            delete_transaction(transaction_id)
            self.transaction_list.delete(selected_index)
            self.update_balance()
        except IndexError:
            pass

    def load_transactions(self):
        for transaction in get_transactions():
            self.transaction_list.insert(tk.END, f"{transaction[1]}: ${transaction[2]:.2f} - {transaction[3]}")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${get_balance():.2f}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ExpenseTracker()
    app.run()

