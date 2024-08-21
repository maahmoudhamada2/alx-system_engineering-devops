#!/usr/bin/python3
"""Module to fetch employee data from an API"""
import requests
import sys

if __name__ == "__main__":
    def fetchTasks(tasksUrl, nameUrl):
        """Helper function to fetch data from an API"""
        tasks = {'name': "", 'total': 0, 'completed': 0, 'titles': []}
        with requests.get(nameUrl) as response:
            tasks['name'] = response.json().get('name')

        with requests.get(tasksUrl) as response:
            data = response.json()
            tasks['total'] = len(data)
            for t in range(tasks['total']):
                if data[t].get('completed'):
                    tasks['completed'] += 1
                    tasks['titles'].append(data[t].get('title'))
            return tasks

    id = sys.argv[1]

    nameUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    tasksUrl = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(id)

    data = fetchTasks(tasksUrl, nameUrl)
    empData = "Employee {} is done with tasks({}/{}):"\
        .format(data.get('name'), data.get('completed'), data.get('total'))
    print("{}".format(empData))
    for task in data.get('titles'):
        print("\t {}".format(task))
