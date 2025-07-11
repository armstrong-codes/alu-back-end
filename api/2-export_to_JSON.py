#!/usr/bin/python3
"""
Exports user TODO list progress to JSON format.

Usage:
    ./2-export_to_JSON.py <user_id>
"""

import json
import requests
import sys


def export_to_json(user_id):
    base_url = 'https://jsonplaceholder.typicode.com'

    user_resp = requests.get(f'{base_url}/users/{user_id}')
    if user_resp.status_code != 200:
        print(f"Error: User with id {user_id} not found.")
        return
    user = user_resp.json()
    username = user.get('username')

    todos_resp = requests.get(f'{base_url}/todos', params={'userId': user_id})
    if todos_resp.status_code != 200:
        print("Error: Could not retrieve TODO list.")
        return
    todos = todos_resp.json()

    # Prepare data in required JSON format
    data = {
        str(user_id): [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in todos
        ]
    }

    json_file = f'{user_id}.json'
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <user_id>")
        sys.exit(1)

    user_id_arg = sys.argv[1]
    if not user_id_arg.isdigit():
        print("Error: user_id must be a number.")
        sys.exit(1)

    export_to_json(user_id_arg)
