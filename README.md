## todo
A simple terminal based todo app to help keep track of tasks
Adds a log file that lets you see what you've removed and what youve finished 

## Installation

```bash
# Install with pipx (recommended)
pipx install git+https://github.com/starcrossd/todo.git

# Or with pip
pip install --user git+https://github.com/starcrossd/todo.git
```

## Uninstall Command
```bash
pipx uninstall todo
```
## How to use
```bash
#arguments only if necessary
todo <command> <argument one> 
```
 ## Commands:
    # anywhere you see "<task>" the quote marks are necessary if an argument is provided but there dosent need to be an argument
    
    h - displays commands if you forget :)
    v <option>  - When called without an option shows the todo list, when called as `todo v log` it shows what youve done with the app
    a "<task>" - add an item to the todo list
    rm "<task>" - removes an item from the todo list
    rd - if youre feeling indecisive it picks a random task for you to complete
    e "<task>" - allows you to edit a task if you got something wrong
    fin "<task>" - do this to signal that youve finished an item on your todo list

Made By Alex G
