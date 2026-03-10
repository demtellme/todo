#!/usr/bin/env python3
import random
import os
import sys

BASEDIR = os.path.expanduser("~")
TODOLIST = os.path.join(BASEDIR, ".todolist.txt")

def help():
    print(""" a "<task>" - adds a task
        v - veiws what tasks need to be done
        rm "<task>" - removes a task
        rd - picks a random task for you to do if you dont know what should be done
        """)


def add(tasktoadd=None):
    if tasktoadd is None:
        tasktoadd = input("What task would you want to add to your list: ")
    open(TODOLIST, "a+").write(tasktoadd + "\n")


def remove(tasktoremove=None):
    lines = open(TODOLIST, "r").readlines()
    if tasktoremove is None:
        for i, line in enumerate(lines):
            print(f"{i}: {line}")
        indextoremove = int(input("what is the number of the line you want removed: "))
        del lines[indextoremove]
    else:
        if tasktoremove + "\n" in lines:
            lines.remove(tasktoremove + "\n")
    open(TODOLIST, "w").writelines(lines)

def view():
    items = open(TODOLIST, "r").readlines()
    for item in items:
        print(item)

def pickrandomtask():
    lines = open(TODOLIST, "r").readlines()
    randomtask = random.choice(lines)
    print(f"{randomtask} - is the random task selected")

def main():
    commands = {
        "h":help,
        "a": add,
        "rm":remove,
        "v":view,
        "rd":pickrandomtask
    }

    argumentone = ""

    command = sys.argv[1]
    if len(sys.argv) == 3:
        argumentone = sys.argv[2]

    if command in commands:
         if argumentone:
             commands[command](argumentone)
         else:
             commands[command]()
    else:
         print("Invalid command, run todo h for help")
