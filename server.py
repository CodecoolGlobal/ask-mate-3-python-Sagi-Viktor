from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/list")
def get_list():
    return "List"


@app.route("/question/<question_id>")
@app.route("/question/<question_id>/new-answer")
@app.route("/question/<question_id>/delete")
@app.route("/question/<question_id>/edit")
@app.route("/question/<question_id>/vote_up and /question/<question_id>/vote_down")

def get_question(question_id):
    return "Question", question_id = question_id


@app.route("/add-question")
def add_question():
    return "Add_question"


@app.route("/answer/<answer_id>/delete ")
@app.route("/answer/<answer_id>/vote_up and /answer/<answer_id>/vote_down ")
def get_answer(answer_id):
    return "Answer_id_delete", answer_id = answer_id


if __name__ == "__main__":
    app.run()
