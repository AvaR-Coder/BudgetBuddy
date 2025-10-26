pip install flask flask_sqlalchemy
from flask import Flask, render_template_string, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calendar.db"
db = SQLAlchemy(app)

# -------------------- Database Models --------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    duration = db.Column(db.Integer, default=60)  # in minutes

# -------------------- Routes --------------------

@app.route("/calendar")
def calendar():
    if "user_id" not in session:
        return redirect("/login")
    user_id = session["user_id"]
    events = Event.query.filter_by(user_id=user_id).all()
    html = """
    <h2>Your Calendar</h2>
    <ul>
    {% for e in events %}
      <li>{{e.date}} {{e.time}} — {{e.title}} 
          <a href="/delete/{{e.id}}">❌</a>
      </li>
    {% endfor %}
    </ul>
    <h3>Add Event</h3>
    <form action="/add" method="post">
      Title: <input name="title"><br>
      Date: <input type="date" name="date"><br>
      Time: <input type="time" name="time"><br>
      Duration (minutes): <input type="number" name="duration" value="60"><br>
      <button>Add Event</button>
    </form>
    <br><a href="/logout">Logout</a>
    """
    return render_template_string(html, events=events)

@app.route("/add", methods=["POST"])
def add():
    if "user_id" not in session:
        return redirect("/login")
    title = request.form["title"]
    date = request.form["date"]
    time = request.form["time"]
    duration = request.form["duration"]
    event = Event(
        user_id=session["user_id"],
        title=title,
        date=date,
        time=time,
        duration=duration
    )
    db.session.add(event)
    db.session.commit()
    return redirect("/calendar")

@app.route("/delete/<int:event_id>")
def delete(event_id):
    if "user_id" not in session:
        return redirect("/login")
    event = Event.query.get(event_id)
    if event and event.user_id == session["user_id"]:
        db.session.delete(event)
        db.session.commit()
    return redirect("/calendar")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run("localhost", 8080, debug=True)
python app.py

