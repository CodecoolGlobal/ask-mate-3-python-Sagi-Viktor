from flask import Flask, render_template

import connection

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("index.html")


@app.route("/list")
def get_list():
    forum_data = connection.import_questions
    return render_template("list.html", forum_data=forum_data)


@app.route("/question/<question_id>")
# @app.route("/question/<question_id>/new-answer")
# @app.route("/question/<question_id>/delete")
# @app.route("/question/<question_id>/edit")
# @app.route("/question/<question_id>/vote_up and /question/<question_id>/vote_down")
def get_question(question_id=None):
    return render_template("index.html", question_id=question_id)


@app.route("/add-question")
def add_question():
    return "Add_question"


@app.route("/answer/<answer_id>/delete ")
# @app.route("/answer/<answer_id>/vote_up and /answer/<answer_id>/vote_down ")
def get_answer(answer_id=None):
    return render_template("index.html", answer_id=answer_id)


if __name__ == "__main__":
    app.run()
