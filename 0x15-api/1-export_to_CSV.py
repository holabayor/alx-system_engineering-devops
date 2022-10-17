#!/usr/bin/python3
"""
Script that uses REST API to return info about a todo list progress
"""
import csv
import requests
from sys import argv


def extract_data(emp_id):
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(emp_id)).json()

    filename = emp_id + ".csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([user.get("id"), user.get("username"),
                               task.get("completed"), task.get("title")])


if __name__ == "__main__":
    extract_data(argv[1])
