import json

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


def read_json_file(): #reads file so it can be updated
    with open("data.json", 'r') as file:
        data = json.load(file)
    return data


def write_jsonfile(x): #location that will be updated
    with open("data.json", 'w') as file:
        json.dump(x, file, indent=4)

def append(x, y, z): # x = task : y = specific task location : z = what to write inside it
    print("append ran")
    data = read_json_file()
    data[x][y].append(z)
    write_jsonfile(data)

def tasks_print(y): #Y = Type of tasks you want to display
    data = read_json_file()
    print("-------------------------\nCurrent Tasks: ")
    for item in data["tasks"][y]:
        print(f"- {item}")
    print("-------------------------")

def delete_task(task_name):
    data = read_json_file()
    removed = False
    for category in data["tasks"]:
        task_list = data["tasks"][category]
        if isinstance(task_list, list) and task_name in task_list:
            task_list.remove(task_name)
            removed = True
    if removed:
        write_jsonfile(data)
        print("Task " + RED + f"{task_name}" + RESET + " has been removed!!")
    else:
        print(f"Task {task_name} is not listed....")

def add_to_category(category, task_name):
    data = read_json_file()
    if data["tasks"][category] == [None]:
        data["tasks"][category] = [task_name]
    else:
        data["tasks"][category].append(task_name)
    write_jsonfile(data)


def update_task(task_name, where_To_Update):
    data = read_json_file()

    if task_name in data["tasks"]["all_tasks"]:
        for category in data["tasks"]:
            task_list = data["tasks"][category]
            if isinstance(task_list, list) and task_name in task_list:
                task_list.remove(task_name)

        target_list = data["tasks"][where_To_Update]
        if target_list == [None]:
            data["tasks"][where_To_Update] = [task_name]
        elif task_name not in target_list:
            target_list.append(task_name)

        write_jsonfile(data)
        print("Task " + RED + f"{task_name}" + RESET + " has been updated to " + f"{where_To_Update}" + "!!")
    else:
        print(f"Task {task_name} is not listed....")

def check_name(): #checks if the name is null
    namecheck = read_json_file()
    if namecheck["user"]["name"] is [None]: #checks if the name is null
        inputname = input("Please enter your name: ") #asks for name if null
        namecheck["user"]["name"] = inputname #updates the name to what was input
        write_jsonfile(namecheck) #writes the updated name to the json file
        return inputname #returns the name that was input
    else:
        return namecheck["user"]["name"] #returns the name if it is not null

username = check_name() 
print(f"\nHello, {username}! What are we doing today?")

while True:
    mainmenu = input("\n1. Add a task\n2. Remove task\n3. View tasks \n4. Update Task \n5. Exit\nPlease select an option: ")
    if mainmenu == "1":
        tasks_print("all_tasks")
        Addtask = input("Please enter the task you would like to add: ")
        add_to_category("all_tasks", Addtask)
        add_to_category("uncompleted", Addtask)
        tasks_print("all_tasks")
        print(GREEN + f"{Addtask}" + RESET + " has been added to the task list!")


    elif mainmenu == "2":
        data = read_json_file()
        tasks_print("all_tasks")
        Removetask = input("Please enter the task you would like to remove: ")
        delete_task(Removetask)


    elif mainmenu == "3":
        which_task = input("\nSelect whcih tasks you'd like to video: \n1. All Tasks \n2. Uncompleted Tasks \n3. Completed Tasks \n4. Pending Tasks \nEnter here ")
        if which_task == "1":
            tasks_print("all_tasks")
        elif which_task == "2":
            tasks_print("uncompleted")
        elif which_task == "3":
            tasks_print("completed")
        elif which_task == "4":
            tasks_print("pending")
        else:
            print("Please select a valid task option")
            break


    elif mainmenu == "4":
        print("View all the following tasks and select which one you'd like to update!")
        tasks_print("all_tasks")
        update_task_select = input("Select: ")
        update_menu_choose = input("Which menu would you like to move this to?\n1. Uncompleted Tasks \n2. Completed Tasks \n3. Pending Tasks\nHere: ")
        if update_menu_choose == "1":
            update_menu_choose = "uncompleted"
            update_task(update_task_select, update_menu_choose)
        elif update_menu_choose == "2":
            update_menu_choose = "completed"
            update_task(update_task_select, update_menu_choose)
        elif update_menu_choose == "3":
            update_menu_choose = "pending"
            update_task(update_task_select, update_menu_choose)


    elif mainmenu == "5":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Please select a menu option\n")
        continue
