#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    users_url = base_url + "users"
    todos_url = base_url + "todos"

    users = requests.get(users_url).json()

    # Prepare data for JSON
    all_todos = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        todos = requests.get(todos_url, params={"userId": user_id}).json()

        # Collect tasks
        tasks = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]

        all_todos[user_id] = tasks

        json.dump(all_todos, jsonfile, indent=4)
