#!/usr/bin/python3
"""
Export TODO list data for an employee to a JSON file in JSON format.
"""

import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    employee_name = employee_data["name"]

    # Create a dictionary to store task data
    task_data = {str(employee_id): []}

    for task in todos_data:
        task_data[str(employee_id)].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    # Write the data to a JSON file
    with open(f"{employee_id}.json", "w") as f:
        json.dump(task_data, f, indent=4)
