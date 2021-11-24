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
    data = csv.import_data(f'{DIRNAME}/data/{file}.csv')
    return data


def generate_id(last_id):
    return int(last_id) + 1


def get_unix_time():
    return round(time.time())


def add_question(form): # argumnet: ImmutableMultiDict([('message', 'How are you?')])
    """ New Question main logic.
        Argument: New questions raw (form)data.
        Return: No return, questions data with the new question and the parameters are appended.
    """
    new_question = {}
    data = import_data('questions')
    id = generate_id(data[-1].get('id'))
    submission_time = get_unix_time()
    view_number = 0
    vote_number = 0
    message = form.get('message')
    title = form.get('title')
    image = form.get('image')
    parameters = [id, submission_time, view_number, vote_number, message, title, image]
    for index, header in enumerate(QUESTION_HEADERS):
        new_question.update({header: parameters[index]})

    data.append(new_question)
    print(new_question)
    export_questions(data)

def get_current_question(question_id):
    data = import_data('questions')
    current_question = data[int(question_id)]
    return current_question

def submit_edited_question(updated_question,id):
    id = int(id)
    data = import_data('questions')
    for key,value in updated_question.items():
        data[id][key]=value
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
    add_question()
