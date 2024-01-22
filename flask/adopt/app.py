from __future__ import print_function  # In python 2.7
import sys

from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet


app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"
connect_db(app)
with app.app_context():
    db.create_all()
testPet1 = Pet(
    name="Dot",
    species="Guinea Pig",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/George_the_amazing_guinea_pig.jpg/1200px-George_the_amazing_guinea_pig.jpg",
    age=100,
    notes="cute",
    available=True,
)
testPet2 = Pet(
    name="Dash",
    species="Lab Rat",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/1/1d/Albino_Rat.jpg",
    age=10,
    notes="cuter",
    available=True,
)
testPet3 = Pet(
    name="Orangey",
    species="House Cat",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg/1024px-Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg",
    age=43,
    notes="So soft",
    available=True,
)
testPet4 = Pet(
    name="Hungy",
    species="House Cat",
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/330px-Lion_waiting_in_Namibia.jpg",
    age=1,
    notes="Super nice, tots wont eat ur face",
    available=False,
)
db.session.add(testPet1)
db.session.add(testPet2)
db.session.add(testPet3)
db.session.add(testPet4)
db.session.commit()


@app.route("/")
def index():
    pets = Pet.query.order_by(Pet.id).all()
    print(pets, file=sys.stderr)
    return render_template("petList.html", pet=pets)
