import os

BASEDIR = os.path.dirname(__file__)
TODOLIST = os.path.join(BASEDIR, ".todolist.txt")
LOGFILE = os.path.join(BASEDIR, ".todolog.txt")

if not os.path.exists(TODOLIST):
    open(TODOLIST, "w").close()
    print("initialised todo to-do list file")

if not os.path.exists(LOGFILE):
    open(LOGFILE, "w").write("added:\nremoved:\nfinished:\nedited:")
    print("initialised todo to-do list log file")
