from __future__ import print_function  # In python 2.7
import sys

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/img/49305"


class User(db.Model):
    """"""

    __tablename__ = "User"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(
        db.Text,
        nullable=False,
    )
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"


class Post(db.Model):
    __tablename__ = "Post"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))


class PostTag(db.Model):
    __tablename__ = "PostTag"
    post_id = db.Column(
        db.Integer,
        db.ForeignKey("Post.id"),
        primary_key=True,
    )
    tag_id = db.Column(
        db.Integer,
        db.ForeignKey("Tag.id"),
        primary_key=True,
    )


class Tag(db.Model):
    __tablename__ = "Tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)


def connect_db(app):
    db.app = app
    db.init_app(app)
