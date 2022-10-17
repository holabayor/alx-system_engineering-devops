#!/usr/bin/python3
"""
Script that uses REST API to return info about a todo list progress
"""
import json
import requests
from sys import argv


def export_data(emp_id):
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(emp_id)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                        .format(emp_id)).json()

    dict_file = {}
    task_list = []
    for task in todo:
        task_list.append({"task":  task.get("title"),
                          "completed": task.get("completed"),
                          "username": user.get("username")})
    dict_file[emp_id] = task_list
    filename = emp_id + ".json"
    with open(filename, 'w') as outfile:
        json.dump(dict_file, outfile)


if __name__ == "__main__":
    export_data(argv[1])
