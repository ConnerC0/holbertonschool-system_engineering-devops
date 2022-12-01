#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""


import json
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    user = requests.get("https://jsonplaceholder.{}.com/users/{}".
                        format("typicode", id)).json()

    ThingstoDo = requests.get("https://jsonplaceholder.{}.com/todos?userId={}".
                              format("typicode", id)).json()


    jsonTask = []
    for task in ThingstoDo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user.get("username")
        jsonTask.append(task_dict)
    json_dict = {}
    json_dict[id] = jsonTask


    with open("./{}.json".format(id), "w", encoding="UTF8", newline='') as file:
        file.write(json.dumps(json_dict))
