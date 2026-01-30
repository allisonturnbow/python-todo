import json
import os

#dictionary style below:
#{task description, "complete": "True/False" }
'''
tasks = [
    {'task': "first task", 'status': "complete"}
    
]
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







