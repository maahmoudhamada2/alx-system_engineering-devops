#!/usr/bin/python3
"""Script to export data in the JSON format."""

import json
import requests

if __name__ == '__main__':
    filename = 'todo_all_employees.json'
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    emp_data = response.json()

    dic = {}
    for record in emp_data:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
            .format(record.get('id'))
        response = requests.get(url)
        tasks_data = response.json()

        user_id = record.get('id')
        username = record.get('username')
        lst = []
        for elem in tasks_data:
            d = {'username': username,
                 'task': elem.get('title'),
                 'completed': elem.get('completed')}
            lst.append(d)
        dic.update({user_id: lst})

    with open(filename, 'w') as f:
        json.dump(dic, f)
