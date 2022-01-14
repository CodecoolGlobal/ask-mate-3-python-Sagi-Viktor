import connect_database


@connect_database.connection_handler
def get_question_list(cursor):
    query = """
        SELECT *
        FROM question
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_list(cursor):
    query = """
        SELECT *
        FROM answer
        ORDER BY id"""
    cursor.execute(query)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_list_by_question_id(cursor, question_id):
    query = """
        SELECT *
        FROM answer
        LEFT JOIN users
            ON answer.user_id = users.id
        WHERE question_id = %(question_id)s
        ORDER BY answer.id"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_message_by_answer_id(cursor, answer_id):
    query = """
        SELECT message
        FROM answer
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_question(cursor, question_id):
    query = """
        SELECT * FROM question
        LEFT JOIN users
            ON question.user_id = users.id
        WHERE question.id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_question_id(cursor, answer_id):
    query = """
        SELECT question_id
        FROM answer
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_question_id_by_comment(cursor, comment_id):
    query = """
        SELECT question_id
        FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_id_by_comment(cursor, comment_id):
    query = """
        SELECT answer_id
        FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchall()


@connect_database.connection_handler
def add_question(cursor, qdata):
    query = """
        INSERT INTO question
        (id, user_id, submission_time, view_number, vote_number, title, message, image)
        VALUES (
        %(qdata0)s,%(qdata1)s,%(qdata2)s,%(qdata3)s,
        %(qdata4)s,%(qdata5)s,%(qdata6)s,%(qdata7)s)"""
    cursor.execute(query, {'qdata0': qdata[0], 'qdata1': qdata[1], 'qdata2': qdata[2], 'qdata3': qdata[3],
                           'qdata4': qdata[4], 'qdata5': qdata[5], 'qdata6': qdata[6], 'qdata7': qdata[7]})


@connect_database.connection_handler
def vote_up_question(cursor, question_id):
    query = """
        UPDATE question
        SET vote_number = vote_number + 1
        WHERE id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def vote_down_question(cursor, question_id):
    query = """
        UPDATE question
        SET vote_number = vote_number - 1
        WHERE id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def vote_up_answer(cursor, answer_id):
    query = """
        UPDATE answer
        SET vote_number = vote_number + 1
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})


@connect_database.connection_handler
def vote_down_answer(cursor, answer_id):
    query = """
        UPDATE answer
        SET vote_number = vote_number - 1
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})


@connect_database.connection_handler
def view_counter(cursor, question_id):
    query = """
        UPDATE question
        SET view_number = view_number + 1
        WHERE id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def add_answer(cursor, adata):
    query = """
        INSERT INTO answer
        (id, user_id, submission_time, vote_number, question_id, message, image)
        VALUES (
        %(adata0)s,%(adata1)s,%(adata2)s,%(adata3)s,
        %(adata4)s,%(adata5)s,%(adata6)s"""
    cursor.execute(query, {'adata0': adata[0], 'adata1': adata[1], 'adata2': adata[2], 'adata3': adata[3],
                           'adata4': adata[4], 'adata5': adata[5], 'adata6': adata[6]})


@connect_database.connection_handler
def delete_question(cursor, question_id):
    query = """
        DELETE FROM question
        WHERE id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def delete_answer(cursor, answer_id):
    query = """
        DELETE FROM answer
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id})


@connect_database.connection_handler
def delete_answer_by_question_id(cursor, question_id):
    query = """
        DELETE FROM answer
        WHERE question_id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def delete_comments_by_question_id(cursor, question_id):
    query = """
        DELETE FROM comment
        WHERE question_id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def delete_comments_by_answer_id(cursor, answer_id):
    query = """
        DELETE FROM comment
        WHERE answer_id = %(answer_is)s"""
    cursor.execute(query, {'answer_id': answer_id})


@connect_database.connection_handler
def delete_question_tag(cursor, question_id):
    query = """
        DELETE FROM question_tag
        WHERE question_id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id})


@connect_database.connection_handler
def sort_question_asc(cursor, sort_by):
    query = f"""
        SELECT *
        FROM question
        ORDER BY {sort_by} ASC"""
    cursor.execute(query)
    return cursor.fetchall()


@connect_database.connection_handler
def sort_question_desc(cursor, sort_by):
    query = f"""
        SELECT *
        FROM question
        ORDER BY {sort_by} DESC"""
    cursor.execute(query)
    return cursor.fetchall()


@connect_database.connection_handler
def get_comments_question_id(cursor, question_id):
    query = """
        SELECT *
        FROM comment
        LEFT JOIN users
            ON comment.user_id = users.id
        WHERE question_id = %(question_id)s
        ORDER BY comment.id"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_comments_by_answer_id(cursor, answer_id):
    query = """
        SELECT id, submission_time, answer_id, message
        FROM comment
        WHERE answer_id = %(answer_id)s
        ORDER BY id"""
    cursor.execute(query, {'answer_id': answer_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_comments(cursor):
    cursor.execute("""
        SELECT * FROM comment
        ORDER BY id """)
    return cursor.fetchall()


@connect_database.connection_handler
def display_question_detail(cursor, question_id):
    query = """
        SELECT submission_time,message
        FROM comment
        WHERE question_id = %(question_id)s
        ORDER BY id"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_question_detail(cursor, question_id):
    query = """
        SELECT submission_time,message,id
        FROM comment
        WHERE question_id = %(question_id)s
        ORDER BY id"""
    cursor.execute(query, {'question_id': question_id})
    return cursor.fetchall()


@connect_database.connection_handler
def add_comment_to_question(cursor, cdata):
    query = """
        INSERT INTO comment
        (id, user_id, question_id, message, submission_time, edited_count)
        VALUES (
        %(cdata0)s,%(cdata1)s,%(cdata2)s,%(cdata3)s,
        %(cdata4)s,%(cdata5)s,%(cdata6)s"""
    cursor.execute(query, {'cdata0': cdata[0], 'cdata1': cdata[1], 'cdata2': cdata[2], 'cdata3': cdata[3],
                           'cdata4': cdata[4], 'cdata5': cdata[5]})


@connect_database.connection_handler
def add_comment_to_answer(cursor, cdata):
    query = """
        INSERT INTO comment
        (answer_id, message, submission_time)
        VALUES (
        %(cdata0)s,%(cdata1)s,%(cdata2)s)"""
    cursor.execute(query, {'cdata0': cdata[0], 'cdata1': cdata[1], 'cdata2': cdata[2]})


@connect_database.connection_handler
def delete_comment(cursor, comment_id):
    query = """
        DELETE FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})


@connect_database.connection_handler
def search_answers(cursor, phrase):
    query = """
        SELECT id, submission_time, question_id, message FROM answer
        WHERE message LIKE %(phrase)s"""
    cursor.execute(query, {'phrase': phrase})
    return cursor.fetchall()


@connect_database.connection_handler
def search_questions(cursor, phrase):
    query = """
        SELECT id, submission_time, title, message FROM question
        WHERE title LIKE %(phrase)s
            OR message LIKE %(phrase)s"""
    cursor.execute(query, {'phrase': phrase})
    return cursor.fetchall()


@connect_database.connection_handler
def get_message_for_comment(cursor, comment_id):
    query = """
        SELECT message
        FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchall()


@connect_database.connection_handler
def edit_question_comment(cursor, comment_id, message, time):
    query = """
        UPDATE comment
        SET message = %(message)s,
        submission_time = %(time)s
        WHERE id = %(comment_id)%"""
    cursor.execute(query, {'comment_id': comment_id, 'message': message, 'time': time})


@connect_database.connection_handler
def get_message_for_comment(cursor, comment_id):
    query = """
        SELECT message
        FROM comment
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_edited_comment_count(cursor, comment_id):
    query = """
        SELECT edited_count
        FROM comment
        where id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_all_edited_comment_count(cursor):
    cursor.execute("""
        SELECT edited_count
        FROM comment""")
    return cursor.fetchall()


@connect_database.connection_handler
def update_edited_comment_count(cursor, comment_id, edited_count):
    query = """
        UPDATE comment
        SET edited_count = %(edited_count)s
        WHERE id = %(comment_id)s"""
    cursor.execute(query, {'comment_id': comment_id, 'edit_count': edited_count})


@connect_database.connection_handler
def convert_comment_edit_count_to_zero(cursor):
    cursor.execute("""
        UPDATE comment
        SET edited_count = 0
        WHERE edited_count IS NULL """)


@connect_database.connection_handler
def edit_question(cursor, question_id, message):
    query = """
        UPDATE question
        SET message = %(message)s
        WHERE id = %(question_id)s"""
    cursor.execute(query, {'question_id': question_id, 'message': message})


@connect_database.connection_handler
def get_tag_list(cursor):
    cursor.execute("""
        SELECT *
        FROM tag
        ORDER BY id""")
    return cursor.fetchall()


@connect_database.connection_handler
def edit_answer(cursor, answer_id, message):
    query = """
        UPDATE answer
        SET message = %(message)s
        WHERE id = %(answer_id)s"""
    cursor.execute(query, {'answer_id': answer_id, 'message': message})


@connect_database.connection_handler
def add_user(cursor, user_data):
    query = """
        INSERT INTO users
        (id, username, password_hash, registration_date)
        VALUES (
        %(user_data0)s,%(user_data1)s,%(user_data2)s,%(user_data3)s)"""
    cursor.execute(query, {'user_data0': user_data[0], 'user_data1': user_data[1], 'user_data2': user_data[2], 'user_data3': user_data[3]})


@connect_database.connection_handler
def get_users(cursor):
    cursor.execute("""
        SELECT *
        FROM users
        ORDER BY id""")
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_questions(cursor, user_id):
    query = """
        SELECT *
        FROM question
        LEFT JOIN users
        ON question.user_id=users.id
        WHERE question.user_id = %(user_id)s"""
    cursor.execute(query, {'user_id': user_id})
    return cursor.fetchall()


@connect_database.connection_handler
def is_user_in_database(cursor, username):
    query = """
        SELECT username, password_hash 
        FROM users 
        WHERE username = %(username)s"""
    cursor.execute(query, {'username': username})
    return cursor.fetchone()


@connect_database.connection_handler
def get_current_user_id(cursor, email):
    query = """
        SELECT id
        FROM users
        WHERE username = %(email)s"""
    cursor.execute(query, {'email': email})
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_data(cursor,user_id):
    query = """
        SELECT *
        FROM users
        WHERE id = %(user_id)s"""
    cursor.execute(query, {'user_id': user_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_answers(cursor, user_id):
    query = """
        SELECT answer.submission_time, answer.vote_number, answer.message, answer.image
        FROM answer
        LEFT JOIN users
        ON answer.user_id=users.id
        WHERE answer.user_id = %(user_id)s"""
    cursor.execute(query, {'user_id': user_id})
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_comments(cursor, user_id):
    query = """
        SELECT comment.submission_time, comment.message, comment.edited_count
        FROM comment
        LEFT JOIN users
        ON comment.user_id=users.id
        WHERE comment.user_id = %(user_id)s"""
    cursor.execute(query, {'user_id': user_id})
    return cursor.fetchall()


if __name__ == "__main__":
    pass
