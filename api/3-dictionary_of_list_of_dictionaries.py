#!/usr/bin/python3
"""
Exports to-do list data of all employees to a JSON file.
"""

import json
import requests


def export_all_tasks_to_json():
    """
    Fetches all users and tasks and exports them to todo_all_employees.json
    in the format:
    {
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            ...
        ],
        ...
    }
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        user_tasks = [
            {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            for task in todos if task.get('userId') == user_id
        ]

        all_tasks[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    export_all_tasks_to_json()
