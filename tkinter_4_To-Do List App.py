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

root = tk.Tk()
root.title("To-do list")

frame = tk.Frame(root)
frame.pack()

listbox = tk.Listbox(frame)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame) 
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack()

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack()

root.mainloop()
