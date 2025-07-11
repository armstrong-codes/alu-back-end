#!/usr/bin/python3
"""
Exports all employees' TODO list progress to JSON format.
Usage:
    ./3-dictionary_of_list_of_dictionaries.py
"""
import json
import requests


def export_all_to_json():
    """Export all employees' TODO list to JSON format"""
    base_url = 'https://jsonplaceholder.typicode.com'
    
    # Get all users
    users_resp = requests.get('{}/users'.format(base_url))
    if users_resp.status_code != 200:
        return

    users = users_resp.json()

    # Get all todos
    todos_resp = requests.get('{}/todos'.format(base_url))
    if todos_resp.status_code != 200:
        return

    todos = todos_resp.json()

    # Map users by ID for quick access to username
    user_dict = {user.get('id'): user.get('username') for user in users}

    # Build the required dictionary structure
    all_tasks = {}
    for task in todos:
        user_id = task.get('userId')
        username = user_dict.get(user_id)
        
        task_entry = {
            "username": username,
            "task": task.get('title'),
            "completed": task.get('completed')
        }
        
        if str(user_id) not in all_tasks:
            all_tasks[str(user_id)] = []
        all_tasks[str(user_id)].append(task_entry)

    # Write to JSON file
    with open('todo_all_employees.json', mode='w', encoding='utf-8') as f:
        json.dump(all_tasks, f)


if __name__ == '__main__':
    export_all_to_json()
