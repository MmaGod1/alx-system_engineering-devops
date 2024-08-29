#!/usr/bin/python3
"""Fetches and exports TODO list progress for a given employee ID
using data from the JSONPlaceholder API and saves it in CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch user and TODOs data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    employee_data = requests.get(user_url).json()
    todos_data = requests.get(todos_url).json()

    # Extract required information
    employee_name = employee_data.get("username")

    # Create the CSV file
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        for task in todos_data:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])

    print(f"Data for employee {employee_id} has been exported to {filename}")
