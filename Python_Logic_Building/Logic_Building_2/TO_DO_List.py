# python TO DO List
# Add Task
# View task
# mark done

import datetime

tasks = []

def add_task():
    task = input("Enter Task: ")
    tasks.append(task)
    print("Task Added! Successfully")

def view_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def mark_done():
    if not tasks:
        print("No task to mark as done")
    else:
        view_tasks()
        index = int(input("Enter task number to mark as done "))-1
        if 0<= index <len(tasks):
            del tasks[index]
            print("Task Marked as done")
        else:
            print("Invalid task number")


while True:
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4.Exit")

    choice = input("Enter your choice ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        break
    else:
        print("Invalid choice")