import connection as csv
import os

DIRNAME = os.path.dirname(__file__)
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']


def export_answers(data, file='data/answers.csv'):
    csv.export_data(data, ANSWER_HEADER, file)


def export_questions(data, file='data/questions.csv'):
    csv.export_data(data, QUESTION_HEADER, file)


def import_data(file):
    return csv.import_data(f'{DIRNAME}/data/{file}.csv')



def generate_id(last_id):
    return int(last_id) + 1


def add_question(foo):
    """ New Question main logic
        Argument: New questions raw (form)data.
        Return questions data with the new question appended """
    # print(foo)
    return None









if __name__ == '__main__':
    # print(import_questions())
    pass