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
    """Export user TODO list to JSON format"""
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user information
    user_resp = requests.get('{}/users/{}'.format(base_url, user_id))
    if user_resp.status_code != 200:
        return

    user = user_resp.json()
    username = user.get('username')

    # Get user's TODO list
    todos_resp = requests.get('{}/todos'.format(base_url),
                              params={'userId': user_id})
    if todos_resp.status_code != 200:
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

    # Write to JSON file
    json_file = '{}.json'.format(user_id)
    with open(json_file, mode='w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id_arg = sys.argv[1]

    # Validate that user_id is a number
    if not user_id_arg.isdigit():
        sys.exit(1)

    export_to_json(user_id_arg)
