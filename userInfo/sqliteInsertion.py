import sqlite3

def insertCustomerData(name, email, password, balance, budget, expences, savings):
 try:
  conn = sqlite3.connect('customers.db')
  cursor = conn.cursor()
  cursor.execute(
   "INSERT INTO customers (name, email, password, balance, budget, expences, savings) VALUES (?, ?, ?, ?, ?, ?, ?)",
   (name, email, password, balance, budget, expences, savings)
  )
  conn.commit()
  return True
 except sqlite3.Error as e:
  print("Database error:", e):
 
 conn.close()
