import data_manager
import datetime
import bcrypt
from operator import itemgetter


def generate_id(table):
    if table == 'question':
        question_data = data_manager.get_question_list()
        numbers = [[row[item] for item in row if item == 'id'] for row in question_data]
        if not numbers:
            return 1
        return numbers[-1][0] + 1
    elif table == 'answer':
        answer_data = data_manager.get_answer_list()
        numbers = [[row[item] for item in row if item == 'id'] for row in answer_data]
        if not numbers:
            return 1
        return numbers[-1][0] + 1
    elif table == 'users':
        users_data = data_manager.get_users()
        numbers = [[row[item] for item in row if item == 'id'] for row in users_data]
        if not numbers:
            return 1
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


def delete_question(question_id):
    answer_data = data_manager.get_answer_list_by_question_id(question_id)
    answer_id = get_answer_ids(answer_data)
    data_manager.delete_question_tag(question_id)
    data_manager.delete_comments_by_question_id(question_id)
    for ids in answer_id:
        data_manager.delete_comments_by_answer_id(ids)
    data_manager.delete_answer_by_question_id(question_id)
    data_manager.delete_question(question_id)


def get_answer_ids(answer_data):
    id_list = [[row[item] for item in row if item == 'id'] for row in answer_data]
    answer_ids = [data[0] for data in id_list]
    return answer_ids


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


def search_engine(phrase):
    answers = data_manager.search_answers(phrase)
    questions = data_manager.search_questions(phrase)
    return [questions, answers]


def check_comment_edit_count(edited_count_dict):
    edited_count = [item['edited_count'] for item in edited_count_dict][0]
    if edited_count is None:
        return 0
    else:
        return edited_count + 1


def export_registration_data(username, password):
    user_data = [generate_id('users'), username, hash_password(password), generate_submission_time()]
    return data_manager.add_user(user_data)


def hash_password(plain_text_password):
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


def check_password(email, plain_text_password):
    try:
        password = users[email]
    except KeyError:
        return False
    return verify_password(plain_text_password, password)


def login_validation(password):
    users_data = data_manager.get_users()
    hashed_password = [[row[item] for item in row if item == 'password_hash'] for row in users_data][2][0]
    is_password_valid = verify_password(password, hashed_password)
    return is_password_valid


if __name__ == "__main__":
    print(login_validation("test"))
    print(login_validation("nem test"))