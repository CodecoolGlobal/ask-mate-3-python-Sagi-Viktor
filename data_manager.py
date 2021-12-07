import connection as csv
import os
import time
from operator import itemgetter
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import connect_database

DIRNAME = os.path.dirname(__file__)
ANSWER_HEADERS = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'voting', 'image']
QUESTION_HEADERS = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'voting', 'image']


def export_answers(data, file=f'{DIRNAME}/data/answers.csv'):
    csv.export_data(data, ANSWER_HEADERS, file)


def export_questions(data, file=f'{DIRNAME}/data/questions.csv'):
    csv.export_data(data, QUESTION_HEADERS, file)


def import_data(file):
    """ Argument should be 'questions' or 'answers'.
        Import Dictionaries in a list, dictionary keys are the ..._HEADERS.
    """
    data = csv.import_data(f'{DIRNAME}/data/{file}.csv')
    return data


def generate_id(data):
    last_id = data[-1].get('id')
    return int(last_id) + 1


def get_unix_time():
    return round(time.time())


@connect_database.connection_handler
def get_question_list(cursor):
    cursor.execute("""
                    SELECT id, submission_time, view_number, vote_number, title, message, image
                    FROM question
                    ORDER BY id
                    """)
    return cursor.fetchall()


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
    voting = 0
    parameters = [id, submission_time, view_number, vote_number, title, message, voting, image]
    export_questions(merge_dict_data(data, parameters, QUESTION_HEADERS))


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
    voting = 0
    parameters = [id, submission_time, vote_number, question_id, message, voting, image]
    export_answers(merge_dict_data(data, parameters, ANSWER_HEADERS))


def merge_dict_data(data, parameters, header):
    """ Merge new_data and overwrite database.
    """
    new = {}
    for index, header in enumerate(header):
        new.update({header: parameters[index]})
    data.append(new)
    return data


def get_current_question(question_id):
    data = import_data('questions')
    for item in data:
        if item['id'] == str(question_id):
            current_question = data.index(item)
            return current_question


def submit_edited_question(updated_question, id):
    id = int(id)
    data = import_data('questions')
    for key, value in updated_question.items():
        data[id][key] = value
    export_questions(data)


def delete_question(id):
    id = int(id)
    data = import_data('questions')
    current_question = get_current_question(id)
    data.pop(current_question)
    export_questions(data)


def question_voting(question_id, operation):
    question_data = import_data('questions')
    new_data = {}
    for item in question_data:
        if item['id'] == question_id:
            place = question_data.index(item)
            old_number = item['vote_number']
            new_data['id'] = item['id']
            new_data['submission_time'] = item['submission_time']
            new_data['view_number'] = item['view_number']
            if operation == '+':
                new_data['vote_number'] = str(int(old_number) + 1)
            else:
                new_data['vote_number'] = str(int(old_number) - 1)
            new_data['title'] = item['title']
            new_data['message'] = item['message']
            new_data['voting'] = item['voting']
            new_data['image'] = item['image']
            question_data.remove(item)
            question_data.insert(place, new_data)
            export_questions(question_data)


def answer_voting(answer_id, operation):
    answer_data = import_data('answers')
    new_data = {}
    for item in answer_data:
        if item['id'] == answer_id:
            place = answer_data.index(item)
            old_number = item['vote_number']
            new_data['id'] = item['id']
            new_data['submission_time'] = item['submission_time']
            if operation == '+':
                new_data['vote_number'] = str(int(old_number) + 1)
            else:
                new_data['vote_number'] = str(int(old_number) - 1)
            new_data['question_id'] = item['question_id']
            new_data['message'] = item['message']
            new_data['voting'] = item['voting']
            new_data['image'] = item['image']
            answer_data.remove(item)
            answer_data.insert(place, new_data)
            export_answers(answer_data)


def view_counter(question_id, question_data):
    for item in question_data:
        if question_id == item['id']:
            place = question_data.index(item)
            item['view_number'] = str(int(item['view_number']) + 1)
            new_item = item
            question_data.remove(item)
            question_data.insert(place, new_item)
            export_questions(question_data)


#def question_sorter(sort_by, orientation='asc'):
    """ Main logic for sorting questions.
        ARGUMENTS: Arg1 == the HEADER name for sort |
        Arg2 == (optional) 'desc' if descending form needed
    """
    #data = import_data('questions')
    #foo = sorted(data, key=itemgetter(sort_by))
    #return foo


@connect_database.connection_handler
def question_sorter(cursor,sort):
    query = f"""
                SELECT id, submission_time, view_number, vote_number, title, message, image
                FROM question
                ORDER BY {sort} DESC
                """
    cursor.execute(query, {'sort':sort})
    return cursor.fetchall()

@connect_database.connection_handler
def delete_answer(cursor,id):
    query = f"""
            DELETE FROM answer
            WHERE id = {id}"""
    cursor.execute(query, {'id':id})