#!/usr/bin/python3
""" Script that uses REST API to return info about a todo list progress
"""
import requests
from sys import argv


def gather_data(emp_id):
    """
    Function to runn the script
    """

    user = requests.get("https://jsonplaceholder.typicode.com/\
                         users/{}".format(emp_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/\
                          todos?userId={}".format(emp_id)).json()
    completed_tasks = []
    for task in todos:
        if task.get("completed"):
            completed_tasks.append(task)
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(completed_tasks),
                                                          len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    gather_data(argv[1])
