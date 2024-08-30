#!/usr/bin/python3
"""
Exports TODO list data for an employee to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee and TODO data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    employee_name = employee_data.get("name")
    tasks_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name
        }
        for task in todos_data
    ]

    # Write to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump({str(employee_id): tasks_list}, jsonfile, indent=4)

    print(f"Data for employee {employee_id} has been exported to {filename}")
