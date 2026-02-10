import tkinter as tk
from tkinter import ttk
import json

# --- Load tasks ---
try:
    with open("todo_list.json", "r") as file:
        tasks = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    tasks = []

# --- Functions ---
def save_tasks():
    with open("todo_list.json", "w") as file:
        json.dump(tasks, file, indent=4)

def refresh_tree():
    for item in tree.get_children():
        tree.delete(item)
    for i, task in enumerate(tasks):
        tree.insert("", "end", values=(i + 1, task["task"], task["status"]))

def add_task():
    task = task_entry.get().strip()
    status = status_entry.get().strip()
    if task:
        tasks.append({"task": task, "status": status})
        save_tasks()
        refresh_tree()
        task_entry.delete(0, tk.END)
        status_entry.delete(0, tk.END)

def delete_task():
    selected = tree.selection()
    if selected:
        index = tree.index(selected[0])
        tasks.pop(index)
        save_tasks()
        refresh_tree()

def delete_all():
    tasks.clear()
    save_tasks()
    refresh_tree()

# --- GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("700x400")

# Top frame for inputs
input_frame = tk.Frame(root, pady=10)
input_frame.pack(fill="x")

tk.Label(input_frame, text="Task:").grid(row=0, column=0, padx=5)
task_entry = tk.Entry(input_frame, width=30)
task_entry.grid(row=0, column=1, padx=5)

tk.Label(input_frame, text="Status:").grid(row=0, column=2, padx=5)
status_entry = tk.Entry(input_frame, width=20)
status_entry.grid(row=0, column=3, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=4, padx=5)

delete_button = tk.Button(input_frame, text="Delete Selected", command=delete_task)
delete_button.grid(row=0, column=5, padx=5)

delete_all_button = tk.Button(input_frame, text="Delete All", command=delete_all)
delete_all_button.grid(row=0, column=6, padx=5)

# Middle frame for task list
tree_frame = tk.Frame(root)
tree_frame.pack(fill="both", expand=True, padx=10, pady=10)

columns = ("#", "Task", "Status")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(fill="both", expand=True, side="left")

# Scrollbar
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(fill="y", side="right")

# --- Initialize ---
refresh_tree()
root.mainloop()
