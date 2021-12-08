import connect_database


@connect_database.connection_handler
def get_question_list(cursor):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_list(cursor):
    cursor.execute("""
                    SELECT *
                    FROM answer
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_question(cursor, question_id):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    WHERE id = '{question_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_question_id(cursor, answer_id):
    cursor.execute(f"""
                    SELECT question_id
                    FROM answer
                    WHERE id = '{answer_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def add_question(cursor, question_data):
    cursor.execute(f"""
                    INSERT INTO question
                    (id, submission_time, view_number, vote_number, title, message, image)
                    VALUES (
                    '{question_data[0]}',
                    '{question_data[1]}',
                    '{question_data[2]}',
                    '{question_data[3]}',
                    '{question_data[4]}',
                    '{question_data[5]}',
                    '{question_data[6]}')
                    """)


@connect_database.connection_handler
def vote_up_question(cursor, question_id):
    cursor.execute(f"""
                    UPDATE question
                    SET vote_number = vote_number + 1
                    WHERE id = '{question_id}'
                    """)


@connect_database.connection_handler
def vote_down_question(cursor, question_id):
    cursor.execute(f"""
                    UPDATE question
                    SET vote_number = vote_number - 1
                    WHERE id = '{question_id}'
                    """)


@connect_database.connection_handler
def vote_up_answer(cursor, answer_id):
    cursor.execute(f"""
                    UPDATE answer
                    SET vote_number = vote_number + 1
                    WHERE id = '{answer_id}'
                    """)


@connect_database.connection_handler
def vote_down_answer(cursor, answer_id):
    cursor.execute(f"""
                    UPDATE answer
                    SET vote_number = vote_number - 1
                    WHERE id = '{answer_id}'
                    """)


@connect_database.connection_handler
def view_counter(cursor, question_id):
    cursor.execute(f"""
                    UPDATE question
                    SET view_number = view_number + 1
                    WHERE id = '{question_id}'
                    """)


@connect_database.connection_handler
def add_answer(cursor, answer_data):
    cursor.execute(f"""
        INSERT INTO answer
        (id, submission_time, vote_number, question_id, message, image)
        VALUES (
                '{answer_data[0]}',
                '{answer_data[1]}',
                '{answer_data[2]}',
                '{answer_data[3]}',
                '{answer_data[4]}',
                '{answer_data[5]}')
        """)


@connect_database.connection_handler
def delete_question(cursor, user_id):
    cursor.execute(f"""
                    DELETE FROM question
                    WHERE id ={user_id}
                    """)


@connect_database.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute(f"""
                    DELETE FROM answer
                    WHERE id = '{answer_id}'
                    """)


@connect_database.connection_handler
def sort_question_asc(cursor, sort_by):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    ORDER BY {sort_by} ASC""")
    return cursor.fetchall()


@connect_database.connection_handler
def sort_question_desc(cursor, sort_by):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    ORDER BY {sort_by} DESC""")
    return cursor.fetchall()


@connect_database.connection_handler
def display_question_detail(cursor, question_id):
    cursor.execute(f"""
                    SELECT submission_time,message
                    FROM comment
                    WHERE question_id = {question_id}
                    ORDER BY id""")
    return cursor.fetchall()


def search_engine(phrase):
    answers = search_answers(phrase)
    questions = search_questions(phrase)
    return [questions, answers]


@connect_database.connection_handler
def search_answers(cursor, phrase):
    query = """
        SELECT id, submission_time, question_id, message FROM answer
        WHERE message LIKE %(phrase)s
        """
    cursor.execute(query, {'phrase': f"%{phrase}%"})
    return cursor.fetchall()


@connect_database.connection_handler
def search_questions(cursor, phrase):
    query = """
            SELECT id, submission_time, title, message FROM question
            WHERE title LIKE %(phrase)s
                OR message LIKE %(phrase)s
            """
    cursor.execute(query, {'phrase': f"%{phrase}%", 'phrase': f"%{phrase}%"})
    return cursor.fetchall()


# @ connect_database.connection_handler
# def get_question_by_id(cursor, question_id):
#     query = """
#         SELECT id, submission_time, title FROM question
#         WHERE id = %s
#         """
#     cursor.execute(query, (question_id,))
#     print(cursor.fetchall())
#     return cursor.fetchall()
#
#
# def get_questions_for_answers(answers):
#
#
#     return answers

