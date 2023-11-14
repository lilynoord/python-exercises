from flask import Flask, render_template
from models import db, connect_db, User


app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"


connect_db(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("base.html")
