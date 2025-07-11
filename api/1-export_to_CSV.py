#!/usr/bin/env python3
"""
Export user TODO list progress to CSV file.
Usage: ./1-export_to_CSV.py <user_id>
"""

import csv
import requests
import sys

def export_to_csv(user_id):
    # Base API URL
    base_url = 'https://jsonplaceholder.typicode.com'

    # Get user info
    user_resp = requests.get(f'{base_url}/users/{user_id}')
    if user_resp.status_code != 200:
        print(f"Error: User with id {user_id} not found.")
        return
    user = user_resp.json()
    username = user.get('username')

    # Get todos for user
    todos_resp = requests.get(f'{base_url}/todos', params={'userId': user_id})
    if todos_resp.status_code != 200:
        print("Error: Could not retrieve TODO list.")
        return
    todos = todos_resp.json()

    # Prepare CSV file name
    csv_file = f'{user_id}.csv'

    # Write to CSV
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    if not user_id.isdigit():
        print("Error: user_id must be a number.")
        sys.exit(1)

    export_to_csv(user_id)
