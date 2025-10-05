from flask import Flask
import sqlite3
import os

app = Flask(__name__)

def connectDB():
  conn = sqlite3.connect("customers.db")
  conn.row_factory = sqlite3.Row
  return conn

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    if request.method == "POST":
        name = request.form["username"]
    return render_template_string(form_html, name=name)

if __name__ == '__main__':
    app.run(debug=True)
