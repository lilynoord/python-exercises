from __future__ import print_function  # In python 2.7
import sys

from flask import Flask, render_template, redirect, request, flash
from models import db, connect_db, Pet
from forms import addPetForm

app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "ihaveasecret"
connect_db(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index():
    pets = Pet.query.order_by(Pet.id).all()
    print(pets, file=sys.stderr)
    return render_template("petList.html", pet=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    form = addPetForm()

    if form.validate_on_submit():
        newPet = Pet(
            name=form.pet_name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data,
        )
        db.session.add(newPet)
        db.session.commit()
        flash("Pet added!")
        return redirect("/")
    else:
        return render_template("addPetForm.html", form=form)
