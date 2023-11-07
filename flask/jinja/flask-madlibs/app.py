from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route("/")
def index():
    """Return questions form"""
    questions = story.prompts
    return render_template("input.html", questions=questions)


@app.route("/story")
def print_story():
    """Return the filled out story"""
    text = story.generate(request.args)

    return render_template("story.html", text=text)
