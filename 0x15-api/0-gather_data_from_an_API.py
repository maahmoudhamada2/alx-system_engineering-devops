#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID"""

import json
import re
import requests
import sys


def fetch_data(id, flag):
    """Function to fetch data from REST API"""
    if flag == 1:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    else:
        url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(url)
    if isinstance(response.json(), dict) and flag == 1:
        return response.json().get('name')
    elif isinstance(response.json(), list) and flag == 2:
        return response.json()
    else:
        return None


def tasks_done(data):
    """Function to count both completed and total tasks"""
    counters = {'done': 0, 'total': 0}
    for record in data:
        if record.get('completed') is True:
            counters['done'] += 1
        counters['total'] += 1
    return counters


if __name__ == '__main__':
    if re.findall('^[0-9]+$', sys.argv[1]) != []:
        id = int(sys.argv[1])
    emp_name = fetch_data(id, 1)
    data = fetch_data(id, 2)
    counters = tasks_done(data)
    info = "Employee {} is done with tasks({}/{}):"\
        .format(emp_name, counters['done'], counters['total'])
    print("{}".format(info))

    for record in data:
        if record.get('completed') is True:
            print("\t {}".format(record.get('title')))
