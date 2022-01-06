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
    cursor.execute(f"""
                    SELECT *
                    FROM answer
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_list_by_question_id(cursor, question_id):
    cursor.execute(f"""
                    SELECT *
                    FROM answer
                    LEFT JOIN users
                        ON answer.user_id = users.id
                    WHERE question_id = '{question_id}'
                    ORDER BY answer.id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_message_by_answer_id(cursor, answer_id):
    cursor.execute(f"""
                    SELECT message
                    FROM answer
                    WHERE id = '{answer_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_question(cursor, question_id):
    cursor.execute(f"""
                    SELECT * FROM question
                    LEFT JOIN users
                        ON question.user_id = users.id
                    WHERE question.id = {question_id};
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
def get_question_id_by_comment(cursor, comment_id):
    cursor.execute(f"""
                    SELECT question_id
                    FROM comment
                    WHERE id = '{comment_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_answer_id_by_comment(cursor, comment_id):
    cursor.execute(f"""
                    SELECT answer_id
                    FROM comment
                    WHERE id = '{comment_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def add_question(cursor, question_data):
    cursor.execute(f"""
                    INSERT INTO question
                    (id, user_id, submission_time, view_number, vote_number, title, message, image)
                    VALUES (
                    '{question_data[0]}',
                    '{question_data[1]}',
                    '{question_data[2]}',
                    '{question_data[3]}',
                    '{question_data[4]}',
                    '{question_data[5]}',
                    '{question_data[6]}',
                    '{question_data[7]}')
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
        (id, user_id, submission_time, vote_number, question_id, message, image)
        VALUES (
                '{answer_data[0]}',
                '{answer_data[1]}',
                '{answer_data[2]}',
                '{answer_data[3]}',
                '{answer_data[4]}',
                '{answer_data[5]}',
                '{answer_data[6]}')
        """)


@connect_database.connection_handler
def delete_question(cursor, question_id):
    cursor.execute(f"""
                    DELETE FROM question
                    WHERE id ={question_id}
                    """)


@connect_database.connection_handler
def delete_answer(cursor, answer_id):
    cursor.execute(f"""
                    DELETE FROM answer
                    WHERE id = '{answer_id}'
                    """)


@connect_database.connection_handler
def delete_answer_by_question_id(cursor, question_id):
    cursor.execute(f"""
                    DELETE FROM answer
                    WHERE question_id = '{question_id}'
                    """)


@connect_database.connection_handler
def delete_comments_by_question_id(cursor, question_id):
    cursor.execute(f"""
                    DELETE FROM comment
                    WHERE question_id = '{question_id}'
                    """)


@connect_database.connection_handler
def delete_comments_by_answer_id(cursor, answer_id):
    cursor.execute(f"""
                    DELETE FROM comment
                    WHERE answer_id = '{answer_id}'
                    """)


@connect_database.connection_handler
def delete_question_tag(cursor, question_id):
    cursor.execute(f"""
                    DELETE FROM question_tag
                    WHERE question_id = '{question_id}'
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
def get_comments_question_id(cursor, question_id):
    cursor.execute(f"""
                    SELECT *
                    FROM comment
                    LEFT JOIN users
                        ON comment.user_id = users.id
                    WHERE question_id = {question_id}
                    ORDER BY comment.id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_comments_by_answer_id(cursor, answer_id):
    cursor.execute(f"""
                    SELECT id, submission_time, answer_id, message
                    FROM comment
                    WHERE answer_id = '{answer_id}'
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_comments(cursor):
    cursor.execute(f"""
                    SELECT * FROM comment
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def display_question_detail(cursor, question_id):
    cursor.execute(f"""
                    SELECT submission_time,message
                    FROM comment
                    WHERE question_id = {question_id}
                    ORDER BY id""")
    return cursor.fetchall()


@connect_database.connection_handler
def get_question_detail(cursor, question_id):
    cursor.execute(f"""
                    SELECT submission_time,message,id
                    FROM comment
                    WHERE question_id = {question_id}
                    ORDER BY id""")
    return cursor.fetchall()


@connect_database.connection_handler
def add_comment_to_question(cursor, comment_data):
    cursor.execute(f"""
        INSERT INTO comment
        (submission_time, message, question_id)
        VALUES ('{comment_data[0]}',
                '{comment_data[1]}',
                '{comment_data[2]}',
                '{comment_data[3]}',
                '{comment_data[4]}',
                '{comment_data[5]}',
                '{comment_data[6]}')
                """)


@connect_database.connection_handler
def add_comment_to_answer(cursor, comment_data):
    cursor.execute(f"""
                    INSERT INTO comment
                    (answer_id, message, submission_time)
                    VALUES (
                    '{comment_data[0]}',
                    '{comment_data[1]}',
                    '{comment_data[2]}')
                    """)


@connect_database.connection_handler
def delete_comment(cursor, comment_id):
    cursor.execute(f"""
                    DELETE FROM comment
                    WHERE id = '{comment_id}'
                    """)


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
    cursor.execute(query, {'phrase': f"%{phrase}%"})
    return cursor.fetchall()


@connect_database.connection_handler
def get_message_for_comment(cursor, comment_id):
    cursor.execute(f"""
                    SELECT message
                    FROM comment
                    WHERE id = {comment_id}
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def edit_question_comment(cursor, comment_id, new_message, time):
    cursor.execute(f"""
            UPDATE comment
            SET message = '{new_message}',
            submission_time = '{time}'
            WHERE id = {comment_id}""")


@connect_database.connection_handler
def get_message_for_comment(cursor, comment_id):
    cursor.execute(f"""
                    SELECT message
                    FROM comment
                    WHERE id = {comment_id}
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_edited_comment_count(cursor, comment_id):
    cursor.execute(f"""
                    SELECT edited_count
                    FROM comment
                    where id = {comment_id}
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_all_edited_comment_count(cursor):
    cursor.execute(f"""
                    SELECT edited_count
                    FROM comment
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def update_edited_comment_count(cursor, comment_id, new_edited_count):
    cursor.execute(f"""
            UPDATE comment
            SET edited_count = {new_edited_count}
            WHERE id = {comment_id}""")


@connect_database.connection_handler
def convert_comment_edit_count_to_zero(cursor):
    cursor.execute(f"""
            UPDATE comment
            SET edited_count = 0
            WHERE edited_count IS NULL """)


@connect_database.connection_handler
def edit_question(cursor, question_id, new_message):
    cursor.execute(f"""
                    UPDATE question
                    SET message = '{new_message}'
                    WHERE id = '{question_id}'
                    """)


@connect_database.connection_handler
def get_tag_list(cursor):
    cursor.execute(f"""
                    SELECT *
                    FROM tag
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def edit_answer(cursor, answer_id, message):
    cursor.execute(f"""
                    UPDATE answer
                    SET message = '{message}'
                    WHERE id = '{answer_id}'
                    """)


@connect_database.connection_handler
def add_user(cursor, user_data):
    cursor.execute(f"""
                    INSERT INTO users
                    (id, username, password_hash, registration_date)
                    VALUES (
                    '{user_data[0]}',
                    '{user_data[1]}',
                    '{user_data[2]}',
                    '{user_data[3]}')
                    """)


@connect_database.connection_handler
def get_users(cursor):
    cursor.execute(f"""
                    SELECT *
                    FROM users
                    ORDER BY id
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def add_user(cursor, user_data):
    cursor.execute(f"""
                    INSERT INTO users
                    (id, username, password_hash, registration_date)
                    VALUES (
                    '{user_data[0]}',
                    '{user_data[1]}',
                    '{user_data[2]}',
                    '{user_data[3]}')
                    """)

@connect_database.connection_handler
def get_current_user_id(cursor,username):
    cursor.execute(f"""
                    SELECT id
                    FROM users
                    WHERE username = '{username}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_data(cursor,user_id):
    cursor.execute(f"""
                    SELECT *
                    FROM users
                    WHERE id = '{user_id}'
                    """)
    return cursor.fetchall()


@connect_database.connection_handler
def get_current_user_questions(cursor,user_id):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    LEFT JOIN users
                    ON question.user_id=users.id
                    WHERE question.user_id = {user_id}
                    """);
    return cursor.fetchall()


if __name__ == "__main__":
    print(get_users())
