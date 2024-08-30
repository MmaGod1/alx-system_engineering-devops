#!/usr/bin/python3
"""
Export TODO list data for an employee to a JSON file in JSON format.
"""

import json
import requests
import sys

# Check if the script is run with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = int(sys.argv[1])

users_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

user_data = requests.get(users_url).json()
todos_data = requests.get(todos_url).json()

employee_username = user_data.get("username")

# Prepare the list of tasks
tasks_list = [
    {
        "task": task.get("title"),
        "completed": task.get("completed"),
        "username": employee_username
    }
    for task in todos_data
]

tasks_dict = {str(employee_id): tasks_list}

filename = f"{employee_id}.json"
with open(filename, 'w') as jsonfile:
    json.dump(tasks_dict, jsonfile, indent=4)

print(f"Data for employee {employee_id} has been exported to {filename}")
