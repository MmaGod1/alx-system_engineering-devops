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

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        employee_response = requests.get(user_url)
        todos_response = requests.get(todos_url)
        employee_response.raise_for_status()
        todos_response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    employee_name = employee_data.get("name", "Unknown")

    # Write data to CSV
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            writer.writerow([
                employee_id,
                employee_name,
                str(task.get("completed", False)),
                task.get("title", "No Title")
            ])

    print(f"Data exported to {employee_id}.csv")
