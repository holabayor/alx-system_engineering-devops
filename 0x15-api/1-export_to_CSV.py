#!/usr/bin/python3
"""
Script that uses REST API to return info about a todo list progress
"""
import csv
import requests
from sys import argv


def export_data(emp_id):
    """ Function to run the script """

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(emp_id)).json()

    filename = "{}.csv".format(emp_id)
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([user.get("id"), user.get("username"),
                               task.get("completed"), task.get("title")])


if __name__ == "__main__":
    export_data(argv[1])
