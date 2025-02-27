import tkinter as tk

class IncomeExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expense Tracker")
        self.root.geometry("600x500")

        # Variables
        self.transaction_type = tk.StringVar(value="Income")
        self.entry_amount = tk.StringVar()
        
        # Title
        tk.Label(root, text="Income & Expense Tracker", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Radio Buttons: Income or Expense
        frame_radio = tk.Frame(root)
        tk.Radiobutton(frame_radio, text="Income", variable=self.transaction_type, value="Income").pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(frame_radio, text="Expense", variable=self.transaction_type, value="Expense").pack(side=tk.LEFT, padx=10)
        frame_radio.pack()
        
        # Amount Entry
        tk.Label(root, text="Amount:").pack()
        tk.Entry(root, textvariable=self.entry_amount).pack()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()