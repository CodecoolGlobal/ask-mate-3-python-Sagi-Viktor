# import csv
# import os


# DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
# DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
# STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


# def export_user_stories(user_stories):
#     with open(DATA_FILE_PATH, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=DATA_HEADER)
#         writer.writeheader()
#         writer.writerows(user_stories)


# def import_user_stories():
#     user_stories = []
#     with open(DATA_FILE_PATH, 'r', newline='') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             user_stories.append(row)
#     return user_stories


# # In FLask
# @app.route('/')
# @app.route('/list')
# def route_list():
#     user_stories = data_handler.import_user_stories()
#     return render_template('list.html', user_stories=user_stories)


# # HTML with Jinja

# <table class="center">
#         <tr>
#             {% if user_stories %}
#                 {% for key in user_stories[0].keys() %}
#                     <th>{{ key.replace('_', ' ').capitalize() }}</th>
#                 {% endfor %}
#             {% endif %}
#         </tr>
#         {% for user_story in user_stories %}
#             <tr>
#             {% for key, value in user_story.items() %}
#                 {% if key == 'title' %}
#                     <td><a href="/story/{{ user_story['id'] }}">{{ value }}</a></td>
#                 {% elif key == 'business_value' %}
#                     <td>{{ value }} points</td>
#                 {% elif key == 'estimation' %}
#                     <td>{{ value }}h</td>
#                 {% else %}
#                     <td>{{ value }}</td>
#                 {% endif %}
#             {% endfor %}
#             </tr>
#         {% endfor %}
#     </table>



id = 0
current_id = 30
question_data = [{'bela':5,'id':50},{'feri':10,'id':30}]

for item in question_data:
     if item['id'] == current_id:
         id = question_data.index(item)

print(id)
    