#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TO DO list progress.
"""


import requests
from sys import argv


def doesstuff():
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    ThingstoDo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                              format(id)).json()

    thingsCompleted = []

    for task in ThingstoDo:
        if task.get("completed") is True:
            thingsCompleted.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(thingsCompleted), len(ThingstoDo)))
    for task in thingsCompleted:
        print("\t {}".format(task))


if __name__ == '__main__':
    doesstuff()
