#!/usr/bin/python3

import requests
import sys


def get_employee_todo_progress(employee_id):

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee details
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    employee_name = user_response.json().get("name")

    # Get todos
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    done_tasks = [task for task in todos if task.get("completed") is True]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

