#!/usr/bin/python3
"""Exports TODO list data for a given employee ID in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos).json()

    username = employee_data["name"]

    tasks = [
        {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        for task in todos_data
    ]

    with open(f"{employee_id}.json", "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file, indent=4)
