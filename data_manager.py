import connection as csv
import os

dirname = os.path.dirname(__file__)
ANSWER_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
QUESTION_HEADER = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'question.csv'


def export_answers(data, file='data/answer.csv'):
    csv.export_data(data, ANSWER_HEADER, file)


def export_questions(data, file='data/questions.csv'):
    csv.export_data(data, QUESTION_HEADER, file)


def import_questions(file=f'{dirname}/data/questions.csv'):
    return csv.import_data(file)


def import_answers(file='data/answer.csv'):
    return csv.import_data(file)


if __name__ == '__main__':
    print(import_questions())