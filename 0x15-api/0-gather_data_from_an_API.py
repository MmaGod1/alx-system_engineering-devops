#!/usr/bin/python3

"""Fetches and displays TODO list progress for a given employee ID
using data from the JSONPlaceholder API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    )

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    employee_name = employee_data["name"]
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task["completed"]]
    completed_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks("
          f"{completed_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")
