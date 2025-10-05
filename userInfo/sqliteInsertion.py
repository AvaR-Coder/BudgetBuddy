import sqlite3

conn = sqlite3.connect('customers.db')
cursor = conn.cursor()

cursor.execute(
 "INSERT INTO customers (firstName, lastName, email, password, balance, budget, expences) VALUES (?, ?, ?, ?, ?, ?, ?)",
 (firstName, lastName, email, password, balance, budget, expences)
)
conn.commit()
conn.close()
