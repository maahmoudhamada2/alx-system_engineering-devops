#!/usr/bin/python3
"""Module to fetch data from an api to store it into json file"""
import json
import requests
import sys


if __name__ == '__main__':

    def getUsername(url):
        with requests.get(url) as response:
            data = response.json()
            userName = data.get('username')
        return userName

    def tasksFormater(url, userName):
        empData, tasksList = {}, []
        with requests.get(url) as response:
            data = response.json()
            for dt in range(len(data)):
                tmpDict = {
                            'task': data[dt].get('title'),
                            'completed': data[dt].get('completed'),
                            'username': userName
                }
                tasksList.append(tmpDict)
        return tasksList

    id = sys.argv[1]
    empUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todosUrl = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(id)

    empUser = getUsername(empUrl)
    empData = tasksFormater(todosUrl, empUser)
    fullData = {id: empData}
    with open("{}.json".format(id), 'w+') as f:
        json.dump(fullData, f)
