import tkinter as tk
import json
import os

#dictionary style below:
#{task description, "complete": "True/False" }
'''
tasks = [
    {'task': "first task", 'status': "complete"}
    
]
'''
root = tk.Tk()

root.title("To-Do List")
root.geometry("900x600")

my_frame = tk.Frame(root)
my_frame.grid(row = 3, column = 0, columnspan = 3)

try:
    with open("todo_list.json" , 'r') as file:
        tasks = json.load(file)

except FileNotFoundError:
    tasks = []

except json.JSONDecodeError:
    tasks = []

'''
def printtodo():
    #Display To-Do List
    #print(clear)
    print("\n\n\n\n-----------------------------------------------------------------------------------------------")
    print("To-do List")
    print("1. add item")
    print("2. delete item")
    print("3. view tasks")
    print("0. exit")
    print("-----------------------------------------------------------------------------------------------")
    #print(clear)
'''
def view_list():
    for index, task in enumerate(tasks):
        temp_label = tk.Label(my_frame, text = f"{index + 1}. {task['task']} -------- {task['status']}").grid()    

def clear_frame():
    for widget in my_frame.winfo_children():
        widget.destroy()

def set_frame():
    label1 = tk.Label(my_frame, text = "To do List items:", font = ("Arial", 14, "bold")).grid
    view_list()



def add_task():
    temptask = input("Task: ")
    tempstatus = input("Status: ")

    newtask = {"task": temptask, "status": tempstatus}
    tasks.append(newtask)

    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent = 4)

    clear_frame()
    view_list()

def del_task():
    del_val = int(input(f"which task would you like to delete? 1 - {len(tasks)}: "))

    tasks.pop(del_val - 1)

    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent = 4)

    clear_frame()
    view_list()




#add button for adding a task to the list
add_button = tk.Button(root, text = "add task", command=add_task).grid(row = 0, column = 0)
del_button = tk.Button(root, text = "delete", command = del_task).grid(row = 1, column = 0)
view_list()


root.mainloop()




'''

def todo():
    while True:
        #file handling'
        try:
            with open("todo_list.json" , 'r') as file:
                tasks = json.load(file)

        except FileNotFoundError:
            tasks = []

        except json.JSONDecodeError:
            tasks = []
            
        printtodo()

        choice = input("\n\n\nEnter your choice (0-3)\n\n")


        if choice == '0' :
            print("Done with Todo List...") 
            break

        elif choice == '1' :
            temptask = input("Task: ")
            tempstatus = input("Status: ")

            newtask = {"task": temptask, "status": tempstatus}
            tasks.append(newtask)

            with open("todo_list.json", "w") as file:
                json.dump(tasks, file, indent = 4)
            

        elif choice == '2' :
            del_val = int(input(f"which task would you like to delete? 1 - {len(tasks)}: "))

            tasks.pop(del_val - 1)

            with open("todo_list.json", "w") as file:
                json.dump(tasks, file, indent = 4)
            



        elif choice == '3' :
            print("viewing to-do list...\n") 
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']} -------- {task['status']}")

        else:
            print("invalid input")

    
        


todo()


'''










'''
root = tk.Tk()

root.title("To-Do List")
root.geometry("900x600")


#going to be a list of dictionaries
#{task description, "complete": "True/False" }
tasks = []

def add_task():
    #temp_label = tk.Label(root, text = "task to add: ", font = ("Arial", 12)).grid(row = 1, column = 0)
    message = add_entry_box.get()
    add_entry_box.delete(0, tk.END)
    #temp_label = tk.Label(root, text = f"{len(tasks) + 1}. {message}" )
    tasks.append({"task": message, "complete": False})

    print_list(tasks)



def update():
    #temp_label = tk.Label(root, text = "task to update: ").grid(row = 1, column = 0, columnspan = 2)
    message = update_entry_box.get()
    update_entry_box.delete(0, tk.END)

    parts = message.split('. ')

    num = int(parts[0])
    message = parts[1]
    tasks[num - 1] = {"task": message, "complete": False}

    print_list(tasks)
    #temp_label = tk.Label(root, text = "retype item: ").grid(row = 1, column = 0, columnspan = 2)
    #message = entry_box.get()
    #entry_box.delete(0, tk.END)

    #tasks[int(list_num)] = tk.Label(root, text = f"{len(tasks)}. {message}")

    #print_list(tasks)


#updated this so check!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def print_list(temp_list):
    for index, task in enumerate(tasks):
        temp_label = tk.Label(root, text = f"{index + 1}. {task['task']} -------- {task['complete']}").grid()





#add button for adding a task to the list
add_button = tk.Button(root, text = "add task", command=add_task).grid(row = 0, column = 0)
update_button = tk.Button(root, text = "update", command = update).grid(row = 1, column = 0)
label1 = tk.Label(root, text = "To do List items:", font = ("Arial", 14, "bold")).grid(row = 4, column = 0, columnspan = 3)




add_entry_box = tk.Entry(root, width=20)
add_entry_box.grid(row = 0, column = 1, columnspan = 2)

update_entry_box = tk.Entry(root, width=20)
update_entry_box.grid(row = 1, column = 1, columnspan = 2)


root.mainloop()

'''