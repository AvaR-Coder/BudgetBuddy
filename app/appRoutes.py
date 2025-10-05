from flask import Flask
import sqlite3
import os

app = Flask(__name__)

def connectDB():
  conn = sqlite3.connect(DB_PATH)
  conn.row_factory = sqlite3.Row
  return conn

@app.route('/')
def helloTest():
  return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
