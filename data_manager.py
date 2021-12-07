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
def get_question(cursor, question_id):
    cursor.execute(f"""
                    SELECT *
                    FROM question
                    WHERE id = '{question_id}'
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


def merge_dict_data(data, parameters, header):
    """ Merge new_data and overwrite database.
    """
    new = {}
    for index, header in enumerate(header):
        new.update({header: parameters[index]})
    data.append(new)
    return data


@connect_database.connection_handler
def delete_question(cursor, user_id):
    query = f"""
    DELETE FROM question
    WHERE id ={user_id}
    """
    cursor.execute(query)


# def view_counter(question_id, question_data):
#     for item in question_data:
#         if question_id == item['id']:
#             place = question_data.index(item)
#             item['view_number'] = str(int(item['view_number']) + 1)
#             new_item = item
#             question_data.remove(item)
#             question_data.insert(place, new_item)
#             export_questions(question_data)
#
#
# def question_sorter(sort_by, orientation='asc'):
#     """ Main logic for sorting questions.
#         ARGUMENTS: Arg1 == the HEADER name for sort |
#         Arg2 == (optional) 'desc' if descending form needed
#     """
#     data = import_data('questions')
#     foo = sorted(data, key=itemgetter(sort_by))
#     return foo
