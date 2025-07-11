#!/usr/bin/python3
"""
Exports all employees' TODO list progress to JSON format.

Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests


def export_all_to_json():
    base_url = 'https://jsonplaceholder.typicode.com'

    users_resp = requests.get(f'{base_url}/users')
    todos_resp = requests.get(f'{base_url}/todos')

    if users_resp.status_code != 200 or todos_resp.status_code != 200:
        print("Error: Failed to retrieve users or todos.")
        return

    users = users_resp.json()
    todos = todos_resp.json()

    # Map users by ID for quick access to username
    user_dict = {user['id']: user['username'] for user in users}

    # Build the required dictionary structure
    all_tasks = {}
    for task in todos:
        user_id = task['userId']
        task_entry = {
            "username": user_dict[user_id],
            "task": task['title'],
            "completed": task['completed']
        }
        if str(user_id) not in all_tasks:
            all_tasks[str(user_id)] = []
        all_tasks[str(user_id)].append(task_entry)

    with open('todo_all_employees.json', mode='w', encoding='utf-8') as f:
        json.dump(all_tasks, f)


if __name__ == '__main__':
    export_all_to_json()
