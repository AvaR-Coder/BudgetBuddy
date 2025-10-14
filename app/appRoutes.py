from flask import Flask, request, render_template_string
from functions import checkPasswordStrength, hashThePassword, connectDB, insertCustomerData

app = Flask(__name__)

@app.route("/signUp", methods=["GET", "POST"])
def signUp():
  name = None
  email = None
  password = None
  balance = None
  error = None
  
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    balance = request.form["balance"]

    error = checkPasswordStrength(password)
    if error is None:
      hashed_password = hashThePassword(password)
      insertCustomerData(name, email, hashed_password, balance, 0, 0, 0)
  
  return render_template_string(form_html, name=name, email=email, balance=balance, error=error)



if __name__ == '__main__':
  app.run(debug=True)
