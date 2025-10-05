from flask import Flask, request, render_template_string
from functions import checkPasswordStrength, hashThePassword, connectDB

app = Flask(__name__)

@app.route("/signUp", methods=["GET", "POST"])
def signUp():
  name = None
  email = None
  password = None
  balance = None
  error = None
  message = None
  
  if request.method == "POST":
    name = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    balance = request.form["balance"]

    error = checkPasswordStrength(password)
    if error is None:
      hashed_password = hashThePassword(password)
      message = "Good password"
  
  return render_template_string(form_html, name=name, email=email, balance=balance, error=error, message=message)

if __name__ == '__main__':
  app.run(debug=True)
