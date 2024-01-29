from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField


class addPetForm(FlaskForm):
    """Form for adding pets"""

    pet_name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")
