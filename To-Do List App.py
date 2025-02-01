import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        del tasks[index]

    except:
        messagebox.showwarning("Warning", "Select a task to delete")

root = tk.Tk()
root.title("To-do list")

frame = tk.Frame(root)
frame.pack()

listbox = tk.Listbox(frame)  # Removed 'orient' parameter
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)  # Added scrollbar initialization
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)  # Corrected configuration
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack()

btn_add = tk.Button(root, text="Add Task", command=add_task)  # Corrected 'test' to 'text'
btn_add.pack()

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)  # Corrected 'test' to 'text'
btn_delete.pack()

root.mainloop()