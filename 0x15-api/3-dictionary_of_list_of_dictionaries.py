#!/usr/bin/python3
"""Module to fetch all emp data from an api"""

import json
import requests
import sys

if __name__ == '__main__':
    def fetchEmp(url):
        """Function to fetch single employee info"""
        with requests.get(url) as response:
            data = response.json()
            empInfo = {'username': data.get('username'), 'id': data.get('id')}
        return empInfo

    def fetchTask(url, empInfo):
        """Function to fetch tasks of a single employee"""
        fullInfo, taskDict = [], {}
        with requests.get(url) as response:
            data = response.json()
            for dt in range(len(data)):
                taskDict = {
                            'username': empInfo.get('username'),
                            'task': data[dt].get('title'),
                            'completed': data[dt].get('completed')
                }
                fullInfo.append(taskDict)
            return fullInfo

    empUrl = 'https://jsonplaceholder.typicode.com/users/'
    with requests.get(empUrl) as response:
        data = response.json()
        empNumb = len(data)
        finalData = {}
        for num in range(empNumb):
            todosUrl = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
                .format(num + 1)
            singleEmpUrl = empUrl + str(num + 1)
            empInfo = fetchEmp(singleEmpUrl)
            singleEmpData = fetchTask(todosUrl, empInfo)
            finalData.update({str(empInfo.get('id')): singleEmpData})

        with open('todo_all_employees.json', 'w+') as f:
            json.dump(finalData, f)
