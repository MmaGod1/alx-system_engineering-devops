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

    employee_id = int(sys.argv[1])
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

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
