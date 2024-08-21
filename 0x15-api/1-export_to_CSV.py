#!/usr/bin/python3
"""Module to fetch data from an API to store it into csv format"""

import csv
import requests
import sys

if __name__ == '__main__':
    def getUsername(url):
        """Function to fetch username of an employee"""
        empData = {'username': "", 'id': ""}

        with requests.get(url) as response:
            data = response.json()
            empData['username'] = data.get('username')
            empData['id'] = data.get('id')
        return empData

    def csvFormater(url, empData):
        """Helper function to perpare csv lists"""
        with requests.get(url) as response:
            data = response.json()
            csvList = []
            for dt in range(len(data)):
                rowList = [
                            empData.get('id'),
                            empData.get('username'),
                            data[dt].get('completed'),
                            data[dt].get('title')
                ]
                csvList.append(rowList)
            return csvList

    id = sys.argv[1]
    empUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    todosUrl = 'https://jsonplaceholder.typicode.com/todos?userId={}'\
        .format(id)
    empData = getUsername(empUrl)
    records = csvFormater(todosUrl, empData)
    csvFile = "{}.csv".format(id)
    with open(csvFile, 'w+', newline="") as f:
        writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)
        for row in records:
            writer.writerow(row)
