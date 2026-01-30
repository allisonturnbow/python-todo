import tkinter as tk


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
add_button = tk.Button(root, text = "add task", command=add_task)
update_button = tk.Button(root, text = "update", command = update)
label1 = tk.Label(root, text = "To do List items:", font = ("Arial", 14, "bold"))

add_button.grid(row = 0, column = 0)
update_button.grid(row = 1, column = 0)
label1.grid(row = 4, column = 0, columnspan = 3)



add_entry_box = tk.Entry(root, width=20)
add_entry_box.grid(row = 0, column = 1, columnspan = 2)

update_entry_box = tk.Entry(root, width=20)
update_entry_box.grid(row = 1, column = 1, columnspan = 2)


root.mainloop()