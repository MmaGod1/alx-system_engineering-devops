#!/usr/bin/python3
"""Exports TODO list data for a given employee ID in JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
            )

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()
    employee_username = employee_data.get("username")

    # Prepare data to be exported
    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        })

    # Store the data in a dictionary with the USER_ID as the key
    tasks_dict = {employee_id: tasks_list}
    filename = f"{employee_id}.json"

    # Write the data to a JSON file
    with open(filename, 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)

    print(f"Data for employee {employee_id} has been exported to {filename}")
