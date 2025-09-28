from flask import Flask

app = Flask(__name__)
app.config('TESTING') = True

@app.route('/')
def hello():
  return "Hello World"
