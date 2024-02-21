from colorama import Fore

def main_menu (todo_list):
    print ("*****To-Do List Menu*****")
    print ("1. Add a new task")
    print("2. Mark a task as completed ")
    print ("3. View all tasks")
    print ("4. Quit")



def add_task (todo_list):
    task = input(Fore.GREEN + "Please add a new task: " + Fore.RESET)
    todo_list.append ({'task': task , 'completed': False})
    print (f"Task '{task}' was added successfully!")

def mark_as_completed (todo_list):
    view_tasks(todo_list)
    index = int(input (Fore.YELLOW + "Please choose the index of the task to me marked as completed: " + Fore.RESET))
    if 0<= index < len (todo_list):
        todo_list [index]["completed"] = True
        print (Fore.YELLOW + f"Task is marked as completed" + Fore.RESET)
    else:
        print (Fore.RED + "The index is invalid. Please enter a valid one." + Fore.RESET)

def view_tasks (todo_list):
    print(Fore.BLUE + "*****Tasks*****" + Fore.RESET)
    for index, task in enumerate (todo_list):
        status = "[completed]" if task['completed'] else "[ ]"
        print (f"Index {index}. {status} {task['task']}")



def todo_list_program ():
    todo_list = []

    while True:
        main_menu(todo_list)
        choice = input ("Please choose (1 - 4): ")
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            mark_as_completed(todo_list)
        elif choice == "3":
            view_tasks(todo_list)
        elif choice == "4":
            print (Fore.MAGENTA +"Exiting program. Thank you! Goodbye!" + Fore. RESET)
            break
        else:
            print (Fore.RED + "Invalid choice! Please enter a number between 1 and 4: " + Fore.RESET)

todo_list_program()