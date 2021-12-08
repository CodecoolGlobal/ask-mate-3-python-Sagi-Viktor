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


def question_sorter(sort_by):
    """ Main logic for sorting questions.
        ARGUMENTS: Arg1 == the HEADER name for sort |
        Arg2 == (optional) 'desc' if descending form needed
    """
    data = data_manager.get_question_list()
    foo = sorted(data, key=itemgetter(sort_by))
    return foo


def get_answer_ids(answer_data):
    id_list = [[row[item] for item in row if item == 'id'] for row in answer_data]
    answer_ids = [data[0] for data in id_list]
    return get_comments_by_answer_ids(answer_ids)


def get_comments_by_answer_ids(answer_ids):
    comments = [data_manager.get_comments_by_answer_id(answer_id) for answer_id in answer_ids]
    id_dict = {key: 0 for key in answer_ids}
    for item in comments:
        if len(item) == 0:
            comments.remove(item)
    for keys, values in id_dict.items():
        for item in comments:
            for data in item:
                if data['answer_id'] == keys:
                    id_dict[keys] += 1
    return id_dict
    # nr_of_comments = [number for number in id_dict.values()]
    # return nr_of_comments
