#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""


import json
import requests


if __name__ == '__main__':
    userstuff = requests.get("https://jsonplaceholder.{}.com/users/".
                             format("typicode"))
    UserInformation = json.loads(userstuff.text)

    json_dict = {}

    for user in UserInformation:
        id = user['id']
        Things = requests.get("https://jsonplaceholder.{}.com/todos?userId={}".
                              format("typicode", id))
        ThingstoDostuff = json.loads(Things.text)

        jsonTask = []
        for task in ThingstoDostuff:
            task_dict = {}
            task_dict["username"] = user['username']
            task_dict["task"] = task['title']
            task_dict["completed"] = task['completed']
            jsonTask.append(task_dict)

        json_dict[id] = jsonTask

    with open("todo_all_employees.json", "w", encoding="UTF8",
              newline='') as file:
        file.write(json.dumps(json_dict))
