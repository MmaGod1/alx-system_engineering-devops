#!/usr/bin/python3
"""Exports to-do list data for a specific employee ID into a CSV file."""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/"
    
    user_response = requests.get(f"{base_url}users/{user_id}")
    username = user_response.json().get("username", "")

    todos_response = requests.get(f"{base_url}todos", params={"userId": user_id})
    todos = todos_response.json()

    # Write to CSV file
    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_id,
                username,
                todo.get("completed", "False"),
                todo.get("title", "")
            ])

    print(f"Data successfully exported to {user_id}.csv")
