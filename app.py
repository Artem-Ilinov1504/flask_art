from flask import Flask, render_template, request, redirect, send_file
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"  # database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)  # binding DB and Flask App


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")
@app.route("/premium")
def premium():
    return render_template("premium.html")
@app.route("/scenery")
def scenery():
    return render_template("scenery.html")
@app.route("/still_life")
def still_life():
    return render_template("still_life.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создаем таблицу в контексте приложения
    app.run(debug=True)