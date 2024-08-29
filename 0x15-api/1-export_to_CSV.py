#!/usr/bin/python3
"""Exports to-do list data for a specific employee ID into a CSV file."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Ensure the script is called with exactly one argument
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(f"{base_url}users/{user_id}")
    user_data = user_response.json()
    username = user_data.get("username", "")

    # Fetch todos
    todos_response = requests.get(f"{base_url}todos", params={"userId": user_id})
    todos_data = todos_response.json()

    # Write data to CSV file
    with open(f"{user_id}.csv", "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos_data:
            writer.writerow([
                user_id,
                username,
                str(todo.get("completed", "False")),
                todo.get("title", "")
            ])

    print(f"Data exported to {user_id}.csv")
