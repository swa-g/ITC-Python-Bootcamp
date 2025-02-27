import tkinter as tk

class IncomeExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expense Tracker")
        self.root.geometry("600x500")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseTracker(root)
    root.mainloop()