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
def get_answer_list(cursor):
    cursor.execute(f"""
                    SELECT *
                    FROM answer
                    ORDER BY id""")
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
    query = f"""
    DELETE FROM question
    WHERE id ={user_id}
    """
    cursor.execute(query)


@connect_database.connection_handler
def delete_answer(cursor, id):
    query = f"""
            DELETE FROM answer
            WHERE id = {id}
            """
    cursor.execute(query, {'id': id})


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
def search_engine(cursor, phrase):
    answers = search_answers(phrase)
    questions = search_questions(phrase)

    return results


@connect_database.connection_handler
def search_answers(cursor, phrase):
    query = """
        
        """
    cursor.execute(query, )
    return cursor.fetchall()


@connect_database.connection_handler
def search_questions(cursor, phrase):
    query = """

        """
    cursor.execute(query, )
    return cursor.fetchall()


