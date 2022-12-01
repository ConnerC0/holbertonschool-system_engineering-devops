#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""


import json
import requests


if __name__ == '__main__':
    user = requests.get("https://jsonplaceholder.{}.com/users/{}".
                        format("typicode", id)).json()

    json_dict = {}

    for i in user:
        ThingstoDo = requests.get("https://jsonplaceholder.{}.com/todos?userId={}".
                                format("typicode", id)).json()
        jsonTask = []
        for task in ThingstoDo:
            task_dict = {}
            task_dict["task"] = task.get('title')
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = user.get("username")
            jsonTask.append(task_dict)
        json_dict[id] = jsonTask

    with open("todo_all_employees.json", "w", encoding="UTF8",
              newline='') as file:
        file.write(json.dumps(json_dict))
