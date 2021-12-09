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
    sorting_asc = request.args.get('status_asc')
    sorting_desc = request.args.get('status_desc')
    if sorting_asc:
        question_data = data_manager.sort_question_asc(sorting_asc)
    elif sorting_desc:
        question_data = data_manager.sort_question_desc(sorting_desc)
    return render_template('source/html/list.html', question_data=question_data, question_headers=question_headers)


@app.route("/question/<question_id>", methods=['POST', 'GET'])
def display_question(question_id):
    data_manager.convert_comment_edit_count_to_zero()
    data_manager.view_counter(question_id)
    current_question = data_manager.get_question(question_id)
    answer_data = data_manager.get_answer_list_by_question_id(question_id)
    answer_ids = util.get_answer_ids(answer_data)
    nr_of_comments = util.get_comments_by_answer_ids(answer_ids)
    comment_data = data_manager.get_comments_question_id(question_id)
    question_comment = request.form.get('add_comment_to_question')
    if question_comment:
        submission_time = util.generate_submission_time()
        data_manager.add_comment_to_question(submission_time, question_comment, question_id)
        return redirect(f'/question/{question_id}')
    elif request.method == 'POST':
        return redirect(f'/question/{question_id}/new-answer')
    return render_template('source/html/display_and_add_answer.html', question_id=int(question_id),
                           answer_data=answer_data, current_question=current_question, comment_data=comment_data,
                           nr_of_comments=nr_of_comments)


@app.route("/question/<question_id>/new-answer", methods=['GET', 'POST'])
def add_answer(question_id):
    question_data = data_manager.get_question_list()
    answer_data = data_manager.get_answer_list_by_question_id(question_id)
    question_id = question_id
    if request.method == 'POST':
        answer_id = util.generate_id('answer')
        submission_time = util.generate_submission_time()
        vote_number = 0
        message = request.form.get('message')
        image = request.form.get('image')
        answer_data = [answer_id, submission_time, vote_number, question_id, message, image]
        data_manager.add_answer(answer_data)
        return redirect(f'/question/{question_id}')
    return render_template('source/html/add_answer.html', question_id=question_id, question_data=question_data,
                           answer_data=answer_data, nr_of_comments=0)


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
        return redirect("/list")
    return render_template('source/html/add_question.html')


@app.route("/question/<question_id>/delete")
def delete_question(question_id):
    util.delete_question(question_id)
    return redirect('/list')


@app.route("/question/<question_id>/edit", methods=["GET", "POST"])
def edit_question(question_id):
    question_data = data_manager.get_question(question_id)
    question_title = [message['title'] for message in question_data][0]
    question_message = [message['message'] for message in question_data][0]
    if request.method == "POST":
        new_message = request.form.get('question-message')
        data_manager.edit_question(question_id, new_message)
        return redirect(f"/question/{question_id}")
    return render_template("source/html/edit_question.html", question_id=question_id, question_title=question_title,
                           question_message=question_message)


@app.route("/question/<question_id>/vote_up")
def question_vote_up(question_id=None):
    data_manager.vote_up_question(question_id)
    return redirect('/list')


@app.route("/question/<question_id>/vote_down")
def question_vote_down(question_id=None):
    data_manager.vote_down_question(question_id)
    return redirect('/list')


@app.route("/answer/<answer_id>/vote_up")
def answer_vote_up(answer_id):
    question_id_dict = data_manager.get_question_id(answer_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    data_manager.vote_up_answer(answer_id)
    return redirect(f'/question/{question_id}')


@app.route("/answer/<answer_id>/vote_down")
def answer_vote_down(answer_id):
    question_id_dict = data_manager.get_question_id(answer_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    data_manager.vote_down_answer(answer_id)
    return redirect(f'/question/{question_id}')


@app.route("/answer/<answer_id>/delete")
def delete_answer(answer_id):
    question_id_dict = data_manager.get_question_id(answer_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    data_manager.delete_answer(answer_id)
    return redirect(f'/question/{question_id}')


@app.route("/answer/<answer_id>/comments", methods=['GET', 'POST'])
def list_answer_comments(answer_id):
    answer = data_manager.get_answer_message_by_answer_id(answer_id)
    comment_data = data_manager.get_comments_by_answer_id(answer_id)
    question_id_dict = data_manager.get_question_id(answer_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    if request.method == 'POST':
        submission_time = util.generate_submission_time()
        comment_message = request.form.get('write-comment')
        comment_items = [answer_id, comment_message, submission_time]
        data_manager.add_comment_to_answer(comment_items)
        return redirect(f'/answer/{answer_id}/comments')
    return render_template("source/html/comment_to_answer.html", answer=answer, comment_data=comment_data,
                           question_id=question_id, answer_id=answer_id)


@app.route("/comments/<comment_id>/delete-answer-comment")
def delete_answer_comment(comment_id):
    answer_id_dict = data_manager.get_answer_id_by_comment(comment_id)
    answer_id = str([item['answer_id'] for item in answer_id_dict][0])
    data_manager.delete_comment(comment_id)
    return redirect(f'/answer/{answer_id}/comments')


@app.route("/question/<question_id>/new-comment")
def add_comment_to_question(question_id):
    comment_data = data_manager.get_comments_question_id(question_id)
    return render_template("source/html/add_comment_to_question.html", question_id=question_id,
                           comment_data=comment_data)


@app.route("/comments/<comment_id>/delete")
def delete_question_comment(comment_id):
    question_id_dict = data_manager.get_question_id_by_comment(comment_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    data_manager.delete_comment(comment_id)
    return redirect(f'/question/{question_id}')


@app.route("/search")
def search_in_question():
    searched_phrase = request.args.get('q')
    results = util.search_engine(searched_phrase)
    return render_template('/source/html/search_results.html', results=results)


@app.route("/comments/<comment_id>/edit",methods=['GET', 'POST'])
def edit_question_comment(comment_id):
    question_id_dict = data_manager.get_question_id_by_comment(comment_id)
    question_id = str([item['question_id'] for item in question_id_dict][0])
    comment_data = data_manager.get_comments_question_id(question_id)
    current_comment_dict = data_manager.get_message_for_comment(comment_id)
    current_comment = [item['message'] for item in current_comment_dict][0]
    if request.method == "POST":
        edition = data_manager.get_edited_comment_count(comment_id)
        new_edition = util.check_comment_edit_count(edition)
        time = util.generate_submission_time()
        new_message = request.form.get("edit_question_comment")
        data_manager.edit_question_comment(comment_id,new_message,time)
        data_manager.update_edited_comment_count(comment_id,new_edition)
        return redirect(f'/question/{question_id}')
    return render_template("/source/html/edit_question_comment.html",comment_id=comment_id, comment_data=comment_data,
                           current_comment=current_comment,question_id=question_id)

@app.route("/answer/<answer_id>/edit", methods=["GET", "POST"])
def edit_answer(answer_id):
    answer_message_dict = data_manager.get_answer_message_by_answer_id(answer_id)
    answer_message = [item['message'] for item in answer_message_dict][0]
    if request.method == "POST":
        new_answer_message = request.form.get("question-message") #which is answer message
        data_manager.edit_answer(answer_id,new_answer_message)
        question_id_dict = data_manager.get_question_id(answer_id)
        question_id = str([item['question_id'] for item in question_id_dict][0])
        return redirect(f'/question/{question_id}')
    return render_template("/source/html/edit_answer.html", answer_message=answer_message,answer_id=answer_id)


if __name__ == "__main__":
    app.run(port=5000,
            debug=True)
