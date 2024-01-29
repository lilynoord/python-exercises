from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = "pet"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(
        db.Text,
        default="https://images.assetsdelivery.com/compings_v2/urfandadashov/urfandadashov1809/urfandadashov180901275.jpg",
        nullable=True,
    )
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, default=True, nullable=False)


def connect_db(app):
    db.app = app
    db.init_app(app)
