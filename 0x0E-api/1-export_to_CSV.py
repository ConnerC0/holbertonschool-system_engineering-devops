#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.{}.com/users/{}".
                        format("typicode", id)).json()

    ThingstoDo = requests.get("https://jsonplaceholder.{}.com/todos?userId={}".
                              format("typicode", id)).json()

    thingsCompleted = []

    for task in ThingstoDo:
        if task.get("completed") is True:
            thingsCompleted.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(thingsCompleted), len(ThingstoDo)))
    for task in thingsCompleted:
        print("\t {}".format(task))

    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in ThingstoDo:
            writer.writerow([int(id), user.get("username"),
                            task.get("completed"), task.get("title")])
