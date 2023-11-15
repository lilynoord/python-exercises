from flask import Flask, render_template, redirect, request
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


@app.route("/adduser")
def add_user_page():
    return render_template("addUser.html")


@app.route("/adduser/submit", methods=["POST"])
def add_user_submit():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    img_url = request.form["img_url"]

    db.session.add(User(first_name=first_name, last_name=last_name, image_url=img_url))
    db.session.commit()
    return redirect("/users")
