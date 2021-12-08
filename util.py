import data_manager
import datetime
from operator import itemgetter


def generate_id(table):
    if table == 'question':
        question_data = data_manager.get_question_list()
        numbers = [[row[item] for item in row if item == 'id'] for row in question_data]
        return numbers[-1][0] + 1
    elif table == 'answer':
        answer_data = data_manager.get_answer_list()
        numbers = [[row[item] for item in row if item == 'id'] for row in answer_data]
        return numbers[-1][0] + 1


def generate_submission_time():
    return str(datetime.datetime.now()).split('.')[0]


def question_sorter(sort_by, orientation='asc'):
    """ Main logic for sorting questions.
        ARGUMENTS: Arg1 == the HEADER name for sort |
        Arg2 == (optional) 'desc' if descending form needed
    """
    data = data_manager.get_question_list()
    foo = sorted(data, key=itemgetter(sort_by))
    return foo
