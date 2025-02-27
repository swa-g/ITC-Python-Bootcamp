import csv
import os

FILENAME = "./transactions.csv"

def save_transaction(transaction_type, amount, category):
    """ Save a transaction to CSV """
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, amount, category])

def load_transactions():
    """ Load transactions from CSV """
    if not os.path.exists(FILENAME):
        return []

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        return list(reader)