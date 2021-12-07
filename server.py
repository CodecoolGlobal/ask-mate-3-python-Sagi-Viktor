import os
from flask import Flask, render_template, request, redirect
import data_manager
import util

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("source/html/index.html")


@app.route("/list", methods=['POST', 'GET'])
def get_list():
    question_data = data_manager.get_question_list()
    question_headers = [keys.capitalize().replace('_', ' ') for keys, values in question_data[0].items()]
    sorting = request.form.get('status')
    if sorting:
        question_data = data_manager.question_sorter(sorting)
    return render_template('source/html/list.html', question_data=question_data, question_headers=question_headers)


@app.route("/question/<question_id>", methods=['POST', 'GET'])
def display_question(question_id):
    current_question = data_manager.get_question(question_id)
    answer_data = data_manager.get_answer_list()
    if request.method == 'POST':
        return redirect(f'/question/{question_id}/new-answer')
    return render_template('source/html/display_and_add_answer.html', question_id=int(question_id),
                           answer_data=answer_data, current_question=current_question)


@app.route("/question/<question_id>/new-answer", methods=['GET', 'POST'])
def new_question(question_id):
    question_data = data_manager.import_data('questions')
    answer_data = data_manager.import_data('answers')
    if request.method == 'POST':
        data_manager.add_answer(request.form)
        return redirect(f'/question/{question_id}')
    return render_template('source/html/add_answer.html', question_id=question_id, question_data=question_data,
                           answer_data=answer_data)


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    data_manager.delete_question(question_id)
    return redirect('/list')


@app.route("/question/<question_id>/edit", methods=["GET", "POST"])
def edit_question(question_id):
    current_question = data_manager.get_current_question(question_id)
    question_data = data_manager.import_data('questions')
    if request.method == "POST":
        data_manager.submit_edited_question(request.form, current_question)
        return redirect(f"/question/{question_id}")
    return render_template("source/html/edit_question.html", question_id=question_id, current_question=current_question,
                           question_data=question_data)


@app.route("/question/<question_id>/vote_up")
def question_vote_up(question_id=None):
    question_id = question_id
    data_manager.question_voting(question_id, '+')
    return redirect('/list')


@app.route("/question/<question_id>/vote_down")
def question_vote_down(question_id=None):
    question_id = question_id
    data_manager.question_voting(question_id, '-')
    return redirect('/list')


@app.route("/answer/<answer_id>/vote_up", methods=['GET', 'POST'])
def answer_vote_up(answer_id=None):
    answer_id = answer_id
    data_manager.answer_voting(answer_id, '+')
    return redirect('/list')


@app.route("/answer/<answer_id>/vote_down")
def answer_vote_down(answer_id=None):
    answer_id = answer_id
    data_manager.answer_voting(answer_id, '-')
    return redirect('/list')


@app.route("/add-question", methods=['POST', 'GET'])
def add_question():
    if request.method == "POST":
        question_id = util.generate_id('question')
        submission_time = util.generate_submission_time()
        view_number = 0
        vote_number = 0
        title = request.form.get('question-title')
        message = request.form.get('question-message')
        image = ''
        question_data = [question_id, submission_time, view_number, vote_number, title, message, image]
        data_manager.add_question(question_data)
    return render_template('source/html/add_question.html')


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    data_manager.delete_answer(answer_id)
    return redirect('/list')

if __name__ == "__main__":
    app.run(port=5000,
            debug=True)
