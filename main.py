#use argparse to create a command line interface for a task tracker application
import argparse
from datetime import datetime
import sys
import json
from argparse import RawTextHelpFormatter
import os

# Check if the JSON file exists or is empty, and create it with an example task if needed
example_task = {
    "1": ["Example Task", "To-Do", "Oct 24, 2025", "10:00 AM", "Oct 24, 2025", "10:00 AM"]
}

if not os.path.exists("data.json") or os.stat("data.json").st_size == 0:
    with open("data.json", 'w') as file:
        json.dump(example_task, file, indent=2)
    print("data.json file created with an example task.")

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser(
    description="Task Tracker CLI: Manage your tasks efficiently with options to add, update, and list tasks.",
    formatter_class=RawTextHelpFormatter
)

parser.add_argument("-add", 
                    default=argparse.SUPPRESS, 
                    help="Add a new task. >>> python main.py -add 'Write documentation'\n")

parser.add_argument("-mip",
                    default=argparse.SUPPRESS,
                    help="Mark a task as 'In Progress'. >>> python main.py -mip 'task id")

parser.add_argument("-update", 
                    nargs=2,
                    default=argparse.SUPPRESS, 
                    help="Update the description of a task. >>> python main.py -update 'task id' New description'\n")

parser.add_argument("-md",
                    default=argparse.SUPPRESS, 
                    help="Mark a task as 'Done'. >>> python main.py -md 'task id'")

parser.add_argument("-list",
                    default=argparse.SUPPRESS, 
                    help="List tasks. >>> python main.py -list t|i|d|a \nUse 't' for To-Do, 'i' for In-Progress, 'd' for Done, or 'a' for All.")

parser.add_argument("-delete",
                    default=argparse.SUPPRESS,
                    help="Delete a task by its ID. >>> python main.py -delete 'task id'\n"
)

args = parser.parse_args()


def formatting():
    print("-"*149)
    print(f"|{"":^10}| {"Task Details":^64} | {"Created AT":^32} | {"Updated AT":^32} |")
    print("-"*149)
    print(f"| {"Task ID":^8} | {"Description":^32} | {"Status":^29} | {"Date":^15} | {"Time":^14} | {"Date":^15} | {"Time":^14} |") 
    print("-"*149)

def printing(status):
        
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)

        tasks = {}
        tasks.update(data)

        formatting()
        if status == "All":
            for key, values in tasks.items():
                print(f"| {key:^8} | {values[0][:29]:<32} | {values[1]:<29} | {values[2]:^15} | {values[3]:^14} | {values[4]:^15} | {values[5]:^14} |") 
        
        else:
            for key, values in tasks.items():
                if values[1] == status:
                    print(f"| {key:^8} | {values[0][:29]:<32} | {values[1]:<29} | {values[2]:^15} | {values[3]:^14} | {values[4]:^15} | {values[5]:^14} |") 
        
        print("-"*149)
    except Exception as e:
        print(f"Some exception Occured!!\n{e}\n")

#IF NO ARGUMENT IS GIVEN
if len(sys.argv) == 1:
    #learn how to prettify thiss
    parser.print_help(sys.stderr)
    sys.exit(1)

#Finding the last ID, to get the value for the new ID
try:
    with open("data.json", 'r') as file:
        data = json.load(file)
        if data:
            task_id = max(int(key) for key in data.keys()) + 1      # Get the next available task_id
        else:
            task_id = 1     # If the file is empty, start with 1

except (FileNotFoundError, json.JSONDecodeError):
    task_id = 1     #If not found, set to 1

# NEW TASK IS ADDED TO THE FILE! ✅
def append_to_file(new_task):  
    global task_id      #Using this so the funtion changes the value of global variable and don't try to find the local variable with the said name.
    tasks = {}

    with open("data.json", 'r') as file:
        data = json.load(file)
    
    tasks.update(data)       #Gets the data from the file of all the previous tasks
    tasks.update(new_task)   #Adds the new task into the file 

    with open("data.json", 'w') as file:        #Overwrites the old tasks and adds the new and old tasks together.
        json.dump(tasks, file, indent=2)


    task_id += 1

    formatting()
    for key, values in tasks.items():
        print(f"| {key:^8} | {values[0][:29]:<32} | {values[1]:<29} | {values[2]:^15} | {values[3]:^14} | {values[4]:^15} | {values[5]:^14} |") 
    print("-"*149)


def task_creation(task_desc):
    global task_id
    task = {}
    status = "To-Do"
    createdAt_date = datetime.now().strftime("%b %d, %Y")
    createdAt_time = datetime.now().strftime("%I:%M %p")
    updated_At_date = datetime.now().strftime("%b %d, %Y")
    updated_At_time = datetime.now().strftime("%I:%M %p")
    task[task_id] = [task_desc, status, createdAt_date, createdAt_time, updated_At_date, updated_At_time]
    append_to_file(task)
    print("\nTask added successfully!! 🎉")


def status_change(task_id_to_update, status): #changes the status of the task (IN-PROGRESS or DONE)
    global task_id
    try:
        if task_id_to_update.isdigit() and int(task_id_to_update) <= task_id:
            with open("data.json", 'r') as file:
                data = json.load(file)

            tasks = {}
            tasks.update(data)

            if task_id_to_update in tasks:
                tasks[task_id_to_update][1] = status
                updated_At_date = datetime.now().strftime("%b %d, %Y")
                updated_At_time = datetime.now().strftime("%I:%M %p")
                tasks[task_id_to_update][4] = updated_At_date
                tasks[task_id_to_update][5] = updated_At_time

            print(f"\nStatus updated to {status} for task ID: {task_id_to_update}")
            if status == "Done":
                print("Yayyy!!! Congrats! 🎉🎉\n")

            # Call a function that prints the table with just that updated record.
            with open("data.json", 'w') as file:        # Overwrites the old tasks and adds the new and old tasks together.
                json.dump(tasks, file, indent=2)
            
        else:
            print(f"Marking In Progress requires ID of the task. '{task_id_to_update}' is not a valid ID ")
    except Exception as e:
        print(f"Some exception Occured!!\n{e}")

def update_desc(task_id_to_change, description): 
    global task_id

    try:
        if task_id_to_change.isdigit() and int(task_id_to_change) <= task_id:
            with open("data.json", 'r') as file:
                data = json.load(file)

            tasks = {}
            tasks.update(data)

            if task_id_to_change in tasks:
                old = tasks[task_id_to_change][0]
                tasks[task_id_to_change][0] = description
                updated_At_date = datetime.now().strftime("%b %d, %Y")
                updated_At_time = datetime.now().strftime("%I:%M %p")
                tasks[task_id_to_change][4] = updated_At_date
                tasks[task_id_to_change][5] = updated_At_time

            print(f"\n Task ID : {task_id_to_change}'s, description changed from {old} to {description}\n")
            formatting()
            for key, values in tasks.items():
                if key == task_id_to_change:
                    print(f"| {key:^8} | {values[0][:29]:<32} | {values[1]:<29} | {values[2]:^15} | {values[3]:^14} | {values[4]:^15} | {values[5]:^14} |") 
            print("-"*149)

            
            with open("data.json", 'w') as file:        #Overwrites the old tasks and adds the new and old tasks together.
                json.dump(tasks, file, indent=2)
            
        else:
            print(f"Marking In Progress requires ID of the task. '{task_id_to_change}' is not a valid ID \n ")
    except Exception as e:
        print(f"Some exception Occured!!\n{e}\n")



def print_tasks(listty):
    # -list t --> for to do, i --> for In-Progress, d --> for Done, a for All.
    try:
        match listty:
            case "t":
                printing("To-Do")
            case "i":
                printing("In-Progress")
            case "d":
                printing("Done")
            case "a":
                printing("All")
            case _:
                print("Wrong input!")
    except Exception as e:
        print("Kind not specified!\n",e)



def delete_task(task_id_to_delete):
    global task_id
    try:
        # Ensure task_id_to_delete is treated as a string
        task_id_to_delete = str(task_id_to_delete)

        # Check if the provided task ID is valid
        with open("data.json", 'r') as file:
            data = json.load(file)

        tasks = {}
        tasks.update(data)

        # Check if the task ID exists in the tasks
        if task_id_to_delete in tasks:
            deleted_task = tasks.pop(task_id_to_delete)  # Remove the task
            print(f"\nTask ID {task_id_to_delete} deleted successfully! 🎉")
            print(f"Deleted Task: {deleted_task}\n")

            # Save the updated tasks back to the file
            with open("data.json", 'w') as file:
                json.dump(tasks, file, indent=2)

            # Print the updated task list
            formatting()
            for key, values in tasks.items():
                print(f"| {key:^8} | {values[0][:29]:<32} | {values[1]:<29} | {values[2]:^15} | {values[3]:^14} | {values[4]:^15} | {values[5]:^14} |")
            print("-" * 149)
        else:
            print(f"Task ID {task_id_to_delete} not found.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")

def menu():
    if hasattr(args, "add"):
        task_creation(args.add)                       # Make a function that actually makes the task thing ✅
    elif hasattr(args, "mip"):
        status_change(args.mip, "In-Progress")        # Fetch the said task and mark it in progress ✅
    elif hasattr(args, "md"):
        status_change(args.md, "Done")                # Fetch and mark done. ✅
    elif hasattr(args, "update"):
        update_desc(args.update[0], args.update[1])   # Fetch the said task and status it  ✅
    elif hasattr(args, "list"):
        print_tasks(args.list)                        # Print the list of tasks ✅
    elif hasattr(args, "delete"):
        delete_task(args.delete)                      # Delete the specified task ✅

menu()

# Format for Output
# ---------------------------------------------------------------------------------------------------
# |         |   Task Details            |       Created AT            |       Updated AT            |
# ---------------------------------------------------------------------------------------------------
# | Task ID |   Description  |  Status  | Date          |   Time      | Date          |   Time      |
# ---------------------------------------------------------------------------------------------------
# |       1 |   First Task   |  To-Do   | Oct 24, 2025  |   06:53 PM  | Oct 24, 2025  |   06:53 PM  |
# |       2 |   Second Task  |  Done    | Oct 24, 2025  |   06:58 PM  | Oct 24, 2025  |   09:00 PM  |
# |       3 |   Third Task   |  To-Do   | Oct 24, 2025  |   07:00 PM  | Oct 24, 2025  |   07:00 PM  |
# ---------------------------------------------------------------------------------------------------