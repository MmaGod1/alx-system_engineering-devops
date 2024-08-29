#!/usr/bin/python3

"""Fetches and exports TODO list progress for a given employee ID
using data from the JSONPlaceholder API to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch employee data
    employee_response = requests.get(user_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name", "")

    # Fetch todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Write data to CSV
    with open(f"{employee
