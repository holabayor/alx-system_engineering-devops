#!/usr/bin/python3
"""
Script that uses REST API to return info about a todo list progress
"""
import json
import requests


def export_data():
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    dict_file = {}
    for user in users:
        user_id = user.get("id")
        task_list = []
        for task in todos:
            if task.get("userId") == user_id:
                task_list.append({"username": user.get("username"),
                                  "task": task.get("title"),
                                  "completed": task.get("completed")})
        dict_file[user_id] = task_list
    filename = "todo_all_employees.json"
    with open(filename, 'w') as outfile:
        json.dump(dict_file, outfile)


if __name__ == "__main__":
    export_data()
