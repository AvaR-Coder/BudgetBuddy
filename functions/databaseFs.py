import sqlite3

def connectDB():
  conn = sqlite3.connect("customers.db")
  conn.row_factory = sqlite3.Row
  return conn

def insertCustomerData(name, email, password, balance, budget, expences, savings):
  conn = connectDB()
  try:
    cursor = conn.cursor()
    cursor.execute(
      "INSERT INTO customers (name, email, password, balance, budget, expenses, savings) VALUES (?, ?, ?, ?, ?, ?, ?)",
      (name, email, password, balance, budget, expenses, savings)
    )
    conn.commit()
    return True
  except sqlite3.Error as e:
    return False
  finally:
    conn.close()
  
