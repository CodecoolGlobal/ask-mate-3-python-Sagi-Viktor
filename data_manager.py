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








if __name__ == '__main__':
    # print(import_questions())
    add_question('a')