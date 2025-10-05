def connectDB():
  conn = sqlite3.connect("customers.db")
  conn.row_factory = sqlite3.Row
  return conn
