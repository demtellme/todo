#!/usr/bin/env python3
import random
import os
import sys

BASEDIR = os.path.dirname(__file__)
TODOLIST = os.path.join(BASEDIR, ".todolist.txt")
LOGFILE = os.path.join(BASEDIR, ".todolog.txt")

lines = open(TODOLIST, "r").readlines()

def log(item,index):
    lines = open(LOGFILE, "r+").readlines()
    lines[index] = lines[index].rstrip("\n") + f"|{item}"
    open(LOGFILE, "w").writelines(lines)



def help():
    print("""a "<task>" - adds a task
        v - veiws what tasks need to be done
        fin "<task>" - signals youve finished a task
        e "<task>" - edits a task, spelling mistake or other changes
        rm "<task>" - removes a task
        rd - picks a random task for you to do if you dont know what should be done
        """)


def add(tasktoadd=None):
    if tasktoadd is None:
        tasktoadd = input("What task would you want to add to your list: ")
    open(TODOLIST, "a+").write(tasktoadd + "\n")
    log(tasktoadd, 0)

def finished(taskthatwasfinished=None):
    if taskthatwasfinished is None:
        for i, line in enumerate(lines):
            print(f"{i}: {line}")

        indextahtwasfinished = int(input("what is the number of the line you want removed: "))

        if indextahtwasfinished < len(lines):
            log(lines[indextahtwasfinished], 2)
            del lines[indextahtwasfinished]
            print("Congrats on finishing that!")
        else:
            print("That index is out of range")
    else:
        if taskthatwasfinished + "\n" in lines:
            lines.remove(taskthatwasfinished + "\n")
            log(taskthatwasfinished, 1)
        else:
            print("Thats not a task I know")
    open(TODOLIST, "w").writelines(lines)

def remove(tasktoremove=None):
    if tasktoremove is None:
        for i, line in enumerate(lines):
            print(f"{i}: {line}")
        indextoremove = int(input("what is the number of the line you want removed: "))
        if indextoremove < len(lines):
            log(lines[indextoremove], 1)
            del lines[indextoremove]
        else:
            print("That index is out of range")

    else:
        if tasktoremove + "\n" in lines:
            lines.remove(tasktoremove + "\n")
            log(tasktoremove, 1)
    open(TODOLIST, "w").writelines(lines)

def view(option=None):
    if option is None:
        for line in lines:
            print(line)
    elif option == "log":
        loglines = open(LOGFILE, "r").readlines()
        for line in loglines:
            print(line + "\n")

        added = loglines[0].split("|")
        removed = loglines[1].split("|")
        finished = loglines[2].split("|")
        edited = loglines[3].split("|")

        print(f"\nadded: {len(added)-1}, removed: {len(removed)-1}, finished: {len(finished)-1}, edited: {len(edited)-1}")
    else:
        print(f"{option} isnt a valid view option")

def pickrandomtask():
    randomtask = random.choice(lines)
    print(f"{randomtask} - is the random task selected")

def edit(tasktoedit=None):
    if tasktoedit is None:
        for i, line in enumerate(lines):
            print(f"{i}: {line}")

        indextoedit = int(input("what is the number of the line you want removed: "))

        if indextoedit < len(lines):
            newtask = input(f"What would you like to replace number {indextoedit} with: ")
            log(lines[indextoedit], 3)
            lines[indextoedit] = newtask + "\n"
            open(TODOLIST, "w").writelines(lines)
        else:
            print("That index is out of range")
    else:
        newtask = input("What would you like to replace that task with: ") + "\n"
        if tasktoedit + "\n" not in lines:
            print(f"`{tasktoedit}` dosent exist, check spelling")
        else:
            lines[lines.index(tasktoedit + "\n")] = newtask
            log(lines[lines.index(tasktoedit + "\n")], 3)
            open(TODOLIST, "w").writelines(lines)

def main():
    commands = {
        "h":help,
        "a": add,
        "rm":remove,
        "v":view,
        "rd":pickrandomtask,
        "e":edit,
        "fin":finished
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
