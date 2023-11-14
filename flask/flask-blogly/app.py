from __future__ import print_function  # In python 2.7
import sys
from flask import Flask, render_template, redirect
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
    return redirect(
        "/users",
    )


@app.route("/users")
def users_index():
    users = User.query.order_by(User.last_name, User.first_name).all()

    return render_template("users.html", users=users)
