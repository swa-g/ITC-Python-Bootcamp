import sqlite3

DB_NAME = "tracker.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY,
                        type TEXT,
                        amount REAL,
                        description TEXT
                    )""")
    conn.commit()
    conn.close()

def add_transaction(type, amount, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (type, amount, description) VALUES (?, ?, ?)",
                   (type, amount, description))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def delete_transaction(transaction_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(CASE WHEN type='Income' THEN amount ELSE -amount END) FROM transactions")
    balance = cursor.fetchone()[0]
    conn.close()
    return balance if balance else 0.0

init_db()
