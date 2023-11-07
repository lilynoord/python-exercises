from flask import Flask, request, render_template, redirect
from surveys import surveys

app = Flask(__name__)
responses = []
print(surveys)


@app.route("/")
def show_index():
    return render_template("index.html", results=responses)


@app.route("/surveys/<survey>")
def show_survey_pages(survey):
    responses.clear()
    return redirect("/questions/" + survey + "/0")


@app.route("/questions/<survey>/<num>")
def show_survey_question(survey, num):
    if int(num) >= len(surveys[survey].questions):
        return redirect("/")
    question = surveys[survey]
    question = question.questions[int(num)]

    return render_template(
        "questions.html",
        survey=survey,
        question_number=num,
        question_text=question.question,
        choices=question.choices,
        allow_text=question.allow_text,
    )


@app.route("/answer/<survey>/<num>")
def handle_answer(survey, num):
    num = int(num) + 1
    responses.append(request.args.get("choice"))
    return redirect("/questions/" + survey + "/" + str(num))
