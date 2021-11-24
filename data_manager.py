import connection as csv
import os
import time

DIRNAME = os.path.dirname(__file__)
ANSWER_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def export_answers(data, file='data/answers.csv'):
    csv.export_data(data, ANSWER_HEADERS, file)


def export_questions(data, file='data/questions.csv'):
    csv.export_data(data, QUESTION_HEADERS, file)


def import_data(file):
    """ Argument should be 'questions' or 'answers'.
        Import Dictionaries in a list, dictionary keys are the ..._HEADERS.
    """
    return csv.import_data(f'{DIRNAME}/data/{file}.csv')




def generate_id(data):
    last_id = data[-1].get('id')
    return int(last_id) + 1


def get_unix_time():
    return round(time.time())


def add_question(form):
    """ New Question main logic.
        Argument: New questions raw (form)data.
        Return: No return, questions data with the new question and the parameters are appended.
    """
    data = import_data('questions')
    id = generate_id(data)
    submission_time = get_unix_time()
    view_number = 0
    vote_number = 0
    message = form.get('message')
    title = form.get('title')
    image = form.get('image')
    parameters = [id, submission_time, view_number, vote_number, message, title, image]
    merge_dict_data(data, parameters)


def add_answer(form, question_id):
    """ New Answer main logic.
        Argument: New Answer raw (form)data.
        Return: No return, answer data with the new answer and the parameters are appended.
    """
    data = import_data('answers')
    id = generate_id(data)
    submission_time = get_unix_time()
    vote_number = 0
    message = form.get('message')
    image = form.get('image')
    parameters = [id, submission_time, vote_number, question_id, message, image]
    merge_dict_data(data, parameters)


def merge_dict_data(data, parameters):
    """ Merge new_data and overwrite database.
    """
    new = {}
    for index, header in enumerate(ANSWER_HEADERS):
        new.update({header: parameters[index]})
    data.append(new)
    export_questions(data)




def question_sorter(sort_by, orientation='asc'):
    """ Main logic for sorting questions.
        ARGUMENTS: Arg1 == the HEADER name for sort |
        Arg2 == (optional) 'desc' if descending form needed
    """
    data = import_data('questions')
    return data


def sort_by_title(data):
    pass


def sort_by_time(data):
    pass


def sort_by_message(data):
    pass


def sort_by_views(data):
    pass


def sort_by_votes(data):
    pass


def get_descend():
    pass




if __name__ == '__main__':
    # print(import_questions())
    # add_question()
    pass
