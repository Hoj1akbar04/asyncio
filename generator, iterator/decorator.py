import time
from datetime import datetime


def task_1():
    with open("file_1", "r") as file:
        while True:
            time.sleep(1)
            content = file.read(10)
            if content == "":
                break
            print(content, end="")


def task_2():
    with open("file_2", "r") as file:
        while True:
            time.sleep(1)
            content = file.read(10)
            if content == "":
                break
            print(content, end="")


def task_3():
    with open("file_3", "r") as file:
        while True:
            time.sleep(1)
            content = file.read(10)
            if content == "":
                break
            print(content, end="")


def task_4():
    with open("file_4", "r") as file:
        while True:
            time.sleep(1)
            content = file.read(10)
            if content == "":
                break
            print(content, end="")


def test():
    tasks = [task_1, task_2, task_3, task_4]
    for task in tasks:
        yield task()


if __name__ == "__main__":
    print(datetime.now().time())
    for i in test():
        print(i)

    print(datetime.now().time())